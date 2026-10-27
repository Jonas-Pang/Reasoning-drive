"""Run Test A / Test B on the labeled images and keep a complete record (Milestone 3, sections 2.4 and 6.6).

  runs/<run_id>/manifest.json   settings (no key), prompt and rule-file hashes, label-file hashes, Git commit, items
  runs/<run_id>/results.jsonl   one line per image and repeat: request settings, raw answer, parsed answer, score
  runs/<run_id>/scores.json     summary per output, actions, evidence groups, citations, tokens, cost, time
  runs/<run_id>/summary.md      the same, readable
  runs/cache/<key>.json         answers by request hash, so re-running the same request costs nothing
No image is ever written under runs/ (it is in Git).
"""
from __future__ import annotations

import hashlib
import json
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from . import __version__
from .client import ApiError, build_payload, call, mock_answer, settings_of
from .config import public, repo_of
from .data import Item, boxed_jpeg, load_items
from .prompts import passages, prompt_parts
from .scoring import compare, contested_actions, evidence_group, majority, parse, score_one, summarize

LABEL_KEYS = ["marking_type", "arrow_type", "position", "dashed_side", "visibility", "behavior_decidable",
              "expected_evidence", "accepted_rule_ids", "act_cross_line", "act_go_straight", "act_turn_left",
              "act_turn_right", "act_u_turn", "act_enter_center_lane_to_wait"]


def runs_dir(cfg: dict) -> Path:
    return repo_of(cfg) / "runs"


def _sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git_commit(repo: Path) -> str:
    head = repo / ".git" / "HEAD"
    try:
        ref = head.read_text().strip()
        if ref.startswith("ref:"):
            p = repo / ".git" / ref[5:].strip()
            if p.exists():
                return p.read_text().strip()[:12]
            packed = repo / ".git" / "packed-refs"
            for line in packed.read_text().splitlines() if packed.exists() else []:
                if line.endswith(ref[5:].strip()):
                    return line.split()[0][:12]
            return ""
        return ref[:12]
    except OSError:
        return ""


CODE_FILES = ["lane_reasoner/client.py", "lane_reasoner/config.py", "lane_reasoner/data.py", "lane_reasoner/prompts.py",
              "lane_reasoner/runner.py", "lane_reasoner/scoring.py", "config/label_schema.json", "config/action_rules.json"]


def code_hash(repo: Path) -> str:
    """Hash of the files that build the requests and score the answers (independent of Git, so a run made from
    uncommitted code can still be matched to its code later). Reports, the demo and the CLI are not included."""
    h = hashlib.sha256()
    files = [repo / f for f in CODE_FILES]
    for f in files:
        if f.exists():
            h.update(f.name.encode() + b"\0" + f.read_bytes())
    return h.hexdigest()[:16]


def cost_of(cfg: dict, usage: dict) -> float:
    pr = cfg["api"].get("price_per_million_tokens", {})
    return (usage.get("input_tokens", 0) * float(pr.get("input", 0)) + usage.get("output_tokens", 0) * float(pr.get("output", 0))) / 1e6


class Context:
    """What stays the same for every request of one run: prompt parts per region, rule IDs, rule table."""

    def __init__(self, cfg: dict, test: str, mock: bool):
        from video_tool.core import load_action_rules
        from types import SimpleNamespace
        self.cfg, self.test, self.mock = cfg, test, mock
        self.parts: dict[str, dict] = {}
        self.rule_ids: dict[str, set] = {}
        self.table = load_action_rules(SimpleNamespace(repo=repo_of(cfg)))
        self.lock = threading.Lock()

    def for_region(self, region: str) -> tuple[dict, set]:
        with self.lock:
            if region not in self.parts:
                self.parts[region] = prompt_parts(self.cfg, self.test, region)
                self.rule_ids[region] = {p["rule_id"] for p in passages(self.cfg, region)}
            return self.parts[region], self.rule_ids[region]


