"""Lane mode of the labeling tool (Milestone 5): label my whole lane per image, locally or in offline packages.

The main labeling tool (python main.py label --data <workspace> label) shows this page in its tabs ② and ③ and makes
lane packages in tab ④. The commands below do the same without the main tool:

  python main.py label --data <workspace> lanes [set]            open only the lane labeling page (as the owner)
  python main.py label --data <workspace> lanes-package --to ann01,ann02 [--max N]
  python main.py label --data <workspace> lanes-import results_*.json
  python main.py label --data <workspace> lanes-status           counts, and agreement between annotators

The images are the kept frames of each set. Every annotator's lane label is its own row in
<set>.lane_annotations.csv; the final lane label (<set>.lanes.csv) comes from two agreeing annotations or from the
owner's decision (reasoning_drive/labeling/lanes.py). The page shows the rule passages of the image's region with their
translation, suggests the actions from regulations/<CODE>/lane_action_rules.json, and for BDD100K and CULane images shows the
boundary lines of the dataset's own lane annotation as a starting point.
"""
from __future__ import annotations

import json
import shutil
import tempfile
import threading
import webbrowser
import zipfile
from collections import Counter, defaultdict
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import __version__
from .annotations import annotator_code, load_annotators
from .core import OWNER, LabelStore, Paths, ToolError, Trip, list_trip_ids, read_csv, utc_now, write_csv
from .lanes import (LANE_FINAL, LaneAnnotationStore, LaneStore, adjudicate_lane, annotation_row, dataset_suggestion,
                    lane_agreement, lane_annotations_csv, lane_differences, lane_prefill, lane_required, lanes_csv, load_lane_rules,
                    load_lane_schema, merge_lanes, remove_lane_image, seed_lane_rows, validate_lane, write_lane_agreement)
from .packages import LICENSE_NOTES, _passages_for_page, _trip_of

WEB_DIR = Path(__file__).resolve().parent / "web"
PACKAGE_FORMAT = "lane-task-package-v1"
RESULTS_FORMAT = "lane-task-results-v1"
LANE_PACKAGE_COLUMNS = ["package_id", "batch", "annotator", "created_utc", "n_items", "items", "status", "imported_utc", "done", "draft", "unsure"]


def lane_packages_csv(paths: Paths) -> Path:
    return paths.labels_dir / "lane_packages.csv"


def _page_payload(paths: Paths) -> dict:
    return {"schema": load_lane_schema(paths.repo), "rules": load_lane_rules(paths.repo), "passages": _passages_for_page(paths)}


