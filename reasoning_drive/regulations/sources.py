"""Download each country's regulation documents and extract them in one go.

Every country lists its documents in regulations/<CODE>/region.yaml under `documents:` (official URL, where the file
is kept, which pages to read). A state or territory that copies a national model law names it with `parent:` and
compares its document with the parent's (`same_as`), so only what it changed is sent to the model.

    python main.py regulations fetch [CODE ...]                      download what is missing into regulations/inbox/<CODE>/
    python main.py regulations extract-all [CODE ...] [--real] [--budget 5]
                                                                     extract every downloaded document not extracted yet
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

from .. import paths as P

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
LOG = "sources_log.json"  # regulations/inbox/sources_log.json: what was downloaded from where, when, and its checksum


def _sha(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def documents(repo, codes: list[str] | None = None) -> list[dict]:
    """The documents of every country (or of the countries named), parents before their states."""
    regs = P.regions(repo)
    want = {c.upper() for c in codes} if codes else None
    out = []
    for code, (d, y) in regs.items():
        if want and code.upper() not in want:
            continue
        docs = y.get("documents") or []
        for doc in docs:
            if not doc.get("tag") or not doc.get("file"):
                raise ValueError(f"regulations/{d.name}/region.yaml: every document needs a tag and a file")
            out.append({**doc, "code": code, "name": y.get("name", code), "driving_side": y.get("driving_side", "right"),
                        "language": doc.get("language") or (y.get("standard") or {}).get("language", "en"),
                        "parent": y.get("parent"), "several": len(docs) > 1, "folder": d})
    depth = {}

    def level(code, seen=()):
        if code in depth:
            return depth[code]
        parent = (regs.get(code, (None, {}))[1] or {}).get("parent")
        depth[code] = 0 if not parent or parent in seen else level(parent, seen + (code,)) + 1
        return depth[code]
    return sorted(out, key=lambda x: level(x["code"]))


def local_file(repo, doc: dict) -> Path | None:
    """The downloaded file of a document (its name without a suffix in region.yaml: the suffix is the type obtained)."""
    stem = Path(repo) / doc["file"]
    if stem.suffix.lower() in (".pdf", ".html", ".htm", ".rtf", ".txt", ".xml"):
        return stem if stem.exists() else None
    for suffix in (".pdf", ".html", ".rtf", ".txt", ".xml"):
        f = stem.with_name(stem.name + suffix)
        if f.exists():
            return f
    return None


def looks_right(data: bytes, kind: str) -> str:
    """'' if the bytes are the kind of document expected, else what is wrong (an error page instead of the law)."""
    head = data[:4096].lstrip().lower()
    if kind == "pdf":
        return "" if data[:5] == b"%PDF-" else "not a PDF"
    if kind == "rtf":
        return "" if head.startswith(b"{\\rtf") else "not an RTF document"
    if kind in ("html", "xml"):
        if b"<" not in head[:200]:
            return "not an HTML page"
        if len(data) < 15000:
            return f"only {len(data)} bytes (an error or cookie page?)"
        return ""
    return ""


def _get(url: str, timeout: int = 120) -> tuple[bytes, str]:
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/pdf,application/rtf,*/*;q=0.8",
                                               "Accept-Language": "en-GB,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310  official legislation sites from region.yaml
        return r.read(), r.geturl()


def _candidates(src: dict) -> list[tuple[str, str]]:
    """(url, type) pairs to try, in order: direct links, then a link found on an index page (find: {page, pattern});
    prefer_find: true puts the index page first (a register whose current version has a new address each time)."""
    direct = [(u["url"], u.get("type", "pdf")) for u in src.get("urls") or []]
    out = [] if src.get("prefer_find") else list(direct)
    find = src.get("find")
    if find:
        try:
            page, final = _get(find["page"])
            from urllib.parse import urljoin
            for m in re.finditer(find["pattern"], page.decode("utf-8", errors="replace"), flags=re.I):
                out.append((urljoin(final, m.group(1).replace("&amp;", "&")), find.get("type", "pdf")))
                break
        except Exception as e:  # noqa: BLE001  the direct links may still work
            out.append(("", f"index page {find['page']}: {type(e).__name__}: {e}"))
    return out + (direct if src.get("prefer_find") else [])


def fetch(repo, codes: list[str] | None = None, force: bool = False, log=print) -> list[dict]:
    """Download every document that is missing (or all with force). Each file is checked (a PDF is a PDF, an HTML page
    is not a cookie notice) before it replaces anything; what was obtained is written to regulations/inbox/sources_log.json."""
    repo = Path(repo)
    log_file = repo / P.REGULATIONS / "inbox" / LOG
    record = json.loads(log_file.read_text(encoding="utf-8")) if log_file.exists() else {}
    results = []
    for doc in documents(repo, codes):
        key = f"{doc['code']}:{doc['tag']}"
        have = local_file(repo, doc)
        if have and not force:
            results.append({"document": key, "status": "kept", "file": have.relative_to(repo).as_posix()})
            log(f"{key}: kept {have.relative_to(repo).as_posix()}")
            continue
        tried = []
        for url, kind in _candidates(doc):
            if not url:
                tried.append(kind)
                continue
            try:
                data, final = _get(url)
            except Exception as e:  # noqa: BLE001  try the next address
                tried.append(f"{url}: {type(e).__name__}: {e}")
                continue
            bad = looks_right(data, kind)
            if bad:
                tried.append(f"{url}: {bad}")
                continue
            stem = repo / doc["file"]
            target = stem if stem.suffix else stem.with_name(stem.name + "." + kind)
            target.parent.mkdir(parents=True, exist_ok=True)
            tmp = target.with_name(target.name + ".part")
            tmp.write_bytes(data)
            if have and have != target and have.exists():
                have.unlink()
            shutil.move(str(tmp), str(target))
            record[key] = {"url": url, "final_url": final, "file": target.relative_to(repo).as_posix(), "bytes": len(data),
                           "sha256": _sha(target), "time_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
            results.append({"document": key, "status": "downloaded", **record[key]})
            log(f"{key}: downloaded {len(data) / 1e6:.1f} MB from {url}")
            break
        else:
            results.append({"document": key, "status": "failed", "tried": tried})
            log(f"{key}: FAILED — " + " | ".join(tried))
        time.sleep(1.0)  # be polite to the registers
    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    return results


def _done(doc: dict, path: Path, mock: bool) -> bool:
    """Extracted already from this very file (same checksum), with no failed request, and for real unless mock."""
    d = doc["folder"]
    logf = d / "drafts" / f"{doc['tag']}_log.json" if doc["several"] else d / "extraction_log.json"
    if not logf.exists():
        return False
    try:
        rep = json.loads(logf.read_text(encoding="utf-8"))
    except ValueError:
        return False
    if rep.get("pdf") != path.name or rep.get("errors") or (rep.get("mock") and not mock):
        return False
    return not rep.get("file_sha256") or rep["file_sha256"] == _sha(path)


def adopt_untagged(doc: dict, path_of) -> None:
    """A country that had one document and now lists several: its earlier draft becomes drafts/<tag>.yaml of the
    document it was made from, so it is kept and not extracted again."""
    d = doc["folder"]
    old, log_old = d / "passages_draft.yaml", d / "extraction_log.json"
    if (d / "drafts").exists() or not old.exists() or not log_old.exists():
        return
    try:
        made_from = json.loads(log_old.read_text(encoding="utf-8")).get("pdf")
    except ValueError:
        return
    for other in doc["siblings"]:
        p = path_of(other)
        if p is not None and p.name == made_from:
            (d / "drafts").mkdir(exist_ok=True)
            shutil.copy2(old, d / "drafts" / f"{other['tag']}.yaml")
            shutil.copy2(log_old, d / "drafts" / f"{other['tag']}_log.json")
            return


def extract_all(repo, cfg: dict, codes: list[str] | None = None, mock: bool = True, budget: float = 5.0,
                max_cost: float = 1.0, log=print) -> list[dict]:
    """Extract every downloaded document that has not been extracted from the same file yet, parents first. Stops
    before a document whose estimate would take the total over the budget (USD)."""
    from .extract import extract
    repo = Path(repo)
    docs = documents(repo, codes)
    by_key = {f"{x['code']}:{x['tag']}": x for x in documents(repo)}
    for x in docs:
        x["siblings"] = [y for y in by_key.values() if y["code"] == x["code"]]
    spent, out = 0.0, []
    for doc in docs:
        key = f"{doc['code']}:{doc['tag']}"
        path = local_file(repo, doc)
        if path is None:
            out.append({"document": key, "status": "not downloaded"})
            log(f"{key}: not downloaded (python main.py regulations fetch {doc['code']})")
            continue
        if doc["several"]:
            adopt_untagged(doc, lambda o: local_file(repo, o))
        if _done(doc, path, mock):
            out.append({"document": key, "status": "done before"})
            log(f"{key}: extracted before from the same file")
            continue
        same_as = None
        if doc.get("same_as"):
            ref = by_key.get(doc["same_as"])
            same_as = local_file(repo, ref) if ref else None
            if same_as is None:
                out.append({"document": key, "status": f"waiting for {doc['same_as']}"})
                log(f"{key}: its reference {doc['same_as']} is not downloaded, skipped")
                continue
        left = budget - spent
        if not mock and left <= 0.01:
            out.append({"document": key, "status": "budget used up"})
            log(f"{key}: budget ${budget} used up, stopped")
            continue
        first, last = 1, None
        if doc.get("pages"):
            a, _, b = str(doc["pages"]).partition("-")
            first, last = int(a), int(b) if b else int(a)
        try:
            rep = extract(repo, cfg, path, doc["code"], doc["name"], doc["driving_side"], doc.get("title", ""),
                          source=doc.get("title", ""), mock=mock, first=first, last=last, log=log, language=doc["language"],
                          max_cost=min(max_cost, left), tag=doc["tag"] if doc["several"] else "",
                          keywords=doc.get("keywords"), min_hits=int(doc.get("min_hits", 2)), same_as=same_as,
                          same_threshold=float(doc.get("same_threshold", 0.85)), all_pages=bool(doc.get("all_pages")))
        except (ValueError, RuntimeError) as e:
            out.append({"document": key, "status": f"error: {e}"})
            log(f"{key}: Error: {e}")
            continue
        spent += rep.get("cost_usd", 0.0)
        out.append({"document": key, "status": "extracted", "passages": rep["passages"], "cost_usd": rep.get("cost_usd", 0.0),
                    "pages_read": len(rep["pages_read"]), "pages_same_as_reference": len(rep.get("pages_same_as_reference") or [])})
        log(f"{key}: {rep['passages']} passages, ${rep.get('cost_usd', 0.0)} (total ${round(spent, 4)})")
    return out
