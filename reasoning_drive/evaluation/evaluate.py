"""Metrics of one saved run, read from its results.jsonl: accuracy, precision, recall, F1 and confusion matrices.

Both tasks:
  marking task (one marked line or arrow per image)   Output 1 marking type, Output 2 the six actions
  lane task (my whole lane, one answer per image)      boundary colour and pattern per side, the seven actions

Actions are scored per (image, action) cell that the label decides. "prohibited" is the positive class: a missed
prohibition (false negative) is an unsafe error when the answer allows the action. Unsafe and over-cautious errors are
counted as in the run's own scores: unsafe = label prohibited, answer allowed; over-cautious = label allowed, answer
prohibited or not_determined. Contested rule-table cells are left out, as in the run's own scoring. With repeats, the majority
answer of each image counts (the same rule as the run's scores.json).

    python main.py evaluate <run_id>                 metrics of one run (written to results/reports/<run_id>.md)
    python main.py evaluate <run_A> <run_B>          two runs side by side, on the images both answered
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from .. import paths as P

DECIDED = ("allowed", "prohibited", "not_determined")
ANSWER_CLASSES = ["allowed", "prohibited", "not_determined", "not_applicable"]


def load_run_files(repo, run_id: str) -> tuple[dict, list[dict], dict]:
    d = P.runs_dir(repo) / run_id
    if not (d / "results.jsonl").exists():
        raise FileNotFoundError(f"No run {run_id} in {P.RUNS}/.")
    manifest = json.loads((d / "manifest.json").read_text(encoding="utf-8")) if (d / "manifest.json").exists() else {}
    records = [json.loads(line) for line in (d / "results.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    scores = json.loads((d / "scores.json").read_text(encoding="utf-8")) if (d / "scores.json").exists() else {}
    return manifest, records, scores


def per_image(records: list[dict]) -> dict:
    """One record per image: the one whose actions are the most common answer of the repeats."""
    by = defaultdict(list)
    for r in records:
        if r.get("answer") and isinstance(r["answer"].get("actions"), dict):
            by[r["image_id"]].append(r)
    out = {}
    for iid, rs in by.items():
        top = Counter(json.dumps(r["answer"]["actions"], sort_keys=True) for r in rs).most_common(1)[0][0]
        out[iid] = next(r for r in rs if json.dumps(r["answer"]["actions"], sort_keys=True) == top)
    return out


def confusion(pairs: list[tuple[str, str]], classes: list[str] | None = None) -> dict:
    classes = list(classes or sorted({a for a, _ in pairs} | {b for _, b in pairs}))
    for a, b in pairs:
        for c in (a, b):
            if c not in classes:
                classes.append(c)
    idx = {c: i for i, c in enumerate(classes)}
    m = [[0] * len(classes) for _ in classes]
    for a, b in pairs:
        m[idx[a]][idx[b]] += 1
    return {"classes": classes, "matrix": m, "rows": "label", "columns": "answer"}


def prf(pairs: list[tuple[str, str]], positive: str) -> dict:
    tp = sum(1 for a, b in pairs if a == positive and b == positive)
    fp = sum(1 for a, b in pairs if a != positive and b == positive)
    fn = sum(1 for a, b in pairs if a == positive and b != positive)
    p = tp / (tp + fp) if tp + fp else None
    r = tp / (tp + fn) if tp + fn else None
    f = 2 * p * r / (p + r) if p and r else (0.0 if p is not None and r is not None else None)
    rnd = lambda x: None if x is None else round(x, 3)  # noqa: E731
    return {"support": tp + fn, "tp": tp, "fp": fp, "fn": fn, "precision": rnd(p), "recall": rnd(r), "f1": rnd(f)}


def per_class(pairs: list[tuple[str, str]]) -> dict:
    classes = sorted({a for a, _ in pairs} | {b for _, b in pairs})
    out = {c: prf(pairs, c) for c in classes}
    supported = [v["f1"] or 0.0 for v in out.values() if v["support"]]
    acc = sum(1 for a, b in pairs if a == b) / len(pairs) if pairs else None
    return {"accuracy": None if acc is None else round(acc, 3), "n": len(pairs),
            "macro_f1": round(sum(supported) / len(supported), 3) if supported else None, "per_class": out}


def action_cells(recs: dict) -> list[dict]:
    """(image, action, label, answer) for every action cell the label decides, contested cells left out."""
    rows = []
    for iid, r in sorted(recs.items()):
        lab, ans = r.get("label") or {}, r["answer"].get("actions") or {}
        contested = set((r.get("score") or {}).get("contested") or {})
        for k, want in lab.items():
            if not k.startswith("act_"):
                continue
            a = k[4:]
            if want not in DECIDED or a in contested:
                continue
            rows.append({"image_id": iid, "action": a, "label": want, "answer": ans.get(a) or "missing"})
    return rows


def evaluate_run(repo, run_id: str) -> dict:
    manifest, records, scores = load_run_files(repo, run_id)
    task = manifest.get("task") or ("lane" if records and records[0].get("task") == "lane" else "marking")
    recs = per_image(records)
    cells = action_cells(recs)
    pairs = [(c["label"], c["answer"]) for c in cells]
    by_action = defaultdict(list)
    for c in cells:
        by_action[c["action"]].append((c["label"], c["answer"]))
    s = scores.get("summary") or {}
    out = {
        "run_id": run_id, "task": task, "test": manifest.get("test"), "region": manifest.get("region"),
        "prompt": (manifest.get("prompt_hashes") or {}).get("prompt_dir"), "model": (manifest.get("settings") or {}).get("model"),
        "split": manifest.get("split"), "mock": manifest.get("mock"), "images": len(recs), "repeats": manifest.get("repeats", 1),
        "actions": {
            "cells": len(pairs),
            "accuracy": round(sum(1 for a, b in pairs if a == b) / len(pairs), 3) if pairs else None,
            "prohibited": prf(pairs, "prohibited"),
            "allowed": prf(pairs, "allowed"),
            "confusion": confusion(pairs, list(ANSWER_CLASSES)),
            "prohibited_recall_by_action": {a: prf(v, "prohibited")["recall"] for a, v in sorted(by_action.items())},
            "unsafe": sum(1 for a, b in pairs if a == "prohibited" and b == "allowed"),
            "over_cautious": sum(1 for a, b in pairs if a == "allowed" and b in ("prohibited", "not_determined")),
        },
        "summary": {k: s.get(k) for k in ("output1", "output2", "lane", "lane_core", "both_boundaries", "unsafe_errors",
                                          "over_cautious_errors", "markings_precision", "markings_recall", "cost_usd") if k in s},
    }
    pa, pp = out["actions"]["allowed"]["f1"], out["actions"]["prohibited"]["f1"]
    out["actions"]["macro_f1"] = round((pa + pp) / 2, 3) if pa is not None and pp is not None else None
    if task == "lane":
        out["boundaries"] = {}
        for side in ("left", "right"):
            for attr in ("color", "pattern"):
                pr = [(str(r["label"].get(f"{side}_{attr}") or ""), str((r["answer"].get(f"{side}_boundary") or {}).get(attr) or "missing"))
                      for r in recs.values() if r["label"].get(f"{side}_{attr}")]
                out["boundaries"][f"{side}_{attr}"] = {**per_class(pr), "confusion": confusion(pr)}
        p, r = s.get("markings_precision"), s.get("markings_recall")
        out["markings"] = {"precision": p, "recall": r, "f1": round(2 * p * r / (p + r), 3) if p and r else None}
        out["subsets"] = lane_subsets(repo, recs, scores)
        if manifest.get("test") == "D":
            out["region_inference"] = region_inference(recs, manifest.get("region"))
        n_pass = [r["request"].get("passages") for r in recs.values() if (r.get("request") or {}).get("passages") is not None]
        if n_pass:
            out["passages_per_prompt"] = {"mean": round(sum(n_pass) / len(n_pass), 1), "min": min(n_pass), "max": max(n_pass)}
    else:
        o1 = [(x["score"].get("o1_label"), x["score"].get("o1_answer")) for x in (scores.get("per_image") or {}).values()
              if x.get("score") and x["score"].get("o1_label")]
        out["output1"] = {**per_class(o1), "confusion": confusion(o1)}
    return out


COUNTRY_WORDS = {"CN": ["china", "chinese", "中国"], "US": ["united states", "u.s.", "usa", "america"],
                 "UK": ["united kingdom", "britain", "british", "england", "u.k."], "JP": ["japan"], "IN": ["india"],
                 "SG": ["singapore"]}


def region_inference(recs: dict, region: str | None) -> dict:
    """Test D: which country the answer names in 'scene' (the user message did not say)."""
    said = Counter()
    for r in recs.values():
        text = str((r.get("answer") or {}).get("scene") or "").lower()
        hits = [c for c, ws in COUNTRY_WORDS.items() if any(w in text for w in ws)]
        said[hits[0] if len(hits) == 1 else ("several" if hits else "none")] += 1
    n = sum(said.values())
    return {"named": dict(said), "correct": said.get(region, 0), "n": n,
            "share_correct": round(said.get(region, 0) / n, 3) if n else None}


def lane_subsets(repo, recs: dict, scores: dict) -> dict:
    """Lane actions (every action the label decides) and unsafe errors per composition level and per rule sensitivity
    (difficulty.py), from the run's own per-image scores."""
    from .difficulty import _tables, describe
    tables = _tables(repo)
    per = scores.get("per_image") or {}
    groups: dict[str, dict] = {}
    for iid, x in per.items():
        sc = x.get("score") or {}
        lab = (recs.get(iid) or {}).get("label")
        if not lab or sc.get("output2") is None:
            continue
        d = describe(repo, (recs[iid].get("region") or ""), lab, tables)
        for key in (d["level"], "rule-sensitive" if d["rule_sensitive"] else "not rule-sensitive"):
            g = groups.setdefault(key, {"n": 0, "correct": 0, "unsafe": 0})
            g["n"] += 1
            g["correct"] += 1 if sc["output2"] else 0
            g["unsafe"] += len(sc.get("unsafe") or [])
    for g in groups.values():
        g["accuracy"] = round(g["correct"] / g["n"], 3) if g["n"] else None
    order = ["L1", "L2", "L3", "rule-sensitive", "not rule-sensitive"]
    return {k: groups[k] for k in order if k in groups}


