"""Named experiments (configs/experiments.yaml): each variant is the settings (configs/experiment.yaml, configs/api.yaml)
with a few values changed.

python main.py experiment            list the experiments
python main.py experiment E2         table of E2 from the saved runs (no API calls)
python main.py experiment E2 --real  also runs the variants that have no saved run
python main.py experiment E5 --mock  the same with made-up answers (free; checks the pipeline)
An experiment with "task: lane" uses the lane-level task (reasoning_drive/lane.py) instead of the single-marking task.
"""
from __future__ import annotations

import copy
from pathlib import Path

from .. import config as C
from .. import paths as P

EXPERIMENTS_FILE = P.EXPERIMENTS_FILE
# short variant keys -> (YAML section, YAML key) of the settings
KEYS = {"use_rules": ("experiment", "use_rules"), "prompt": ("experiment", "prompt"), "repeats": ("experiment", "repeats"),
        "split": ("experiment", "split"), "region": ("experiment", "region"), "model": ("model", "name"),
        "reasoning_effort": ("model", "reasoning_effort"), "temperature": ("model", "temperature"),
        "reasoning_summary": ("model", "reasoning_summary"), "max_output_tokens": ("model", "max_output_tokens"),
        "lane_prompt": ("lane", "prompt"), "lane_max_output_tokens": ("lane", "max_output_tokens")}


def load_experiments(repo: Path) -> dict:
    p = Path(repo) / EXPERIMENTS_FILE
    if not p.exists():
        raise C.ConfigError(f"{p} is missing.")
    return C._yaml().safe_load(p.read_text(encoding="utf-8")) or {}


def variant_cfg(repo: Path, settings: dict) -> dict:
    """The settings of one variant: the settings files with the given short keys changed."""
    repo = Path(repo)
    y = C.read_settings(repo)
    y = copy.deepcopy(y)
    for k, v in settings.items():
        if k not in KEYS:
            raise C.ConfigError(f"Unknown variant setting \"{k}\" in {EXPERIMENTS_FILE}; known: {', '.join(KEYS)}.")
        sec, key = KEYS[k]
        y.setdefault(sec, {})[key] = v
    cfg = C.from_yaml(y)
    cfg["_repo"] = str(repo)
    C._load_env(repo)
    C.check(cfg)
    return cfg


def variants(exp: dict) -> list[tuple[str, dict, str | None]]:
    """(name, settings, reported run ID) for every variant; experiment-level settings apply to all variants."""
    common = exp.get("settings") or {}
    out = []
    for name, v in (exp.get("variants") or {}).items():
        v = dict(v or {})
        run = v.pop("run", None)
        src = v.pop("from", None)  # Test R: the variant whose Test A run chooses the passages
        out.append((str(name), {**common, **v, **({"_from": src} if src else {})}, run))
    return out


def resolve(repo: Path, exp: dict, real: bool = False, log=print, mock: bool = False) -> list[dict]:
    """Find the saved run of every variant (the reported one if it still exists, else a matching run);
    with real=True, run the variants that have none; with mock=True, use (or make) runs with made-up answers."""
    from ..agent.lane import find_lane_run, find_or_run_lane
    from .report import find_or_run, find_run
    from ..agent.runner import runs_dir
    lane = exp.get("task") == "lane"
    rows = []
    done_ids: dict[str, str] = {}
    for name, st, reported in variants(exp):
        src = st.pop("_from", None)
        cfg = variant_cfg(repo, st)
        test, region = cfg["run"]["test"], cfg["run"]["region"]
        split, reps = cfg["run"]["split"], int(cfg["run"]["repeats"])
        rid = reported if reported and not mock and (runs_dir(cfg) / reported / "scores.json").exists() else None
        if lane:
            ur = str(st.get("use_rules", "")).lower()
            test = {"other_region": "C", "c": "C", "no_country": "D", "d": "D", "retrieved": "R", "r": "R"}.get(ur, test)
            rid = rid or find_lane_run(cfg, test, region, split, mock=mock)
            if not rid and (real or mock):
                cfg["mock"] = mock
                rid = find_or_run_lane(cfg, test, region, split, mock=mock, log=log, stage1_run=done_ids.get(src) if src else None)
            if rid:
                done_ids[name] = rid
        else:
            rid = rid or find_run(cfg, test, region, split, reps, mock=mock)
            if not rid and (real or mock):
                cfg["mock"] = mock
                rid = find_or_run(cfg, test, region, split, reps, mock=mock, log=log)
        rows.append({"variant": name, "settings": {**st, **({"from": src} if src else {})}, "run_id": rid, "cfg": cfg})
    return rows


