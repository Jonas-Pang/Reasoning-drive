"""Settings (config/experiment.yaml) and the API key (environment variable, normally from the .env file).

The YAML file is written for people: experiment, model, data, image and regions. load() turns it into the
dictionary the rest of the code uses (cfg["api"], cfg["run"], cfg["prompt"], cfg["regions"], ...).
"""
from __future__ import annotations

import copy
import json
import os
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG_FILE = "config/experiment.yaml"
TESTS = {"A": "image only", "B": "image + rule passages"}
RULE_TEXT = {"en": "text_en", "zh": "text_zh", "both": "both"}


class ConfigError(Exception):
    """A problem with the settings, with a message meant for the user."""


def _load_env(repo: Path) -> None:
    from video_tool.core import _load_env_file
    _load_env_file(repo / ".env")


def _yaml():
    try:
        import yaml
    except ImportError:
        raise ConfigError("PyYAML is missing: run  pip install -r requirements.txt") from None
    return yaml


def _off(v) -> bool:
    return v is None or v is False or str(v).strip().lower() in ("", "off", "none", "no", "false")


def from_yaml(y: dict) -> dict:
    """The internal settings dictionary from the YAML structure."""
    exp, model, data, image = y.get("experiment") or {}, y.get("model") or {}, y.get("data") or {}, y.get("image") or {}
    region = exp.get("region")
    if isinstance(region, bool):
        raise ConfigError("experiment.region was read as true/false: write the code in quotes, e.g. region: \"NO\".")
    regions = {}
    for code, r in (y.get("regions") or {}).items():
        if isinstance(code, bool):
            raise ConfigError("A region code was read as true/false: write it in quotes, e.g. \"NO\":")
        rules = r.get("rules") or {}
        lang = str(rules.get("language", "en"))
        if lang not in RULE_TEXT:
            raise ConfigError(f"regions.{code}.rules.language must be en, zh or both.")
        regions[str(code)] = {"name": r.get("name", str(code)), "name_zh": r.get("name_zh", ""),
                              "rule_region": str(rules.get("code", code)), "rule_text": RULE_TEXT[lang],
                              "rules_title": rules.get("title", ""), "rules_file": rules.get("file", "rules/rule_passages.json")}
    summary = model.get("reasoning_summary")
    return {
        "version": "3",
        "mock": bool(exp.get("mock", True)),
        "api": {
            "provider": model.get("provider", "openai"),
            "base_url": model.get("base_url", "https://api.openai.com/v1"),
            "api_key_env": model.get("api_key_env", "OPENAI_API_KEY"),
            "model": model.get("name", ""),
            "reasoning_effort": model.get("reasoning_effort"),
            "reasoning_summary": None if _off(summary) else str(summary),
            "temperature": model.get("temperature"),
            "image_detail": model.get("image_detail", "high"),
            "max_output_tokens": model.get("max_output_tokens", 2000),
            "instruction_role": model.get("instruction_role", "developer"),
            "store": model.get("store", False),
            "timeout_s": model.get("timeout_s", 90),
            "max_retries": model.get("max_retries", 4),
            "parallel": model.get("parallel", 5),
            "price_per_million_tokens": model.get("price_per_million_tokens", {}),
        },
        "run": {
            "test": "B" if exp.get("use_rules") is True or str(exp.get("use_rules")).lower() in ("yes", "true", "b") else "A",
            "region": str(region),
            "split": exp.get("split", "dev"),
            "repeats": exp.get("repeats", 1),
            "limit": exp.get("limit", 0),
            "marking_types": exp.get("marking_types") or [],
            "order_seed": exp.get("order_seed", 6216),
        },
        "datasets_root": data.get("datasets_root") or "",
        "workspaces": data.get("workspaces") or [],
        "data_policy": {"send_to_api": data.get("send_to_api", [])},
        "prompt": {
            "dir": f"prompts/{exp.get('prompt', 'v3')}",
            "box_color_rgb": image.get("box_color_rgb", [0, 229, 255]),
            "box_width": image.get("box_width", 3),
            "box_margin": image.get("box_margin", 6),
            "jpeg_quality": image.get("jpeg_quality", 92),
            "restrict_rule_ids_in_schema": bool(image.get("restrict_rule_ids_in_schema", False)),
        },
        "regions": regions,
    }


def load(repo: Path | None = None) -> dict:
    repo = Path(repo or REPO)
    p = repo / CONFIG_FILE
    if not p.exists():
        raise ConfigError(f"{p} is missing.")
    try:
        y = _yaml().safe_load(p.read_text(encoding="utf-8")) or {}
    except _yaml().YAMLError as e:
        raise ConfigError(f"{p} is not valid YAML: {e}") from None
    cfg = from_yaml(y)
    cfg["_repo"] = str(repo)
    _load_env(repo)
    check(cfg)
    return cfg


