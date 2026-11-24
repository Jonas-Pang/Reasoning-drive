"""Download the images of each country's label collections (datasets/<CODE>/dataset.yaml: fetch).

Only what the lane task needs is fetched where the host allows it: from a large zip on Google Drive the candidate frames
(datasets/<CODE>/candidates_geodrive.csv) are read one by one with byte-range requests, so 488 London frames come out
of a 57 GB archive without downloading it. Small archives are downloaded whole. Datasets behind a registration or a
licence form (Waymo, nuScenes, IDD, CoVLA) are listed with what the user has to do; nothing is accepted on their behalf.

    python main.py data status [CODES]                  what is there, what is missing, what needs the user
    python main.py data fetch [CODES] --root F:/datasets download what can be downloaded into <root>/<collection>/
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import tarfile
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from .. import paths as P

DRIVE = "https://drive.usercontent.google.com/download?id={id}&export=download&confirm=t"
LOG = "fetch_log.json"  # <root>/<collection>/fetch_log.json


def collections(repo, codes: list[str] | None = None) -> list[dict]:
    want = {c.upper() for c in codes} if codes else None
    out = []
    for f in sorted((Path(repo) / P.DATASETS).glob("*/dataset.yaml")):
        y = P.read_yaml(f) or {}
        code = str(y.get("region") or f.parent.name)
        if want and code.upper() not in want:
            continue
        for c in y.get("collections") or []:
            if c.get("fetch") or c.get("access"):
                out.append({**c, "region": code, "folder": f.parent})
    return out


def candidates(repo, col: dict) -> list[str]:
    f = Path(repo) / col["candidates"] if col.get("candidates") else None
    if not f or not f.exists():
        return []
    with open(f, encoding="utf-8") as h:
        return [r["rel"] for r in csv.DictReader(h) if r.get("collection", col["name"]) == col["name"]]


class HttpFile(io.RawIOBase):
    """A file on a web server that answers byte-range requests, opened read-only and seekable (for zipfile)."""

    def __init__(self, url: str, session=None, block: int = 1 << 20):
        import requests
        self.url, self.s, self.block = url, session or requests.Session(), block
        r = self.s.get(url, headers={"Range": "bytes=0-0"}, timeout=120)
        if r.status_code != 206 or "Content-Range" not in r.headers:
            raise OSError(f"the server does not answer byte ranges (HTTP {r.status_code})")
        self.size = int(r.headers["Content-Range"].rsplit("/", 1)[1])
        self.pos, self.buf_start, self.buf = 0, -1, b""
        self.requests = 1

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else self.pos + off if whence == 1 else self.size + off
        return self.pos

    def _fetch(self, start: int, end: int) -> bytes:
        for attempt in range(5):
            try:
                r = self.s.get(self.url, headers={"Range": f"bytes={start}-{end}"}, timeout=300)
                if r.status_code == 206:
                    self.requests += 1
                    return r.content
                raise OSError(f"HTTP {r.status_code}")
            except Exception:  # noqa: BLE001  a dropped connection: try again
                if attempt == 4:
                    raise
                time.sleep(3 * (attempt + 1))
        return b""

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.size - self.pos
        n = min(n, self.size - self.pos)
        if n <= 0:
            return b""
        in_buf = self.buf_start <= self.pos and self.pos + n <= self.buf_start + len(self.buf)
        if not in_buf:
            if n > self.block:  # a large read (a central directory, a big member): one request of that size
                data = self._fetch(self.pos, self.pos + n - 1)
                self.pos += len(data)
                return data
            self.buf_start = self.pos
            self.buf = self._fetch(self.pos, min(self.size, self.pos + self.block) - 1)
        i = self.pos - self.buf_start
        data = self.buf[i:i + n]
        self.pos += len(data)
        return data

    def readinto(self, b):
        data = self.read(len(b))
        b[:len(data)] = data
        return len(data)


def _key(path: str, depth: int) -> str:
    return "/".join(path.replace("\\", "/").strip("/").split("/")[-depth:])


def zip_members(url: str, want: list[str], dest: Path, log=print, session=None) -> dict:
    """Extract from a remote zip the members whose last path parts equal a wanted relative path (train/<id>/0.jpg
    matches images/train/<id>/0.jpg). Frames already on disk are skipped."""
    hf = HttpFile(url, session)
    z = zipfile.ZipFile(hf)
    by_depth = {}
    for rel in want:
        by_depth.setdefault(len(rel.strip("/").split("/")), {})[_key(rel, 99)] = rel
    found, written = 0, 0
    for info in z.infolist():
        for depth, keys in by_depth.items():
            rel = keys.get(_key(info.filename, depth))
            if rel is None:
                continue
            found += 1
            target = dest / rel
            if target.exists() and target.stat().st_size == info.file_size:
                break
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(info))
            written += 1
            if written % 50 == 0:
                log(f"    {written} frames written")
            break
    return {"archive_bytes": hf.size, "members": len(z.infolist()), "matched": found, "written": written,
            "requests": hf.requests}


def download(url: str, target: Path, log=print, session=None) -> Path:
    """A whole file, resumed with a byte range if a partial download is there."""
    import requests
    s = session or requests.Session()
    part = target.with_name(target.name + ".part")
    target.parent.mkdir(parents=True, exist_ok=True)
    have = part.stat().st_size if part.exists() else 0
    headers = {"Range": f"bytes={have}-"} if have else {}
    with s.get(url, headers=headers, stream=True, timeout=300) as r:
        if r.status_code not in (200, 206):
            raise OSError(f"HTTP {r.status_code} for {url}")
        if r.status_code == 200:
            have = 0
        total = have + int(r.headers.get("Content-Length", 0))
        last = time.time()
        with open(part, "ab" if have else "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)
                have += len(chunk)
                if time.time() - last > 30:
                    log(f"    {target.name}: {have / 1e9:.2f} / {total / 1e9:.2f} GB")
                    last = time.time()
    part.replace(target)
    return target


def tar_members(tar: Path, want: list[str], dest: Path) -> dict:
    keys = {_key(r, 99): r for r in want}
    depth = {len(r.strip("/").split("/")) for r in want}
    found = written = 0
    with tarfile.open(tar) as t:
        for m in t:
            if not m.isfile():
                continue
            rel = next((keys[k] for k in (_key(m.name, d) for d in depth) if k in keys), None)
            if rel is None:
                continue
            found += 1
            target = dest / rel
            if target.exists() and target.stat().st_size == m.size:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with t.extractfile(m) as src:
                target.write_bytes(src.read())
            written += 1
    return {"matched": found, "written": written}


def _sha(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def status(repo, root: Path | None, codes: list[str] | None = None) -> list[dict]:
    rows = []
    for col in collections(repo, codes):
        want = candidates(repo, col)
        dest = Path(root) / col["name"] if root else None
        have = sum(1 for r in want if dest and (dest / r).exists())
        rows.append({"region": col["region"], "collection": col["name"], "candidates": len(want), "on_disk": have,
                     "access": col.get("access", "open"), "how": col.get("access_note", ""),
                     "auto": bool(col.get("fetch")) and col.get("access", "open") == "open"})
    return rows


def fetch(repo, root: Path, codes: list[str] | None = None, log=print) -> list[dict]:
    """Fetch every collection whose source is open; collections behind a form are reported, not fetched."""
    import requests
    s = requests.Session()
    s.headers["User-Agent"] = "reasoning-drive dataset fetch (python-requests)"
    out = []
    for col in collections(repo, codes):
        name, want = col["name"], candidates(repo, col)
        dest = Path(root) / name
        if col.get("access", "open") != "open" or not col.get("fetch"):
            out.append({"collection": name, "status": "needs the user", "how": col.get("access_note", "")})
            log(f"{col['region']} {name}: needs the user — {col.get('access_note', '')}")
            continue
        dest.mkdir(parents=True, exist_ok=True)
        logf = dest / LOG
        record = json.loads(logf.read_text(encoding="utf-8")) if logf.exists() else {}
        missing = [r for r in want if not (dest / r).exists()]
        log(f"{col['region']} {name}: {len(want)} candidate frames, {len(missing)} missing")
        for step in col["fetch"]:
            label = step.get("name") or step.get("file_id")
            url = step.get("url") or DRIVE.format(id=step["file_id"])
            try:
                if step["kind"] == "zip_members":
                    if not missing:
                        continue
                    res = zip_members(url, missing, dest, log, s)
                elif step["kind"] == "file":
                    target = dest / "raw" / step["name"]
                    if target.exists() and not step.get("refresh"):
                        continue
                    download(url, target, log, s)
                    res = {"file": str(target), "bytes": target.stat().st_size, "sha256": _sha(target)}
                    if step.get("extract_candidates") and target.suffix == ".tar":
                        res.update(tar_members(target, missing, dest))
                    elif step.get("extract_all") and target.suffix == ".zip":
                        with zipfile.ZipFile(target) as z:
                            z.extractall(dest / step.get("extract_to", "."))
                        res["extracted"] = True
                else:
                    raise ValueError(f"unknown fetch kind {step['kind']}")
            except Exception as e:  # noqa: BLE001  the next step or collection may still work
                res = {"error": f"{type(e).__name__}: {e}"}
                log(f"  {label}: ERROR {res['error']}")
            else:
                log(f"  {label}: {res}")
            record[label] = {**res, "url": url, "time_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
            logf.write_text(json.dumps(record, indent=2), encoding="utf-8")
            missing = [r for r in want if not (dest / r).exists()]
        have = len(want) - len(missing)
        out.append({"collection": name, "status": "done" if not missing else "partial", "frames": have, "of": len(want)})
        log(f"{col['region']} {name}: {have} of {len(want)} candidate frames in {dest}")
    return out