def table(repo: Path, name: str, real: bool = False, log=print, mock: bool = False) -> str:
    from .report import experiment_table, repeat_analysis, to_markdown
    from ..agent.runner import compare_runs
    exps = load_experiments(repo)
    if name not in exps:
        raise C.ConfigError(f"No experiment \"{name}\" in {EXPERIMENTS_FILE}; there are: {', '.join(k for k in exps if not k.startswith('_'))}.")
    exp = exps[name]
    rows = resolve(repo, exp, real, log, mock)
    if exp.get("task") == "lane":
        return _lane_table(name, exp, rows, mock)
    out = [f"## {name}", "", f"Question: {exp.get('question', '')}", f"Changed: {exp.get('changed', '')}",
           f"Held fixed: {exp.get('fixed', '')}", f"Judged by: {exp.get('judged', '')}", ""]
    missing = [r["variant"] for r in rows if not r["run_id"]]
    if missing:
        out += [f"No saved run for: {', '.join(missing)}. Run `python main.py experiment {name} --real` (calls the API).", ""]
    done = [r for r in rows if r["run_id"]]
    if done:
        cfg = done[0]["cfg"]
        df = experiment_table(cfg, [(r["variant"], r["run_id"], ", ".join(f"{k}={v}" for k, v in r["settings"].items())) for r in done])
        out += [to_markdown(df), ""]
        if exp.get("analysis") == "repeats":
            out += ["Single request (repeat 1 only) against the majority of the repeats:", "",
                    "| Variant | Output 2, majority | Output 2, single request | Unsafe, majority | Unsafe, single | Images where they differ |",
                    "|---|---|---|---|---|---|"]
            for r in done:
                a = repeat_analysis(cfg, r["run_id"])
                out.append(f"| {r['variant']} | {a['majority_o2']} | {a['single_o2']} | {a['majority_unsafe']} | {a['single_unsafe']} | {a['differ_o2']} |")
            out.append("")
        by = {r["variant"]: r["run_id"] for r in done}
        for a, b in exp.get("compare") or []:
            if a in by and b in by:
                c = compare_runs(cfg, by[a], by[b])
                for k in ("output1", "output2"):
                    d = c[k]
                    out.append(f"* {a} vs {b}, {k}: only {a} right {d['only_A_right']}, only {b} right {d['only_B_right']}, "
                               f"exact McNemar p = {d['p_value']}")
        out.append("")
    return "\n".join(out)


def _lane_table(name: str, exp: dict, rows: list[dict], mock: bool) -> str:
    from ..agent.lane import compare_lane_runs, lane_table_markdown
    out = [f"## {name}" + (" (MOCK ANSWERS: checks the pipeline, says nothing about the model)" if mock else ""), "",
           f"Question: {exp.get('question', '')}", f"Changed: {exp.get('changed', '')}", f"Held fixed: {exp.get('fixed', '')}",
           f"Judged by: {exp.get('judged', '')}", ""]
    missing = [r["variant"] for r in rows if not r["run_id"]]
    if missing:
        out += [f"No saved run for: {', '.join(missing)}. It needs final lane labels; then run "
                f"`python main.py experiment {name} --real` (calls the API) or `--mock` (free).", ""]
    done = [r for r in rows if r["run_id"]]
    if done:
        cfg = done[0]["cfg"]
        out += [lane_table_markdown(cfg, [(r["variant"], r["run_id"], ", ".join(f"{k}={v}" for k, v in r["settings"].items())) for r in done]), ""]
        by = {r["variant"]: r["run_id"] for r in done}
        for a, b in exp.get("compare") or []:
            if a in by and b in by:
                c = compare_lane_runs(cfg, by[a], by[b])
                for k in ("lane", "lane_core", "output2", "both_boundaries", "markings", "no_unsafe"):
                    d = c[k]
                    ci = d.get("ci95") or [None, None]
                    diff = f", difference {d['diff']:+.3f} (95% CI {ci[0]:+.3f} to {ci[1]:+.3f})" if d.get("diff") is not None else ""
                    out.append(f"* {a} vs {b}, {k}: only {a} right {d['only_A_right']}, only {b} right {d['only_B_right']}, "
                               f"exact McNemar p = {d['p_value']}{diff}")
                out.append(f"* {a} vs {b}, unsafe errors: {a} {c['unsafe_errors']['A']}, {b} {c['unsafe_errors']['B']}")
        out.append("")
    return "\n".join(out)


def listing(repo: Path) -> str:
    exps = load_experiments(repo)
    return "\n".join(f"{k:22s} {v.get('question', '')}" for k, v in exps.items() if not str(k).startswith("_"))
