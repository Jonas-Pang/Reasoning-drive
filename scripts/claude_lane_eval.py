"""Written by Claude: run the lane tests with the real API on the final lane labels, both countries, then list the runs.

    python scripts/claude_lane_eval.py                       dev split, CN and US, tests A B C, prompt lane_v3 (D and R: --tests A,B,C,D,R)
    python scripts/claude_lane_eval.py --split test          the held-out test split (run once the prompt is frozen)
    python scripts/claude_lane_eval.py --limit 2 --tests A   smoke test
    python scripts/claude_lane_eval.py --regions CN --tests C,R   only these (R re-asks the newest matching Test A run)

China uses the MapDR images only: the older CULane workspace (68 China dev images labeled before the current rules and
not screened for line-crossing frames) is left out with --exclude culane (the default). configs/experiment.yaml is not
changed; the exclusion holds for this script only. Log: results/claude_logs/lane_eval_<split>.log"""
import argparse
import io
import json
import os
import sys
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
os.chdir(repo)
sys.path.insert(0, str(repo))

ap = argparse.ArgumentParser()
ap.add_argument("--split", default="dev")
ap.add_argument("--regions", default="CN,US")
ap.add_argument("--tests", default="A,B,C")   # owner 2026-11-17: D and R not used for now
ap.add_argument("--prompt", default="lane_v3")
ap.add_argument("--limit", type=int, default=0)
ap.add_argument("--exclude", default="culane", help="workspace folders to leave out, comma separated ('' = none)")
ap.add_argument("--api", default="", help="a model profile of configs/api_profiles.yaml (e.g. local_qwen35_9b); default: "
                "configs/api.yaml (gpt-6.1-sol)")
ap.add_argument("--again", action="store_true", help="test split: run a test again that already has a run (the manifest "
                "records it); used after a run that failed, e.g. because the API credits ran out")
a = ap.parse_args()

logp = repo / "results" / "claude_logs" / f"lane_eval_{a.split}{'_' + a.api if a.api else ''}.log"
logp.parent.mkdir(parents=True, exist_ok=True)
logf = open(logp, "a", encoding="utf-8")


class Tee(io.TextIOBase):
    seen = []

    def __init__(self, *s):
        self.s = s

    def write(self, x):
        Tee.seen.append(x)
        del Tee.seen[:-400]
        for s in self.s:
            s.write(x)
            s.flush()
        return len(x)

    def flush(self):
        for s in self.s:
            s.flush()


sys.stdout = Tee(sys.__stdout__, logf)
sys.stderr = Tee(sys.__stderr__, logf)

# environment as in scripts/claude_run.py: DATASETS_ROOT / DATA_DIR from .env, the system certificate store
env = repo / ".env"
if env.exists():
    for line in env.read_text(encoding="utf-8").splitlines():
        k, _, v = line.partition("=")
        if k.strip() in ("DATASETS_ROOT", "DATA_DIR", "HF_TOKEN") and v.strip() and not os.environ.get(k.strip()):
            os.environ[k.strip()] = v.strip().strip('"')
for k in ("DATASETS_ROOT", "DATA_DIR"):
    if os.environ.get(k) and not os.path.isabs(os.environ[k]):
        os.environ[k] = str((repo / os.environ[k]).resolve())
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass

import reasoning_drive.data as data  # noqa: E402
from reasoning_drive.cli import main  # noqa: E402

excluded = {x.strip().lower() for x in a.exclude.split(",") if x.strip()}
_orig = data.workspace_dirs


def workspace_dirs(cfg):
    return [p for p in _orig(cfg) if p.name.lower() not in excluded]


data.workspace_dirs = workspace_dirs


def run(args):
    print("\n$ main.py " + " ".join(args), flush=True)
    try:
        main(args)
        rc = 0
    except SystemExit as e:
        rc = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    except Exception as e:  # noqa: BLE001
        print(f"Error: {type(e).__name__}: {e}", flush=True)
        rc = 1
    print(f"[exit {rc}]", flush=True)
    return rc


def latest_a_run(region: str) -> str | None:
    """The newest saved Test A run of this region on the same split and prompt (Test R re-asks its images)."""
    runs = repo / "results" / "runs"
    for d in sorted(runs.glob(f"*_laneA_{region}"), reverse=True):
        try:
            text = (d / "manifest.json").read_text(encoding="utf-8")
        except OSError:
            continue
        try:
            run_model = json.loads(text).get("settings", {}).get("model", "")
        except ValueError:
            continue
        if run_model != MODEL:
            continue
        if f'"{a.split}"' in text and a.prompt in text and (d / "scores.json").exists():
            try:
                if json.loads((d / "scores.json").read_text(encoding="utf-8"))["summary"].get("errors"):
                    continue   # a run with failed requests (e.g. no API credits) is not a source for Test R
            except (OSError, ValueError, KeyError):
                continue
            return d.name
    return None


