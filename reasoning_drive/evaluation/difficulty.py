"""Two properties of every lane label, computed from the label and the countries' rule tables (no model involved).

Rule-sensitive (after GeoDrive-Bench's counterfactual check): the label's observed lane (boundaries and markings) is read
with every other country's rule table; an image is rule-sensitive when at least one action that both tables decide gets
a different value (for example a Chinese white solid lane line: prohibited under GB 5768, allowed under the MUTCD). Only
these images can show what the region's own rules add; the others can be answered with any country's rules.

Composition level (after DriveCombo's ladder, reduced to what a lane shows):
  L1  one kind of governing element: only lane boundaries of one kind, no arrow, prohibited-movement marking or area
  L2  several kinds of governing elements, each deciding its own actions
  L3  elements that interact: an action decided by two elements (an arrow and a waiting area, an arrow and a no-turn
      marking), a solid-and-broken pair (the side decides), a special lane (bus, HOV, tidal, reversible), or a lane that
      commits the car: a marking in the lane prohibits a movement and a boundary prohibits leaving the lane, so the two
      rules together decide where the car can go
Words, symbols and lines across the lane govern none of the seven actions and do not count.

    python main.py lane difficulty        both properties for every lane label (results/reports/lane_difficulty.csv)
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from .. import paths as P

DECIDED = ("allowed", "prohibited")
SIDES = ("left", "right")


def _tables(repo) -> tuple[dict, dict]:
    import json
    return P.lane_action_rules(repo), json.loads((Path(repo) / P.LANE_SCHEMA).read_text(encoding="utf-8"))


def _tokens(label: dict) -> list[str]:
    return [t for t in str(label.get("markings") or "").split(";") if t]


def governing_tokens(label: dict, schema: dict) -> list[str]:
    out = []
    for t in _tokens(label):
        if t in schema.get("movement_arrows", {}) or t in schema.get("no_turn", {}) or t.startswith("area:left_turn_waiting") \
                or t.startswith("area:two_way_left_turn_lane") or t.startswith("arrow:"):
            out.append(t)
    return out


def _only(label: dict, keep_side: str | None = None, keep_tokens: list[str] | None = None) -> dict:
    row = dict(label)
    for side in SIDES:
        if side != keep_side:
            for f in ("color", "pattern", "near_line", "curb", "role"):
                row[f"{side}_{f}"] = "none" if f in ("color", "pattern") else ("no" if f == "curb" else "")
    row["markings"] = ";".join(keep_tokens or [])
    return row


def element_actions(table: dict, schema: dict, region: str, label: dict) -> dict:
    """{element: set of actions it decides}, each element read alone with the region's rule table."""
    from ..labeling.lanes import lane_prefill
    out = {}
    for side in SIDES:
        if (label.get(f"{side}_pattern") or "none") != "none" or label.get(f"{side}_curb") == "yes":
            acts = lane_prefill(table, schema, region, _only(label, side, []))["actions"]
            out[f"{side}_boundary"] = {a for a, v in acts.items() if v in DECIDED}
    for t in governing_tokens(label, schema):
        acts = lane_prefill(table, schema, region, _only(label, None, [t]))["actions"]
        out[t] = {a for a, v in acts.items() if v in DECIDED}
    return out


def level(table: dict, schema: dict, region: str, label: dict) -> tuple[str, str]:
    """(L1|L2|L3, why)."""
    el = element_actions(table, schema, region, label)
    if not el:
        return "L1", "no governing element"
    counts = Counter(a for acts in el.values() for a in acts)
    shared = sorted(a for a, n in counts.items() if n >= 2)
    pair = [s for s in SIDES if label.get(f"{s}_pattern") == "solid_dashed"]
    special = [s for s in SIDES if label.get(f"{s}_role") == "special_lane_line"]
    from ..labeling.lanes import lane_prefill
    acts = lane_prefill(table, schema, region, label)["actions"]
    moves_closed = [a for a in ("go_straight", "turn_left", "turn_right", "u_turn") if acts.get(a) == "prohibited"]
    sides_closed = [a for a in ("change_left", "change_right") if acts.get(a) == "prohibited"]
    commits = bool(moves_closed and sides_closed)
    if shared or pair or special or commits:
        why = "; ".join(x for x in (f"actions decided by two elements: {', '.join(shared)}" if shared else "",
                                    f"solid-and-broken pair on the {' and '.join(pair)}" if pair else "",
                                    "special lane" if special else "",
                                    f"the lane commits the car ({', '.join(moves_closed)} prohibited by a marking, "
                                    f"{', '.join(sides_closed)} by a boundary)" if commits else "") if x)
        return "L3", why
    kinds = set()
    for k in el:
        if k.endswith("_boundary"):
            s = k.split("_")[0]
            kinds.add(("boundary", label.get(f"{s}_color"), label.get(f"{s}_pattern"), label.get(f"{s}_curb"), label.get(f"{s}_role")))
        else:
            kinds.add(("marking", k))
    return ("L1", "one kind of element") if len(kinds) == 1 else ("L2", f"{len(kinds)} kinds of element, each deciding its own actions")


