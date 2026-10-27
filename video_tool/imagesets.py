"""Public-dataset images (BDD100K for the US, CULane for China): pick, label and share them like own frames.

One workspace (data folder) per dataset, separate from the own-video folder:

  On the data drive, e.g. /Volumes/T9/数据集/bdd100k (ignored by Git):
    workspace.json                   marks the folder as a dataset workspace (which dataset)
    index/<set>/candidates.csv       every image of the dataset with its hints (built once by `images init`)
    selected/<set>/<image_id>.jpg    copies of the images you picked (the originals are never changed)
    packages/  returned/             labeling packages for helpers and the results they send back
    report_figures/<set>/            copies with plates and faces blurred, for reports only
    annotators.json                  private: helper code -> real name

  In Git (repository):
    labels/<dataset>/<set>.set.json         where the dataset is, region, license, quotas, index summary
    labels/<dataset>/<set>.labels.csv       one row per picked image: target box + FINAL label
    labels/<dataset>/<set>.annotations.csv  every independent label
    labels/<dataset>/packages.csv           packages sent to helpers (codes only)
    labels/labels.csv, labels/split_v1.csv  all final labels of every workspace together (`combine`)

The dataset's own labels are only used to find candidates and to suggest a target box. Every label that is
scored (type, visibility, actions, rules) is made by hand with the same guide as the own frames.
"""
from __future__ import annotations

import ast
import hashlib
import json
import shutil
from collections import Counter, defaultdict
from pathlib import Path

from . import __version__
from .core import (LABEL_COLUMNS, OWNER, WORKSPACE_FILE, LabelStore, Paths, ToolError, Trip, assign_split,
                   list_trip_ids, read_csv, read_json, today, utc_now, write_csv, write_json)

GROUPS = ["solid", "dashed", "yellow", "arrow", "degraded"]
GROUP_OF_TYPE = {
    "white_solid": "solid", "white_double_solid": "solid",
    "white_dashed": "dashed",
    "yellow_dashed": "yellow", "yellow_solid": "yellow", "yellow_double_solid": "yellow",
    "yellow_solid_dashed": "yellow", "two_way_left_turn_lane": "yellow",
    "arrow": "arrow",
}
# Milestone 3: 6 development images per marking type and region; 30 test images per type and region plus
# 30 degraded test images per region.
DEFAULT_QUOTA = {"dev": {"solid": 6, "dashed": 6, "yellow": 6, "arrow": 6, "degraded": 0},
                 "test": {"solid": 30, "dashed": 30, "yellow": 30, "arrow": 30, "degraded": 30}}

DATASETS = {
    "bdd100k": {
        "set_id": "bdd100k_val", "dataset": "BDD100K", "region": "US",
        "default_source": "data/extracted/bdd100k/mirror/val",
        "license": ("BDD100K (Yu et al., CVPR 2020), 2020 label release, validation split, Dataset Ninja mirror. "
                    "Copyright (c) 2018 The Regents of the University of California. Educational, research and "
                    "not-for-profit use; copies keep the copyright notice."),
        "split_unit": "image (each BDD100K image comes from a different video)",
    },
    "culane": {
        "set_id": "culane_test", "dataset": "CULane", "region": "CN",
        "default_source": "data/extracted/culane",
        "license": ("CULane (Pan et al., AAAI 2018), test split. Rights reserved by SenseTime Group Limited. "
                    "Free for non-commercial research with citation; the dataset or modified versions may not be "
                    "redistributed. Helpers label under a written no-sharing notice and delete the images afterwards."),
        "split_unit": "video clip (driver folder + clip)",
    },
}

# BDD100K lane attributes -> the hint shown when picking (the closest marking type of this project)
BDD_HINT = {
    ("single white", "solid"): "white_solid", ("single white", "dashed"): "white_dashed",
    ("double white", "solid"): "white_double_solid", ("double white", "dashed"): "white_double_solid",
    ("single yellow", "solid"): "yellow_solid", ("single yellow", "dashed"): "yellow_dashed",
    ("double yellow", "solid"): "yellow_double_solid", ("double yellow", "dashed"): "yellow_solid_dashed",
}
HINT_GROUP = {
    "white_solid": "solid", "white_double_solid": "solid", "white_dashed": "dashed",
    "yellow_solid": "yellow", "yellow_dashed": "yellow", "yellow_double_solid": "yellow", "yellow_solid_dashed": "yellow",
    "crosswalk": "arrow", "no_lane": "degraded",
    "cu_arrow": "arrow", "cu_noline": "degraded",
}
CULANE_CATEGORIES = ["normal", "crowd", "hlight", "shadow", "noline", "arrow", "curve", "cross", "night"]
CANDIDATE_COLUMNS = ["cand_id", "rel", "clip_id", "pool", "width", "height", "time_of_day", "weather", "scene",
                     "category", "hints", "boxes"]


