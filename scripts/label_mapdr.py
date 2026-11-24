"""One click for the China (MapDR) labeling: build the workspace once, then open the labeling tool in the browser.
Everything printed is also written to results/claude_logs/label_mapdr.log."""
import os, subprocess, sys
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
log = open(repo / "results" / "claude_logs" / "label_mapdr.log", "a", encoding="utf-8")
def say(msg):
    print(msg, flush=True); log.write(msg + "\n"); log.flush()
root = ""
for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
    k, _, v = line.partition("=")
    if k.strip() == "DATASETS_ROOT" and v.strip():
        root = v.strip().strip('"')
if not root:
    say("DATASETS_ROOT is not set in .env"); sys.exit(1)
root = str((repo / root).resolve())   # relative values (e.g. ../数据集) are relative to the project folder
images, ws = Path(root) / "mapdr", Path(root) / "mapdr_ws"
if not images.exists():
    say(f"MapDR images not found in {images}: run scripts/claude_fetch_mapdr.bat first"); sys.exit(1)
main = [sys.executable, str(repo / "main.py"), "label", "--data", str(ws)]
if not (ws / "workspace.json").exists():
    say(f"Step 1/2: building the MapDR workspace in {ws} (once) ...")
    r = subprocess.run(main + ["images", "init", "mapdr", "--source", str(images)], cwd=repo,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    say(r.stdout.strip()); say(r.stderr.strip())
    if r.returncode != 0:
        say("Building the workspace failed (see above)."); sys.exit(1)
else:
    say(f"Step 1/2: workspace {ws} already built, skipped.")
say("Step 2/2: opening the labeling tool (the browser opens http://127.0.0.1:8765; close this window to stop it) ...")
log.close()
sys.exit(subprocess.call(main + ["label"] + sys.argv[1:], cwd=repo))
