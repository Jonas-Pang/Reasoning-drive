"""Written by Claude. One click for the US (BDD100K) labeling: point the existing workspace DATASETS_ROOT\bdd100k at the
BDD100K images on this PC (the workspace was built on a Mac), then open the labeling tool in the browser.
Labels already made are kept. Everything printed is also written to results/claude_logs/label_bdd.log."""
import subprocess, sys
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
(repo / "results" / "claude_logs").mkdir(parents=True, exist_ok=True)
log = open(repo / "results" / "claude_logs" / "label_bdd.log", "a", encoding="utf-8")
def say(msg):
    print(msg, flush=True); log.write(msg + "\n"); log.flush()
env = {}
for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
    k, _, v = line.partition("=")
    if k.strip() in ("DATASETS_ROOT", "DATA_DIR") and v.strip():
        env[k.strip()] = v.strip().strip('"')
if "DATASETS_ROOT" not in env:
    say("DATASETS_ROOT is not set in .env"); sys.exit(1)
root = (repo / env["DATASETS_ROOT"]).resolve()   # relative values (e.g. ../数据集) are relative to the project
ws = root / "bdd100k"
cands = [(repo / env["DATA_DIR"]).resolve() / "extracted" / "bdd100k" / "mirror" / "val"] if "DATA_DIR" in env else []
cands += [repo / "data" / "extracted" / "bdd100k" / "mirror" / "val",
          repo.parent / "Reasning_Drive" / "data" / "extracted" / "bdd100k" / "mirror" / "val"]
src = next((p for p in cands if (p / "img").is_dir()), None)
if src is None:
    say("BDD100K images not found in: " + "; ".join(map(str, cands))); sys.exit(1)
main = [sys.executable, str(repo / "main.py"), "label", "--data", str(ws)]
say(f"Step 1/2: workspace {ws}, images {src} ...")
r = subprocess.run(main + ["images", "init", "bdd100k", "--source", str(src)], cwd=repo,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
say(r.stdout.strip()); say(r.stderr.strip())
if r.returncode != 0:
    say("Setting the image folder failed (see above)."); sys.exit(1)
say("Step 2/2: opening the labeling tool at http://127.0.0.1:8766 (port 8766, so it can run next to the China tool on 8765; close this window to stop it) ...")
log.close()
sys.exit(subprocess.call(main + ["label", "--port", "8766"] + sys.argv[1:], cwd=repo))