def ask(cfg: dict, item: Item, test: str, repeat: int = 0, mock: bool | None = None, use_cache: bool = True,
        ctx: Context | None = None) -> dict:
    """One request for one image (or the cached answer), parsed and scored."""
    mock = cfg.get("mock", False) if mock is None else mock
    ctx = ctx or Context(cfg, test, mock)
    parts, rule_ids = ctx.for_region(item.region)
    jpeg = boxed_jpeg(item, cfg)
    img_sha = _sha(jpeg)
    settings = settings_of(cfg)
    key = _sha(json.dumps({"settings": settings, "instructions": parts["hashes"]["instructions"], "schema": parts["hashes"]["schema"],
                           "user": parts["hashes"]["user_text"], "image": img_sha, "repeat": repeat, "mock": mock}, sort_keys=True).encode())
    cache = runs_dir(cfg) / "cache" / f"{key[:40]}.json"
    rec = {"image_id": item.image_id, "collection": item.collection, "region": item.region, "dataset": item.dataset,
           "split": item.split, "test": test, "repeat": repeat, "mock": mock, "cached": False,
           "request": {"settings": settings, "hashes": parts["hashes"], "image_sha256": img_sha[:16], "box": item.box,
                       "cache_key": key[:40]},
           "label": {k: item.label.get(k, "") for k in LABEL_KEYS},
           "response": None, "text": "", "answer": None, "parse_error": "", "error": "", "score": None,
           "time_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    resp = None
    if use_cache and cache.exists():
        resp = json.loads(cache.read_text(encoding="utf-8"))
        rec["cached"] = True
    else:
        try:
            resp = mock_answer(cfg, item, test, repeat) if mock else call(cfg, build_payload(cfg, parts, jpeg))
        except ApiError as e:
            rec["error"] = str(e)
            return rec
    rec["response"] = {k: resp.get(k) for k in ("model", "usage", "latency_s", "response_id", "attempts")}
    rec["text"] = resp.get("text", "")
    ans, perr = parse(rec["text"])
    rec["answer"], rec["parse_error"] = ans, perr
    if ans:
        rec["score"] = score_one(ans, item.label, test, rule_ids, contested_actions(ctx.table, item.region, item.label))
        if not rec["cached"]:
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(resp, ensure_ascii=False), encoding="utf-8")
    return rec


def _label_hashes(items: list[Item]) -> dict:
    """Dataset version of a run: per collection, a hash of the image IDs, splits, boxes and every scored label field."""
    out: dict[str, list] = {}
    for it in items:
        line = "|".join([it.image_id, it.split, ",".join(map(str, it.box))] + [str(it.label.get(k, "")) for k in LABEL_KEYS])
        out.setdefault(it.collection, []).append(line)
    return {k: _sha("\n".join(sorted(v)).encode())[:16] for k, v in out.items()}


def split_version(cfg: dict) -> int:
    """1 + the number of recorded split changes (labels/split_changes.csv), matching labels/split_v<N>.csv."""
    p = repo_of(cfg) / "labels" / "split_changes.csv"
    if not p.exists():
        return 1
    return 1 + max(0, len([x for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]) - 1)


def summarize_records(cfg: dict, records: list[dict]) -> dict:
    maj = majority(records)
    scored = []
    for iid, m in maj.items():
        r = m["record"]
        if r.get("score"):
            s = dict(r["score"])
            # requirement 6: output 2 is taken from the majority of the actions
            if m["actions_record"] is not r and m["actions_record"].get("score"):
                for k in ("output2", "actions", "contested", "unsafe", "over_cautious", "contested_unsafe", "contested_over_cautious", "consistency"):
                    s[k] = m["actions_record"]["score"].get(k, [])
                s["evidence_group"] = evidence_group(r["answer"], r["label"], s["output1"], s["output2"])
            scored.append({"image_id": iid, "score": s, "stable_o1": m["stable_o1"], "stable_o2": m["stable_o2"]})
    usage = Counter()
    lat = []
    for r in records:
        u = (r.get("response") or {}).get("usage") or {}
        if not r.get("cached") and not r.get("mock"):
            usage["input_tokens"] += u.get("input_tokens", 0)
            usage["output_tokens"] += u.get("output_tokens", 0)
            if (r.get("response") or {}).get("latency_s"):
                lat.append(r["response"]["latency_s"])
    s = summarize(scored, dict(usage))
    n_req = len(records)
    s["requests"] = n_req
    s["errors"] = sum(1 for r in records if r.get("error"))
    s["readable"] = {"n": sum(1 for r in records if r.get("answer")), "of": n_req}
    s["cached"] = sum(1 for r in records if r.get("cached"))
    s["cost_usd"] = round(cost_of(cfg, usage), 4)
    s["latency_s"] = {"mean": round(sum(lat) / len(lat), 2), "max": max(lat)} if lat else {}
    reps = Counter(r["image_id"] for r in records)
    if reps and max(reps.values()) > 1:
        s["flip_rate_output1"] = round(sum(1 for x in scored if not x["stable_o1"]) / max(1, len(scored)), 3)
        s["flip_rate_output2"] = round(sum(1 for x in scored if not x["stable_o2"]) / max(1, len(scored)), 3)
    return {"summary": s, "per_image": {x["image_id"]: x for x in scored}}


