"""Blind review of the lane answers that disagree with the label (before any change to the prompt).

For every image, each field where at least one saved answer of Test A or Test B differs from the final label becomes
one item:

  boundary:<side>    which description of that line is right (colour, pattern, the line nearer my lane, curb)
  marking:<token>    is this marking painted in my lane (yes or no)
  action:<action>    which value is right for this action

The options are the values of the label and of the answers, in an order fixed by a hash of the item, and the page never
says which value came from the label, from the model or from which test. "Cannot tell from the photo" is always
possible. Decisions are written to results/runs/review/lane_review.csv (one row per item, the newest decision counts); the
label files are not changed. Scores after the review apply the decisions on top of the labels (label_after_review):

  boundary  the chosen line replaces the label's; cannot tell -> the side is not scored
  marking   yes adds the token, no removes it; cannot tell -> the token is accepted whether listed or not
  action    the chosen value replaces the label's; cannot tell -> the action is not scored

python main.py lane review              items and decisions per region
python main.py lane rescore --reviewed  scores after the review (scores_reviewed.json), next to the originals
The review page: http://localhost:8770/review (python main.py demo).
"""
from __future__ import annotations

import csv
import hashlib
import threading
from datetime import datetime, timezone
from pathlib import Path

from .. import paths as P
from ..config import repo_of
from .lane_scoring import ACTIONS, SIDES, tokens_of

REVIEW_FILE = Path(P.RUNS) / "review" / "lane_review.csv"
COLUMNS = ["item_id", "image_id", "region", "field", "decision", "value", "reviewer", "time_utc"]
DECISIONS = ("option", "cannot_tell")
_LOCK = threading.Lock()


def review_path(cfg: dict) -> Path:
    return repo_of(cfg) / REVIEW_FILE


def boundary_value(attrs: dict) -> str:
    """colour|pattern|line nearer my lane (solid-and-broken pairs only)|curb"""
    pattern = attrs.get("pattern") or "none"
    near = (attrs.get("near_line") or "") if pattern == "solid_dashed" else ""
    return "|".join([attrs.get("color") or "none", pattern, near, attrs.get("curb") or "no"])


def _label_side(label: dict, side: str) -> dict:
    return {k: label.get(f"{side}_{k}", "") for k in ("color", "pattern", "near_line", "curb")}


def _shuffled(item_id: str, values: set) -> list:
    return sorted(values, key=lambda v: hashlib.sha1(f"{item_id}\0{v}".encode()).hexdigest())


