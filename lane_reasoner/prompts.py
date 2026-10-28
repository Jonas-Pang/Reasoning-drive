"""The prompt parts, the region's rule passages and the answer schema.

Test A and Test B use the same instructions, examples, schema and image; Test B adds the rule block of the
image's region and two one-line slots that refer to it. Everything that goes into a request is hashed, and the
hashes are saved with every result, so two runs can be checked to differ only where they should.

A prompt folder holds either one instructions.txt (v1, v2) or the parts role.txt, procedure.txt and fields.txt
(v3), joined in this order. answer_fields.txt, if present, sets the order of the answer fields; the model writes
them in that order, so fields placed before "actions" are reasoning that comes before the decision.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .config import ConfigError, repo_of


def _read(cfg: dict, name: str) -> str:
    p = repo_of(cfg) / cfg["prompt"]["dir"] / name
    if not p.exists():
        raise ConfigError(f"Prompt file missing: {p}")
    return p.read_text(encoding="utf-8").strip()


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _exists(cfg: dict, name: str) -> bool:
    return (repo_of(cfg) / cfg["prompt"]["dir"] / name).exists()


def template(cfg: dict) -> str:
    """The instructions with the two slots not filled in."""
    if _exists(cfg, "instructions.txt"):
        return _read(cfg, "instructions.txt")
    return "\n\n".join(_read(cfg, n) for n in ("role.txt", "procedure.txt", "fields.txt"))


def label_schema(cfg: dict) -> dict:
    return json.loads((repo_of(cfg) / "config" / "label_schema.json").read_text(encoding="utf-8"))


def _rules_path(cfg: dict, region: str | None) -> Path:
    rel = (cfg["regions"].get(region) or {}).get("rules_file") if region else None
    return repo_of(cfg) / (rel or "rules/rule_passages.json")


def read_passages_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        import yaml
        return yaml.safe_load(text) or []
    return json.loads(text)


def passages(cfg: dict, region: str) -> list[dict]:
    rc = cfg["regions"][region]
    path = _rules_path(cfg, region)
    if not path.exists():
        raise ConfigError(f"Rules file of region {region} not found: {path}")
    allp = read_passages_file(path)
    out = [p for p in allp if p.get("region", rc["rule_region"]) == rc["rule_region"]]
    if not out:
        raise ConfigError(f"No rule passages with region \"{rc['rule_region']}\" in {path.name}.")
    return out


def rules_file_hash(cfg: dict, region: str | None = None) -> str:
    return hashlib.sha256(_rules_path(cfg, region).read_bytes()).hexdigest()[:16]


def _passage_text(p: dict, mode: str) -> str:
    en, zh = (p.get("text_en") or "").strip(), (p.get("text_zh") or "").strip()
    if mode == "text_zh" and zh:
        return zh
    if mode == "both" and zh and en and zh != en:
        return f"{zh}\n(English: {en})" if p.get("text_en_is_translation") else f"{en}\n(中文: {zh})"
    return en or zh


def rules_block(cfg: dict, region: str) -> str:
    rc = cfg["regions"][region]
    head = _read(cfg, "rules_header.txt").format(region_name=rc["name"], rules_title=rc["rules_title"])
    lines = [head, ""]
    for p in passages(cfg, region):
        where = ", ".join(x for x in (p.get("source", ""), f"section {p.get('section', '')}" if p.get("section") else "",
                                      f"page {p['page']}" if p.get("page") else "") if x)
        lines.append(f"[{p['rule_id']}] {where}")
        lines.append(_passage_text(p, rc["rule_text"]))
        lines.append("")
    return "\n".join(lines).strip()


def examples_block(cfg: dict) -> str:
    p = repo_of(cfg) / cfg["prompt"]["dir"] / "examples.json"
    ex = json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
    if not ex:
        return ""
    parts = ["EXAMPLES (written from development images; text only):"]
    for i, e in enumerate(ex, 1):
        parts.append(f"Example {i}. {e['situation']}\nAnswer: {json.dumps(e['answer'], ensure_ascii=False)}")
    return "\n\n".join(parts)


def instructions(cfg: dict, test: str, region: str) -> str:
    text = template(cfg)
    text = text.replace("{STEP2}", _read(cfg, f"step2_{test}.txt")).replace("{CITATION}", _read(cfg, f"citation_{test}.txt"))
    parts = [text]
    if test == "B":
        parts.append(rules_block(cfg, region))
    ex = examples_block(cfg)
    if ex:
        parts.append(ex)
    return "\n\n".join(parts)


def user_text(cfg: dict, region: str) -> str:
    return _read(cfg, "user.txt").format(region_name=cfg["regions"][region]["name"])


DEFAULT_FIELDS = ["description", "evidence", "marking", "actions", "cited_rule_id", "reasoning"]
REASONING_FIELDS = ["description", "rule_reasoning", "action_reasons", "self_check", "reasoning"]


def answer_fields(cfg: dict) -> list[str]:
    if not _exists(cfg, "answer_fields.txt"):
        return list(DEFAULT_FIELDS)
    return [ln.split("#")[0].strip() for ln in _read(cfg, "answer_fields.txt").splitlines() if ln.split("#")[0].strip()]


def answer_schema(cfg: dict, test: str, region: str) -> dict:
    s = label_schema(cfg)
    enum = lambda vals: {"type": "string", "enum": list(vals)}  # noqa: E731
    cite: dict = {"anyOf": [{"type": "string"}, {"type": "null"}]}
    if test == "B" and cfg["prompt"].get("restrict_rule_ids_in_schema"):
        cite = {"anyOf": [enum([p["rule_id"] for p in passages(cfg, region)]), {"type": "null"}]}
    spec = {
        "description": {"type": "string"},
        "evidence": enum(s["evidence"]),
        "marking": {
            "type": "object",
            "properties": {
                "marking_type": enum(s["marking_type"]),
                "arrow_type": {"anyOf": [enum(s["arrow_type"]), {"type": "null"}]},
                "position": enum(s["position"]),
            },
            "required": ["marking_type", "arrow_type", "position"],
            "additionalProperties": False,
        },
        "rule_reasoning": {"type": "string"},
        "action_reasons": {
            "type": "object",
            "properties": {a: {"type": "string"} for a in s["actions"]},
            "required": list(s["actions"]),
            "additionalProperties": False,
        },
        "self_check": {"type": "string"},
        "actions": {
            "type": "object",
            "properties": {a: enum(s["action_values"]) for a in s["actions"]},
            "required": list(s["actions"]),
            "additionalProperties": False,
        },
        "cited_rule_id": cite,
        "reasoning": {"type": "string"},
    }
    fields = answer_fields(cfg)
    unknown = [f for f in fields if f not in spec]
    if unknown or not {"evidence", "marking", "actions", "cited_rule_id"} <= set(fields):
        raise ConfigError(f"answer_fields.txt: unknown fields {unknown} or one of evidence, marking, actions, cited_rule_id missing.")
    return {"type": "object", "properties": {f: spec[f] for f in fields}, "required": fields, "additionalProperties": False}


def prompt_parts(cfg: dict, test: str, region: str) -> dict:
    """Everything except the image, with hashes: what the demo page shows and what every result records."""
    ins = instructions(cfg, test, region)
    usr = user_text(cfg, region)
    sch = answer_schema(cfg, test, region)
    shared = template(cfg) + examples_block(cfg) + json.dumps(sch, sort_keys=True) + usr
    return {
        "test": test, "region": region, "instructions": ins, "user_text": usr, "schema": sch,
        "rules_block": rules_block(cfg, region) if test == "B" else "",
        "slots": {"step2": _read(cfg, f"step2_{test}.txt"), "citation": _read(cfg, f"citation_{test}.txt")},
        "hashes": {"instructions": _sha(ins), "user_text": _sha(usr), "schema": _sha(json.dumps(sch, sort_keys=True)),
                   "shared_parts": _sha(shared), "rules_file": rules_file_hash(cfg, region), "prompt_dir": cfg["prompt"]["dir"]},
    }