def _fmt(x) -> str:
    return "–" if x is None else (f"{x:.3f}" if isinstance(x, float) else str(x))


def _matrix_md(cm: dict) -> list[str]:
    cls = cm["classes"]
    lines = ["| label \\ answer | " + " | ".join(cls) + " |", "|---|" + "---|" * len(cls)]
    lines += [f"| {c} | " + " | ".join(str(v) for v in row) + " |" for c, row in zip(cls, cm["matrix"])]
    return lines


def to_markdown(ev: dict) -> str:
    a = ev["actions"]
    L = [f"# {ev['run_id']}", "",
         f"{ev['task']} task · Test {ev['test']} · {ev['region']} · {ev['prompt']} · {ev['model']} · split {ev['split']} · "
         f"{ev['images']} images × {ev['repeats']}" + (" · mock" if ev.get("mock") else ""), "",
         "## Actions (cells the label decides, contested cells left out)", "",
         f"{a['cells']} cells, accuracy {_fmt(a['accuracy'])}, macro-F1 (allowed, prohibited) {_fmt(a['macro_f1'])}", "",
         "| class | support | precision | recall | F1 | TP | FP | FN |", "|---|---|---|---|---|---|---|---|"]
    for c in ("prohibited", "allowed"):
        v = a[c]
        L.append(f"| {c} | {v['support']} | {_fmt(v['precision'])} | {_fmt(v['recall'])} | {_fmt(v['f1'])} | {v['tp']} | {v['fp']} | {v['fn']} |")
    L += ["", f"Unsafe errors (label prohibited, answer allowed): {a['unsafe']}; over-cautious errors (label allowed, answer "
              f"prohibited or not_determined): {a['over_cautious']}", "",
          "Confusion matrix:", ""] + _matrix_md(a["confusion"])
    L += ["", "Recall of prohibited per action: " + ", ".join(f"{k} {_fmt(v)}" for k, v in a["prohibited_recall_by_action"].items())]
    if "output1" in ev:
        o = ev["output1"]
        L += ["", "## Output 1: marking type", "", f"accuracy {_fmt(o['accuracy'])} on {o['n']} images, macro-F1 {_fmt(o['macro_f1'])}", "",
              "| class | support | precision | recall | F1 |", "|---|---|---|---|---|"]
        L += [f"| {c} | {v['support']} | {_fmt(v['precision'])} | {_fmt(v['recall'])} | {_fmt(v['f1'])} |" for c, v in o["per_class"].items()]
        L += ["", "Confusion matrix:", ""] + _matrix_md(o["confusion"])
    if "boundaries" in ev:
        L += ["", "## Boundaries of my lane", "", "| attribute | images | accuracy | macro-F1 |", "|---|---|---|---|"]
        L += [f"| {k} | {v['n']} | {_fmt(v['accuracy'])} | {_fmt(v['macro_f1'])} |" for k, v in ev["boundaries"].items()]
        m = ev["markings"]
        L += ["", f"Lane markings (tokens): precision {_fmt(m['precision'])}, recall {_fmt(m['recall'])}, F1 {_fmt(m['f1'])}"]
        for k in ("left_pattern", "right_pattern"):
            L += ["", f"Confusion matrix, {k}:", ""] + _matrix_md(ev["boundaries"][k]["confusion"])
        if ev.get("subsets"):
            L += ["", "## Lane actions by composition level and rule sensitivity", "",
                  "| subset | images | lane actions correct | accuracy | unsafe errors |", "|---|---|---|---|---|"]
            L += [f"| {k} | {v['n']} | {v['correct']} | {_fmt(v['accuracy'])} | {v['unsafe']} |" for k, v in ev["subsets"].items()]
        if ev.get("region_inference"):
            ri = ev["region_inference"]
            L += ["", f"Country named in the answer (Test D, not given in the prompt): {ri['named']}; correct {ri['correct']}/{ri['n']}"]
        if ev.get("passages_per_prompt"):
            L += ["", f"Passages per prompt (Test R): {ev['passages_per_prompt']}"]
    return "\n".join(L) + "\n"


