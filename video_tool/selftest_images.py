"""Self-test part 2: two tiny synthetic datasets in the BDD100K (Dataset Ninja) and CULane layouts."""
from __future__ import annotations

import hashlib
import json
import urllib.request
import threading
from pathlib import Path

import cv2
import numpy as np


def _road(w: int, h: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    img = np.full((h, w, 3), 40, np.uint8)
    img[int(h * 0.45):] = (70, 70, 70)
    for _ in range(12):  # random blocks so that every image hashes differently
        x, y = int(rng.integers(0, w - 60)), int(rng.integers(0, h // 2))
        c = [int(v) for v in rng.integers(0, 255, 3)]
        cv2.rectangle(img, (x, y), (x + int(rng.integers(20, 160)), y + int(rng.integers(20, 120))), c, -1)
    return img


def _bdd_lane(typ: str, style: str, pts: list) -> dict:
    return {"classTitle": "lane", "geometryType": "line", "points": {"exterior": pts},
            "tags": [{"name": "attributes", "value": str({"laneDirection": "parallel", "laneStyle": style, "laneType": typ})}]}


def make_bdd(root: Path, n: int = 24) -> Path:
    src = root / "bdd_mirror" / "val"
    (src / "img").mkdir(parents=True)
    (src / "ann").mkdir(parents=True)
    for i in range(n):
        stem = f"{i:08x}-{(i * 2654435761) % (1 << 32):08x}"
        img = _road(1280, 720, i)
        objects = []
        kind = i % 4
        if kind == 0:  # a single yellow solid line, both edges labeled
            cv2.line(img, (560, 400), (380, 700), (0, 200, 230), 10)
            objects += [_bdd_lane("single yellow", "solid", [[556, 400], [375, 700]]),
                        _bdd_lane("single yellow", "solid", [[564, 400], [386, 700]])]
        elif kind == 1:  # white dashed
            for y in range(420, 720, 80):
                cv2.line(img, (700 + (y - 420) // 3, y), (700 + (y + 40 - 420) // 3, y + 40), (230, 230, 230), 8)
            objects += [_bdd_lane("single white", "dashed", [[696, 420], [796, 720]]),
                        _bdd_lane("single white", "dashed", [[704, 420], [806, 720]])]
        elif kind == 2:  # intersection: crosswalk, no lane lines
            objects += [{"classTitle": "lane", "geometryType": "line", "points": {"exterior": [[300, 600], [900, 600]]},
                         "tags": [{"name": "attributes", "value": str({"laneDirection": "vertical", "laneStyle": "dashed", "laneType": "crosswalk"})}]}]
        cv2.imwrite(str(src / "img" / f"{stem}.jpg"), img)
        ann = {"size": {"width": 1280, "height": 720},
               "tags": [{"name": "timeofday", "value": "night" if i % 2 else "daytime"}, {"name": "weather", "value": "clear"},
                        {"name": "scene", "value": "city street"}],
               "objects": objects}
        (src / "ann" / f"{stem}.jpg.json").write_text(json.dumps(ann), encoding="utf-8")
    return src


def _pool(clip: str) -> str:
    return "dev" if int(hashlib.sha1(("6216:" + clip).encode()).hexdigest(), 16) % 10 == 0 else "test"


def make_culane(root: Path) -> tuple[Path, list[str], list[str]]:
    src = root / "culane"
    dev, test = [], []
    k = 0
    while len(dev) < 2 or len(test) < 3:
        clip = f"0525{k:04d}_{k:04d}.MP4"
        (dev if _pool(f"driver_100_30frame/{clip}") == "dev" else test).append(clip)
        k += 1
    clips = dev[:2] + test[:3]
    lists = {"test0_normal.txt": [], "test5_arrow.txt": [], "test4_noline.txt": []}
    for ci, clip in enumerate(clips):
        d = src / "driver_100_30frame" / clip
        d.mkdir(parents=True)
        for fi in range(4):
            frame = f"{fi * 30:05d}"
            img = _road(1640, 590, 1000 + ci * 10 + fi)
            cv2.line(img, (700, 330), (300, 590), (230, 230, 230), 9)
            cv2.line(img, (940, 330), (1300, 590), (230, 230, 230), 9)
            cv2.imwrite(str(d / f"{frame}.jpg"), img)
            left = " ".join(f"{700 - (y - 330) * 400 / 260:.1f} {y}" for y in range(590, 320, -10))
            right = " ".join(f"{940 + (y - 330) * 360 / 260:.1f} {y}" for y in range(590, 320, -10))
            (d / f"{frame}.lines.txt").write_text(left + "\n" + right + "\n", encoding="utf-8")
            name = ["test0_normal.txt", "test5_arrow.txt", "test4_noline.txt"][fi % 3]
            lists[name].append(f"/driver_100_30frame/{clip}/{frame}.jpg")
    (src / "list" / "test_split").mkdir(parents=True)
    for name, rows in lists.items():
        (src / "list" / "test_split" / name).write_text("\n".join(rows) + "\n", encoding="utf-8")
    return src, dev[:2], test[:3]


def run_dataset_checks(tmp: Path, repo: Path, own_data: Path, check, quiet) -> None:
    from .annotations import AnnotationStore
    from .core import LabelStore, Paths, ToolError, Trip, list_trip_ids, load_action_rules, prefill, read_csv
    from .imagesets import combine, init_workspace, near_duplicates_across_split
    from .packages import build_packages, import_results
    from .server import ImageApp, make_handler, QuietServer

    (tmp / "ws").mkdir(exist_ok=True)
    bdd_src = make_bdd(tmp / "datasets")
    pb = init_workspace(repo, tmp / "ws" / "bdd100k", "bdd100k", str(bdd_src), log=quiet)
    cands = read_csv(pb.scan_csv("bdd100k_val"))
    pools = {c["pool"] for c in cands}
    yellow = [c for c in cands if "yellow_solid" in c["hints"].split(";")]
    ybox = json.loads(yellow[0]["boxes"]).get("yellow_solid", []) if yellow else []
    check(pb.collection == "bdd100k" and pb.labels_dir.name == "bdd100k" and len(cands) == 24 and pools == {"dev", "test"}
          and len(ybox) == 1 and ybox[0][3] >= 700,
          f"images init (BDD100K): own workspace and label folder, {len(cands)} images indexed, both pools, the two edges of a line merged into one suggested box")

    app = ImageApp(pb, Trip(pb, "bdd100k_val"), "selftest")
    q_dev = app.candidates({"pool": "dev", "hide": "1"})
    q_y = app.candidates({"pool": "all", "hint": "yellow_solid"})
    picks = {}
    for g, hint in (("yellow", "yellow_solid"), ("dashed", "white_dashed"), ("arrow", "crosswalk"), ("degraded", "no_lane")):
        c = app.candidates({"pool": "test", "hint": hint})["items"][0]
        picks[g] = app.pick(c["cand_id"], g)["row"]
    qt = app.quota()
    yrow = picks["yellow"]
    ok_copy = (pb.data / yrow["source_path"]).exists() and yrow["image_id"].startswith("bdd100k_val__")
    check(q_dev["total"] + app.candidates({"pool": "test", "hide": "0"})["total"] == 24 and q_y["total"] == 6 and ok_copy
          and json.loads(yrow["box_hints"]) and [r["test_have"] for r in qt["rows"]] == [0, 1, 1, 1, 1],
          "pick: filters by pool and hint, the picked image is copied into the workspace with a suggested box, quota counted per cell")

    table = load_action_rules(pb)
    sug = prefill(table, "US", "yellow_solid", "", "", "full")
    box = json.loads(yrow["box_hints"])[0]
    out = app.save_label(yrow["image_id"], {"marking_type": "yellow_solid", "position": "left", "visibility": "V2",
                                            "actions": sug["actions"], "accepted_rule_ids": sug["rule_ids"], "box": box}, "done")
    for g in ("dashed", "arrow"):
        app.save_label(picks[g]["image_id"], {"box": [600, 400, 800, 700]}, "box")
    check(out["row"]["label_status"] == "waiting" and not out["errors"], "label: a dataset image is labeled like an own frame")

    httpd = QuietServer(("127.0.0.1", 0), make_handler(app))
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    ok = True
    base = f"http://127.0.0.1:{port}"
    st = json.loads(urllib.request.urlopen(base + "/api/state", timeout=30).read())
    ok &= st["kind"] == "images" and st["set"]["dataset"] == "BDD100K" and len(st["labels"]) == 4
    cj = json.loads(urllib.request.urlopen(base + "/api/candidates?pool=test&hint=white_dashed", timeout=30).read())
    ok &= cj["total"] >= 1
    with urllib.request.urlopen(base + "/api/cand_image?c=" + cj["items"][0]["cand_id"] + "&w=320", timeout=30) as r:
        ok &= r.headers["Content-Type"].startswith("image/jpeg")
    with urllib.request.urlopen(base + "/static/pick.css", timeout=30) as r:
        ok &= r.status == 200
    httpd.shutdown()
    httpd.server_close()
    check(ok, "web app (dataset mode): state, candidate list, candidate image and page files are served")

    zips = build_packages(pb, ["Alice", "Bob"], practice=1, log=quiet)
    import zipfile
    page = zipfile.ZipFile(zips[0]).read([n for n in zipfile.ZipFile(zips[0]).namelist() if n.endswith("data.js")][0]).decode()
    reg = read_csv(pb.packages_csv)
    out_dir = tmp / "returned_bdd"
    out_dir.mkdir()
    for r in reg:
        items = []
        for iid in [i for i in r["items"].split(";") if i]:
            items.append({"image_id": iid, "status": "done", "unsure": False, "comment": "", "privacy_boxes": [],
                          "saved_utc": "2026-10-22T10:00:00Z",
                          "fields": {"marking_type": "yellow_solid", "position": "left", "visibility": "V2",
                                     "actions": sug["actions"], "accepted_rule_ids": sug["rule_ids"]}})
        (out_dir / f"results_{r['annotator']}.json").write_text(json.dumps(
            {"format": "lane-label-results-v1", "package_id": r["package_id"], "annotator": r["annotator"],
             "exported_utc": "2026-10-22T10:00:00Z", "results": items}), encoding="utf-8")
    import_results(pb, [str(out_dir)], log=quiet)
    final = {r["image_id"]: r["label_status"] for r in read_csv(pb.labels_csv("bdd100k_val"))}
    check(len(zips) == 2 and "BDD100K images: Copyright" in page and final[yrow["image_id"]] == "done"
          and all(z.parent == pb.packages_dir for z in zips) and pb.packages_dir != Paths.discover(repo, own_data).packages_dir,
          "package and import (BDD100K): zips and results stay in the BDD100K workspace; an agreed label becomes final")

    cu_src, dev_clips, test_clips = make_culane(tmp / "datasets")
    pc = init_workspace(repo, tmp / "ws" / "culane", "culane", str(cu_src), log=quiet)
    capp = ImageApp(pc, Trip(pc, "culane_test"), "selftest")
    clip = f"driver_100_30frame/{test_clips[0]}"
    same = [c for c in capp.picker.cands if c["clip_id"] == clip]
    r1 = capp.pick(same[0]["cand_id"], "solid")["row"]
    capp.pick(same[1]["cand_id"], "solid")
    try:
        capp.pick(same[2]["cand_id"], "solid")
        third = "allowed"
    except ToolError:
        third = "refused"
    hints = json.loads(r1["box_hints"])
    check(pc.labels_dir.name == "culane" and third == "refused" and len(hints) == 2 and hints[0][0] < hints[1][0],
          "images init (CULane) and pick: at most 2 test images per clip; our lane's two boundaries are suggested as boxes")

    dev_c = next(c for c in capp.picker.cands if c["pool"] == "dev")
    rd = capp.pick(dev_c["cand_id"], "dashed")["row"]
    import shutil
    shutil.copy(pc.data / rd["source_path"], pc.data / r1["source_path"])  # a dev image that looks like a test image
    dups = near_duplicates_across_split(pc, LabelStore(pc.labels_csv("culane_test")).all())
    capp.save_label(r1["image_id"], {"box": hints[0]}, "box")
    zc = build_packages(pc, ["Chen"], practice=0, log=quiet)
    data_js = zipfile.ZipFile(zc[0]).read([n for n in zipfile.ZipFile(zc[0]).namelist() if n.endswith("data.js")][0]).decode()
    check(any(a == rd["image_id"] and b == r1["image_id"] for a, b, _ in dups) and "CULane images" in data_js,
          "split check flags a development image that looks like a test image; CULane packages carry the no-sharing notice")

    res = combine(repo, [str(own_data), str(pb.data), str(pc.data)], log=quiet)
    rows = read_csv(repo / "labels" / "labels.csv")
    splits = read_csv(repo / "labels" / "split_v1.csv")
    paths_ok = all((Path(res["root"]) / r["image_path"]).exists() for r in rows)
    cols = {"own_video", "bdd100k"} <= {r["collection"] for r in rows}
    check(rows and paths_ok and cols and len(splits) == len(rows),
          f"combine: {len(rows)} final labels from every workspace in labels/labels.csv and split_v1.csv, image paths resolve")

    from .resplit import resplit
    po = Paths.discover(repo, own_data)
    own_trip = list_trip_ids(po)[0]
    before = {r["split"] for r in LabelStore(po.labels_csv(own_trip)).all()}
    rs = resplit(po, own_trip, "dev", "selftest: used while developing the prompt", log=quiet)
    combine(repo, [str(own_data), str(pb.data), str(pc.data)], log=quiet)
    v2 = read_csv(repo / "labels" / "split_v2.csv")
    own_rows = [r for r in v2 if r["collection"] == "own_video"]
    check(before == {"test"} and own_rows and all(r["split"] == "dev" for r in own_rows) and (repo / "labels" / "split_v1.csv").exists()
          and read_csv(repo / "labels" / "split_changes.csv")[0]["to_split"] == "dev" and rs["labels_changed"] == len(own_rows),
          "resplit: a whole own-video drive moves to dev, the change is logged, combine writes split_v2.csv and keeps v1")
    chk = json.loads((repo / "labels" / "split_check_v2.json").read_text(encoding="utf-8"))
    cov = read_csv(repo / "labels" / "coverage_v2.csv")
    check(chk["clips_on_both_sides"] == [] and chk["split_changes"] and chk["images_hashed"] == len(v2)
          and sum(int(r["images"]) for r in cov) == len(v2) and all(int(r["clips"]) >= 1 for r in cov),
          "combine saves the separation check (clips, dHash, prompt examples, moves) and usable counts per type with clip counts")
    sup = read_csv(repo / "labels" / "candidate_supply.csv")
    check(sup and {"bdd100k", "culane"} <= {r["collection"] for r in sup} and all(int(r["clips"]) <= int(r["images"]) for r in sup),
          "combine writes what the datasets could still supply: candidates and distinct clips per pool and hint")
