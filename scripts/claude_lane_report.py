"""Written by Claude: a table of the lane runs, with the owner's rule of 2026-11-16 applied to the action score.

    python scripts/claude_lane_report.py                 every finished real run on the test split
    python scripts/claude_lane_report.py --split dev
    python scripts/claude_lane_report.py --runs 20261116_003746_laneA_CN 20261116_004611_laneB_CN

Owner's rule (2026-11-16): an action the label marks "not_determined" (无法判断, the label could not decide it from the
image) is not scored. Such a cell counts neither as right nor as wrong, like a contested cell; an image whose decided
actions are all not_determined drops out of the action score. Nothing else changes: the boundaries, the markings, the
unsafe and over-cautious counts are as the run scored them (a not_determined label is never unsafe or over-cautious).

This only re-counts the saved answers in results/runs/<run>/results.jsonl; it sends nothing to the API and does not
touch the frozen scoring code (reasoning_drive/evaluation/lane_scoring.py), so the frozen protocol stays valid.
Both numbers are reported: the score as frozen and the score with the rule. The rule was decided after the first test
runs; say so where the numbers are published.

Extra columns (2026-11-17, owner's request to find why the local models score low; re-counted from the saved answers):
  lines_seen_right        both boundaries with the label's colour and pattern
  change_ok_if_seen       change_left/right correct where that side's line was seen right (the reasoning)
  change_ok_if_misseen    the same where the line was seen wrong (perception errors carried into the decision)
  next_actions_allowed    the owner's simpler reading: per image, only which of change left/right and turn left/right
                          are allowed (allowed or stop_first), plus whether a stop is required, all right
Only Tests A, B and C are listed by default (owner's decision 2026-11-17: D and R are not used for now; --tests to change).

Writes results/lane_report_<split>.csv and .md and prints the table."""
import argparse
import csv
import json
import sys
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
runs_dir = repo / "results" / "runs"

ap = argparse.ArgumentParser()
ap.add_argument("--split", default="test")
ap.add_argument("--runs", nargs="*", help="run IDs (default: every finished real run on --split, newest per model, test and region)")
ap.add_argument("--tests", default="A,B,C", help="tests to list (default A,B,C)")
ap.add_argument("--all", action="store_true", help="list every matching run, not only the newest per model, test and region")
a = ap.parse_args()


def pct(k, n):
    return f"{k}/{n} ({k / n:.0%})" if n else "-"