def group_of(row: dict, ann: dict | None = None) -> str:
    """The quota cell of a picked image: its labeled type if there is one, else the group it was picked for."""
    if row.get("pick_group") == "degraded":
        return "degraded"
    mt = row.get("marking_type") or (ann or {}).get("marking_type") or ""
    return GROUP_OF_TYPE.get(mt) or row.get("pick_group") or "other"


# ------------------------------------------------------------------ geometry helpers

def _ends(pts: list) -> tuple:
    a, b = pts[0], pts[-1]
    return (a, b) if a[1] <= b[1] else (b, a)  # (top, bottom)


def _close(p, q, tol) -> bool:
    return abs(p[0] - q[0]) <= tol and abs(p[1] - q[1]) <= tol


def _box_of(points: list, w: int, h: int, margin: int = 12) -> list:
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return [max(0, int(min(xs)) - margin), max(0, int(min(ys)) - margin),
            min(w, int(max(xs)) + margin), min(h, int(max(ys)) + margin)]


def group_polylines(lines: list, w: int, h: int, keep: int = 3) -> list:
    """BDD100K draws both edges of a painted line: merge edges that belong together, then box each marking.

    Nearest markings first (bottom point closest to the bottom centre of the image)."""
    groups: list[list] = []
    for pts in lines:
        top, bot = _ends(pts)
        for g in groups:
            gt, gb = _ends(g[0])
            tol_b = 25 + 0.12 * max(bot[1], gb[1])
            tol_t = 25 + 0.12 * max(top[1], gt[1])
            if _close(bot, gb, tol_b) and _close(top, gt, tol_t):
                g.append(pts)
                break
        else:
            groups.append([pts])
    boxes = []
    for g in groups:
        allp = [p for pts in g for p in pts]
        bot = max(allp, key=lambda p: p[1])
        boxes.append(((abs(bot[0] - w / 2) + (h - bot[1]) * 2), _box_of(allp, w, h)))
    boxes.sort(key=lambda t: t[0])
    return [b for _, b in boxes if b[2] - b[0] >= 8 and b[3] - b[1] >= 8][:keep]


def culane_lane_boxes(lines_file: Path, w: int = 1640, h: int = 590) -> list:
    """Boxes around the two boundaries of our lane (CULane lists up to 4 lines, left to right)."""
    if not lines_file.exists():
        return []
    lanes = []
    for line in lines_file.read_text(encoding="utf-8", errors="replace").splitlines():
        v = [float(x) for x in line.split()]
        pts = [(v[i], v[i + 1]) for i in range(0, len(v) - 1, 2)]
        pts = [p for p in pts if 0 <= p[0] < w and p[1] >= h * 0.55]  # the near half, inside the image
        if len(pts) >= 2:
            lanes.append(pts)
    if not lanes:
        return []
    bottom_x = [max(p, key=lambda q: q[1])[0] for p in lanes]
    left = [i for i, x in enumerate(bottom_x) if x < w / 2]
    right = [i for i, x in enumerate(bottom_x) if x >= w / 2]
    out = []
    if left:
        out.append(_box_of(lanes[max(left, key=lambda i: bottom_x[i])], w, h))
    if right:
        out.append(_box_of(lanes[min(right, key=lambda i: bottom_x[i])], w, h))
    return out


# ------------------------------------------------------------------ index

