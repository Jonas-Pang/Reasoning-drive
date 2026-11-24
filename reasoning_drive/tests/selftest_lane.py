"""Self-test of the lane-level task (called by selftest.py): labels, prompts, rule table, scoring, mock runs, the
request format against the fake API (also streamed), the demo page (thinking window, uploaded photo, batch log), the named experiment, dataset suggestions, merging and agreement."""
from __future__ import annotations

import base64
import json
import shutil
import time
from pathlib import Path

import cv2
import numpy as np

from .. import paths as P

# (region, left: color, pattern, near, curb, role | right: ... | markings | lane_count, ego_index)
LANES = [
    ("US", ("yellow", "double_solid", "", "no", "center_line"), ("white", "dashed", "", "no", "lane_line"), "arrow:left;text:only", 2, 1),
    ("US", ("white", "dashed", "", "no", "lane_line"), ("white", "solid", "", "no", "edge_line"), "arrow:straight_right", 2, 2),
    ("US", ("white", "solid", "", "no", "lane_line"), ("white", "dashed", "", "no", "lane_line"), "", 3, 2),
    ("US", ("yellow", "solid_dashed", "dashed", "no", "center_line"), ("none", "none", "", "yes", "edge_line"), "area:two_way_left_turn_lane", 1, 1),
    ("CN", ("yellow", "solid", "", "no", "center_line"), ("white", "solid", "", "no", "lane_line"), "arrow:left;area:left_turn_waiting", 3, 1),
    ("CN", ("white", "dashed", "", "no", "lane_line"), ("white", "dotted", "", "no", "lane_line"), "no_turn:u_turn;arrow:straight", 3, 2),
]


def build_lane_labels(repo: Path, ws: Path) -> list[dict]:
    """Synthetic images and final lane labels in the self-test workspace (set st_lanes)."""
    from ..labeling.lanes import LANE_COLUMNS, lane_prefill, load_lane_rules, load_lane_schema
    from ..labeling.core import write_csv
    schema, table = load_lane_schema(repo), load_lane_rules(repo)
    (ws / "selected" / "st_lanes").mkdir(parents=True, exist_ok=True)
    rows = []
    for i, (region, left, right, marks, n, k) in enumerate(LANES):
        img = np.full((360, 640, 3), 70, np.uint8)
        cv2.line(img, (150, 359), (300, 200), (0, 200, 230) if left[0] == "yellow" else (230, 230, 230), 6)
        cv2.line(img, (500, 359), (350, 200), (230, 230, 230), 6)
        rel = f"selected/st_lanes/lane{i:02d}.jpg"
        cv2.imwrite(str(ws / rel), img)
        row = {c: "" for c in LANE_COLUMNS}
        row.update({"image_id": f"st_lanes__lane{i:02d}", "region": region, "dataset": "synthetic", "source_path": rel,
                    "split": "dev" if i % 2 == 0 else "test", "width": 640, "height": 360, "lane_count": n, "ego_index": k,
                    "scene_evidence": "full", "markings": marks, "markings_evidence": "full",
                    "lane_status": "done", "final_source": "agreed"})
        for side, (col, pat, near, curb, role) in (("left", left), ("right", right)):
            row.update({f"{side}_color": col, f"{side}_pattern": pat, f"{side}_near_line": near or "not_applicable",
                        f"{side}_curb": curb, f"{side}_role": role, f"{side}_evidence": "full"})
        sug = lane_prefill(table, schema, region, row)
        for a, v in sug["actions"].items():
            row["act_" + a] = v or "not_determined"
        row["accepted_rule_ids"] = ";".join(sug["rule_ids"])
        rows.append(row)
    extra = dict(rows[0], image_id="st_lanes__lane99", lane_status="waiting")
    lab = P.collection_dir(repo, "selftest")
    write_csv(lab / "st_lanes.lanes.csv", rows + [extra], LANE_COLUMNS)
    (lab / "st_lanes.set.json").write_text("{}", encoding="utf-8")
    return rows


def perfect_answer(label: dict, test: str) -> dict:
    from ..evaluation.lane_scoring import ACTIONS

    def side(s):
        return {"observation": "seen", "color": label[f"{s}_color"], "pattern": label[f"{s}_pattern"],
                "near_line": label[f"{s}_near_line"] or "not_applicable", "curb": label[f"{s}_curb"], "role": label[f"{s}_role"],
                "evidence": label[f"{s}_evidence"]}
    ids = [i for i in label.get("accepted_rule_ids", "").split(";") if i]
    return {"scene": "test", "lane_count": int(label["lane_count"]), "ego_lane_index": int(label["ego_index"]), "scene_evidence": "full",
            "left_boundary": side("left"), "right_boundary": side("right"),
            "lane_markings": [{"observation": "seen", "marking": t, "evidence": "full"} for t in label["markings"].split(";") if t],
            "cross_check": {"position": "ok", "roles": "ok", "markings": "ok", "unseen": "none", "result": "consistent"},
            "element_rules": [{"element": "left_boundary", "rule_id": ids[0] if (ids and test == "B") else None, "meaning": "m"}],
            "action_reasons": {a: "r" for a in ACTIONS}, "decision_check": "consistent",
            "actions": {a: label["act_" + a] for a in ACTIONS}, "advice": "stay"}


