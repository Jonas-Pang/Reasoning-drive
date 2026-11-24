"""Replay the frozen test set through the advisor's verification + feedback path (no model call).

For every test photo with an answer of the main configuration (model + lane prompt below), the script
  1. runs the verification layer (reasoning_drive/web/guard.py) on the saved answer and logs it like a live request
     (results/app/predictions.jsonl, mode = "replay"), and
  2. writes the feedback a careful reviewer would give, taken from the final label: each action right/wrong, each line
     right/wrong, overall good if all 7 actions are right, and a short comment naming the error
     (results/app/feedback.csv, source = "simulated_reviewer").

This is how the monitoring and the feedback analysis are tested before real users exist; the rows are marked as
simulated everywhere (Monitor tab, Grafana label source, feedback_report.py). Run it again with --clear to start over.

usage: python scripts/replay_feedback.py [--model gemma4:31b] [--prompt lane_v4c] [--test B] [--limit 0] [--clear]
Added by Claude, 2026-11-18.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from reasoning_drive import config as C            # noqa: E402
from reasoning_drive import paths as P             # noqa: E402
from reasoning_drive.agent import lane as L        # noqa: E402
from reasoning_drive.web import guard              # noqa: E402
from reasoning_drive.web.feedback import ACTIONS, AppLog   # noqa: E402


def comment_for(ans: dict, lab: dict) -> str:
    """A reviewer-style comment naming the first error (English, feeds the theme coding)."""
    notes = []
    for side in ("left", "right"):
        b = ans.get(f"{side}_boundary") or {}
        lc, lp = lab.get(f"{side}_color", ""), lab.get(f"{side}_pattern", "")
        if b.get("pattern") and lp and b.get("pattern") != lp:
            notes.append(f"the {side} line is {lp.replace('_', ' ')}, not {str(b.get('pattern')).replace('_', ' ')}")
        elif b.get("color") and lc and b.get("color") != lc:
            notes.append(f"the {side} line is {lc}, not {b.get('color')} (line colour)")
        if lab.get(f"{side}_role") == "special_lane_line" and b.get("role") != "special_lane_line":
            notes.append(f"the {side} side is a bus / special lane")
    acts = ans.get("actions") or {}
    for a in ACTIONS:
        want, got = lab.get(f"act_{a}", ""), acts.get(a, "")
        if want and got and want != got:
            if want == "prohibited" and got == "allowed":
                notes.append(f"{a.replace('_', ' ')} should be prohibited (unsafe)")
            elif want == "allowed" and got == "prohibited":
                notes.append(f"{a.replace('_', ' ')} should be allowed (too cautious)")
            elif a in ("turn_left", "turn_right", "u_turn", "go_straight"):
                notes.append(f"{a.replace('_', ' ')}: check the arrow ({want.replace('_', ' ')})")
    return "; ".join(notes[:3])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="gemma4:31b")
    ap.add_argument("--prompt", default="lane_v4c")
    ap.add_argument("--test", default="B", choices=["A", "B"])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--clear", action="store_true", help="remove earlier simulated rows first")
    args = ap.parse_args()
    cfg = C.load(REPO)
    log = AppLog(REPO)
    if args.clear:
        for f in (log.pred, log.fb):
            if f.exists():
                f.write_text("", encoding="utf-8")   # emptied, not deleted (some shared drives do not allow deleting)
        log = AppLog(REPO)
    labels = {}
    for region in ("CN", "US", "UK", "IN"):
        for it in L.load_lane_items(cfg, region, "test"):
            labels[it.image_id] = (it, it.label)
    recs = {}
    for d in sorted(P.runs_dir(REPO).glob(f"*_lane{args.test}_*")):
        try:
            man = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if man.get("mock") or man.get("split") != "test" or man["settings"].get("model") != args.model:
            continue
        if man.get("prompt_hashes", {}).get("prompt_dir") != f"prompts/{args.prompt}":
            continue
        for r in L.load_lane_run(cfg, d.name)["records"]:
            if r.get("answer") and r["image_id"] in labels:
                recs[r["image_id"]] = r                     # the newest run wins (runs are sorted by time)
    items = sorted(recs.values(), key=lambda r: (r["region"], r["image_id"]))
    if args.limit:
        items = items[: args.limit]
    cfg["api"]["model"] = args.model
    cfg.setdefault("lane", {})["prompt_dir"] = f"prompts/{args.prompt}"
    n_bad = n_rev = 0
    for r in items:
        it, lab = labels[r["image_id"]]
        check = guard.verify(REPO, r["region"], r, it.path)
        rid = log.log_prediction(r, check, cfg, "replay")
        ans = r["answer"]
        acts = {a: ("right" if (ans.get("actions") or {}).get(a) == lab.get(f"act_{a}") else "wrong") for a in ACTIONS if lab.get(f"act_{a}")}
        lines = {s: ("right" if (ans.get(f"{s}_boundary") or {}).get("color") == lab.get(f"{s}_color")
                     and (ans.get(f"{s}_boundary") or {}).get("pattern") == lab.get(f"{s}_pattern") else "wrong") for s in ("left", "right")}
        rating = "good" if all(v == "right" for v in acts.values()) else "bad"
        n_bad += rating == "bad"
        n_rev += bool(check["needs_review"])
        log.add_feedback({"request_id": rid, "rating": rating, "actions": acts, "lines": lines, "comment": comment_for(ans, lab)},
                         source="simulated_reviewer")
    print(f"replayed {len(items)} answers ({args.model}, {args.prompt}, Test {args.test}): "
          f"{n_bad} rated bad, {n_rev} flagged for review -> {log.pred} and {log.fb}")


if __name__ == "__main__":
    main()