class LaneApp:
    """The state behind the lane page: one data folder, its image sets, one annotator (the owner).

    Used on its own (python main.py label lanes) and inside the main labeling tool, which passes remove_hook so that an image
    can be removed from the set on the lane page."""

    def __init__(self, paths: Paths, annotator: str = OWNER, set_ids: list[str] | None = None, remove_hook=None):
        self.paths, self.annotator = paths, annotator
        self.set_ids = set_ids or list_trip_ids(paths)
        if not self.set_ids:
            raise ToolError(f"No image set or trip in {paths.data}.")
        self.trips = {s: Trip(paths, s) for s in self.set_ids}
        self.remove_hook = remove_hook
        self.lock = threading.Lock()
        self._seed()
        self.static = _page_payload(paths)
        self.rule_ids = {r: {p["rule_id"] for p in self.static["passages"].get(r, [])} for r in self.static["passages"]}

    def _seed(self) -> None:
        """Frames kept or picked since the last call get their lane rows."""
        with self.lock:
            for s in self.set_ids:
                seed_lane_rows(self.paths, s)

    def _stores(self, sid: str):
        return LaneStore(lanes_csv(self.paths, sid)), LaneAnnotationStore(lane_annotations_csv(self.paths, sid))

    def counts(self) -> dict:
        self._seed()
        c = Counter()
        for sid in self.set_ids:
            lanes, anns = self._stores(sid)
            for r in lanes.all():
                c[r.get("lane_status") or "kept"] += 1
                mine = anns.get(r["image_id"], self.annotator)
                c["mine_done"] += bool(mine and mine.get("status") == "done")
                c["images"] += 1
        return dict(c)

    def remove(self, image_id: str) -> dict:
        if self.remove_hook is None:
            raise ToolError("Images are removed in the main labeling tool (python main.py label label).")
        sid = _trip_of(image_id)
        if sid not in self.trips:
            raise ToolError(f"Unknown image {image_id}")
        self.remove_hook(image_id)
        with self.lock:
            remove_lane_image(self.paths, sid, image_id)
        return {"ok": True}

    def state(self) -> dict:
        self._seed()
        items = []
        for sid in self.set_ids:
            lanes, anns = self._stores(sid)
            frames = LabelStore(self.paths.labels_csv(sid))
            for r in sorted(lanes.all(), key=lambda r: (r.get("split", ""), r["image_id"])):
                mine = anns.get(r["image_id"], self.annotator)
                fr = frames.get(r["image_id"]) or {}
                items.append({"image_id": r["image_id"], "set_id": sid, "region": r["region"], "dataset": r.get("dataset", ""),
                              "split": r.get("split", ""), "status": r.get("lane_status") or "kept",
                              "mine": (mine or {}).get("status", ""), "n_done": sum(1 for a in anns.for_image(r["image_id"]) if a["status"] == "done"),
                              "width": int(float(r.get("width") or fr.get("width") or 0)), "height": int(float(r.get("height") or fr.get("height") or 0)),
                              "marking_hint": fr.get("marking_type", "")})
        counts = Counter(it["status"] for it in items)
        counts.update(mine_done=sum(it["mine"] == "done" for it in items), images=len(items))
        return {"mode": "server", "annotator": self.annotator, "data": str(self.paths.data), "collection": self.paths.collection,
                "items": items, "counts": dict(counts), "can_remove": self.remove_hook is not None, **self.static}

    def item(self, image_id: str) -> dict:
        sid = _trip_of(image_id)
        if sid not in self.trips:
            raise ToolError(f"Unknown image {image_id}")
        lanes, anns = self._stores(sid)
        row = lanes.get(image_id)
        if row is None:
            raise ToolError(f"Unknown image {image_id}")
        frame = LabelStore(self.paths.labels_csv(sid)).get(image_id) or {}
        sug = dataset_suggestion(self.paths, self.trips[sid], {**frame, **row}) if self.paths.collection in ("bdd100k", "culane") else {}
        others = [a for a in anns.for_image(image_id) if a["annotator"] != self.annotator]
        mine = anns.get(image_id, self.annotator)
        diff = sorted({f for a in anns.for_image(image_id) for b in anns.for_image(image_id) if a is not b for f in lane_differences(a, b)})
        return {"final": row, "mine": mine, "others": others if row.get("lane_status") in ("conflict", "done") else
                [{"annotator": a["annotator"], "status": a["status"]} for a in others],
                "differences": diff, "suggestion": sug}

    def image(self, image_id: str) -> bytes:
        sid = _trip_of(image_id)
        lanes, _ = self._stores(sid)
        row = lanes.get(image_id)
        if row is None:
            raise ToolError(f"Unknown image {image_id}")
        p = self.paths.data / row["source_path"]
        if not p.exists():
            raise ToolError(f"Image missing: {p}")
        return p.read_bytes()

    def check(self, region: str, fields: dict) -> dict:
        errors, warnings = validate_lane(fields, self.static["schema"], self.rule_ids.get(region, set()))
        pre = lane_prefill(self.static["rules"], self.static["schema"], region, fields)
        return {"errors": errors, "warnings": warnings, "prefill": pre}

    def save(self, image_id: str, fields: dict, status: str, unsure: bool = False, comment: str = "") -> dict:
        sid = _trip_of(image_id)
        with self.lock:
            lanes, anns = self._stores(sid)
            row = lanes.get(image_id)
            if row is None:
                raise ToolError(f"Unknown image {image_id}")
            res = self.check(row["region"], fields)
            if status == "done" and res["errors"] and not unsure:
                raise ToolError("Not saved as done: " + "; ".join(res["errors"]))
            anns.put(annotation_row(image_id, self.annotator, fields, "done" if status == "done" else "draft", unsure=unsure, comment=comment))
            anns.save()
            counts = merge_lanes(self.paths, self.trips[sid])
            final = LaneStore(lanes_csv(self.paths, sid)).get(image_id)
        return {"status": final.get("lane_status"), "counts": dict(counts), "warnings": res["warnings"]}

    def adjudicate(self, image_id: str, choice: str, fields: dict | None, note: str) -> dict:
        with self.lock:
            item = adjudicate_lane(self.paths, self.trips[_trip_of(image_id)], image_id, choice, fields, note, self.annotator)
        return {"status": item["lane_status"], "final_source": item.get("final_source", "")}

    def agreement(self) -> dict:
        return lane_agreement(self.paths, self.set_ids)