def load_decisions(cfg: dict) -> dict:
    """item_id -> the newest decision row."""
    p = review_path(cfg)
    if not p.exists():
        return {}
    out = {}
    with open(p, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("item_id") and row.get("decision") in DECISIONS:
                out[row["item_id"]] = row
    return out


def decisions_by_image(decisions: dict) -> dict:
    out: dict[str, dict] = {}
    for row in decisions.values():
        out.setdefault(row["image_id"], {})[row["field"]] = row
    return out


def save_decision(cfg: dict, item: dict, decision: str, value: str = "", reviewer: str = "") -> dict:
    if decision not in DECISIONS:
        raise ValueError(f"decision must be one of {', '.join(DECISIONS)}")
    if decision == "option" and value not in item["options"]:
        raise ValueError("The value is not one of the options of this item.")
    row = {"item_id": item["item_id"], "image_id": item["image_id"], "region": item["region"], "field": item["field"],
           "decision": decision, "value": value if decision == "option" else "", "reviewer": str(reviewer or "")[:40],
           "time_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    p = review_path(cfg)
    with _LOCK:
        rows = load_decisions(cfg)
        rows[row["item_id"]] = row
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(".tmp")
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            w.writeheader()
            for r in sorted(rows.values(), key=lambda r: (r["region"], r["image_id"], r["field"])):
                w.writerow({k: r.get(k, "") for k in COLUMNS})
        tmp.replace(p)
    return row


def label_after_review(label: dict, decisions: dict | None) -> dict:
    """The label with the review decisions of its image applied (decisions: field -> row)."""
    if not decisions:
        return label
    lab = dict(label)
    toks, optional = tokens_of(lab.get("markings", "")), tokens_of(lab.get("markings_optional", ""))
    for field, d in decisions.items():
        kind, _, key = field.partition(":")
        tell = d.get("decision") == "option"
        if kind == "boundary" and key in SIDES:
            if not tell:
                lab[f"{key}_evidence"] = "insufficient"
                continue
            color, pattern, near, curb = (d["value"].split("|") + ["", "", "", ""])[:4]
            lab.update({f"{key}_color": color, f"{key}_pattern": pattern, f"{key}_near_line": near or "not_applicable",
                        f"{key}_curb": curb})
            if lab.get(f"{key}_evidence") == "insufficient":
                lab[f"{key}_evidence"] = "partial"
        elif kind == "marking":
            if not tell:
                optional.add(key)
            elif d["value"] == "yes":
                toks.add(key)
            else:
                toks.discard(key)
        elif kind == "action" and key in ACTIONS:
            lab[f"act_{key}"] = d["value"] if tell else ""
    lab["markings"] = ";".join(sorted(toks))
    lab["markings_optional"] = ";".join(sorted(optional))
    return lab


def review_items(cfg: dict, region: str, run_ids: list | None = None) -> dict:
    """The items of one region from the saved answers of the finished lane runs of Test A and Test B (mock runs and the
    control Test C left out: its actions follow another region's rules, so they say nothing about the label)."""
    from ..agent.lane import list_lane_runs, load_lane_items, load_lane_run
    labels = {it.image_id: it.label for it in load_lane_items(cfg, region, "any")}
    runs = run_ids or [r["run_id"] for r in list_lane_runs(cfg)
                       if r["finished"] and not r["mock"] and r["region"] == region and r["test"] in ("A", "B")]
    answers: dict[str, list] = {}
    for rid in runs:
        for rec in load_lane_run(cfg, rid)["records"]:
            if rec.get("answer") and rec["image_id"] in labels:
                answers.setdefault(rec["image_id"], []).append(rec["answer"])
    decided = load_decisions(cfg)
    items = []
    for image_id in sorted(answers):
        lab, ans = labels[image_id], answers[image_id]
        fields: dict[str, set] = {}
        for side in SIDES:
            if lab.get(f"{side}_evidence") == "insufficient" or not lab.get(f"{side}_color"):
                continue
            want = boundary_value(_label_side(lab, side))
            got = {boundary_value(a.get(f"{side}_boundary") or {}) for a in ans}
            if got - {want}:
                fields[f"boundary:{side}"] = got | {want}
        if lab.get("markings_evidence") != "insufficient":
            lt = tokens_of(lab.get("markings", ""))
            for a in ans:
                at = {m.get("marking") for m in a.get("lane_markings") or [] if isinstance(m, dict) and m.get("marking")}
                for t in lt ^ at:
                    fields[f"marking:{t}"] = {"yes", "no"}
        for act in ACTIONS:
            want = lab.get(f"act_{act}", "")
            if want in ("", "not_applicable"):
                continue
            got = {(a.get("actions") or {}).get(act) for a in ans} - {None}
            if got - {want}:
                fields[f"action:{act}"] = got | {want}
        for field, values in sorted(fields.items()):
            item_id = f"{region}|{image_id}|{field}"
            kind, _, key = field.partition(":")
            d = decided.get(item_id)
            items.append({"item_id": item_id, "image_id": image_id, "region": region, "field": field, "kind": kind, "key": key,
                          "options": ["yes", "no"] if kind == "marking" else _shuffled(item_id, values),
                          "decided": {"decision": d["decision"], "value": d["value"]} if d else None})
    return {"region": region, "runs": runs, "items": items, "n": len(items), "decided": sum(1 for i in items if i["decided"]),
            "images": len({i["image_id"] for i in items})}


def find_item(cfg: dict, item_id: str) -> dict:
    region = item_id.split("|", 1)[0]
    for it in review_items(cfg, region)["items"]:
        if it["item_id"] == item_id:
            return it
    raise ValueError(f"No review item {item_id}.")


def review_summary(cfg: dict, region: str) -> dict:
    """How the decided items compare with the label: kept, changed, cannot tell; per kind of field."""
    from ..agent.lane import load_lane_items
    labels = {it.image_id: it.label for it in load_lane_items(cfg, region, "any")}
    res = review_items(cfg, region)
    out: dict = {"region": region, "items": res["n"], "decided": res["decided"], "images": res["images"], "by_kind": {}}
    for it in res["items"]:
        k = out["by_kind"].setdefault(it["kind"], {"items": 0, "label_kept": 0, "label_changed": 0, "cannot_tell": 0})
        k["items"] += 1
        d = it["decided"]
        if not d:
            continue
        lab = labels[it["image_id"]]
        if d["decision"] == "cannot_tell":
            k["cannot_tell"] += 1
            continue
        if it["kind"] == "boundary":
            same = d["value"] == boundary_value(_label_side(lab, it["key"]))
        elif it["kind"] == "marking":
            same = (d["value"] == "yes") == (it["key"] in tokens_of(lab.get("markings", "")))
        else:
            same = d["value"] == lab.get(f"act_{it['key']}", "")
        k["label_kept" if same else "label_changed"] += 1
    return out


__all__ = ["review_items", "review_summary", "save_decision", "load_decisions", "decisions_by_image", "label_after_review",
           "boundary_value", "find_item", "REVIEW_FILE"]
