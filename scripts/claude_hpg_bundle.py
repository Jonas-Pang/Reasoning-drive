"""Written by Claude, 2026-11-16: pack the project for HiPerGator (hpg/README.md).

    python scripts/claude_hpg_bundle.py        -> ../reasoning_drive_hpg.zip  (next to the project folder)

Contents: reasoning_drive_hpg/Reasoning_Drive (the project without .env, keys, the Python environment, data/, caches,
run results and Claude's logs) and reasoning_drive_hpg/datasets_ws (the MapDR and BDD100K labeling workspaces: the
selected frames and their index). A fresh .env in the bundle points DATASETS_ROOT at ../datasets_ws; it holds no key
(the Gemma runs on HiPerGator need none)."""
import os
import sys
import zipfile
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
out = repo.parent / "reasoning_drive_hpg.zip"


def datasets_root() -> Path:
    v = ""
    for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
        k, _, val = line.partition("=")
        if k.strip() == "DATASETS_ROOT":
            v = val.strip().strip('"')
    p = Path(v)
    return p if p.is_absolute() else (repo / p).resolve()


SKIP_DIRS = {".venv", "venv", "__pycache__", ".git", ".ipynb_checkpoints", ".pytest_cache", ".vscode", "data",
             "hpg_logs", "node_modules"}
SKIP_PATHS = {"results/runs", "results/claude_logs", "results/carla", "regulations/inbox"}
SKIP_FILES = {".env", "desktop.ini", "Thumbs.db", ".DS_Store", "labeling_tool.lock"}
MAX_BYTES = 50 * 1024 * 1024


def keep(rel: str, name: str, size: int) -> bool:
    if name in SKIP_FILES or name.startswith("._") or size > MAX_BYTES:
        return False
    if name.startswith("claude_") and name.endswith(".bat"):     # Windows helpers with this computer's paths
        return False
    return True


n = 0
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(repo):
        rel_root = Path(root).relative_to(repo).as_posix()
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and
                   (f"{rel_root}/{d}".lstrip("./") if rel_root != "." else d) not in SKIP_PATHS]
        for f in files:
            p = Path(root) / f
            rel = p.relative_to(repo).as_posix()
            if keep(rel, f, p.stat().st_size):
                z.write(p, f"reasoning_drive_hpg/Reasoning_Drive/{rel}")
                n += 1
    z.writestr("reasoning_drive_hpg/Reasoning_Drive/.env",
               "# HiPerGator bundle (scripts/claude_hpg_bundle.py). No key needed for the Gemma runs.\n"
               "DATASETS_ROOT=../datasets_ws\nDATA_DIR=../data\n")
    root_ds = datasets_root()
    for ws in ("mapdr_ws", "bdd100k"):
        base = root_ds / ws
        if not base.is_dir():
            sys.exit(f"Workspace not found: {base}")
        for root, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for f in files:
                p = Path(root) / f
                if keep("", f, p.stat().st_size):
                    z.write(p, f"reasoning_drive_hpg/datasets_ws/{ws}/{p.relative_to(base).as_posix()}")
                    n += 1
print(f"{n} files -> {out} ({out.stat().st_size / 1e6:.1f} MB)")
print("Next: upload it in Open OnDemand (Files) to /blue/<group>/<you>/ and follow hpg/README.md.")