def write_summary_md(path: Path, manifest: dict, s: dict) -> None:
    pct = lambda d: f"{d['correct']}/{d['n']} ({d['correct'] / d['n']:.0%})" if d and d.get("n") else "—"  # noqa: E731
    lines = [f"# Run {manifest['run_id']}", "",
             f"Test {manifest['test']} ({'image only' if manifest['test'] == 'A' else 'image + rule passages'}), region {manifest['region']}, "
             f"{manifest['n_items']} images × {manifest['repeats']} repeat(s), model {manifest['settings']['model']}"
             + (" — MOCK ANSWERS, no model was called" if manifest["mock"] else ""), "",
             f"- Output 1 (marking type): {pct(s.get('output1'))}",
             f"- Output 2 (actions the marking decides, contested cells excluded): {pct(s.get('output2'))}",
             f"- Contested cells, separately: {pct(s.get('contested'))}",
             f"- Unsafe errors (label prohibited, answer allowed): {s.get('unsafe_errors', 0)}; over-cautious errors: {s.get('over_cautious_errors', 0)}"
             f" (contested cells, separately: {s.get('contested_unsafe_errors', 0)} unsafe, {s.get('contested_over_cautious_errors', 0)} over-cautious)",
             f"- Evidence groups: {s.get('evidence_groups', {})}",
             f"- Citations (Test B): {s.get('citations', {})}",
             f"- Answers that contradict themselves (hallucination indicator): {s.get('inconsistent_answers', 0)}",
             f"- Readable answers: {s['readable']['n']}/{s['readable']['of']}; errors: {s['errors']}; from cache: {s['cached']}",
             f"- Tokens: {s.get('usage', {})}; cost ≈ ${s.get('cost_usd', 0)}; latency: {s.get('latency_s', {})}", "",
             "| Label | Images | Output 1 correct |", "|---|---|---|"]
    for k, v in s.get("output1_by_type", {}).items():
        lines.append(f"| {k} | {v['n']} | {v['correct']} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_batch(cfg: dict, test: str | None = None, region: str | None = None, limit: int | None = None,
              repeats: int | None = None, split: str | None = None, mock: bool | None = None,
              image_ids: list | None = None, progress=None, log=print, use_cache: bool = True) -> str:
    test = test or cfg["run"]["test"]
    region = region or cfg["run"]["region"]
    repeats = int(repeats or cfg["run"].get("repeats", 1))
    limit = cfg["run"].get("limit", 0) if limit is None else limit
    mock = cfg.get("mock", False) if mock is None else mock
    items = load_items(cfg, region, split)
    if image_ids:
        want = set(image_ids)
        items = [it for it in items if it.image_id in want]
    if limit:
        items = items[:int(limit)]
    if not items:
        raise ValueError(f"No finished labels for region {region} in the configured workspaces.")
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = f"{stamp}_test{test}_{region}" + ("_mock" if mock else "")
    run_id, k = base, 1
    while True:  # two runs started in the same second (another window, another notebook) get different folders
        out = runs_dir(cfg) / run_id
        try:
            out.mkdir(parents=True, exist_ok=False)
            break
        except FileExistsError:
            k += 1
            run_id = f"{base}_{k}"
    ctx = Context(cfg, test, mock)
    parts, _ = ctx.for_region(region)
    manifest = {"run_id": run_id, "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "tool": f"lane_reasoner {__version__}", "git_commit": git_commit(repo_of(cfg)), "code_sha": code_hash(repo_of(cfg)),
                "test": test, "region": region,
                "mock": mock, "use_cache": use_cache, "repeats": repeats, "n_items": len(items), "settings": settings_of(cfg), "prompt_hashes": parts["hashes"],
                "label_sets": _label_hashes(items), "split": split or cfg["run"].get("split", "any"),
                "split_version": split_version(cfg), "items": [it.image_id for it in items], "config": public(cfg)}
    manifest["config"]["api"].pop("api_key_hint", None)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    tasks = [(it, r) for it in items for r in range(repeats)]
    records, lock = [], threading.Lock()
    done = [0]
    t0 = time.time()

    def work(task):
        it, rep = task
        rec = ask(cfg, it, test, rep, mock, use_cache=use_cache, ctx=ctx)
        with lock:
            records.append(rec)
            with open(out / "results.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            done[0] += 1
            if progress:
                progress(done[0], len(tasks), rec)
        return rec

    workers = 1 if mock else max(1, int(cfg["api"].get("parallel", 5)))
    with ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(work, tasks))
    res = summarize_records(cfg, records)
    s = res["summary"]
    s["elapsed_s"] = round(time.time() - t0, 1)
    (out / "scores.json").write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    write_summary_md(out / "summary.md", manifest, s)
    errs = [r["error"] for r in records if r.get("error")]
    log(f"Run {run_id}: Output 1 {s.get('output1', {}).get('acc')}, Output 2 {s.get('output2', {}).get('acc')}, "
        f"{s['errors']} errors, cost ≈ ${s['cost_usd']}" + (f". First error: {errs[0]}" if errs else ""))
    return run_id


