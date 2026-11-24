"""Settings and the API key (environment variable, normally from the .env file).

The settings are read from three places, all written for people:
  configs/experiment.yaml          experiment, lane, data, image
  configs/api.yaml                 model (name, reasoning, prices); the key stays in .env
  regulations/<CODE>/region.yaml   one file per country: name, driving side, standard, passage files
read_settings() puts them together as one YAML structure; from_yaml() turns it into the dictionary the rest of the
code uses (cfg["api"], cfg["run"], cfg["prompt"], cfg["regions"], ...).
"""
from __future__ import annotations

import copy
import json
import os
import sys
import re
from pathlib import Path

from . import paths as P

REPO = P.REPO
CONFIG_FILE = P.EXPERIMENT_FILE
API_FILE = P.API_FILE
TESTS = {"A": "image only", "B": "image + rule passages"}
RULE_TEXT = {"en": "text_en", "zh": "text_zh", "both": "both"}


class ConfigError(Exception):
    """A problem with the settings, with a message meant for the user."""


def _load_env(repo: Path) -> None:
    from .labeling.core import _load_env_file
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
    lane = y.get("lane") or {}
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
        lane_rules = r.get("lane_rules") or [rules.get("file")]
        regions[str(code)] = {"name": r.get("name", str(code)), "name_zh": r.get("name_zh", ""),
                              "rule_region": str(rules.get("code", code)), "rule_text": RULE_TEXT[lang],
                              "rules_title": rules.get("title", ""), "rules_file": rules.get("file", ""),
                              "driving_side": str(r.get("driving_side", "right")), "draft": bool(r.get("draft", False)),
                              "lane_rules_files": [str(x) for x in (lane_rules if isinstance(lane_rules, list) else [lane_rules])],
                              "rule_regions": [str(x) for x in r.get("rule_regions") or [rules.get("code", code)]]}
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
        "lane": {
            "prompt_dir": f"prompts/{lane.get('prompt', 'lane_v1')}",
            "max_output_tokens": lane.get("max_output_tokens"),
            **({"control_region": dict(lane["control_region"])} if lane.get("control_region") else {}),
        },
    }


def _read(p: Path, required: bool = True) -> dict:
    if not p.exists():
        if required:
            raise ConfigError(f"{p} is missing.")
        return {}
    try:
        return _yaml().safe_load(p.read_text(encoding="utf-8")) or {}
    except _yaml().YAMLError as e:
        raise ConfigError(f"{p} is not valid YAML: {e}") from None


DRAFT_FILE = "passages_draft.yaml"


def region_entries(repo: Path, drafts: bool = False) -> dict:
    """regulations/<CODE>/region.yaml of every country, in the form from_yaml() reads (paths relative to the repository).
    A country whose passages are still a draft is left out, unless drafts=True (lane try --draft): then its
    passages_draft.yaml is used and the country is marked as a draft, so nothing it produces is taken for a result."""
    out = {}
    for code, (d, r) in P.regions(repo).items():
        if isinstance(code, bool) or str(code).lower() in ("true", "false"):
            raise ConfigError(f"{d / 'region.yaml'}: write the code in quotes, e.g. code: \"NO\".")
        rel = d.relative_to(repo).as_posix()
        std, pas = r.get("standard") or {}, r.get("passages") or {}
        draft = False
        if not pas.get("marking") or not (d / pas["marking"]).exists():
            if not (drafts and (d / DRAFT_FILE).exists()):
                continue  # a country whose passages are still a draft (regulations accept <CODE>) is not used yet
            pas, draft = {"marking": DRAFT_FILE, "lane": [DRAFT_FILE]}, True
        lane = pas.get("lane") or [pas.get("marking")]
        out[str(code)] = {"name": r.get("name", str(code)), "name_zh": r.get("name_zh", ""),
                          "driving_side": r.get("driving_side", "right"), "draft": draft,
                          "lane_rules": [f"{rel}/{f}" for f in (lane if isinstance(lane, list) else [lane]) if f],
                          "rules": {"file": f"{rel}/{pas.get('marking')}" if pas.get("marking") else "", "code": str(code),
                                    "title": std.get("title", ""), "language": _prompt_language(std.get("language", "en"))},
                          **({"parent": str(r["parent"])} if r.get("parent") else {})}
    for code, e in out.items():
        _inherit(code, e, out)
    for e in out.values():
        e.pop("_inherited", None)
    return out


def _inherit(code: str, e: dict, regions: dict, seen: tuple = ()) -> None:
    """A state or territory whose road rules copy a national model law (region.yaml: parent: AU) gets the parent's lane
    passages first and its own (only what it changed or added) after them; a passage of its own with the same section
    as a parent passage is the one that counts (agent prompt: later passages override earlier ones of that section)."""
    parent = e.get("parent")
    if not parent or e.get("_inherited"):
        return
    if parent in seen or parent == code:
        raise ConfigError(f"regulations/{code}/region.yaml: parent {parent} leads back to {code}.")
    p = regions.get(parent)
    if p is None:
        e["parent_missing"] = parent  # parent not usable yet (no accepted passages): the region runs on its own passages
        return
    _inherit(parent, p, regions, seen + (code,))
    e["lane_rules"] = [f for f in p["lane_rules"] if f not in e["lane_rules"]] + e["lane_rules"]
    e["rule_regions"] = [x for x in p.get("rule_regions", [parent]) if x != code] + [code]
    e["draft"] = e["draft"] or p["draft"]
    e["_inherited"] = True