def _bdd_index(source: Path, log=print) -> list[dict]:
    ann_dir, img_dir = source / "ann", source / "img"
    if not ann_dir.is_dir() or not img_dir.is_dir():
        raise ToolError(f"{source} should contain ann/ and img/ (the Dataset Ninja mirror of BDD100K, val split).")
    files = sorted(p for p in ann_dir.glob("*.json") if not p.name.startswith("._"))
    if not files:
        raise ToolError(f"No label files in {ann_dir}.")
    rows, bad = [], []
    for n, f in enumerate(files, 1):
        if n % 1000 == 0:
            log(f"  {n} / {len(files)} label files read")
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            bad.append(f.name)
            continue
        name = f.name[:-len(".json")]  # e.g. b1c66a42-6f7d68ca.jpg
        stem = name.rsplit(".", 1)[0]
        size = d.get("size") or {}
        w, h = int(size.get("width", 1280)), int(size.get("height", 720))
        tags = {t.get("name"): t.get("value") for t in d.get("tags", [])}
        lines = defaultdict(list)
        crosswalk = False
        for o in d.get("objects", []):
            if o.get("classTitle") != "lane":
                continue
            attrs = {}
            for t in o.get("tags", []):
                if t.get("name") == "attributes":
                    try:
                        attrs = ast.literal_eval(t.get("value") or "{}")
                    except (ValueError, SyntaxError):
                        attrs = {}
            typ, style = str(attrs.get("laneType", "")).lower(), str(attrs.get("laneStyle", "")).lower()
            if typ == "crosswalk":
                crosswalk = True
                continue
            if str(attrs.get("laneDirection", "parallel")).lower() != "parallel":
                continue
            hint = BDD_HINT.get((typ, style))
            pts = (o.get("points") or {}).get("exterior") or []
            if hint and len(pts) >= 2:
                lines[hint].append(pts)
        boxes = {hint: group_polylines(pl, w, h) for hint, pl in lines.items()}
        hints = sorted(h for h, b in boxes.items() if b)
        if crosswalk:
            hints.append("crosswalk")
        if not lines:
            hints.append("no_lane")
        rows.append({"cand_id": stem, "rel": f"img/{name}", "clip_id": stem, "pool": assign_split("hash", stem),
                     "width": w, "height": h, "time_of_day": tags.get("timeofday", "") or "",
                     "weather": tags.get("weather", "") or "", "scene": tags.get("scene", "") or "", "category": "",
                     "hints": ";".join(hints), "boxes": json.dumps({k: v for k, v in boxes.items() if v}, separators=(",", ":"))})
    if bad:
        log(f"  {len(bad)} label files could not be read and were skipped, e.g. {bad[0]}")
    return rows


def culane_key(rel: str) -> tuple[str, str]:
    """driver_100_30frame/05251551_0440.MP4/04560.jpg -> ('d100_05251551_0440_04560', 'driver_100_30frame/05251551_0440.MP4')"""
    parts = rel.strip("/").split("/")
    if len(parts) != 3:
        raise ToolError(f"Unexpected CULane path: {rel}")
    driver, clip, frame = parts
    num = driver.split("_")[1] if "_" in driver else driver
    return f"d{num}_{clip.split('.')[0]}_{frame.rsplit('.', 1)[0]}", f"{driver}/{clip}"


def _culane_index(source: Path, log=print) -> list[dict]:
    split_dir = source / "list" / "test_split"
    if not split_dir.is_dir():
        raise ToolError(f"{source} should contain list/test_split/ (CULane test split lists).")
    rows, seen = [], set()
    for f in sorted(split_dir.glob("test*_*.txt")):
        if f.name.startswith("._"):
            continue
        cat = f.stem.split("_", 1)[1]
        for line in f.read_text(encoding="utf-8").splitlines():
            rel = line.strip().strip("/")
            if not rel or rel in seen:
                continue
            seen.add(rel)
            key, clip = culane_key(rel)
            rows.append({"cand_id": key, "rel": rel, "clip_id": clip, "pool": assign_split("hash", clip),
                         "width": 1640, "height": 590, "time_of_day": "night" if cat == "night" else "",
                         "weather": "", "scene": "", "category": cat, "hints": "cu_" + cat, "boxes": "{}"})
    if not rows:
        raise ToolError(f"No frames listed in {split_dir}.")
    return rows


def resolve_source(paths: Paths, dataset: str, source: str | None) -> Path:
    cfg = DATASETS[dataset]
    p = Path(source).expanduser() if source else paths.repo / cfg["default_source"]
    if dataset == "bdd100k" and (p / "val").is_dir() and not (p / "ann").is_dir():
        p = p / "val"
    if not p.is_dir():
        raise ToolError(f"Dataset folder not found: {p}. Give it with --source.")
    return p.resolve()


