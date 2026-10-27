"""Check the labels, make blurred copies for reports, count what you have, compare re-checks."""
from __future__ import annotations

import json
from collections import Counter, defaultdict

import cv2

from .annotations import AnnotationStore, migrate_owner_labels, write_agreement
from .core import (ACTION_COLUMNS, ANNOTATION_COLUMNS, LABEL_COLUMNS, RECHECK_COLUMNS, LabelStore, Paths, ToolError, Trip,
                   list_trip_ids, load_action_rules, load_rule_passages, load_schema, read_csv, sha256_of,
                   validate_label, write_csv)
from .video import VideoReader, blur_boxes, read_image, render_frame, write_jpeg

RECHECK_FIELDS = ["marking_type", "arrow_type", "visibility", "behavior_decidable", *ACTION_COLUMNS]


def _boxes(row: dict) -> list:
    try:
        return json.loads(row.get("privacy_boxes") or "[]")
    except json.JSONDecodeError:
        return []


def export_trip(paths: Paths, trip_id: str, log=print) -> dict:
    trip = Trip(paths, trip_id)
    migrate_owner_labels(paths, trip)
    schema = load_schema(paths)
    table = load_action_rules(paths)
    rule_ids = {p["rule_id"] for p in load_rule_passages(paths, trip.region)}
    store = LabelStore(paths.labels_csv(trip_id))
    rows = sorted(store.all(), key=lambda r: int(r["frame_index"]))
    status = Counter(r["label_status"] for r in rows)
    log(f"\n== {trip_id}: {len(rows)} kept frames  (final {status['done']}, conflict {status['conflict']}, "
        f"waiting for labels {status['waiting']}, no target box {status['kept']}, excluded {status['excluded']})")

    problems = 0
    for r in rows:
        if r["label_status"] != "done":
            continue
        errors, warnings = validate_label(r, schema, rule_ids, table)
        if r["label_status"] == "done" and errors:
            problems += 1
            log(f"  ✗ {r['image_id']}: " + " ".join(errors))
        for w in warnings:
            log(f"  ! {r['image_id']}: {w}")
    if not problems:
        log("  All finished labels pass the checks.")

    out_dir = paths.figures_dir(trip_id)
    made, missing = 0, 0
    for r in rows:
        src = paths.data / r["source_path"]
        if not src.exists():
            missing += 1
            continue
        img = blur_boxes(read_image(src), _boxes(r))
        write_jpeg(out_dir / f"{r['image_id']}.jpg", img, 92)
        if r.get("bbox_x1") not in ("", None):
            boxed = img.copy()
            x1, y1, x2, y2 = (int(float(r[k])) for k in ("bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2"))
            cv2.rectangle(boxed, (x1, y1), (x2, y2), (200, 224, 54), 3)
            write_jpeg(out_dir / f"{r['image_id']}_box.jpg", boxed, 92)
        made += 1
    log(f"  Report figures (plates and faces blurred): {made} in {out_dir}" + (f"; {missing} frames missing, run: python -m video_tool rebuild {trip_id}" if missing else ""))
    no_privacy = [r["image_id"] for r in rows if r["label_status"] == "done" and not _boxes(r)]
    if no_privacy:
        log(f"  {len(no_privacy)} finished frames have no privacy box. Fine if they show no readable plate or face; check before using one in a report.")

    done = [r for r in rows if r["label_status"] == "done"]
    by_type = Counter(r["marking_type"] + (f"/{r['arrow_type']}" if r["arrow_type"] else "") for r in done)
    by_vis = Counter(r["visibility"] for r in done)
    if done:
        log("  Finished labels by type: " + ", ".join(f"{k} {v}" for k, v in sorted(by_type.items())))
        log("  By visibility: " + ", ".join(f"{k} {v}" for k, v in sorted(by_vis.items())))

    if trip.kind == "images":
        from .imagesets import near_duplicates_across_split, quota_table
        q = quota_table(trip, store, AnnotationStore(paths.annotations_csv(trip_id)))
        log("  Quota (picked / target): " + "; ".join(
            f"{r['group']} dev {r['dev_have']}/{r['dev_target']} test {r['test_have']}/{r['test_target']}" for r in q["rows"]))
        dups = near_duplicates_across_split(paths, rows)
        for a, b, d in dups:
            log(f"  ! development image {a} and test image {b} look almost the same ({d}/64 bits): exclude one of them (6.5)")
        if not dups:
            log("  No development image looks like a test image (dHash, 4 bits).")
    agreement = recheck_agreement(paths, trip_id, store, log)
    return {"trip_id": trip_id, "rows": rows, "status": status, "problems": problems, "agreement": agreement}


