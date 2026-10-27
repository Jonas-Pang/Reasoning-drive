"""End-to-end check on a synthetic night video and two tiny synthetic datasets, in a temporary folder (your data is not touched)."""
from __future__ import annotations

import json
import shutil
import tempfile
import threading
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

import numpy as np

from . import synthetic
from .core import DEFAULT_REPO, Paths, Trip, load_action_rules, prefill, read_csv
from .video import VideoReader, read_image


def run(log=print) -> bool:
    results: list[tuple[bool, str]] = []

    def check(ok, text):
        results.append((bool(ok), text))
        log(("  PASS  " if ok else "  FAIL  ") + text)

    with tempfile.TemporaryDirectory(prefix="video_tool_selftest_") as tmp:
        tmp = Path(tmp)
        repo = tmp / "repo"
        for rel in ("rules/rule_passages.json", "config/label_schema.json", "config/action_rules.json"):
            (repo / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(DEFAULT_REPO / rel, repo / rel)
        paths = Paths.discover(repo, tmp / "data")
        quiet = lambda *a, **k: None  # noqa: E731

        log("Making a 45 s synthetic night video ...")
        video = synthetic.make_video(tmp / "in" / "20261016_213000_F.mp4", 45)

        from .ingest import ingest
        tid = ingest(paths, video, time_of_day="night", log=quiet)
        trip = Trip(paths, tid)
        check(tid == "fl_20261016_night_01" and trip.video_path.exists(), f"ingest: trip {tid}, video copied, SHA-256 recorded")

        from .scan import scan_trip
        summary = scan_trip(paths, trip, log=quiet)
        rows = read_csv(paths.scan_csv(tid))
        stop = [r for r in rows if 16 <= float(r["time_s"]) <= 24]
        drive = [r for r in rows if 2 <= float(r["time_s"]) <= 12 or 28 <= float(r["time_s"]) <= 44]
        stop_hidden = sum(r["stationary"] == "1" for r in stop) / len(stop)
        drive_shown = sum(r["candidate"] == "1" for r in drive) / len(drive)
        check(stop_hidden >= 0.8, f"scan: {stop_hidden:.0%} of the red-light stop is hidden")
        check(drive_shown >= 0.9, f"scan: {drive_shown:.0%} of the driving is shown ({summary['candidates']} of {summary['samples']} samples)")

        from .server import App, make_handler
        app = App(paths, trip, "selftest")
        f_arrow, f_plate = 33 * synthetic.FPS, 5 * synthetic.FPS
        res = app.keep(f_arrow)
        img_path = paths.data / res["row"]["source_path"]
        saved = read_image(img_path)
        check(saved.shape[:2] == (720, 1280), f"keep: frame {f_arrow} saved as {img_path.name} at 1280x720")
        ref = None
        rd = VideoReader(trip.video_path)
        for idx, fr in rd.iter_frames(f_arrow, f_arrow + 1, 1):
            ref = fr
        rd.close()
        diff = float(np.abs(saved.astype(np.int16) - ref.astype(np.int16)).mean())
        check(diff < 2.0, f"keep: saved frame equals the sequentially decoded frame (mean difference {diff:.2f})")

        app.set_masks([synthetic.OVERLAY_BOX])
        x1, y1, x2, y2 = synthetic.OVERLAY_BOX
        masked = read_image(img_path)[y1:y2, x1:x2]
        check(masked.mean() < 6, "masks: the burned-in date / speed / GPS overlay is blacked out in saved frames")

        table = load_action_rules(paths)
        sug = prefill(table, "US", "arrow", "straight_right", "", "full")
        out = app.save_label(res["row"]["image_id"], {
            "marking_type": "arrow", "arrow_type": "straight_right", "position": "in_ego_lane",
            "visibility": "V2", "actions": sug["actions"], "accepted_rule_ids": sug["rule_ids"],
            "box": [560, 470, 720, 560], "privacy_boxes": [],
        }, "done")
        check(out["row"]["label_status"] == "waiting" and not out["errors"],
              f"label: your arrow label is saved and waits for a second, independent label ({out['errors'] or 'no errors'})")

        res2 = app.keep(f_plate)
        near_ok = res2["near"] == []
        out2 = app.save_label(res2["row"]["image_id"], {"marking_type": "white_dashed", "box": [1000, 520, 1200, 700]}, "done")
        mine2 = [a for a in out2["annotations"] if a["annotator"] == "owner"][0]
        check(mine2["status"] == "draft" and out2["errors"], f"label: an unfinished label is kept as draft ({len(out2['errors'])} problems listed)")
        sug2 = prefill(table, "US", "white_dashed", "", "", "full")
        plate = [590, 460, 690, 500]
        out2 = app.save_label(res2["row"]["image_id"], {
            "marking_type": "white_dashed", "position": "right", "visibility": "V2", "actions": sug2["actions"],
            "accepted_rule_ids": sug2["rule_ids"], "privacy_boxes": [plate],
        }, "done")
        check(out2["row"]["label_status"] == "waiting" and near_ok, "label: dashed line with a privacy box over the plate is saved")
        res3 = app.keep(40 * synthetic.FPS)
        app.save_label(res3["row"]["image_id"], {"box": [1000, 520, 1200, 700]}, "box")

        sh = app.share_state()
        tr = sh["trips"][0]
        open_ok = isinstance(sh["open_cells"], list) and all(c["actions"] for c in sh["open_cells"])
        check(tr["boxed"] == 3 and tr["need"] == 4 and tr["mine_done"] == 2 and open_ok,
              f"share tab: 3 boxed frames need 4 more labels, 2 practice items, open conventions checked")
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(app))
        port = httpd.server_address[1]
        th = threading.Thread(target=httpd.serve_forever, daemon=True)
        th.start()
        ok = True
        for url, ctype in [("/", "text/html"), ("/static/app.js", "text/javascript"), ("/static/style.css", "text/css"),
                           ("/static/guide.js", "text/javascript"), ("/static/offline.css", "text/css"),
                           ("/static/i18n.js", "text/javascript"), ("/static/share.css", "text/css"), ("/api/share", "application/json"),
                           ("/api/state", "application/json"), (f"/api/preview?f={f_arrow}&w=640", "image/jpeg"),
                           (f"/api/image?id={res['row']['image_id']}&w=144", "image/jpeg")]:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}{url}", timeout=30) as r:
                ok &= r.status == 200 and r.headers["Content-Type"].startswith(ctype)
        state = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/api/state", timeout=30).read())
        ok &= len(state["labels"]) == 3 and len(state["scan"]) == summary["samples"] and len(state["annotations"]) == 2
        from .server import LOCK_FILE, running_instance
        (paths.data / LOCK_FILE).write_text(json.dumps({"port": port, "trip": trip.id}), encoding="utf-8")
        found = running_instance(paths)
        httpd.shutdown()
        httpd.server_close()
        check(ok, "web app: page, scripts, state, preview and saved images are served")
        check(found == f"http://127.0.0.1:{port}/" and running_instance(paths) is None,
              "a second window on the same data folder is refused; a lock left by a closed window is ignored")
        (paths.data / LOCK_FILE).unlink()
        app.close()

        # helpers: offline packages, results back, merge, adjudication
        from .packages import build_packages, import_results
        zips = build_packages(paths, ["Alice", "Bob"], practice=1, log=quiet)
        import zipfile
        reg = read_csv(paths.packages_csv)
        assigned = {r["annotator"]: [i for i in r["items"].split(";") if i] for r in reg}
        names = zipfile.ZipFile(zips[0]).namelist()
        page = zipfile.ZipFile(zips[0]).read([n for n in names if n.endswith("index.html")][0]).decode("utf-8")
        every = sorted(i for v in assigned.values() for i in v)
        need = sorted([res["row"]["image_id"], res2["row"]["image_id"], res3["row"]["image_id"], res3["row"]["image_id"]])
        check(len(zips) == 2 and every == need and "LANE_GUIDE" in page and "lane-label-results-v1" in page,
              f"package: 2 zips; frames you labeled get 1 more label, the box-only frame gets 2 ({sum(map(len, assigned.values()))} assignments)")
        check(set(assigned["ann01"]).isdisjoint({i for i in reg[0]["practice"].split(";") if i}),
              "package: practice items are never frames the same helper must label")
        out_dir = tmp / "returned"
        out_dir.mkdir()
        for r in reg:
            items_out = []
            for iid in assigned[r["annotator"]]:
                if iid == res["row"]["image_id"]:
                    f = {"marking_type": "arrow", "arrow_type": "straight_right", "position": "in_ego_lane", "visibility": "V2",
                         "actions": sug["actions"], "accepted_rule_ids": sug["rule_ids"]}
                else:
                    f = {"marking_type": "white_dashed", "position": "right", "visibility": "V1", "behavior_decidable": "yes",
                         "actions": sug2["actions"], "accepted_rule_ids": sug2["rule_ids"]}
                items_out.append({"image_id": iid, "status": "done", "unsure": False, "comment": "", "fields": f,
                                 "privacy_boxes": [], "saved_utc": "2026-10-18T10:00:00Z"})
            (out_dir / f"results_{r['annotator']}.json").write_text(json.dumps(
                {"format": "lane-label-results-v1", "package_id": r["package_id"], "annotator": r["annotator"],
                 "exported_utc": "2026-10-18T10:00:00Z", "results": items_out, "practice_score": "1/1"}), encoding="utf-8")
        import_results(paths, [str(out_dir)], log=quiet)
        final = {r["image_id"]: r for r in read_csv(paths.labels_csv(tid))}
        st = (final[res["row"]["image_id"]]["label_status"], final[res2["row"]["image_id"]]["label_status"], final[res3["row"]["image_id"]]["label_status"])
        check(st == ("done", "conflict", "done"), f"import: agreeing labels become final, a disagreement goes to adjudication {st}")
        from .annotations import AnnotationStore, adjudicate as adj
        from .core import LabelStore
        lab, anns = LabelStore(paths.labels_csv(tid)), AnnotationStore(paths.annotations_csv(tid))
        row = adj(lab, anns, res2["row"]["image_id"], "owner", None, "the gaps are visible when zoomed", "selftest", 2)
        lab.save()
        check(row["label_status"] == "done" and row["final_source"] == "adjudicated" and row["visibility"] == "V2",
              "adjudication: your decision becomes the final label, with the reason recorded")

        from .export import export_all, rebuild_trip
        export_all(paths, log=quiet)
        fig = paths.figures_dir(tid) / f"{res2['row']['image_id']}.jpg"
        orig = read_image(paths.data / res2["row"]["source_path"])
        blurred = read_image(fig)
        px1, py1, px2, py2 = plate
        before = float(orig[py1:py2, px1:px2].std())
        after = float(blurred[py1:py2, px1:px2].std())
        check(fig.exists() and after < 0.5 * before, f"export: plate blurred in the report copy (detail {before:.0f} -> {after:.0f})")
        check(all((paths.labels_dir / f).exists() for f in ("all_labels.csv", "all_annotations.csv", "summary.csv", "agreement.csv")),
              "export: all_labels, all_annotations, summary and agreement files written")
        n = rebuild_trip(paths, tid, log=quiet)
        check(n == 3 and read_image(img_path)[y1:y2, x1:x2].mean() < 6, "rebuild: frames re-created from the video with the same masks")

        rapp = App(paths, Trip(paths, tid), "selftest", recheck=True)
        ids = list(rapp.recheck.rows)
        check(len(ids) == 3, f"re-check: sample of {len(ids)} finished labels drawn")
        rapp.save_recheck(res["row"]["image_id"], {"marking_type": "arrow", "arrow_type": "straight_right", "position": "in_ego_lane",
                                                   "visibility": "V2", "actions": sug["actions"]}, "done")
        rapp.save_recheck(res2["row"]["image_id"], {"marking_type": "white_dashed", "position": "right", "visibility": "V1",
                                                    "behavior_decidable": "yes", "actions": sug2["actions"]}, "done")
        rapp.close()
        from .export import export_trip
        rep = export_trip(paths, tid, log=quiet)["agreement"]
        got = {r["marking_type"]: (r["changed"], r["rechecked"]) for r in rep}
        check(got == {"arrow": (0, 1), "white_dashed": (1, 1)}, f"re-check: agreement computed per type {got}")

        log("Making two tiny synthetic datasets (BDD100K and CULane layouts) ...")
        from .selftest_images import run_dataset_checks
        run_dataset_checks(tmp, repo, paths.data, check, quiet)

    passed = sum(ok for ok, _ in results)
    log(f"\n{passed}/{len(results)} checks passed." + ("" if passed == len(results) else "  Something is wrong; send this output."))
    return passed == len(results)
