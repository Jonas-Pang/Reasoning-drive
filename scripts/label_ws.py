"""Written by Claude: run the labeling tool on one workspace under DATASETS_ROOT (from .env), so VS Code tasks need no
personal paths.   python scripts/label_ws.py <workspace> <label arguments...>   ({root} in an argument = DATASETS_ROOT)
                  python scripts/label_ws.py --combine <workspace> <workspace> ...
Examples: label_ws.py mapdr_ws images init mapdr --source {root}/mapdr     label_ws.py mapdr_ws label"""
import os, subprocess, sys
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
root = os.environ.get("DATASETS_ROOT", "")
env_file = repo / ".env"
if not root and env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        k, _, v = line.partition("=")
        if k.strip() == "DATASETS_ROOT" and v.strip():
            root = v.strip().strip('"')
if not root:
    sys.exit("Set DATASETS_ROOT in .env (the folder that holds the labeling workspaces).")
root = str((repo / root).resolve())   # relative values (e.g. ../数据集) are relative to the project folder
args = sys.argv[1:]
if not args:
    sys.exit(__doc__)
if args[0] == "--combine":
    cmd = ["label", "combine"] + [str(Path(root) / n) for n in args[1:]]
else:
    ws, rest = args[0], [a.replace("{root}", root) for a in args[1:]]
    cmd = ["label", "--data", str(Path(root) / ws)] + rest
print("python main.py " + " ".join(cmd), flush=True)
sys.exit(subprocess.call([sys.executable, str(repo / "main.py")] + cmd, cwd=repo))
