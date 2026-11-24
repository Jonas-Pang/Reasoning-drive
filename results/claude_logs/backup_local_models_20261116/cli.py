"""Command line: python main.py <command> ...

Everything in one place:
  web         the web page: run the model, watch its reasoning, results, evaluation, regulations, simulation
  run / lane  the model runs (marking task / lane task), results in results/runs/<run_id>/
  evaluate    accuracy, precision, recall, F1 and confusion matrices of saved runs
  results     every saved run in one table (results/index.csv)
  regulations the countries' rules: list, check, extract a new standard from its PDF, accept the draft
  carla       the CARLA simulation: a continuous route through every marking type, its video, the start map
  label       the labeling tool (images, own videos, lane labels, packages for helpers)
  selftest    every check, without the API and without CARLA

  config    show the settings in configs/ (and whether an API key is set)
  prompt    print the exact prompt of Test A or Test B for a region
  items     list the labeled images the runs use (final labels from every workspace)
  ping      one tiny text request: checks the API key, the model name and the settings (costs almost nothing)
  ask       ask the model about one image and print its reasoning step by step, next to the label
  run       run Test A or Test B on all labeled images of a region; results go to results/runs/<run_id>/ (--trace prints each answer's reasoning)
  trace     print the reasoning steps of the answers of a saved run (also written to results/runs/<run_id>/trace.md)
  runs      list the runs
  rescore   score the saved answers of runs again (after a scoring or rule-table change; no API calls)
  table     experiment table of saved runs in Markdown
  experiment table of a named experiment (configs/experiments.yaml); --real also runs its missing variants
  compare   compare two runs (normally Test A and Test B): accuracy and McNemar test
  demo      the same as web (also what the Docker image runs; metrics for Prometheus at /metrics)
  lane      the lane-level task (my whole lane, one request per image):
              lane prompt [--test B] | lane items | lane ask [image_id] | lane run --test AB | lane run --test C | lane runs
              lane trace <run_id> | lane compare <run_1> <run_2> [<run_3> <run_4> ...] [--reviewed] | lane rescore <run_id>... [--reviewed]
              lane table <run_id>... | lane review | lane freeze --note "..." | lane protocol
  selftest  check everything without the API (synthetic images, mock answers, a fake API server)

Mock or real: experiment.mock in configs/experiment.yaml decides; --mock / --real override it for one command.
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
    cfg = C.load(args.repo, drafts=bool(getattr(args, "draft", False)))
    if getattr(args, "mock", None) is not None:
        cfg["mock"] = args.mock
    if getattr(args, "region", None):
        cfg["run"]["region"] = args.region
    if getattr(args, "test", None) in C.TESTS:
        cfg["run"]["test"] = args.test
    if getattr(args, "prompt", None) and getattr(args, "cmd", "") == "lane":
        cfg["lane"]["prompt_dir"] = f"prompts/{args.prompt}"
    C.check(cfg)
    return cfg


_PRINT = threading.Lock()


def _print_trace(cfg: dict, rec: dict) -> None:
    from .agent.runner import cost_of
    from .agent.trace import passage_map, trace_text
    try:
        pm = passage_map(cfg, rec["region"])
    except Exception:  # noqa: BLE001
        pm = {}
    cost = None if rec.get("cached") or rec.get("mock") else cost_of(cfg, (rec.get("response") or {}).get("usage") or {}, (rec.get("response") or {}).get("model"))
    with _PRINT:
        print(trace_text(rec, pm, cost) + "\n", flush=True)


def _lane(cfg: dict, args) -> None:
    from .agent import lane as L
    region = cfg["run"]["region"]
    tests = ["A", "B"] if args.test == "AB" else [args.test or cfg["run"]["test"]]

    def show(rec):
        pm = {}
        try:
            pm = {p["rule_id"]: p for p in L.lane_passages(L.lane_cfg(cfg), rec["region"])}
        except Exception:  # noqa: BLE001
            pass
        with _PRINT:
            print(L.lane_trace_text(rec, pm) + "\n", flush=True)

    if args.action == "prompt":
        parts = L.lane_prompt_parts(L.lane_cfg(cfg), tests[-1], region)
        print("=== instructions (developer message) ===\n" + parts["instructions"])
        print("\n=== user message (followed by the photo, no box) ===\n" + parts["user_text"])
        if args.schema:
            print("\n=== JSON schema ===\n" + json.dumps(parts["schema"], indent=2))
        print("\nhashes:", parts["hashes"])
    elif args.action == "items":
        items = L.load_lane_items(cfg, region, args.split or "any")
        for it in items:
            lab = it.label
            print(f"{it.image_id:40s} {it.collection:10s} {it.split:5s} L {lab.get('left_color')}/{lab.get('left_pattern')} "
                  f"R {lab.get('right_color')}/{lab.get('right_pattern')} {lab.get('markings')}")
        print(f"{len(items)} images with a final lane label for region {region}")
    elif args.action == "ask":
        items = L.load_lane_items(cfg, region, "any")
        if not items:
            raise ValueError(f"No final lane labels for region {region}.")
        it = next((x for x in items if x.image_id == args.ids[0]), None) if args.ids else items[0]
        if it is None:
            raise ValueError(f"No lane-labeled image {args.ids[0]} in region {region}.")
        for t in tests:
            show(L.ask_lane(cfg, it, t, cfg.get("mock"), use_cache=not args.no_cache))
    elif args.action == "try":
        if not args.ids:
            raise ValueError("lane try needs one or more image files.")
        out, recs = L.try_images(cfg, region, args.ids, tests if args.test else ["A", "B"], cfg.get("mock"),
                                 use_cache=not args.no_cache, mirror=args.mirror)
        if args.trace:
            for r in recs:
                show(r)
        print((out / "summary.md").read_text(encoding="utf-8"))
        print(f"Saved in {out.relative_to(L.repo_of(cfg)).as_posix()}/ (summary.md, answers.jsonl, manifest.json, images/)")
    elif args.action == "run":
        prog = (lambda *a: show(a[-1])) if args.trace else None
        if len(tests) == 2:
            ids = L.run_lane_pair(cfg, region, args.limit, args.split, cfg.get("mock"), use_cache=not args.no_cache, progress=prog,
                                  again=args.again)
            c = L.compare_lane_runs(cfg, ids["A"], ids["B"])
            print(f"Saved in results/runs/{ids['A']}/ and results/runs/{ids['B']}/")
            _print_lane_compare(c)
        else:
            rid = L.run_lane(cfg, tests[0], region, args.limit, args.split, cfg.get("mock"), use_cache=not args.no_cache, progress=prog,
                             again=args.again, stage1_run=args.stage1)
            print(f"Saved in results/runs/{rid}/ (summary.md, trace.md, scores.json, results.jsonl, manifest.json)")
    elif args.action == "difficulty":
        from .evaluation import difficulty as D
        path, rows = D.write_table(cfg)
        print(D.overview_text(rows))
        print(f"Written to {path}")
    elif args.action == "runs":
        for r in L.list_lane_runs(cfg):
            print(f"{r['run_id']:38s} Test {r['test']} {r['region']} n={r['n_items']} lane={r['lane']} actions={r['output2']} "
                  f"unsafe={r['unsafe']} ${r['cost_usd']}" + (" MOCK" if r["mock"] else ""))
    elif args.action == "trace":
        for rid in args.ids:
            for r in sorted(L.load_lane_run(cfg, rid)["records"], key=lambda r: r["image_id"]):
                show(r)
            print("Written to", L.write_lane_trace(cfg, rid))
    elif args.action == "compare":
        if len(args.ids) < 2 or len(args.ids) % 2:
            raise ValueError("lane compare needs two run IDs (first, second), or several pairs for a pooled comparison.")
        pairs = list(zip(args.ids[::2], args.ids[1::2]))
        for a, b in pairs:
            _print_lane_compare(L.compare_lane_runs(cfg, a, b, reviewed=args.reviewed))
            print()
        if len(pairs) > 1:
            _print_lane_compare(L.compare_lane_pooled(cfg, pairs, reviewed=args.reviewed))
    elif args.action == "rescore":
        for rid in args.ids:
            s = L.rescore_lane_run(cfg, rid, reviewed=args.reviewed)
            print(f"{rid}: lane {s['lane']['acc']}, actions {s['output2']['acc']}, unsafe {s['unsafe_errors']}"
                  + (" (after the blind review, in scores_reviewed.json)" if args.reviewed else ""))
    elif args.action == "review":
        from .evaluation.review import review_summary
        for reg in ([args.region] if args.region else list(cfg["regions"])):
            r = review_summary(cfg, reg)
            print(f"{reg}: {r['decided']}/{r['items']} items decided on {r['images']} images (http://localhost:8770/review)")
            for kind, k in r["by_kind"].items():
                print(f"  {kind:9s} items {k['items']:3d}  label kept {k['label_kept']:3d}  label changed {k['label_changed']:3d}  cannot tell {k['cannot_tell']:3d}")
    elif args.action == "freeze":
        from .evaluation.protocol import PROTOCOL_FILE, freeze
        doc = freeze(cfg, args.note or "")
        print(f"Frozen at {doc['frozen_utc']}: {len(doc['files'])} files, settings and {len(doc['prompts'])} prompt hashes in {PROTOCOL_FILE}.")
    elif args.action == "protocol":
        from .evaluation.protocol import protocol_check
        c = protocol_check(cfg)
        print("Frozen at " + str(c["frozen_utc"]) + (": everything matches." if c["matches"] else ": DIFFERENT") if c["frozen"] else "Not frozen.")
        for d in c["differences"]:
            print("  " + d)
    elif args.action == "table":
        rows = [(str(i), rid, f"Test {L.load_lane_run(cfg, rid)['manifest']['test']}") for i, rid in enumerate(args.ids, 1)]
        print(L.lane_table_markdown(cfg, rows))


def _print_lane_compare(c: dict) -> None:
    t1, t2 = c["tests"][0], c["tests"][1]
    if c.get("pooled"):
        rep_note = f"; images answered more than once: share of correct answers per image, {c['answers'][0]} and {c['answers'][1]} answers" if c.get("repeated") else ""
        print(f"Pooled over {len(c['runs'])} pairs of runs ({t1} vs {t2}), {c['n']} paired images{rep_note}")
    else:
        print(f"Runs: {c['runs'][0]} (Test {t1})  vs  {c['runs'][1]} (Test {t2}), {c['n']} paired images")
    for k in ("lane", "lane_core", "output2", "both_boundaries", "markings", "no_unsafe"):
        d = c[k]
        ci = d.get("ci95") or [None, None]
        diff = f"  difference {d['diff']:+.3f} (95% CI {ci[0]:+.3f} to {ci[1]:+.3f})" if d.get("diff") is not None else ""
        a_lab, b_lab = ("second right more often", "first right more often") if c.get("repeated") else ("only second right", "only first right")
        test_name = "sign test" if c.get("repeated") else "McNemar exact"
        print(f"{k:16s} n={d['n']}  {t1}={d['acc_A']}  {t2}={d['acc_B']}  {a_lab}={d['only_B_right']}  "
              f"{b_lab}={d['only_A_right']}  {test_name} p={d['p_value']}{diff}")
    print(f"unsafe errors: first {c['unsafe_errors']['A']}, second {c['unsafe_errors']['B']}")
    if c.get("only_in_one_run"):
        print(f"{c['only_in_one_run']} images are in only one of the runs and are not paired.")
    if not c.get("pooled") and not (c["same_settings"] and c["same_shared_prompt"]):
        print("WARNING: the two runs differ in settings or in the shared prompt parts; the comparison is not clean.")


def main(argv: list[str] | None = None) -> None:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "label":          # the labeling tool has its own options (--data before the command)
        from .labeling.cli import main as label_main
        return label_main(argv[1:])
    if argv and argv[0] == "carla":          # the simulation needs the carla package only for these commands
        return carla_command(argv[1:])
    ap = argparse.ArgumentParser(prog="python main.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
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
    p = sub.add_parser("experiment", help="table of a named experiment in configs/experiments.yaml (--real also runs missing variants)")
    p.add_argument("name", nargs="?", help="experiment name (default: list them)")
    mode(p)
    p = sub.add_parser("table", help="experiment table (Markdown) of saved runs")
    p.add_argument("run_ids", nargs="+")
    p = sub.add_parser("rescore", help="score the saved answers of runs again (no API calls)")
    p.add_argument("run_ids", nargs="+")
    p = sub.add_parser("compare", help="compare two runs")
    p.add_argument("run_a")
    p.add_argument("run_b")
    for name in ("web", "demo"):
        p = sub.add_parser(name, help="open the web page" + (" (same as web)" if name == "demo" else ""))
        p.add_argument("--port", type=int, default=8770)
        p.add_argument("--host", default="127.0.0.1", help="address to listen on; the Docker image uses 0.0.0.0")
        p.add_argument("--no-browser", action="store_true")
        mode(p)
    p = sub.add_parser("evaluate", help="accuracy, precision, recall, F1 and confusion matrices of saved runs")
    p.add_argument("run_ids", nargs="+", help="one run, or two runs to put side by side")
    p = sub.add_parser("results", help="every saved run in one table (writes results/index.csv)")
    p.add_argument("--kind", help="only this kind: marking, lane, carla_route, carla_suite, ...")
    p = sub.add_parser("regulations", help="the countries' rules (regulations/<CODE>/)")
    p.add_argument("action", choices=["list", "check", "extract", "accept", "norms", "fetch", "extract-all"])
    p.add_argument("code", nargs="?", help="country code (check, accept, norms; extract with --code); fetch and extract-all: "
                                           "one code or several separated by commas (default: every country with documents)")
    p.add_argument("--force", action="store_true", help="fetch: download again even if the file is there")
    p.add_argument("--budget", type=float, default=5.0, help="extract-all: stop before the total estimated cost (USD) passes this")
    p.add_argument("--pdf", help="extract: the standard's file (put it in regulations/inbox/): a PDF, or a text, HTML or XML document")
    p.add_argument("--language", default="en", help="extract: language of the standard, e.g. en, zh, ja (how its 'shall' words are read)")
    p.add_argument("--write", action="store_true", help="norms: write the proposals to regulations/<CODE>/norms.yaml")
    p.add_argument("--max-cost", type=float, default=2.0, help="extract: stop before sending if the estimated cost (USD) is higher")
    p.add_argument("--code", dest="new_code", help="extract: the country code, e.g. UK")
    p.add_argument("--name", help="extract: the country's name as it goes into the prompt, e.g. \"the United Kingdom\"")
    p.add_argument("--driving-side", choices=["right", "left"], default="right")
    p.add_argument("--title", default="", help="extract: title and edition of the standard")
    p.add_argument("--pages", help="extract: only these pages, e.g. 20-45")
    p.add_argument("--all-pages", action="store_true", help="extract: every page with text, not only those with marking words")
    p.add_argument("--tag", default="", help="extract: a short name for this document when a country has several (e.g. tsrgd); "
                                             "each gets its own draft in regulations/<CODE>/drafts/ and they are merged")
    p.add_argument("--keywords", help="extract: comma-separated words that select the pages (instead of the built-in list), "
                                      "e.g. \"dividing line,lane line,marked lane\" for a long law")
    p.add_argument("--min-hits", type=int, default=2, help="extract: keyword hits a page needs to be read (default 2)")
    p.add_argument("--same-as", help="extract: a reference document (e.g. the national model law a state copies); pages whose "
                                     "lines are almost all in it are not sent, only what the state changed or added")
    p.add_argument("--same-threshold", type=float, default=0.85, help="extract: share of a page's lines found word for word "
                                                                      "in --same-as above which the page is skipped (default 0.85)")
    mode(p)
    p = sub.add_parser("lane", help="the lane-level task: my whole lane, one request per image")
    p.add_argument("action", choices=["prompt", "items", "ask", "try", "run", "runs", "trace", "compare", "rescore", "table", "review",
                                      "freeze", "protocol", "difficulty"])
    p.add_argument("ids", nargs="*", help="image ID (ask), image files (try), run ID(s) (trace, compare, rescore, table)")
    p.add_argument("--test", choices=["A", "B", "C", "D", "R", "AB"],
                   help="A image only, B with the region's passages, C with another region's passages (control), D image only without "
                        "the country, R with the passages about the elements of a saved Test A answer (--from)")
    p.add_argument("--prompt", help="the lane prompt folder under prompts/ for this command, e.g. lane_v2 (default: lane.prompt)")
    p.add_argument("--from", dest="stage1", help="Test R: the saved Test A run whose answers choose the passages")
    p.add_argument("--region")
    p.add_argument("--limit", type=int)
    p.add_argument("--split", choices=["any", "dev", "test"])
    p.add_argument("--schema", action="store_true", help="prompt: also print the JSON schema")
    p.add_argument("--no-cache", action="store_true")
    p.add_argument("--trace", action="store_true", help="run: print the reasoning of every answer as it arrives")
    p.add_argument("--reviewed", action="store_true", help="rescore, compare: against the labels with the blind review decisions applied")
    p.add_argument("--again", action="store_true", help="run: run a test on the test images again (recorded in the manifest)")
    p.add_argument("--note", help="freeze: why or what is frozen")
    p.add_argument("--draft", action="store_true", help="try: a country whose passages are still a draft may be used (marked as draft)")
    p.add_argument("--mirror", action="store_true",
                   help="try: flip the photos left to right first, e.g. a right-hand-traffic simulator frame for a left-hand-traffic country")
    mode(p)
    p = sub.add_parser("data", help="download the countries' images (datasets/<CODE>/dataset.yaml: fetch)")
    p.add_argument("action", choices=["status", "fetch"])
    p.add_argument("codes", nargs="?", help="one country code or several separated by commas (default: all)")
    p.add_argument("--root", help="folder for the images (default: DATASETS_ROOT / experiment.datasets_root)")
    sub.add_parser("selftest", help="check everything without the API")
    sub.add_parser("carla", help="the CARLA simulation: python main.py carla --help")
    sub.add_parser("label", help="the labeling tool: python main.py label --help")
    args = ap.parse_args(argv)

    try:
        if args.cmd == "selftest":
            import importlib.util
            missing = [m for m in ("numpy", "cv2", "pandas", "matplotlib") if importlib.util.find_spec(m) is None]
            if missing:
                print(f"Missing packages: {', '.join(missing)}. You are probably not in the project environment.\n"
                      "Run:  conda activate reasoning-driving   (then, once)  pip install -r requirements.txt", file=sys.stderr)
                sys.exit(1)
            from .tests.selftest import main as st
            from .tests.labeling_video import run as labeling_checks
            from .tests.project import run as project_checks
            print("== model runs, scoring, web page, lane task, deployment files ==")
            ok1 = st() == 0
            print("\n== labeling tool ==")
            ok2 = labeling_checks()
            print("\n== layout, regulations, evaluation, results, simulation settings ==")
            ok3 = project_checks()
            sys.exit(0 if ok1 and ok2 and ok3 else 1)
        if args.cmd == "regulations":
            return regulations_command(args)
        if args.cmd == "data":
            return data_command(args)
        if args.cmd == "results":
            from .evaluation.registry import build_index, table
            rows = [r for r in build_index(args.repo or C.REPO) if not args.kind or r["kind"] == args.kind]
            print(table(rows))
            print(f"\n{len(rows)} runs; the full table with every column is results/index.csv")
            return
        if args.cmd == "evaluate":
            from .evaluation.evaluate import side_by_side, to_markdown, evaluate_run, write_report
            repo = args.repo or C.REPO
            if len(args.run_ids) == 2:
                print(side_by_side(repo, *args.run_ids))
            for rid in args.run_ids:
                if len(args.run_ids) == 1:
                    print(to_markdown(evaluate_run(repo, rid)))
                print("written:", write_report(repo, rid))
            return
        cfg = _cfg(args)
        if args.cmd == "config":
            pub = C.public(cfg)
            print(json.dumps(pub, indent=2, ensure_ascii=False))
            print(f"\nMode: {'MOCK (no API calls)' if cfg.get('mock') else 'REAL API calls'}; "
                  f"API key {cfg['api']['api_key_env']}: {'set ' + pub['api']['api_key_hint'] if pub['api']['api_key_set'] else 'NOT set'}")
        elif args.cmd == "prompt":
            from .agent.prompts import prompt_parts
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
            from .agent.client import ping
            r = ping(cfg)
            print(f"OK: model {r['model']} answered {r['text']!r} in {r['latency_s']} s, tokens {r['usage']}")
            if r.get("reasoning_summary"):
                print("Reasoning summary:", r["reasoning_summary"])
            if r.get("reasoning_summary_note"):
                print("Note:", r["reasoning_summary_note"])
        elif args.cmd == "ask":
            from .data import load_items
            from .agent.runner import ask
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
            from .agent.runner import compare_runs, run_pair
            ids = run_pair(cfg, cfg["run"]["region"], args.limit, args.repeats, args.split, cfg.get("mock"), use_cache=not args.no_cache,
                           progress=(lambda t, d, n, r: _print_trace(cfg, r)) if args.trace else None)
            c = compare_runs(cfg, ids["A"], ids["B"])
            print(f"Saved in results/runs/{ids['A']}/ and results/runs/{ids['B']}/")
            for k in ("output1", "output2"):
                d = c[k]
                print(f"{k}: n={d['n']}  Test A {d['acc_A']}  Test B {d['acc_B']}  only B right {d['only_B_right']}  "
                      f"only A right {d['only_A_right']}  McNemar exact p={d['p_value']}")
        elif args.cmd == "run":
            from .agent.runner import run_batch
            rid = run_batch(cfg, cfg["run"]["test"], cfg["run"]["region"], args.limit, args.repeats, args.split, cfg.get("mock"),
                            progress=(lambda d, n, r: _print_trace(cfg, r)) if args.trace else
                            (lambda d, n, r: print(f"\r{d}/{n}", end="", flush=True) if d < n else print(f"\r{d}/{n}")),
                            use_cache=not args.no_cache)
            print(f"Saved in results/runs/{rid}/ (summary.md, trace.md, scores.json, results.jsonl, manifest.json)")
        elif args.cmd == "trace":
            from .agent.runner import load_run
            from .agent.trace import write_trace_file
            want = set(args.image_ids)
            for r in sorted(load_run(cfg, args.run_id)["records"], key=lambda r: (r["image_id"], r.get("repeat", 0))):
                if not want or r["image_id"] in want or any(r["image_id"].endswith(w) for w in want):
                    _print_trace(cfg, r)
            print("Written to", write_trace_file(cfg, args.run_id))
        elif args.cmd == "experiment":
            from .evaluation.experiments import listing, table
            print(table(cfg["_repo"], args.name, real=args.mock is False, mock=args.mock is True) if args.name else listing(cfg["_repo"]))
        elif args.cmd == "runs":
            from .agent.runner import list_runs
            for r in list_runs(cfg):
                print(f"{r['run_id']:38s} Test {r['test']} {r['region']} n={r['n_items']}x{r['repeats']} "
                      f"O1={r['output1']} O2={r['output2']} ${r['cost_usd']}" + (" MOCK" if r["mock"] else ""))
        elif args.cmd == "table":
            from .evaluation.report import experiment_table, to_markdown
            from .agent.runner import load_run
            rows = []
            for i, rid in enumerate(args.run_ids, 1):
                m = load_run(cfg, rid)["manifest"]
                rows.append((str(i), rid, f"Test {m['test']} · {m['prompt_hashes']['prompt_dir']}"))
            print(to_markdown(experiment_table(cfg, rows)))
        elif args.cmd == "rescore":
            from .agent.runner import rescore_run
            for rid in args.run_ids:
                s = rescore_run(cfg, rid)
                print(f"{rid}: Output 1 {s['output1']['acc']}, Output 2 {s['output2']['acc']}, unsafe {s['unsafe_errors']}, "
                      f"over-cautious {s['over_cautious_errors']} (contested: {s['contested_unsafe_errors']} / {s['contested_over_cautious_errors']})")
        elif args.cmd == "compare":
            from .agent.runner import compare_runs
            c = compare_runs(cfg, args.run_a, args.run_b)
            print(f"Runs: {c['runs'][0]} (Test {c['tests'][0]})  vs  {c['runs'][1]} (Test {c['tests'][1]})")
            for k in ("output1", "output2"):
                d = c[k]
                print(f"{k}: n={d['n']}  acc {c['tests'][0]}={d['acc_A']}  acc {c['tests'][1]}={d['acc_B']}  "
                      f"only second right={d['only_B_right']}  only first right={d['only_A_right']}  McNemar exact p={d['p_value']}")
            if not (c["same_settings"] and c["same_shared_prompt"]):
                print("WARNING: the two runs differ in settings or in the shared prompt parts; the comparison is not clean.")
        elif args.cmd == "lane":
            _lane(cfg, args)
        elif args.cmd in ("demo", "web"):
            from .web.server import serve
            serve(cfg, args.port, not args.no_browser, args.host)
    except (C.ConfigError, ValueError, KeyError, FileNotFoundError) as e:
        print("Error:", str(e).strip("'"), file=sys.stderr)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        from .agent.client import ApiError
        if isinstance(e, ApiError):
            print("API error:", e, file=sys.stderr)
            sys.exit(2)
        raise



def data_command(args) -> None:
    import os
    from pathlib import Path
    from .labeling import fetch as F
    repo = Path(args.repo or C.REPO)
    codes = [c.strip() for c in args.codes.split(",") if c.strip()] if args.codes else None
    root = args.root or os.environ.get("DATASETS_ROOT") or C.load(repo).get("datasets_root") or ""
    if args.action == "status":
        for r in F.status(repo, Path(root) if root else None, codes):
            print(f"{r['region']:3} {r['collection']:12} {r['on_disk']:4}/{r['candidates']:<4} candidate frames  "
                  f"{'download: python main.py data fetch ' + r['region'] if r['auto'] else r['access'] + ': ' + r['how']}")
        return
    if not root:
        raise ValueError("Where should the images go? --root <folder> (or DATASETS_ROOT in .env)")
    res = F.fetch(repo, Path(root), codes)
    bad = [r for r in res if r["status"] == "partial"]
    sys.exit(1 if bad else 0)


def regulations_command(args) -> None:
    from .regulations import store
    repo = args.repo or C.REPO
    if args.action == "list":
        for r in store.overview(repo):
            print(f"{r['code']:4} {r['name']:22} {r['driving_side']:5} {r['passages']:4} passages  "
                  f"rule tables: {'marking' if r['rule_table_marking'] else '-'} {'lane' if r['rule_table_lane'] else '-'}"
                  f"{'  DRAFT waiting' if r['draft'] else ''}  [{r['status']}]  {r['standard']}")
        return
    if args.action == "check":
        probs = store.check(repo, args.code)
        print("\n".join(probs) if probs else "No problems: every country's files fit the template.")
        sys.exit(1 if probs else 0)
    if args.action == "norms":
        from .regulations import norms as N
        if not args.code:
            raise ValueError("Which country? python main.py regulations norms <CODE> [--write]")
        if args.write:
            f, n = N.write_proposals(repo, args.code.upper())
            print(f"{f}: {n} proposals added (existing values kept). Read them and set checked: true.")
        for r in N.table(repo, args.code.upper()):
            print(f"{r['rule_id']:22} {r['proposed']:12} {r['word'] or '-':10} {('reviewed: ' + r['reviewed']) if r['reviewed'] else '':22} {r['text'][:70]}")
        return
    if args.action in ("fetch", "extract-all"):
        from .regulations import sources as SRC
        codes = [c.strip() for c in args.code.split(",") if c.strip()] if args.code else None
        if args.action == "fetch":
            res = SRC.fetch(repo, codes, force=args.force)
            bad = [r for r in res if r["status"] == "failed"]
            print(f"{len(res) - len(bad)} of {len(res)} documents are in regulations/inbox/ (log: regulations/inbox/{SRC.LOG}).")
            sys.exit(1 if bad else 0)
        cfg = C.load(repo)
        mock = cfg.get("mock", True) if args.mock is None else args.mock
        res = SRC.extract_all(repo, cfg, codes, mock=mock, budget=args.budget, max_cost=min(args.max_cost, args.budget))
        cost = sum(r.get("cost_usd", 0.0) for r in res)
        errs = [r for r in res if str(r["status"]).startswith("error")]
        print(f"{sum(1 for r in res if r['status'] == 'extracted')} extracted, {sum(1 for r in res if r['status'] == 'done before')} "
              f"done before, {len(errs)} errors; cost ${round(cost, 4)}. Read the drafts, then: python main.py regulations accept <CODE>")
        sys.exit(1 if errs else 0)
    from .regulations.extract import accept, extract
    if args.action == "accept":
        if not args.code:
            raise ValueError("Which country? python main.py regulations accept <CODE>")
        accept(repo, args.code)
        return
    if not (args.pdf and args.new_code and args.name):
        raise ValueError("extract needs --pdf, --code and --name (and --driving-side left for left-hand traffic)")
    cfg = C.load(repo)
    first, last = 1, None
    if args.pages:
        a, _, b = args.pages.partition("-")
        first, last = int(a), int(b or a)
    mock = cfg.get("mock", True) if args.mock is None else args.mock
    try:
        extract(repo, cfg, args.pdf, args.new_code, args.name, args.driving_side, args.title, mock=mock,
                all_pages=args.all_pages, first=first, last=last, language=args.language, max_cost=args.max_cost,
                tag=args.tag, keywords=[k.strip() for k in args.keywords.split(",") if k.strip()] if args.keywords else None,
                min_hits=args.min_hits, same_as=args.same_as, same_threshold=args.same_threshold)
    except RuntimeError as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)


def carla_command(argv: list[str]) -> None:
    """python main.py carla route [name] [--mock] [--record] [--preview] | video <run folder> | map <Town> | routes"""
    usage = ("python main.py carla route [route1] [--mock] [--record] [--preview]   drive one route of configs/carla.yaml\n"
             "python main.py carla video <results/carla/run> [findings.json]       the replay video of a route run (needs ffmpeg)\n"
             "python main.py carla map Town03_Opt                                   the map CARLA opens at start (restart CARLA)\n"
             "python main.py carla routes                                           the routes and their stops\n"
             "python main.py carla countries [--countries US,CN,UK,JP] [--mock]     the same places asked and driven as each country\n"
             "python main.py carla countries-video <results/carla/run>              the video of a countries run, with the prompts\n"
             "python main.py carla opendrive-test [--lht]                           an OpenDRIVE road in standalone mode (CARLA 0.9.16)")
    if not argv or argv[0] in ("-h", "--help"):
        print(usage)
        return
    cmd, rest = argv[0], argv[1:]
    from .simulation import settings as S
    if cmd == "routes":
        st = S.load_settings(C.REPO)
        for name, r in (st.get("routes") or {}).items():
            print(f"{name}: {r.get('map')} {r.get('weather')}{' night' if r.get('night') else ''}, seed {r.get('seed')}, "
                  f"drive with {r.get('drive_with')}")
            for s_ in r.get("stops") or []:
                print(f"    {s_.get('label', s_.get('type'))}  ->  {s_.get('intent')}")
        return
    if cmd == "map":
        if not rest:
            raise SystemExit("python main.py carla map <Town, e.g. Town03_Opt>")
        print("CARLA will start with", rest[0], "(", S.set_map(rest[0]), "); close and start CARLA again.")
        return
    if cmd in ("route", "countries", "opendrive-test"):
        import importlib.util
        if importlib.util.find_spec("carla") is None:
            # this Python has no carla package (the project Python is 3.11; CARLA 0.9.15 ships it for 3.7/3.8):
            # run the same command with the Python named in configs/carla.yaml (server.python)
            import subprocess
            from pathlib import Path
            py = (S.load_settings(C.REPO).get("server") or {}).get("python") or ""
            if not py or not Path(py).exists():
                raise SystemExit("No carla package in this Python and no server.python in configs/carla.yaml: install carla==0.9.15 "
                                 "into a Python 3.8 and name it there.")
            print(f"(carla is not installed here; running with {py})", flush=True)
            raise SystemExit(subprocess.call([py, str(C.REPO / "main.py"), "carla", cmd, *rest], cwd=str(C.REPO)))
        if cmd == "countries":
            from .simulation.countries import main as countries_main
            return countries_main(rest)
        if cmd == "opendrive-test":
            from .simulation.opendrive_test import main as od_main
            return od_main(rest)
        from .simulation.route import main as route_main
        return route_main(rest)
    if cmd == "countries-video":
        from .simulation.countries_video import main as cv_main
        return cv_main(rest)
    if cmd == "video":
        try:
            from .simulation.route_video import main as video_main
        except ModuleNotFoundError as e:
            raise SystemExit(f"The replay video needs the package {e.name!r} (pillow): install it into this Python "
                             f"({sys.executable}) with pip install pillow, or run the command with the project's Python.")
        return video_main(rest)
    raise SystemExit(usage)


if __name__ == "__main__":
    main()
