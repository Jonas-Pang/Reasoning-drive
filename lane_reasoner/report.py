"""Analysis for the model exploration notebook (Milestone 4): data audit, reuse of finished runs, metrics,
error cases with image crops, configuration record and the experiment table.

Everything here reads the saved runs (runs/<run_id>/); nothing calls the API except find_or_run when no
matching finished run exists.
"""
from __future__ import annotations

import json
import math
import textwrap
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

import cv2
import numpy as np

from . import config as C
from .client import settings_of
from .data import allowed_collections, boxed_jpeg, load_items, workspaces
from .prompts import passages, prompt_parts
from .runner import _label_hashes, list_runs, load_run, run_batch, split_version
from .scoring import ACTIONS

BOX_KEYS = ("bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2")
NOT_SHOWN = {"culane"}  # collections whose images must not appear in a public notebook


# ---------------------------------------------------------------- data

def all_label_rows(cfg: dict) -> list[dict]:
    """Every label row of every workspace, whatever its status."""
    from video_tool.core import LabelStore, list_trip_ids
    rows = []
    for p in workspaces(cfg):
        for tid in list_trip_ids(p):
            for r in LabelStore(p.labels_csv(tid)).all():
                rows.append({**r, "collection": p.collection, "trip": tid,
                             "_file": str(p.data / r["source_path"]) if r.get("source_path") else ""})
    return rows


def data_audit(cfg: dict) -> dict:
    """Which label rows the runs use, which are dropped and why, and what the label checker reports for the rest.

    Nothing is filled in: a row is either used as it is or dropped, and empty fields that carry meaning
    (arrow_type of a line, accepted_rule_ids of a crosswalk, not_applicable actions) are left unchanged."""
    from video_tool.core import derive_evidence, load_action_rules, validate_label
    repo = C.repo_of(cfg)
    schema = json.loads((repo / "config" / "label_schema.json").read_text(encoding="utf-8"))
    table = load_action_rules(SimpleNamespace(repo=repo))
    rule_ids = {code: {p["rule_id"] for p in passages(cfg, code)} for code in cfg["regions"]}
    used, dropped, issues = [], Counter(), []
    allowed = allowed_collections(cfg)
    for r in all_label_rows(cfg):
        if r.get("label_status") != "done":
            dropped[f"not final yet ({r.get('label_status') or 'empty'})"] += 1
            continue
        if r.get("region") not in cfg["regions"]:
            dropped[f"region {r.get('region')!r} not configured"] += 1
            continue
        try:
            [int(float(r[k])) for k in BOX_KEYS]
        except (TypeError, ValueError, KeyError):
            dropped["no target box"] += 1
            continue
        if not r["_file"] or not Path(r["_file"]).exists():
            dropped["image file missing"] += 1
            continue
        if allowed is not None and r["collection"] not in allowed:
            dropped[f"{r['collection']}: no permission yet to send its images to the API"] += 1
            continue
        errs, warns = validate_label(r, schema, rule_ids[r["region"]], table)
        ev = derive_evidence(r.get("visibility", ""), r.get("behavior_decidable", ""))
        if ev and r.get("expected_evidence") and ev != r["expected_evidence"]:
            warns.append(f"expected_evidence is {r['expected_evidence']} but visibility gives {ev}")
        issues += [(r["image_id"], "error", e) for e in errs] + [(r["image_id"], "warning", w) for w in warns]
        used.append(r)
    return {"used": used, "dropped": dict(dropped), "issues": issues}


# ---------------------------------------------------------------- runs

def find_run(cfg: dict, test: str, region: str, split: str, repeats: int, mock: bool | None = None) -> str | None:
    """The newest finished run with exactly these settings, prompt, images, labels and repeats, without errors."""
    mock = cfg.get("mock", False) if mock is None else mock
    items = load_items(cfg, region, split, [])
    ids = sorted(it.image_id for it in items)
    labels = _label_hashes(items)
    parts = prompt_parts(cfg, test, region)
    want = settings_of(cfg)
    for r in list_runs(cfg):
        if not r["finished"] or r["test"] != test or r["region"] != region or r["mock"] != mock or r["repeats"] != repeats or r["errors"]:
            continue
        m = load_run(cfg, r["run_id"])["manifest"]
        same_prompt = all(m["prompt_hashes"].get(k) == parts["hashes"][k] for k in ("instructions", "user_text", "schema"))
        if m["settings"] == want and same_prompt and sorted(m["items"]) == ids and m.get("label_sets") == labels:
            return r["run_id"]
    return None


