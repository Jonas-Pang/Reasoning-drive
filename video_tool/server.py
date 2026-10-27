"""Local labeling app: a small web server on 127.0.0.1 that only you can reach.

Own video: the browser shows the video moment by moment (frames are decoded on request and kept in
memory), you keep the frames you want, and label them on the same page.
Dataset images (ImageApp): the browser lists candidate images of the dataset with their hints; you pick
images into the quota cells and label them on the same page.
"""
from __future__ import annotations

import json
import math
import random
import threading
import webbrowser
from collections import OrderedDict
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from .annotations import AnnotationStore, adjudicate, fields_to_row, merge_item, migrate_owner_labels, required_for
from .core import (OWNER, RECHECK_COLUMNS, LabelStore, Paths, ToolError, Trip, assign_split,
                   derive_evidence, load_action_rules, load_rule_passages, load_schema, read_csv,
                   today, utc_now, validate_label)
from .video import VideoReader, encode_jpeg, read_image, render_frame, resize, write_jpeg

WEB_DIR = Path(__file__).resolve().parent / "web"
NUMERIC_SCAN = ["sample", "frame_index", "time_s", "motion_smooth", "stationary", "dup", "brightness",
                "sharpness", "paint", "yellow", "dark", "blurry", "candidate"]


class QuietServer(ThreadingHTTPServer):
    daemon_threads = True

    def handle_error(self, request, client_address):
        import sys
        if isinstance(sys.exc_info()[1], (BrokenPipeError, ConnectionResetError)):
            return
        super().handle_error(request, client_address)


