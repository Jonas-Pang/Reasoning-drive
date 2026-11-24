"""Written by Claude: after the project was copied to the shared drive (F:\\Project\\Reasoning_Drive on Windows,
/Volumes/<drive>/Project/Reasoning_Drive on the Mac), make its paths work on both computers and check the pipeline.
  1. .env: DATASETS_ROOT=../../数据集 and DATA_DIR=../Reasning_Drive/data (relative to the project; other lines unchanged)
  2. every datasets/<country>/<set>/*.set.json: source_root relative to the workspaces folder
  3. the image sets, the labeled items, and a smoke test: lane tests A, B, C on 2 US development images (real API)
Run:  python scripts/claude_move_check.py            (add --no-api to skip the API calls)
Log:  results/claude_logs/move_check.log"""
import json, os, subprocess, sys, types
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo))
logp = repo / "results" / "claude_logs" / "move_check.log"
logp.parent.mkdir(parents=True, exist_ok=True)
log = open(logp, "w", encoding="utf-8")
def say(msg=""):
    print(msg, flush=True); log.write(msg + "\n"); log.flush()
say(f"Project: {repo}")

# 1. .env (only these two keys are touched; the values of the other keys are not printed)
want = {"DATASETS_ROOT": "../../数据集", "DATA_DIR": "../Reasning_Drive/data"}
envf = repo / ".env"
lines = envf.read_text(encoding="utf-8").splitlines() if envf.exists() else []
seen, out = set(), []
for line in lines:
    k = line.partition("=")[0].strip()
    if k in want and not line.lstrip().startswith("#"):
        out.append(f"{k}={want[k]}"); seen.add(k)
    else:
        out.append(line)
out += [f"{k}={v}" for k, v in want.items() if k not in seen]
envf.write_text("\n".join(out) + "\n", encoding="utf-8")
root = (repo / want["DATASETS_ROOT"]).resolve()
say(f"1. .env: DATASETS_ROOT -> {root} ({'found' if root.is_dir() else 'MISSING'}),"
    f" DATA_DIR -> {(repo / want['DATA_DIR']).resolve()} ({'found' if (repo / want['DATA_DIR']).is_dir() else 'MISSING'})")

# 2. source_root of every image set
from reasoning_drive.labeling.core import source_path, source_to_store
fake = types.SimpleNamespace(data=root / "_")
say("2. Image sets (source_root):")
for f in sorted((repo / "datasets").glob("*/*/*.set.json")):
    if f.name.startswith("._"):
        continue
    meta = json.loads(f.read_text(encoding="utf-8"))
    old = meta.get("source_root", "")
    p = source_path(fake, old)
    if p.is_dir() and p.drive != root.drive:  # e.g. still on D: - use the copy on the shared drive if there is one
        alt = source_path(fake, "/" + Path(p).relative_to(p.anchor).as_posix())
        p = alt if alt.is_dir() else p
    if p.is_dir():
        meta["source_root"] = source_to_store(fake, p)
        f.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    say(f"   {f.relative_to(repo)}: {old}  ->  {meta['source_root']}  [{'OK ' + str(p) if p.is_dir() else 'NOT FOUND'}]")

# 3. the pipeline
def run(args):
    cmd = [sys.executable, "-u", str(repo / "scripts" / "claude_run.py")] + args
    say("\n$ main.py " + " ".join(args))
    p = subprocess.Popen(cmd, cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
    for line in p.stdout:
        print(line, end="", flush=True); log.write(line); log.flush()
    rc = p.wait(); say(f"[exit {rc}]")
    return rc
say("\n3. Labeled items (only lane labels marked done are used by the runs):")
for region, split in (("US", "dev"), ("US", "test"), ("CN", "dev"), ("CN", "test")):
    run(["lane", "items", "--region", region, "--split", split])
if "--no-api" not in sys.argv:
    say("\nSmoke test: tests A, B, C on 2 US development images each (real API, a few cents)")
    for t in ("A", "B", "C"):
        run(["lane", "run", "--test", t, "--region", "US", "--split", "dev", "--prompt", "lane_v2", "--real", "--limit", "2"])
    run(["lane", "runs"])
say("\nALL DONE")
