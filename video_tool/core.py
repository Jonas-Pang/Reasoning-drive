"""Paths, trip registry, label files, schema and label checks.

There are two kinds of workspace, each with its own data folder (DATA_DIR) and its own label folder:
  own videos      one "trip" = one recorded video          labels/own_video/
  dataset images  one "set" = the images of one dataset     labels/<dataset>/ (bdd100k, culane)
A data folder that holds dataset images has a workspace.json; see imagesets.py for that layout.

Where things live for own videos (one "trip" = one recorded video):

  In Git (repository, small text files):
    labels/own_video/trips.csv              one row per trip: source record for 6.2
    labels/own_video/<trip>.trip.json       video metadata, settings, scan summary
    labels/own_video/<trip>.labels.csv      one row per kept frame: target box + FINAL label
    labels/own_video/<trip>.annotations.csv every independent label (one row per frame and annotator)
    labels/own_video/<trip>.recheck.csv     blind re-check labels (risk R2)
    labels/own_video/packages.csv           labeling packages sent to helpers (annotator codes only)

  On the data drive (DATA_DIR, ignored by Git):
    raw/own_video/<trip>/<video>            the original video, never changed
    interim/own_video/<trip>/scan.csv       scan results (can be rebuilt)
    extracted/own_video/<trip>/frames/      the kept frames (can be rebuilt from the video)
    report_figures/own_video/<trip>/        copies with plates and faces blurred, for reports only
    packages/                               labeling packages (zip) for helpers
    annotators.json                         private: annotator code -> real name (never in Git)
"""
from __future__ import annotations

import csv
import getpass
import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
DEFAULT_REPO = PACKAGE_DIR.parent
TRIP_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$")

ACTIONS = [
    "cross_line",
    "go_straight",
    "turn_left",
    "turn_right",
    "u_turn",
    "enter_center_lane_to_wait",
]
ACTION_COLUMNS = ["act_" + a for a in ACTIONS]

LABEL_COLUMNS = [
    # identity and lineage
    "image_id", "region", "dataset", "source_path", "split", "clip_id",
    "frame_index", "time_s", "width", "height", "time_of_day", "weather",
    # Output 1: the marking
    "marking_type", "arrow_type", "position", "dashed_side",
    "bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2",
    # evidence (requirement 5)
    "visibility", "behavior_decidable", "expected_evidence",
    # Output 2: actions
    *ACTION_COLUMNS,
    # citations, privacy, bookkeeping
    "accepted_rule_ids", "privacy_boxes", "label_status", "labeler", "label_date", "notes",
    # how the final label was reached (agreed by annotators, adjudicated by the owner, or a single annotator)
    "final_source", "annotators", "adjudication_note",
    # dataset images only: the cell it was picked for, suggested target boxes, its path in the original dataset
    "pick_group", "box_hints", "source_ref",
]
# label_status of the FINAL label:
#   kept      frame saved, no target box yet
#   waiting   target box drawn, fewer finished annotations than required
#   conflict  annotations disagree, or someone marked it unsure -> adjudication
#   done      final label decided
#   excluded  not used in the experiment
FINAL_FIELDS = [
    "marking_type", "arrow_type", "position", "dashed_side", "visibility", "behavior_decidable",
    "expected_evidence", *ACTION_COLUMNS, "accepted_rule_ids",
]
COMPARE_FIELDS = ["marking_type", "arrow_type", "position", "dashed_side", "visibility", "behavior_decidable", *ACTION_COLUMNS]

ANNOTATION_COLUMNS = [
    "image_id", "annotator", "source", "package_id",
    "marking_type", "arrow_type", "position", "dashed_side", "visibility", "behavior_decidable",
    "expected_evidence", *ACTION_COLUMNS, "accepted_rule_ids", "privacy_boxes",
    "status", "unsure", "comment", "saved_utc",
]
OWNER = "owner"  # annotator code of the project owner (labels made in the local app)

RECHECK_COLUMNS = [
    "image_id", "marking_type", "arrow_type", "position", "dashed_side",
    "visibility", "behavior_decidable", "expected_evidence", *ACTION_COLUMNS,
    "recheck_status", "labeler", "label_date", "notes",
]

