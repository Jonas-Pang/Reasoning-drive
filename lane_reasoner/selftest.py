"""Self-test of the model-run code without the real API: python -m lane_reasoner selftest

Builds a throw-away copy of the repository (settings, rules, prompts) and a tiny synthetic image workspace with
final labels, then checks: loading the labels, the prompts of Test A and Test B, the boxed image, mock runs and
their comparison, a fake Responses API server (request format, parsing, retries, errors, cache), the demo
server, and that the API key is not written to any file.
"""
from __future__ import annotations

import json
import os
import shutil
import tempfile
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import cv2
import numpy as np

SECRET = "sk-selftest-DO-NOT-STORE-0123456789abcd"
LABELS = [  # (marking_type, arrow_type, position, region)
    ("yellow_double_solid", "", "left", "US"), ("white_dashed", "", "right", "US"), ("white_dashed", "", "left", "US"),
    ("yellow_solid", "", "left", "US"), ("arrow", "left", "in_ego_lane", "US"), ("arrow", "straight", "in_ego_lane", "US"),
    ("two_way_left_turn_lane", "", "left", "US"), ("white_solid", "", "right", "US"), ("yellow_dashed", "", "left", "US"),
    ("white_dashed", "", "left", "CN"),
]


def _build(root: Path, src_repo: Path) -> Path:
    from video_tool.core import LABEL_COLUMNS, load_action_rules, prefill, write_csv
    from types import SimpleNamespace
    repo = root / "repo"
    for d in ("config", "prompts"):
        shutil.copytree(src_repo / d, repo / d, ignore=shutil.ignore_patterns("._*", ".DS_Store"))  # macOS helper files
    (repo / "rules").mkdir(parents=True)
    shutil.copy(src_repo / "rules" / "rule_passages.json", repo / "rules" / "rule_passages.json")
    ws = root / "ws"
    (ws / "selected" / "st_set").mkdir(parents=True)
    (ws / "workspace.json").write_text(json.dumps({"collection": "selftest", "kind": "images", "dataset": "synthetic"}), encoding="utf-8")
    import yaml
    y = yaml.safe_load((repo / "config" / "experiment.yaml").read_text(encoding="utf-8"))
    y["data"]["workspaces"] = [str(ws)]
    y["data"]["send_to_api"] = ["selftest"]
    y["experiment"]["mock"] = True
    y["model"]["parallel"] = 3
    (repo / "config" / "experiment.yaml").write_text(yaml.safe_dump(y, allow_unicode=True, sort_keys=False), encoding="utf-8")
    table = load_action_rules(SimpleNamespace(repo=repo))
    passages = json.loads((repo / "rules" / "rule_passages.json").read_text(encoding="utf-8"))
    rows = []
    for i, (mt, at, pos, region) in enumerate(LABELS + [("white_dashed", "", "left", "US")]):
        img = np.full((360, 640, 3), 60, np.uint8)
        cv2.line(img, (200 + 20 * i, 360), (300 + 10 * i, 180), (230, 230, 230), 6)
        p = ws / "selected" / "st_set" / f"img{i:02d}.jpg"
        cv2.imwrite(str(p), img)
        sug = prefill(table, region, mt, at, "", "full")
        ids = sug.get("rule_ids") or [x["rule_id"] for x in passages if x["region"] == region][:1]
        row = {c: "" for c in LABEL_COLUMNS}
        row.update({"image_id": f"st_set__img{i:02d}", "region": region, "dataset": "synthetic", "source_path": f"selected/st_set/img{i:02d}.jpg",
                    "split": "dev" if i % 4 == 0 else "test", "width": 640, "height": 360, "marking_type": mt, "arrow_type": at,
                    "position": pos, "bbox_x1": 180 + 20 * i, "bbox_y1": 170, "bbox_x2": 320 + 10 * i, "bbox_y2": 359,
                    "visibility": "V2", "behavior_decidable": "yes", "expected_evidence": "full", "accepted_rule_ids": ";".join(ids),
                    "label_status": "done" if i < len(LABELS) else "waiting"})
        for a, v in sug.get("actions", {}).items():
            row["act_" + a] = v
        rows.append(row)
    lab = repo / "labels" / "selftest"
    lab.mkdir(parents=True)
    (lab / "st_set.set.json").write_text("{}", encoding="utf-8")
    write_csv(lab / "st_set.labels.csv", rows, LABEL_COLUMNS)
    return repo