def init_workspace(repo: str | Path | None, data: str | Path, dataset: str, source: str | None = None,
                   rebuild_index: bool = False, log=print) -> Paths:
    """Mark a data folder as the workspace of one dataset, register its image set and build the candidate index."""
    if dataset not in DATASETS:
        raise ToolError(f"Unknown dataset '{dataset}'. Use one of: {', '.join(DATASETS)}")
    cfg = DATASETS[dataset]
    base = Paths.discover(repo, data)
    if not (base.data / WORKSPACE_FILE).exists() and any((base.data / d / "own_video").exists() for d in ("raw", "interim", "extracted")):
        raise ToolError(f"{base.data} is the own-video folder. Use a separate folder for {cfg['dataset']}, e.g. a sibling folder named {dataset}.")
    ws_file = base.data / WORKSPACE_FILE
    if ws_file.exists():
        w = read_json(ws_file)
        if w.get("collection") != dataset:
            raise ToolError(f"{base.data} is the workspace of {w.get('collection')}. Use a separate folder for {dataset}.")
    else:
        write_json(ws_file, {"collection": dataset, "kind": "images", "dataset": cfg["dataset"], "region": cfg["region"],
                             "created_utc": utc_now(), "note": "Dataset workspace of video_tool. See video_tool/imagesets.py."})
    paths = Paths.discover(repo, data)
    src = resolve_source(paths, dataset, source)
    set_id = cfg["set_id"]
    meta_path = paths.trip_json(set_id)
    meta = read_json(meta_path) if meta_path.exists() else None
    if meta and Path(meta["source_root"]) != src:
        log(f"Note: the dataset folder changed from {meta['source_root']} to {src}.")
    cand_path = paths.scan_csv(set_id)
    rebuilt = rebuild_index or not cand_path.exists()
    if rebuilt:
        log(f"Reading the {cfg['dataset']} labels in {src} (once; this can take a few minutes) ...")
        rows = _bdd_index(src, log) if dataset == "bdd100k" else _culane_index(src, log)
        write_csv(cand_path, rows, CANDIDATE_COLUMNS)
    else:
        rows = read_csv(cand_path)
        log(f"Candidate index already there ({len(rows)} images). Use --rebuild-index to read the dataset again.")
    pools = Counter(r["pool"] for r in rows)
    hints = Counter(h for r in rows for h in r["hints"].split(";") if h)
    built = utc_now() if rebuilt else ((meta or {}).get("index", {}).get("built_utc") or utc_now())
    index = {"built_utc": built, "images": len(rows), "dev_pool": pools["dev"], "test_pool": pools["test"],
             "hints": dict(sorted(hints.items()))}
    new = meta is None
    meta = meta or {"trip_id": set_id, "set_id": set_id, "kind": "images", "registered_utc": utc_now(),
                    "annotators_required": 2, "split": "hash", "quota": DEFAULT_QUOTA,
                    "time_of_day": "", "weather": ""}
    meta.update({"dataset": cfg["dataset"], "region": cfg["region"], "source_root": str(src), "license": cfg["license"],
                 "split_unit": cfg["split_unit"], "index": index, "tool_version": __version__, "updated_utc": utc_now()})
    write_json(meta_path, meta)
    if not paths.labels_csv(set_id).exists():
        write_csv(paths.labels_csv(set_id), [], LABEL_COLUMNS)
    log(f"{'Set up' if new else 'Updated'} {set_id}: {len(rows)} images ({pools['dev']} in the development pool, "
        f"{pools['test']} in the test pool).")
    log(f"  labels: {paths.labels_dir}")
    log(f"  picked images, packages, results: {paths.data}")
    log(f"Next: python -m video_tool --data \"{paths.data}\" label")
    return paths


# ------------------------------------------------------------------ picking