class App:
    def __init__(self, paths: Paths, trip: Trip, labeler: str, recheck: bool = False, new_sample: bool = False):
        self.paths, self.trip, self.labeler = paths, trip, labeler
        self.schema = load_schema(paths)
        self.table = load_action_rules(paths)
        self.passages = load_rule_passages(paths, trip.region)
        self.rule_ids = {p["rule_id"] for p in self.passages}
        self.reader = VideoReader(trip.check_video())
        scan_rows = read_csv(paths.scan_csv(trip.id))
        if not scan_rows:
            raise ToolError(f"No scan for '{trip.id}' yet. Run first: python -m video_tool scan {trip.id}")
        self.scan = []
        for r in scan_rows:
            row = {}
            for k in NUMERIC_SCAN:
                v = r.get(k, "")
                row[k] = float(v) if v not in ("", None) else None
            self.scan.append(row)
        migrate_owner_labels(paths, trip)
        self.labels = LabelStore(paths.labels_csv(trip.id))
        self.anns = AnnotationStore(paths.annotations_csv(trip.id))
        self.required = required_for(trip.meta)
        self.lock = threading.RLock()
        self.cache: OrderedDict = OrderedDict()
        self.mask_version = 0
        out = trip.meta["output"]
        self.out_size = (int(out["width"]), int(out["height"]))
        self.quality = int(out.get("jpeg_quality", 95))
        self.recheck_mode = recheck
        self.recheck = None
        if recheck:
            self.recheck = LabelStore(paths.recheck_csv(trip.id), RECHECK_COLUMNS)
            if new_sample or not self.recheck.rows:
                self._draw_recheck_sample()

    # ------------------------------------------------------------ state
    def state(self) -> dict:
        m = self.trip.meta
        return {
            "trip": {k: m.get(k) for k in ("trip_id", "region", "dataset", "time_of_day", "weather", "road_type",
                                          "recorded_date", "split", "masks", "trim")},
            "video": {**m["video"], "fps": self.reader.fps},
            "output": {"width": self.out_size[0], "height": self.out_size[1]},
            "scan": self.scan,
            "scan_summary": m.get("scan", {}),
            "labels": self.labels.all(),
            "annotations": self.anns.all(),
            "required": self.required,
            "owner": OWNER,
            "schema": self.schema,
            "rules_table": self.table.get(self.trip.region, {}),
            "passages": self._passages_with_zh(),
            "labeler": self.labeler,
            "recheck_mode": self.recheck_mode,
            "recheck": self.recheck.all() if self.recheck else [],
            "mask_version": self.mask_version,
        }

    def _passages_with_zh(self) -> list[dict]:
        from .packages import _passages_for_page
        return _passages_for_page(self.paths).get(self.trip.region, [])

    # ------------------------------------------------------------ frames
    def preview(self, frame_index: int, width: int) -> bytes:
        width = max(160, min(int(width), self.reader.width))
        key = (frame_index, width, self.mask_version)
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
        h = int(round(self.reader.height * width / self.reader.width))
        frame = render_frame(self.reader, frame_index, self.trip.meta.get("masks", []), (width, h))
        data = encode_jpeg(frame, 85)
        with self.lock:
            self.cache[key] = data
            while len(self.cache) > 400:
                self.cache.popitem(last=False)
        return data

    def image_path(self, image_id: str) -> Path:
        return self.paths.frames_dir(self.trip.id) / f"{image_id}.jpg"

    def image(self, image_id: str, width: int | None = None) -> bytes:
        row = self.labels.get(image_id)
        if row is None and not (self.recheck and self.recheck.get(image_id)):
            raise ToolError(f"Unknown image {image_id}")
        p = self.image_path(image_id)
        if not p.exists():
            self._render_kept(image_id, int((row or self.labels.get(image_id))["frame_index"]))
        if not width:
            return p.read_bytes()
        img = read_image(p)
        h = int(round(img.shape[0] * width / img.shape[1]))
        return encode_jpeg(resize(img, (int(width), h)), 80)

    def _render_kept(self, image_id: str, frame_index: int) -> None:
        frame = render_frame(self.reader, frame_index, self.trip.meta.get("masks", []), self.out_size)
        write_jpeg(self.image_path(image_id), frame, self.quality)

    # ------------------------------------------------------------ keep / label
    def image_id_for(self, frame_index: int) -> str:
        return f"{self.trip.id}_f{frame_index:07d}"

    def keep(self, frame_index: int) -> dict:
        frame_index = int(frame_index)
        if frame_index < 0:
            raise ToolError("Bad frame index.")
        image_id = self.image_id_for(frame_index)
        with self.lock:
            existing = self.labels.get(image_id)
            if existing:
                return {"row": existing, "near": []}
            self._render_kept(image_id, frame_index)
            m = self.trip.meta
            fps = self.reader.fps
            row = {
                "image_id": image_id, "region": m["region"], "dataset": m["dataset"],
                "source_path": self.paths.rel(self.image_path(image_id)),
                "split": assign_split(m.get("split", "test"), m.get("drive_id") or self.trip.id),
                "clip_id": m.get("drive_id") or self.trip.id,
                "frame_index": frame_index, "time_s": round(frame_index / fps, 3),
                "width": self.out_size[0], "height": self.out_size[1],
                "time_of_day": m.get("time_of_day", ""), "weather": m.get("weather", ""),
                "privacy_boxes": "[]", "label_status": "kept", "labeler": self.labeler, "label_date": today(),
            }
            self.labels.put(row)
            self.labels.save()
            near = [r["image_id"] for r in self.labels.all()
                    if r["image_id"] != image_id and abs(float(r["time_s"]) - frame_index / fps) < 3.0]
            return {"row": self.labels.get(image_id), "near": near}

    def unkeep(self, image_id: str) -> dict:
        with self.lock:
            if self.labels.get(image_id) is None:
                raise ToolError(f"Unknown image {image_id}")
            self.labels.delete(image_id)
            self.labels.save()
            self.anns.delete_image(image_id)
            self.anns.save()
            p = self.image_path(image_id)
            if p.exists():
                p.unlink()
        return {"ok": True}

    def _ann_from_fields(self, row: dict, fields: dict) -> dict:
        return fields_to_row(row, fields, self.schema)

    @staticmethod
    def _set_box(item: dict, fields: dict) -> None:
        if "box" not in fields:
            return
        box = fields.get("box")
        if box and len(box) == 4:
            x1, y1, x2, y2 = (int(round(float(v))) for v in box)
            item["bbox_x1"], item["bbox_x2"] = sorted((x1, x2))
            item["bbox_y1"], item["bbox_y2"] = sorted((y1, y2))
        else:
            for k in ("bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2"):
                item[k] = ""

    def save_label(self, image_id: str, fields: dict, status: str) -> dict:
        """The owner's own work in the local app: the target box (for everyone) and the owner's annotation.

        status: 'box' saves only the target box; 'draft' / 'done' also save the owner's annotation;
        'excluded' drops the frame from the experiment.
        """
        if status not in ("box", "draft", "done", "excluded"):
            raise ToolError("Bad status.")
        with self.lock:
            item = self.labels.get(image_id)
            if item is None:
                raise ToolError(f"Unknown image {image_id}")
            item = dict(item)
            self._set_box(item, fields)
            if "notes" in fields:
                item["notes"] = str(fields.get("notes") or "").strip()
            self.labels.put(item)
            errors, warnings = [], []
            if status in ("draft", "done"):
                ann = self._ann_from_fields(dict(self.anns.get(image_id, OWNER) or {}), fields)
                errors, warnings = validate_label({**item, **ann}, self.schema, self.rule_ids, self.table)
                if status == "done" and errors:
                    status = "draft"
                ann.update({"image_id": image_id, "annotator": OWNER, "source": "local", "package_id": "",
                            "status": status, "unsure": "0", "comment": "", "saved_utc": utc_now()})
                self.anns.put(ann)
            elif status == "box" and not (item.get("bbox_x1") not in ("", None)):
                errors = ["Draw the target box first."]
            if status == "excluded":
                item = adjudicate(self.labels, self.anns, image_id, "exclude", None, "excluded by owner", self.labeler, self.required)
            else:
                item = merge_item(self.labels.get(image_id), self.anns.for_image(image_id), self.required)
                self.labels.put(item)
            self.labels.save()
            self.anns.save()
            return {"row": self.labels.get(image_id), "annotations": self.anns.for_image(image_id),
                    "errors": errors, "warnings": warnings}

    def adjudicate(self, image_id: str, choice: str, fields: dict | None, note: str) -> dict:
        with self.lock:
            item = self.labels.get(image_id)
            if item is None:
                raise ToolError(f"Unknown image {image_id}")
            final = None
            if choice == "edit":
                final = self._ann_from_fields({}, fields or {})
                errors, warnings = validate_label({**item, **final}, self.schema, self.rule_ids, self.table)
                if errors:
                    return {"row": item, "annotations": self.anns.for_image(image_id), "errors": errors, "warnings": warnings}
            row = adjudicate(self.labels, self.anns, image_id, choice, final, note, self.labeler, self.required)
            self.labels.save()
            return {"row": row, "annotations": self.anns.for_image(image_id), "errors": [], "warnings": []}

    def set_masks(self, masks: list) -> dict:
        clean = []
        for m in masks or []:
            if len(m) == 4:
                x1, y1, x2, y2 = (int(round(float(v))) for v in m)
                if abs(x2 - x1) >= 4 and abs(y2 - y1) >= 4:
                    clean.append([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)])
        with self.lock:
            self.trip.meta["masks"] = clean
            self.trip.save()
            self.mask_version += 1
            self.cache.clear()
            for r in self.labels.all():  # kept frames are re-rendered so every saved frame has the same masks
                self._render_kept(r["image_id"], int(r["frame_index"]))
        return {"masks": clean, "mask_version": self.mask_version, "rerendered": len(self.labels.all())}

    # ------------------------------------------------------------ blind re-check (risk R2)
    def _draw_recheck_sample(self) -> None:
        done = [r for r in self.labels.all() if r["label_status"] == "done"]
        if not done:
            raise ToolError("There are no finished labels to re-check yet.")
        groups: dict = {}
        for r in done:
            groups.setdefault(r["marking_type"], []).append(r)
        rng = random.Random(f"recheck:{self.trip.id}:{datetime.now():%Y-%m-%d}")
        picked = []
        for mt in sorted(groups):
            rows = sorted(groups[mt], key=lambda r: r["image_id"])
            n = min(len(rows), max(3, math.ceil(0.1 * len(rows))))
            picked += rng.sample(rows, n)
        self.recheck.rows.clear()
        for r in sorted(picked, key=lambda r: rng.random()):
            self.recheck.put({"image_id": r["image_id"], "recheck_status": "pending"})
        self.recheck.save()

    def save_recheck(self, image_id: str, fields: dict, status: str) -> dict:
        with self.lock:
            row = self.recheck.get(image_id)
            if row is None:
                raise ToolError(f"{image_id} is not in the re-check sample.")
            base = self.labels.get(image_id) or {}
            full = self._ann_from_fields(dict(base), fields)
            for k in RECHECK_COLUMNS:
                if k not in ("image_id", "recheck_status", "labeler", "label_date", "notes"):
                    row[k] = full.get(k, "")
            row["notes"] = str(fields.get("notes") or "")
            errors, _ = validate_label(full, self.schema, self.rule_ids)
            row["recheck_status"] = "done" if status == "done" and not errors else "pending"
            row["labeler"] = self.labeler
            row["label_date"] = today()
            self.recheck.put(row)
            self.recheck.save()
            return {"row": row, "errors": errors, "warnings": []}

    # ------------------------------------------------------------ ④ share with helpers
    def _reload(self) -> None:
        self.labels = LabelStore(self.paths.labels_csv(self.trip.id))
        self.anns = AnnotationStore(self.paths.annotations_csv(self.trip.id))

    def share_state(self) -> dict:
        from .annotations import has_box, load_annotators
        from .core import list_trip_ids
        trips, regions = [], set()
        registry = read_csv(self.paths.packages_csv)
        outstanding: dict = {}
        for r in registry:
            if r.get("status") in ("sent", "partial"):
                for iid in (r.get("items") or "").split(";"):
                    if iid:
                        outstanding.setdefault(iid, set()).add(r["annotator"])
        for tid in list_trip_ids(self.paths):
            t = Trip(self.paths, tid)
            regions.add(t.region)
            labels = LabelStore(self.paths.labels_csv(tid)).all()
            anns = AnnotationStore(self.paths.annotations_csv(tid))
            req = required_for(t.meta)
            row = {"trip_id": tid, "region": t.region, "time_of_day": t.meta.get("time_of_day", ""), "required": req,
                   "kept": len(labels), "boxed": 0, "need": 0, "mine_done": 0, "waiting": 0, "conflict": 0, "done": 0,
                   "excluded": 0, "no_box": 0, "outstanding": 0}
            for item in labels:
                st = item.get("label_status")
                row[{"kept": "no_box"}.get(st, st)] = row.get({"kept": "no_box"}.get(st, st), 0) + 1
                if st == "excluded" or not has_box(item):
                    continue
                row["boxed"] += 1
                done_by = {a["annotator"] for a in anns.for_image(item["image_id"]) if a.get("status") == "done"}
                mine = anns.get(item["image_id"], OWNER)
                if mine and mine.get("status") == "done" and mine.get("unsure") != "1":
                    row["mine_done"] += 1
                out = outstanding.get(item["image_id"], set()) - done_by
                row["outstanding"] += len(out)
                if st not in ("done", "conflict"):
                    row["need"] += max(0, req - len(done_by) - len(out))
            trips.append(row)
        names = load_annotators(self.paths)
        packages = []
        for r in registry:
            items = [i for i in (r.get("items") or "").split(";") if i]
            zips = sorted(self.paths.packages_dir.glob(f"{r['package_id']}_*.zip"))
            packages.append({**{k: r.get(k, "") for k in ("package_id", "batch", "annotator", "created_utc", "status",
                                                             "imported_utc", "done", "unsure", "practice_score")},
                             "name": names.get(r["annotator"], {}).get("name", ""), "n_items": len(items),
                             "file": zips[0].name if zips else "",
                             "size_bytes": zips[0].stat().st_size if zips else 0})
        open_cells = []
        for region in sorted(regions):
            for key, entry in self.table.get(region, {}).items():
                empty = [a for a, v in entry.get("actions", {}).items() if v == ""]
                if empty:
                    open_cells.append({"region": region, "key": key, "actions": empty,
                                       "note": entry.get("note", ""), "note_zh": entry.get("note_zh", "")})
        return {"trips": trips, "packages": packages,
                "helpers": [{"code": c, "name": v.get("name", "")} for c, v in sorted(names.items())],
                "open_cells": open_cells, "packages_dir": str(self.paths.packages_dir),
                "returned_dir": str(self.paths.data / "returned")}

    def make_packages(self, names: list, practice: int, max_per_person: int | None) -> dict:
        from .packages import build_packages
        log: list[str] = []
        before = {r["package_id"] for r in read_csv(self.paths.packages_csv)}
        with self.lock:
            try:
                build_packages(self.paths, names, None, practice=int(practice), max_per_person=max_per_person, log=log.append)
            except ToolError as e:
                return {"ok": False, "error": str(e), "log": log, "made": []}
        made = [p for p in self.share_state()["packages"] if p["package_id"] not in before]
        return {"ok": True, "log": log, "made": made}

    def import_files(self, files: list) -> dict:
        from .packages import import_results
        import re as _re
        folder = self.paths.data / "returned"
        folder.mkdir(parents=True, exist_ok=True)
        saved = []
        for f in files or []:
            name = _re.sub(r"[^A-Za-z0-9._-]", "_", Path(str(f.get("name") or "results.json")).name) or "results.json"
            if not name.endswith(".json"):
                name += ".json"
            text = str(f.get("text") or "")
            target = folder / name
            n = 1
            while target.exists() and target.read_text(encoding="utf-8", errors="replace") != text:
                target = folder / f"{name[:-5]}_{n}.json"
                n += 1
            target.write_text(text, encoding="utf-8")
            saved.append(str(target))
        return self._import(saved or [str(folder)])

    def import_folder(self) -> dict:
        folder = self.paths.data / "returned"
        folder.mkdir(parents=True, exist_ok=True)
        return self._import([str(folder)])

    def _import(self, inputs: list) -> dict:
        from .packages import import_results
        log: list[str] = []
        with self.lock:
            try:
                res = import_results(self.paths, inputs, log=log.append)
                counts = dict(res.get("counts") or {})
                files = [{"file": f, "annotator": code, **dict(st)} for f, code, st in res.get("files", [])]
                ok, err = True, ""
            except ToolError as e:
                counts, files, ok, err = {}, [], False, str(e)
            self._reload()
        return {"ok": ok, "error": err, "log": log, "files": files, "counts": counts}

    def open_folder(self, which: str) -> dict:
        import subprocess
        import sys as _sys
        target = {"packages": self.paths.packages_dir, "returned": self.paths.data / "returned",
                  "figures": self.paths.figures_root}.get(which)
        if target is None:
            raise ToolError("Unknown folder.")
        target.mkdir(parents=True, exist_ok=True)
        cmd = ["open", str(target)] if _sys.platform == "darwin" else (["explorer", str(target)] if _sys.platform.startswith("win") else ["xdg-open", str(target)])
        try:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return {"ok": True, "path": str(target)}
        except OSError:
            return {"ok": False, "path": str(target)}

    def close(self) -> None:
        self.reader.close()


