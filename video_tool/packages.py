"""Offline labeling packages for helpers, and importing their results.

package: every frame that has a target box and still needs independent labels is assigned to
         helpers so that it gets `annotators_required` labels from different people (the owner's
         own labels count). Each helper gets one zip: index.html + data.js + images/ + README.
         The page works offline in any browser: no account, no server, no region limits.
import:  reads the results files the helpers send back, stores them as annotations under their
         code (ann01, ...), and recomputes the final labels (agreed / conflict / waiting).
"""
from __future__ import annotations

import json
import random
import shutil
import tempfile
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from . import __version__
from .annotations import (AnnotationStore, annotator_code, differences, fields_to_row, has_box, load_annotators,
                          merge_trip, required_for, write_agreement)
from .core import (ACTION_COLUMNS, ACTIONS, OWNER, LabelStore, Paths, ToolError, Trip, list_trip_ids,
                   load_action_rules, load_rule_passages, load_schema, read_csv, read_json, utc_now, validate_label,
                   write_csv)

PACKAGE_COLUMNS = ["package_id", "batch", "annotator", "created_utc", "n_items", "items", "practice",
                   "status", "imported_utc", "done", "draft", "unsure", "practice_score"]
WEB_DIR = Path(__file__).resolve().parent / "web"
RESULTS_FORMAT = "lane-label-results-v1"
PACKAGE_FORMAT = "lane-label-package-v1"

LICENSE_NOTES = {
    "BDD100K": "BDD100K images: Copyright (c) 2018 The Regents of the University of California. Educational, research and not-for-profit use only.",
    "CULane": ("CULane images (Pan et al., AAAI 2018): only for this labeling task. Do not share, upload or copy them, "
               "and delete this folder after you send back your results. "
               "CULane 图片仅用于本次标注：请勿转发、上传或复制，交回结果后请删除整个文件夹。"),
}


def _trip_of(image_id: str) -> str:
    """Trip or image set of an image: <set>__<image> for dataset images, <trip>_f<frame> for own frames."""
    if "__" in image_id:
        return image_id.split("__", 1)[0]
    return image_id.rsplit("_f", 1)[0]


def _translations(paths: Paths) -> dict:
    p = paths.repo / "config" / "rule_translations_zh.json"
    return read_json(p).get("translations", {}) if p.exists() else {}


def _type_names_zh(paths: Paths) -> dict:
    p = paths.repo / "config" / "rule_translations_zh.json"
    return read_json(p).get("marking_types", {}) if p.exists() else {}


def _passages_for_page(paths: Paths) -> dict:
    """Rule passages for the labeling pages: original text plus translation, and which one is which."""
    zh = _translations(paths)
    types_zh = _type_names_zh(paths)
    out = {}
    for region in ("US", "CN"):
        rows = []
        for p in load_rule_passages(paths, region):
            r = {k: p.get(k, "") for k in ("rule_id", "source", "section", "page", "marking_type", "text_en", "text_zh")}
            r["marking_type_zh"] = types_zh.get(p.get("marking_type", ""), "")
            r["en_is_translation"] = bool(p.get("text_en_is_translation"))
            if not r["text_zh"] and p["rule_id"] in zh:
                r["text_zh"] = zh[p["rule_id"]]
                r["zh_is_translation"] = True
            else:
                r["zh_is_translation"] = False
            rows.append(r)
        out[region] = rows
    return out


def _item_payload(item: dict, file: str) -> dict:
    box = [int(float(item[k])) for k in ("bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2")]
    return {"image_id": item["image_id"], "set_id": _trip_of(item["image_id"]), "region": item["region"],
            "dataset": item["dataset"], "file": file, "width": int(float(item["width"])),
            "height": int(float(item["height"])), "box": box, "time_of_day": item.get("time_of_day", "")}


def _reference(ann: dict) -> dict:
    return {"marking_type": ann["marking_type"], "arrow_type": ann["arrow_type"], "position": ann["position"],
            "dashed_side": ann["dashed_side"], "visibility": ann["visibility"],
            "behavior_decidable": ann["behavior_decidable"],
            "actions": {a: ann["act_" + a] for a in ACTIONS},
            "accepted_rule_ids": [i for i in ann["accepted_rule_ids"].split(";") if i]}