def _prompt_language(lang) -> str:
    """Which text of the passages goes into the prompt: Chinese and English standards as written; a standard in any other
    language (Japanese, Hindi, ...) through the English text the extractor writes next to the original (text_en)."""
    lang = str(lang or "en")
    return lang if lang in RULE_TEXT else "en"


_KEY_WARNED = []


def looks_like_key(v) -> bool:
    return isinstance(v, str) and v.strip().startswith(("sk-", "sk_")) and len(v.strip()) > 20


def _take_key(model: dict) -> dict:
    """An API key written into configs/api.yaml (as api_key, or by mistake as api_key_env) is moved into the process
    environment and removed from the settings, so it never reaches a manifest, a log or the web page. It still works,
    but api.yaml is in Git and in the Docker image: the key belongs in .env (a warning says so once)."""
    env = model.get("api_key_env", "OPENAI_API_KEY")
    key = model.pop("api_key", None)
    if looks_like_key(env):
        key, env = env, "OPENAI_API_KEY"
        model["api_key_env"] = env
    if looks_like_key(key):
        os.environ.setdefault(env, key.strip())
        if not _KEY_WARNED:
            _KEY_WARNED.append(1)
            print(f"Note: configs/api.yaml holds the API key. It is used, but api.yaml goes into Git and into the Docker image; "
                  f"put it in .env as {env}=... and remove it from api.yaml.", file=sys.stderr)
    return model


def read_settings(repo: Path | None = None, drafts: bool = False) -> dict:
    """configs/experiment.yaml + configs/api.yaml + every regulations/<CODE>/region.yaml, as one YAML structure."""
    repo = Path(repo or REPO)
    y = _read(repo / CONFIG_FILE)
    api = _read(repo / API_FILE, required=False)
    if api.get("model"):
        y["model"] = _take_key(dict(api["model"]))
    if not y.get("regions"):
        y["regions"] = region_entries(repo, drafts)
    return y


def load(repo: Path | None = None, drafts: bool = False) -> dict:
    repo = Path(repo or REPO)
    cfg = from_yaml(read_settings(repo, drafts))
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
        if r.get("driving_side", "right") not in ("right", "left"):
            raise ConfigError(f"regions.{code}.driving_side must be right or left.")


# ------------------------------------------------------------------ saving (keeps the comments of the file)

# internal key -> (YAML section, YAML key)
YAML_PATH = {"mock": ("experiment", "mock"), "run.test": ("experiment", "use_rules"), "run.region": ("experiment", "region"),
             "run.repeats": ("experiment", "repeats"), "run.limit": ("experiment", "limit"), "run.split": ("experiment", "split"),
             "prompt.dir": ("experiment", "prompt"), "api.model": ("model", "name"), "api.reasoning_effort": ("model", "reasoning_effort"),
             "api.reasoning_summary": ("model", "reasoning_summary"), "api.temperature": ("model", "temperature"),
             "api.image_detail": ("model", "image_detail"), "api.max_output_tokens": ("model", "max_output_tokens"),
             "api.parallel": ("model", "parallel"), "lane.prompt_dir": ("lane", "prompt"),
             "lane.max_output_tokens": ("lane", "max_output_tokens")}


def _yaml_value(path: str, v) -> str:
    if path == "run.test":
        return "yes" if v == "B" else "no"
    if path in ("prompt.dir", "lane.prompt_dir"):
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
    raise ConfigError(f"{section}.{key} not found.")


def settings_file(section: str) -> str:
    """The file that holds a top-level section: model is in configs/api.yaml, the rest in configs/experiment.yaml."""
    return API_FILE if section == "model" else CONFIG_FILE


def save(cfg: dict) -> None:
    """Write the editable settings back into configs/experiment.yaml and configs/api.yaml (other lines and comments
    stay as they are)."""
    check(cfg)
    repo = Path(cfg["_repo"])
    texts = {}
    for path, (section, key) in YAML_PATH.items():
        f = settings_file(section)
        if not (repo / f).exists():
            f = CONFIG_FILE  # an older layout with the model section in experiment.yaml
        if f not in texts:
            texts[f] = (repo / f).read_text(encoding="utf-8")
        node = cfg
        for k in path.split("."):
            node = node[k]
        try:
            texts[f] = set_yaml_value(texts[f], section, key, _yaml_value(path, node))
        except ConfigError:
            if section != "lane":  # an older settings file without the lane section
                raise ConfigError(f"{section}.{key} not found in {f}.") from None
    for f, text in texts.items():
        (repo / f).write_text(text, encoding="utf-8")


def api_key(cfg: dict) -> str:
    # "_key": a key a user typed on the web page (/app, "Your API key"); kept in memory only, never saved (Claude, 2026-11-18)
    a = cfg["api"]
    return str(a.get("_key") or os.environ.get(a.get("api_key_env", "OPENAI_API_KEY"), "")).strip()


def public(cfg: dict) -> dict:
    """The settings to show or save with a run, with the key replaced by whether it is set."""
    out = copy.deepcopy({k: v for k, v in cfg.items() if not k.startswith("_")})
    key = api_key(cfg)
    out["api"].pop("_key", None)
    out["api"]["api_key_set"] = bool(key)
    out["api"]["api_key_hint"] = ("…" + key[-4:]) if len(key) >= 8 else ""
    return out


def repo_of(cfg: dict) -> Path:
    return Path(cfg["_repo"])
