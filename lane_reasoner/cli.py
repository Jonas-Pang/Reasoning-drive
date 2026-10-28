"""Command line: python -m lane_reasoner <command> ...

  config    show the settings in config/experiment.yaml (and whether an API key is set)
  prompt    print the exact prompt of Test A or Test B for a region
  items     list the labeled images the runs use (final labels from every workspace)
  ping      one tiny text request: checks the API key, the model name and the settings (costs almost nothing)
  ask       ask the model about one image and print its reasoning step by step, next to the label
  run       run Test A or Test B on all labeled images of a region; results go to runs/<run_id>/ (--trace prints each answer's reasoning)
  trace     print the reasoning steps of the answers of a saved run (also written to runs/<run_id>/trace.md)
  runs      list the runs
  rescore   score the saved answers of runs again (after a scoring or rule-table change; no API calls)
  table     experiment table of saved runs in Markdown
  compare   compare two runs (normally Test A and Test B): accuracy and McNemar test
  demo      open the demo page in the browser
  selftest  check everything without the API (synthetic images, mock answers, a fake API server)

Mock or real: experiment.mock in config/experiment.yaml decides; --mock / --real override it for one command.
The API key is read from the environment variable named in api.api_key_env (default OPENAI_API_KEY),
usually set in the .env file of the repository.
"""
from __future__ import annotations

import argparse
import json
import sys
import threading

from . import config as C


def _cfg(args) -> dict:
    cfg = C.load(args.repo)
    if getattr(args, "mock", None) is not None:
        cfg["mock"] = args.mock
    if getattr(args, "region", None):
        cfg["run"]["region"] = args.region
    if getattr(args, "test", None) in C.TESTS:
        cfg["run"]["test"] = args.test
    C.check(cfg)
    return cfg


_PRINT = threading.Lock()