def find_or_run(cfg: dict, test: str, region: str, split: str, repeats: int = 1, mock: bool | None = None, log=print) -> str:
    """Reuse a matching finished run (so re-running the notebook costs nothing), otherwise run it.

    Stops with the first error if any request failed; answers that did arrive are cached, so running again
    only pays for the failed ones."""
    mock = cfg.get("mock", False) if mock is None else mock
    rid = find_run(cfg, test, region, split, repeats, mock)
    if rid:
        log(f"Test {test}: reusing run {rid} (same settings, prompt, images, labels and repeats).")
        return rid
    log(f"Test {test}: no matching finished run, running it now ({'mock answers' if mock else 'real API calls'}) ...")
    rid = run_batch(cfg, test, region, 0, repeats, split, mock, log=log)
    run = load_run(cfg, rid)
    bad = [r["error"] for r in run["records"] if r.get("error")]
    if bad:
        raise RuntimeError(f"{len(bad)} of {len(run['records'])} requests of run {rid} failed. First error: {bad[0]}\n"
                           "Fix the cause and run the cell again: answers that arrived are cached and not paid again.")
    return rid


def config_record(cfg: dict, run_id: str) -> dict:
    """The configuration of one run, as recorded in its manifest (Milestone 4, section 3)."""
    run = load_run(cfg, run_id)
    m, recs = run["manifest"], run["records"]
    returned = sorted({(r.get("response") or {}).get("model") or "" for r in recs} - {""})
    st, ph = m["settings"], m["prompt_hashes"]
    return {
        "run_id": run_id, "date (UTC)": m["created_utc"], "test": f"{m['test']} ({C.TESTS[m['test']]})",
        "model requested": st["model"], "model returned by the API": ", ".join(returned) or "—",
        "API": f"{st['base_url']}/responses (OpenAI Responses API)", "reasoning_effort": st.get("reasoning_effort"),
        "temperature": "not sent (the model does not accept it)" if st.get("temperature") is None else st["temperature"],
        "image_detail": st.get("image_detail"), "max_output_tokens": st.get("max_output_tokens"),
        "instruction role": st.get("instruction_role"), "store": st.get("store"),
        "prompt": f"{ph['prompt_dir']} · instructions {ph['instructions']} · shared parts {ph['shared_parts']} · rules file {ph['rules_file']}",
        "examples in prompt": "none (zero-shot)",
        "dataset version": ", ".join(f"{k} {v}" for k, v in m["label_sets"].items()) + f" · split v{m.get('split_version', 1)}",
        "region / split": f"{m['region']} / {m.get('split', 'any')}", "images × repeats": f"{m['n_items']} × {m['repeats']}",
        "order seed": m["config"]["run"].get("order_seed"),
        "sampling seed": "none (the API offers no seed and the model takes no temperature; variation is measured with repeats)",
        "code": f"{m['tool']} · Git commit {m['git_commit'] or '—'}", "mock": m["mock"],
    }


def _pct(a, b):
    return round(a / b, 3) if b else None