def _json_reply(obj) -> tuple:
    return 200, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8"


def lane_route(app: LaneApp, method: str, path: str, q: dict, body: dict | None):
    """Answer one request of the lane page: (status, body, content type), or None for an unknown path.

    Shared by the lanes server (paths from /) and the main labeling tool (the same paths under /lanes/). The page
    uses relative addresses, so it works in both places."""
    if method == "GET":
        if path in ("/", "/index.html"):
            return 200, (WEB_DIR / "lanes.html").read_bytes(), "text/html; charset=utf-8"
        if path in ("/lanes.js", "/lanes.css"):
            ctype = "text/javascript" if path.endswith(".js") else "text/css"
            return 200, (WEB_DIR / path.lstrip("/")).read_bytes(), ctype + "; charset=utf-8"
        if path == "/api/state":
            return _json_reply(app.state())
        if path == "/api/item":
            return _json_reply(app.item(q["id"]))
        if path == "/api/image":
            return 200, app.image(q["id"]), "image/jpeg"
        if path == "/api/agreement":
            return _json_reply(app.agreement())
        return None
    body = body or {}
    if path == "/api/check":
        return _json_reply(app.check(body["region"], body.get("fields", {})))
    if path == "/api/save":
        return _json_reply(app.save(body["image_id"], body.get("fields", {}), body.get("status", "draft"),
                                    bool(body.get("unsure")), str(body.get("comment") or "")))
    if path == "/api/adjudicate":
        return _json_reply(app.adjudicate(body["image_id"], body.get("choice", ""), body.get("fields"), body.get("note", "")))
    if path == "/api/remove":
        return _json_reply(app.remove(body["image_id"]))
    return None


def make_handler(app: LaneApp):
    class Handler(BaseHTTPRequestHandler):
        server_version = "video_tool_lanes"

        def log_message(self, fmt, *args):
            pass

        def _send(self, code: int, body: bytes, ctype: str):
            try:
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def _json(self, obj, code: int = 200):
            self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

        def _error(self, e: Exception):
            if not isinstance(e, ToolError):
                import traceback
                traceback.print_exc()
            self._json({"error": str(e) if isinstance(e, ToolError) else f"{type(e).__name__}: {e}"}, 400 if isinstance(e, ToolError) else 500)

        def do_GET(self):
            u = urlparse(self.path)
            q = {k: v[0] for k, v in parse_qs(u.query).items()}
            try:
                r = lane_route(app, "GET", u.path, q, None)
                return self._send(*r) if r else self._send(404, b"not found", "text/plain")
            except Exception as e:  # noqa: BLE001
                return self._error(e)

        def do_POST(self):
            u = urlparse(self.path)
            try:
                body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
                r = lane_route(app, "POST", u.path, {}, body)
                return self._send(*r) if r else self._send(404, b"not found", "text/plain")
            except Exception as e:  # noqa: BLE001
                return self._error(e)

    return Handler


def serve_lanes(paths: Paths, set_ids: list[str] | None = None, annotator: str = OWNER, port: int = 8766,
                open_browser: bool = True, log=print) -> None:
    from .server import QuietServer
    app = LaneApp(paths, annotator, set_ids)
    httpd = None
    for p in range(port, port + 20):
        try:
            httpd = QuietServer(("127.0.0.1", p), make_handler(app))
            port = p
            break
        except OSError:
            continue
    if httpd is None:
        raise ToolError(f"No free port between {port} and {port + 19}.")
    url = f"http://127.0.0.1:{port}/"
    log(f"Lane labeling for {', '.join(app.set_ids)} is running at {url} (annotator {annotator}).")
    log("Everything is saved as you go. Press Ctrl+C here to stop.")
    if open_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        log("\nStopped. Lane labels are in " + str(paths.labels_dir))
    finally:
        httpd.server_close()


