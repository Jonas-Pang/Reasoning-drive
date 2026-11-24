"""A new country's marking standard (PDF) -> rule passages in the template of regulations/_template/.

    python main.py regulations extract --pdf regulations/inbox/uk_highway_code.pdf --code UK \
        --name "the United Kingdom" --driving-side left --title "The Highway Code (2024), rules 127-132" [--real]
    python main.py regulations accept UK

1. The text of every page is read with pypdf (a scanned PDF without a text layer needs OCR first).
2. Pages that mention lane markings (keywords in several languages, or --all-pages) are grouped, a few per request.
3. Each group is sent to the model of configs/api.yaml with the fixed prompt in prompts/regulation_extraction/ and a
   strict JSON schema. The answer lists passages: section, page, marking type, element, the original text, an English
   text and what the passage says about each movement.
4. Every quoted text is checked against the page it came from (verified_quote); passages the model may have
   reworded or invented are kept but marked, so they are easy to find when reading the draft.
5. regulations/<CODE>/passages_draft.yaml is written, with region.yaml (from the template) if the country is new.
   Nothing is used by the experiments until `regulations accept <CODE>` renames the draft to passages_lane.yaml.

With --mock (the default unless --real is given) no request is sent: the draft holds the sentences of the selected
pages that contain a keyword, so the whole procedure can be tried for free.
"""
from __future__ import annotations

import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from .. import paths as P
from .norms import NORMS, NORM_WORDS, propose

KEYWORDS = [
    # English
    "lane", "line", "marking", "arrow", "broken", "solid", "dashed", "centre", "center", "edge line", "overtak", "chevron",
    "hatch", "box junction", "give way", "stop line", "turn",
    # Chinese
    "车道", "标线", "实线", "虚线", "箭头", "导向", "跨越", "黄色", "白色", "停止线", "让行线",
    # German, French, Spanish, Portuguese, Italian, Dutch
    "fahrstreifen", "markierung", "linie", "pfeil", "voie", "ligne", "flèche", "marquage", "carril", "línea", "flecha",
    "marca vial", "faixa", "linha", "seta", "corsia", "striscia", "freccia", "rijstrook", "streep", "pijl",
    # Japanese, Korean
    "車線", "区画線", "矢印", "차선", "차로", "실선", "점선",
]
ELEMENTS = ["boundary", "lane_marking", "lane_type", "transverse", "area", "general"]
MOVES = ["cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"]
VALUES = ["allowed", "prohibited", "not_stated"]


def answer_schema() -> dict:
    passage = {
        "type": "object", "additionalProperties": False,
        "properties": {
            "section": {"type": "string"}, "page": {"type": "integer"}, "marking_type": {"type": "string"},
            "element": {"type": "string", "enum": ELEMENTS}, "text_original": {"type": "string"}, "text_en": {"type": "string"},
            "text_en_is_translation": {"type": "boolean"},
            "norm": {"type": "string", "enum": NORMS},
            "actions": {"type": "object", "additionalProperties": False, "required": MOVES,
                        "properties": {m: {"type": "string", "enum": VALUES} for m in MOVES}},
        },
        "required": ["section", "page", "marking_type", "element", "text_original", "text_en", "text_en_is_translation", "norm", "actions"],
    }
    return {"type": "object", "additionalProperties": False, "required": ["passages"],
            "properties": {"passages": {"type": "array", "items": passage}}}


# ------------------------------------------------------------------ PDF pages

def text_pages(text: str, size: int = 3000) -> list[str]:
    """A text document cut into pseudo-pages of about `size` characters, at paragraph ends."""
    paras = []
    for p in (p.strip() for p in re.split(r"\n\s*\n", text)):
        while len(p) > size:  # a paragraph longer than a page (a long table) is cut at a line end or a space
            cut = max(p.rfind("\n", 0, size), p.rfind(" ", 0, size), p.rfind("。", 0, size))
            cut = cut if cut > size // 2 else size
            paras.append(p[:cut].strip())
            p = p[cut:].strip()
        if p:
            paras.append(p)
    pages, cur = [], ""
    for para in paras:
        if cur and len(cur) + len(para) > size:
            pages.append(cur)
            cur = ""
        cur = (cur + "\n\n" + para).strip()
    if cur:
        pages.append(cur)
    return pages