def metrics(cfg: dict, run_id: str) -> dict:
    """Every number the notebook reports for one run."""
    run = load_run(cfg, run_id)
    m, s, per = run["manifest"], run["scores"]["summary"], run["scores"]["per_image"]
    if not per:
        raise ValueError(f"Run {run_id} has no scored answer (errors: {s.get('errors')}). Look at runs/{run_id}/results.jsonl.")
    pairs = [(x["score"]["o1_label"], x["score"]["o1_answer"]) for x in per.values()]
    classes = sorted({a for a, _ in pairs} | {b for _, b in pairs})
    prf = {}
    for c in classes:
        tp = sum(1 for a, b in pairs if a == c and b == c)
        fp = sum(1 for a, b in pairs if a != c and b == c)
        fn = sum(1 for a, b in pairs if a == c and b != c)
        p, r = (tp / (tp + fp) if tp + fp else None), (tp / (tp + fn) if tp + fn else None)
        f = (2 * p * r / (p + r) if p and r else 0.0) if (p is not None and r is not None) else (0.0 if tp + fn else None)
        prf[c] = {"support": tp + fn, "precision": p, "recall": r, "f1": f}
    supported = [v["f1"] or 0.0 for v in prf.values() if v["support"]]
    lat = sorted(r["response"]["latency_s"] for r in run["records"]
                 if r.get("response") and not r.get("cached") and not r.get("mock") and r["response"].get("latency_s"))
    q = lambda p: lat[min(len(lat) - 1, math.ceil(p * len(lat)) - 1)] if lat else None  # noqa: E731
    confident = sum(1 for x in per.values() if x["score"]["evidence_group"] == "wrong"
                    and next((r["answer"]["evidence"] for r in run["records"] if r["image_id"] == x["image_id"] and r.get("answer")), "") == "full")
    stable = [x for x in per.values() if "stable_o1" in x]
    n_req = s.get("requests", 0)
    return {
        "images": m["n_items"], "repeats": m["repeats"], "requests": n_req,
        "readable": _pct(s["readable"]["n"], s["readable"]["of"]), "errors": s.get("errors", 0),
        "output1_acc": s["output1"]["acc"], "output1_n": s["output1"]["n"],
        "output1_macro_f1": round(sum(supported) / len(supported), 3) if supported else None, "output1_per_class": prf,
        "output2_acc": s["output2"]["acc"], "output2_correct": s["output2"]["correct"], "output2_n": s["output2"]["n"],
        "actions": s.get("actions", {}), "contested": s.get("contested", {}),
        "unsafe_errors": s.get("unsafe_errors", 0), "over_cautious_errors": s.get("over_cautious_errors", 0),
        "contested_unsafe_errors": s.get("contested_unsafe_errors", 0), "contested_over_cautious_errors": s.get("contested_over_cautious_errors", 0),
        "evidence_groups": s.get("evidence_groups", {}), "confidently_wrong": confident, "citations": s.get("citations", {}),
        "inconsistent_answers": s.get("inconsistent_answers"),
        "unsupported_citations": sum(v for k, v in s.get("citations", {}).items() if k in ("unlisted", "in_pack_not_accepted")),
        "same_answer_all_repeats": _pct(sum(1 for x in stable if x["stable_o1"] and x["stable_o2"]), len(stable)) if m["repeats"] > 1 else None,
        "latency_mean_s": round(sum(lat) / len(lat), 2) if lat else None, "latency_p50_s": q(0.5), "latency_p95_s": q(0.95),
        "wall_time_s": s.get("elapsed_s"), "input_tokens": s.get("usage", {}).get("input_tokens", 0),
        "output_tokens": s.get("usage", {}).get("output_tokens", 0), "cost_usd": s.get("cost_usd", 0),
        "cost_per_request_usd": round(s.get("cost_usd", 0) / max(1, n_req - s.get("cached", 0)), 5), "cached": s.get("cached", 0),
    }


def confusion(cfg: dict, run_id: str):
    import pandas as pd
    per = load_run(cfg, run_id)["scores"]["per_image"].values()
    df = pd.DataFrame([{"label": x["score"]["o1_label"], "answer": x["score"]["o1_answer"]} for x in per])
    return pd.crosstab(df["label"], df["answer"])


def action_confusion(cfg: dict, run_id: str, include_contested: bool = False):
    """Output 2 as a classification: one row per (image, action) that the label decides (label not
    not_applicable), using the majority answer of the repeats. Returns (confusion table, rows)."""
    import pandas as pd
    from .scoring import majority
    run = load_run(cfg, run_id)
    per = run["scores"]["per_image"]
    rows = []
    for iid, m in majority(run["records"]).items():
        rec = m["actions_record"]
        contested = set((per.get(iid) or {}).get("score", {}).get("contested", {}))
        for a in ACTIONS:
            want = rec["label"].get("act_" + a, "")
            if want in ("", "not_applicable") or (a in contested and not include_contested):
                continue
            rows.append({"image_id": iid, "action": a, "label": want, "answer": rec["answer"]["actions"].get(a, "")})
    df = pd.DataFrame(rows, columns=["image_id", "action", "label", "answer"])
    return pd.crosstab(df["label"], df["answer"]) if len(df) else df, df


