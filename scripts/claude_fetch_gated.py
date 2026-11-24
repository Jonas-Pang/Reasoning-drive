"""Written by Claude: fetch the candidate frames of the registered datasets.
  CoVLA (JP)   : videos of the candidate scenes from Hugging Face (HF token from .env), frames cut at 2 Hz (index i -> video frame i*10)
  nuScenes (SG): samples/CAM_FRONT frames from the keyframe archive Chrome downloaded to Downloads
  IDD (IN)     : primary/dX/leftCamImgs frames from the IDD Multimodal Primary archive in Downloads
Log: results/claude_logs/fetch_gated.log (unbuffered)."""
import csv, os, re, sys, tarfile, time, zipfile, json
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
env = {}
for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
    k, _, v = line.partition("=")
    if v.strip() and not k.strip().startswith("#"):
        env[k.strip().upper()] = v.strip().strip('"')
root = Path(env.get("DATASETS_ROOT", r"F:\数据集"))
downloads = Path(os.path.expanduser("~")) / "Downloads"
only = set(a.upper() for a in sys.argv[1:]) or {"JP", "SG", "IN"}
try:
    import truststore; truststore.inject_into_ssl()
except Exception:
    pass
import requests

def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)

def cands(code):
    with open(repo / "datasets" / code / "candidates_geodrive.csv", encoding="utf-8") as f:
        return [r["rel"] for r in csv.DictReader(f)]

def wait_for(patterns, max_hours=6):
    """Wait until a finished download matching one of the patterns is in Downloads."""
    t0 = time.time()
    while time.time() - t0 < max_hours * 3600:
        for p in sorted(downloads.iterdir(), key=lambda x: -x.stat().st_mtime):
            if p.suffix == ".crdownload" or not p.is_file():
                continue
            if any(re.search(pat, p.name, re.I) for pat in patterns):
                return p
        time.sleep(30)
    return None

def covla():
    want = cands("JP")
    scenes = sorted({r.split("/")[1] for r in want})
    dest = root / "covla"
    tok = env.get("HF_TOKEN")
    if not tok:
        log("JP: no HF_TOKEN in .env"); return
    import cv2
    s = requests.Session(); s.headers["Authorization"] = f"Bearer {tok}"
    done = 0
    for i, sc in enumerate(scenes, 1):
        frames = [r for r in want if r.split("/")[1] == sc]
        if all((dest / r).exists() for r in frames):
            done += len(frames); continue
        mp4 = dest / "raw" / "videos" / f"{sc}.mp4"
        mp4.parent.mkdir(parents=True, exist_ok=True)
        if not mp4.exists():
            url = f"https://huggingface.co/datasets/turing-motors/CoVLA-Dataset/resolve/main/videos/{sc}.mp4"
            for attempt in range(4):
                try:
                    with s.get(url, stream=True, timeout=300) as r:
                        r.raise_for_status()
                        part = mp4.with_suffix(".part")
                        with open(part, "wb") as f:
                            for ch in r.iter_content(1 << 20):
                                f.write(ch)
                    part.replace(mp4); break
                except Exception as e:
                    log(f"JP {sc}: retry {attempt+1}: {e}"); time.sleep(5)
        cap = cv2.VideoCapture(str(mp4))
        for r in frames:
            idx = int(Path(r).stem) * 10
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ok, img = cap.read()
            if ok:
                out = dest / r; out.parent.mkdir(parents=True, exist_ok=True)
                cv2.imencode(".jpg", img)[1].tofile(str(out)); done += 1
        cap.release()
        if i % 10 == 0:
            log(f"JP covla: {i}/{len(scenes)} scenes, {done} frames")
    log(f"JP covla: {done} of {len(want)} candidate frames in {dest}")

def from_archive(code, coll, patterns, extra_prefix=None, extra_max=0):
    want = cands(code)
    dest = root / coll
    arc = wait_for(patterns)
    if not arc:
        log(f"{code}: no finished download matching {patterns} in {downloads}"); return
    log(f"{code}: reading {arc.name} ({arc.stat().st_size/1e9:.2f} GB)")
    keys = {r.replace("\\", "/"): r for r in want}
    found = extra = 0
    def take(name):
        n = name.replace("\\", "/")
        for k in keys:
            if n.endswith(k):
                return keys[k]
        if extra_prefix and re.search(extra_prefix, n):
            return "extra/" + n.split("/")[-1]
        return None
    if tarfile.is_tarfile(arc):
        with tarfile.open(arc) as t:
            for m in t:
                if not m.isfile():
                    continue
                rel = take(m.name)
                if not rel or (rel.startswith("extra/") and extra >= extra_max):
                    continue
                out = dest / rel; out.parent.mkdir(parents=True, exist_ok=True)
                with t.extractfile(m) as src:
                    out.write_bytes(src.read())
                if rel.startswith("extra/"): extra += 1
                else: found += 1
    else:
        with zipfile.ZipFile(arc) as z:
            for info in z.infolist():
                rel = take(info.filename)
                if not rel or (rel.startswith("extra/") and extra >= extra_max):
                    continue
                out = dest / rel; out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(z.read(info))
                if rel.startswith("extra/"): extra += 1
                else: found += 1
    (dest / "fetch_log.json").write_text(json.dumps({"archive": str(arc), "candidates": len(want), "found": found,
                                                     "extra": extra, "time": time.ctime()}, indent=2), encoding="utf-8")
    log(f"{code} {coll}: {found} of {len(want)} candidate frames, {extra} extra frames, in {dest}")

if "JP" in only: covla()
if "SG" in only: from_archive("SG", "nuscenes_sg", [r"trainval.*keyframe.*\.tgz$", r"keyframes.*\.tgz$"],
                              extra_prefix=r"samples/CAM_FRONT/n015-", extra_max=150)
if "IN" in only: from_archive("IN", "idd", [r"multimodal.*primary", r"idd.*primary", r"primary.*\.(zip|tar|tgz|tar\.gz)$"])
log("Finished")