def run_checks(cfg: dict, repo: Path, ws: Path, check, strict_ok, FakeApi) -> None:  # noqa: N803
    from .. import config as C
    from ..agent import lane as L
    from ..evaluation.lane_scoring import compare_lane, consistency_issues, paired_difference, score_lane
    from ..labeling.lanes import (LaneAnnotationStore, LaneStore, adjudicate_lane, annotation_row, bdd_lines, contested_lane_actions,
                                  ego_boundaries, lane_agreement, lane_annotations_csv, lane_prefill, lanes_csv, load_lane_rules,
                                  load_lane_schema, merge_lanes, validate_lane)
    from ..labeling.core import Paths, Trip

    rows = build_lane_labels(repo, ws)
    schema, table = load_lane_schema(repo), load_lane_rules(repo)

    # labels and the rule table
    us, cn = L.load_lane_items(cfg, "US", "any"), L.load_lane_items(cfg, "CN", "any")
    check("lane: final lane labels loaded per region (waiting rows left out), split filter",
          len(us) == 4 and len(cn) == 2 and len(L.load_lane_items(cfg, "US", "dev")) == 2, f"{len(us)} {len(cn)}")
    r0, r1, r2, r3, r4, r5 = rows
    check("lane rule table: US solid white lane line allowed (contested), edge line prohibited (contested), double yellow prohibited",
          r2["act_change_left"] == "allowed" and "change_left" in contested_lane_actions(table, schema, "US", r2)
          and r1["act_change_right"] == "prohibited" and "change_right" in contested_lane_actions(table, schema, "US", r1)
          and r0["act_change_left"] == "prohibited", f"{r2['act_change_left']} {r1['act_change_right']}")
    check("lane rule table: arrows allow what they show; curb prohibits; TWLTL next to my lane may be entered; China waiting area, no-U-turn marking",
          r0["act_turn_left"] == "allowed" and r0["act_go_straight"] == "prohibited" and r1["act_turn_right"] == "allowed"
          and r2["act_go_straight"] == "not_applicable" and r3["act_change_right"] == "prohibited" and r3["act_enter_waiting_area"] == "allowed"
          and r4["act_enter_waiting_area"] == "allowed" and r4["act_change_right"] == "prohibited" and r5["act_u_turn"] == "prohibited"
          and r5["act_go_straight"] == "allowed" and r5["act_change_right"] == "allowed",
          json.dumps({k: v for k, v in r5.items() if k.startswith("act_")}))
    part = dict(r0, left_evidence="partial", markings_evidence="partial")
    pp = lane_prefill(table, schema, "US", part)["actions"]
    check("lane rule table: partial evidence turns decided values into not_determined",
          pp["change_left"] == "not_determined" and pp["turn_left"] == "not_determined" and pp["change_right"] == "allowed")
    errs, warns = validate_lane(dict(r0, left_pattern="solid_dashed", left_near_line="not_applicable", ego_index="3", markings="arrow:sideways"), schema)
    e2, w2 = validate_lane(r0, schema, {p["rule_id"] for p in L.lane_passages(L.lane_cfg(cfg), "US")})
    check("lane label check: missing near line, position beyond the count, unknown marking; a clean label passes",
          len(errs) >= 3 and not e2, f"{errs} / {e2} {w2}")

    # prompts
    lc = L.lane_cfg(cfg)
    a, b = L.lane_prompt_parts(lc, "A", "US"), L.lane_prompt_parts(lc, "B", "US")
    us_ids = [p["rule_id"] for p in L.lane_passages(lc, "US")]
    cn_ids = [p["rule_id"] for p in L.lane_passages(lc, "CN")]
    check("lane prompt: Test A has no passages; Test B has every US lane passage (both files) and no CN one",
          "RULE PASSAGES" not in a["instructions"] and all(f"[{i}]" in b["instructions"] for i in us_ids)
          and not any(f"[{i}]" in b["instructions"] for i in cn_ids) and any(i.startswith("US-3B.21") for i in us_ids)
          and "US-3B.01-04" in us_ids)
    check("lane prompt: A and B share skeleton, schema and user text; slots filled; strict schema; driving side named",
          a["hashes"]["shared_parts"] == b["hashes"]["shared_parts"] and a["schema"] == b["schema"] and a["user_text"] == b["user_text"]
          and "{RULES_STEP}" not in a["instructions"] + b["instructions"] and "{CITATION}" not in a["instructions"] + b["instructions"]
          and strict_ok(a["schema"]) and "keeps to the right" in a["user_text"])
    order = list(a["schema"]["properties"])
    check("lane prompt: observations, cross-check, rules and reasons come before the actions; advice last",
          order.index("left_boundary") < order.index("cross_check") < order.index("element_rules") < order.index("action_reasons")
          < order.index("decision_check") < order.index("actions") < order.index("advice"), str(order))
    left = dict(cfg)
    left["regions"] = dict(cfg["regions"], US=dict(cfg["regions"]["US"], driving_side="left"))
    check("lane prompt: a left-hand-traffic region says so", "keeps to the left" in L.lane_user_text(L.lane_cfg(left), "US"))
    cc = L.lane_prompt_parts(lc, "C", "US")
    check("lane prompt, control Test C: the words of Test B with the other region's passages (under their own title) instead of the region's",
          cc["rules_region"] == "CN" and all(f"[{i}]" in cc["instructions"] for i in cn_ids) and not any(f"[{i}]" in cc["instructions"] for i in us_ids)
          and cc["instructions"].split("RULE PASSAGES")[0] == b["instructions"].split("RULE PASSAGES")[0]
          and cc["hashes"]["shared_parts"] == b["hashes"]["shared_parts"] and cc["user_text"] == b["user_text"], cc["rules_region"])
    it = us[0]
    img = cv2.imdecode(np.frombuffer(L.plain_jpeg(it, lc), np.uint8), cv2.IMREAD_COLOR)
    orig = cv2.imread(str(it.path))
    check("lane image: sent without any box (same size, pixels unchanged apart from JPEG)",
          img.shape == orig.shape and float(np.abs(img.astype(int) - orig.astype(int)).mean()) < 3)

    # scoring
    lab = {k: r0.get(k, "") for k in L.LABEL_KEYS}
    rid = set(us_ids)
    good = score_lane(perfect_answer(lab, "B"), lab, "B", rid, contested_lane_actions(table, schema, "US", lab), schema)
    bad_ans = perfect_answer(lab, "B")
    bad_ans["lane_markings"].append({"observation": "x", "marking": "arrow:straight", "evidence": "full"})
    bad_ans["actions"]["change_left"] = "allowed"
    bad_ans["element_rules"][0]["rule_id"] = "US-9Z.99"
    bad = score_lane(bad_ans, lab, "B", rid, set(), schema)
    check("lane scoring: perfect answer; an added marking, an unsafe lane change and a made-up citation are caught",
          good["lane"] and good["output2"] and good["citation"] == "accepted" and not good["consistency"]
          and bad["lane"] is False and bad["markings"]["added"] == ["arrow:straight"] and bad["unsafe"] == ["change_left"]
          and bad["citation"] == "unlisted" and bad["output2"] is False, f"{good} / {bad}")
    odd = perfect_answer(dict(lab, right_curb="yes"), "A")
    odd["actions"]["change_right"] = "allowed"
    odd["actions"]["go_straight"] = "allowed"
    issues = consistency_issues(odd, schema)
    check("lane consistency check (no label): crossing a curb, a movement no arrow shows",
          any("curb" in i for i in issues) and any("go_straight allowed" in i for i in issues), str(issues))
    odd2 = perfect_answer(lab, "A")
    odd2["left_boundary"].update(pattern="dashed", role="lane_line", curb="no", evidence="full", color="white")
    odd2["right_boundary"].update(pattern="solid_dashed", near_line="solid", curb="no", evidence="full")
    odd2["actions"].update(change_left="prohibited", change_right="allowed")
    odd3 = perfect_answer(lab, "A")
    odd3["right_boundary"]["evidence"] = "insufficient"
    odd3["actions"]["change_right"] = "prohibited"
    i2, i3 = consistency_issues(odd2, schema), consistency_issues(odd3, schema)
    check("lane consistency check: a broken lane line not crossed, the solid side of a solid-and-broken pair crossed, a side that cannot be seen decided",
          any("broken lane line" in i for i in i2) and any("solid line of a solid-and-broken pair" in i for i in i2)
          and any("cannot be seen" in i for i in i3), f"{i2} {i3}")
    br = perfect_answer(lab, "B")
    br["element_rules"][0]["rule_id"] = f"[{br['element_rules'][0]['rule_id']}]"
    br["lane_markings"].append({"observation": "far ahead", "marking": "line:crosswalk", "evidence": "partial"})
    sbr = score_lane(br, lab, "B", rid, set(), schema)
    ctl = score_lane(perfect_answer(lab, "B"), lab, "C", set(cn_ids), set(), schema)
    check("lane scoring: an ID in brackets is read without them and counted; an added crosswalk fails the lane but not the lane without lines "
          "across it; Test C citations are checked against the passages it was given",
          sbr["citation"] == "accepted" and sbr["cite_format_fixed"] == 1 and sbr["lane"] is False and sbr["lane_core"] is True
          and sbr["markings"]["added_evidence"] == {"line:crosswalk": "partial"} and ctl["citation"] == "unlisted", f"{sbr['citation']} {ctl['citation']}")
    pd = paired_difference(15, 6, 20, 5)
    check("lane comparison: difference of paired proportions with Newcombe's interval (reference example: -0.196, -0.370 to -0.003)",
          pd["diff"] == -0.1957 and pd["ci95"] == [-0.3699, -0.0026], str(pd))

    # mock runs, comparison, rescore, trace
    ids = L.run_lane_pair(cfg, "US", 0, "any", True, log=lambda *x: None)
    d = P.runs_dir(C.repo_of(cfg)) / ids["A"]
    man = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    tr = (d / "trace.md").read_text(encoding="utf-8")
    check("lane mock runs: files, one request per image, task recorded, trace shows the seven steps",
          all((d / f).exists() for f in ("manifest.json", "results.jsonl", "scores.json", "summary.md", "trace.md"))
          and len((d / "results.jsonl").read_text(encoding="utf-8").splitlines()) == 4 and man["task"] == "lane" and man["repeats"] == 1
          and all(k in tr for k in ("Step 2  Left", "Step 4  Cross-check", "Step 7  Reflect", "Advice")))
    c = L.compare_lane_runs(cfg, ids["A"], ids["B"])
    before = L.load_lane_run(cfg, ids["A"])["scores"]["summary"]
    after = L.rescore_lane_run(cfg, ids["A"])
    check("lane compare (paired, same settings and shared prompt) and rescore without the API",
          c["n"] == 4 and c["same_settings"] and c["same_shared_prompt"] and c["tests"] == ["A", "B"]
          and after["lane"] == before["lane"] and after["output2"] == before["output2"], json.dumps(c)[:300])
    from ..agent.runner import list_runs
    check("lane runs are listed apart from the single-marking runs",
          {r["run_id"] for r in L.list_lane_runs(cfg)} >= set(ids.values()) and not (set(ids.values()) & {r["run_id"] for r in list_runs(cfg)}))
    check("lane find_run reuses a matching mock run", L.find_lane_run(cfg, "B", "US", "any", mock=True) == ids["B"])
    pa = compare_lane({"x": {"score": good}}, {"x": {"score": bad}})
    check("lane McNemar on paired images", pa["lane"]["only_A_right"] == 1 and pa["unsafe_errors"] == {"A": 0, "B": 1})

    # the frozen protocol: the test images are answered only with it, and each test runs once on them
    from ..evaluation.protocol import freeze, protocol_check
    api = FakeApi()
    c2 = dict(cfg, mock=False, api=dict(cfg["api"], base_url=api.url))
    api.answer = perfect_answer({k: it.label.get(k, "") for k in L.LABEL_KEYS}, "B")
    test_item = next(x for x in us if x.split == "test")
    n_req = len(api.requests)
    refused_ask = L.ask_lane(c2, test_item, "B", False, use_cache=False)
    try:
        L.run_lane(c2, "A", "US", 0, "test", False, log=lambda *x: None)
        refused_run = False
    except C.ConfigError:
        refused_run = True
    sent_before_freeze = len(api.requests) - n_req
    unfrozen = protocol_check(c2)
    doc = freeze(c2, "self-test")
    ok1 = protocol_check(c2)
    role = repo / c2["lane"]["prompt_dir"] / "role.txt"
    keep = role.read_bytes()
    role.write_bytes(keep + b"\nOne more sentence.")
    changed = protocol_check(c2)
    role.write_bytes(keep)
    first_test = L.run_lane(c2, "A", "US", 0, "test", False, log=lambda *x: None)
    try:
        L.run_lane(c2, "A", "US", 0, "test", False, log=lambda *x: None)
        twice = True
    except C.ConfigError:
        twice = False
    again_id = L.run_lane(c2, "A", "US", 0, "test", False, log=lambda *x: None, again=True)
    m_first, m_again = (json.loads((P.runs_dir(C.repo_of(c2)) / r / "manifest.json").read_text(encoding="utf-8")) for r in (first_test, again_id))
    check("protocol: before freezing, test images get no new answer (no request sent); freezing records files, settings and prompts; "
          "a changed prompt file is reported; each test runs once on the test images, again only with --again (recorded)",
          "frozen protocol" in refused_ask["error"] and sent_before_freeze == 0 and refused_run and not unfrozen["frozen"]
          and ok1["matches"] and doc["prompts"].get("C_US") and any("role.txt" in d for d in changed["differences"]) and not twice
          and m_first["protocol"]["matches"] and not m_first["again"] and m_again["again"], f"{unfrozen} {changed['differences'][:2]}")

    # request format (fake API), on a development image: the streamed request below changes a setting, which the frozen protocol
    # refuses on test images
    it = next(x for x in us if x.split == "dev")
    api.answer = perfect_answer({k: it.label.get(k, "") for k in L.LABEL_KEYS}, "B")
    rec = L.ask_lane(c2, it, "B", False, use_cache=False)
    req = api.requests[-1]
    img_part = req["input"][1]["content"][1]
    check("lane request: plain image, lane schema, the lane output limit, rule passages only in Test B; answer parsed and scored",
          req["text"]["format"]["name"] == "lane_answer" and req["max_output_tokens"] == int(cfg["lane"]["max_output_tokens"])
          and img_part["image_url"].startswith("data:image/jpeg;base64,") and "RULE PASSAGES" in req["input"][0]["content"][0]["text"]
          and rec["score"] and rec["score"]["lane"], json.dumps(rec)[:300])
    events = []
    c3 = dict(c2, api=dict(c2["api"], reasoning_summary="auto"))
    rec_s = L.ask_lane(c3, it, "B", False, use_cache=False, on_event=lambda k, d: events.append((k, d)))
    kinds = [k for k, _ in events]
    check("lane request, streamed: the summary of the reasoning and then the answer arrive in pieces; the record is the same as without streaming",
          api.requests[-1].get("stream") is True and "reasoning" in kinds and kinds.index("reasoning") < kinds.index("text")
          and "".join(d for k, d in events if k == "text") == rec_s["text"] == rec["text"] and rec_s["score"] == rec["score"]
          and rec_s["response"]["reasoning_summary"].startswith("The line"), f"{kinds[:5]} {json.dumps(rec_s)[:200]}")

    # the demo page in the lane task: items, the photo without a box, the prompt, an answer, the answers of a finished run
    import threading
    import urllib.error
    import urllib.request
    from http.server import ThreadingHTTPServer
    from ..web.server import Demo, make_handler
    real_run = L.run_lane(c2, "B", "US", 2, "any", False, log=lambda *x: None)
    demo = Demo(c2)
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(demo))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{httpd.server_address[1]}"
    get = lambda p: urllib.request.urlopen(base + p, timeout=20).read()  # noqa: E731
    items = json.loads(get("/api/items?task=lane&region=US&split=any"))
    dev = json.loads(get("/api/items?task=lane&region=US&split=dev"))
    first = next(i for i in items if i["saved"].get("B"))
    jpg = get(f"/api/image?task=lane&id={first['image_id']}&w=200")
    pr = json.loads(get("/api/prompt?task=lane&test=B&region=US"))
    saved = json.loads(get(f"/api/saved?id={first['image_id']}"))
    rq = urllib.request.Request(base + "/api/ask", data=json.dumps({"image_id": first["image_id"], "test": "B", "cache": False, "task": "lane"}).encode(),
                                headers={"Content-Type": "application/json"}, method="POST")
    asked = json.loads(urllib.request.urlopen(rq, timeout=30).read())
    runs = json.loads(get("/api/runs?task=lane"))
    check("demo, lane task: items per split with the answers of finished runs, photo, prompt with its two Test B slots, an answer with its passages",
          len(items) == 4 and len(dev) == 2 and sum(1 for i in items if i["saved"].get("B")) == 2 and jpg[:2] == b"\xff\xd8"
          and pr["rules_block"] and all(v in pr["instructions"] for v in pr["slots"].values())
          and saved["B"]["from_run"]["run_id"] == real_run and saved["B"]["answer"] and "passages" in saved["B"]
          and asked["answer"] and asked["score"] is not None and "passages" in asked and real_run in {r["run_id"] for r in runs},
          f"{len(items)} {len(dev)} {list(saved)}")

    # the thinking window: the answer as server-sent events, live from the API or replayed from the cache
    def sse(p):
        evs, name = [], ""
        with urllib.request.urlopen(base + p, timeout=30) as r:
            for raw in r:
                line = raw.decode("utf-8").rstrip("\r\n")
                if line.startswith("event:"):
                    name = line[6:].strip()
                elif line.startswith("data:"):
                    evs.append((name, json.loads(line[5:])))
        return evs

    phases = lambda evs: [d.get("phase") for k, d in evs if k == "status"]  # noqa: E731
    text_of = lambda evs: "".join(d["d"] for k, d in evs if k == "text")  # noqa: E731
    live = sse(f"/api/ask_stream?id={first['image_id']}&test=B&cache=0")
    again = sse(f"/api/ask_stream?id={first['image_id']}&test=B&cache=1")
    done_l, done_a = live[-1][1], again[-1][1]
    check("demo, thinking window: a new answer streams (start, writing, the text in pieces, done); the same question again is replayed from the cache",
          phases(live)[:2] == ["start", "writing"] and live[-1][0] == "done" and text_of(live) == done_l["text"] and done_l["score"] is not None
          and "passages" in done_l and again[-1][0] == "done" and "replay" in phases(again) and done_a["cached"] and text_of(again) == done_a["text"],
          f"{phases(live)} {phases(again)} {[k for k, _ in live][-3:]}")
    bad = sse("/api/ask_stream?id=no_such_image&test=A")
    check("demo, thinking window: an unknown image ends with a fail event, not a broken stream", bad and bad[-1][0] == "fail", str(bad)[:200])

    # a photo uploaded on the page: no label, so no score, only the contradictions inside the answer
    ok_png = base64.b64encode(cv2.imencode(".png", np.full((180, 320, 3), 90, np.uint8))[1].tobytes()).decode()
    post = lambda p, obj: json.loads(urllib.request.urlopen(urllib.request.Request(  # noqa: E731
        base + p, data=json.dumps(obj).encode(), headers={"Content-Type": "application/json"}, method="POST"), timeout=30).read())
    up = post("/api/upload", {"data": "data:image/png;base64," + ok_png, "name": "my photo.png", "region": "US"})
    listed = json.loads(get("/api/items?task=lane&region=US&split=dev"))
    on_up = sse(f"/api/ask_stream?id={up['image_id']}&test=A&cache=0")
    try:
        post("/api/upload", {"data": base64.b64encode(b"not an image").decode(), "region": "US"})
        refused = False
    except urllib.error.HTTPError:
        refused = True
    check("demo, uploaded photo: listed first, answered with no score and its consistency checks; a file that is not an image is refused",
          up["image_id"].startswith("upload_") and listed[0]["image_id"] == up["image_id"] and listed[0]["upload"]
          and on_up[-1][0] == "done" and on_up[-1][1]["answer"] and on_up[-1][1]["score"] is None and isinstance(on_up[-1][1]["checks"], list)
          and refused, f"{up} {on_up[-1][0]}")

    # a batch run from the page: its log grows line by line; each line opens that image's answer
    post("/api/run", {"task": "lane", "test": "B", "region": "US", "split": "dev", "cache": False})
    t_end = time.time() + 60
    while json.loads(get("/api/progress"))["running"] and time.time() < t_end:
        time.sleep(0.1)
    prog = json.loads(get("/api/progress?since=0"))
    tail = json.loads(get(f"/api/progress?since={prog['log_total']}"))
    one = prog["log"][0] if prog["log"] else {}
    from_job = json.loads(get(f"/api/record?test=B&id={one.get('image_id')}"))
    lines = json.loads(get(f"/api/run_records?id={real_run}"))
    from_run = json.loads(get(f"/api/record?run={real_run}&test=B&id={lines[0]['image_id']}"))
    # blind review of the disagreements (the fake API gives every image the answer of one image, so there are some)
    from ..evaluation.review import label_after_review, review_items, review_summary, save_decision
    page = get("/review")
    ri = json.loads(get("/api/review/items?region=US"))
    kinds = {i["kind"] for i in ri["items"]}
    mk = next((i for i in ri["items"] if i["kind"] == "marking"), None)
    bd = next((i for i in ri["items"] if i["kind"] == "boundary"), None)
    try:
        post("/api/review/decide", {"item_id": bd["item_id"], "decision": "option", "value": "purple|zigzag||no"})
        bad_value = True
    except urllib.error.HTTPError:
        bad_value = False
    lab_of = {x.image_id: x.label for x in L.load_lane_items(c2, "US", "any")}
    has = mk["key"] in lab_of[mk["image_id"]]["markings"].split(";")
    post("/api/review/decide", {"item_id": mk["item_id"], "decision": "option", "value": "no" if has else "yes", "reviewer": "st"})
    save_decision(c2, bd, "cannot_tell", "", "st")
    after_items = review_items(c2, "US")
    rs = review_summary(c2, "US")
    rel = label_after_review(lab_of[mk["image_id"]], {mk["field"]: {"decision": "option", "value": "no" if has else "yes"}})
    rel2 = label_after_review(lab_of[bd["image_id"]], {bd["field"]: {"decision": "cannot_tell", "value": ""}})
    orig_scores = (P.runs_dir(C.repo_of(c2)) / real_run / "scores.json").read_text(encoding="utf-8")
    L.rescore_lane_run(c2, real_run, reviewed=True)
    eff = json.loads(get("/api/review/effect?region=US"))
    cmp_rev = json.loads(get(f"/api/compare?task=lane&a={real_run}&b={real_run}&reviewed=1"))
    check("blind review: items only where answers and label differ, options without their source; a value that is not an option is refused; "
          "decisions saved and counted; applied on top of the label (a marking flipped, an undecidable side not scored); scores after the review "
          "written next to the unchanged originals",
          b"review.js" in page and ri["n"] > 0 and {"marking", "boundary"} <= kinds and not bad_value
          and sum(1 for i in after_items["items"] if i["decided"]) == 2 and rs["by_kind"]["marking"]["label_changed"] == 1
          and rs["by_kind"]["boundary"]["cannot_tell"] == 1 and (mk["key"] in rel["markings"].split(";")) != has
          and rel2[f"{bd['key']}_evidence"] == "insufficient" and (P.runs_dir(C.repo_of(c2)) / real_run / "scores_reviewed.json").exists()
          and (P.runs_dir(C.repo_of(c2)) / real_run / "scores.json").read_text(encoding="utf-8") == orig_scores
          and any(e["run_id"] == real_run for e in eff["runs"]) and cmp_rev["reviewed"] and eff["decisions"] == 2,
          f"{ri['n']} {kinds} {rs}")
    httpd.shutdown()
    check("demo, batch log: one line per answer (since= returns only new lines); the answer of a line, from the running batch or a finished run",
          prog["log_total"] == 2 and len(prog["log"]) == 2 and tail["log"] == [] and one["o1"] is not None and one["actions"]
          and from_job["answer"] and "passages" in from_job and len(lines) == 2 and from_run["answer"] and "passages" in from_run,
          f"{prog.get('log_total')} {prog.get('error')} {len(lines)}")
    api.httpd.shutdown()

    # named experiment (mock)
    from ..evaluation.experiments import table as exp_table
    import yaml
    ef = repo / P.EXPERIMENT_FILE
    y = yaml.safe_load(ef.read_text(encoding="utf-8"))
    y["data"]["workspaces"], y["data"]["send_to_api"] = cfg["workspaces"], cfg["data_policy"]["send_to_api"]
    ef.write_text(yaml.safe_dump(y, allow_unicode=True, sort_keys=False), encoding="utf-8")
    yf = repo / P.EXPERIMENTS_FILE
    yf.write_text(yf.read_text(encoding="utf-8").replace("{split: dev, model: gpt-6.1-sol", "{split: any, model: gpt-6.1-sol"), encoding="utf-8")
    md = exp_table(repo, "E5_lane_rules", mock=True, log=lambda *x: None)
    check("experiment E5 (lane, mock): table and paired comparison for both regions",
          "A_lane_US" in md and "B_lane_CN" in md and "McNemar" in md and "No saved run" not in md, md[-600:])

    # dataset suggestions: BDD100K lines with attributes, CULane positions
    ann = {"objects": [
        {"classTitle": "lane", "tags": [{"name": "attributes", "value": "{'laneDirection': 'parallel', 'laneStyle': 'solid', 'laneType': 'double yellow'}"}],
         "points": {"exterior": [[600, 400], [400, 700]]}},
        {"classTitle": "lane", "tags": [{"name": "attributes", "value": "{'laneDirection': 'parallel', 'laneStyle': 'dashed', 'laneType': 'single white'}"}],
         "points": {"exterior": [[700, 400], [900, 700]]}},
        {"classTitle": "lane", "tags": [{"name": "attributes", "value": "{'laneDirection': 'parallel', 'laneStyle': 'solid', 'laneType': 'road curb'}"}],
         "points": {"exterior": [[760, 400], [1270, 700]]}},
        {"classTitle": "lane", "tags": [{"name": "attributes", "value": "{'laneDirection': 'vertical', 'laneStyle': 'solid', 'laneType': 'crosswalk'}"}],
         "points": {"exterior": [[300, 600], [900, 600]]}}]}
    pick = ego_boundaries(bdd_lines(ann), 1280, 720)
    check("BDD100K suggestion: the nearest line on each side of my lane, with colour, pattern and curb",
          pick["left"]["color"] == "yellow" and pick["left"]["pattern"] == "double_solid" and pick["right"]["pattern"] == "dashed"
          and pick["right"]["curb"] == "no", json.dumps(pick)[:300])

    # merging two annotators and agreement
    paths = Paths(repo, ws, "selftest", "images")
    trip = Trip.__new__(Trip)
    trip.paths, trip.id, trip.meta = paths, "st_lanes", {"annotators_required": 2}
    anns = LaneAnnotationStore(lane_annotations_csv(paths, "st_lanes"))
    store = LaneStore(lanes_csv(paths, "st_lanes"))
    for iid in ("st_lanes__lane00", "st_lanes__lane01"):
        r = dict(store.get(iid), final_source="", lane_status="kept")
        store.put(r)
        anns.put(annotation_row(iid, "owner", r, "done"))
        other = dict(r)
        if iid.endswith("01"):
            other["left_pattern"] = "solid"
        anns.put(annotation_row(iid, "ann01", other, "done"))
    store.save()
    anns.save()
    counts = merge_lanes(paths, trip)
    st = LaneStore(lanes_csv(paths, "st_lanes"))
    ag = lane_agreement(paths, ["st_lanes"])
    adj = adjudicate_lane(paths, trip, "st_lanes__lane01", "owner", None, "owner's reading", "owner")
    check("lane labels: two agreeing annotations give a final label, a disagreement goes to adjudication; agreement per field",
          st.get("st_lanes__lane00")["lane_status"] == "done" and st.get("st_lanes__lane01")["lane_status"] == "conflict"
          and adj["lane_status"] == "done" and adj["final_source"] == "adjudicated" and ag["items"] == 2 and ag["all_fields_agree"] == 0.5
          and next(f for f in ag["fields"] if f["field"] == "left_pattern")["percent_agreement"] == 0.5, f"{counts} {ag['all_fields_agree']}")
    from ..labeling.lanes import lane_required
    per_split = {"annotators_required": 2, "lane_annotators_required": {"dev": 1, "test": 2}}
    check("lane labels: the number of annotators can differ per split (one for development, two for test)",
          lane_required(per_split, "dev") == 1 and lane_required(per_split, "test") == 2 and lane_required({"annotators_required": 2}, "dev") == 2
          and lane_required({"lane_annotators_required": 1}, "test") == 1)

    check_deploy_files(check)