def class_prf(rows, positive: str = "prohibited") -> dict:
    """Precision, recall and F1 of one answer class over the action rows of action_confusion.

    For "prohibited": a missed prohibition (false negative) is an unsafe error, a prohibition the label does
    not have (false positive) is an over-cautious one."""
    lab, ans = rows["label"] == positive, rows["answer"] == positive
    tp, fp, fn = int((lab & ans).sum()), int((~lab & ans).sum()), int((lab & ~ans).sum())
    p = tp / (tp + fp) if tp + fp else None
    r = tp / (tp + fn) if tp + fn else None
    f = 2 * p * r / (p + r) if p and r else (0.0 if p is not None and r is not None else None)
    return {"support (label)": tp + fn, "true positives": tp, "false positives": fp, "false negatives": fn,
            "precision": None if p is None else round(p, 3), "recall": None if r is None else round(r, 3), "f1": None if f is None else round(f, 3)}


def error_cases(cfg: dict, run_id: str, include_contested: bool = True) -> list[dict]:
    """Images where the (majority) answer is wrong somewhere, with what differs and the model's own words."""
    from .scoring import majority
    run = load_run(cfg, run_id)
    maj = majority(run["records"])  # the answers the scores are based on: majority marking, majority actions
    out = []
    for iid, x in run["scores"]["per_image"].items():
        sc = x["score"]
        rec, act = maj[iid]["record"], maj[iid]["actions_record"]
        L, A = rec["label"], dict(act["answer"], marking=rec["answer"]["marking"], evidence=rec["answer"].get("evidence"))
        kinds = []
        if not sc["output1"]:
            kinds.append("output 1")
        if sc["output2"] is False:
            kinds.append("output 2")
        if sc["unsafe"]:
            kinds.append("unsafe")
        if include_contested and False in sc["contested"].values():
            kinds.append("contested cell")
        if sc["citation"] not in (None, "accepted", "none_needed"):
            kinds.append(f"citation: {sc['citation']}")
        if sc.get("consistency"):
            kinds.append("inconsistent: " + "; ".join(sc["consistency"]))
        if sc["evidence_group"] not in ("correct",) and "output 1" not in kinds and "output 2" not in kinds:
            kinds.append(f"evidence: {sc['evidence_group']}")
        if not kinds:
            continue
        diffs = {a: (L.get("act_" + a), A["actions"].get(a)) for a in ACTIONS if L.get("act_" + a) != A["actions"].get(a)}
        n = maj[iid]["n"]
        out.append({"image_id": iid, "region": rec["region"], "test": rec["test"], "kinds": kinds,
                    "label": sc["o1_label"], "answer": sc["o1_answer"], "evidence": A.get("evidence"),
                    "action_diffs": diffs, "cited": A.get("cited_rule_id"),
                    "reasoning": (rec["answer"].get("reasoning", "") if not sc["output1"] else act["answer"].get("reasoning", ""))
                                 + ("" if x.get("stable_o2", True) and x.get("stable_o1", True) else f" [answers differ across the {n} repeats]"),
                    "description": A.get("description", "")})
    return sorted(out, key=lambda c: (-("unsafe" in c["kinds"]), c["image_id"]))