class Picker:
    """Candidate browsing, picking into quota cells, and suggested boxes for one image set."""

    def __init__(self, paths: Paths, trip: Trip):
        self.paths, self.trip = paths, trip
        self.source = Path(trip.meta["source_root"])
        if not self.source.exists():
            raise ToolError(f"The dataset folder {self.source} is not there. Is the external drive connected?")
        self.cands = read_csv(paths.scan_csv(trip.id))
        if not self.cands:
            raise ToolError(f"No candidate index for {trip.id}. Run: python -m video_tool --data \"{paths.data}\" images init "
                            f"{paths.collection}")
        self.by_id = {c["cand_id"]: c for c in self.cands}
        self._orders: dict[str, list] = {}
        self._culane_boxes: dict[str, list] = {}
        self.facets = self._facets()

    def image_id(self, cand_id: str) -> str:
        return f"{self.trip.id}__{cand_id}"

    def cand_of(self, image_id: str) -> str:
        return image_id.split("__", 1)[1] if "__" in image_id else image_id

    def _facets(self) -> dict:
        out = {}
        for pool in ("dev", "test", "all"):
            c = Counter()
            for r in self.cands:
                if pool != "all" and r["pool"] != pool:
                    continue
                c["*"] += 1
                for h in r["hints"].split(";"):
                    if h:
                        c[h] += 1
            out[pool] = dict(c)
        tods = Counter(r["time_of_day"] for r in self.cands if r["time_of_day"])
        return {"hints": out, "time_of_day": dict(tods)}

    def order(self, seed: str) -> list:
        if seed not in self._orders:
            self._orders[seed] = sorted(self.cands, key=lambda r: hashlib.sha1(f"{seed}:{r['cand_id']}".encode()).hexdigest())
            if len(self._orders) > 8:
                self._orders.pop(next(iter(self._orders)))
        return self._orders[seed]

    def query(self, labels: LabelStore, pool: str = "dev", hint: str = "", tod: str = "", hide_kept: bool = True,
              page: int = 0, size: int = 24, seed: str = "6216") -> dict:
        kept = {self.cand_of(iid): iid for iid in labels.rows}
        rows = []
        for r in self.order(seed or "6216"):
            if pool in ("dev", "test") and r["pool"] != pool:
                continue
            if hint and hint not in r["hints"].split(";"):
                continue
            if tod and r["time_of_day"] != tod:
                continue
            if hide_kept and r["cand_id"] in kept:
                continue
            rows.append(r)
        size = max(1, min(int(size), 60))
        pages = max(1, (len(rows) + size - 1) // size)
        page = max(0, min(int(page), pages - 1))
        items = []
        for r in rows[page * size:(page + 1) * size]:
            items.append({**{k: r[k] for k in ("cand_id", "rel", "clip_id", "pool", "time_of_day", "weather", "scene", "category")},
                          "hints": [h for h in r["hints"].split(";") if h], "kept": kept.get(r["cand_id"], ""),
                          "width": int(r["width"]), "height": int(r["height"])})
        return {"total": len(rows), "page": page, "pages": pages, "size": size, "items": items}

    def boxes(self, cand_id: str) -> dict:
        r = self.by_id.get(cand_id)
        if r is None:
            raise ToolError(f"Unknown image {cand_id}")
        if self.trip.meta.get("dataset") == "CULane":
            if cand_id not in self._culane_boxes:
                lines = self.source / (r["rel"][:-len(".jpg")] + ".lines.txt")
                self._culane_boxes[cand_id] = culane_lane_boxes(lines, int(r["width"]), int(r["height"]))
            return {"lane": self._culane_boxes[cand_id]} if self._culane_boxes[cand_id] else {}
        try:
            return json.loads(r["boxes"] or "{}")
        except json.JSONDecodeError:
            return {}

    def source_file(self, cand_id: str) -> Path:
        r = self.by_id.get(cand_id)
        if r is None:
            raise ToolError(f"Unknown image {cand_id}")
        return self.source / r["rel"]

    def details(self, cand_id: str, labels: LabelStore) -> dict:
        r = self.by_id.get(cand_id)
        if r is None:
            raise ToolError(f"Unknown image {cand_id}")
        clip_test = sum(1 for x in labels.all() if x.get("clip_id") == r["clip_id"] and x.get("split") == "test"
                        and x.get("label_status") != "excluded")
        return {**{k: r[k] for k in ("cand_id", "rel", "clip_id", "pool", "time_of_day", "weather", "scene", "category")},
                "hints": [h for h in r["hints"].split(";") if h], "boxes": self.boxes(cand_id),
                "width": int(r["width"]), "height": int(r["height"]),
                "kept": self.image_id(cand_id) if self.image_id(cand_id) in labels.rows else "", "clip_test_kept": clip_test}

    def suggested(self, cand_id: str, group: str) -> list:
        """Suggested target boxes for the group the image is picked for (nearest first)."""
        boxes = self.boxes(cand_id)
        if "lane" in boxes:  # CULane: our lane's two boundaries
            return boxes["lane"] if group != "arrow" else []
        want = [h for h, g in HINT_GROUP.items() if g == group and h in boxes]
        out = [b for h in want for b in boxes[h]]
        if not out and group == "degraded":
            out = [b for v in boxes.values() for b in v]
        return out[:3]

    def pick(self, labels: LabelStore, cand_id: str, group: str, labeler: str) -> dict:
        if group not in GROUPS:
            raise ToolError("Choose what the image is picked for (1–5).")
        r = self.by_id.get(cand_id)
        if r is None:
            raise ToolError(f"Unknown image {cand_id}")
        iid = self.image_id(cand_id)
        if iid in labels.rows:
            return {"row": labels.get(iid), "existing": True, "warnings": []}
        warnings = []
        if r["pool"] == "test" and self.trip.meta.get("dataset") == "CULane":
            n = sum(1 for x in labels.all() if x.get("clip_id") == r["clip_id"] and x.get("split") == "test"
                    and x.get("label_status") != "excluded")
            if n >= 2:
                raise ToolError("This clip already has 2 test images (section 6.5 allows at most 2 per clip). Pick another clip.")
        q = self.trip.meta.get("quota") or DEFAULT_QUOTA
        have = quota_counts(labels, None).get((r["pool"], group), 0)
        target = int(q.get(r["pool"], {}).get(group, 0))
        if have >= target:
            warnings.append("over_quota")
        src = self.source_file(cand_id)
        if not src.exists():
            raise ToolError(f"Image missing: {src}")
        dest = self.paths.frames_dir(self.trip.id) / f"{iid}.jpg"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copy2(src, dest)
        seq = max([int(x["frame_index"]) for x in labels.all() if str(x.get("frame_index", "")).isdigit()] or [0]) + 1
        m = self.trip.meta
        row = {"image_id": iid, "region": m["region"], "dataset": m["dataset"], "source_path": self.paths.rel(dest),
               "split": r["pool"], "clip_id": r["clip_id"], "frame_index": seq, "time_s": "",
               "width": r["width"], "height": r["height"], "time_of_day": r["time_of_day"], "weather": r["weather"],
               "privacy_boxes": "[]", "label_status": "kept", "labeler": labeler, "label_date": today(),
               "pick_group": group, "box_hints": json.dumps(self.suggested(cand_id, group)), "source_ref": r["rel"]}
        labels.put(row)
        labels.save()
        return {"row": labels.get(iid), "existing": False, "warnings": warnings}


def quota_counts(labels: LabelStore, anns=None) -> Counter:
    c = Counter()
    for r in labels.all():
        if r.get("label_status") == "excluded":
            continue
        ann = anns.get(r["image_id"], OWNER) if anns is not None else None
        c[(r.get("split", ""), group_of(r, ann))] += 1
    return c


def quota_table(trip: Trip, labels: LabelStore, anns=None) -> dict:
    q = trip.meta.get("quota") or DEFAULT_QUOTA
    have = quota_counts(labels, anns)
    rows = []
    for g in GROUPS:
        rows.append({"group": g, **{f"{p}_have": have.get((p, g), 0) for p in ("dev", "test")},
                     **{f"{p}_target": int(q.get(p, {}).get(g, 0)) for p in ("dev", "test")}})
    other = sum(v for (p, g), v in have.items() if g == "other")
    return {"rows": rows, "other": other,
            "totals": {p: {"have": sum(have.get((p, g), 0) for g in GROUPS), "target": sum(int(v) for v in q.get(p, {}).values())}
                       for p in ("dev", "test")}}


# ------------------------------------------------------------------ dHash check across the split (section 6.5)

def dhash(path: Path, size: int = 8):
    import cv2
    import numpy as np
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    g = cv2.resize(img, (size + 1, size), interpolation=cv2.INTER_AREA).astype(np.int16)
    return np.packbits((g[:, 1:] > g[:, :-1]).ravel())


def near_duplicates_across_split(paths: Paths, rows: list[dict], max_bits: int = 4) -> list[tuple]:
    import numpy as np
    hashes = {}
    for r in rows:
        if r.get("label_status") == "excluded" or r.get("split") not in ("dev", "test"):
            continue
        h = dhash(paths.data / r["source_path"])
        if h is not None:
            hashes[r["image_id"]] = (r["split"], h)
    dev = [(k, h) for k, (s, h) in hashes.items() if s == "dev"]
    test = [(k, h) for k, (s, h) in hashes.items() if s == "test"]
    out = []
    for a, ha in dev:
        for b, hb in test:
            d = int(np.unpackbits(ha ^ hb).sum())
            if d <= max_bits:
                out.append((a, b, d))
    return out


# ------------------------------------------------------------------ all workspaces together (for the model runs)

COMBINED_EXTRA = ["collection", "image_path"]
COVERAGE_COLUMNS = ["region", "split", "group", "marking", "images", "clips", "collections",
                    "agreed_by_two", "adjudicated", "single_label", "not_full_evidence"]


def split_check(repo: Path, rows: list[dict], root: Path, version: int, changes: list[dict], max_bits: int = 4) -> dict:
    """Milestone 3, 6.5 checks on the final labels of every workspace, saved with each split version:
    no clip on both sides, no development image within max_bits (dHash) of a test image, prompt examples only
    from development images, and the recorded split changes."""
    import numpy as np
    sides = defaultdict(set)
    for r in rows:
        sides[(r["collection"], r.get("clip_id") or r["image_id"])].add(r["split"])
    both = sorted(f"{c}:{k}" for (c, k), v in sides.items() if len(v) > 1)
    hashes = {}
    for r in rows:
        if r["split"] in ("dev", "test"):
            h = dhash(root / r["image_path"])
            if h is not None:
                hashes[r["image_id"]] = (r["split"], h)
    dev = [(k, h) for k, (sp, h) in hashes.items() if sp == "dev"]
    test = [(k, h) for k, (sp, h) in hashes.items() if sp == "test"]
    dups = []
    for a, ha in dev:
        for b, hb in test:
            d = int(np.unpackbits(ha ^ hb).sum())
            if d <= max_bits:
                dups.append([a, b, d])
    split_of = {r["image_id"]: r["split"] for r in rows}
    examples, outside = 0, []
    try:
        prompt_dir = json.loads((repo / "config" / "experiment.json").read_text(encoding="utf-8"))["prompt"]["dir"]
        ex_file = repo / prompt_dir / "examples.json"
        ex = json.loads(ex_file.read_text(encoding="utf-8")) if ex_file.exists() else []
        examples = len(ex)
        outside = [e.get("source_image_id", "") for e in ex if split_of.get(e.get("source_image_id", "")) != "dev"]
    except (OSError, ValueError, KeyError):
        prompt_dir = ""
    return {"split_version": version, "date_utc": utc_now(), "tool": f"video_tool {__version__}",
            "final_labels": dict(Counter(r["split"] for r in rows)),
            "clips": {sp: len({(r["collection"], r.get("clip_id") or r["image_id"]) for r in rows if r["split"] == sp}) for sp in ("dev", "test")},
            "clips_on_both_sides": both, "max_bits": max_bits, "near_duplicates_across_split": dups,
            "images_hashed": len(hashes), "prompt_dir": prompt_dir, "prompt_examples": examples, "examples_not_from_dev": outside,
            "split_changes": changes}


SUPPLY_COLUMNS = ["collection", "pool", "hint", "images", "clips", "night_images"]


def supply_table(workspaces: list) -> list[dict]:
    """What the dataset workspaces could still supply: candidate images and distinct clips per pool (dev/test)
    and hint (BDD100K lane type, CULane scene category), from each candidate index."""
    out = []
    for p in workspaces:
        if not p.is_images:
            continue
        for tid in list_trip_ids(p):
            cells = defaultdict(lambda: [0, set(), 0])
            for r in read_csv(p.scan_csv(tid)):
                for h in [x for x in (r.get("hints") or "").split(";") if x] or ["(no hint)"]:
                    c = cells[(r["pool"], h)]
                    c[0] += 1
                    c[1].add(r.get("clip_id") or r["cand_id"])
                    c[2] += r.get("time_of_day") == "night"
            for (pool, h), (n, clips, night) in sorted(cells.items()):
                out.append({"collection": p.collection, "pool": pool, "hint": h, "images": n, "clips": len(clips), "night_images": night})
    return out


def coverage_table(rows: list[dict]) -> list[dict]:
    """Usable final labels per region, split and marking type (arrows by direction), with the number of distinct
    clips (own video: drive; BDD100K: image; CULane: clip) and how certain the labels are."""
    cells = defaultdict(list)
    for r in rows:
        mt = r.get("marking_type") or ""
        marking = f"arrow/{r['arrow_type'] or '?'}" if mt == "arrow" else mt
        cells[(r["region"], r["split"], group_of(r), marking)].append(r)
    out = []
    for (region, split, group, marking), rs in sorted(cells.items()):
        out.append({"region": region, "split": split, "group": group, "marking": marking, "images": len(rs),
                    "clips": len({(r["collection"], r.get("clip_id") or r["image_id"]) for r in rs}),
                    "collections": ";".join(sorted({r["collection"] for r in rs})),
                    "agreed_by_two": sum(1 for r in rs if r.get("final_source") == "agreed"),
                    "adjudicated": sum(1 for r in rs if r.get("final_source") == "adjudicated"),
                    "single_label": sum(1 for r in rs if r.get("final_source") in ("single", "")),
                    "not_full_evidence": sum(1 for r in rs if r.get("expected_evidence") != "full")})
    return out


def combine(repo: str | Path | None, data_dirs: list[str], log=print) -> dict:
    """labels/labels.csv (every FINAL label of every workspace) and labels/split_v1.csv, for the model runs.

    image_path is relative to the folder that holds all workspaces (set DATASETS_ROOT to it when running the model)."""
    ws, seen_coll = [], set()
    for d in data_dirs:
        dp = Path(d).expanduser()
        own = any((dp / x / "own_video").exists() for x in ("raw", "interim", "extracted"))
        if not dp.is_dir() or not ((dp / WORKSPACE_FILE).exists() or own):
            log(f"Skipped {dp}: not set up yet.")
            continue
        p = Paths.discover(repo, dp)
        if p.collection in seen_coll:
            raise ToolError(f"Two folders hold {p.collection}; give each workspace once.")
        seen_coll.add(p.collection)
        ws.append(p)
    if not ws:
        raise ToolError("Give the data folders to combine, e.g. /Volumes/T9/数据集/UF /Volumes/T9/数据集/bdd100k /Volumes/T9/数据集/culane")
    import os
    root = Path(os.path.commonpath([str(p.data) for p in ws])) if len(ws) > 1 else ws[0].data.parent
    rows, split_rows, counts = [], [], Counter()
    seen = set()
    for p in ws:
        for tid in list_trip_ids(p):
            for r in LabelStore(p.labels_csv(tid)).all():
                if r["label_status"] != "done":
                    continue
                if r["image_id"] in seen:
                    raise ToolError(f"{r['image_id']} appears in two workspaces.")
                seen.add(r["image_id"])
                img = (p.data / r["source_path"]).resolve()
                rows.append({**r, "collection": p.collection, "image_path": img.relative_to(root).as_posix()})
                split_rows.append({"image_id": r["image_id"], "collection": p.collection, "region": r["region"],
                                   "dataset": r["dataset"], "clip_id": r["clip_id"], "split": r["split"]})
                counts[(r["region"], r["split"], group_of(r))] += 1
    rows.sort(key=lambda r: (r["collection"], r["split"], r["image_id"]))
    split_rows.sort(key=lambda r: (r["collection"], r["split"], r["image_id"]))
    repo_path = ws[0].repo
    write_csv(repo_path / "labels" / "labels.csv", rows, LABEL_COLUMNS + COMBINED_EXTRA)
    changes = read_csv(repo_path / "labels" / "split_changes.csv")
    version = len(changes) + 1  # a new version after every recorded split change; older files stay
    split_name = f"split_v{version}.csv"
    write_csv(repo_path / "labels" / split_name, split_rows, ["image_id", "collection", "region", "dataset", "clip_id", "split"])
    log(f"Wrote labels/labels.csv ({len(rows)} final labels) and labels/{split_name}.")
    check = split_check(repo_path, rows, root, version, changes)
    cov = coverage_table(rows)
    write_json(repo_path / "labels" / f"split_check_v{version}.json", check)
    write_csv(repo_path / "labels" / f"coverage_v{version}.csv", cov, COVERAGE_COLUMNS)
    supply = supply_table(ws)
    if supply:
        write_csv(repo_path / "labels" / "candidate_supply.csv", supply, SUPPLY_COLUMNS)
    log(f"Separation check (labels/split_check_v{version}.json): {len(check['clips_on_both_sides'])} clips on both sides, "
        f"{len(check['near_duplicates_across_split'])} near-duplicate dev/test pairs (dHash <= {check['max_bits']} bits), "
        f"{len(check['examples_not_from_dev'])} prompt examples not from development images.")
    log(f"Usable counts per region, split and marking type: labels/coverage_v{version}.csv")
    log(f"Image paths are relative to {root} (set DATASETS_ROOT to this folder for the model runs).")
    for (region, split, g), n in sorted(counts.items()):
        log(f"  {region} {split:4s} {g:9s} {n}")
    return {"rows": len(rows), "root": str(root), "counts": counts}
