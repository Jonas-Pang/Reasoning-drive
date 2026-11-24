"""Written by Claude: download MapDR-mini (Amap / XJTU, CVPR 2025, CC BY-NC-SA 4.0) from ModelScope into
<DATASETS_ROOT>/mapdr/<category>__<clip>/ (frames + data.json), one folder per clip for reader: folder.
Log: results/claude_logs/fetch_mapdr.log"""
import json, os, time, urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
repo = Path(__file__).resolve().parent.parent
env = {}
for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
    k, _, v = line.partition("=")
    if v.strip() and not k.strip().startswith("#"):
        env[k.strip().upper()] = v.strip().strip('"')
root = Path(env.get("DATASETS_ROOT", r"F:\数据集")) / "mapdr"
try:
    import truststore; truststore.inject_into_ssl()
except Exception:
    pass
import requests
API = "https://modelscope.cn/api/v1/datasets/MIV-XJTU/MapDR-mini/repo"
s = requests.Session()
def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
files, page = [], 1
while True:
    r = s.get(API + "/tree", params={"Revision": "master", "Root": "/", "Recursive": "true", "PageNumber": page, "PageSize": 1000}, timeout=120)
    f = (r.json().get("Data") or {}).get("Files") or []
    files += [x for x in f if x.get("Type") != "tree" and x.get("Size", 0) > 0 and x["Path"].startswith("mapdr_mini/")]
    if len(f) < 1000: break
    page += 1
log(f"{len(files)} files, {sum(x['Size'] for x in files)/1e9:.2f} GB")
def target(p):
    parts = p.split("/")            # mapdr_mini/<cat>/<clip>/(img/<frame>.jpg | data.json)
    return root / f"{parts[1]}__{parts[2]}" / parts[-1]
def get(x):
    t = target(x["Path"])
    if t.exists() and t.stat().st_size == x["Size"]:
        return 0
    t.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(5):
        try:
            r = s.get(API, params={"Revision": "master", "FilePath": x["Path"]}, timeout=300)
            r.raise_for_status()
            t.write_bytes(r.content); return 1
        except Exception as e:
            time.sleep(3 * (attempt + 1))
    log("FAILED", x["Path"]); return 0
done = 0
with ThreadPoolExecutor(8) as ex:
    for i, n in enumerate(ex.map(get, files), 1):
        done += n
        if i % 500 == 0: log(f"{i}/{len(files)} checked, {done} written")
clips = sorted({p.name for p in root.iterdir() if p.is_dir()})
(root / "fetch_log.json").write_text(json.dumps({"source": "modelscope MIV-XJTU/MapDR-mini", "files": len(files),
    "clips": len(clips), "licence": "CC BY-NC-SA 4.0", "time": time.ctime()}, indent=2), encoding="utf-8")
log(f"MapDR-mini: {len(clips)} clips in {root}. Finished")
