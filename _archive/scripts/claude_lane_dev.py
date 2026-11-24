"""Written by Claude: run lane tests on the development images (real API, prompt lane_v3 unless --prompt is given), then list the lane runs.
Only images whose lane label is final ("done") are used. Log: results/claude_logs/lane_dev.log
    python scripts/claude_lane_dev.py US                     all dev images, tests A B C
    python scripts/claude_lane_dev.py US --limit 2           smoke test: 2 images per test (a few cents)
    python scripts/claude_lane_dev.py US --limit 2 --tests A"""
import argparse, subprocess, sys
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser()
ap.add_argument("region", nargs="?", default="US")
ap.add_argument("--limit", type=int, default=0, help="only the first N images per test (0 = all)")
ap.add_argument("--tests", default="A,B,C")
ap.add_argument("--split", default="dev")
ap.add_argument("--prompt", default="lane_v3", help="prompt folder under prompts/")
a = ap.parse_args()
logp = repo / "results" / "claude_logs" / "lane_dev.log"
logp.parent.mkdir(parents=True, exist_ok=True)
log = open(logp, "a", encoding="utf-8")
def run(args):
    cmd = [sys.executable, "-u", str(repo / "scripts" / "claude_run.py")] + args
    log.write("\n$ main.py " + " ".join(args) + "\n"); log.flush(); print("\n$ main.py " + " ".join(args), flush=True)
    p = subprocess.Popen(cmd, cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
    for line in p.stdout:
        print(line, end="", flush=True); log.write(line); log.flush()
    rc = p.wait(); log.write(f"[exit {rc}]\n"); log.flush()
    return rc
run(["lane", "items", "--region", a.region, "--split", a.split])
limit = ["--limit", str(a.limit)] if a.limit else []
for t in a.tests.split(","):
    run(["lane", "run", "--test", t.strip(), "--region", a.region, "--split", a.split, "--prompt", a.prompt, "--real"] + limit)
run(["lane", "runs"])
log.write("\nALL DONE\n"); log.close()
print("\nALL DONE. Log: " + str(logp))
