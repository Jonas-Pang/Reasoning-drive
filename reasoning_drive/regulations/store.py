"""List and check the countries in regulations/.

    python main.py regulations list           every country: passages, rule tables, a draft waiting to be read
    python main.py regulations check [CODE]   the files of one country (or all) against the template
"""
from __future__ import annotations

import json
from pathlib import Path

from .. import paths as P

PASSAGE_FIELDS = ["rule_id", "region", "source", "section", "page", "marking_type"]


def overview(repo) -> list[dict]:
    rows = []
    for code, (d, y) in P.regions(repo).items():
        pas = y.get("passages") or {}
        files = P.passage_files(repo, code)
        n = len(P.all_passages(repo, code))
        tables = y.get("rule_tables") or {}
        rows.append({"code": code, "name": y.get("name", ""), "driving_side": y.get("driving_side", ""),
                     "standard": (y.get("standard") or {}).get("title", ""), "passages": n,
                     "files": [f.name for f in files], "marking_file": pas.get("marking", ""),
                     "rule_table_marking": (d / tables.get("marking", "action_rules.json")).exists(),
                     "rule_table_lane": (d / tables.get("lane", "lane_action_rules.json")).exists(),
                     "draft": (d / "passages_draft.yaml").exists(), "folder": d.relative_to(Path(repo)).as_posix(),
                     "status": y.get("status") or ("in use" if n else "planned")})
    return rows


def check(repo, code: str | None = None) -> list[str]:
    """Problems found (an empty list means the country's files fit the template)."""
    problems = []
    regs = P.regions(repo)
    for c, (d, y) in regs.items():
        if code and c != code:
            continue
        where = f"regulations/{d.name}"
        for k in ("code", "name", "driving_side", "standard", "passages"):
            if k not in y:
                problems.append(f"{where}/region.yaml: no '{k}'")
        if y.get("driving_side") not in ("right", "left"):
            problems.append(f"{where}/region.yaml: driving_side must be right or left")
        if d.name != str(y.get("code")):
            problems.append(f"{where}: folder name and code ({y.get('code')}) differ")
        pas = y.get("passages") or {}
        # a planned country (no text read yet) or one whose draft waits to be read is not a problem: it is just not used yet
        waiting = y.get("status") in ("planned", "draft") or (d / "passages_draft.yaml").exists()
        for rel in dict.fromkeys([pas.get("marking")] + list(pas.get("lane") or [])):
            if rel and not (d / rel).exists() and not waiting:
                problems.append(f"{where}: {rel} listed in region.yaml but missing")
        ids = []
        for p in P.all_passages(repo, c):
            miss = [k for k in PASSAGE_FIELDS if k not in p]
            if miss:
                problems.append(f"{where}: passage {p.get('rule_id', '?')} lacks {', '.join(miss)}")
            if not (p.get("text_en") or p.get("text_zh") or p.get("text_original")):
                problems.append(f"{where}: passage {p.get('rule_id', '?')} has no text")
            ids.append(p.get("rule_id"))
        dup = sorted({i for i in ids if ids.count(i) > 1})
        if dup:
            problems.append(f"{where}: rule_id used twice: {', '.join(dup)}")
        known = set(ids)
        for name in ("action_rules.json", "lane_action_rules.json"):
            f = d / name
            if f.exists():
                txt = f.read_text(encoding="utf-8")
                for rid in sorted(set(json.loads(json.dumps(_rule_ids(json.loads(txt)))))):
                    if rid and rid not in known:
                        problems.append(f"{where}/{name}: rule ID {rid} is not one of the country's passages")
    return problems


def _rule_ids(node) -> list:
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "rule_ids" and isinstance(v, list):
                out += v
            else:
                out += _rule_ids(v)
    elif isinstance(node, list):
        for v in node:
            out += _rule_ids(v)
    return out
