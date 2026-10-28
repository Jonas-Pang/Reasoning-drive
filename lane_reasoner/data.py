"""The labeled images: FINAL labels (label_status == done) from every workspace (own video, BDD100K, CULane)."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path

import cv2

from video_tool.core import WORKSPACE_FILE, LabelStore, Paths, list_trip_ids


@dataclass
class Item:
    image_id: str
    collection: str
    region: str
    dataset: str
    split: str
    path: Path
    box: list
    width: int
    height: int
    label: dict = field(repr=False)

    @property
    def marking(self) -> str:
        mt = self.label.get("marking_type", "")
        return mt + (f"/{self.label['arrow_type']}" if self.label.get("arrow_type") else "")


def workspace_dirs(cfg: dict) -> list[Path]:
    """The data folders: absolute paths as written, relative ones under DATASETS_ROOT (environment or .env),
    else under data.datasets_root in config/experiment.yaml."""
    import os
    root = Path(os.environ.get("DATASETS_ROOT") or cfg.get("datasets_root") or ".").expanduser()
    return [Path(d).expanduser() if Path(d).expanduser().is_absolute() else root / d for d in cfg.get("workspaces", [])]


def allowed_collections(cfg: dict) -> set | None:
    """Collections whose images may be sent to the API (data_policy.send_to_api); None = no restriction."""
    pol = (cfg.get("data_policy") or {}).get("send_to_api")
    return None if pol is None else set(pol)


def workspaces(cfg: dict) -> list[Paths]:
    from .config import repo_of
    out = []
    for dp in workspace_dirs(cfg):
        own = any((dp / x / "own_video").exists() for x in ("raw", "interim", "extracted"))
        if dp.is_dir() and ((dp / WORKSPACE_FILE).exists() or own):
            out.append(Paths.discover(repo_of(cfg), dp))
    return out


def load_items(cfg: dict, region: str | None = None, split: str | None = None, types: list | None = None) -> list[Item]:
    region = region or cfg["run"]["region"]
    split = split or cfg["run"].get("split", "any")
    types = types if types is not None else cfg["run"].get("marking_types") or []
    items = []
    allowed = allowed_collections(cfg)
    for p in workspaces(cfg):
        if allowed is not None and p.collection not in allowed:
            continue  # not listed in data_policy.send_to_api
        for tid in list_trip_ids(p):
            for r in LabelStore(p.labels_csv(tid)).all():
                if r.get("label_status") != "done" or r.get("region") != region:
                    continue
                if split not in ("any", "") and r.get("split") != split:
                    continue
                if types and r.get("marking_type") not in types:
                    continue
                try:
                    box = [int(float(r[k])) for k in ("bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2")]
                except (TypeError, ValueError):
                    continue
                items.append(Item(r["image_id"], p.collection, r["region"], r.get("dataset", ""), r.get("split", ""),
                                  p.data / r["source_path"], box, int(float(r.get("width") or 0)), int(float(r.get("height") or 0)), r))
    seed = str(cfg["run"].get("order_seed", 6216))
    items.sort(key=lambda it: hashlib.sha1(f"{seed}:{it.image_id}".encode()).hexdigest())  # fixed random order
    return items


def boxed_jpeg(item: Item, cfg: dict) -> bytes:
    """The image exactly as the model sees it: a copy with the cyan target box drawn on it (the original is not changed)."""
    img = cv2.imread(str(item.path), cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Image not found: {item.path}")
    pc = cfg["prompt"]
    h, w = img.shape[:2]
    m = int(pc.get("box_margin", 6))
    x1, y1, x2, y2 = item.box
    x1, y1, x2, y2 = max(0, x1 - m), max(0, y1 - m), min(w - 1, x2 + m), min(h - 1, y2 + m)
    r, g, b = pc.get("box_color_rgb", [0, 229, 255])
    thick = max(2, round(int(pc.get("box_width", 3)) * w / 1280))
    cv2.rectangle(img, (x1, y1), (x2, y2), (int(b), int(g), int(r)), thick)
    ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, int(pc.get("jpeg_quality", 92))])
    if not ok:
        raise RuntimeError("Could not encode the image.")
    return buf.tobytes()
