"""results/index.csv: one line per saved run (model runs in results/runs/, simulation runs in results/carla/), so every
result can be found again without opening the folders.

    python main.py results              print the table (and write results/index.csv)
    python main.py results --kind lane  only the lane-task runs
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

from .. import paths as P

COLUMNS = ["run_id", "kind", "date", "test", "region", "prompt", "model", "reasoning_effort", "split", "images", "repeats", "mock",
           "main_metric", "unsafe", "cost_usd", "experiments", "folder"]


def _experiments_by_run(repo) -> dict:
    f = Path(repo) / P.EXPERIMENTS_FILE
    out: dict[str, list[str]] = {}
    if not f.exists():
        return out
    for name, exp in (P.read_yaml(f) or {}).items():
        if name.startswith("_") or not isinstance(exp, dict):
            continue
        for vname, v in (exp.get("variants") or {}).items():
            if isinstance(v, dict) and v.get("run"):
                out.setdefault(v["run"], []).append(f"{name}:{vname}")
    return out


def _date(run_id: str) -> str:
    d = run_id.split("_")[0]
    return f"{d[:4]}-{d[4:6]}-{d[6:8]}" if len(d) == 8 and d.isdigit() else ""


def model_runs(repo) -> list[dict]:
    rows, exps = [], _experiments_by_run(repo)
    root = P.runs_dir(repo)
    for m in sorted(list(root.glob("*/manifest.json")) + list(root.glob("archive/*/manifest.json"))):
        d = m.parent
        man = json.loads(m.read_text(encoding="utf-8"))
        s = (json.loads((d / "scores.json").read_text(encoding="utf-8")).get("summary") or {}) if (d / "scores.json").exists() else {}
        task = man.get("task") or "marking"
        if task == "lane":
            lane = s.get("lane") or {}
            metric = f"lane actions {(s.get('output2') or {}).get('correct')}/{(s.get('output2') or {}).get('n')}; lane identified {lane.get('correct')}/{lane.get('n')}"
        else:
            o1, o2 = s.get("output1") or {}, s.get("output2") or {}
            metric = f"Output 1 {o1.get('correct')}/{o1.get('n')}; Output 2 {o2.get('correct')}/{o2.get('n')}"
        st = man.get("settings") or {}
        rows.append({"run_id": d.name, "kind": task, "date": _date(d.name), "test": man.get("test", ""), "region": man.get("region", ""),
                     "prompt": (man.get("prompt_hashes") or {}).get("prompt_dir", ""), "model": st.get("model", ""),
                     "reasoning_effort": st.get("reasoning_effort", ""), "split": man.get("split", ""), "images": man.get("n_items", ""),
                     "repeats": man.get("repeats", ""), "mock": man.get("mock", ""), "main_metric": metric,
                     "unsafe": s.get("unsafe_errors", ""), "cost_usd": s.get("cost_usd", ""),
                     "experiments": " ".join(exps.get(d.name, [])), "folder": d.relative_to(Path(repo)).as_posix()})
    return rows


def carla_runs(repo) -> list[dict]:
    rows = []
    root = Path(repo) / P.CARLA_RESULTS
    for f in sorted(root.glob("*/summary.json")):
        d = f.parent
        s = json.loads(f.read_text(encoding="utf-8"))
        meta = s.get("meta") or {}
        if "per_experiment" in s:
            kind = "carla_route"
            pe = s["per_experiment"]
            metric = "; ".join(f"{k}: Output 2 {v.get('output2_correct')}/{v.get('output2_scored')}" for k, v in pe.items())
            unsafe = " ".join(f"{k}:{v.get('unsafe')}" for k, v in pe.items())
            tests = ",".join(pe)
        elif "per_ask" in s:
            kind = "carla_suite"
            pa = s["per_ask"]
            metric = "; ".join(f"{k}: actions {v.get('actions_correct')}/{v.get('actions_checked')}" for k, v in pa.items())
            unsafe = " ".join(f"{k}:{v.get('unsafe')}" for k, v in pa.items())
            tests = ",".join(pa)
        else:
            kind = "carla_loop" if "a_vs_b_cross_line" in s else "carla_scenario"
            pt = s.get("per_test") or {}
            metric = "; ".join(f"{k}: answered {v.get('answered')}/{v.get('requests')}" for k, v in pt.items())
            unsafe = " ".join(f"{k}:{v.get('unsafe', sum((b.get('unsafe') or 0) for b in (v.get('by_kind') or {}).values()))}" for k, v in pt.items())
            tests = ",".join(pt)
        cost = s.get("cost_usd")
        if cost is None:
            cost = round(sum((v.get("cost_usd") or 0) for v in (s.get("per_test") or {}).values()), 4)
        rows.append({"run_id": d.name, "kind": kind, "date": _date(d.name), "test": tests, "region": meta.get("region", ""),
                     "prompt": meta.get("prompt", ""), "model": meta.get("model", ""), "reasoning_effort": meta.get("reasoning_effort", ""),
                     "split": meta.get("map", ""), "images": "", "repeats": "", "mock": meta.get("mock", s.get("mock", "")),
                     "main_metric": metric, "unsafe": unsafe, "cost_usd": cost, "experiments": meta.get("route", meta.get("scenario", "")),
                     "folder": d.relative_to(Path(repo)).as_posix()})
    return rows


def build_index(repo) -> list[dict]:
    rows = model_runs(repo) + carla_runs(repo)
    rows.sort(key=lambda r: r["run_id"])
    out = Path(repo) / P.RESULTS_INDEX
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    return rows


def table(rows: list[dict]) -> str:
    cols = ["run_id", "kind", "test", "region", "prompt", "model", "images", "main_metric", "unsafe", "cost_usd"]
    width = {c: max(len(c), *(len(str(r[c])) for r in rows)) if rows else len(c) for c in cols}
    width["main_metric"] = min(width["main_metric"], 70)
    line = lambda r: "  ".join(str(r[c])[:width[c]].ljust(width[c]) for c in cols)  # noqa: E731
    return "\n".join([line({c: c for c in cols})] + [line(r) for r in rows])