class ImageApp(App):
    """The same app for public-dataset images: ① picks images from the candidate index instead of a video."""

    def __init__(self, paths: Paths, trip: Trip, labeler: str, recheck: bool = False, new_sample: bool = False):
        from .imagesets import Picker
        self.paths, self.trip, self.labeler = paths, trip, labeler
        self.schema = load_schema(paths)
        self.table = load_action_rules(paths)
        self.passages = load_rule_passages(paths, trip.region)
        self.rule_ids = {p["rule_id"] for p in self.passages}
        self.reader = None
        self.picker = Picker(paths, trip)
        self.scan = []
        self.labels = LabelStore(paths.labels_csv(trip.id))
        self.anns = AnnotationStore(paths.annotations_csv(trip.id))
        self.required = required_for(trip.meta)
        self.lock = threading.RLock()
        self.cache: OrderedDict = OrderedDict()
        self.mask_version = 0
        self.out_size = (1280, 720)
        self.quality = 95
        self.recheck_mode = recheck
        self.recheck = None
        if recheck:
            self.recheck = LabelStore(paths.recheck_csv(trip.id), RECHECK_COLUMNS)
            if new_sample or not self.recheck.rows:
                self._draw_recheck_sample()

    def state(self) -> dict:
        from .imagesets import GROUPS, quota_table
        m = self.trip.meta
        d = {
            "trip": {k: m.get(k) for k in ("trip_id", "region", "dataset", "time_of_day", "weather", "road_type",
                                          "recorded_date", "split", "masks", "trim")},
            "output": {"width": self.out_size[0], "height": self.out_size[1]},
            "scan": [], "scan_summary": {},
            "labels": self.labels.all(), "annotations": self.anns.all(), "required": self.required, "owner": OWNER,
            "schema": self.schema, "rules_table": self.table.get(self.trip.region, {}),
            "passages": self._passages_with_zh(), "labeler": self.labeler, "recheck_mode": self.recheck_mode,
            "recheck": self.recheck.all() if self.recheck else [], "mask_version": self.mask_version,
        }
        d.update({"kind": "images", "video": {"fps": 1, "width": 1280, "height": 720},
                  "set": {k: m.get(k) for k in ("set_id", "dataset", "region", "split_unit", "license", "quota")},
                  "index": m.get("index", {}), "facets": self.picker.facets, "groups": GROUPS,
                  "quota": quota_table(self.trip, self.labels, self.anns),
                  "workspace": str(self.paths.data), "labels_dir": str(self.paths.labels_dir)})
        return d

    def quota(self) -> dict:
        from .imagesets import quota_table
        return quota_table(self.trip, self.labels, self.anns)

    def candidates(self, q: dict) -> dict:
        return self.picker.query(self.labels, pool=q.get("pool", "dev"), hint=q.get("hint", ""), tod=q.get("tod", ""),
                                 hide_kept=q.get("hide", "1") == "1", page=int(q.get("page", 0) or 0),
                                 size=int(q.get("size", 24) or 24), seed=q.get("seed", "6216"))

    def candidate(self, cand_id: str) -> dict:
        return self.picker.details(cand_id, self.labels)

    def cand_image(self, cand_id: str, width: int) -> bytes:
        key = ("cand", cand_id, int(width))
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
        src = self.picker.source_file(cand_id)
        if not src.exists():
            raise ToolError(f"Image missing: {src}")
        img = read_image(src)
        width = max(120, min(int(width), img.shape[1]))
        h = int(round(img.shape[0] * width / img.shape[1]))
        data = encode_jpeg(resize(img, (width, h)), 82)
        with self.lock:
            self.cache[key] = data
            while len(self.cache) > 600:
                self.cache.popitem(last=False)
        return data

    def pick(self, cand_id: str, group: str) -> dict:
        with self.lock:
            res = self.picker.pick(self.labels, cand_id, group, self.labeler)
            res["quota"] = self.quota()
            return res

    def image(self, image_id: str, width: int | None = None) -> bytes:
        row = self.labels.get(image_id)
        if row is None and not (self.recheck and self.recheck.get(image_id)):
            raise ToolError(f"Unknown image {image_id}")
        p = self.image_path(image_id)
        if not p.exists():
            self._render_kept(image_id, 0)
        if not width:
            return p.read_bytes()
        img = read_image(p)
        h = int(round(img.shape[0] * width / img.shape[1]))
        return encode_jpeg(resize(img, (int(width), h)), 80)

    def _render_kept(self, image_id: str, frame_index: int) -> None:
        """Copy the picked image again from the dataset (if the copy was deleted)."""
        import shutil
        row = self.labels.get(image_id)
        if row is None:
            raise ToolError(f"Unknown image {image_id}")
        src = self.picker.source / row["source_ref"]
        if not src.exists():
            raise ToolError(f"Image missing: {src}")
        dest = self.image_path(image_id)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    def keep(self, frame_index: int) -> dict:
        raise ToolError("Dataset images are picked from the list (① pick images).")

    def preview(self, frame_index: int, width: int) -> bytes:
        raise ToolError("No video in a dataset workspace.")

    def set_masks(self, masks: list) -> dict:
        raise ToolError("Masks are only for own videos (burned-in date / speed overlays).")

    def close(self) -> None:
        pass