def check_deploy_files(check) -> None:
    """The Docker files keep their safety settings and the package versions agree with requirements.txt.
    Skipped inside the Docker image, which holds no Docker files."""
    import re
    from .. import config as C
    root = C.REPO
    if not (root / "Dockerfile").exists():
        print("SKIP deploy checks: no Dockerfile here (inside the image)")
        return

    def pins(path: Path) -> dict:
        out = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^([A-Za-z0-9_.\-]+)==([^\s;\\]+)", line.strip())
            if m:
                out[m.group(1).lower().replace("_", "-")] = m.group(2)
        return out
    req, img, lock = pins(root / "requirements.txt"), pins(root / "deploy" / "requirements-docker.txt"), pins(root / "deploy" / "requirements-docker.lock")
    differ = {k: (req.get(k), v, lock.get(k)) for k, v in img.items() if req.get(k) != v or lock.get(k) != v}
    check("deploy: the image packages have the same versions in requirements.txt, deploy/requirements-docker.txt and the lock file",
          bool(img) and not differ, str(differ))
    docker = (root / "Dockerfile").read_text(encoding="utf-8")
    ignore = [x.strip() for x in (root / ".dockerignore").read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]
    compose = (root / "docker-compose.yml").read_text(encoding="utf-8")
    ports = re.findall(r'^\s*- "([^"]+:\d+)"', compose, re.M)
    check("deploy: the image runs as a normal user that can read the code, copies named folders only, keeps .env and data out; ports only on 127.0.0.1",
          "USER appuser" in docker and "COPY . ." not in docker and "--require-hashes" in docker and ignore[0] == "*"
          and all("--chmod=" in line for line in docker.splitlines() if line.startswith("COPY ") and "requirements" not in line)
          and not any(x.startswith("!") and (".env" in x or "data" in x or "results" in x or "runs" in x or "labels" in x) for x in ignore)
          and bool(ports) and all(p.startswith("127.0.0.1:") for p in ports) and 'GF_AUTH_ANONYMOUS_ENABLED: "false"' in compose
          and "GRAFANA_ADMIN_PASSWORD:?" in compose and "OPENAI_API_KEY" not in docker, f"{ports}")
    keyish = [f.name for f in (root / "configs").glob("*.yaml") if re.search(r"\bsk-[A-Za-z0-9_-]{20,}", f.read_text(encoding="utf-8"))]
    check("deploy: no API key in configs/ (it would go into Git and into the image; it belongs in .env)", not keyish, str(keyish))
    copied = re.findall(r"^COPY --chmod=755 (\S+) ", docker, re.M)
    check("deploy: the image holds main.py, the package, the settings, the prompts and the rules, starts the web page, and the datasets are mounted read-only",
          sorted(copied) == ["configs", "main.py", "prompts", "reasoning_drive", "regulations"]
          and '"main.py", "web"' in docker and "./datasets:/app/datasets:ro" in compose and "./results:/app/results" in compose
          and "regulations/inbox/" in ignore, str(copied))