def write_report(repo, run_id: str) -> Path:
    ev = evaluate_run(repo, run_id)
    out = Path(repo) / P.REPORTS
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{run_id}.json").write_text(json.dumps(ev, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / f"{run_id}.md").write_text(to_markdown(ev), encoding="utf-8")
    return out / f"{run_id}.md"


def side_by_side(repo, run_a: str, run_b: str) -> str:
    ea, eb = evaluate_run(repo, run_a), evaluate_run(repo, run_b)
    rows = [("action cells", lambda e: e["actions"]["cells"]), ("action accuracy", lambda e: e["actions"]["accuracy"]),
            ("prohibited precision", lambda e: e["actions"]["prohibited"]["precision"]),
            ("prohibited recall", lambda e: e["actions"]["prohibited"]["recall"]),
            ("prohibited F1", lambda e: e["actions"]["prohibited"]["f1"]), ("unsafe errors", lambda e: e["actions"]["unsafe"]),
            ("over-cautious errors", lambda e: e["actions"]["over_cautious"]), ("actions macro-F1", lambda e: e["actions"]["macro_f1"])]
    for key in ("L1", "L2", "L3", "rule-sensitive", "not rule-sensitive"):
        if key in (ea.get("subsets") or {}) or key in (eb.get("subsets") or {}):
            rows.append((f"lane actions, {key}", lambda e, k=key: (lambda v: f"{v['correct']}/{v['n']}" if v else None)((e.get("subsets") or {}).get(k))))
    if "output1" in ea and "output1" in eb:
        rows += [("Output 1 accuracy", lambda e: e["output1"]["accuracy"]), ("Output 1 macro-F1", lambda e: e["output1"]["macro_f1"])]
    L = [f"| | {run_a} (Test {ea['test']}) | {run_b} (Test {eb['test']}) |", "|---|---|---|"]
    L += [f"| {name} | {_fmt(f(ea))} | {_fmt(f(eb))} |" for name, f in rows]
    return "\n".join(L) + "\n"