# ------------------------------------------------------------------ offline packages for helpers

def _lane_page_html() -> str:
    read = lambda n: (WEB_DIR / n).read_text(encoding="utf-8")  # noqa: E731
    html = read("lanes.html")
    html = html.replace('<link rel="stylesheet" href="lanes.css">', "<style>\n" + read("lanes.css") + "\n</style>")
    html = html.replace('<script src="lanes.js"></script>', '<script src="data.js"></script>\n<script>\n' + read("lanes.js") + "\n</script>")
    return html


def build_lane_packages(paths: Paths, names: list[str], set_ids: list[str] | None = None, max_per_person: int | None = None,
                        split: str | None = None, log=print) -> list[Path]:
    """One zip per helper with the images that still need independent lane labels (two per image, the owner's count)."""
    names = [n.strip() for n in names if n.strip()]
    if not names:
        raise ToolError("Give at least one helper name, e.g. --to ann01,ann02")
    codes = {n: (n if n in load_annotators(paths) else annotator_code(paths, n)) for n in names}
    registry = read_csv(lane_packages_csv(paths))
    outstanding = defaultdict(set)
    for r in registry:
        if r["status"] in ("sent", "partial"):
            for iid in r["items"].split(";"):
                if iid:
                    outstanding[iid].add(r["annotator"])
    pool = []
    for sid in set_ids or list_trip_ids(paths):
        trip = Trip(paths, sid)
        seed_lane_rows(paths, sid)
        lanes, anns = LaneStore(lanes_csv(paths, sid)), LaneAnnotationStore(lane_annotations_csv(paths, sid))
        for item in sorted(lanes.all(), key=lambda r: r["image_id"]):
            if item.get("lane_status") in ("done", "conflict", "excluded") or (split and item.get("split") != split):
                continue
            have = {a["annotator"] for a in anns.for_image(item["image_id"]) if a["status"] == "done"}
            busy = have | outstanding[item["image_id"]]
            need = lane_required(trip.meta, item.get("split", "")) - len(busy)
            if need > 0:
                pool.append((sid, item, need, busy))
    if not pool:
        raise ToolError("Nothing to send: every image already has enough lane labels or an open package.")
    load = Counter({c: 0 for c in codes.values()})
    assigned: dict[str, list] = defaultdict(list)
    for sid, item, need, busy in pool:
        cands = sorted((c for c in codes.values() if c not in busy), key=lambda c: (load[c], c))
        if max_per_person:
            cands = [c for c in cands if load[c] < max_per_person]
        for c in cands[:need]:
            assigned[c].append((sid, item))
            load[c] += 1
    static = _page_payload(paths)
    day = __import__("datetime").datetime.now().strftime("%Y%m%d")
    batch = next(f"L{day}{c}" for c in "abcdefghijklmnopqrstuvwxyz" if f"L{day}{c}" not in {r["batch"] for r in registry})
    paths.packages_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for name, code in codes.items():
        items = assigned.get(code, [])
        if not items:
            log(f"  {name} ({code}): nothing to label in this batch.")
            continue
        package_id = f"{batch}_{code}"
        payload = {"format": PACKAGE_FORMAT, "tool_version": __version__, "package_id": package_id, "annotator": code,
                   "created_utc": utc_now(), "mode": "offline", "items": [], "notices": [], **static}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / f"lane_task_{package_id}"
            (root / "images").mkdir(parents=True)
            datasets = set()
            for sid, item in items:
                src = paths.data / item["source_path"]
                if not src.exists():
                    raise ToolError(f"Image missing: {src}")
                shutil.copy(src, root / "images" / f"{item['image_id']}.jpg")
                frame = LabelStore(paths.labels_csv(sid)).get(item["image_id"]) or {}
                sug = dataset_suggestion(paths, Trip(paths, sid), {**frame, **item}) if paths.collection in ("bdd100k", "culane") else {}
                payload["items"].append({"image_id": item["image_id"], "region": item["region"], "dataset": item.get("dataset", ""),
                                         "file": f"images/{item['image_id']}.jpg", "width": int(float(item.get("width") or 0)),
                                         "height": int(float(item.get("height") or 0)), "suggestion": sug})
                datasets.add(item.get("dataset", ""))
            payload["notices"] = [LICENSE_NOTES[d] for d in sorted(datasets) if d in LICENSE_NOTES]
            (root / "data.js").write_text("window.LANE_TASK_PACKAGE = " + json.dumps(payload, ensure_ascii=False) + ";\n", encoding="utf-8")
            (root / "index.html").write_text(_lane_page_html(), encoding="utf-8")
            (root / "README.txt").write_text(
                "Lane labeling / 车道标注\n\n1. Unzip the folder, then double-click index.html (works offline).\n   解压后双击 index.html（无需联网）。\n"
                "2. Read the guide at the top of the page, then label every image.\n   先看页面上方的说明，再逐张标注。\n"
                "3. Click \"Export results\" and send back the results_*.json file. Your work is also kept in this browser.\n"
                "   点击“导出结果”，把 results_*.json 文件发回来。进度也会保存在浏览器里。\n"
                "4. Do not share, upload or screenshot the images; delete the folder when you are done.\n"
                "   请勿转发、上传或截图图片；完成后删除整个文件夹。\n\n" + "\n".join(payload["notices"]) + "\n", encoding="utf-8")
            zpath = paths.packages_dir / f"{package_id}.zip"
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
                for f in sorted(root.rglob("*")):
                    if f.is_file():
                        z.write(f, f.relative_to(root.parent).as_posix())
        registry.append({"package_id": package_id, "batch": batch, "annotator": code, "created_utc": utc_now(), "n_items": len(items),
                         "items": ";".join(it["image_id"] for _, it in items), "status": "sent"})
        made.append(zpath)
        log(f"  {name} ({code}): {len(items)} images -> {zpath}")
    write_csv(lane_packages_csv(paths), registry, LANE_PACKAGE_COLUMNS)
    return made


