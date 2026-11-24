"""The frozen protocol of the lane test run: what may not change between freezing and the run on the test images.

python main.py lane freeze --note "..."   writes configs/lane_protocol.json
python main.py lane protocol              shows whether the current files still match it

Frozen: every file of the lane prompt folder, the answer schema and rule table, the rule passage files of every
region, the code that builds the prompt and scores the answers, the model settings, and the prompt hashes of Test A,
B and C per region. The test images are answered by the model only while all of these match (run_lane and the demo
page refuse otherwise), and each test runs once per region on the test images; a second run needs --again and is
recorded as such. Development images are not affected.

Countries added after the freeze (added by Claude, 2026-11-16): the protocol covers the regions it was frozen with. A
country added later (its rule passages, rule table and prompts) is not a difference for those regions, so their test runs
go on; the new country's test images are answered only after `lane freeze --add` has added it to the protocol, which keeps
everything frozen before (and the frozen time, so "each test runs once" still holds) and records the extension.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone

from .. import paths as P
from ..config import ConfigError, repo_of

PROTOCOL_FILE = P.PROTOCOL_FILE
CODE_FILES = ["reasoning_drive/agent/lane.py", "reasoning_drive/evaluation/lane_scoring.py", "reasoning_drive/labeling/lanes.py",
              P.LANE_SCHEMA]


def _sha_file(path) -> str:
    return hashlib.sha256(P.text_bytes(path)).hexdigest()[:16]


def protocol_state(cfg: dict) -> dict:
    from ..agent.client import settings_of
    from ..agent.lane import lane_cfg, lane_prompt_parts, lane_rule_files
    repo, lc = repo_of(cfg), lane_cfg(cfg)
    prompt_dir = repo / cfg["lane"]["prompt_dir"]
    files = {str(p.relative_to(repo)): _sha_file(p) for p in sorted(prompt_dir.glob("*")) if p.is_file() and not p.name.startswith(".")}
    for f in CODE_FILES:
        if (repo / f).exists():
            files[f] = _sha_file(repo / f)
    for p in P.rule_table_files(repo, lane=True):
        files[str(p.relative_to(repo).as_posix())] = _sha_file(p)
    prompts = {}
    for region in cfg["regions"]:
        for p in lane_rule_files(lc, region):
            files[str(p.relative_to(repo))] = _sha_file(p)
        for test in ("A", "B", "C"):
            try:
                h = lane_prompt_parts(lc, test, region)["hashes"]
            except ConfigError:
                continue
            prompts[f"{test}_{region}"] = {k: h[k] for k in ("instructions", "user_text", "schema")}
    return {"files": files, "settings": settings_of(lc), "prompts": prompts}


def protocol_file(cfg: dict) -> str:
    """configs/lane_protocol.json, or the model's own file when the run uses an API profile with its own protocol
    (configs/api_profiles.yaml, protocol_file): each model is frozen separately, so freezing a second model leaves the
    first model's frozen protocol and its test runs as they were (added by Claude, 2026-11-16)."""
    return (cfg.get("api") or {}).get("protocol_file") or PROTOCOL_FILE


def load_protocol(cfg: dict) -> dict | None:
    p = repo_of(cfg) / protocol_file(cfg)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def freeze(cfg: dict, note: str = "") -> dict:
    from ..agent.runner import git_commit
    state = protocol_state(cfg)
    doc = {"frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "git_commit": git_commit(repo_of(cfg)),
           "note": note, **state}
    (repo_of(cfg) / protocol_file(cfg)).write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return doc


def frozen_regions(doc: dict) -> list[str]:
    """The regions a frozen protocol covers: those it lists, else those of its prompt hashes (A_CN -> CN)."""
    regs = set(doc.get("regions") or []) | {k.split("_", 1)[1] for k in (doc.get("prompts") or {}) if "_" in k}
    return sorted(regs)


def _region_of_file(f: str) -> str | None:
    """regulations/UK/passages_lane.yaml -> UK (None for any other file)."""
    parts = f.replace("\\", "/").split("/")
    return parts[1] if len(parts) > 2 and parts[0] == "regulations" and not parts[1].startswith("_") else None