def paired_differences(cfg: dict, run_a: str, run_b: str):
    """Images where Test A and Test B answer differently, and which one matches the label."""
    import pandas as pd
    pa, pb = load_run(cfg, run_a)["scores"]["per_image"], load_run(cfg, run_b)["scores"]["per_image"]
    ra = {r["image_id"]: r for r in load_run(cfg, run_a)["records"] if r.get("answer")}
    rb = {r["image_id"]: r for r in load_run(cfg, run_b)["records"] if r.get("answer")}
    rows = []
    for iid in sorted(set(pa) & set(pb)):
        a, b = ra[iid]["answer"], rb[iid]["answer"]
        diff = {k: (a["actions"].get(k), b["actions"].get(k)) for k in ACTIONS if a["actions"].get(k) != b["actions"].get(k)}
        if a["marking"] != b["marking"]:
            diff["marking"] = (pa[iid]["score"]["o1_answer"], pb[iid]["score"]["o1_answer"])
        if not diff:
            continue
        L = ra[iid]["label"]
        rows.append({"image": iid, "label": pa[iid]["score"]["o1_label"],
                     "differences (A → B)": "; ".join(f"{k}: {x} → {y}" + (f" (label {L.get('act_' + k)})" if k in ACTIONS else "")
                                                     for k, (x, y) in diff.items()),
                     "A output 2": pa[iid]["score"]["output2"], "B output 2": pb[iid]["score"]["output2"],
                     "A unsafe": ", ".join(pa[iid]["score"]["unsafe"]), "B unsafe": ", ".join(pb[iid]["score"]["unsafe"]),
                     "B cited": b.get("cited_rule_id")})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- pictures

def crop(cfg: dict, image_id: str, region: str, width: int = 420, context: float = 0.8) -> np.ndarray:
    """The image as the model saw it (cyan box), cropped to the box plus some road around it, as RGB.

    The crop keeps the notebook readable and shows little beyond the road surface (privacy of the own videos)."""
    it = next(i for i in load_items(cfg, region, "any", []) if i.image_id == image_id)
    if it.collection in NOT_SHOWN:  # e.g. CULane: the licence forbids redistribution, and notebooks are public
        ph = np.full((int(width * 0.5), width, 3), 40, np.uint8)
        cv2.putText(ph, f"{it.collection} image not shown", (12, int(width * 0.25)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (220, 220, 220), 1)
        cv2.putText(ph, "(licence: no redistribution)", (12, int(width * 0.25) + 26), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (180, 180, 180), 1)
        return ph
    img = cv2.imdecode(np.frombuffer(boxed_jpeg(it, cfg), np.uint8), cv2.IMREAD_COLOR)
    h, w = img.shape[:2]
    x1, y1, x2, y2 = it.box
    bw, bh = x2 - x1, y2 - y1
    pad_x, pad_y = int(bw * context) + 40, int(bh * context) + 40
    x1, y1, x2, y2 = max(0, x1 - pad_x), max(0, y1 - pad_y), min(w, x2 + pad_x), min(h, y2 + pad_y)
    c = img[y1:y2, x1:x2]
    c = cv2.resize(c, (width, max(1, int(c.shape[0] * width / c.shape[1]))), interpolation=cv2.INTER_AREA)
    return cv2.cvtColor(c, cv2.COLOR_BGR2RGB)


def show_cases(cfg: dict, cases: list[dict], cols: int = 2, width: int = 420):
    """A grid of error cases: crop on top, label vs answer and the model's reasoning below."""
    import matplotlib.pyplot as plt
    if not cases:
        print("No error cases.")
        return None
    rows = math.ceil(len(cases) / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(6.2 * cols, 5.6 * rows))
    axes = np.atleast_1d(axes).ravel()
    for ax, c in zip(axes, cases):
        ax.imshow(crop(cfg, c["image_id"], c["region"], width))
        ax.set_axis_off()
        diffs = "; ".join(f"{k}: label {v[0]} / answer {v[1]}" for k, v in c["action_diffs"].items())
        text = (f"{c['image_id'][-14:]} · Test {c['test']} · {', '.join(c['kinds'])}\n"
                f"label {c['label']} · answer {c['answer']} · evidence {c['evidence']}"
                + (f" · cited {c['cited']}" if c["test"] == "B" else "") + "\n"
                + textwrap.fill(diffs, 70) + "\n" + textwrap.fill("Reasoning: " + c["reasoning"], 70))
        ax.set_title(text, fontsize=8.5, loc="left")
    for ax in axes[len(cases):]:
        ax.set_axis_off()
    fig.tight_layout()
    return fig


def plot_comparison(named: dict):
    """Bar charts: headline metrics and per-action accuracy for each run. named = {"Test A": metrics, ...}."""
    import matplotlib.pyplot as plt
    names = list(named)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4.2))
    keys = [("output1_acc", "Output 1\naccuracy"), ("output1_macro_f1", "Output 1\nmacro-F1"), ("output2_acc", "Output 2\nexact match"),
            ("readable", "Readable\nanswers")]
    x = np.arange(len(keys))
    wbar = 0.8 / len(names)
    for i, n in enumerate(names):
        vals = [named[n].get(k) or 0 for k, _ in keys]
        bars = ax1.bar(x + i * wbar, vals, wbar, label=n)
        ax1.bar_label(bars, labels=[f"{v:.0%}" for v in vals], fontsize=8)
    ax1.set_xticks(x + wbar * (len(names) - 1) / 2, [k[1] for k in keys])
    ax1.set_ylim(0, 1.25)
    ax1.set_title("Headline metrics")
    ax1.legend(loc="upper left", ncol=len(names), fontsize=8)
    acts = [a for a in ACTIONS if any(a in named[n]["actions"] for n in names)]
    x2 = np.arange(len(acts))
    for i, n in enumerate(names):
        vals = [(named[n]["actions"].get(a, {}).get("correct", 0) / named[n]["actions"][a]["n"]) if a in named[n]["actions"] else 0 for a in acts]
        bars = ax2.bar(x2 + i * wbar, vals, wbar, label=n)
        ax2.bar_label(bars, labels=[f"{named[n]['actions'][a]['correct']}/{named[n]['actions'][a]['n']}" if a in named[n]["actions"] else ""
                                    for a in acts], fontsize=7)
    ax2.set_xticks(x2 + wbar * (len(names) - 1) / 2, [a.replace("_", "\n") for a in acts], fontsize=8)
    ax2.set_ylim(0, 1.15)
    ax2.set_title("Per-action accuracy (actions the label decides, contested cells excluded)")
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------- experiment table