def _print_trace(cfg: dict, rec: dict) -> None:
    from .runner import cost_of
    from .trace import passage_map, trace_text
    try:
        pm = passage_map(cfg, rec["region"])
    except Exception:  # noqa: BLE001
        pm = {}
    cost = None if rec.get("cached") or rec.get("mock") else cost_of(cfg, (rec.get("response") or {}).get("usage") or {})
    with _PRINT:
        print(trace_text(rec, pm, cost) + "\n", flush=True)


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="python -m lane_reasoner", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", help="repository folder (default: the one this package is in)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def mode(p):
        g = p.add_mutually_exclusive_group()
        g.add_argument("--mock", dest="mock", action="store_const", const=True, default=None, help="made-up answers, no API call")
        g.add_argument("--real", dest="mock", action="store_const", const=False, help="call the API")

    sub.add_parser("config", help="show the settings")
    p = sub.add_parser("prompt", help="print the prompt")
    p.add_argument("--test", choices=["A", "B"])
    p.add_argument("--region")
    p.add_argument("--schema", action="store_true", help="also print the JSON schema")
    p = sub.add_parser("items", help="list the labeled images")
    p.add_argument("--region")
    p = sub.add_parser("ping", help="check the API key and the model with one tiny text request (always calls the API)")
    mode(p)  # accepted for symmetry with the other commands; ping always sends its one request
    p = sub.add_parser("ask", help="ask about one image")
    p.add_argument("image_id", nargs="?", help="default: the first image of the region")
    p.add_argument("--test", choices=["A", "B", "AB"], default="AB")
    p.add_argument("--region")
    p.add_argument("--no-cache", action="store_true")
    mode(p)
    p = sub.add_parser("run", help="run Test A or Test B (or both at the same time: --test AB) on the labeled images")
    p.add_argument("--test", choices=["A", "B", "AB"])
    p.add_argument("--region")
    p.add_argument("--limit", type=int, help="only the first N images (fixed random order); 0 = all")
    p.add_argument("--repeats", type=int)
    p.add_argument("--split", choices=["any", "dev", "test"])
    p.add_argument("--no-cache", action="store_true", help="ask again even if the same request was answered before")
    p.add_argument("--trace", action="store_true", help="print the reasoning steps of every answer as it arrives")
    mode(p)
    p = sub.add_parser("trace", help="print the reasoning steps of a saved run")
    p.add_argument("run_id")
    p.add_argument("image_ids", nargs="*", help="only these images (default: all)")
    sub.add_parser("runs", help="list the runs")
    p = sub.add_parser("table", help="experiment table (Markdown) of saved runs")
    p.add_argument("run_ids", nargs="+")
    p = sub.add_parser("rescore", help="score the saved answers of runs again (no API calls)")
    p.add_argument("run_ids", nargs="+")
    p = sub.add_parser("compare", help="compare two runs")
    p.add_argument("run_a")
    p.add_argument("run_b")
    p = sub.add_parser("demo", help="open the demo page")
    p.add_argument("--port", type=int, default=8770)
    p.add_argument("--no-browser", action="store_true")
    mode(p)
    sub.add_parser("selftest", help="check everything without the API")
    args = ap.parse_args(argv)

    try:
        if args.cmd == "selftest":
            import importlib.util
            missing = [m for m in ("numpy", "cv2", "pandas", "matplotlib") if importlib.util.find_spec(m) is None]
            if missing:
                print(f"Missing packages: {', '.join(missing)}. You are probably not in the project environment.\n"
                      "Run:  conda activate reasoning-driving   (then, once)  pip install -r requirements.txt", file=sys.stderr)
                sys.exit(1)
            from .selftest import main as st
            sys.exit(st())
        cfg = _cfg(args)
        if args.cmd == "config":
            pub = C.public(cfg)
            print(json.dumps(pub, indent=2, ensure_ascii=False))
            print(f"\nMode: {'MOCK (no API calls)' if cfg.get('mock') else 'REAL API calls'}; "
                  f"API key {cfg['api']['api_key_env']}: {'set ' + pub['api']['api_key_hint'] if pub['api']['api_key_set'] else 'NOT set'}")
        elif args.cmd == "prompt":
            from .prompts import prompt_parts
            parts = prompt_parts(cfg, cfg["run"]["test"], cfg["run"]["region"])
            print("=== instructions (developer message) ===\n" + parts["instructions"])
            print("\n=== user message (followed by the image) ===\n" + parts["user_text"])
            if args.schema:
                print("\n=== JSON schema ===\n" + json.dumps(parts["schema"], indent=2))
            print("\nhashes:", parts["hashes"])
        elif args.cmd == "items":
            from .data import load_items
            items = load_items(cfg, cfg["run"]["region"], "any", [])
            for it in items:
                print(f"{it.image_id:40s} {it.collection:10s} {it.split:5s} {it.marking}")
            print(f"{len(items)} labeled images for region {cfg['run']['region']}")
        elif args.cmd == "ping":
            from .client import ping
            r = ping(cfg)
            print(f"OK: model {r['model']} answered {r['text']!r} in {r['latency_s']} s, tokens {r['usage']}")
            if r.get("reasoning_summary"):
                print("Reasoning summary:", r["reasoning_summary"])
            if r.get("reasoning_summary_note"):
                print("Note:", r["reasoning_summary_note"])
        elif args.cmd == "ask":
            from .data import load_items
            from .runner import ask
            items = load_items(cfg, cfg["run"]["region"], "any", [])
            if not items:
                raise ValueError(f"No finished labels for region {cfg['run']['region']}.")
            it = next((x for x in items if x.image_id == args.image_id), None) if args.image_id else items[0]
            if it is None:
                raise ValueError(f"No labeled image {args.image_id} in region {cfg['run']['region']}.")
            print(f"{it.image_id} ({it.marking}), {'MOCK' if cfg.get('mock') else cfg['api']['model']}")
            for t in args.test:
                _print_trace(cfg, ask(cfg, it, t, 0, cfg.get("mock"), use_cache=not args.no_cache))
        elif args.cmd == "run" and args.test == "AB":
            from .runner import compare_runs, run_pair
            ids = run_pair(cfg, cfg["run"]["region"], args.limit, args.repeats, args.split, cfg.get("mock"), use_cache=not args.no_cache,
                           progress=(lambda t, d, n, r: _print_trace(cfg, r)) if args.trace else None)
            c = compare_runs(cfg, ids["A"], ids["B"])
            print(f"Saved in runs/{ids['A']}/ and runs/{ids['B']}/")
            for k in ("output1", "output2"):
                d = c[k]
                print(f"{k}: n={d['n']}  Test A {d['acc_A']}  Test B {d['acc_B']}  only B right {d['only_B_right']}  "
                      f"only A right {d['only_A_right']}  McNemar exact p={d['p_value']}")
        elif args.cmd == "run":
            from .runner import run_batch
            rid = run_batch(cfg, cfg["run"]["test"], cfg["run"]["region"], args.limit, args.repeats, args.split, cfg.get("mock"),
                            progress=(lambda d, n, r: _print_trace(cfg, r)) if args.trace else
                            (lambda d, n, r: print(f"\r{d}/{n}", end="", flush=True) if d < n else print(f"\r{d}/{n}")),
                            use_cache=not args.no_cache)
            print(f"Saved in runs/{rid}/ (summary.md, trace.md, scores.json, results.jsonl, manifest.json)")
        elif args.cmd == "trace":
            from .runner import load_run
            from .trace import write_trace_file
            want = set(args.image_ids)
            for r in sorted(load_run(cfg, args.run_id)["records"], key=lambda r: (r["image_id"], r.get("repeat", 0))):
                if not want or r["image_id"] in want or any(r["image_id"].endswith(w) for w in want):
                    _print_trace(cfg, r)
            print("Written to", write_trace_file(cfg, args.run_id))
        elif args.cmd == "runs":
            from .runner import list_runs
            for r in list_runs(cfg):
                print(f"{r['run_id']:38s} Test {r['test']} {r['region']} n={r['n_items']}x{r['repeats']} "
                      f"O1={r['output1']} O2={r['output2']} ${r['cost_usd']}" + (" MOCK" if r["mock"] else ""))
        elif args.cmd == "table":
            from .report import experiment_table, to_markdown
            from .runner import load_run
            rows = []
            for i, rid in enumerate(args.run_ids, 1):
                m = load_run(cfg, rid)["manifest"]
                rows.append((str(i), rid, f"Test {m['test']} · {m['prompt_hashes']['prompt_dir']}"))
            print(to_markdown(experiment_table(cfg, rows)))
        elif args.cmd == "rescore":
            from .runner import rescore_run
            for rid in args.run_ids:
                s = rescore_run(cfg, rid)
                print(f"{rid}: Output 1 {s['output1']['acc']}, Output 2 {s['output2']['acc']}, unsafe {s['unsafe_errors']}, "
                      f"over-cautious {s['over_cautious_errors']} (contested: {s['contested_unsafe_errors']} / {s['contested_over_cautious_errors']})")
        elif args.cmd == "compare":
            from .runner import compare_runs
            c = compare_runs(cfg, args.run_a, args.run_b)
            print(f"Runs: {c['runs'][0]} (Test {c['tests'][0]})  vs  {c['runs'][1]} (Test {c['tests'][1]})")
            for k in ("output1", "output2"):
                d = c[k]
                print(f"{k}: n={d['n']}  acc {c['tests'][0]}={d['acc_A']}  acc {c['tests'][1]}={d['acc_B']}  "
                      f"only second right={d['only_B_right']}  only first right={d['only_A_right']}  McNemar exact p={d['p_value']}")
            if not (c["same_settings"] and c["same_shared_prompt"]):
                print("WARNING: the two runs differ in settings or in the shared prompt parts; the comparison is not clean.")
        elif args.cmd == "demo":
            from .demo import serve
            serve(cfg, args.port, not args.no_browser)
    except (C.ConfigError, ValueError, KeyError, FileNotFoundError) as e:
        print("Error:", str(e).strip("'"), file=sys.stderr)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        from .client import ApiError
        if isinstance(e, ApiError):
            print("API error:", e, file=sys.stderr)
            sys.exit(2)
        raise


if __name__ == "__main__":
    main()