def _json_files(inputs: list[str]) -> list[Path]:
    files: list[Path] = []
    for i in inputs:
        p = Path(i).expanduser()
        files += sorted(f for f in p.glob("*.json") if not f.name.startswith("._")) if p.is_dir() else [p]
    return files


def import_lane_results(paths: Paths, inputs: list[str], log=print) -> dict:
    """Read helpers' results files into <set>.lane_annotations.csv and merge.

    Returns {"counts": final lane statuses of the touched sets, "files": [(file name, annotator, per-file counts)]}."""
    files = _json_files(inputs)
    per_file: list[tuple] = []
    registry = read_csv(lane_packages_csv(paths))
    by_id = {r["package_id"]: r for r in registry}
    schema = load_lane_schema(paths.repo)
    passages = _passages_for_page(paths)
    rule_ids = {r: {p["rule_id"] for p in passages.get(r, [])} for r in passages}
    stores: dict[str, LaneAnnotationStore] = {}
    touched = set()
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            log(f"  x {f.name}: not a lane results file")
            continue
        pkg = by_id.get(data.get("package_id"))
        if data.get("format") != RESULTS_FORMAT or not pkg or data.get("annotator") != pkg["annotator"]:
            log(f"  x {f.name}: not a results file of a known lane package")
            continue
        allowed = set(pkg["items"].split(";"))
        st = Counter()
        for r in data.get("results", []):
            iid = r.get("image_id")
            if iid not in allowed:
                st["skipped"] += 1
                continue
            sid = _trip_of(iid)
            store = stores.setdefault(sid, LaneAnnotationStore(lane_annotations_csv(paths, sid)))
            old = store.get(iid, pkg["annotator"])
            saved = r.get("saved_utc") or data.get("exported_utc") or utc_now()
            if old and old.get("saved_utc", "") >= saved:
                st["unchanged"] += 1
                continue
            fields = {k: str(v) for k, v in (r.get("fields") or {}).items() if k in LANE_FINAL}
            region = (LaneStore(lanes_csv(paths, sid)).get(iid) or {}).get("region", "")
            status = "done" if r.get("status") == "done" else "draft"
            errors, _ = validate_lane(annotation_row(iid, pkg["annotator"], fields, status), schema, rule_ids.get(region, set()))
            if status == "done" and errors and not r.get("unsure"):
                status, st["invalid"] = "draft", st["invalid"] + 1
            row = annotation_row(iid, pkg["annotator"], fields, status, source="package", package_id=pkg["package_id"],
                                 unsure=bool(r.get("unsure")), comment=str(r.get("comment") or "")[:500])
            row["saved_utc"] = saved
            store.put(row)
            touched.add(sid)
            st[status] += 1
        def ann(iid, code=pkg["annotator"]):
            s = stores.get(_trip_of(iid)) or LaneAnnotationStore(lane_annotations_csv(paths, _trip_of(iid)))
            return s.get(iid, code) or {}
        n_done = sum(1 for iid in allowed if iid and ann(iid).get("status") == "done")
        st["unsure"] = sum(1 for r in data.get("results", []) if r.get("unsure") and r.get("image_id") in allowed)
        pkg.update({"status": "complete" if n_done >= len([i for i in allowed if i]) else "partial", "imported_utc": utc_now(),
                    "done": n_done, "draft": st["draft"], "unsure": st["unsure"]})
        per_file.append((f.name, pkg["annotator"], dict(st)))
        log(f"  ok {f.name}: {pkg['annotator']} done {st['done']}, draft {st['draft']}" + (f", invalid {st['invalid']}" if st["invalid"] else ""))
    for s in stores.values():
        s.save()
    counts = Counter()
    for sid in touched:
        counts += merge_lanes(paths, Trip(paths, sid))
    write_csv(lane_packages_csv(paths), registry, LANE_PACKAGE_COLUMNS)
    if counts:
        log(f"Final lane labels now: done {counts['done']}, conflict {counts['conflict']}, waiting {counts['waiting']}, not started {counts['kept']}.")
    ag = write_lane_agreement(paths)
    if ag["items"]:
        log(f"Agreement of two annotators on {ag['items']} images: all compared fields equal on {ag['all_fields_agree']:.0%} (datasets/<CODE>/<collection>/lane_agreement.csv).")
    return {"counts": dict(counts), "files": per_file}


