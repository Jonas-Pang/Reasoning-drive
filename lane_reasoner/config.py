"""Settings (config/experiment.json) and the API key (environment variable, normally from the .env file)."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG_FILE = "config/experiment.json"
TESTS = {"A": "image only", "B": "image + rule passages"}


class ConfigError(Exception):
    """A problem with the settings, with a message meant for the user."""


def _load_env(repo: Path) -> None:
    from video_tool.core import _load_env_file
    _load_env_file(repo / ".env")


def load(repo: Path | None = None) -> dict:
    repo = Path(repo or REPO)
    p = repo / CONFIG_FILE
    if not p.exists():
        raise ConfigError(f"{p} is missing.")
    cfg = json.loads(p.read_text(encoding="utf-8"))
    cfg["_repo"] = str(repo)
    _load_env(repo)
    check(cfg)
    return cfg


def check(cfg: dict) -> None:
    run = cfg.get("run", {})
    if run.get("test") not in TESTS:
        raise ConfigError("run.test must be \"A\" or \"B\".")
    if run.get("region") not in cfg.get("regions", {}):
        raise ConfigError(f"run.region \"{run.get('region')}\" is not one of the regions: {', '.join(cfg.get('regions', {}))}.")
    pol = (cfg.get("data_policy") or {}).get("send_to_api")
    if pol is not None and not isinstance(pol, list):
        raise ConfigError("data_policy.send_to_api must be a list of collections (e.g. [\"own_video\"]).")
    for code, r in cfg.get("regions", {}).items():
        for k in ("name", "rule_region", "rule_text", "rules_title"):
            if k not in r:
                raise ConfigError(f"regions.{code} needs \"{k}\".")
        if r["rule_text"] not in ("text_en", "text_zh", "both"):
            raise ConfigError(f"regions.{code}.rule_text must be text_en, text_zh or both.")


def save(cfg: dict) -> None:
    repo = Path(cfg["_repo"])
    out = {k: v for k, v in cfg.items() if not k.startswith("_") or k == "_comment"}
    check(out | {"_repo": cfg["_repo"]})
    (repo / CONFIG_FILE).write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def api_key(cfg: dict) -> str:
    return os.environ.get(cfg["api"].get("api_key_env", "OPENAI_API_KEY"), "").strip()


def public(cfg: dict) -> dict:
    """The settings to show or save with a run: never the key itself, only whether one is set."""
    out = copy.deepcopy({k: v for k, v in cfg.items() if not k.startswith("_")})
    key = api_key(cfg)
    out["api"]["api_key_set"] = bool(key)
    out["api"]["api_key_hint"] = ("…" + key[-4:]) if len(key) >= 8 else ""
    return out


def repo_of(cfg: dict) -> Path:
    return Path(cfg["_repo"])