class FakeApi:
    """A stand-in for POST /v1/responses. mode: ok | 429once | bad_param | incomplete."""

    def __init__(self):
        self.mode, self.hits, self.requests, self.auth = "ok", 0, [], []
        api = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                api.hits += 1
                api.requests.append(body)
                api.auth.append(self.headers.get("Authorization", ""))
                if api.mode == "429once" and api.hits == 1:
                    return self._send(429, {"error": {"message": "Rate limit"}}, {"retry-after": "0.05"})
                if api.mode == "bad_param":
                    return self._send(400, {"error": {"message": "Unsupported value", "param": "temperature"}})
                wants_summary = "summary" in (body.get("reasoning") or {})
                if api.mode == "no_summary" and wants_summary:
                    return self._send(400, {"error": {"message": "Your organization must be verified to generate reasoning summaries.",
                                                      "param": "reasoning.summary"}})
                text = json.dumps(api.answer)
                summary = [{"type": "summary_text", "text": "The line is solid and yellow, so crossing is prohibited."}] if wants_summary else []
                out = {"id": "resp_fake", "model": body["model"] + "-2026-01-01", "status": "completed",
                       "output": [{"type": "reasoning", "summary": summary},
                                  {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": text}]}],
                       "usage": {"input_tokens": 1234, "output_tokens": 99, "total_tokens": 1333}}
                if api.mode == "incomplete":
                    out.update(status="incomplete", incomplete_details={"reason": "max_output_tokens"})
                self._send(200, out)

            def _send(self, code, obj, headers=None):
                b = json.dumps(obj).encode()
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(b)))
                for k, v in (headers or {}).items():
                    self.send_header(k, v)
                self.end_headers()
                self.wfile.write(b)

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.url = f"http://127.0.0.1:{self.httpd.server_address[1]}/v1"
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()


