"""The force of each rule passage: mandatory, recommended, permissive or informative.

Standards say how binding a sentence is with fixed words: MUTCD "shall" (Standard), "should" (Guidance), "may" (Option);
GB 5768 应 / 不应 / 不得 / 禁止, 宜 / 不宜, 可; the UK Traffic Signs Manual and the Highway Code "must" / "should" / "may";
Japanese laws しなければならない / してはならない. The lane prompt from lane_v2 on prints the force next to every passage,
so a passage that only recommends (should) is not read as a prohibition, and a mandatory one is not read as advice.

Where the words come from:
  1. NORM_WORDS below, per language (the standard's language in region.yaml);
  2. norm_words in regulations/<CODE>/region.yaml, which replace them for one country.
The tagger only proposes. The reviewed values are kept in regulations/<CODE>/norms.yaml (rule_id -> norm), next to the
passage files, which are not changed; a value written there by hand wins over the proposal.

    python main.py regulations norms US            proposals and the reviewed values, side by side
    python main.py regulations norms US --write    write the proposals for passages that have no reviewed value yet
"""
from __future__ import annotations

import re
from pathlib import Path

from .. import paths as P

NORMS = ["mandatory", "recommended", "permissive", "informative"]

# Regular expressions per language; the strongest level found decides (mandatory > recommended > permissive).
NORM_WORDS = {
    "en": {"mandatory": [r"\bshall\b", r"\bmust\b", r"\bmay not\b", r"\bis not permitted\b", r"\bare not permitted\b", r"\bis prohibited\b",
                         r"\bare prohibited\b", r"\bprohibits\b"],
           "recommended": [r"\bshould\b"],
           "permissive": [r"\bmay\b", r"\bis permitted\b", r"\bare permitted\b"]},
    # 应 but not 对应 相应 反应 适应 供应 响应 应用; 可 but not 可变 可能 可见 可视 可靠 不可 (不可 is mandatory)
    "zh": {"mandatory": [r"(?<![对相反适供响])应(?![用])", r"不得", r"禁止", r"严禁", r"必须", r"不可", r"不准", r"不允许"],
           "recommended": [r"宜"],
           "permissive": [r"(?<![不])可(?![变能见视靠])", r"(?<![不])允许"]},
    "ja": {"mandatory": [r"しなければならない", r"してはならない", r"禁止", r"ものとする"],
           "recommended": [r"望ましい", r"努めなければならない"],
           "permissive": [r"ことができる"]},
}


def _lang(region_yaml: dict) -> str:
    lang = ((region_yaml.get("standard") or {}).get("language") or "en").lower()
    return "zh" if lang in ("zh", "both") else lang


def words_for(region_yaml: dict, lang: str | None = None) -> dict:
    custom = region_yaml.get("norm_words") or {}
    if custom:
        return {k: list(custom.get(k) or []) for k in ("mandatory", "recommended", "permissive")}
    return NORM_WORDS.get(lang or _lang(region_yaml), NORM_WORDS["en"])


def passage_text(p: dict, region_yaml: dict) -> tuple[str, str]:
    """(text in the standard's own words, its language): the original text if the passage has one (text_original,
    or text_zh when the English text is a translation), else the English text."""
    if p.get("text_original"):
        return p["text_original"], _lang(region_yaml)
    if p.get("text_zh") and (p.get("text_en_is_translation") or _lang(region_yaml) == "zh"):
        return p["text_zh"], "zh"
    return p.get("text_en") or "", "en"


def propose_for(p: dict, region_yaml: dict) -> tuple[str, str]:
    text, lang = passage_text(p, region_yaml)
    return propose(text, words_for(region_yaml, lang))


def propose(text: str, words: dict) -> tuple[str, str]:
    """(norm, the word that decided it); informative when no word is found."""
    for level in ("mandatory", "recommended", "permissive"):
        for pat in words.get(level) or []:
            m = re.search(pat, text, re.I)
            if m:
                return level, m.group(0)
    return "informative", ""


def norms_file(repo, code: str) -> Path:
    return Path(repo) / P.REGULATIONS / code / "norms.yaml"


def reviewed(repo, code: str) -> dict:
    """rule_id -> norm from regulations/<CODE>/norms.yaml (empty if there is none)."""
    f = norms_file(repo, code)
    if not f.exists():
        return {}
    data = P.read_yaml(f) or {}
    return {str(k): (v.get("norm") if isinstance(v, dict) else v) for k, v in data.items() if (v.get("norm") if isinstance(v, dict) else v) in NORMS}


def norm_map(repo, code: str, passages: list[dict] | None = None) -> dict:
    """rule_id -> norm for a country: the reviewed value, else a norm written in the passage, else the proposal."""
    _, y = P.regions(repo).get(code, (None, {}))
    out = {}
    for p in passages if passages is not None else P.all_passages(repo, code):
        out[p["rule_id"]] = p.get("norm") if p.get("norm") in NORMS else propose_for(p, y)[0]
    out.update(reviewed(repo, code))
    return out


def table(repo, code: str) -> list[dict]:
    regs = P.regions(repo)
    if code not in regs:
        raise KeyError(f"No country {code} in {P.REGULATIONS}/.")
    _, y = regs[code]
    rev = reviewed(repo, code)
    rows = []
    for p in P.all_passages(repo, code):
        prop, word = propose_for(p, y)
        rows.append({"rule_id": p["rule_id"], "proposed": prop, "word": word, "reviewed": rev.get(p["rule_id"], ""),
                     "marking_type": p.get("marking_type", ""), "text": " ".join(passage_text(p, y)[0].split())[:110]})
    return rows


def write_proposals(repo, code: str) -> tuple[Path, int]:
    """Add the proposals for passages without a reviewed value to norms.yaml (existing values are kept)."""
    import yaml
    f = norms_file(repo, code)
    data = (P.read_yaml(f) or {}) if f.exists() else {}
    added = 0
    for r in table(repo, code):
        if r["rule_id"] not in data:
            data[r["rule_id"]] = {"norm": r["proposed"], "word": r["word"], "checked": False}
            added += 1
    head = (f"# Force of each passage of {code} (mandatory, recommended, permissive, informative), proposed from the\n"
            "# standard's own words (shall/should/may, 应/宜/可 ...). Read each one against its passage; set checked: true\n"
            "# when it is right, or change norm. The lane prompt from lane_v2 on prints these values.\n\n")
    f.write_text(head + yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    return f, added