def experiment_table(cfg: dict, rows: list[tuple[str, str, str]]):
    """rows = [(name, run_id, change)]. One line per finished run, for the submission."""
    import pandas as pd
    out = []
    for name, rid, change in rows:
        mm, rec = metrics(cfg, rid), config_record(cfg, rid)
        out.append({
            "Run": name, "run_id": rid,
            "Configuration": f"{rec['model requested']} · effort {rec['reasoning_effort']} · {rec['test']} · {Path(rec['prompt'].split(' · ')[0]).name}",
            "Change": change, "Images × repeats": rec["images × repeats"],
            "Output 1 acc.": mm["output1_acc"], "Output 1 macro-F1": mm["output1_macro_f1"],
            "Output 2 exact match": f"{mm['output2_correct']}/{mm['output2_n']} ({mm['output2_acc']:.1%})" if mm["output2_n"] else "—",
            "Unsafe errors": mm["unsafe_errors"], "Inconsistent answers": mm["inconsistent_answers"], "Readable": mm["readable"],
            "Same answer in all repeats": mm["same_answer_all_repeats"],
            "Mean / p95 latency (s)": f"{mm['latency_mean_s']} / {mm['latency_p95_s']}", "Wall time (s)": mm["wall_time_s"],
            "Cost (USD)": mm["cost_usd"],
        })
    return pd.DataFrame(out)


def to_markdown(df) -> str:
    """A pandas table as Markdown (no extra package needed)."""
    cols = list(df.columns)
    fmt = lambda v: "" if v is None or (isinstance(v, float) and math.isnan(v)) else str(v)  # noqa: E731
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    lines += ["| " + " | ".join(fmt(v).replace("|", "/") for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join(lines)


def check_separation(cfg: dict, region: str, split: str, run_ids: list[str]) -> dict:
    """Milestone 3, 6.5: the runs use only images of the chosen split, and no clip is on both sides."""
    from collections import defaultdict
    sides = defaultdict(set)
    for r in all_label_rows(cfg):
        if r.get("label_status") == "done":
            sides[(r["collection"], r.get("clip_id") or r["image_id"])].add(r.get("split"))
    mixed = [k for k, v in sides.items() if len(v) > 1]
    want = {it.image_id for it in load_items(cfg, region, split, [])}
    used = set()
    for rid in run_ids:
        used |= set(load_run(cfg, rid)["manifest"]["items"])
    return {"runs use only this split": used <= want, "images used": len(used),
            "clips on both sides of the split": mixed, "split version": split_version(cfg)}
