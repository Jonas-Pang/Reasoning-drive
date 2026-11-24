"""Analyse the feedback of the lane advisor (results/app/feedback.csv + predictions.jsonl).

Quantitative: ratings by region and source, wrong-rate per action and per line, and whether the verification layer
catches the answers users call bad (the "needs review" flag treated as a detector of bad answers: recall, precision).
Qualitative: comment themes (keyword coding, reasoning_drive/web/feedback.py THEMES) by region, plus example comments
per theme. If scikit-learn is installed, the comments are also clustered (TF-IDF + k-means) to find themes the keyword
list misses.

Writes results/app/feedback_report.md and results/app/feedback_actions.csv.
usage: python scripts/feedback_report.py [--source user|simulated_reviewer|all]
Added by Claude, 2026-11-18.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from reasoning_drive.web.feedback import ACTIONS, AppLog   # noqa: E402


def pct(a, b):
    return f"{100 * a / b:.0f} %" if b else "—"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="all")
    args = ap.parse_args()
    log = AppLog(REPO)
    fb = [r for r in log.feedback() if args.source == "all" or r.get("source") == args.source]
    preds = {p["request_id"]: p for p in log.predictions()}
    out = [f"# Feedback report ({len(fb)} feedback rows, source: {args.source})", ""]
    if not fb:
        print("no feedback yet"); return

    # ---- ratings
    out += ["## Ratings by region", "", "| region | good | bad | bad rate |", "|---|---|---|---|"]
    byr = defaultdict(Counter)
    for r in fb:
        byr[r["region"]][r["rating"] or "none"] += 1
    for reg, c in sorted(byr.items()):
        out.append(f"| {reg} | {c['good']} | {c['bad']} | {pct(c['bad'], c['good'] + c['bad'])} |")

    # ---- actions and lines
    out += ["", "## Wrong rate per action (right + wrong verdicts)", "", "| action | wrong | judged | wrong rate |", "|---|---|---|---|"]
    rows = []
    for a in ACTIONS:
        c = Counter(r.get(f"act_{a}") for r in fb if r.get(f"act_{a}"))
        n = c["right"] + c["wrong"]
        rows.append({"action": a, "wrong": c["wrong"], "judged": n, "wrong_rate": round(c["wrong"] / n, 3) if n else ""})
        out.append(f"| {a} | {c['wrong']} | {n} | {pct(c['wrong'], n)} |")
    with (log.dir / "feedback_actions.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    out += ["", "| line | wrong | judged | wrong rate |", "|---|---|---|---|"]
    for s in ("left", "right"):
        c = Counter(r.get(f"{s}_line") for r in fb if r.get(f"{s}_line"))
        out.append(f"| {s} | {c['wrong']} | {c['right'] + c['wrong']} | {pct(c['wrong'], c['right'] + c['wrong'])} |")

    # ---- does the verification layer catch bad answers?
    tp = fp = fn = tn = 0
    for r in fb:
        p = preds.get(r["request_id"])
        if not p or r["rating"] not in ("good", "bad"):
            continue
        flag, bad = bool(p.get("needs_review")), r["rating"] == "bad"
        tp += flag and bad; fp += flag and not bad; fn += (not flag) and bad; tn += (not flag) and not bad
    out += ["", "## Verification layer vs feedback", "",
            "The 'needs review' flag is set without a label (rule check, visibility). Treated as a detector of answers users rate bad:", "",
            f"- flagged and bad (caught): {tp} · flagged but good: {fp} · not flagged but bad (missed): {fn} · not flagged, good: {tn}",
            f"- recall (bad answers caught) = {pct(tp, tp + fn)}, precision (flagged answers that were bad) = {pct(tp, tp + fp)}",
            f"- bad rate among flagged = {pct(tp, tp + fp)} vs not flagged = {pct(fn, fn + tn)}"]

    # ---- themes
    themes = Counter(t for r in fb for t in (r.get("themes") or "").split(";") if t)
    out += ["", "## Comment themes (keyword coding)", "", "| theme | comments | example |", "|---|---|---|"]
    for t, n in themes.most_common():
        ex = next((r["comment"] for r in fb if t in (r.get("themes") or "")), "")
        out.append(f"| {t} | {n} | {ex[:90]} |")
    out += ["", "| theme | " + " | ".join(sorted(byr)) + " |", "|---" * (len(byr) + 1) + "|"]
    for t, _ in themes.most_common():
        out.append(f"| {t} | " + " | ".join(str(sum(1 for r in fb if r['region'] == reg and t in (r.get('themes') or ''))) for reg in sorted(byr)) + " |")

    # ---- optional clustering
    comments = [r["comment"] for r in fb if r.get("comment")]
    try:
        from sklearn.cluster import KMeans
        from sklearn.feature_extraction.text import TfidfVectorizer
        if len(comments) >= 12:
            k = min(6, len(comments) // 4)
            X = TfidfVectorizer(stop_words="english", min_df=2).fit_transform(comments)
            km = KMeans(n_clusters=k, n_init=10, random_state=6216).fit(X)
            out += ["", f"## Comment clusters (TF-IDF + k-means, k={k})", ""]
            for c in range(k):
                members = [comments[i] for i in range(len(comments)) if km.labels_[i] == c]
                out.append(f"- cluster {c + 1} ({len(members)}): " + " / ".join(m[:70] for m in members[:2]))
    except ImportError:
        out += ["", "(scikit-learn not installed: clustering skipped)"]

    (log.dir / "feedback_report.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