TRIP_COLUMNS = [
    "trip_id", "region", "dataset", "recorded_date", "time_of_day", "weather", "road_type",
    "video_file", "size_bytes", "sha256", "duration_s", "width", "height", "fps",
    "split_policy", "registered_utc", "license",
]

OWN_LICENSE = "Own recording by the project author; no third-party license. Raw video stays private; faces and plates are blurred in any published figure."


class ToolError(Exception):
    """An error with a message meant for the user (no traceback needed)."""


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return
    try:
        from dotenv import load_dotenv  # python-dotenv is in requirements.txt
        load_dotenv(path)
        return
    except ImportError:
        pass
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


WORKSPACE_FILE = "workspace.json"


@dataclass
class Paths:
    repo: Path
    data: Path
    collection: str = "own_video"  # own_video, bdd100k, culane: the folder under labels/
    kind: str = "video"            # video (own recordings) or images (a public dataset)

    @classmethod
    def discover(cls, repo: str | Path | None = None, data: str | Path | None = None) -> "Paths":
        repo_path = Path(repo or os.environ.get("VIDEO_TOOL_REPO") or DEFAULT_REPO).expanduser().resolve()
        if not (repo_path / "rules" / "rule_passages.json").exists():
            raise ToolError(f"{repo_path} does not look like the project repository (rules/rule_passages.json is missing).")
        _load_env_file(repo_path / ".env")
        data_path = Path(data or os.environ.get("DATA_DIR") or repo_path / "data").expanduser().resolve()
        if not data_path.parent.exists():
            raise ToolError(f"{data_path.parent} does not exist. Is the external drive connected? (DATA_DIR is set in .env)")
        data_path.mkdir(parents=True, exist_ok=True)
        collection, kind = "own_video", "video"
        ws = data_path / WORKSPACE_FILE
        if ws.exists():
            w = json.loads(ws.read_text(encoding="utf-8"))
            collection, kind = w.get("collection", collection), w.get("kind", kind)
        return cls(repo_path, data_path, collection, kind)

    @property
    def is_images(self) -> bool:
        return self.kind == "images"

    @property
    def meta_suffix(self) -> str:
        return ".set.json" if self.is_images else ".trip.json"

    # Git side
    @property
    def labels_dir(self) -> Path:
        return self.repo / "labels" / self.collection

    @property
    def trips_csv(self) -> Path:
        return self.labels_dir / "trips.csv"

    def trip_json(self, trip_id: str) -> Path:
        return self.labels_dir / f"{trip_id}{self.meta_suffix}"

    def labels_csv(self, trip_id: str) -> Path:
        return self.labels_dir / f"{trip_id}.labels.csv"

    def recheck_csv(self, trip_id: str) -> Path:
        return self.labels_dir / f"{trip_id}.recheck.csv"

    def annotations_csv(self, trip_id: str) -> Path:
        return self.labels_dir / f"{trip_id}.annotations.csv"

    @property
    def packages_csv(self) -> Path:
        return self.labels_dir / "packages.csv"

    @property
    def packages_dir(self) -> Path:
        return self.data / "packages"

    @property
    def annotators_json(self) -> Path:
        return self.data / "annotators.json"

    # data drive side
    def raw_dir(self, trip_id: str) -> Path:
        return self.data / "raw" / "own_video" / trip_id

    def scan_csv(self, trip_id: str) -> Path:
        """Own video: the scan of the video. Dataset images: the candidate index."""
        if self.is_images:
            return self.data / "index" / trip_id / "candidates.csv"
        return self.data / "interim" / "own_video" / trip_id / "scan.csv"

    def frames_dir(self, trip_id: str) -> Path:
        """Where the kept images are (own video: rendered frames; dataset images: copies of the picked images)."""
        if self.is_images:
            return self.data / "selected" / trip_id
        return self.data / "extracted" / "own_video" / trip_id / "frames"

    @property
    def figures_root(self) -> Path:
        return self.data / "report_figures" / ("" if self.is_images else "own_video")

    def figures_dir(self, trip_id: str) -> Path:
        return self.figures_root / trip_id

    def rel(self, path: Path) -> str:
        """Path relative to DATA_DIR, with forward slashes (what the label file stores)."""
        return Path(path).resolve().relative_to(self.data).as_posix()