def protocol_check(cfg: dict, region: str | None = None) -> dict:
    """{'frozen': bool, 'matches': bool, 'differences': [...], 'frozen_utc': ..., 'regions': [...], 'not_covered': [...]}

    Only the regions the protocol covers are compared: files and prompts of a country added later are listed in
    'not_covered', not as differences. With region given, a region the protocol does not cover is a difference."""
    doc = load_protocol(cfg)
    if not doc:
        return {"frozen": False, "matches": False, "differences": ["no frozen protocol (python main.py lane freeze)"], "frozen_utc": None,
                "regions": [], "not_covered": []}
    covered = set(frozen_regions(doc))
    now = protocol_state(cfg)
    diff, outside = [], set()
    for f in sorted(set(doc["files"]) | set(now["files"])):
        if doc["files"].get(f) != now["files"].get(f):
            r = _region_of_file(f)
            if f not in doc["files"] and r and r not in covered:
                outside.add(r)
                continue
            diff.append(f"file {f} " + ("added" if f not in doc["files"] else "removed" if f not in now["files"] else "changed"))
    for k in sorted(set(doc["settings"]) | set(now["settings"])):
        if doc["settings"].get(k) != now["settings"].get(k):
            diff.append(f"setting {k}: {doc['settings'].get(k)!r} -> {now['settings'].get(k)!r}")
    for k in sorted(set(doc["prompts"]) | set(now["prompts"])):
        if doc["prompts"].get(k) != now["prompts"].get(k):
            r = k.split("_", 1)[1] if "_" in k else None
            if k not in doc["prompts"] and r and r not in covered:
                outside.add(r)
                continue
            diff.append(f"prompt {k} changed")
    if region and region not in covered:
        diff.append(f"region {region} is not in the frozen protocol (add it with: python main.py lane freeze --add --note \"...\")")
    return {"frozen": True, "matches": not diff, "differences": diff, "frozen_utc": doc["frozen_utc"], "regions": sorted(covered),
            "not_covered": sorted(outside)}


def _caller_region() -> str | None:
    """The region of the lane run that asks (run_lane's 'region', or the 'item' being answered), read from the calling
    frames, since the frozen code in agent/lane.py calls require_frozen(cfg) without it."""
    import sys
    f = sys._getframe(2)
    for _ in range(3):
        if f is None:
            break
        loc = f.f_locals
        if isinstance(loc.get("region"), str) and loc.get("region"):
            return loc["region"]
        item = loc.get("item")
        if getattr(item, "region", None):
            return item.region
        f = f.f_back
    return None


def require_frozen(cfg: dict, region: str | None = None) -> dict:
    chk = protocol_check(cfg, region or _caller_region())
    if not chk["matches"]:
        raise ConfigError("Test images are answered only with the frozen protocol. " + "; ".join(chk["differences"][:5])
                          + (" ..." if len(chk["differences"]) > 5 else ""))
    return chk


def freeze_add(cfg: dict, note: str = "") -> dict:
    """Add the regions the frozen protocol does not cover yet. Everything frozen before must still match; it is kept as it
    was, with its frozen time, and the extension (time, regions, note) is recorded in 'extensions'."""
    doc = load_protocol(cfg)
    if not doc:
        raise ConfigError("No frozen protocol yet: use python main.py lane freeze --note \"...\" first.")
    chk = protocol_check(cfg)
    if not chk["matches"]:
        raise ConfigError("The frozen part has changed, so no region is added: " + "; ".join(chk["differences"][:5]))
    covered = set(frozen_regions(doc))
    new = [r for r in cfg["regions"] if r not in covered]
    if not new:
        return {"added": [], **doc}
    state = protocol_state(cfg)
    doc["files"].update({f: h for f, h in state["files"].items() if f not in doc["files"]})
    doc["prompts"].update({k: v for k, v in state["prompts"].items() if k not in doc["prompts"]})
    doc["regions"] = sorted(covered | set(new))
    doc.setdefault("extensions", []).append({"utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "regions": new, "note": note})
    (repo_of(cfg) / protocol_file(cfg)).write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"added": new, **doc}


__all__ = ["protocol_file", "freeze", "freeze_add", "frozen_regions", "protocol_check", "protocol_state", "require_frozen", "load_protocol",
           "PROTOCOL_FILE"]