def make_handler(app: App):
    class Handler(BaseHTTPRequestHandler):
        server_version = "video_tool"

        def log_message(self, fmt, *args):  # keep the terminal quiet
            pass

        def _send(self, code: int, body: bytes, ctype: str, cache: bool = False):
            try:
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "max-age=3600" if cache else "no-store")
                self.end_headers()
                self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError):
                pass  # the browser moved on to another frame before this one arrived

        def _json(self, obj, code: int = 200):
            self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

        def _error(self, e: Exception):
            msg = str(e) if isinstance(e, ToolError) else f"{type(e).__name__}: {e}"
            if not isinstance(e, ToolError):
                import traceback
                traceback.print_exc()
            self._json({"error": msg}, 400 if isinstance(e, ToolError) else 500)

        def do_GET(self):
            u = urlparse(self.path)
            q = {k: v[0] for k, v in parse_qs(u.query).items()}
            try:
                if u.path in ("/", "/index.html"):
                    return self._send(200, (WEB_DIR / "index.html").read_bytes(), "text/html; charset=utf-8")
                if u.path.startswith("/static/"):
                    name = Path(u.path).name
                    f = WEB_DIR / name
                    if not f.is_file():
                        return self._send(404, b"not found", "text/plain")
                    ctype = {"js": "text/javascript", "css": "text/css"}.get(name.rsplit(".", 1)[-1], "application/octet-stream")
                    return self._send(200, f.read_bytes(), ctype + "; charset=utf-8")
                if u.path == "/api/instance":  # lets a second start find this window (see serve)
                    return self._json({"tool": "video_tool", "data": str(app.paths.data), "trip": app.trip.id})
                if u.path == "/api/state":
                    return self._json(app.state())
                if u.path == "/api/share":
                    return self._json(app.share_state())
                if u.path == "/api/preview":
                    data = app.preview(int(q["f"]), int(q.get("w", 1280)))
                    return self._send(200, data, "image/jpeg", cache=True)
                if u.path == "/api/image":
                    w = int(q["w"]) if q.get("w") else None
                    return self._send(200, app.image(q["id"], w), "image/jpeg")
                if isinstance(app, ImageApp):
                    if u.path == "/api/candidates":
                        return self._json(app.candidates(q))
                    if u.path == "/api/candidate":
                        return self._json(app.candidate(q["c"]))
                    if u.path == "/api/cand_image":
                        return self._send(200, app.cand_image(q["c"], int(q.get("w", 320))), "image/jpeg", cache=True)
                    if u.path == "/api/quota":
                        return self._json(app.quota())
                return self._send(404, b"not found", "text/plain")
            except Exception as e:  # noqa: BLE001 - report every error to the page
                return self._error(e)

        def do_POST(self):
            u = urlparse(self.path)
            try:
                n = int(self.headers.get("Content-Length") or 0)
                body = json.loads(self.rfile.read(n) or b"{}")
                if u.path == "/api/keep":
                    return self._json(app.keep(body["frame_index"]))
                if u.path == "/api/pick" and isinstance(app, ImageApp):
                    return self._json(app.pick(body["cand_id"], body.get("group", "")))
                if u.path == "/api/unkeep":
                    return self._json(app.unkeep(body["image_id"]))
                if u.path == "/api/label":
                    return self._json(app.save_label(body["image_id"], body.get("fields", {}), body.get("status", "draft")))
                if u.path == "/api/adjudicate":
                    return self._json(app.adjudicate(body["image_id"], body.get("choice", ""), body.get("fields"), body.get("note", "")))
                if u.path == "/api/package":
                    mx = body.get("max")
                    return self._json(app.make_packages(body.get("names") or [], int(body.get("practice", 6)),
                                                        int(mx) if mx not in (None, "", 0, "0") else None))
                if u.path == "/api/import":
                    return self._json(app.import_files(body.get("files") or []))
                if u.path == "/api/import_folder":
                    return self._json(app.import_folder())
                if u.path == "/api/open":
                    return self._json(app.open_folder(body.get("which", "")))
                if u.path == "/api/masks":
                    return self._json(app.set_masks(body.get("masks", [])))
                if u.path == "/api/recheck":
                    if not app.recheck:
                        raise ToolError("Start the tool with --recheck to re-check labels.")
                    return self._json(app.save_recheck(body["image_id"], body.get("fields", {}), body.get("status", "draft")))
                return self._send(404, b"not found", "text/plain")
            except Exception as e:  # noqa: BLE001
                return self._error(e)

    return Handler


