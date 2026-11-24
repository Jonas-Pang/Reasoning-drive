"""Lane labels (Milestone 5): my lane as a whole, labeled per image.

One row per image in datasets/<CODE>/<collection>/<set>.lanes.csv (the FINAL lane label) and one row per image and
annotator in <set>.lane_annotations.csv. The images are the kept frames of the set (<set>.labels.csv), so the
split stays the one fixed for the single-marking task.

A lane label holds
  * the lane count of my direction and the position of my lane (1 = leftmost), with their evidence;
  * for each boundary (left, right): colour, pattern, which line of a solid-and-broken pair is on my side,
    whether a curb forms it, its role (lane line, centre line, edge line, special lane line), its evidence,
    and optionally the line drawn on the image (left_line / right_line, kept for checking, never sent to the model);
  * the guidance markings in my lane as tokens (configs/schemas/lane_schema.json), e.g. arrow:left;text:only;line:stop_line;
  * the seven lane actions and the accepted rule IDs.
Final label from the annotations: the same rule as the single-marking task (two finished annotations that agree
on every compared field -> done; otherwise conflict, decided by the owner).
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from .. import paths as P
from .core import LabelStore, Paths, ToolError, Trip, list_trip_ids, read_csv, read_json, source_path, today, utc_now, write_csv

SIDES = ["left", "right"]
BOUNDARY_FIELDS = ["color", "pattern", "near_line", "curb", "role", "evidence"]
LANE_ACTIONS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"]
LANE_ACTION_COLUMNS = ["act_" + a for a in LANE_ACTIONS]
MOVES = ["go_straight", "turn_left", "turn_right", "u_turn"]
IDENTITY = ["image_id", "region", "dataset", "source_path", "split", "clip_id", "frame_index", "width", "height",
            "time_of_day", "weather"]
SCENE_FIELDS = ["lane_count", "ego_index", "scene_evidence"]
SIDE_COLUMNS = [f"{s}_{f}" for s in SIDES for f in BOUNDARY_FIELDS]
LINE_COLUMNS = ["left_line", "right_line"]
# compared between annotators and scored against the model
LANE_COMPARE = [*SCENE_FIELDS, *SIDE_COLUMNS, "markings", "markings_evidence", *LANE_ACTION_COLUMNS]
LANE_FINAL = [*LANE_COMPARE, "accepted_rule_ids", *LINE_COLUMNS]
LANE_COLUMNS = [*IDENTITY, *LANE_FINAL, "lane_status", "labeler", "label_date", "notes", "final_source", "annotators",
                "adjudication_note", "prefill_source"]
LANE_ANNOTATION_COLUMNS = ["image_id", "annotator", "source", "package_id", *LANE_FINAL, "status", "unsure", "comment",
                           "saved_utc"]


# ------------------------------------------------------------------ files

def lanes_csv(paths: Paths, set_id: str) -> Path:
    return paths.labels_dir / f"{set_id}.lanes.csv"


def lane_annotations_csv(paths: Paths, set_id: str) -> Path:
    return paths.labels_dir / f"{set_id}.lane_annotations.csv"


def load_lane_schema(repo: Path) -> dict:
    return read_json(Path(repo) / P.LANE_SCHEMA)


def load_lane_rules(repo: Path) -> dict:
    return P.lane_action_rules(repo)


class LaneStore(LabelStore):
    def __init__(self, path: Path):
        super().__init__(path, LANE_COLUMNS)


class LaneAnnotationStore:
    """All lane annotations of one set, keyed by (image_id, annotator)."""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.rows: dict[tuple, dict] = {}
        for r in read_csv(self.path):
            self.rows[(r["image_id"], r["annotator"])] = {c: r.get(c, "") or "" for c in LANE_ANNOTATION_COLUMNS}

    def save(self) -> None:
        write_csv(self.path, sorted(self.rows.values(), key=lambda r: (r["image_id"], r["annotator"])), LANE_ANNOTATION_COLUMNS)

    def get(self, image_id: str, annotator: str) -> dict | None:
        return self.rows.get((image_id, annotator))

    def for_image(self, image_id: str) -> list[dict]:
        return sorted((r for (i, _), r in self.rows.items() if i == image_id), key=lambda r: (r.get("saved_utc", ""), r["annotator"]))

    def put(self, row: dict) -> None:
        clean = {c: ("" if row.get(c) is None else str(row.get(c))) for c in LANE_ANNOTATION_COLUMNS}
        clean["markings"] = join_tokens(split_tokens(clean["markings"]))
        self.rows[(clean["image_id"], clean["annotator"])] = clean

    def all(self) -> list[dict]:
        return list(self.rows.values())


def split_tokens(text) -> list[str]:
    if isinstance(text, (list, tuple)):
        items = list(text)
    else:
        items = str(text or "").replace(",", ";").split(";")
    return sorted({t.strip() for t in items if t and t.strip()})


def join_tokens(tokens) -> str:
    return ";".join(split_tokens(tokens))


def seed_lane_rows(paths: Paths, set_id: str, save: bool = True) -> int:
    """Add a lane row for every kept frame of the set that has none yet (identity copied from <set>.labels.csv)."""
    frames = LabelStore(paths.labels_csv(set_id))
    lanes = LaneStore(lanes_csv(paths, set_id))
    n = 0
    for r in frames.all():
        if r.get("label_status") == "excluded" or r["image_id"] in lanes.rows:
            continue
        row = {c: r.get(c, "") for c in IDENTITY}
        row.update({"lane_status": "kept", "prefill_source": ""})
        lanes.put(row)
        n += 1
    if save and (n or not lanes.path.exists()):
        lanes.save()
    return n


def remove_lane_image(paths: Paths, set_id: str, image_id: str) -> bool:
    """Drop the lane row and every lane annotation of an image that was removed from the set."""
    lanes = LaneStore(lanes_csv(paths, set_id))
    found = lanes.get(image_id) is not None
    if found:
        lanes.delete(image_id)
        lanes.save()
    anns = LaneAnnotationStore(lane_annotations_csv(paths, set_id))
    keep = {k: v for k, v in anns.rows.items() if k[0] != image_id}
    if len(keep) != len(anns.rows):
        anns.rows = keep
        anns.save()
    return found


# ------------------------------------------------------------------ rule table suggestions

def _match(when: dict, attrs: dict) -> bool:
    for k, v in when.items():
        want = v if isinstance(v, list) else [v]
        if (attrs.get(k) or "") not in want:
            return False
    return True


def boundary_rule(table: dict, region: str, attrs: dict) -> dict:
    """The first boundary row of the region whose 'when' matches one side: {'change', 'rule_ids', 'note', 'contested'}."""
    for row in (table.get(region) or {}).get("boundary", []):
        if _match(row.get("when", {}), attrs):
            return {"change": row.get("change", ""), "rule_ids": list(row.get("rule_ids", [])), "note": row.get("note", ""),
                    "contested": bool(row.get("contested"))}
    return {"change": "", "rule_ids": [], "note": "", "contested": False}


def side_attrs(row: dict, side: str) -> dict:
    return {f: row.get(f"{side}_{f}", "") for f in BOUNDARY_FIELDS}


# markings that make my own lane a special lane (bus, HOV)
SPECIAL_LANE_TOKENS = ("text:bus", "text:hov", "symbol:hov_diamond")

# lanes where carrying on straight is not the default: my lane ends and merges, or it is a two-way left-turn lane
ENDS_OR_TURN_ONLY = ("arrow:merge_left", "arrow:merge_right", "arrow:two_way_left")


def lane_prefill(table: dict, schema: dict, region: str, row: dict) -> dict:
    """Suggested actions and rule IDs for a lane label from its observed attributes (never used for scoring).

    Returns {'actions': {...}, 'rule_ids': [...], 'notes': [...], 'contested': [...]}; '' = the tool does not guess."""
    acts = {a: "" for a in LANE_ACTIONS}
    ids, notes, contested = [], [], []

    def add_ids(xs):
        for x in xs:
            if x not in ids:
                ids.append(x)

    for side in SIDES:
        a = side_attrs(row, side)
        if not a["pattern"] and a["curb"] != "yes":
            continue
        r = boundary_rule(table, region, a)
        act = f"change_{side}"
        acts[act] = r["change"]
        add_ids(r["rule_ids"])
        if r["note"]:
            notes.append(f"{side}: {r['note']}")
        if r["contested"]:
            contested.append(act)
        if a["role"] == "special_lane_line" and not acts[act]:
            # project convention (owner's decision, 2026-11-15): my car is an ordinary car and the reserved time cannot
            # be seen, so a bus, HOV, tidal or similar special lane across this line is taken as reserved: changing
            # into it is prohibited (contested). If my own lane is the special lane, leaving it follows the line type.
            if any(t in SPECIAL_LANE_TOKENS for t in split_tokens(row.get("markings", ""))):
                acts[act] = boundary_rule(table, region, dict(a, role="lane_line"))["change"]
            else:
                acts[act] = "prohibited"
            if act not in contested:
                contested.append(act)
        # owner, 2026-11-17: a recognisable line decides its action even when partly hidden (no not_determined)
    toks = split_tokens(row.get("markings", ""))
    rules = (table.get(region) or {}).get("markings", {})
    arrows = [t for t in toks if t in schema.get("movement_arrows", {})]
    if arrows:
        shown = {m for t in arrows for m in schema["movement_arrows"][t]}
        for m in MOVES:
            acts[m] = "allowed" if m in shown else "prohibited"
        # the region's table may say otherwise for single arrows (e.g. U-turn conventions): take its values if one arrow
        if len(arrows) == 1 and arrows[0] in rules:
            for m, v in rules[arrows[0]].get("actions", {}).items():
                if m in MOVES:
                    acts[m] = v
            contested += [c for c in rules[arrows[0]].get("contested", []) if c not in contested]
    for t in toks:
        r = rules.get(t)
        if not r:
            continue
        add_ids(r.get("rule_ids", []))
        if r.get("note"):
            notes.append(f"{t}: {r['note']}")
        for m, v in r.get("actions", {}).items():
            if t in schema.get("no_turn", {}) or not arrows or m not in MOVES:
                acts[m] = v
    for m in MOVES:
        if acts[m]:
            continue
        if m == "go_straight" and not arrows and not any(t in ENDS_OR_TURN_ONLY for t in toks):
            # project convention (owner's decision, 2026-11-15): with no arrow in my lane, and my lane neither ending
            # nor a two-way left-turn lane, nothing restricts carrying on straight along it, so going straight is
            # allowed; a lane line that prohibits or discourages a lane change does not touch it. Scored separately as
            # contested, since no passage says it in words.
            acts[m] = "allowed"
            if m not in contested:
                contested.append(m)
        elif not arrows and not any(t in schema.get("no_turn", {}) for t in toks):
            acts[m] = "not_applicable"
    if not acts["enter_waiting_area"]:
        acts["enter_waiting_area"] = "not_applicable"
    if any(t in schema.get("stop_tokens", []) for t in toks):  # STOP word or 停 stop-and-yield line: stop first, then go
        for m in MOVES:
            if acts[m] == "allowed":
                acts[m] = "stop_first"
    # owner, 2026-11-17: no not_determined for partly hidden markings either
    return {"actions": acts, "rule_ids": ids, "notes": notes, "contested": contested}


def contested_lane_actions(table: dict, schema: dict, region: str, label: dict) -> set:
    """Actions of a label whose value comes from a project convention (scored separately)."""
    return set(lane_prefill(table, schema, region, label)["contested"])


# ------------------------------------------------------------------ checks

def validate_lane(row: dict, schema: dict, rule_ids: set | None = None) -> tuple[list[str], list[str]]:
    """Errors (must be fixed before the label counts) and warnings for one lane label or annotation."""
    errors, warnings = [], []
    b = schema["boundary"]
    for side in SIDES:
        a = side_attrs(row, side)
        for f, allowed in (("color", b["color"]), ("pattern", b["pattern"]), ("curb", b["curb"]), ("role", b["role"]),
                           ("evidence", schema["evidence"])):
            if a[f] not in allowed:
                errors.append(f"{side} {f}: choose one of {', '.join(allowed)}")
        if a["pattern"] == "solid_dashed" and a["near_line"] not in ("solid", "dashed"):
            errors.append(f"{side}: say which line of the solid-and-broken pair is on my side")
        if a["pattern"] != "solid_dashed" and a["near_line"] not in ("", "not_applicable"):
            errors.append(f"{side}: 'line on my side' is only for a solid-and-broken pair")
        if (a["pattern"] == "none") != (a["color"] == "none") and a["pattern"] in b["pattern"]:
            errors.append(f"{side}: colour none and pattern none go together (no painted line)")
        if a["pattern"] == "none" and a["curb"] == "no" and a["role"] not in ("unknown", "other", ""):
            warnings.append(f"{side}: nothing marked and no curb, but a role is given")
    lc, ei = row.get("lane_count", ""), row.get("ego_index", "")
    if lc and not str(lc).isdigit():
        errors.append("lane count: a whole number, or empty if it cannot be seen")
    if ei and not str(ei).isdigit():
        errors.append("my lane position: a whole number (1 = leftmost lane of my direction), or empty")
    if str(lc).isdigit() and str(ei).isdigit() and int(ei) > int(lc):
        errors.append("my lane position is larger than the lane count")
    if row.get("scene_evidence") not in schema["evidence"]:
        errors.append("scene evidence: choose full, partial or insufficient")
    if row.get("markings_evidence") not in schema["evidence"]:
        errors.append("markings evidence: choose full, partial or insufficient")
    unknown = [t for t in split_tokens(row.get("markings", "")) if t not in schema["marking_tokens"]]
    if unknown:
        errors.append("unknown markings: " + ", ".join(unknown))
    for a in LANE_ACTIONS:
        if row.get("act_" + a) not in schema["action_values"]:
            errors.append(f"{a}: choose allowed, stop_first, prohibited, not_determined or not_applicable")
    if str(ei) == "1" and row.get("left_role") == "lane_line":
        warnings.append("my lane is the leftmost lane, but its left boundary is a lane line between lanes of my direction")
    if str(lc).isdigit() and str(ei) == str(lc) and row.get("right_role") == "lane_line":
        warnings.append("my lane is the rightmost lane, but its right boundary is a lane line between lanes of my direction")
    toks = split_tokens(row.get("markings", ""))
    arrows = [t for t in toks if t in schema.get("movement_arrows", {})]
    if "text:only" in toks and any(len(schema["movement_arrows"][t]) > 1 for t in arrows):
        warnings.append("ONLY together with an arrow that shows two movements (MUTCD 3B.21 ¶08: not in a shared lane)")
    if rule_ids is not None:
        bad = [i for i in (row.get("accepted_rule_ids") or "").split(";") if i and i not in rule_ids]
        if bad:
            errors.append("rule IDs not in the region's passages: " + ", ".join(bad))
    for side in SIDES:
        line = row.get(f"{side}_line", "")
        if line:
            try:
                pts = json.loads(line)
                assert isinstance(pts, list) and all(len(p) == 2 for p in pts)
            except (ValueError, AssertionError, TypeError):
                errors.append(f"{side} line: not a list of [x, y] points")
    return errors, warnings


# ------------------------------------------------------------------ suggestions from the datasets' own lane annotations

BDD_TYPE = {  # BDD100K laneType -> (colour, pattern when solid, pattern when dashed)
    "single white": ("white", "solid", "dashed"), "double white": ("white", "double_solid", "double_dashed"),
    "single yellow": ("yellow", "solid", "dashed"), "double yellow": ("yellow", "double_solid", "solid_dashed"),
    "single other": ("other", "solid", "dashed"), "double other": ("other", "double_solid", "double_dashed"),
}


def _x_at(pts: list, y: float) -> float | None:
    pts = sorted(pts, key=lambda p: p[1])
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if y1 <= y <= y2 and y2 > y1:
            return x1 + (x2 - x1) * (y - y1) / (y2 - y1)
    return None


def _bottom_x(pts: list, h: int) -> float | None:
    """x of a line near the bottom of the image (extended from its lowest part when it ends higher up)."""
    pts = sorted(pts, key=lambda p: p[1])
    if len(pts) < 2:
        return None
    y = min(h * 0.92, pts[-1][1])
    x = _x_at(pts, y)
    if x is None:
        return None
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    if y2 > y1 and y2 < h * 0.92:
        x = x2 + (x2 - x1) * (h * 0.92 - y2) / (y2 - y1)
    return x


def ego_boundaries(lines: list[dict], w: int, h: int) -> dict:
    """Pick the two lines that bound my lane: the nearest on each side of the image centre, near the bottom.

    lines: [{'points': [[x, y], ...], ...attributes}]. Returns {'left': line or None, 'right': line or None}."""
    cx = w / 2
    best = {"left": None, "right": None}
    for ln in lines:
        x = _bottom_x(ln["points"], h)
        if x is None:
            continue
        side = "left" if x < cx else "right"
        d = abs(x - cx)
        if best[side] is None or d < best[side][0]:
            best[side] = (d, ln)
    return {s: (v[1] if v else None) for s, v in best.items()}


def bdd_lines(ann: dict) -> list[dict]:
    """The parallel lane lines of one Dataset Ninja BDD100K annotation, with colour, pattern and curb."""
    import ast
    out = []
    for o in ann.get("objects", []):
        if o.get("classTitle") != "lane":
            continue
        attrs = {}
        for t in o.get("tags", []):
            if t.get("name") == "attributes":
                try:
                    attrs = ast.literal_eval(t.get("value") or "{}")
                except (ValueError, SyntaxError):
                    attrs = {}
        if str(attrs.get("laneDirection", "parallel")).lower() != "parallel":
            continue
        typ, style = str(attrs.get("laneType", "")).lower(), str(attrs.get("laneStyle", "")).lower()
        pts = (o.get("points") or {}).get("exterior") or []
        if len(pts) < 2:
            continue
        if typ == "road curb":
            out.append({"points": pts, "color": "none", "pattern": "none", "curb": "yes"})
        elif typ in BDD_TYPE:
            col, solid, dashed = BDD_TYPE[typ]
            out.append({"points": pts, "color": col, "pattern": dashed if style == "dashed" else solid, "curb": "no"})
    return out


def culane_lines(lines_file: Path) -> list[dict]:
    """CULane lines (positions only; CULane gives no colour or pattern)."""
    out = []
    if not Path(lines_file).exists():
        return out
    for line in Path(lines_file).read_text(encoding="utf-8", errors="replace").splitlines():
        v = [float(x) for x in line.split()]
        pts = [[v[i], v[i + 1]] for i in range(0, len(v) - 1, 2) if v[i] >= 0]
        if len(pts) >= 2:
            out.append({"points": pts})
    return out


def dataset_suggestion(paths: Paths, trip: Trip, frame: dict) -> dict:
    """Boundary suggestions for one picked dataset image from the dataset's own lane annotation ({} if none).

    BDD100K: colour, pattern, curb and the line; CULane: the line only. Shown in the lane form for the annotator to
    accept or change, and recorded in prefill_source."""
    src_root = source_path(paths, trip.meta.get("source_root", ""))
    ref = frame.get("source_ref", "")
    w, h = int(float(frame.get("width") or 0) or 1280), int(float(frame.get("height") or 0) or 720)
    if not ref or not src_root.exists():
        return {}
    if paths.collection == "bdd100k":
        name = Path(ref).name
        f = src_root / "ann" / f"{name}.json"
        if not f.exists():
            return {}
        lines = bdd_lines(json.loads(f.read_text(encoding="utf-8")))
        source = "bdd100k lane annotation"
    elif paths.collection == "culane":
        f = (src_root / ref).with_suffix(".lines.txt")
        lines = culane_lines(f)
        source = "culane lane annotation (positions only)"
    else:
        return {}
    pick = ego_boundaries(lines, w, h)
    out = {"prefill_source": source}
    for side, ln in pick.items():
        if not ln:
            continue
        out[f"{side}_line"] = json.dumps([[round(x, 1), round(y, 1)] for x, y in ln["points"]])
        for f_ in ("color", "pattern", "curb"):
            if ln.get(f_):
                out[f"{side}_{f_}"] = ln[f_]
    return out


# ------------------------------------------------------------------ final label from the annotations

def lane_differences(a: dict, b: dict) -> list[str]:
    out = []
    for f in LANE_COMPARE:
        x, y = a.get(f) or "", b.get(f) or ""
        if f == "markings":
            x, y = join_tokens(x), join_tokens(y)
        if f.endswith("_near_line"):
            x, y = (x if x != "not_applicable" else ""), (y if y != "not_applicable" else "")
        if x != y:
            out.append(f)
    return out


def merge_lane_item(item: dict, anns: list[dict], required: int) -> dict:
    item = dict(item)
    if item.get("final_source") == "adjudicated" or item.get("lane_status") == "excluded":
        return item
    done = [a for a in anns if a.get("status") == "done"]
    item["annotators"] = ";".join(a["annotator"] for a in done)
    for f in LANE_FINAL:
        item[f] = ""
    item["final_source"] = ""
    if len(done) < required:
        item["lane_status"] = "waiting" if done else "kept"
        return item
    if any(a.get("unsure") == "1" for a in done) or any(lane_differences(done[0], a) for a in done[1:]):
        item["lane_status"] = "conflict"
        return item
    for f in LANE_FINAL:
        item[f] = done[0].get(f, "")
    ids = []
    for a in done:
        for i in (a.get("accepted_rule_ids") or "").split(";"):
            if i and i not in ids:
                ids.append(i)
    item["accepted_rule_ids"] = ";".join(ids)
    item["lane_status"] = "done"
    item["final_source"] = "agreed" if len(done) > 1 else "single"
    return item


def lane_required(meta: dict, split: str = "") -> int:
    """Independent lane labels an image needs: the set's lane_annotators_required, a number or one number per split
    (for example {"dev": 1, "test": 2}), else annotators_required, else 2."""
    base = meta.get("annotators_required", 2)
    value = meta.get("lane_annotators_required", base)
    if isinstance(value, dict):
        value = value.get(split, value.get("default", base))
    return int(value)


def merge_lanes(paths: Paths, trip: Trip, save: bool = True) -> Counter:
    lanes = LaneStore(lanes_csv(paths, trip.id))
    anns = LaneAnnotationStore(lane_annotations_csv(paths, trip.id))
    counts = Counter()
    for iid, item in list(lanes.rows.items()):
        new = merge_lane_item(item, anns.for_image(iid), lane_required(trip.meta, item.get("split", "")))
        lanes.put(new)
        counts[new["lane_status"]] += 1
    if save:
        lanes.save()
    return counts


def adjudicate_lane(paths: Paths, trip: Trip, image_id: str, choice: str, fields: dict | None, note: str, decided_by: str) -> dict:
    """choice: an annotator code, 'edit' (fields given), 'exclude' or 'reopen'."""
    lanes = LaneStore(lanes_csv(paths, trip.id))
    anns = LaneAnnotationStore(lane_annotations_csv(paths, trip.id))
    item = lanes.get(image_id)
    if item is None:
        raise ToolError(f"Unknown image {image_id}")
    item = dict(item)
    req = lane_required(trip.meta, item.get("split", ""))
    if choice == "reopen":
        item.update({"final_source": "", "adjudication_note": "", "lane_status": "kept"})
        item = merge_lane_item(item, anns.for_image(image_id), req)
    elif choice == "exclude":
        item.update({"lane_status": "excluded", "final_source": "adjudicated", "adjudication_note": f"exclude: {note}".strip()})
    else:
        src = fields if choice == "edit" else anns.get(image_id, choice)
        if not src:
            raise ToolError(f"No lane annotation from {choice} for {image_id}")
        for f in LANE_FINAL:
            item[f] = src.get(f, "") or ""
        item["markings"] = join_tokens(item["markings"])
        item.update({"lane_status": "done", "final_source": "adjudicated", "adjudication_note": f"{choice}: {note}".strip(),
                     "labeler": decided_by, "label_date": today()})
    item["annotators"] = ";".join(a["annotator"] for a in anns.for_image(image_id) if a.get("status") == "done")
    lanes.put(item)
    lanes.save()
    return item


def _kappa(pairs: list[tuple[str, str]]) -> float | None:
    if not pairs:
        return None
    po = sum(a == b for a, b in pairs) / len(pairs)
    cats = Counter(v for p in pairs for v in p)
    pe = sum((c / (2 * len(pairs))) ** 2 for c in cats.values())
    return None if pe >= 1.0 else (po - pe) / (1 - pe)


def lane_agreement(paths: Paths, set_ids: list[str] | None = None) -> dict:
    """Agreement of two independent lane annotations per image: percent and Fleiss' kappa per compared field."""
    pairs: dict[str, list] = defaultdict(list)
    all_ok = []
    for sid in set_ids or list_trip_ids(paths):
        by = defaultdict(list)
        for a in LaneAnnotationStore(lane_annotations_csv(paths, sid)).all():
            if a.get("status") == "done":
                by[a["image_id"]].append(a)
        for rows in by.values():
            if len(rows) < 2:
                continue
            x, y = sorted(rows, key=lambda r: (r.get("saved_utc", ""), r["annotator"]))[:2]
            for f in LANE_COMPARE:
                vx, vy = x.get(f, ""), y.get(f, "")
                if f == "markings":
                    vx, vy = join_tokens(vx), join_tokens(vy)
                pairs[f].append((vx, vy))
            all_ok.append(not lane_differences(x, y))
    fields = []
    for f in LANE_COMPARE:
        ps = pairs.get(f, [])
        k = _kappa(ps)
        fields.append({"field": f, "items": len(ps),
                       "percent_agreement": round(sum(a == b for a, b in ps) / len(ps), 3) if ps else "",
                       "fleiss_kappa": round(k, 3) if k is not None else ""})
    return {"items": len(all_ok), "all_fields_agree": round(sum(all_ok) / len(all_ok), 3) if all_ok else None, "fields": fields}