def lane_status_report(paths: Paths, log=print) -> dict:
    out = {}
    for sid in list_trip_ids(paths):
        seed_lane_rows(paths, sid)
        c = Counter(r.get("lane_status") or "kept" for r in LaneStore(lanes_csv(paths, sid)).all())
        out[sid] = dict(c)
        log(f"{sid}: " + ", ".join(f"{k} {c[k]}" for k in ("kept", "waiting", "conflict", "done", "excluded")))
    ag = write_lane_agreement(paths)
    if ag["items"]:
        log(f"Agreement on {ag['items']} doubly labeled images: all fields equal on {ag['all_fields_agree']:.0%}")
        for f in ag["fields"]:
            if f["items"]:
                log(f"  {f['field']:24s} {f['percent_agreement']:.0%}  kappa {f['fleiss_kappa'] if f['fleiss_kappa'] != '' else '-'}")
    return out


# ------------------------------------------------------------------ share tab of the main labeling tool

def lane_open_cells(paths: Paths, regions) -> list[dict]:
    """Cells of regulations/<CODE>/lane_action_rules.json left empty: conventions to settle before packages go out."""
    table = load_lane_rules(paths.repo)
    out = []
    for region in sorted(regions):
        t = table.get(region) or {}
        for row in t.get("boundary", []):
            if row.get("change") == "":
                out.append({"region": region, "kind": "boundary", "when": row.get("when", {}), "token": "",
                            "actions": ["change_left", "change_right"], "note": row.get("note", ""), "note_zh": row.get("note_zh", "")})
        for tok, entry in (t.get("markings") or {}).items():
            empty = [a for a, v in (entry.get("actions") or {}).items() if v == ""]
            if empty:
                out.append({"region": region, "kind": "marking", "when": {}, "token": tok, "actions": empty,
                            "note": entry.get("note", ""), "note_zh": entry.get("note_zh", "")})
    return out