LOCK_FILE = "labeling_tool.lock"


def running_instance(paths: Paths) -> str | None:
    """The address of a labeling window that is already open on this data folder, or None.

    Several windows may run at once (each picks a free port), but only one per data folder: each window keeps
    the label files in memory and writes them back, so two windows on the same folder would overwrite each other."""
    import urllib.request
    lock = paths.data / LOCK_FILE
    if not lock.exists():
        return None
    try:
        info = json.loads(lock.read_text(encoding="utf-8"))
        url = f"http://127.0.0.1:{int(info['port'])}/"
        with urllib.request.urlopen(url + "api/instance", timeout=2) as r:
            me = json.loads(r.read())
        return url if me.get("tool") == "video_tool" and me.get("data") == str(paths.data) else None
    except Exception:  # noqa: BLE001 - no answer: the lock is left over from a window that was closed
        return None


def serve(paths: Paths, trip: Trip, labeler: str, port: int = 8765, open_browser: bool = True,
          recheck: bool = False, new_sample: bool = False, log=print) -> None:
    other = running_instance(paths)
    if other:
        if open_browser:
            webbrowser.open(other)
        raise ToolError(f"This data folder is already open in the labeling tool at {other} . Use that window "
                        "(other data folders can be open at the same time).")
    cls = ImageApp if trip.kind == "images" else App
    app = cls(paths, trip, labeler, recheck=recheck, new_sample=new_sample)
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
    lock = paths.data / LOCK_FILE
    lock_text = json.dumps({"port": port, "trip": trip.id, "started": datetime.now().isoformat(timespec="seconds")})
    try:
        lock.write_text(lock_text, encoding="utf-8")
    except OSError:
        pass
    log(f"Labeling tool for '{trip.id}' is running at {url}")
    log("Everything is saved as you go. Press Ctrl+C here to stop.")
    if open_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        log("\nStopped. Labels are in " + str(paths.labels_csv(trip.id)))
    finally:
        httpd.server_close()
        app.close()
        try:
            if lock.read_text(encoding="utf-8") == lock_text:
                lock.unlink()
        except OSError:
            pass