def load(run_id):
    d = runs_dir / run_id
    m = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    rows = [json.loads(line) for line in (d / "results.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    return m, rows


def summarize(m, rows):
    n_img = len(rows)
    errors = sum(1 for r in rows if r.get("error") or r.get("parse_error"))
    act_all = act_ok = act2_all = act2_ok = cells = cells_ok = cells2 = cells2_ok = 0
    lane_n = lane_ok = both_n = both_ok = unsafe = cautious = nd_cells = 0
    ex = {"seen": [0, 0], "miss": [0, 0], "lines": [0, 0], "next": [0, 0]}
    for r in rows:
        s, lab = r["score"], r["label"]
        acts = s.get("actions") or {}
        if acts:
            act_all += 1
            act_ok += all(acts.values())
            cells += len(acts)
            cells_ok += sum(acts.values())
        kept = {k: v for k, v in acts.items() if lab.get("act_" + k) != "not_determined"}
        nd_cells += len(acts) - len(kept)
        if kept:
            act2_all += 1
            act2_ok += all(kept.values())
            cells2 += len(kept)
            cells2_ok += sum(kept.values())
        if s.get("lane") is not None:
            lane_n += 1
            lane_ok += bool(s["lane"])
        sides = [v["all"] for v in (s.get("sides") or {}).values() if v]
        if sides:
            both_n += 1
            both_ok += all(sides)
        unsafe += len(s.get("unsafe") or [])
        cautious += len(s.get("over_cautious") or [])
        ans = r.get("answer") or {}
        seen = {}
        for side in ("left", "right"):
            b = ans.get(side + "_boundary") or {}
            seen[side] = b.get("color") == lab.get(side + "_color") and b.get("pattern") == lab.get(side + "_pattern")
            act = "change_" + side
            if lab.get("act_" + act) in (None, "", "not_determined"):
                continue
            ok = (ans.get("actions") or {}).get(act) == lab.get("act_" + act)
            ex["seen" if seen[side] else "miss"][0] += ok
            ex["seen" if seen[side] else "miss"][1] += 1
        if ans:
            ex["lines"][1] += 1
            ex["lines"][0] += seen["left"] and seen["right"]
        four = ["change_left", "change_right", "turn_left", "turn_right"]
        if ans and not any(lab.get("act_" + k) == "not_determined" for k in four):
            got = ans.get("actions") or {}
            allow = lambda v: v in ("allowed", "stop_first")
            stop_l = any(v == "stop_first" for k, v in lab.items() if k.startswith("act_"))
            stop_a = any(v == "stop_first" for v in got.values())
            ex["next"][1] += 1
            ex["next"][0] += all(allow(lab.get("act_" + k)) == allow(got.get(k)) for k in four) and stop_l == stop_a
    return {
        "run_id": m["run_id"], "model": (m.get("settings") or {}).get("model", ""), "test": m.get("test"), "region": m.get("region"), "split": m.get("split"),
        "prompt": (m.get("prompt_hashes") or {}).get("prompt_dir", ""), "again": bool(m.get("again")),
        "images": n_img, "errors": errors,
        "lane_identified": pct(lane_ok, lane_n), "both_boundaries": pct(both_ok, both_n),
        "actions_all_correct_frozen": pct(act_ok, act_all),
        "actions_all_correct_owner_rule": pct(act2_ok, act2_all),
        "action_cells_correct_frozen": pct(cells_ok, cells),
        "action_cells_correct_owner_rule": pct(cells2_ok, cells2),
        "not_determined_cells_left_out": nd_cells,
        "unsafe": unsafe, "over_cautious": cautious,
        "lines_seen_right": pct(*ex["lines"]), "change_ok_if_seen": pct(*ex["seen"]),
        "change_ok_if_misseen": pct(*ex["miss"]), "next_actions_allowed": pct(*ex["next"]),
    }


ids = a.runs
if not ids:
    found = []
    for d in sorted(runs_dir.glob("*_lane*")):
        if d.name.endswith("_mock") or not (d / "results.jsonl").exists() or not (d / "manifest.json").exists():
            continue
        try:
            m = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
        except ValueError:
            continue
        if m.get("mock") or m.get("split") != a.split or m.get("test") not in a.tests.split(","):
            continue
        found.append((d.name, m))
    if not a.all:   # newest run per test and region that has no failed requests
        best = {}
        for rid, m in found:
            try:
                sc = json.loads((runs_dir / rid / "scores.json").read_text(encoding="utf-8"))["summary"]
            except (OSError, ValueError, KeyError):
                continue
            if sc.get("errors"):
                continue
            best[((m.get("settings") or {}).get("model", ""), m.get("test"), m.get("region"))] = rid
        ids = [best[k] for k in sorted(best, key=lambda k: (k[0] != "gpt-6.1-sol", k[0], k[2], k[1]))]
    else:
        ids = [rid for rid, _ in found]
if not ids:
    sys.exit(f"No finished runs on the {a.split} split.")

table = [summarize(*load(r)) for r in ids]
cols = list(table[0].keys())
out = repo / "results" / f"lane_report_{a.split}"
with open(out.with_suffix(".csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(table)
show = ["model", "region", "test", "images", "lane_identified", "both_boundaries", "actions_all_correct_frozen",
        "actions_all_correct_owner_rule", "action_cells_correct_owner_rule", "not_determined_cells_left_out", "unsafe",
        "over_cautious", "lines_seen_right", "change_ok_if_seen", "change_ok_if_misseen", "next_actions_allowed",
        "again", "run_id"]
md = [f"# Lane runs, {a.split} split", "",
      "Owner's rule (2026-11-16): actions the label marks not_determined are not scored (columns 'owner rule').", "",
      "| " + " | ".join(show) + " |", "|" + "---|" * len(show)]
md += ["| " + " | ".join(str(t[c]) for c in show) + " |" for t in table]
out.with_suffix(".md").write_text("\n".join(md) + "\n", encoding="utf-8")
print("\n".join(md))
print(f"\nWritten: {out.with_suffix('.csv')} and .md")