def html_text(raw: str) -> str:
    """Plain text of an HTML or XML document: tags removed, block ends kept as line breaks."""
    import html
    raw = re.sub(r"(?is)<(script|style|ImageData)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"[A-Za-z0-9+/]{200,}={0,2}", " ", raw)  # embedded images (base64) are not text
    raw = re.sub(r"(?i)</?(p|div|br|li|tr|h\d|table|section|article|paragraph|item|sentence|tablerow|row|title)[^>]*>", "\n\n", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"[ \t]+", " ", html.unescape(raw))


def rtf_text(raw: str) -> str:
    """Plain text of an RTF document (some legislation registers publish the consolidated text only as RTF)."""
    out, stack, skip, i = [], [], False, 0
    destinations = ("fonttbl", "colortbl", "stylesheet", "info", "pict", "header", "footer", "themedata", "colorschememapping",
                    "datastore", "latentstyles", "listtable", "listoverridetable", "rsidtbl", "generator", "xmlnstbl", "mmathPr")
    tok = re.compile(r"\\([a-zA-Z]+)(-?\d+)? ?|\\'([0-9a-fA-F]{2})|\\([^a-zA-Z])|([{}])|[\r\n]+|([^\\{}\r\n]+)")
    for m in tok.finditer(raw):
        word, _arg, hexc, sym, brace, text = m.groups()
        if brace == "{":
            stack.append(skip)
        elif brace == "}":
            skip = stack.pop() if stack else False
        elif sym:
            if sym == "*":
                skip = True
            elif not skip and sym in "\\{}":
                out.append(sym)
        elif word:
            if word in destinations:
                skip = True
            elif not skip and word in ("par", "line", "sect", "page"):
                out.append("\n")
            elif not skip and word == "tab":
                out.append("\t")
        elif hexc and not skip:
            out.append(bytes.fromhex(hexc).decode("cp1252", errors="replace"))
        elif text and not skip:
            out.append(text)
        i += 1
    return re.sub(r"\n{3,}", "\n\n", "".join(out))


def read_pages(pdf: Path) -> list[str]:
    """The text of every page. A PDF is read page by page; a text, HTML, XML or RTF document (a law published on a web
    page or as a word-processor file) is cut into pseudo-pages of about 3,000 characters, so the rest works the same."""
    suffix = pdf.suffix.lower()
    if suffix in (".txt", ".md"):
        return text_pages(pdf.read_text(encoding="utf-8", errors="replace"))
    if suffix == ".rtf":
        return text_pages(rtf_text(pdf.read_text(encoding="latin-1", errors="replace")))
    if suffix in (".html", ".htm", ".xml"):
        return text_pages(html_text(pdf.read_text(encoding="utf-8", errors="replace")))
    from pypdf import PdfReader
    reader = PdfReader(str(pdf))
    out = []
    for page in reader.pages:
        try:
            out.append(page.extract_text() or "")
        except Exception:  # noqa: BLE001  a damaged page should not stop the others
            out.append("")
    return out


def _norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return re.sub(r"\s+", "", text)


def relevant_pages(pages: list[str], all_pages: bool = False, first: int = 1, last: int | None = None,
                   keywords: list[str] | None = None, min_hits: int = 2) -> list[int]:
    """1-based numbers of the pages to read: pages with at least min_hits keyword hits (or all with text). A long law in
    which "line", "lane" and "turn" are on almost every page can be given narrower keywords (e.g. "dividing line")."""
    last = last or len(pages)
    words = [k.lower() for k in (keywords or KEYWORDS)]
    keep = []
    for i in range(first, last + 1):
        t = (pages[i - 1] or "").lower()
        if not t.strip():
            continue
        if all_pages or sum(t.count(k) for k in words) >= min_hits:
            keep.append(i)
    return keep


def _flat(text: str) -> str:
    """Letters and digits only, lower case: two editions of the same rules compare equal whatever their line breaks,
    hyphens, quotes or page layout."""
    t = unicodedata.normalize("NFKC", text).lower()
    return re.sub(r"[^a-z0-9\u3040-\u30ff\u4e00-\u9fff]+", "", t)


def _lines(text: str) -> list[str]:
    """The lines of a page (flattened, 30+ characters): the unit compared with the reference document."""
    return [x for x in (_flat(line) for line in text.splitlines()) if len(x) >= 30]


def same_as_reference(page_numbers: list[int], pages: list[str], reference: list[str], threshold: float = 0.85) -> tuple[list[int], list[int]]:
    """(pages to read, pages skipped): a page is skipped when at least `threshold` of its lines occur word for word in
    the reference document, e.g. a state's road rules against the national model law they copy (headers, page numbers
    and the state's own notes make up the rest). Only what the state changed or added goes to the model; the rest
    comes from the reference country's passages (region.yaml: parent)."""
    ref = "\n".join(_flat(t) for t in reference)
    keep, skipped = [], []
    for n in page_numbers:
        lines = _lines(pages[n - 1])
        if lines and sum(1 for x in lines if x in ref) / len(lines) >= threshold:
            skipped.append(n)
        else:
            keep.append(n)
    return keep, skipped


def groups(page_numbers: list[int], pages: list[str], max_chars: int = 12000, max_pages: int = 6) -> list[list[int]]:
    out, cur, size = [], [], 0
    for n in page_numbers:
        n_chars = len(pages[n - 1])
        if cur and (size + n_chars > max_chars or len(cur) >= max_pages):
            out.append(cur)
            cur, size = [], 0
        cur.append(n)
        size += n_chars
    if cur:
        out.append(cur)
    return out


def page_block(numbers: list[int], pages: list[str]) -> str:
    return "\n\n".join(f"[page {n}]\n{pages[n - 1].strip()}" for n in numbers)


# ------------------------------------------------------------------ prompt and request

def prompt_parts(repo, meta: dict, block: str) -> dict:
    d = Path(repo) / P.PROMPTS / "regulation_extraction"
    role = (d / "role.txt").read_text(encoding="utf-8").strip()
    instr = (d / "instructions.txt").read_text(encoding="utf-8").strip()
    user = (d / "user.txt").read_text(encoding="utf-8").strip().format(pages=block, **meta)
    return {"instructions": role + "\n\n" + instr, "user_text": user, "schema": answer_schema()}


def build_request(cfg: dict, parts: dict, max_output_tokens: int = 8000) -> dict:
    from ..agent.client import _reasoning
    a = cfg["api"]
    payload = {"model": a["model"],
               "input": [{"role": a.get("instruction_role", "developer"), "content": [{"type": "input_text", "text": parts["instructions"]}]},
                         {"role": "user", "content": [{"type": "input_text", "text": parts["user_text"]}]}],
               "text": {"format": {"type": "json_schema", "name": "regulation_passages", "schema": parts["schema"], "strict": True}},
               "max_output_tokens": max_output_tokens}
    _reasoning(payload, a)
    if a.get("store") is not None:
        payload["store"] = bool(a["store"])
    return payload


def mock_passages(numbers: list[int], pages: list[str]) -> list[dict]:
    """Free stand-in for the model: sentences of the pages that contain a keyword (shows the procedure, not the model)."""
    out = []
    for n in numbers:
        for sent in re.split(r"(?<=[.。;；])\s*", pages[n - 1]):
            s = " ".join(sent.split())
            if 25 <= len(s) <= 400 and sum(s.lower().count(k) for k in KEYWORDS) >= 2:
                out.append({"section": f"p{n}-{len(out) + 1}", "page": n, "marking_type": "(mock)", "element": "general",
                            "text_original": s, "text_en": s, "text_en_is_translation": False,
                            "norm": propose(s, NORM_WORDS["en"])[0], "actions": {m: "not_stated" for m in MOVES}})
            if len(out) >= 40:
                return out
    return out


def estimate_cost(cfg: dict, chars: int, requests: int) -> float:
    from ..agent.runner import price_for
    price = price_for(cfg) or {}
    tokens_in = chars / 3.5 + 900 * requests
    tokens_out = 1500 * requests
    return round((tokens_in * float(price.get("input", 0)) + tokens_out * float(price.get("output", 0))) / 1e6, 4)


# ------------------------------------------------------------------ checks and the draft

def check_quote(p: dict, pages: list[str]) -> bool:
    """True when text_original appears on its page (or the page before/after), ignoring spaces, case and width forms."""
    q = _norm(p.get("text_original", ""))
    if len(q) < 8:
        return False
    n = int(p.get("page") or 0)
    near = " ".join(pages[i - 1] for i in (n - 1, n, n + 1) if 1 <= i <= len(pages))
    hay = _norm(near)
    if q in hay:
        return True
    pieces = [q[i:i + 20] for i in range(0, max(1, len(q) - 19), 20)]  # long quotes: most 20-character pieces must be there
    return bool(pieces) and sum(1 for x in pieces if x in hay) >= 0.8 * len(pieces)


def to_template(passages: list[dict], code: str, source: str, pages: list[str], language: str = "en", tag: str = "") -> list[dict]:
    """Passages in the template, with two checks: verified_quote (the original text is on its page) and norm_check
    (the force the model gave agrees with the standard's own words, norms.py). With a document tag (a country with
    several documents) the rule IDs carry it: UK-TSRGD-9.4.1."""
    words = NORM_WORDS.get("zh" if language in ("zh", "both") else language, NORM_WORDS["en"])
    out, used = [], set()
    prefix = f"{code}-{tag.upper()}" if tag else code
    for p in passages:
        sec = re.sub(r"\s+", "", str(p.get("section") or f"p{p.get('page')}")).strip(".") or "x"
        rid = f"{prefix}-{sec}"
        k = 1
        while rid in used:
            k += 1
            rid = f"{prefix}-{sec}-{k}"
        used.add(rid)
        out.append({"rule_id": rid, "region": code, "source": source, **({"document": tag} if tag else {}),
                    "section": str(p.get("section") or ""),
                    "page": int(p.get("page") or 0), "marking_type": p.get("marking_type", ""), "element": p.get("element", "general"),
                    "text_original": p.get("text_original", ""), "text_en": p.get("text_en", ""),
                    "text_en_is_translation": bool(p.get("text_en_is_translation")),
                    "norm": p.get("norm") if p.get("norm") in NORMS else "informative",
                    "actions_stated": {m: v for m, v in (p.get("actions") or {}).items() if v != "not_stated"},
                    "verified_quote": check_quote(p, pages)})
        word_norm, word = propose(p.get("text_original", ""), words)
        out[-1]["norm_check"] = "agrees" if word_norm == out[-1]["norm"] else f"words say {word_norm}" + (f" ({word})" if word else "")
    return out


def _dedupe(passages: list[dict]) -> list[dict]:
    seen, out = set(), []
    for p in passages:
        k = _norm(p.get("text_original", ""))[:120]
        if k and k not in seen:
            seen.add(k)
            out.append(p)
    return out


def write_region_if_new(repo, code: str, name: str, driving_side: str, title: str, pdf: Path, language: str) -> Path:
    d = Path(repo) / P.REGULATIONS / code
    d.mkdir(parents=True, exist_ok=True)
    f = d / "region.yaml"
    if not f.exists():
        tpl = (Path(repo) / P.REGULATIONS_TEMPLATE / "region.yaml").read_text(encoding="utf-8")
        body = tpl[tpl.index("code: XX"):]
        tpl = (f"# {name} ({code}): added by the regulation extractor from {pdf.name}. Check every field.\n\n" + body)
        try:
            pdf_rel = pdf.resolve().relative_to(Path(repo).resolve()).as_posix()
        except ValueError:
            pdf_rel = pdf.as_posix()
        tpl = (tpl.replace("code: XX ", f"code: {code} ").replace("name: Countryland ", f"name: {json.dumps(name)} ")
               .replace("driving_side: right ", f"driving_side: {driving_side} ").replace('title: ""', f"title: {json.dumps(title)}")
               .replace('source_pdf: ""', f"source_pdf: {json.dumps(pdf_rel)}").replace("language: en ", f"language: {language} ")
               .replace("marking: passages_marking.yaml", "marking: passages_lane.yaml")
               .replace("lane: [passages_marking.yaml, passages_lane.yaml]", "lane: [passages_lane.yaml]"))
        f.write_text(tpl, encoding="utf-8")
    _set_status(f, "draft", only_from=("planned",))
    return f


def _set_status(region_file: Path, status: str, only_from: tuple = ("planned", "draft")) -> None:
    """Change the status field of region.yaml (planned -> draft -> in use), keeping the rest of the file as it is."""
    txt = region_file.read_text(encoding="utf-8")
    m = re.search(r"(?m)^status:[ \t]*([A-Za-z ]+?)[ \t]*(#.*)?$", txt)
    if m and m.group(1).strip() in only_from:
        line = f"status: {status}".ljust(32) + (m.group(2) or "")
        region_file.write_text(txt[:m.start()] + line.rstrip() + txt[m.end():], encoding="utf-8")


DRAFTS = "drafts"  # regulations/<CODE>/drafts/<tag>.yaml: one draft per document of a country with several documents


def merge_drafts(d: Path) -> list[dict]:
    """passages_draft.yaml of a country with several documents: the drafts of all its documents, in name order."""
    import yaml
    items = []
    for f in sorted((d / DRAFTS).glob("*.yaml")):
        items += yaml.safe_load(f.read_text(encoding="utf-8")) or []
    return items


def _start_drafts(d: Path, first_tag: str) -> None:
    """Before the first document with a tag: a draft written earlier without one is kept as drafts/<first document>.yaml."""
    dd = d / DRAFTS
    if dd.exists() or not (d / "passages_draft.yaml").exists():
        dd.mkdir(parents=True, exist_ok=True)
        return
    dd.mkdir(parents=True, exist_ok=True)
    old = d / "passages_draft.yaml"
    log_old = d / "extraction_log.json"
    name = "base"
    if log_old.exists():
        try:
            name = re.sub(r"[^A-Za-z0-9_]+", "_", Path(json.loads(log_old.read_text(encoding="utf-8")).get("pdf", "base")).stem)[:40] or "base"
        except ValueError:
            pass
    if name == first_tag:
        name += "_earlier"
    (dd / f"{name}.yaml").write_text(old.read_text(encoding="utf-8"), encoding="utf-8")
    if log_old.exists():
        (dd / f"{name}_log.json").write_text(log_old.read_text(encoding="utf-8"), encoding="utf-8")


def extract(repo, cfg: dict, pdf: str | Path, code: str, name: str, driving_side: str = "right", title: str = "",
            source: str = "", mock: bool = True, all_pages: bool = False, first: int = 1, last: int | None = None,
            log=print, language: str = "en", max_cost: float = 2.0, tag: str = "", keywords: list[str] | None = None,
            min_hits: int = 2, same_as: str | Path | None = None, same_threshold: float = 0.85) -> dict:
    import yaml
    pdf = Path(pdf)
    if not pdf.exists():
        raise FileNotFoundError(f"{pdf} not found")
    code = code.upper()
    tag = re.sub(r"[^A-Za-z0-9_]+", "_", tag or "").strip("_")
    pages = read_pages(pdf)
    if not any(t.strip() for t in pages):
        raise ValueError(f"{pdf.name}: no text layer on any page (a scanned PDF needs OCR first).")
    nums = relevant_pages(pages, all_pages, first, last, keywords, min_hits)
    skipped = []
    if same_as:
        nums, skipped = same_as_reference(nums, pages, read_pages(Path(same_as)), same_threshold)
        log(f"{len(skipped)} pages are the same as {Path(same_as).name} and are not sent; {len(nums)} pages differ.")
    grp = groups(nums, pages)
    chars = sum(len(pages[n - 1]) for n in nums)
    meta = {"title": title or pdf.stem, "name": name, "code": code, "driving_side": driving_side}
    est = estimate_cost(cfg, chars, len(grp))
    log(f"{pdf.name}: {len(pages)} pages, {len(nums)} with lane-marking words, {len(grp)} requests, about ${est} "
        f"({'mock: no request is sent' if mock else 'model ' + cfg['api']['model']})")
    if not mock and est > max_cost:
        raise ValueError(f"The estimated cost ${est} is above the limit ${max_cost}. Read fewer pages (--pages 20-45), or allow it "
                         f"with --max-cost {round(est + 0.5, 1)}.")
    found, usage, errors = [], {"input_tokens": 0, "output_tokens": 0}, []
    for i, g in enumerate(grp, 1):
        if mock:
            found += mock_passages(g, pages)
            continue
        from ..agent.client import call_with_fallback
        parts = prompt_parts(repo, meta, page_block(g, pages))
        try:
            resp = call_with_fallback(cfg, build_request(cfg, parts))
            ans = json.loads(resp["text"])
            found += ans.get("passages") or []
            u = resp.get("usage") or {}
            usage["input_tokens"] += u.get("input_tokens", 0)
            usage["output_tokens"] += u.get("output_tokens", 0)
            log(f"  pages {g[0]}-{g[-1]}: {len(ans.get('passages') or [])} passages")
        except Exception as e:  # noqa: BLE001  one failed group should not lose the others
            errors.append(f"pages {g[0]}-{g[-1]}: {type(e).__name__}: {e}")
            log("  " + errors[-1])
    if errors and not found:
        raise RuntimeError(f"None of the {len(grp)} requests succeeded, so no draft was written (an earlier draft is kept). "
                           f"First error: {errors[0]}")
    items = to_template(_dedupe(found), code, source or title or pdf.stem, pages, language, tag)
    region_file = write_region_if_new(repo, code, name, driving_side, title or pdf.stem, pdf, language)
    d = Path(region_file).parent
    out = d / "passages_draft.yaml"
    head = (f"# DRAFT passages of {name} ({code}) from {pdf.name}, {datetime.now(timezone.utc):%Y-%m-%d} "
            f"({'mock' if mock else cfg['api']['model']}).\n"
            "# Read every passage against the PDF. verified_quote: false means the original text was not found on its page.\n"
            "# Delete what is not a rule for drivers, fix sections and texts, then:  python main.py regulations accept "
            f"{code}\n\n")
    body = yaml.safe_dump(items, allow_unicode=True, sort_keys=False, width=120)
    if tag:
        _start_drafts(d, tag)
        (d / DRAFTS / f"{tag}.yaml").write_text(head + body, encoding="utf-8")
        merged = merge_drafts(d)
        docs = sorted(f.stem for f in (d / DRAFTS).glob("*.yaml"))
        out.write_text(f"# DRAFT passages of {name} ({code}): the drafts of {len(docs)} documents ({', '.join(docs)}) in "
                       f"{DRAFTS}/, merged. Edit those files, not this one; each extraction writes this file again.\n"
                       f"# Then:  python main.py regulations accept {code}\n\n"
                       + yaml.safe_dump(merged, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    else:
        out.write_text(head + body, encoding="utf-8")
    from ..agent.runner import cost_of
    from .sources import _sha
    report = {"pdf": pdf.name, "file_sha256": _sha(pdf), "code": code, "document": tag, "pages": len(pages), "pages_read": nums,
              "pages_same_as_reference": skipped, "reference": Path(same_as).name if same_as else "", "requests": len(grp),
              "mock": mock, "passages": len(items), "verified_quotes": sum(1 for p in items if p["verified_quote"]), "errors": errors,
              "usage": usage, "cost_usd": 0.0 if mock else round(cost_of(cfg, usage), 4), "draft": str(out),
              "region_file": str(region_file), "time_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    if tag:
        (d / DRAFTS / f"{tag}_log.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        logs = [json.loads(f.read_text(encoding="utf-8")) for f in sorted((d / DRAFTS).glob("*_log.json"))]
        report_all = dict(report, pdf=", ".join(x.get("pdf", "") for x in logs), document="",
                          documents={x.get("document") or Path(x.get("pdf", "")).stem: x.get("passages", 0) for x in logs},
                          passages=len(merge_drafts(d)), errors=[e for x in logs for e in x.get("errors") or []],
                          mock=any(x.get("mock") for x in logs), cost_usd=round(sum(x.get("cost_usd", 0) for x in logs), 4))
        (d / "extraction_log.json").write_text(json.dumps(report_all, indent=2, ensure_ascii=False), encoding="utf-8")
    else:
        (d / "extraction_log.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"Draft: {out} ({len(items)} passages{' from ' + tag if tag else ''}, {report['verified_quotes']} quotes found on their page). "
        f"Read it, then: python main.py regulations accept {code}")
    if errors:
        log(f"Incomplete: {len(errors)} of {len(grp)} requests failed; their pages are missing from the draft. "
            "Run the same command again when the cause is fixed.")
    return report


def accept(repo, code: str, log=print) -> Path:
    """passages_draft.yaml -> passages_lane.yaml (the draft's comments and check fields are dropped)."""
    import yaml
    d = Path(repo) / P.REGULATIONS / code.upper()
    draft = d / "passages_draft.yaml"
    if not draft.exists():
        raise FileNotFoundError(f"No draft in {d} (run regulations extract first).")
    items = yaml.safe_load(draft.read_text(encoding="utf-8")) or []
    keep = [{k: v for k, v in p.items() if k not in ("verified_quote", "actions_stated", "norm_check")} for p in items]
    bad = [p["rule_id"] for p in keep if not p.get("text_en") or not p.get("rule_id")]
    if bad:
        raise ValueError(f"These passages have no rule_id or text_en: {', '.join(map(str, bad))}")
    out = d / "passages_lane.yaml"
    from .norms import norms_file
    nf = norms_file(repo, code.upper())
    nd = (P.read_yaml(nf) or {}) if nf.exists() else {}
    for p in keep:
        nd.setdefault(p["rule_id"], {"norm": p.get("norm", "informative"), "word": "", "checked": False})
    nf.write_text("# Force of each passage (see regulations/US/norms.yaml). Set checked: true after reading.\n\n"
                  + yaml.safe_dump(nd, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    rf = d / "region.yaml"
    if rf.exists():
        _set_status(rf, "in use")
    head = f"# Rule passages of {code.upper()} (accepted from passages_draft.yaml on {datetime.now(timezone.utc):%Y-%m-%d}).\n\n"
    out.write_text(head + yaml.safe_dump(keep, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    log(f"{out}: {len(keep)} passages. The prompts of Test B for {code.upper()} now use them; add the rule tables "
        f"(regulations/{code.upper()}/action_rules.json, lane_action_rules.json; see regulations/_template/) before labeling.")
    return out