def check(cfg: dict) -> None:
    run = cfg.get("run", {})
    if run.get("test") not in TESTS:
        raise ConfigError("run.test must be \"A\" or \"B\" (experiment.use_rules: no or yes).")
    if run.get("region") not in cfg.get("regions", {}):
        raise ConfigError(f"experiment.region \"{run.get('region')}\" is not one of the regions: {', '.join(cfg.get('regions', {}))}.")
    pol = (cfg.get("data_policy") or {}).get("send_to_api")
    if pol is not None and not isinstance(pol, list):
        raise ConfigError("data.send_to_api must be a list of collections (e.g. [own_video]).")
    for code, r in cfg.get("regions", {}).items():
        for k in ("name", "rule_region", "rule_text", "rules_title"):
            if k not in r:
                raise ConfigError(f"regions.{code} needs \"{k}\".")
        if r["rule_text"] not in ("text_en", "text_zh", "both"):
            raise ConfigError(f"regions.{code}.rules.language must be en, zh or both.")


# ------------------------------------------------------------------ saving (keeps the comments of the file)

# internal key -> (YAML section, YAML key)
YAML_PATH = {"mock": ("experiment", "mock"), "run.test": ("experiment", "use_rules"), "run.region": ("experiment", "region"),
             "run.repeats": ("experiment", "repeats"), "run.limit": ("experiment", "limit"), "run.split": ("experiment", "split"),
             "prompt.dir": ("experiment", "prompt"), "api.model": ("model", "name"), "api.reasoning_effort": ("model", "reasoning_effort"),
             "api.reasoning_summary": ("model", "reasoning_summary"), "api.temperature": ("model", "temperature"),
             "api.image_detail": ("model", "image_detail"), "api.max_output_tokens": ("model", "max_output_tokens"),
             "api.parallel": ("model", "parallel")}


def _yaml_value(path: str, v) -> str:
    if path == "run.test":
        return "yes" if v == "B" else "no"
    if path == "prompt.dir":
        return str(v).split("/")[-1]
    if path == "api.reasoning_summary" and v in (None, ""):
        return "off"
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    return s if re.fullmatch(r"[A-Za-z0-9_.\-/]+", s) and s.lower() not in ("yes", "no", "on", "off", "true", "false", "null") else json.dumps(s)


def set_yaml_value(text: str, section: str, key: str, value: str) -> str:
    """Replace one scalar 'key: value' inside a top-level section, keeping indentation and the comment."""
    lines = text.split("\n")
    inside = False
    for i, line in enumerate(lines):
        if re.match(r"^\S", line):
            inside = line.split(":")[0].strip() == section
            continue
        m = re.match(rf"^(  {re.escape(key)}:\s*)([^#]*?)(\s*#.*)?$", line) if inside else None
        if m:
            head, comment = m.group(1), m.group(3) or ""
            if comment:
                column = len(head) + len(m.group(2)) + len(comment) - len(comment.lstrip())
                lines[i] = head + value + " " * max(1, column - len(head) - len(value)) + comment.lstrip()
            else:
                lines[i] = head + value
            return "\n".join(lines)
    raise ConfigError(f"{section}.{key} not found in {CONFIG_FILE}.")


def save(cfg: dict) -> None:
    """Write the editable settings back into config/experiment.yaml (other lines and comments stay as they are)."""
    check(cfg)
    p = Path(cfg["_repo"]) / CONFIG_FILE
    text = p.read_text(encoding="utf-8")
    for path, (section, key) in YAML_PATH.items():
        node = cfg
        for k in path.split("."):
            node = node[k]
        text = set_yaml_value(text, section, key, _yaml_value(path, node))
    p.write_text(text, encoding="utf-8")


def api_key(cfg: dict) -> str:
    return os.environ.get(cfg["api"].get("api_key_env", "OPENAI_API_KEY"), "").strip()


def public(cfg: dict) -> dict:
    """The settings to show or save with a run, with the key replaced by whether it is set."""
    out = copy.deepcopy({k: v for k, v in cfg.items() if not k.startswith("_")})
    key = api_key(cfg)
    out["api"]["api_key_set"] = bool(key)
    out["api"]["api_key_hint"] = ("…" + key[-4:]) if len(key) >= 8 else ""
    return out


def repo_of(cfg: dict) -> Path:
    return Path(cfg["_repo"])