def _next_batch(rows: list[dict]) -> str:
    day = datetime.now().strftime("%Y%m%d")
    used = {r["batch"] for r in rows}
    for c in "abcdefghijklmnopqrstuvwxyz":
        if f"b{day}{c}" not in used:
            return f"b{day}{c}"
    raise ToolError("Too many batches today.")


def build_packages(paths: Paths, names: list[str], trip_ids: list[str] | None = None, practice: int = 6,
                   max_per_person: int | None = None, log=print) -> list[Path]:
    names = [n.strip() for n in names if n.strip()]
    if not names:
        raise ToolError("Give at least one helper name, e.g. --to Alice,Bob")
    codes = {n: annotator_code(paths, n) for n in names}
    registry = read_csv(paths.packages_csv)
    outstanding = defaultdict(set)  # image_id -> codes with an unreturned package
    for r in registry:
        if r["status"] in ("sent", "partial"):
            for iid in r["items"].split(";"):
                if iid:
                    outstanding[iid].add(r["annotator"])

    pool, gold, no_box = [], [], 0
    for tid in trip_ids or list_trip_ids(paths):
        trip = Trip(paths, tid)
        labels = LabelStore(paths.labels_csv(tid))
        anns = AnnotationStore(paths.annotations_csv(tid))
        req = required_for(trip.meta)
        for item in sorted(labels.all(), key=lambda r: int(r["frame_index"] or 0)):
            if item["label_status"] == "excluded":
                continue
            if not has_box(item):
                no_box += 1
                continue
            mine = anns.get(item["image_id"], OWNER)
            if mine and mine["status"] == "done" and mine.get("unsure") != "1":
                gold.append((tid, item, mine))
            if item["label_status"] in ("done", "conflict"):
                continue
            have = {a["annotator"] for a in anns.for_image(item["image_id"]) if a["status"] == "done"}
            busy = have | outstanding[item["image_id"]]
            need = req - len(have) - len(outstanding[item["image_id"]])
            if need > 0:
                pool.append((tid, item, need, busy))
    if no_box:
        log(f"Note: {no_box} kept frames have no target box yet. Draw it in the local app (② label, 'save box') to include them.")
    if not pool:
        raise ToolError("Nothing to send: every frame with a target box already has enough labels or an open package.")

    load = Counter({c: 0 for c in codes.values()})
    assigned: dict[str, list] = defaultdict(list)
    for tid, item, need, busy in pool:
        cands = sorted((c for c in codes.values() if c not in busy), key=lambda c: (load[c], c))
        if max_per_person:
            cands = [c for c in cands if load[c] < max_per_person]
        for c in cands[:need]:
            assigned[c].append((tid, item))
            load[c] += 1
    short = sum(max(0, need - sum(1 for c in codes.values() if c not in busy)) for _, _, need, busy in pool)
    if short:
        log(f"Note: {short} labels still missing after this batch (not enough different helpers for some frames).")

    schema = load_schema(paths)
    tables = load_action_rules(paths)
    passages = _passages_for_page(paths)
    batch = _next_batch(registry)
    paths.packages_dir.mkdir(parents=True, exist_ok=True)
    reg_names = load_annotators(paths)
    made = []
    for name, code in codes.items():
        items = assigned.get(code, [])
        if not items:
            log(f"  {name} ({code}): nothing to label in this batch.")
            continue
        mine_ids = {it["image_id"] for _, it in items}
        rng = random.Random(f"{batch}:{code}")
        cand = [g for g in gold if g[1]["image_id"] not in mine_ids]
        rng.shuffle(cand)
        by_type, picked = set(), []
        for g in cand:  # prefer different marking types
            if g[2]["marking_type"] not in by_type and len(picked) < practice:
                picked.append(g)
                by_type.add(g[2]["marking_type"])
        for g in cand:
            if len(picked) >= practice:
                break
            if g not in picked:
                picked.append(g)
        package_id = f"{batch}_{code}"
        payload = {
            "format": PACKAGE_FORMAT, "tool_version": __version__, "package_id": package_id, "batch": batch,
            "annotator": code, "annotator_name": reg_names.get(code, {}).get("name", name), "created_utc": utc_now(),
            "schema": schema, "rules_tables": {r: tables.get(r, {}) for r in ("US", "CN")}, "passages": passages,
            "items": [], "practice": [], "notices": [],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / f"lane_labeling_{package_id}"
            (root / "images").mkdir(parents=True)
            datasets = set()
            for tid, item in items:
                src = paths.data / item["source_path"]
                if not src.exists():
                    raise ToolError(f"Frame missing: {src}. Run: python -m video_tool rebuild {tid}")
                shutil.copy(src, root / "images" / f"{item['image_id']}.jpg")
                payload["items"].append(_item_payload(item, f"images/{item['image_id']}.jpg"))
                datasets.add(item["dataset"])
            for tid, item, ann in picked:
                shutil.copy(paths.data / item["source_path"], root / "images" / f"{item['image_id']}.jpg")
                p = _item_payload(item, f"images/{item['image_id']}.jpg")
                p["reference"] = _reference(ann)
                payload["practice"].append(p)
                datasets.add(item["dataset"])
            payload["notices"] = [LICENSE_NOTES[d] for d in sorted(datasets) if d in LICENSE_NOTES]
            (root / "data.js").write_text("window.LANE_PACKAGE = " + json.dumps(payload, ensure_ascii=False) + ";\n", encoding="utf-8")
            (root / "index.html").write_text(_page_html(), encoding="utf-8")
            (root / "README.txt").write_text(_readme(payload), encoding="utf-8")
            safe = "".join(ch for ch in name if ch.isalnum() or ch in "-_") or code
            zpath = paths.packages_dir / f"{package_id}_{safe}.zip"
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
                for f in sorted(root.rglob("*")):
                    if f.is_file():
                        z.write(f, f.relative_to(root.parent).as_posix())
        registry.append({"package_id": package_id, "batch": batch, "annotator": code, "created_utc": utc_now(),
                         "n_items": len(items), "items": ";".join(it["image_id"] for _, it in items),
                         "practice": ";".join(it["image_id"] for _, it, _ in picked), "status": "sent"})
        made.append(zpath)
        log(f"  {name} ({code}): {len(items)} frames + {len(picked)} practice -> {zpath}")
    write_csv(paths.packages_csv, registry, PACKAGE_COLUMNS)
    if not gold:
        log("No practice items yet: label a few frames yourself first (local app, 'done'); they become practice with your answers.")
    log("Send each zip to its helper. They unzip it, open index.html, label, and send back the results .json file.")
    return made


def _page_html() -> str:
    """index.html with every style and script inlined; only data.js and images/ sit next to it."""
    read = lambda name: (WEB_DIR / name).read_text(encoding="utf-8")  # noqa: E731
    html = read("offline.html")
    html = html.replace("<!--STYLE-->", "<style>\n" + read("style.css") + "\n" + read("offline.css") + "\n</style>")
    scripts = "".join("<script>\n" + read(n) + "\n</script>\n" for n in ("i18n.js", "guide.js", "offline.js"))
    html = html.replace("<!--SCRIPT-->", '<script src="data.js"></script>\n' + scripts)
    return html


def _readme(payload: dict) -> str:
    notices = "\n".join(payload["notices"])
    return f"""Lane marking labeling / 道路标线标注
Package {payload['package_id']} for {payload['annotator_name']} ({payload['annotator']}): {len(payload['items'])} images, {len(payload['practice'])} practice.

1. Unzip this folder (do not open index.html from inside the zip).
   先把整个文件夹解压出来（不要在压缩包里直接打开）。
2. Double-click index.html. It opens in your browser and works offline. Chrome, Edge, Safari and Firefox all work.
   双击 index.html，会在浏览器中打开，不需要联网。
3. Read the guide and the privacy note, do the practice items, then label.
   先看说明和隐私须知，做完练习再开始标注。
4. Your work is saved in this browser automatically. Click "Export results" at least once a day and at the end,
   and send the downloaded results_*.json file back. Clearing the browser data deletes unsaved work.
   进度会自动保存在浏览器里。请每天至少导出一次，做完后把下载的 results_*.json 文件发回来。
5. Privacy: the images show real roads. Do not share, upload or screenshot them. Delete this folder when you are done.
   隐私：图片来自真实道路。请不要转发、上传或截图；标完后请删除整个文件夹。

{notices}
"""


# ------------------------------------------------------------------ import

def import_results(paths: Paths, inputs: list[str], log=print) -> dict:
    files: list[Path] = []
    for i in inputs:
        p = Path(i).expanduser()
        if p.is_dir():
            files += sorted(f for f in p.glob("*.json") if not f.name.startswith("._"))
        elif p.is_file():
            files.append(p)
        else:
            raise ToolError(f"Not found: {p}")
    if not files:
        raise ToolError("No results .json files found.")
    registry = read_csv(paths.packages_csv)
    by_id = {r["package_id"]: r for r in registry}
    schema = load_schema(paths)
    rule_ids = {r: {p["rule_id"] for p in load_rule_passages(paths, r)} for r in ("US", "CN")}
    stores: dict[str, AnnotationStore] = {}
    labels_cache: dict[str, LabelStore] = {}
    touched, summary = set(), []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            log(f"  ✗ {f.name}: not a results file")
            continue
        if data.get("format") != RESULTS_FORMAT:
            log(f"  ✗ {f.name}: not a results file (format {data.get('format')!r})")
            continue
        pid = data.get("package_id")
        pkg = by_id.get(pid)
        if not pkg:
            log(f"  ✗ {f.name}: package {pid} is not in packages.csv")
            continue
        code = pkg["annotator"]
        if data.get("annotator") != code:
            log(f"  ✗ {f.name}: annotator {data.get('annotator')} does not match package {pid} ({code})")
            continue
        allowed = set(pkg["items"].split(";"))
        st = Counter()
        for r in data.get("results", []):
            iid = r.get("image_id")
            if iid not in allowed:
                st["skipped"] += 1
                continue
            tid = _trip_of(iid)
            store = stores.setdefault(tid, AnnotationStore(paths.annotations_csv(tid)))
            labels = labels_cache.setdefault(tid, LabelStore(paths.labels_csv(tid)))
            item = labels.get(iid)
            if item is None:
                st["skipped"] += 1
                continue
            old = store.get(iid, code)
            saved = r.get("saved_utc") or data.get("exported_utc") or utc_now()
            if old and old.get("saved_utc", "") >= saved:
                st["unchanged"] += 1
                continue
            row = fields_to_row({}, r.get("fields", {}), schema)
            row["privacy_boxes"] = json.dumps([b for b in (r.get("privacy_boxes") or []) if isinstance(b, list) and len(b) == 4])
            status = "done" if r.get("status") == "done" else "draft"
            errors, _ = validate_label({**item, **row}, schema, rule_ids.get(item["region"], set()), check_box=False)
            if status == "done" and errors and not r.get("unsure"):
                status = "draft"
                st["invalid"] += 1
            row.update({"image_id": iid, "annotator": code, "source": "package", "package_id": pid, "status": status,
                        "unsure": "1" if r.get("unsure") else "0", "comment": str(r.get("comment") or "")[:500],
                        "saved_utc": saved})
            store.put(row)
            touched.add(tid)
            st[status] += 1
            st["unsure"] += 1 if r.get("unsure") else 0
        prac = data.get("practice_score")
        n_done = 0
        for iid in (i for i in allowed if i):
            a = stores.setdefault(_trip_of(iid), AnnotationStore(paths.annotations_csv(_trip_of(iid)))).get(iid, code)
            n_done += bool(a and a["status"] == "done")
        complete = n_done >= len([i for i in allowed if i])
        pkg.update({"status": "complete" if complete else "partial", "imported_utc": utc_now(), "done": n_done,
                    "draft": st["draft"], "unsure": st["unsure"], "practice_score": prac if prac is not None else ""})
        summary.append((f.name, code, st))
        log(f"  ✓ {f.name}: {code}  done {st['done']}, draft {st['draft']}, unsure {st['unsure']}"
            + (f", invalid {st['invalid']}" if st["invalid"] else "") + (f", unchanged {st['unchanged']}" if st["unchanged"] else "")
            + (f"  practice {prac}" if prac is not None else ""))
    for tid, store in stores.items():
        store.save()
    counts = Counter()
    for tid in touched:
        counts += merge_trip(paths, Trip(paths, tid), labels_cache.get(tid), stores[tid])
    write_csv(paths.packages_csv, registry, PACKAGE_COLUMNS)
    if counts:
        log(f"Final labels now: done {counts['done']}, conflict {counts['conflict']} (decide them in the local app, ③), "
            f"waiting {counts['waiting']}, no box {counts['kept']}, excluded {counts['excluded']}.")
    write_agreement(paths, log)
    return {"files": summary, "counts": counts}


__all__ = ["build_packages", "import_results", "differences", "ACTION_COLUMNS"]