# ---------------------------------------------------------------- files

def read_json(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    _atomic_write(Path(path), json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def read_csv(path: Path) -> list[dict]:
    path = Path(path)
    if not path.exists():
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return [dict(r) for r in csv.DictReader(f)]


def write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
    import io
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow({c: ("" if r.get(c) is None else r.get(c)) for c in columns})
    _atomic_write(Path(path), buf.getvalue())


def sha256_of(path: Path, progress=None, chunk: int = 8 << 20) -> str:
    h = hashlib.sha256()
    total = Path(path).stat().st_size
    done = 0
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
            done += len(block)
            if progress:
                progress(done, total)
    return h.hexdigest()


def default_labeler() -> str:
    return os.environ.get("LABELER") or getpass.getuser()


def check_trip_id(trip_id: str) -> str:
    if not TRIP_ID_RE.match(trip_id or ""):
        raise ToolError(f"Trip name '{trip_id}' is not allowed. Use letters, digits, '_' or '-' (for example fl_20261016_night_01).")
    return trip_id


# ---------------------------------------------------------------- trips

class Trip:
    def __init__(self, paths: Paths, trip_id: str):
        self.paths = paths
        self.id = check_trip_id(trip_id)
        p = paths.trip_json(trip_id)
        if not p.exists():
            known = ", ".join(list_trip_ids(paths)) or "none yet"
            if paths.is_images:
                raise ToolError(f"Image set '{trip_id}' is not set up in {paths.data}. Known sets: {known}. Set it up with: python -m video_tool images init <dataset>")
            raise ToolError(f"Trip '{trip_id}' is not registered. Known trips: {known}. Register a video with: python -m video_tool ingest <video>")
        self.meta = read_json(p)

    @property
    def kind(self) -> str:
        return self.meta.get("kind", "video")

    def save(self) -> None:
        self.meta["updated_utc"] = utc_now()
        write_json(self.paths.trip_json(self.id), self.meta)

    @property
    def video_path(self) -> Path:
        return self.paths.data / self.meta["video"]["file"]

    @property
    def region(self) -> str:
        return self.meta["region"]

    def check_video(self) -> Path:
        vp = self.video_path
        if not vp.exists():
            raise ToolError(f"The video for trip '{self.id}' is not at {vp}. Is the external drive connected?")
        return vp


def list_trip_ids(paths: Paths) -> list[str]:
    if not paths.labels_dir.exists():
        return []
    suf = paths.meta_suffix
    return sorted(p.name[: -len(suf)] for p in paths.labels_dir.glob("*" + suf) if not p.name.startswith("._"))


def assign_split(policy: str, clip_id: str) -> str:
    """test / dev for a fixed trip; 'hash' applies the clip rule from section 6.5."""
    if policy in ("test", "dev"):
        return policy
    if policy == "hash":
        return "dev" if int(hashlib.sha1(("6216:" + clip_id).encode()).hexdigest(), 16) % 10 == 0 else "test"
    raise ToolError(f"Unknown split policy '{policy}' (use test, dev or hash).")


def update_trips_csv(paths: Paths) -> None:
    rows = []
    for tid in list_trip_ids(paths):
        m = read_json(paths.trip_json(tid))
        v = m.get("video", {})
        rows.append({
            "trip_id": tid, "region": m.get("region"), "dataset": m.get("dataset"),
            "recorded_date": m.get("recorded_date"), "time_of_day": m.get("time_of_day"),
            "weather": m.get("weather"), "road_type": m.get("road_type"),
            "video_file": v.get("file"), "size_bytes": v.get("size_bytes"), "sha256": v.get("sha256"),
            "duration_s": v.get("duration_s"), "width": v.get("width"), "height": v.get("height"),
            "fps": v.get("fps"), "split_policy": m.get("split"), "registered_utc": m.get("registered_utc"),
            "license": m.get("license", OWN_LICENSE),
        })
    write_csv(paths.trips_csv, rows, TRIP_COLUMNS)


# ---------------------------------------------------------------- schema and rules

def load_schema(paths: Paths) -> dict:
    return read_json(paths.repo / "config" / "label_schema.json")


def load_action_rules(paths: Paths) -> dict:
    return read_json(paths.repo / "config" / "action_rules.json")


def load_rule_passages(paths: Paths, region: str | None = None) -> list[dict]:
    items = read_json(paths.repo / "rules" / "rule_passages.json")
    if region:
        items = [p for p in items if p.get("region") == region]
    return items


def rules_file_sha256(paths: Paths) -> str:
    return hashlib.sha256((paths.repo / "rules" / "rule_passages.json").read_bytes()).hexdigest()


def derive_evidence(visibility: str, decidable: str) -> str:
    if visibility == "V2":
        return "full"
    if visibility == "V1":
        return {"yes": "full", "no": "partial"}.get(decidable, "")
    if visibility == "V0":
        return "insufficient"
    return ""


def rule_key(marking_type: str, arrow_type: str = "", dashed_side: str = "") -> str:
    if marking_type == "arrow":
        return f"arrow|{arrow_type}" if arrow_type else ""
    if marking_type == "yellow_solid_dashed":
        return f"{marking_type}|{dashed_side}" if dashed_side else ""
    return marking_type or ""


UNKNOWN_SUBTYPE = {  # actions when the type is known but its detail is hidden (V1, behavior not decidable)
    "arrow": {"cross_line": "not_applicable", "go_straight": "not_determined", "turn_left": "not_determined",
              "turn_right": "not_determined", "u_turn": "not_determined", "enter_center_lane_to_wait": "not_applicable"},
    "yellow_solid_dashed": {"cross_line": "not_determined", "go_straight": "not_applicable", "turn_left": "not_applicable",
                            "turn_right": "not_applicable", "u_turn": "not_applicable", "enter_center_lane_to_wait": "not_applicable"},
}


def prefill(table: dict, region: str, marking_type: str, arrow_type: str = "", dashed_side: str = "", evidence: str = "") -> dict:
    """The rule-table suggestion for one label: {'actions': {...}, 'rule_ids': [...], 'note': str} or {}."""
    entry = table.get(region, {}).get(rule_key(marking_type, arrow_type, dashed_side))
    if not entry and evidence in ("partial", "insufficient") and marking_type in UNKNOWN_SUBTYPE:
        return {"actions": dict(UNKNOWN_SUBTYPE[marking_type]), "rule_ids": [], "note": ""}
    if not entry:
        return {}
    acts = dict(entry["actions"])
    if evidence in ("partial", "insufficient"):
        acts = {a: (v if v == "not_applicable" else "not_determined") for a, v in acts.items()}
    return {"actions": acts, "rule_ids": list(entry.get("rule_ids", [])), "note": entry.get("note", "")}


# ---------------------------------------------------------------- label checks

def _num(v) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def validate_label(row: dict, schema: dict, region_rule_ids: set[str], table: dict | None = None,
                   check_box: bool = True) -> tuple[list[str], list[str]]:
    """Errors block 'done'; warnings are shown but allowed. Annotations have no box (the owner draws it)."""
    errors: list[str] = []
    warnings: list[str] = []
    mt = row.get("marking_type", "")
    ev_pre = derive_evidence(row.get("visibility", ""), row.get("behavior_decidable", ""))
    detail_optional = ev_pre in ("partial", "insufficient")  # e.g. an arrow whose head is hidden
    if mt not in schema["marking_type"]:
        errors.append("Choose a marking type.")
    if mt == "arrow":
        if row.get("arrow_type") not in schema["arrow_type"] and not (detail_optional and not row.get("arrow_type")):
            errors.append("Choose the arrow type.")
    elif row.get("arrow_type"):
        errors.append("Arrow type is only for arrows; clear it.")
    if row.get("position") not in schema["position"]:
        errors.append("Choose the position (left / in_ego_lane / right).")
    if mt in schema.get("needs_dashed_side", []):
        if row.get("dashed_side") not in schema["dashed_side"] and not (detail_optional and not row.get("dashed_side")):
            errors.append("Say which side the broken line is on.")
    elif row.get("dashed_side"):
        errors.append("Broken-line side is only for solid-dashed lines; clear it.")

    box = [_num(row.get(k)) for k in ("bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2")]
    w, h = _num(row.get("width")), _num(row.get("height"))
    if not check_box:
        pass
    elif any(v is None for v in box):
        errors.append("Draw the box around the marking.")
    else:
        x1, y1, x2, y2 = box
        if x2 - x1 < 4 or y2 - y1 < 4:
            errors.append("The marking box is too small.")
        if w and h and (x1 < 0 or y1 < 0 or x2 > w or y2 > h):
            errors.append("The marking box is outside the image.")

    vis = row.get("visibility", "")
    if vis not in schema["visibility"]:
        errors.append("Choose the visibility (V2 / V1 / V0).")
    if vis == "V1" and row.get("behavior_decidable") not in ("yes", "no"):
        errors.append("For V1, say whether the visible part decides the behavior.")
    ev = derive_evidence(vis, row.get("behavior_decidable", ""))
    if row.get("expected_evidence") != ev:
        errors.append(f"Expected evidence should be '{ev}' for this visibility.")
    if vis == "V0" and mt != "none_visible":
        warnings.append("V0 (no usable evidence) is usually labeled none_visible.")
    if mt == "none_visible" and vis != "V0":
        errors.append("none_visible only goes with V0.")

    vals = schema["action_values"]
    acts = {a: row.get("act_" + a, "") for a in ACTIONS}
    missing = [a for a, v in acts.items() if v not in vals]
    if missing:
        errors.append("Set every action: " + ", ".join(missing) + ".")
    if ev in ("partial", "insufficient"):
        decided = [a for a, v in acts.items() if v in ("allowed", "prohibited")]
        if decided:
            errors.append(f"With {ev} evidence no action can be allowed or prohibited ({', '.join(decided)}).")
    elif ev == "full" and mt not in schema.get("no_rule_needed", []):
        if not any(v in ("allowed", "prohibited") for v in acts.values()):
            warnings.append("Full evidence but no action is allowed or prohibited.")

    ids = [i for i in (row.get("accepted_rule_ids") or "").split(";") if i]
    unknown = [i for i in ids if i not in region_rule_ids]
    if unknown:
        errors.append("Rule IDs not in this region's rule file: " + ", ".join(unknown))
    if not ids and ev == "full" and mt not in schema.get("no_rule_needed", []):
        errors.append("Tick at least one accepted rule ID.")

    try:
        boxes = json.loads(row.get("privacy_boxes") or "[]")
        if not isinstance(boxes, list) or not all(isinstance(b, list) and len(b) == 4 for b in boxes):
            errors.append("Privacy boxes are damaged.")
    except json.JSONDecodeError:
        errors.append("Privacy boxes are damaged.")

    if table is not None and not errors:
        sug = prefill(table, row.get("region", ""), mt, row.get("arrow_type", ""), row.get("dashed_side", ""), ev)
        for a, v in sug.get("actions", {}).items():
            if v and acts.get(a) != v:
                warnings.append(f"{a} = {acts.get(a)} differs from the rule table ({v}). Fine if you meant it.")
    return errors, warnings


class LabelStore:
    """The label rows of one trip, kept in memory and written back on every change."""

    def __init__(self, path: Path, columns: list[str] = LABEL_COLUMNS):
        self.path = Path(path)
        self.columns = columns
        self.rows: dict[str, dict] = {}
        for r in read_csv(self.path):
            row = {c: r.get(c, "") or "" for c in columns}
            if columns is LABEL_COLUMNS and row.get("label_status") == "draft":
                row["label_status"] = "waiting"  # files written before annotations existed
            self.rows[r["image_id"]] = row

    def save(self) -> None:
        key = "frame_index" if "frame_index" in self.columns else "image_id"
        ordered = sorted(self.rows.values(), key=lambda r: (int(r[key]) if str(r.get(key, "")).isdigit() else 0, r["image_id"]))
        write_csv(self.path, ordered, self.columns)

    def get(self, image_id: str) -> dict | None:
        return self.rows.get(image_id)

    def put(self, row: dict) -> None:
        self.rows[row["image_id"]] = {c: ("" if row.get(c) is None else row.get(c)) for c in self.columns}

    def delete(self, image_id: str) -> None:
        self.rows.pop(image_id, None)

    def all(self) -> list[dict]:
        return list(self.rows.values())