def sensitivity(table: dict, schema: dict, region: str, label: dict) -> dict:
    """Actions whose value changes when the same observed lane is read with another country's rule table."""
    from ..labeling.lanes import lane_prefill
    own = lane_prefill(table, schema, region, label)["actions"]
    out = {}
    for other in sorted(k for k in table if k != region and isinstance(table.get(k), dict) and "boundary" in table[k]):
        alt = lane_prefill(table, schema, other, label)["actions"]
        diff = sorted(a for a in own if own[a] in DECIDED and alt.get(a) in DECIDED and own[a] != alt[a])
        if diff:
            out[other] = diff
    return {"sensitive": bool(out), "by_region": out, "actions": sorted({a for v in out.values() for a in v})}


def describe(repo, region: str, label: dict, tables: tuple[dict, dict] | None = None) -> dict:
    table, schema = tables or _tables(repo)
    lv, why = level(table, schema, region, label)
    sens = sensitivity(table, schema, region, label)
    return {"level": lv, "level_why": why, "rule_sensitive": sens["sensitive"], "sensitive_actions": sens["actions"],
            "sensitive_vs": sorted(sens["by_region"])}


def all_labels(cfg: dict) -> list[dict]:
    """Every final lane label in datasets/<CODE>/<collection>/*.lanes.csv (the images themselves are not needed)."""
    from ..config import repo_of
    out = []
    for f in sorted((repo_of(cfg) / P.DATASETS).glob("*/*/*.lanes.csv")):
        with open(f, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r.get("lane_status") == "done" and r.get("region") in cfg["regions"]:
                    out.append({"image_id": r["image_id"], "region": r["region"], "split": r.get("split", ""),
                                "dataset": r.get("dataset", ""), "label": r})
    return out


def write_table(cfg: dict) -> tuple[Path, list[dict]]:
    from ..config import repo_of
    repo = repo_of(cfg)
    tables = _tables(repo)
    rows = []
    for x in all_labels(cfg):
        d = describe(repo, x["region"], x["label"], tables)
        rows.append({"image_id": x["image_id"], "region": x["region"], "split": x["split"], "dataset": x["dataset"],
                     "level": d["level"], "level_why": d["level_why"], "rule_sensitive": "yes" if d["rule_sensitive"] else "no",
                     "sensitive_actions": ";".join(d["sensitive_actions"]), "sensitive_vs": ";".join(d["sensitive_vs"]),
                     "markings": x["label"].get("markings", ""),
                     "left": f"{x['label'].get('left_color')}/{x['label'].get('left_pattern')}",
                     "right": f"{x['label'].get('right_color')}/{x['label'].get('right_pattern')}"})
    out = repo / P.REPORTS / "lane_difficulty.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["image_id"])
        w.writeheader()
        w.writerows(rows)
    return out, rows


def overview_text(rows: list[dict]) -> str:
    lines = ["region  split  images  L1  L2  L3  rule-sensitive  (actions that change)"]
    for (reg, split), group in sorted(Counter((r["region"], r["split"]) for r in rows).items()):
        rs = [r for r in rows if r["region"] == reg and r["split"] == split]
        lv = Counter(r["level"] for r in rs)
        acts = Counter(a for r in rs for a in r["sensitive_actions"].split(";") if a)
        lines.append(f"{reg:6}  {split:5}  {len(rs):6}  {lv['L1']:2}  {lv['L2']:2}  {lv['L3']:2}  "
                     f"{sum(1 for r in rs if r['rule_sensitive'] == 'yes'):14}  {dict(acts)}")
    return "\n".join(lines)