def rescore_run(cfg: dict, run_id: str) -> dict:
    """Score the saved answers of a run again (after a change to the scoring or the rule table), without calling the API.

    Uses the label snapshot stored with each answer. results.jsonl, scores.json and summary.md are rewritten;
    the raw answers are not touched."""
    from types import SimpleNamespace
    from video_tool.core import load_action_rules
    d = runs_dir(cfg) / run_id
    run = load_run(cfg, run_id)
    table = load_action_rules(SimpleNamespace(repo=repo_of(cfg)))
    ids: dict[str, set] = {}
    for r in run["records"]:
        if r.get("answer"):
            if r["region"] not in ids:
                ids[r["region"]] = {p["rule_id"] for p in passages(cfg, r["region"])}
            r["score"] = score_one(r["answer"], r["label"], r["test"], ids[r["region"]], contested_actions(table, r["region"], r["label"]))
    with open(d / "results.jsonl", "w", encoding="utf-8") as f:
        for r in run["records"]:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    res = summarize_records(cfg, run["records"])
    old = (run["scores"] or {}).get("summary", {})
    res["summary"]["elapsed_s"] = old.get("elapsed_s")
    res["summary"]["rescored_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (d / "scores.json").write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    write_summary_md(d / "summary.md", run["manifest"], res["summary"])
    return res["summary"]


def run_pair(cfg: dict, region: str | None = None, limit: int | None = None, repeats: int | None = None,
             split: str | None = None, mock: bool | None = None, progress=None, log=print, use_cache: bool = True) -> dict:
    """Test A and Test B at the same time (two threads) on the same images. Returns {"A": run_id, "B": run_id}."""
    out, errors = {}, {}

    def one(test):
        try:
            out[test] = run_batch(cfg, test, region, limit, repeats, split, mock,
                                  progress=(lambda d, n, r: progress(test, d, n, r)) if progress else None, log=log, use_cache=use_cache)
        except Exception as e:  # noqa: BLE001
            errors[test] = e

    threads = [threading.Thread(target=one, args=(t,)) for t in ("A", "B")]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    if errors:
        raise next(iter(errors.values()))
    return out


def list_runs(cfg: dict) -> list[dict]:
    out = []
    for d in sorted(runs_dir(cfg).glob("*_test*"), reverse=True):
        m, s = d / "manifest.json", d / "scores.json"
        if m.exists():
            man = json.loads(m.read_text(encoding="utf-8"))
            sc = json.loads(s.read_text(encoding="utf-8"))["summary"] if s.exists() else {}
            out.append({"run_id": man["run_id"], "test": man["test"], "region": man["region"], "mock": man["mock"],
                        "n_items": man["n_items"], "repeats": man["repeats"], "model": man["settings"]["model"],
                        "output1": (sc.get("output1") or {}).get("acc"), "output2": (sc.get("output2") or {}).get("acc"),
                        "cost_usd": sc.get("cost_usd"), "errors": sc.get("errors"), "finished": s.exists()})
    return out


def load_run(cfg: dict, run_id: str) -> dict:
    d = runs_dir(cfg) / run_id
    man = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    recs = [json.loads(x) for x in (d / "results.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()] if (d / "results.jsonl").exists() else []
    sc = json.loads((d / "scores.json").read_text(encoding="utf-8")) if (d / "scores.json").exists() else None
    return {"manifest": man, "records": recs, "scores": sc}


def compare_runs(cfg: dict, run_a: str, run_b: str) -> dict:
    a, b = load_run(cfg, run_a), load_run(cfg, run_b)
    if not a["scores"] or not b["scores"]:
        raise ValueError("Both runs must be finished.")
    res = compare(a["scores"]["per_image"], b["scores"]["per_image"])
    ma, mb = a["manifest"], b["manifest"]
    res["same_settings"] = ma["settings"] == mb["settings"]
    res["same_shared_prompt"] = ma["prompt_hashes"]["shared_parts"] == mb["prompt_hashes"]["shared_parts"]
    res["tests"] = [ma["test"], mb["test"]]
    res["runs"] = [run_a, run_b]
    return res
