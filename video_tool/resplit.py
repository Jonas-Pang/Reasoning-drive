"""Move a whole own-video drive to the other side of the split (Milestone 3, 6.5: "update the record if data or
evaluation cases change, explaining which earlier results are affected").

Only test -> dev is meant for normal use: a drive that has been looked at while developing the prompt is
development data. The move is logged in labels/split_changes.csv; `combine` then writes the next
labels/split_v<N>.csv and keeps the older files.
"""
from __future__ import annotations

from .core import LabelStore, Paths, ToolError, Trip, list_trip_ids, read_csv, update_trips_csv, utc_now, write_csv

CHANGE_COLUMNS = ["date_utc", "collection", "drive_id", "trips", "from_split", "to_split", "labels_changed", "reason"]


def resplit(paths: Paths, trip_id: str, new_split: str, reason: str, log=print) -> dict:
    if paths.is_images:
        raise ToolError("resplit is for own-video drives. Dataset images follow the hash rule of 6.5.")
    if new_split not in ("dev", "test"):
        raise ToolError("The new split must be dev or test.")
    if not reason.strip():
        raise ToolError("Say why (--reason \"...\"); it is written to labels/split_changes.csv.")
    if trip_id not in list_trip_ids(paths):
        raise ToolError(f"No trip {trip_id}. Trips: {', '.join(list_trip_ids(paths))}")
    drive = Trip(paths, trip_id).meta.get("drive_id") or trip_id
    group = [t for t in list_trip_ids(paths) if (Trip(paths, t).meta.get("drive_id") or t) == drive]  # the drive is the unit
    old = sorted({Trip(paths, t).meta.get("split", "") for t in group})
    if old == [new_split]:
        raise ToolError(f"Drive {drive} is already {new_split}.")
    if new_split == "test":
        log("Warning: moving development data into the test set means the test images have been seen during development.")
    changed, now = 0, utc_now()
    for t in group:
        tr = Trip(paths, t)
        tr.meta.setdefault("split_history", []).append({"date_utc": now, "from": tr.meta.get("split"), "to": new_split, "reason": reason})
        tr.meta["split"] = new_split
        tr.save()
        store = LabelStore(paths.labels_csv(t))
        for r in store.all():
            if r.get("split") != new_split:
                r["split"] = new_split
                changed += 1
        store.save()
    update_trips_csv(paths)
    log_file = paths.repo / "labels" / "split_changes.csv"
    rows = read_csv(log_file) + [{"date_utc": now, "collection": paths.collection, "drive_id": drive, "trips": ";".join(group),
                                  "from_split": "/".join(old), "to_split": new_split, "labels_changed": changed, "reason": reason}]
    write_csv(log_file, rows, CHANGE_COLUMNS)
    log(f"Drive {drive} ({len(group)} trip(s)) moved from {'/'.join(old)} to {new_split}: {changed} label rows changed. "
        f"Logged in labels/split_changes.csv. Run `combine` to write labels/split_v{len(rows) + 1}.csv.")
    return {"drive": drive, "trips": group, "labels_changed": changed, "split_version": len(rows) + 1}