def recheck_agreement(paths: Paths, trip_id: str, store: LabelStore, log=print) -> list[dict]:
    rec = [r for r in read_csv(paths.recheck_csv(trip_id)) if r.get("recheck_status") == "done"]
    if not rec:
        return []
    groups: dict = defaultdict(lambda: {"n": 0, "changed": 0, "fields": Counter()})
    for r in rec:
        base = store.get(r["image_id"])
        if not base:
            continue
        g = groups[base["marking_type"]]
        g["n"] += 1
        diff = [f for f in RECHECK_FIELDS if (base.get(f) or "") != (r.get(f) or "")]
        if diff:
            g["changed"] += 1
            g["fields"].update(diff)
    out = []
    log("  Blind re-check (risk R2: more than 1 in 10 changed in a type -> revise the guide and re-label that type):")
    for mt, g in sorted(groups.items()):
        rate = g["changed"] / g["n"]
        flag = "TRIGGER" if rate > 0.10 else "ok"
        top = ", ".join(f"{f} {c}" for f, c in g["fields"].most_common(3))
        log(f"    {mt:24s} {g['changed']}/{g['n']} changed ({rate:.0%}) {flag}" + (f"   most changed: {top}" if top else ""))
        out.append({"trip_id": trip_id, "marking_type": mt, "rechecked": g["n"], "changed": g["changed"],
                    "change_rate": round(rate, 3), "r2_trigger": int(rate > 0.10), "most_changed_fields": top})
    write_csv(paths.labels_dir / f"{trip_id}.recheck_agreement.csv", out,
              ["trip_id", "marking_type", "rechecked", "changed", "change_rate", "r2_trigger", "most_changed_fields"])
    return out


def export_all(paths: Paths, trip_ids: list[str] | None = None, log=print) -> None:
    ids = trip_ids or list_trip_ids(paths)
    if not ids:
        raise ToolError("No trips registered yet.")
    for tid in ids:
        export_trip(paths, tid, log)
    # combined files for the rest of the pipeline: every trip, every row
    all_rows, all_anns, summary = [], [], Counter()
    for tid in list_trip_ids(paths):
        all_anns += AnnotationStore(paths.annotations_csv(tid)).all()
        for r in LabelStore(paths.labels_csv(tid)).all():
            all_rows.append(r)
            if r["label_status"] == "done":
                summary[(r["region"], r["dataset"], r["time_of_day"], r["marking_type"], r["arrow_type"], r["visibility"])] += 1
    all_rows.sort(key=lambda r: (r["clip_id"], int(r["frame_index"])))
    write_csv(paths.labels_dir / "all_labels.csv", all_rows, LABEL_COLUMNS)
    write_csv(paths.labels_dir / "all_annotations.csv", sorted(all_anns, key=lambda a: (a["image_id"], a["annotator"])), ANNOTATION_COLUMNS)
    cols = ["region", "dataset", "time_of_day", "marking_type", "arrow_type", "visibility", "done_labels"]
    write_csv(paths.labels_dir / "summary.csv",
              [dict(zip(cols, (*k, v))) for k, v in sorted(summary.items())], cols)
    log("")
    write_agreement(paths, log)
    log(f"\nWrote {paths.labels_dir / 'all_labels.csv'} ({len(all_rows)} rows; the answer key is label_status == done), "
        f"all_annotations.csv ({len(all_anns)} independent labels), summary.csv and agreement.csv.")


def rebuild_trip(paths: Paths, trip_id: str, skip_hash: bool = False, log=print) -> int:
    if Trip(paths, trip_id).kind == "images":
        return _recopy_images(paths, trip_id, log)
    return _rebuild_video_trip(paths, trip_id, skip_hash, log)


def _recopy_images(paths: Paths, trip_id: str, log=print) -> int:
    import shutil
    from pathlib import Path
    trip = Trip(paths, trip_id)
    src_root = Path(trip.meta["source_root"])
    n = 0
    for r in LabelStore(paths.labels_csv(trip_id)).all():
        dest = paths.data / r["source_path"]
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_root / r["source_ref"], dest)
            n += 1
    log(f"Copied {n} missing images again from {src_root}.")
    return n


def _rebuild_video_trip(paths: Paths, trip_id: str, skip_hash: bool = False, log=print) -> int:
    """Re-create every kept frame from the video (after a mask change, a lost file, or to prove lineage)."""
    trip = Trip(paths, trip_id)
    video = trip.check_video()
    if not skip_hash:
        log(f"Checking the video hash of {video.name} ...")
        if sha256_of(video) != trip.meta["video"]["sha256"]:
            raise ToolError("The video file is not the one that was registered (SHA-256 differs).")
    reader = VideoReader(video)
    out = trip.meta["output"]
    size = (int(out["width"]), int(out["height"]))
    rows = LabelStore(paths.labels_csv(trip_id)).all()
    for r in rows:
        frame = render_frame(reader, int(r["frame_index"]), trip.meta.get("masks", []), size)
        write_jpeg(paths.data / r["source_path"], frame, int(out.get("jpeg_quality", 95)))
    reader.close()
    log(f"Rebuilt {len(rows)} frames for '{trip_id}' from the video.")
    return len(rows)


__all__ = ["export_trip", "export_all", "rebuild_trip", "recheck_agreement", "RECHECK_COLUMNS"]