def main() -> int:
    from . import config as C
    from .client import ApiError, ping
    from .data import boxed_jpeg, load_items
    from .prompts import passages, prompt_parts
    from .runner import ask, compare_runs, list_runs, run_batch
    from .scoring import mcnemar_exact, score_one

    results: list[tuple[str, bool, str]] = []

    def check(name, ok, detail=""):
        results.append((name, bool(ok), detail))
        print(("PASS " if ok else "FAIL ") + name + (f" — {detail}" if detail and not ok else ""))

    tmp = Path(tempfile.mkdtemp(prefix="lane_reasoner_selftest_"))
    old_env = {k: os.environ.get(k) for k in ("OPENAI_API_KEY", "NO_PROXY", "no_proxy", "DATASETS_ROOT")}
    try:
        os.environ.pop("DATASETS_ROOT", None)  # the self-test uses its own folders
        os.environ["OPENAI_API_KEY"] = SECRET
        for k in ("NO_PROXY", "no_proxy"):
            os.environ[k] = ",".join(x for x in (os.environ.get(k, ""), "127.0.0.1,localhost") if x)
        repo = _build(tmp, C.REPO)
        cfg = C.load(repo)

        # 1. labels
        us, cn = load_items(cfg, "US", "any", []), load_items(cfg, "CN", "any", [])
        check("final labels loaded per region (waiting rows left out)", len(us) == 9 and len(cn) == 1, f"US {len(us)}, CN {len(cn)}")
        check("split filter", len(load_items(cfg, "US", "dev", [])) == sum(1 for i in range(9) if i % 4 == 0))
        from .data import workspace_dirs
        blocked = dict(cfg, data_policy={"send_to_api": ["own_video"]})
        rel = dict(cfg, workspaces=["ws"], datasets_root=str(tmp))
        check("data policy keeps collections without permission away from the API; relative workspaces use datasets_root",
              load_items(blocked, "US", "any", []) == [] and workspace_dirs(rel) == [tmp / "ws"] and len(load_items(rel, "US", "any", [])) == 9)

        # 2. prompts
        a, b = prompt_parts(cfg, "A", "US"), prompt_parts(cfg, "B", "US")
        us_ids = [p["rule_id"] for p in passages(cfg, "US")]
        check("Test A prompt has no rule passages", not any(f"[{i}]" in a["instructions"] for i in us_ids) and "RULE PASSAGES" not in a["instructions"])
        check("Test B prompt has every US passage and only US ones",
              all(f"[{i}]" in b["instructions"] for i in us_ids) and not any(f"[{p['rule_id']}]" in b["instructions"] for p in passages(cfg, "CN")))
        check("A and B share instructions skeleton, schema, user text", a["hashes"]["shared_parts"] == b["hashes"]["shared_parts"]
              and a["schema"] == b["schema"] and a["user_text"] == b["user_text"] and a["hashes"]["instructions"] != b["hashes"]["instructions"])
        check("no unfilled slots", "{STEP2}" not in a["instructions"] + b["instructions"] and "{CITATION}" not in a["instructions"] + b["instructions"])
        bc = prompt_parts(cfg, "B", "CN")
        check("CN prompt names China and has CN passages", "China" in bc["user_text"] and all(f"[{p['rule_id']}]" in bc["instructions"] for p in passages(cfg, "CN")))
        s = a["schema"]
        def strict_ok(node):
            if isinstance(node, dict):
                if node.get("type") == "object" and (node.get("additionalProperties") is not False or set(node["required"]) != set(node["properties"])):
                    return False
                return all(strict_ok(v) for v in node.values())
            if isinstance(node, list):
                return all(strict_ok(v) for v in node)
            return True
        check("schema is valid for strict mode (all fields required, no extra fields)", strict_ok(s))

        # 3. the boxed image
        it = us[0]
        before = it.path.read_bytes()
        img = cv2.imdecode(np.frombuffer(boxed_jpeg(it, cfg), np.uint8), cv2.IMREAD_COLOR)
        x1 = max(0, it.box[0] - 6)
        px = img[(it.box[1] + it.box[3]) // 2, x1 + 1].astype(int)
        check("cyan box drawn on a copy, original unchanged", px[0] > 180 and px[1] > 160 and px[2] < 90 and it.path.read_bytes() == before, str(px))

        # 4. scoring
        def perfect_for(x):
            return {"evidence": "full", "marking": {"marking_type": x.label["marking_type"], "arrow_type": x.label["arrow_type"] or None,
                                                    "position": x.label["position"]},
                    "actions": {k: x.label["act_" + k] for k in ("cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_center_lane_to_wait")},
                    "cited_rule_id": x.label["accepted_rule_ids"].split(";")[0]}
        ys = next(x for x in us if x.label["marking_type"] == "yellow_double_solid")
        sc = score_one(perfect_for(ys), ys.label, "B", set(us_ids), set())
        bad = perfect_for(ys)
        bad["actions"]["cross_line"] = "allowed"
        bad["cited_rule_id"] = "US-9Z.99-99"
        sb = score_one(bad, ys.label, "B", set(us_ids), set())
        from .scoring import consistency_issues
        odd = perfect_for(ys)
        odd["actions"]["turn_left"] = "allowed"
        check("consistency check flags an action the marking does not govern, and passes a clean answer",
              consistency_issues(odd) and not consistency_issues(perfect_for(ys)), str(consistency_issues(odd)))
        check("scoring: perfect answer, unsafe error, made-up citation",
              sc["output1"] and sc["output2"] and sc["citation"] == "accepted" and sb["unsafe"] == ["cross_line"]
              and sb["output2"] is False and sb["citation"] == "unlisted", f"{sc} / {sb}")
        perfect = perfect_for(it)
        check("exact McNemar", abs(mcnemar_exact(0, 5) - 0.0625) < 1e-9 and mcnemar_exact(0, 0) is None and mcnemar_exact(3, 3) == 1.0)

        # 5. mock runs and comparison
        ra = run_batch(cfg, "A", "US", 0, 2, "any", True, log=lambda *x: None)
        rb = run_batch(cfg, "B", "US", 0, 2, "any", True, log=lambda *x: None)
        d = C.repo_of(cfg) / "runs" / ra
        files_ok = all((d / f).exists() for f in ("manifest.json", "results.jsonl", "scores.json", "summary.md", "trace.md"))
        lines = (d / "results.jsonl").read_text(encoding="utf-8").splitlines()
        man = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
        check("mock run writes manifest (with code hash and split version), results (9 images × 2), scores, summary, trace",
              files_ok and len(lines) == 18 and len(man.get("code_sha", "")) == 16 and man.get("split_version") == 1)
        c = compare_runs(cfg, ra, rb)
        check("compare A vs B: paired on 9 images, same settings and shared prompt",
              c["output1"]["n"] == 9 and c["same_settings"] and c["same_shared_prompt"] and c["tests"] == ["A", "B"], json.dumps(c))
        check("runs listed", {r["run_id"] for r in list_runs(cfg)} >= {ra, rb})
        from .runner import load_run, rescore_run
        before = load_run(cfg, ra)["scores"]["summary"]
        after = rescore_run(cfg, ra)
        sc_c = score_one(bad, ys.label, "B", set(us_ids), {"cross_line"})
        check("rescore without API gives the same scores; contested cells stay out of the main error counts",
              after["output1"] == before["output1"] and after["output2"] == before["output2"] and len(load_run(cfg, ra)["records"]) == 18
              and sc_c["unsafe"] == [] and sc_c["contested_unsafe"] == ["cross_line"], f"{before['output2']} / {after['output2']} / {sc_c}")

        # report helpers used by the model exploration notebook
        import matplotlib
        matplotlib.use("Agg")
        from . import report as R
        audit = R.data_audit(cfg)
        found = R.find_run(cfg, "A", "US", "any", 2, mock=True)
        mt = R.metrics(cfg, ra)
        table = R.experiment_table(cfg, [("A", ra, "baseline"), ("B", rb, "add rule passages")])
        cases = R.error_cases(cfg, ra)
        fig1 = R.show_cases(cfg, cases[:2]) if cases else None
        fig2 = R.plot_comparison({"Test A": mt, "Test B": R.metrics(cfg, rb)})
        sep = R.check_separation(cfg, "US", "any", [ra, rb])
        rec = R.config_record(cfg, ra)
        check("report: data audit, reuse of a matching run, metrics, error cases, figures, experiment table, separation check",
              len(audit["used"]) == 10 and audit["dropped"] == {"not final yet (waiting)": 1} and found == ra
              and mt["images"] == 9 and 0 <= (mt["output1_macro_f1"] or 0) <= 1 and mt["same_answer_all_repeats"] is not None
              and len(table) == 2 and "|" in R.to_markdown(table) and fig2 is not None and (fig1 is not None or not cases)
              and sep["runs use only this split"] and rec["model requested"] == cfg["api"]["model"]
              and R.crop(cfg, it.image_id, "US").shape[1] == 420 and len(R.paired_differences(cfg, ra, rb).columns) >= 0
              and int(R.action_confusion(cfg, ra)[0].values.sum()) == len(R.action_confusion(cfg, ra)[1]) > 0
              and R.class_prf(R.action_confusion(cfg, ra)[1])["support (label)"] >= 0,
              f"{audit['dropped']} {found} {mt.get('output1_macro_f1')} {sep}")

        # 6. fake API server: request format, parsing, retries, errors, cache
        api = FakeApi()
        cfg["api"]["base_url"] = api.url
        cfg["mock"] = False
        api.answer = dict(perfect, description="A double yellow line.", reasoning="Fake.")
        rec = ask(cfg, it, "B", 0, False, use_cache=True)
        req = api.requests[-1]
        msgs = req["input"]
        img_part = msgs[1]["content"][1]
        fmt = req["text"]["format"]
        check("request: developer + user message, image as data URL with detail, strict JSON schema",
              msgs[0]["role"] == cfg["api"]["instruction_role"] and msgs[0]["content"][0]["type"] == "input_text"
              and img_part["type"] == "input_image" and img_part["image_url"].startswith("data:image/jpeg;base64,")
              and img_part["detail"] == cfg["api"]["image_detail"] and fmt["type"] == "json_schema" and fmt["strict"] is True
              and req["model"] == cfg["api"]["model"] and req["max_output_tokens"] == cfg["api"]["max_output_tokens"], json.dumps(req)[:400])
        check("request: key only in the Authorization header", api.auth[-1] == f"Bearer {SECRET}" and SECRET not in json.dumps(req))
        check("response parsed and scored", rec["answer"] and rec["score"]["output1"] and rec["response"]["model"].startswith(cfg["api"]["model"])
              and rec["response"]["usage"]["input_tokens"] == 1234, json.dumps(rec)[:400])
        n = api.hits
        rec2 = ask(cfg, it, "B", 0, False, use_cache=True)
        check("identical request is answered from the cache", rec2["cached"] and api.hits == n)
        api.mode, api.hits = "429once", 0
        rec3 = ask(cfg, it, "A", 0, False, use_cache=False)
        check("rate limit (429) is retried", rec3["answer"] is not None and rec3["response"]["attempts"] == 2, rec3.get("error", ""))
        api.mode = "bad_param"
        rec4 = ask(cfg, it, "A", 0, False, use_cache=False)
        check("400 error names the parameter and is not retried", "temperature" in rec4["error"] and "400" in rec4["error"], rec4["error"])
        api.mode = "incomplete"
        rec5 = ask(cfg, it, "A", 0, False, use_cache=False)
        check("incomplete answer reported with a hint", "max_output_tokens" in rec5["error"], rec5["error"])
        api.mode = "ok"
        r = ping(cfg)
        check("ping sends a tiny text request with the same model and settings",
              "input_image" not in json.dumps(api.requests[-1]) and api.requests[-1]["model"] == cfg["api"]["model"] and r["text"])
        from .client import settings_of
        from .trace import trace_text
        cfg["api"]["reasoning_summary"] = "auto"
        rec6 = ask(cfg, it, "B", 0, False, use_cache=False)
        req6 = api.requests[-1]
        check("reasoning summary: requested when set, kept with the answer and shown in the trace",
              req6["reasoning"].get("summary") == "auto" and "solid and yellow" in (rec6["response"] or {}).get("reasoning_summary", "")
              and "Model's summary" in trace_text(rec6) and settings_of(cfg).get("reasoning_summary") == "auto", json.dumps(rec6.get("response"))[:300])
        api.mode = "no_summary"
        rec7 = ask(cfg, it, "B", 0, False, use_cache=False)
        check("reasoning summary refused by the API: sent again without it, the answer notes why",
              rec7["answer"] is not None and "summary" not in (api.requests[-1].get("reasoning") or {})
              and "not available" in (rec7["response"] or {}).get("reasoning_summary_note", ""), rec7.get("error", ""))
        api.mode = "ok"
        cfg["api"]["reasoning_summary"] = None
        check("settings without a reasoning summary are the same as before it existed", "reasoning_summary" not in settings_of(cfg))
        os.environ["OPENAI_API_KEY"] = ""
        n = api.hits
        nokey = ask(cfg, it, "A", 0, False, use_cache=False)["error"]
        try:
            ping(cfg)
        except ApiError as e:
            nokey += " | " + str(e)
        check("no key: clear message, no request", nokey.count("No API key") == 2 and api.hits == n, nokey)
        os.environ["OPENAI_API_KEY"] = SECRET
        api.httpd.shutdown()

        # 7. demo server
        from .demo import Demo, make_handler
        cfg["mock"] = True
        demo = Demo(cfg)
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(demo))
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{httpd.server_address[1]}"
        get = lambda p: urllib.request.urlopen(base + p, timeout=20).read()  # noqa: E731

        def post(p, body):
            rq = urllib.request.Request(base + p, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}, method="POST")
            return json.loads(urllib.request.urlopen(rq, timeout=30).read())
        page = get("/").decode()
        conf_raw = get("/api/config").decode()
        conf = json.loads(conf_raw)
        check("demo: page, config with key status but never the key",
              "demo.js" in page and conf["config"]["api"]["api_key_set"] and SECRET not in conf_raw and conf["items_per_region"]["US"] == 9)
        items = json.loads(get("/api/items?region=US"))
        jpg = get("/api/image?id=" + items[0]["image_id"] + "&w=200")
        check("demo: items and boxed thumbnails", len(items) == 9 and jpg[:2] == b"\xff\xd8")
        pb = json.loads(get("/api/prompt?test=B&region=US"))
        check("demo: prompt B with rule block", pb["rules_block"] and pb["rules_block"] in pb["instructions"])
        ans = post("/api/ask", {"image_id": items[0]["image_id"], "test": "B", "cache": False})
        check("demo: ask (mock) returns a scored answer with the cited passage", ans["score"] is not None and ans["mock"]
              and (ans["cited_passage"] or ans["answer"]["cited_rule_id"] is None))
        conf2 = post("/api/config", {"run.test": "B", "api.temperature": ""})
        check("demo: settings change (not saved)", conf2["config"]["run"]["test"] == "B" and conf2["config"]["api"]["temperature"] is None
              and C.load(repo)["run"]["test"] == "A")
        conf3 = post("/api/config", {"api.model": "gpt-ui", "prompt.dir": "prompts/v2"})
        unsaved_ok = {"model.name", "experiment.prompt"} <= set(conf3["unsaved"]) and C.load(repo)["api"]["model"] != "gpt-ui"
        conf4 = post("/api/config", {"save": True})
        on_file = C.load(repo)
        saved_ok = on_file["api"]["model"] == "gpt-ui" and on_file["prompt"]["dir"] == "prompts/v2" and conf4["unsaved"] == []
        yf = repo / "config" / "experiment.yaml"
        yf.write_text(yf.read_text(encoding="utf-8").replace("gpt-ui", "gpt-file"), encoding="utf-8")
        conf5 = post("/api/config", {"reload": True})
        check("demo: page settings are listed as unsaved, written to the YAML file on request, and reloaded after a manual edit",
              unsaved_ok and saved_ok and conf5["config"]["api"]["model"] == "gpt-file" and conf5["unsaved"] == [],
              f"{conf3['unsaved']} {conf4['unsaved']} {conf5['config']['api']['model']}")
        post("/api/run", {"test": "AB", "region": "US", "limit": 3, "repeats": 1})
        for _ in range(100):
            pr = json.loads(get("/api/progress"))
            if not pr["running"]:
                break
            time.sleep(0.1)
        check("demo: Test A and Test B batch at the same time in the background",
              set(pr["run_ids"]) == {"A", "B"} and pr["done"] == 6 and not pr["error"], json.dumps(pr))
        httpd.shutdown()
        r1 = run_batch(cfg, "A", "US", 2, 1, "any", True, log=lambda *x: None)
        r2 = run_batch(cfg, "A", "US", 2, 1, "any", True, log=lambda *x: None)
        from .runner import run_pair
        pair = run_pair(cfg, "US", 2, 1, "any", True, log=lambda *x: None)
        check("runs started in the same second get their own folders; run_pair runs A and B together",
              r1 != r2 and set(pair) == {"A", "B"} and pair["A"] != pair["B"], f"{r1} {r2} {pair}")

        # 8. settings file, prompt versions, reasoning trace, a new region
        import yaml
        from types import SimpleNamespace
        from video_tool.core import load_rule_passages
        base = yaml.safe_load((C.REPO / "config" / "experiment.yaml").read_text(encoding="utf-8"))
        yb = yaml.safe_load(yaml.safe_dump(base)); yb["experiment"]["use_rules"] = True; yb["model"]["reasoning_summary"] = False
        mb = C.from_yaml(yb)
        try:
            C.from_yaml(yaml.safe_load("experiment: {region: NO}\nregions: {}"))
            quoted = False
        except C.ConfigError:
            quoted = True
        check("YAML settings: use_rules yes = Test B, reasoning_summary off = not sent, a region code read as true/false is refused",
              mb["run"]["test"] == "B" and mb["api"]["reasoning_summary"] is None and C.from_yaml(base)["run"]["test"] == "A" and quoted)
        src_text = (C.REPO / "config" / "experiment.yaml").read_text(encoding="utf-8")
        (repo / "config" / "experiment.yaml").write_text(src_text, encoding="utf-8")
        c2 = C.load(repo)
        c2["run"]["test"], c2["api"]["model"], c2["api"]["temperature"] = "B", "gpt-test", None
        C.save(c2)
        saved = (repo / "config" / "experiment.yaml").read_text(encoding="utf-8")
        c3 = C.load(repo)
        check("saving settings changes only the values and keeps the comments of the YAML file",
              c3["run"]["test"] == "B" and c3["api"]["model"] == "gpt-test" and saved.count("#") == src_text.count("#")
              and len(saved.splitlines()) == len(src_text.splitlines()))
        same = []
        for m in sorted((C.REPO / "runs").glob("2026*/manifest.json")):
            man = json.loads(m.read_text(encoding="utf-8"))
            h = man["prompt_hashes"]
            c3["prompt"]["dir"] = h["prompt_dir"]
            got = prompt_parts(c3, man["test"], man["region"])["hashes"]
            same.append(all(got[k] == h[k] for k in ("instructions", "user_text", "schema")))
        check("prompts v1 and v2 are byte for byte the ones of the saved runs", all(same), f"{len(same)} runs checked")
        c3["prompt"]["dir"] = "prompts/v3"
        p3 = prompt_parts(c3, "B", "US")
        order = list(p3["schema"]["properties"])
        check("prompt v3: the reasoning fields come before the actions in the answer schema",
              order.index("rule_reasoning") < order.index("actions") and order.index("action_reasons") < order.index("actions")
              and order.index("self_check") < order.index("actions") and order[-1] == "actions" and strict_ok(p3["schema"]), str(order))
        c3["mock"], c3["workspaces"], c3["data_policy"] = True, cfg["workspaces"], cfg["data_policy"]
        r3 = run_batch(c3, "B", "US", 2, 1, "any", True, log=lambda *x: None)
        tr = (C.repo_of(c3) / "runs" / r3 / "trace.md").read_text(encoding="utf-8")
        check("trace: every answer of a run, step by step (look, rule, decide, check)",
              all(k in tr for k in ("Step 1  Look", "Step 2  Rule", "Step 3  Decide", "Step 4  Check", "cross_line")) and tr.count("Step 1  Look") == 2)
        (repo / "rules" / "xx_rules.yaml").write_text(yaml.safe_dump([
            {"rule_id": "XX-1", "region": "XX", "source": "Test standard", "section": "1", "page": 1, "marking_type": "white_solid",
             "text_en": "A solid white line shall not be crossed."},
            {"rule_id": "XX-2", "region": "XX", "source": "Test standard", "section": "2", "page": 2, "marking_type": "white_dashed",
             "text_en": "A broken white line may be crossed."}]), encoding="utf-8")
        y4 = yaml.safe_load(src_text)
        y4["regions"]["XX"] = {"name": "Testland", "rules": {"file": "rules/xx_rules.yaml", "code": "XX", "title": "Test standard", "language": "en"}}
        c4 = C.from_yaml(y4); c4["_repo"] = str(repo); C.check(c4)
        px = prompt_parts(c4, "B", "XX")
        check("a new region needs only a passages file and a YAML entry (model prompt and labeling tool both see it)",
              "[XX-1]" in px["instructions"] and "[XX-2]" in px["instructions"] and "Testland" in px["user_text"]
              and "[US-" not in px["instructions"] and len(load_rule_passages(SimpleNamespace(repo=repo), "XX")) == 2)
        (repo / "rules" / "xx_rules.yaml").unlink()

        # 9. the key is not written to any file
        leaked = [str(p) for p in repo.rglob("*") if p.is_file() and SECRET.encode() in p.read_bytes()]
        check("the API key is in no file (runs, cache, config)", not leaked, ", ".join(leaked))
        try:
            C.check(dict(cfg, run=dict(cfg["run"], region="XX")))
            bad_region = False
        except C.ConfigError:
            bad_region = True
        check("unknown region is refused with a clear message", bad_region)
    finally:
        for k, v in old_env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(tmp, ignore_errors=True)
    passed = sum(1 for _, ok, _ in results if ok)
    print(f"\n{passed}/{len(results)} checks passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
