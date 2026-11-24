"""The frozen protocol of the lane test run: what may not change between freezing and the run on the test images.

python main.py lane freeze --note "..."   writes configs/lane_protocol.json
python main.py lane protocol              shows whether the current files still match it

Frozen: every file of the lane prompt folder, the answer schema and rule table, the rule passage files of every
region, the code that builds the prompt and scores the answers, the model settings, and the prompt hashes of Test A,
B and C per region. The test images are answered by the model only while all of these match (run_lane and the demo
page refuse otherwise), and each test runs once per region on the test images; a second run needs --again and is
recorded as such. Development images are not affected.
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


def load_protocol(cfg: dict) -> dict | None:
    p = repo_of(cfg) / PROTOCOL_FILE
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def freeze(cfg: dict, note: str = "") -> dict:
    from ..agent.runner import git_commit
    state = protocol_state(cfg)
    doc = {"frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "git_commit": git_commit(repo_of(cfg)),
           "note": note, **state}
    (repo_of(cfg) / PROTOCOL_FILE).write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return doc


def protocol_check(cfg: dict) -> dict:
    """{'frozen': bool, 'matches': bool, 'differences': [...], 'frozen_utc': ...}"""
    doc = load_protocol(cfg)
    if not doc:
        return {"frozen": False, "matches": False, "differences": ["no frozen protocol (python main.py lane freeze)"], "frozen_utc": None}
    now = protocol_state(cfg)
    diff = []
    for f in sorted(set(doc["files"]) | set(now["files"])):
        if doc["files"].get(f) != now["files"].get(f):
            diff.append(f"file {f} " + ("added" if f not in doc["files"] else "removed" if f not in now["files"] else "changed"))
    for k in sorted(set(doc["settings"]) | set(now["settings"])):
        if doc["settings"].get(k) != now["settings"].get(k):
            diff.append(f"setting {k}: {doc['settings'].get(k)!r} -> {now['settings'].get(k)!r}")
    for k in sorted(set(doc["prompts"]) | set(now["prompts"])):
        if doc["prompts"].get(k) != now["prompts"].get(k):
            diff.append(f"prompt {k} changed")
    return {"frozen": True, "matches": not diff, "differences": diff, "frozen_utc": doc["frozen_utc"]}


def require_frozen(cfg: dict) -> dict:
    chk = protocol_check(cfg)
    if not chk["matches"]:
        raise ConfigError("Test images are answered only with the frozen protocol. " + "; ".join(chk["differences"][:5])
                          + (" ..." if len(chk["differences"]) > 5 else ""))
    return chk


__all__ = ["freeze", "protocol_check", "protocol_state", "require_frozen", "load_protocol", "PROTOCOL_FILE"]
