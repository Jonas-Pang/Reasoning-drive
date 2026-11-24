"""Written by Claude: run main.py with DATASETS_ROOT from .env and the Windows certificate store (truststore),
so sites behind a local HTTPS inspector (self-signed certificate in chain) can be reached."""
import os, subprocess, sys
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
os.chdir(repo)
sys.path.insert(0, str(repo))
env = repo / ".env"
if env.exists():
    for line in env.read_text(encoding="utf-8").splitlines():
        k, _, v = line.partition("=")
        if k.strip() in ("DATASETS_ROOT", "DATA_DIR", "HF_TOKEN") and v.strip() and not os.environ.get(k.strip()):
            os.environ[k.strip()] = v.strip().strip('"')
for k in ("DATASETS_ROOT", "DATA_DIR"):   # relative values (e.g. ../../数据集) are relative to the project folder
    if os.environ.get(k) and not os.path.isabs(os.environ[k]):
        os.environ[k] = str((repo / os.environ[k]).resolve())
try:
    import truststore
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "-q", "truststore"])
    try:
        import truststore
    except ImportError:
        truststore = None
if truststore:
    truststore.inject_into_ssl()
    print("truststore: using the system certificate store", flush=True)
from reasoning_drive.cli import main
main(sys.argv[1:])