def write_lane_agreement(paths: Paths) -> dict:
    ag = lane_agreement(paths)
    write_csv(paths.labels_dir / "lane_agreement.csv", ag["fields"], ["field", "items", "percent_agreement", "fleiss_kappa"])
    return ag


def lane_status_counts(paths: Paths, set_id: str) -> Counter:
    return Counter(r.get("lane_status") or "kept" for r in LaneStore(lanes_csv(paths, set_id)).all())


def annotation_row(image_id: str, annotator: str, fields: dict, status: str, source: str = "local", package_id: str = "",
                   unsure: bool = False, comment: str = "") -> dict:
    row = {c: fields.get(c, "") for c in LANE_FINAL}
    row.update({"image_id": image_id, "annotator": annotator, "source": source, "package_id": package_id,
                "status": status, "unsure": "1" if unsure else "0", "comment": comment, "saved_utc": utc_now()})
    for s in SIDES:
        if row.get(f"{s}_pattern") != "solid_dashed":
            row[f"{s}_near_line"] = "not_applicable"
    row["markings"] = join_tokens(row["markings"])
    return row


__all__ = ["LANE_ACTIONS", "LANE_COLUMNS", "LANE_COMPARE", "LANE_FINAL", "LaneStore", "LaneAnnotationStore", "lanes_csv",
           "lane_annotations_csv", "load_lane_schema", "load_lane_rules", "lane_prefill", "contested_lane_actions",
           "validate_lane", "seed_lane_rows", "dataset_suggestion", "merge_lanes", "adjudicate_lane", "lane_agreement",
           "split_tokens", "join_tokens", "annotation_row"]
