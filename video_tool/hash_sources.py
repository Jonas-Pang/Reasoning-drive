"""Add SHA-256 (and MD5, for comparison with published checksums) of every downloaded source file to
data_manifest.csv, including the archives downloaded by hand and the BDD100K mirror copy. The hashes are also
kept in data_hashes.csv, which playground.ipynb does not rewrite, so they survive a new run of the notebook and are
merged back into the manifest without hashing again.

    python -m video_tool hash-sources            # looks in DATA_DIR/raw (from .env), else <repo>/data/raw

Files are found by name anywhere under raw/. Files in raw/ that the manifest does not list are reported, so the
record can be completed. Nothing in raw/ is changed.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path

from .core import ToolError, _load_env_file, read_csv, utc_now, write_csv

NEW_COLUMNS = ["size_bytes", "sha256", "md5", "hashed_utc", "local_path"]
HASH_FILE = "data_hashes.csv"
HASH_COLUMNS = ["file"] + NEW_COLUMNS
SKIP = {".DS_Store"}


def _hashes(path: Path, chunk: int = 8 << 20) -> tuple[str, str]:
    sha, md5 = hashlib.sha256(), hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            sha.update(block)
            md5.update(block)
    return sha.hexdigest(), md5.hexdigest()


def hash_sources(repo: Path, raw: Path | None = None, log=print, rehash: bool = False, budget_s: float | None = None) -> dict:
    """Files already hashed with the same size are skipped unless rehash; with budget_s, no new file is started
    after that many seconds (run again to continue)."""
    import time
    t0 = time.time()
    repo = Path(repo)
    _load_env_file(repo / ".env")
    if raw is None:
        data = os.environ.get("DATA_DIR") or str(repo / "data")
        raw = Path(data).expanduser() / "raw"
    raw = Path(raw)
    if not raw.is_dir():
        raise ToolError(f"{raw} does not exist. Is the external drive connected? (DATA_DIR in .env)")
    manifest = repo / "data_manifest.csv"
    rows = read_csv(manifest)
    if not rows:
        raise ToolError(f"{manifest} is empty or missing.")
    files = {}
    for d in [raw] + [x for x in raw.iterdir() if not x.name.startswith("._") and x.is_dir()]:  # raw/<file> and raw/<source>/<file>
        for p in d.iterdir():                 # unpacked folders below are not downloads and are not walked
            if p.name.startswith("._") or p.name in SKIP or p.name.endswith(".meta.json") or not p.is_file():
                continue
            files[p.name] = p
    known = {h["file"]: h for h in read_csv(repo / HASH_FILE)}
    missing, done, left = [], 0, []
    for r in rows:
        h = known.get(r["file"])
        if h and not r.get("sha256"):
            r.update({k: h.get(k, "") for k in NEW_COLUMNS})  # hashed before; the manifest was rewritten since
        p = files.get(r["file"])
        if p is None:
            missing.append(r["file"])
            continue
        if not rehash and r.get("sha256") and str(r.get("size_bytes")) == str(p.stat().st_size):
            continue
        if budget_s is not None and time.time() - t0 > budget_s:
            left.append(r["file"])
            continue
        log(f"hashing {r['file']} ({p.stat().st_size / 1e9:.2f} GB) ...")
        sha, md5 = _hashes(p)
        r.update({"size_bytes": p.stat().st_size, "sha256": sha, "md5": md5, "hashed_utc": utc_now(),
                  "local_path": p.relative_to(raw.parent).as_posix()})
        done += 1
    listed = {r["file"] for r in rows}
    unlisted = sorted(n for n in files if n not in listed and not n.endswith((".part", ".done")))
    cols = list(rows[0].keys())
    cols += [c for c in NEW_COLUMNS if c not in cols]
    write_csv(manifest, rows, cols)
    for r in rows:
        if r.get("sha256"):
            known[r["file"]] = {k: r.get(k, "") for k in HASH_COLUMNS}
    write_csv(repo / HASH_FILE, sorted(known.values(), key=lambda h: h["file"]), HASH_COLUMNS)
    log(f"data_manifest.csv: {done} files hashed" + (f"; not found under {raw}: {', '.join(missing)}" if missing else "")
        + (f"; in raw/ but not in the manifest: {', '.join(unlisted)}" if unlisted else "")
        + (f"; still to hash (run again): {', '.join(left)}" if left else ""))
    return {"hashed": done, "missing": missing, "unlisted": unlisted, "left": left}