def lane_share_state(paths: Paths, set_ids: list[str] | None = None) -> dict:
    """What the share tab shows: per set how many lane labels are still needed, the lane packages, earlier helpers."""
    set_ids = set_ids or list_trip_ids(paths)
    registry = read_csv(lane_packages_csv(paths))
    outstanding = defaultdict(set)
    for r in registry:
        if r.get("status") in ("sent", "partial"):
            for iid in (r.get("items") or "").split(";"):
                if iid:
                    outstanding[iid].add(r["annotator"])
    trips, regions = [], set()
    for sid in set_ids:
        trip = Trip(paths, sid)
        regions.add(trip.region)
        seed_lane_rows(paths, sid)
        lanes, anns = LaneStore(lanes_csv(paths, sid)), LaneAnnotationStore(lane_annotations_csv(paths, sid))
        row = {"trip_id": sid, "region": trip.region, "required": trip.meta.get("lane_annotators_required", trip.meta.get("annotators_required", 2)), "kept": 0, "need": 0, "outstanding": 0, "mine_done": 0,
               "waiting": 0, "conflict": 0, "done": 0, "excluded": 0}
        for item in lanes.all():
            iid, st = item["image_id"], item.get("lane_status") or "kept"
            if st == "excluded":
                row["excluded"] += 1
                continue
            row["kept"] += 1
            if st in ("waiting", "conflict", "done"):
                row[st] += 1
            done_by = {a["annotator"] for a in anns.for_image(iid) if a["status"] == "done"}
            mine = anns.get(iid, OWNER)
            row["mine_done"] += bool(mine and mine["status"] == "done" and mine.get("unsure") != "1")
            out = outstanding.get(iid, set()) - done_by
            row["outstanding"] += len(out)
            if st not in ("done", "conflict"):
                row["need"] += max(0, lane_required(trip.meta, item.get("split", "")) - len(done_by) - len(out))
        trips.append(row)
    names = load_annotators(paths)
    packages = []
    for r in registry:
        z = paths.packages_dir / f"{r['package_id']}.zip"
        packages.append({**{k: r.get(k, "") for k in ("package_id", "batch", "annotator", "created_utc", "status", "imported_utc", "done", "unsure")},
                         "practice_score": "", "name": names.get(r["annotator"], {}).get("name", ""),
                         "n_items": len([i for i in (r.get("items") or "").split(";") if i]),
                         "file": z.name if z.exists() else "", "size_bytes": z.stat().st_size if z.exists() else 0})
    return {"lane": True, "trips": trips, "packages": packages,
            "helpers": [{"code": c, "name": v.get("name", "")} for c, v in sorted(names.items())],
            "open_cells": lane_open_cells(paths, regions), "packages_dir": str(paths.packages_dir),
            "returned_dir": str(paths.data / "returned")}


def lane_make_packages(paths: Paths, names: list[str], set_ids: list[str] | None = None, max_per_person: int | None = None) -> dict:
    log: list[str] = []
    before = {r["package_id"] for r in read_csv(lane_packages_csv(paths))}
    try:
        build_lane_packages(paths, names, set_ids, max_per_person=max_per_person, log=log.append)
    except ToolError as e:
        return {"ok": False, "error": str(e), "log": log, "made": []}
    made = [p for p in lane_share_state(paths, set_ids)["packages"] if p["package_id"] not in before]
    return {"ok": True, "log": log, "made": made}


def import_any_results(paths: Paths, inputs: list[str], log=print) -> dict:
    """Import returned files of both kinds: lane packages and the earlier single-marking packages (by their format)."""
    lane, single = [], []
    for f in _json_files(inputs):
        try:
            fmt = json.loads(f.read_text(encoding="utf-8")).get("format", "")
        except (OSError, UnicodeDecodeError, json.JSONDecodeError, AttributeError):
            log(f"  x {f.name}: not a results file")
            continue
        (single if fmt == "lane-label-results-v1" else lane).append(str(f))
    if not lane and not single:
        raise ToolError("No results .json files found.")
    counts: Counter = Counter()
    files: list = []
    if lane:
        res = import_lane_results(paths, lane, log=log)
        counts.update(res["counts"])
        files += res["files"]
    if single:
        from .packages import import_results
        res = import_results(paths, single, log=log)
        files += [(f, code, dict(st)) for f, code, st in res.get("files", [])]
    return {"counts": dict(counts), "files": files}
