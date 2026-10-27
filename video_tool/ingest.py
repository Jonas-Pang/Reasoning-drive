"""Register a new video as a trip: copy it into data/raw, hash it, record its metadata."""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime
from pathlib import Path

from . import __version__
from .core import (LABEL_COLUMNS, OWN_LICENSE, Paths, ToolError, check_trip_id, list_trip_ids, read_json,
                   sha256_of, update_trips_csv, utc_now, write_csv, write_json)
from .video import VideoReader, output_size

TIME_OF_DAY = ["daytime", "night", "dawn_dusk"]          # same groups as BDD100K
WEATHER = ["clear", "partly_cloudy", "overcast", "rainy", "foggy", "snowy"]


def _date_from_name(name: str) -> str | None:
    m = re.search(r"(20\d{2})[-_]?([01]\d)[-_]?([0-3]\d)", name)
    if not m:
        return None
    try:
        return datetime(int(m[1]), int(m[2]), int(m[3])).strftime("%Y-%m-%d")
    except ValueError:
        return None


def _progress(label: str, log):
    state = {"last": -1}

    def cb(done: int, total: int):
        pct = int(done * 100 / max(total, 1))
        if pct // 10 != state["last"] // 10:
            log(f"  {label} {pct}%")
            state["last"] = pct
    return cb


def _copy(src: Path, dst: Path, log) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_name(".tmp_" + dst.name)
    total = src.stat().st_size
    cb = _progress("copying", log)
    done = 0
    with open(src, "rb") as fi, open(tmp, "wb") as fo:
        while True:
            block = fi.read(16 << 20)
            if not block:
                break
            fo.write(block)
            done += len(block)
            cb(done, total)
    shutil.copystat(src, tmp)
    tmp.replace(dst)


def ingest_many(paths: Paths, videos: list, trip_id: str | None = None, drive_id: str | None = None, log=print, **kw) -> list[str]:
    """Several files of one drive (cameras split long recordings): one trip per file, one shared drive id.

    The drive id is the unit of the train/test split, like a CULane clip."""
    files = sorted((Path(v).expanduser().resolve() for v in videos), key=lambda p: p.name)
    if len(files) == 1 and not drive_id:
        return [ingest(paths, files[0], trip_id=trip_id, log=log, **kw)]
    if not drive_id:
        first = files[0]
        date = kw.get("recorded_date") or _date_from_name(first.name) or datetime.fromtimestamp(first.stat().st_mtime).strftime("%Y-%m-%d")
        base = trip_id or f"{kw.get('place', 'FL').lower()}_{date.replace('-', '')}_{kw.get('time_of_day', 'night')}"
        existing = list_trip_ids(paths)
        n = 1
        while any(t.startswith(f"{base}_{n:02d}_s") for t in existing):
            n += 1
        drive_id = trip_id or f"{base}_{n:02d}"
    check_trip_id(drive_id)
    existing = list_trip_ids(paths)
    k = 1 + sum(1 for t in existing if t.startswith(drive_id + "_s"))
    out = []
    for f in files:
        out.append(ingest(paths, f, trip_id=f"{drive_id}_s{k:02d}", drive_id=drive_id, log=log, **kw))
        k += 1
    log(f"Drive '{drive_id}': {len(out)} file(s) registered as {', '.join(out)} (one split group).")
    return out


def ingest(paths: Paths, video: str | Path, trip_id: str | None = None, recorded_date: str | None = None,
           time_of_day: str = "night", weather: str = "clear", road_type: str = "", place: str = "FL",
           region: str = "US", split: str = "test", out_width: int = 1280, copy: bool = True,
           notes: str = "", drive_id: str | None = None, annotators_required: int = 2, log=print) -> str:
    src = Path(video).expanduser().resolve()
    if not src.is_file():
        raise ToolError(f"Video not found: {src}")
    if time_of_day not in TIME_OF_DAY:
        raise ToolError(f"--time-of-day must be one of {', '.join(TIME_OF_DAY)}")
    if weather not in WEATHER:
        raise ToolError(f"--weather must be one of {', '.join(WEATHER)}")
    if split not in ("test", "dev", "hash"):
        raise ToolError("--split must be test, dev or hash")
    if region not in ("US", "CN"):
        raise ToolError("--region must be US or CN (the regions that have a rule pack)")

    reader = VideoReader(src)  # fails early if OpenCV cannot decode it
    info = reader.info()
    reader.close()

    date = recorded_date or _date_from_name(src.name) or datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ToolError("--date must look like 2026-10-16")
    existing = list_trip_ids(paths)
    if trip_id is None:
        base = f"{place.lower()}_{date.replace('-', '')}_{time_of_day}"
        n = 1
        while f"{base}_{n:02d}" in existing:
            n += 1
        trip_id = f"{base}_{n:02d}"
    check_trip_id(trip_id)
    if trip_id in existing:
        raise ToolError(f"Trip '{trip_id}' already exists. Pick another --trip name.")

    log(f"Hashing {src.name} ({src.stat().st_size / 1e9:.2f} GB) ...")
    digest = sha256_of(src, _progress("hashing", log))
    for other in existing:
        if read_json(paths.trip_json(other)).get("video", {}).get("sha256") == digest:
            raise ToolError(f"This video is already registered as trip '{other}'.")

    raw_dir = paths.raw_dir(trip_id)
    if copy:
        dst = raw_dir / src.name
        if src != dst:
            log(f"Copying the video to {dst} ...")
            _copy(src, dst, log)
        stored = paths.rel(dst)
        meta_target = dst
    else:
        try:
            stored = paths.rel(src)
        except ValueError:
            stored = str(src)  # outside DATA_DIR: keep the absolute path
        meta_target = src
    Path(str(meta_target) + ".meta.json").write_text(json.dumps({
        "origin": f"own recording, registered from {src}",
        "retrieved_utc": utc_now()[:10],
        "sha256": digest,
        "trip_id": trip_id,
        "license": OWN_LICENSE,
    }, indent=2), encoding="utf-8")

    ow, oh = output_size(info["width"], info["height"], out_width)
    meta = {
        "trip_id": trip_id,
        "region": region,
        "dataset": f"own_{place}",
        "place": place,
        "recorded_date": date,
        "time_of_day": time_of_day,
        "weather": weather,
        "road_type": road_type,
        "notes": notes,
        "license": OWN_LICENSE,
        "split": split,
        "drive_id": drive_id or trip_id,
        "annotators_required": int(annotators_required),
        "video": {"file": stored, "original_name": src.name, "sha256": digest,
                  "size_bytes": src.stat().st_size, **info},
        "output": {"width": ow, "height": oh, "jpeg_quality": 95},
        "trim": {"start_s": 0.0, "end_s": None},
        "masks": [],
        "registered_utc": utc_now(),
        "tool_version": __version__,
    }
    write_json(paths.trip_json(trip_id), meta)
    if not paths.labels_csv(trip_id).exists():
        write_csv(paths.labels_csv(trip_id), [], LABEL_COLUMNS)
    update_trips_csv(paths)
    log(f"Registered trip '{trip_id}': {info['width']}x{info['height']}, {info['fps']} fps, "
        f"{(info['duration_s'] or 0) / 60:.1f} min, frames will be saved at {ow}x{oh}.")
    log(f"Next: python -m video_tool scan {trip_id}")
    return trip_id