def run_test(region: str, t: str, limit: list) -> int:
    args = ["lane", "run", "--test", t, "--region", region, "--split", a.split, "--prompt", a.prompt, "--real"] + limit + API
    if a.again:
        args.append("--again")
    if t == "R":
        src = latest_a_run(region)
        if not src:
            print(f"Test R {region}: no saved Test A run on {a.split} with {a.prompt}; skipped", flush=True)
            return 1
        args += ["--from", src]
    Tee.seen.clear()
    rc = run(args)
    if "no credits remaining" in "".join(Tee.seen):
        print("\nSTOPPED: the OpenAI account has no credits left. Add credits, then run the remaining tests again "
              "(on the test split with --again).", flush=True)
        sys.exit(2)
    if rc != 0:   # a dropped connection (SSL / timeout) usually clears on a second try
        print("Trying once more ...", flush=True)
        rc = run(args)
    return rc


API = ["--api", a.api] if a.api else []
MODEL, PROTOCOL = "gpt-6.1-sol", "configs/lane_protocol.json"
if a.api:
    import yaml  # noqa: E402
    prof = (yaml.safe_load((repo / "configs" / "api_profiles.yaml").read_text(encoding="utf-8")) or {}).get("profiles", {})
    if a.api not in prof:
        sys.exit(f"--api {a.api}: not in configs/api_profiles.yaml ({', '.join(prof)})")
    MODEL, PROTOCOL = prof[a.api]["name"], prof[a.api].get("protocol_file", PROTOCOL)
else:
    import yaml  # noqa: E402
    MODEL = ((yaml.safe_load((repo / "configs" / "api.yaml").read_text(encoding="utf-8")) or {}).get("model") or {}).get("name", MODEL)

if a.api and prof[a.api].get("provider") == "ollama":   # is the local model there? (otherwise every image fails)
    import urllib.request  # noqa: E402
    base = (os.environ.get("RD_OLLAMA_URL") or prof[a.api]["base_url"]).rstrip("/")
    try:
        with urllib.request.urlopen(base + "/api/tags", timeout=10) as r:
            have = {m.get("name") for m in json.loads(r.read().decode("utf-8")).get("models", [])}
    except OSError as e:
        sys.exit(f"Ollama does not answer at {base} ({e}). Start Ollama (the llama icon near the clock), then try again.")
    if MODEL not in have and MODEL + ":latest" not in have:
        sys.exit(f"Model {MODEL} is not downloaded. Run:  ollama pull {MODEL}   (downloaded: {', '.join(sorted(have)) or 'none'})")

from datetime import datetime  # noqa: E402
print(f"\n=== {datetime.now():%Y-%m-%d %H:%M:%S}  model={MODEL} split={a.split} regions={a.regions} tests={a.tests} "
      f"prompt={a.prompt} excluded={sorted(excluded) or 'none'}", flush=True)
limit = ["--limit", str(a.limit)] if a.limit else []
if a.split == "test" and not (repo / PROTOCOL).exists():
    # the test images are answered only under a frozen protocol (reasoning_drive/evaluation/protocol.py); the owner
    # froze prompt lane_v3 on 2026-11-16 after the development runs, so freeze it once here
    if run(["lane", "freeze", "--prompt", a.prompt, "--note",
            f"owner decision 2026-11-16: prompt {a.prompt} frozen after the development runs (CN MapDR, US BDD100K), "
            f"model {MODEL}"] + API) != 0:
        sys.exit("Freezing the protocol failed; nothing was sent for the test images.")
if a.split == "test" and (repo / PROTOCOL).exists():
    # a country added after the freeze (UK, India: 2026-11-16) is added to the frozen protocol before its first test run;
    # the countries frozen before keep their hashes and frozen time (protocol.freeze_add)
    _doc = json.loads((repo / PROTOCOL).read_text(encoding="utf-8"))
    _frozen = set(_doc.get("regions") or []) | {k.split("_", 1)[1] for k in _doc.get("prompts", {}) if "_" in k}
    _new = [r.strip() for r in a.regions.split(",") if r.strip() and r.strip() not in _frozen]
    if _new and run(["lane", "freeze", "--add", "--prompt", a.prompt, "--note",
                     f"countries added after the freeze: {', '.join(_new)} (owner decision 2026-11-16: small pilot)"] + API) != 0:
        sys.exit("Adding the new countries to the frozen protocol failed; nothing was sent for their test images.")
for region in [r.strip() for r in a.regions.split(",") if r.strip()]:
    if run(["lane", "items", "--region", region, "--split", a.split]) != 0:
        continue
    for t in [t.strip() for t in a.tests.split(",") if t.strip()]:
        run_test(region, t, limit)
run(["lane", "runs"] + API)
print(f"\nALL DONE. Log: {logp}", flush=True)
