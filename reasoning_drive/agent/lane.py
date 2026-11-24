"""The lane-level task (Milestone 5): my whole lane, one request per image.

  python main.py lane prompt --test B      the exact prompt
  python main.py lane items                the images with a final lane label
  python main.py lane run --test AB        Test A and Test B on the same images; results in results/runs/<run_id>/
  python main.py lane compare <A> <B>      paired comparison (exact McNemar, difference with 95% interval)

The model sees the photo without any box. Test A and Test B differ only in the rules step, the citation slot and
the rule block (the passages of every file in regions.<R>.lane_rules, grouped by the part of a lane they are about).
Test C is a control: the prompt of Test B with the rule block of another region (a wrong rule pack, under its real
title). B and C differ only in the content of the passages, so C shows whether the answers follow the passages.
Test D is Test A without the country: the user message does not say where the photo was taken (user_D.txt), so the
model has to infer the local conventions from the photo (as in GeoDrive-Bench). Test R is Test B with only the passages
about the elements the model itself reported in a saved Test A answer of the same image (stage 1, --from <run>): a
shorter rule block, chosen without the label.
From lane_v2 on, every passage line carries its force (mandatory, recommended, permissive, informative; norms.py) when
the prompt folder has passage_line.txt.
Runs are kept like the single-marking runs (manifest, results, scores, summary, trace) in folders named
<time>_lane<A|B>_<region>, so the two tasks never mix.
"""
from __future__ import annotations

import copy
import hashlib
import json
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from ..imageio import imread
from .. import __version__
from .client import ApiError, build_payload, call_streaming, call_with_fallback, settings_of
from .. import paths as P
from ..config import ConfigError, public, repo_of
from ..evaluation.lane_scoring import ACTIONS, compare_lane, compare_lane_repeated, parse_lane, score_failed, score_lane, summarize_lane
from .prompts import read_passages_file

ELEMENT_TITLES = [("general", "General"), ("boundary", "Lines and curbs beside a lane"),
                  ("lane_marking", "Arrows, words and symbols in a lane"), ("lane_type", "Special lanes"),
                  ("transverse", "Lines across a lane"), ("area", "Marked areas")]
SIDE_WORD = {"right": "right", "left": "left"}
LANE_TESTS = {"A": "image only", "B": "image + the region's rule passages", "C": "image + another region's rule passages (control)",
              "D": "image only, country not given", "R": "image + the passages about the elements of the model's own Test A answer"}


# ------------------------------------------------------------------ settings, schema, rules

def lane_cfg(cfg: dict) -> dict:
    """The settings of the lane task: the lane prompt folder and its output limit; everything else as configured."""
    c = copy.copy(cfg)
    c["api"] = dict(cfg["api"])
    lane = cfg.get("lane") or {}
    if lane.get("max_output_tokens"):
        c["api"]["max_output_tokens"] = int(lane["max_output_tokens"])
    c["prompt"] = dict(cfg["prompt"], dir=lane.get("prompt_dir", "prompts/lane_v1"))
    return c


def lane_schema_values(cfg: dict) -> dict:
    return json.loads((repo_of(cfg) / P.LANE_SCHEMA).read_text(encoding="utf-8"))


def lane_rule_table(cfg: dict) -> dict:
    return P.lane_action_rules(repo_of(cfg))


def _read(cfg: dict, name: str) -> str:
    p = repo_of(cfg) / cfg["lane"]["prompt_dir"] / name
    if not p.exists():
        raise ConfigError(f"Prompt file missing: {p}")
    return p.read_text(encoding="utf-8").strip()


def _sha(text: str | bytes) -> str:
    return hashlib.sha256(text if isinstance(text, bytes) else text.encode("utf-8")).hexdigest()[:16]


def lane_rule_files(cfg: dict, region: str) -> list[Path]:
    return [repo_of(cfg) / f for f in cfg["regions"][region].get("lane_rules_files") or [cfg["regions"][region]["rules_file"]]]


def lane_passages(cfg: dict, region: str) -> list[dict]:
    """The region's passages from every lane rules file, in file order, each rule ID once. A state with a parent
    (region.yaml: parent: AU) also takes the parent's passages; where the state has its own passage of a section,
    the parent's passages of that section are left out (the state changed that rule)."""
    rc = cfg["regions"][region]
    own = rc["rule_region"]
    allowed = set(rc.get("rule_regions") or [own])
    out, seen = [], set()
    for path in lane_rule_files(cfg, region):
        if not path.exists():
            raise ConfigError(f"Lane rules file of region {region} not found: {path}")
        for p in read_passages_file(path):
            if p.get("region", own) in allowed and p["rule_id"] not in seen:
                seen.add(p["rule_id"])
                out.append(p)
    if len(allowed) > 1:
        changed = {_rule_number(p) for p in out if p.get("region", own) == own} - {""}
        out = [p for p in out if p.get("region", own) == own or _rule_number(p) not in changed]
    if not out:
        raise ConfigError(f"No lane rule passages for region {region}.")
    return out


def _rule_number(p: dict) -> str:
    """The rule a passage belongs to, from its section ("132(2)", "Rule 132", "r 132" -> "132")."""
    import re
    m = re.search(r"\d+[A-Za-z]?", str(p.get("section") or ""))
    return m.group(0).upper() if m else ""


def lane_rules_hash(cfg: dict, region: str) -> str:
    h = hashlib.sha256()
    for path in lane_rule_files(cfg, region):
        h.update(path.name.encode() + b"\0" + P.text_bytes(path))
    return h.hexdigest()[:16]


def element_of(p: dict) -> str:
    """The part of a lane a passage is about (passages of the single-marking file have no 'element')."""
    if p.get("element"):
        return p["element"]
    mt = (p.get("marking_type") or "").lower()
    if "arrow" in mt:
        return "lane_marking"
    if "two-way left-turn lane" in mt:
        return "lane_type"
    return "boundary"


def _passage_text(p: dict, mode: str) -> str:
    en, zh = (p.get("text_en") or "").strip(), (p.get("text_zh") or "").strip()
    if mode == "text_zh" and zh:
        return zh
    if mode == "both" and zh and en and zh != en:
        return f"{zh}\n(English: {en})" if p.get("text_en_is_translation") else f"{en}\n(中文: {zh})"
    return en or zh


def _optional(cfg: dict, name: str) -> str | None:
    p = repo_of(cfg) / cfg["lane"]["prompt_dir"] / name
    return p.read_text(encoding="utf-8").strip() if p.exists() else None


def lane_rules_block(cfg: dict, region: str, passages: list[dict] | None = None) -> str:
    """The rule block: the header, then the passages grouped by the part of a lane they are about. The heading line of
    each passage follows passage_line.txt of the prompt folder if there is one (lane_v2: with the passage's force),
    else "[rule_id] source, section, page"."""
    rc = cfg["regions"][region]
    lines = [_read(cfg, "rules_header.txt").format(region_name=rc["name"], rules_title=rc["rules_title"]), ""]
    fmt = _optional(cfg, "passage_line.txt")
    passages = lane_passages(cfg, region) if passages is None else passages
    norms = {}
    if fmt and "{norm}" in fmt:
        from ..regulations.norms import norm_map
        norms = norm_map(repo_of(cfg), rc["rule_region"], passages)
    groups: dict[str, list] = {}
    for p in passages:
        groups.setdefault(element_of(p), []).append(p)
    for key, title in ELEMENT_TITLES:
        if not groups.get(key):
            continue
        lines += [f"## {title}", ""]
        for p in groups[key]:
            where = ", ".join(x for x in (p.get("source", ""), f"section {p['section']}" if p.get("section") else "",
                                          f"page {p['page']}" if p.get("page") else "") if x)
            head = fmt.format(rule_id=p["rule_id"], where=where, norm=norms.get(p["rule_id"], "informative")) if fmt else f"[{p['rule_id']}] {where}"
            lines += [head, _passage_text(p, rc["rule_text"]), ""]
    return "\n".join(lines).strip()


# words of the observed attributes and markings that point to the passages about them (Test R)
_PATTERN_WORDS = {"solid": ["solid"], "dashed": ["broken", "dashed"], "dotted": ["dotted"], "double_solid": ["double"],
                  "double_dashed": ["double", "reversible"], "solid_dashed": ["broken-solid", "solid and broken", "solid-and-broken",
                                                                              "broken and solid", "solid/broken", "double"]}
_ROLE_WORDS = {"center_line": ["centre", "center"], "edge_line": ["edge"], "lane_line": ["lane line"],
               "special_lane_line": ["bus", "hov", "high-occupancy", "tidal", "reversible", "preferential", "special"]}
_TOKEN_WORDS = {"arrow": ["arrow"], "no_turn": ["no u-turn", "no turn", "u-turn", "prohibited movement"], "text:only": ["only"],
                "text:bus": ["bus"], "text:hov": ["hov", "high-occupancy", "preferential"], "text:keep_clear": ["keep clear", "do not block", "grid"],
                "text:stop": ["stop"], "text:speed_limit": ["speed"], "symbol:hov_diamond": ["hov", "diamond", "preferential"],
                "symbol:bike": ["bicycle", "bike", "non-motorized"], "area:left_turn_waiting": ["waiting"],
                "area:two_way_left_turn_lane": ["two-way left"], "area:grid": ["grid", "keep clear", "do not block"],
                "area:channelizing": ["channeliz", "chevron", "diagonal"], "line:stop_line": ["stop line"],
                "line:yield_line": ["yield"], "line:stop_yield": ["stop", "yield"], "line:crosswalk": ["crosswalk", "pedestrian"]}


def retrieval_words(answer: dict) -> set:
    """Words that point to the passages about what an answer reported (both boundaries and every marking)."""
    words = set()
    for side in ("left_boundary", "right_boundary"):
        b = (answer or {}).get(side) or {}
        if b.get("pattern") and b["pattern"] != "none":
            words |= set(_PATTERN_WORDS.get(b["pattern"], []))
            words |= set(_ROLE_WORDS.get(b.get("role", ""), []))
        if b.get("curb") == "yes":
            words |= {"curb", "edge"}
    for m in (answer or {}).get("lane_markings") or []:
        t = m.get("marking", "")
        words |= set(_TOKEN_WORDS.get(t, _TOKEN_WORDS.get(t.split(":")[0], [])))
    return words


# a passage about one of these special markings is kept only if the answer reported that marking
_SPECIAL = {"two-way left": {"area:two_way_left_turn_lane", "arrow:two_way_left"}, "reversible": {"special", "double_dashed"},
            "tidal": {"special", "double_dashed"}, "wrong-way": set(), "lane-reduction": {"dotted", "arrow:merge_left", "arrow:merge_right"},
            "lane reduction": {"dotted", "arrow:merge_left", "arrow:merge_right"}, "lane drop": {"dotted"}, "non-continuing": {"dotted"},
            "channeliz": {"area:channelizing"}, "preferential": {"special", "text:hov", "text:bus", "symbol:hov_diamond"},
            "bus": {"special", "text:bus"}, "high-occupancy": {"special", "text:hov", "symbol:hov_diamond"}, "waiting": {"area:left_turn_waiting"}}


def _reported(answer: dict) -> set:
    out = {m.get("marking", "") for m in (answer or {}).get("lane_markings") or []}
    for side in ("left_boundary", "right_boundary"):
        b = (answer or {}).get(side) or {}
        out.add(b.get("pattern", ""))
        if b.get("role") == "special_lane_line":
            out.add("special")
    return out


def select_passages(passages: list[dict], answer: dict) -> list[dict]:
    """The passages a Test R prompt keeps: those about lines or markings in general, and those whose marking type names
    an element of the stage-1 answer (its pattern, role or marking), except passages about a special marking (a two-way
    left-turn lane, a reversible lane, a lane drop ...) the answer did not report. Chosen from the answer, never the label."""
    words, reported = retrieval_words(answer), _reported(answer)
    out = []
    for p in passages:
        mt = (p.get("marking_type") or "").lower()
        special = [k for k in _SPECIAL if k in mt]
        if special and not any(_SPECIAL[k] & reported for k in special):
            continue
        if element_of(p) == "general" or "(general)" in mt or any(w in mt for w in words):
            out.append(p)
    return out


def rules_region(cfg: dict, test: str, region: str) -> str | None:
    """The region whose passages the prompt lists: none in Test A, the photo's region in Test B, and in Test C the
    region set in lane.control_region (otherwise the first other region)."""
    if test in ("A", "D"):
        return None
    if test in ("B", "R"):
        return region
    if test != "C":
        raise ConfigError(f"Unknown lane test {test!r}; use A, B or C.")
    ctl = ((cfg.get("lane") or {}).get("control_region") or {}).get(region)
    others = [r for r in cfg["regions"] if r != region]
    if ctl and ctl != region and ctl in cfg["regions"]:
        return ctl
    if not others:
        raise ConfigError("Test C needs a second region with lane rule passages.")
    return others[0]


def lane_template(cfg: dict, region: str | None = None) -> str:
    text = "\n\n".join(_read(cfg, n) for n in ("role.txt", "procedure.txt", "fields.txt"))
    # boundary patterns of one country only (2026-11-17: zigzag, United Kingdom): named in that country's prompt only, so
    # the prompts of the other countries are unchanged
    for value, how in _region_only_patterns(cfg, region):
        text = text.replace("; none (no painted line).", f"; {value} ({how}); none (no painted line).", 1)
    return text


def _region_only_patterns(cfg: dict, region: str | None) -> list:
    s = lane_schema_values(cfg)
    return [(v, d["text"]) for v, d in (s.get("region_only_patterns") or {}).items() if region in d.get("regions", [])]


def _zoom_cfg(cfg: dict) -> dict | None:
    """lane_v4: zoom.json in the prompt folder = send a close-up of the road ahead as a second image (Claude, 2026-11-17)."""
    p = repo_of(cfg) / cfg["prompt"]["dir"] / "zoom.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def zoom_jpeg(item, cfg: dict, z: dict) -> bytes:
    """The road just ahead of my car, cut from the photo at its own resolution (box per dataset, fractions of the photo)."""
    import cv2
    img = imread(str(item.path), cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Image not found: {item.path}")
    h, w = img.shape[:2]
    x0, y0, x1, y1 = (z.get("boxes") or {}).get(item.dataset) or z["default_box"]
    crop = img[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)]
    ok, buf = cv2.imencode(".jpg", crop, [cv2.IMWRITE_JPEG_QUALITY, int(cfg["prompt"].get("jpeg_quality", 92))])
    if not ok:
        raise RuntimeError("Could not encode the close-up.")
    return buf.tobytes()


def lane_instructions(cfg: dict, test: str, region: str, passages: list[dict] | None = None) -> str:
    rr = rules_region(cfg, test, region)
    t = "B" if rr else "A"  # Test C and R use the words of Test B, Test D those of Test A
    text = lane_template(cfg, region).replace("{RULES_STEP}", _read(cfg, f"rules_step_{t}.txt")).replace("{CITATION}", _read(cfg, f"citation_{t}.txt"))
    return text + ("\n\n" + lane_rules_block(cfg, rr, passages) if rr else "")


def lane_user_text(cfg: dict, region: str, test: str = "A") -> str:
    rc = cfg["regions"][region]
    if test == "D":
        if _optional(cfg, "user_D.txt") is None:
            raise ConfigError(f"Test D needs user_D.txt in {cfg['lane']['prompt_dir']} (the user message without the country).")
        return _read(cfg, "user_D.txt")
    return _read(cfg, "user.txt").format(region_name=rc["name"], driving_side=SIDE_WORD.get(rc.get("driving_side", "right"), "right"))


def lane_answer_schema(cfg: dict, region: str | None = None) -> dict:
    s = lane_schema_values(cfg)
    b = dict(s["boundary"])
    only = s.get("region_only_patterns") or {}
    b["pattern"] = [v for v in b["pattern"] if v not in only or region in only[v].get("regions", [])]
    enum = lambda vals: {"type": "string", "enum": list(vals)}  # noqa: E731
    obj = lambda props: {"type": "object", "properties": props, "required": list(props), "additionalProperties": False}  # noqa: E731
    boundary = obj({"observation": {"type": "string"}, "color": enum(b["color"]), "pattern": enum(b["pattern"]),
                    "near_line": enum(b["near_line"]), "curb": enum(b["curb"]), "role": enum(b["role"]), "evidence": enum(s["evidence"])})
    num = {"anyOf": [{"type": "integer"}, {"type": "null"}]}
    props = {
        "scene": {"type": "string"},
        "lane_count": num,
        "ego_lane_index": num,
        "scene_evidence": enum(s["evidence"]),
        "left_boundary": boundary,
        "right_boundary": boundary,
        "lane_markings": {"type": "array", "items": obj({"observation": {"type": "string"}, "marking": enum(s["marking_tokens"]),
                                                          "evidence": enum(s["evidence"])})},
        "cross_check": obj({k: {"type": "string"} for k in (("close_up",) if _zoom_cfg(cfg) else ()) + ("position", "roles", "markings", "unseen", "result")}),
        "element_rules": {"type": "array", "items": obj({"element": enum(["left_boundary", "right_boundary", *s["marking_tokens"]]),
                                                          "rule_id": {"anyOf": [{"type": "string"}, {"type": "null"}]},
                                                          "meaning": {"type": "string"}})},
        "action_reasons": obj({a: {"type": "string"} for a in s["actions"]}),
        "decision_check": {"type": "string"},
        "actions": obj({a: enum(s["action_values"]) for a in s["actions"]}),
        "advice": {"type": "string"},
    }
    return obj(props)


def lane_prompt_parts(cfg: dict, test: str, region: str, passages: list[dict] | None = None) -> dict:
    ins, usr, sch = lane_instructions(cfg, test, region, passages), lane_user_text(cfg, region, test), lane_answer_schema(cfg, region)
    shared = lane_template(cfg, region) + json.dumps(sch, sort_keys=True) + usr
    rr = rules_region(cfg, test, region)
    return {"test": test, "region": region, "rules_region": rr, "instructions": ins, "user_text": usr, "schema": sch,
            "rules_block": lane_rules_block(cfg, rr, passages) if rr else "",
            "passages": len(passages) if passages is not None else None,
            "hashes": {"instructions": _sha(ins), "user_text": _sha(usr), "schema": _sha(json.dumps(sch, sort_keys=True)),
                       "shared_parts": _sha(shared), "rules_file": lane_rules_hash(cfg, rr or region), "prompt_dir": cfg["lane"]["prompt_dir"]}}


# ------------------------------------------------------------------ images with a final lane label

@dataclass
class LaneItem:
    image_id: str
    collection: str
    region: str
    dataset: str
    split: str
    path: Path
    width: int
    height: int
    label: dict = field(repr=False)


def load_lane_items(cfg: dict, region: str | None = None, split: str | None = None) -> list[LaneItem]:
    from ..labeling.core import list_trip_ids
    from ..labeling.lanes import LaneStore, lanes_csv
    from ..data import allowed_collections, workspaces
    region = region or cfg["run"]["region"]
    split = split or cfg["run"].get("split", "any")
    allowed = allowed_collections(cfg)
    items = []
    for p in workspaces(cfg):
        if allowed is not None and p.collection not in allowed:
            continue
        for sid in list_trip_ids(p):
            for r in LaneStore(lanes_csv(p, sid)).all():
                if r.get("lane_status") != "done" or r.get("region") != region:
                    continue
                if split not in ("any", "") and r.get("split") != split:
                    continue
                items.append(LaneItem(r["image_id"], p.collection, r["region"], r.get("dataset", ""), r.get("split", ""),
                                      p.data / r["source_path"], int(float(r.get("width") or 0)), int(float(r.get("height") or 0)), r))
    seed = str(cfg["run"].get("order_seed", 6216))
    items.sort(key=lambda it: hashlib.sha1(f"{seed}:{it.image_id}".encode()).hexdigest())
    return items


def plain_jpeg(item: LaneItem, cfg: dict) -> bytes:
    """The image as the model sees it in the lane task: re-encoded without any drawing (metadata dropped)."""
    import cv2
    img = imread(str(item.path), cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Image not found: {item.path}")
    ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, int(cfg["prompt"].get("jpeg_quality", 92))])
    if not ok:
        raise RuntimeError("Could not encode the image.")
    return buf.tobytes()


LABEL_KEYS = ["lane_count", "ego_index", "scene_evidence", "left_color", "left_pattern", "left_near_line", "left_curb", "left_role",
              "left_evidence", "right_color", "right_pattern", "right_near_line", "right_curb", "right_role", "right_evidence",
              "markings", "markings_evidence", *[f"act_{a}" for a in ACTIONS], "accepted_rule_ids"]


def label_hashes(items: list[LaneItem]) -> dict:
    out: dict[str, list] = {}
    for it in items:
        out.setdefault(it.collection, []).append("|".join([it.image_id, it.split] + [str(it.label.get(k, "")) for k in LABEL_KEYS]))
    return {k: hashlib.sha256("\n".join(sorted(v)).encode()).hexdigest()[:16] for k, v in out.items()}


# ------------------------------------------------------------------ mock answers

def mock_lane_answer(cfg: dict, item: LaneItem, test: str) -> dict:
    """A made-up answer for trying the pipeline without the API: the label with deterministic mistakes.

    Test A makes more mistakes than Test B on purpose, so the report has something to show. Says nothing about the model."""
    from ..labeling.lanes import lane_prefill
    lab = dict(item.label)
    rng = random.Random(f"lane:{item.image_id}:{test}")
    err = 0.12 if test == "B" else 0.30
    schema, table = lane_schema_values(cfg), lane_rule_table(cfg)
    swap = {"solid": "dashed", "dashed": "solid", "double_solid": "solid", "dotted": "dashed"}
    acts = {a: lab.get("act_" + a) or "not_applicable" for a in ACTIONS}
    side = rng.choice(["left", "right"])
    if rng.random() < err and lab.get(f"{side}_pattern") in swap:
        lab[f"{side}_pattern"] = swap[lab[f"{side}_pattern"]]
        sug = lane_prefill(table, schema, item.region, lab)["actions"]
        if sug.get(f"change_{side}"):
            acts[f"change_{side}"] = sug[f"change_{side}"]
    toks = [t for t in (lab.get("markings") or "").split(";") if t]
    if rng.random() < err:
        toks.append(rng.choice(["arrow:straight", "text:only", "line:crosswalk"]))  # a marking that may not be there
    if rng.random() < err / 2:
        flip = {"allowed": "prohibited", "prohibited": "allowed"}
        decided = [a for a, v in acts.items() if v in flip]
        if decided:
            a = rng.choice(decided)
            acts[a] = flip[acts[a]]

    def boundary(s):
        return {"observation": f"(mock) {lab.get(f'{s}_color', '')} {lab.get(f'{s}_pattern', '')}", "color": lab.get(f"{s}_color") or "none",
                "pattern": lab.get(f"{s}_pattern") or "none", "near_line": lab.get(f"{s}_near_line") or "not_applicable",
                "curb": lab.get(f"{s}_curb") or "no", "role": lab.get(f"{s}_role") or "unknown", "evidence": lab.get(f"{s}_evidence") or "full"}

    ids = [i for i in (lab.get("accepted_rule_ids") or "").split(";") if i]
    ans = {"scene": "(mock) no model was called", "lane_count": int(lab["lane_count"]) if str(lab.get("lane_count", "")).isdigit() else None,
           "ego_lane_index": int(lab["ego_index"]) if str(lab.get("ego_index", "")).isdigit() else None,
           "scene_evidence": lab.get("scene_evidence") or "full", "left_boundary": boundary("left"), "right_boundary": boundary("right"),
           "lane_markings": [{"observation": "(mock)", "marking": t, "evidence": lab.get("markings_evidence") or "full"} for t in sorted(set(toks))],
           "cross_check": {**{k: "(mock)" for k in ("position", "roles", "markings", "unseen")}, "result": "consistent"},
           "element_rules": [{"element": "left_boundary", "rule_id": (ids[0] if ids else None) if test == "B" else None, "meaning": "(mock)"}],
           "action_reasons": {a: "(mock)" for a in ACTIONS}, "decision_check": "(mock) consistent", "actions": acts,
           "advice": "(mock answer: no model was called)"}
    return {"text": json.dumps(ans), "model": "mock", "usage": {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0},
            "latency_s": 0.0, "response_id": "", "attempts": 0}


# ------------------------------------------------------------------ one request

class LaneContext:
    def __init__(self, cfg: dict, test: str, mock: bool, stage1: dict | None = None):
        self.cfg, self.test, self.mock = lane_cfg(cfg), test, mock
        self.schema, self.table = lane_schema_values(cfg), lane_rule_table(cfg)
        self.parts: dict[str, dict] = {}
        self.rule_ids: dict[str, set] = {}
        self.stage1 = stage1 or {}  # Test R: image_id -> the parsed answer of a saved Test A run
        self.lock = threading.Lock()

    def for_item(self, item) -> tuple[dict, set]:
        """The prompt of one image: the region's prompt, except in Test R, where the rule block holds only the passages
        about the elements of the image's stage-1 answer (all passages if the image has none)."""
        parts, ids = self.for_region(item.region)
        if self.test != "R" or item.image_id not in self.stage1:
            return parts, ids
        chosen = select_passages(lane_passages(self.cfg, item.region), self.stage1[item.image_id])
        return lane_prompt_parts(self.cfg, "R", item.region, chosen), ids

    def for_region(self, region: str) -> tuple[dict, set]:
        with self.lock:
            if region not in self.parts:
                self.parts[region] = lane_prompt_parts(self.cfg, self.test, region)
                rr = self.parts[region]["rules_region"] or region
                self.rule_ids[region] = {p["rule_id"] for p in lane_passages(self.cfg, rr)}
            return self.parts[region], self.rule_ids[region]


def _runs(cfg: dict) -> Path:
    return P.runs_dir(repo_of(cfg))


def ask_lane(cfg: dict, item: LaneItem, test: str, mock: bool | None = None, use_cache: bool = True, ctx: LaneContext | None = None,
             on_event=None) -> dict:
    """One request (or the cached answer), parsed and scored. With on_event, a new request is streamed and on_event(kind, text)
    gets the model's text as it is written (client.call_stream)."""
    from ..labeling.lanes import contested_lane_actions
    mock = cfg.get("mock", False) if mock is None else mock
    ctx = ctx or LaneContext(cfg, test, mock)
    lc = ctx.cfg
    parts, rule_ids = ctx.for_item(item)
    jpeg = plain_jpeg(item, lc)
    z = _zoom_cfg(lc)
    extra = [(z["text"], zoom_jpeg(item, lc, z))] if z else []
    img_sha = hashlib.sha256(jpeg + b"".join(e[1] for e in extra)).hexdigest()
    settings = settings_of(lc)
    key = hashlib.sha256(json.dumps({"task": "lane", "settings": settings, "instructions": parts["hashes"]["instructions"],
                                     "schema": parts["hashes"]["schema"], "user": parts["hashes"]["user_text"], "image": img_sha,
                                     "mock": mock}, sort_keys=True).encode()).hexdigest()
    cache = _runs(cfg) / "cache" / f"{key[:40]}.json"
    rec = {"task": "lane", "image_id": item.image_id, "collection": item.collection, "region": item.region, "dataset": item.dataset,
           "split": item.split, "test": test, "repeat": 0, "mock": mock, "cached": False,
           "request": {"settings": settings, "hashes": parts["hashes"], "image_sha256": img_sha[:16], "cache_key": key[:40],
                       **({"passages": parts["passages"]} if parts.get("passages") is not None else {})},
           "label": {k: item.label.get(k, "") for k in LABEL_KEYS},
           "response": None, "text": "", "answer": None, "parse_error": "", "error": "", "score": None,
           "time_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    if use_cache and cache.exists():
        resp = json.loads(cache.read_text(encoding="utf-8"))
        rec["cached"] = True
    else:
        try:
            if mock:
                resp = mock_lane_answer(lc, item, test)
            else:
                if item.split == "test":
                    from ..evaluation.protocol import require_frozen
                    try:
                        require_frozen(cfg)
                    except ConfigError as e:
                        rec["error"] = str(e)
                        return rec
                payload = build_payload(lc, parts, jpeg, extra)
                payload["text"]["format"]["name"] = "lane_answer"
                resp = call_streaming(lc, payload, on_event) if on_event else call_with_fallback(lc, payload)
        except ApiError as e:
            rec["error"] = str(e)
            return rec
    rec["response"] = {k: resp.get(k) for k in ("model", "usage", "latency_s", "response_id", "attempts", "reasoning_summary", "reasoning_summary_note")}
    rec["text"] = resp.get("text", "")
    ans, perr = parse_lane(rec["text"])
    rec["answer"], rec["parse_error"] = ans, perr
    if ans:
        contested = contested_lane_actions(ctx.table, ctx.schema, item.region, rec["label"])
        rec["score"] = score_lane(ans, rec["label"], test, rule_ids, contested, ctx.schema)
        if not rec["cached"]:
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(resp, ensure_ascii=False), encoding="utf-8")
    return rec


# ------------------------------------------------------------------ any photo, no label (lane try)

_SHORT = {"allowed": "yes", "stop_first": "STOP", "prohibited": "NO", "not_determined": "?", "not_applicable": "-"}


def try_images(cfg: dict, region: str, paths: list, tests: list[str], mock: bool | None = None, use_cache: bool = True,
               mirror: bool = False) -> tuple[Path, list[dict]]:
    """Ask about photos that have no label (a simulator frame, a photo of a country without labeled images): every test
    once per photo, nothing scored. With mirror, each photo is flipped left to right first, so a right-hand-traffic frame
    can stand in for a left-hand-traffic country. Writes results/trials/<time>_<region>/ with the photos as sent,
    answers.jsonl, manifest.json and summary.md (the answers of the tests side by side and what the passages changed)."""
    import cv2
    from ..imageio import imwrite
    from .runner import cost_of
    mock = cfg.get("mock", False) if mock is None else mock
    rc = cfg["regions"][region]
    repo = repo_of(cfg)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = repo / "results" / "trials" / f"{stamp}_{region}{'_mirrored' if mirror else ''}{'_mock' if mock else ''}"
    (out / "images").mkdir(parents=True, exist_ok=True)
    items, sources = [], []
    for src in paths:
        src = Path(src)
        img = imread(str(src))
        if img is None:
            raise ValueError(f"Cannot read the image {src}.")
        if mirror:
            img = cv2.flip(img, 1)
        sha = hashlib.sha256(cv2.imencode(".png", img)[1].tobytes()).hexdigest()[:10]
        name = f"{src.stem}{'_mirrored' if mirror else ''}"
        dst = out / "images" / f"{name}.png"
        imwrite(str(dst), img)
        h, w = img.shape[:2]
        items.append(LaneItem(f"try_{name}_{sha}", "try", region, "try", "try", dst, w, h, {}))
        sources.append(str(src))
    recs = []
    for t in tests:
        ctx = LaneContext(cfg, t, mock)
        for it in items:
            recs.append(ask_lane(cfg, it, t, mock, use_cache, ctx=ctx))
    n_pass = len(lane_passages(lane_cfg(cfg), region)) if "B" in tests else None
    cost = round(sum(cost_of(cfg, (r.get("response") or {}).get("usage") or {}, (r.get("response") or {}).get("model"))
                     for r in recs if not r.get("cached") and not r.get("mock") and r.get("response")), 4)
    manifest = {"kind": "lane_try", "region": region, "region_name": rc["name"], "driving_side": rc["driving_side"],
                "draft_passages": bool(rc.get("draft")), "passages": n_pass, "mirrored": mirror, "tests": tests, "mock": mock,
                "prompt_dir": cfg["lane"]["prompt_dir"], "settings": public(cfg)["api"] if not mock else {"model": "mock"},
                "sources": sources, "requests": len(recs), "errors": sum(1 for r in recs if r.get("error")),
                "cached": sum(1 for r in recs if r.get("cached")), "cost_usd": cost, "time": stamp, "version": __version__}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    with open(out / "answers.jsonl", "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    (out / "summary.md").write_text(try_summary(manifest, items, recs), encoding="utf-8")
    return out, recs


def try_summary(manifest: dict, items: list, recs: list[dict]) -> str:
    def side(a, s):
        b = (a or {}).get(f"{s}_boundary") or {}
        return " ".join(x for x in (b.get("color"), b.get("pattern"), b.get("role")) if x and x not in ("none", "unknown")) or "none"

    lines = [f"# Lane try: {manifest['region_name']} ({manifest['region']}), drives on the {manifest['driving_side']}", "",
             f"{len(items)} photos" + (" flipped left to right" if manifest["mirrored"] else "") + f", tests {', '.join(manifest['tests'])}, "
             f"prompt {manifest['prompt_dir']}" + (f", {manifest['passages']} passages" if manifest["passages"] else "")
             + (" from the DRAFT (not reviewed; not a result)" if manifest["draft_passages"] else "")
             + (" (MOCK ANSWERS)" if manifest["mock"] else ""), "",
             f"Requests {manifest['requests']}, errors {manifest['errors']}, from cache {manifest['cached']}, cost about ${manifest['cost_usd']}. "
             "Not scored: these photos have no label.", "",
             "Actions: yes = allowed, NO = prohibited, ? = not determined, - = not applicable.", ""]
    by = {(r["image_id"], r["test"]): r for r in recs}
    for it in items:
        lines += [f"## {Path(it.path).name}", "",
                  "| Test | Left boundary | Right boundary | Markings in the lane | " + " | ".join(ACTIONS) + " | Passages cited |",
                  "|---|---|---|---|" + "---|" * len(ACTIONS) + "---|"]
        acts = {}
        for t in manifest["tests"]:
            r = by.get((it.image_id, t)) or {}
            a = r.get("answer")
            if not a:
                lines.append(f"| {t} | {r.get('error') or r.get('parse_error') or 'no answer'} |" + " |" * (len(ACTIONS) + 3))
                continue
            acts[t] = a.get("actions") or {}
            marks = ", ".join(m.get("marking", "") for m in a.get("lane_markings") or []) or "none"
            cited = sorted({e.get("rule_id") for e in a.get("element_rules") or [] if e.get("rule_id")})
            lines.append(f"| {t} | {side(a, 'left')} | {side(a, 'right')} | {marks} | "
                         + " | ".join(_SHORT.get(acts[t].get(x), str(acts[t].get(x) or "")) for x in ACTIONS) + f" | {', '.join(cited) or '-'} |")
        if "A" in acts and len(acts) > 1:
            for t in [x for x in manifest["tests"] if x != "A" and x in acts]:
                ch = [f"{x} {_SHORT.get(acts['A'].get(x), acts['A'].get(x))} -> {_SHORT.get(acts[t].get(x), acts[t].get(x))}"
                      for x in ACTIONS if acts["A"].get(x) != acts[t].get(x)]
                lines += ["", f"Changed from A to {t}: " + ("; ".join(ch) if ch else "nothing")]
        lines.append("")
    return "\n".join(lines)


# ------------------------------------------------------------------ runs

def summarize_lane_records(cfg: dict, records: list[dict]) -> dict:
    """Summary of one run. An image without a readable answer is scored as failed (wrong wherever the label decides)."""
    from ..labeling.lanes import contested_lane_actions
    from .runner import cost_of
    schema, table = lane_schema_values(cfg), lane_rule_table(cfg)
    scored = []
    for r in records:
        if r.get("score"):
            scored.append({"image_id": r["image_id"], "score": r["score"]})
        elif r.get("label"):
            reason = r.get("error") and "request failed" or r.get("parse_error") or "no readable answer"
            scored.append({"image_id": r["image_id"],
                           "score": score_failed(r["label"], r["test"], contested_lane_actions(table, schema, r["region"], r["label"]), reason)})
    s = summarize_lane(scored)
    usage = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0}
    cost, lat = 0.0, []
    for r in records:
        u = (r.get("response") or {}).get("usage") or {}
        if r.get("cached") or r.get("mock"):
            continue
        usage["input_tokens"] += u.get("input_tokens", 0)
        usage["cached_input_tokens"] += (u.get("input_tokens_details") or {}).get("cached_tokens", 0) or 0
        usage["output_tokens"] += u.get("output_tokens", 0)
        cost += cost_of(cfg, u, (r.get("response") or {}).get("model") or r["request"]["settings"].get("model"))
        if (r.get("response") or {}).get("latency_s"):
            lat.append(r["response"]["latency_s"])
    s.update({"requests": len(records), "errors": sum(1 for r in records if r.get("error")),
              "readable": {"n": sum(1 for r in records if r.get("answer")), "of": len(records)},
              "cached": sum(1 for r in records if r.get("cached")), "usage": usage, "cost_usd": round(cost, 4),
              "latency_s": {"mean": round(sum(lat) / len(lat), 2), "max": max(lat)} if lat else {}})
    return {"summary": s, "per_image": {x["image_id"]: x for x in scored}}


def _pct(d: dict | None) -> str:
    return f"{d['correct']}/{d['n']} ({d['correct'] / d['n']:.0%})" if d and d.get("n") else "-"


def write_lane_summary(path: Path, manifest: dict, s: dict, reviewed: bool = False) -> None:
    lines = [f"# Lane run {manifest['run_id']}" + (" after the blind review" if reviewed else ""), "",
             *([f"Scored against the labels with the {s.get('review_decisions', 0)} decisions of the blind review applied "
                "(results/runs/review/lane_review.csv); the original scores are in summary.md.", ""] if reviewed else []),
             f"Test {manifest['test']} ({LANE_TESTS.get(manifest['test'], '')}"
             + (f", passages of {manifest.get('rules_region')}" if manifest['test'] == 'C' else "") + f"), region {manifest['region']}, "
             f"{manifest['n_items']} images, one request each, model {manifest['settings']['model']}"
             + (" (MOCK ANSWERS, no model was called)" if manifest["mock"] else ""), "",
             f"- Lane identified (both boundaries and the markings): {_pct(s.get('lane'))}; without the lines across the lane: {_pct(s.get('lane_core'))}",
             f"- Lane actions (every action the label decides, contested cells excluded): {_pct(s.get('output2'))}",
             f"- Left boundary: {_pct(s.get('left_boundary'))}; right boundary: {_pct(s.get('right_boundary'))}; both: {_pct(s.get('both_boundaries'))}",
             f"- Markings in the lane, exact set: {_pct(s.get('markings_exact'))} (without the lines across the lane {_pct(s.get('markings_core_exact'))}); "
             f"added (not in the label): {s.get('markings_added', 0)}, of them lines across the lane {s.get('added_transverse', 0)}, "
             f"by the evidence the answer gave {s.get('added_by_evidence', {})}; missed: {s.get('markings_missed', 0)}",
             f"- Lane count: {_pct(s.get('lane_count'))}; position of my lane: {_pct(s.get('ego_index'))}",
             f"- Unsafe errors (label prohibited, answer allowed): {s.get('unsafe_errors', 0)} {s.get('unsafe_by_action', {})}; "
             f"over-cautious: {s.get('over_cautious_errors', 0)}; contested unsafe: {s.get('contested_unsafe_errors', 0)}",
             f"- Prohibited actions also prohibited by the answer: {_pct(s.get('prohibited_recall'))}",
             f"- Actions decided where the label has no governing marking: {s.get('extra_decisions', 0)}",
             f"- Answers that contradict themselves: {s.get('inconsistent_answers', 0)} {s.get('consistency_kinds', {})}",
             f"- Citations (Test B and C): {s.get('citations', {})}; IDs written with brackets (read without them): {s.get('citation_ids_with_brackets', 0)}",
             f"- Boundary evidence: {s.get('boundary_evidence', {})}",
             f"- Readable answers: {s['readable']['n']}/{s['readable']['of']} (an unreadable or failed answer counts as wrong); errors: {s['errors']}; from cache: {s['cached']}",
             f"- Tokens: {s.get('usage', {})}; cost about ${s.get('cost_usd', 0)}; latency: {s.get('latency_s', {})}", "",
             "| Action | Decided by the label | Correct |", "|---|---|---|"]
    for a, v in (s.get("actions") or {}).items():
        lines.append(f"| {a} | {v['n']} | {v['correct']} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_lane(cfg: dict, test: str | None = None, region: str | None = None, limit: int | None = None, split: str | None = None,
             mock: bool | None = None, image_ids: list | None = None, progress=None, log=print, use_cache: bool = True,
             again: bool = False, stage1_run: str | None = None) -> str:
    """One test on the lane-labeled images of a region. Test R needs stage1_run, a saved Test A run of the same images
    whose answers choose the passages. On the test split (real answers) the frozen protocol must match
    (protocol.py) and each test runs once per region; again=True runs it again and says so in the manifest."""
    from ..evaluation.protocol import protocol_check, require_frozen
    from .runner import code_hash, git_commit, split_version
    test = test or cfg["run"]["test"]
    region = region or cfg["run"]["region"]
    limit = cfg["run"].get("limit", 0) if limit is None else limit
    mock = cfg.get("mock", False) if mock is None else mock
    items = load_lane_items(cfg, region, split)
    if image_ids:
        want = set(image_ids)
        items = [it for it in items if it.image_id in want]
    if limit:
        items = items[:int(limit)]
    if not items:
        raise ValueError(f"No final lane labels for region {region} in the configured workspaces "
                         "(label lanes with: python main.py label --data <workspace> lanes).")
    on_test = not mock and any(it.split == "test" for it in items)
    protocol = require_frozen(cfg) if on_test else protocol_check(cfg)
    if on_test and not again:
        for r in list_lane_runs(cfg):
            if not r["finished"] or r["mock"] or r["test"] != test or r["region"] != region:
                continue
            m = load_lane_run(cfg, r["run_id"])["manifest"]
            if m.get("split") in ("test", "any") and (m.get("protocol") or {}).get("frozen_utc") == protocol["frozen_utc"]:
                raise ConfigError(f"Test {test} already ran on the test images of region {region} with this protocol ({r['run_id']}). "
                                  "The test set is run once; use --again to run it again (the manifest records it).")
    base = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_lane{test}_{region}" + ("_mock" if mock else "")
    run_id, k = base, 1
    while True:
        out = _runs(cfg) / run_id
        try:
            out.mkdir(parents=True, exist_ok=False)
            break
        except FileExistsError:
            k += 1
            run_id = f"{base}_{k}"
    stage1 = {}
    if test == "R":
        if not stage1_run:
            raise ConfigError("Test R needs a saved Test A run of the same images: --from <run_id>.")
        src = load_lane_run(cfg, stage1_run)
        if src["manifest"].get("test") not in ("A", "D"):
            raise ConfigError(f"{stage1_run} is a Test {src['manifest'].get('test')} run; Test R takes its elements from a Test A (or D) run.")
        stage1 = {r["image_id"]: r["answer"] for r in src["records"] if r.get("answer")}
    ctx = LaneContext(cfg, test, mock, stage1)
    parts, _ = ctx.for_region(region)
    manifest = {"run_id": run_id, "task": "lane", "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "tool": f"reasoning_drive {__version__}", "git_commit": git_commit(repo_of(cfg)), "code_sha": lane_code_hash(repo_of(cfg)),
                "marking_code_sha": code_hash(repo_of(cfg)), "test": test, "region": region, "mock": mock, "use_cache": use_cache,
                "repeats": 1, "n_items": len(items), "rules_region": parts["rules_region"], "settings": settings_of(ctx.cfg), "prompt_hashes": parts["hashes"],
                "label_sets": label_hashes(items), "split": split or cfg["run"].get("split", "any"), "split_version": split_version(cfg),
                "protocol": {k: protocol.get(k) for k in ("frozen", "matches", "frozen_utc")}, "again": bool(again),
                **({"stage1_run": stage1_run, "stage1_answers": len(stage1)} if test == "R" else {}),
                "items": [it.image_id for it in items], "config": public(cfg)}
    manifest["config"]["api"].pop("api_key_hint", None)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    records, lock, done, t0 = [], threading.Lock(), [0], time.time()

    def work(it):
        rec = ask_lane(cfg, it, test, mock, use_cache, ctx)
        with lock:
            records.append(rec)
            with open(out / "results.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            done[0] += 1
            if progress:
                progress(done[0], len(items), rec)
        return rec

    with ThreadPoolExecutor(max_workers=1 if mock else max(1, int(cfg["api"].get("parallel", 5)))) as ex:
        list(ex.map(work, items))
    res = summarize_lane_records(cfg, records)
    res["summary"]["elapsed_s"] = round(time.time() - t0, 1)
    (out / "scores.json").write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    write_lane_summary(out / "summary.md", manifest, res["summary"])
    write_lane_trace(cfg, run_id)
    s = res["summary"]
    errs = [r["error"] for r in records if r.get("error")]
    log(f"Lane run {run_id}: lane {s.get('lane', {}).get('acc')}, actions {s.get('output2', {}).get('acc')}, unsafe {s.get('unsafe_errors')}, "
        f"{s['errors']} errors, cost about ${s['cost_usd']}" + (f". First error: {errs[0]}" if errs else ""))
    if errs:
        log(f"{len(errs)} of {len(records)} requests failed, so this run is incomplete. Fix the cause and run the same command "
            "again: the answers that arrived are cached and are not paid again.")
    return run_id


def run_lane_pair(cfg: dict, region: str | None = None, limit: int | None = None, split: str | None = None, mock: bool | None = None,
                  progress=None, log=print, use_cache: bool = True, again: bool = False) -> dict:
    out, errors = {}, {}

    def one(test):
        try:
            out[test] = run_lane(cfg, test, region, limit, split, mock, progress=(lambda d, n, r: progress(test, d, n, r)) if progress else None,
                                 log=log, use_cache=use_cache, again=again)
        except Exception as e:  # noqa: BLE001
            errors[test] = e

    threads = [threading.Thread(target=one, args=(t,)) for t in ("A", "B")]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    if errors:
        raise next(iter(errors.values()))
    return out


LANE_CODE_FILES = ["reasoning_drive/agent/lane.py", "reasoning_drive/evaluation/lane_scoring.py", "reasoning_drive/agent/client.py",
                   "reasoning_drive/labeling/lanes.py", P.LANE_SCHEMA]


def lane_code_hash(repo: Path) -> str:
    h = hashlib.sha256()
    for p in [Path(repo) / f for f in LANE_CODE_FILES] + P.rule_table_files(repo, lane=True):
        if p.exists():
            h.update(p.name.encode() + b"\0" + P.text_bytes(p))
    return h.hexdigest()[:16]


def list_lane_runs(cfg: dict) -> list[dict]:
    out = []
    for d in sorted(_runs(cfg).glob("*_lane*"), reverse=True):
        m, s = d / "manifest.json", d / "scores.json"
        if not m.exists():
            continue
        man = json.loads(m.read_text(encoding="utf-8"))
        sc = json.loads(s.read_text(encoding="utf-8"))["summary"] if s.exists() else {}
        out.append({"run_id": man["run_id"], "test": man["test"], "region": man["region"], "mock": man["mock"], "n_items": man["n_items"],
                    "model": man["settings"]["model"], "lane": (sc.get("lane") or {}).get("acc"), "output2": (sc.get("output2") or {}).get("acc"),
                    "unsafe": sc.get("unsafe_errors"), "cost_usd": sc.get("cost_usd"), "errors": sc.get("errors"), "finished": s.exists()})
    return out


def load_lane_run(cfg: dict, run_id: str) -> dict:
    from .runner import load_run
    return load_run(cfg, run_id)


def _per_image(cfg: dict, run: dict, reviewed: bool) -> dict:
    if not run["scores"]:
        raise ValueError("The runs must be finished.")
    if not reviewed:
        return run["scores"]["per_image"]
    return summarize_lane_records(cfg, rescore_records(cfg, run["records"], True))["per_image"]


def compare_lane_runs(cfg: dict, run_a: str, run_b: str, reviewed: bool = False) -> dict:
    a, b = load_lane_run(cfg, run_a), load_lane_run(cfg, run_b)
    res = compare_lane(_per_image(cfg, a, reviewed), _per_image(cfg, b, reviewed))
    res["reviewed"] = reviewed
    ma, mb = a["manifest"], b["manifest"]
    res.update({"same_settings": ma["settings"] == mb["settings"],
                "same_shared_prompt": ma["prompt_hashes"]["shared_parts"] == mb["prompt_hashes"]["shared_parts"],
                "tests": [ma["test"], mb["test"]], "runs": [run_a, run_b]})
    return res


def compare_lane_pooled(cfg: dict, pairs: list[tuple[str, str]], reviewed: bool = False) -> dict:
    """One paired comparison over several pairs of runs: more images (for example China and US) and, when an image is in
    more than one pair (repeated runs), the share of correct answers per image (compare_lane_repeated)."""
    a_all: dict[str, list] = {}
    b_all: dict[str, list] = {}
    tests, used = set(), (set(), set())
    for ra, rb in pairs:
        a, b = load_lane_run(cfg, ra), load_lane_run(cfg, rb)
        tests.add((a["manifest"]["test"], b["manifest"]["test"]))
        for run, acc, seen in ((a, a_all, used[0]), (b, b_all, used[1])):
            if run["manifest"]["run_id"] in seen:  # a run in several pairs (for example one control against two repeats) counts once
                continue
            seen.add(run["manifest"]["run_id"])
            for k, v in _per_image(cfg, run, reviewed).items():
                acc.setdefault(f"{run['manifest']['region']}:{k}", []).append(v["score"])
    if all(len(v) == 1 for v in list(a_all.values()) + list(b_all.values())):
        res = compare_lane({k: {"score": v[0]} for k, v in a_all.items()}, {k: {"score": v[0]} for k, v in b_all.items()})
    else:
        res = compare_lane_repeated(a_all, b_all)
    res.update({"tests": sorted(tests)[0] if len(tests) == 1 else sorted(tests), "runs": pairs, "pooled": True, "reviewed": reviewed})
    return res


def find_lane_run(cfg: dict, test: str, region: str, split: str, mock: bool | None = None) -> str | None:
    """The newest finished lane run with exactly these settings, prompt, images and labels, without errors."""
    mock = cfg.get("mock", False) if mock is None else mock
    items = load_lane_items(cfg, region, split)
    ids, labels = sorted(it.image_id for it in items), label_hashes(items)
    lc = lane_cfg(cfg)
    parts, want = lane_prompt_parts(lc, test, region), settings_of(lc)
    for r in list_lane_runs(cfg):
        if not r["finished"] or r["test"] != test or r["region"] != region or r["mock"] != mock or r["errors"]:
            continue
        m = load_lane_run(cfg, r["run_id"])["manifest"]
        if (m["settings"] == want and all(m["prompt_hashes"].get(k) == parts["hashes"][k] for k in ("instructions", "user_text", "schema"))
                and sorted(m["items"]) == ids and m.get("label_sets") == labels):
            return r["run_id"]
    return None


def find_or_run_lane(cfg: dict, test: str, region: str, split: str, mock: bool | None = None, log=print,
                     stage1_run: str | None = None) -> str:
    mock = cfg.get("mock", False) if mock is None else mock
    rid = find_lane_run(cfg, test, region, split, mock)
    if rid:
        log(f"Lane Test {test}: reusing run {rid}.")
        return rid
    rid = run_lane(cfg, test, region, 0, split, mock, log=log, stage1_run=stage1_run)
    bad = [r["error"] for r in load_lane_run(cfg, rid)["records"] if r.get("error")]
    if bad:
        raise RuntimeError(f"{len(bad)} requests of run {rid} failed. First error: {bad[0]}")
    return rid


def rescore_records(cfg: dict, records: list[dict], reviewed: bool = False) -> list[dict]:
    """The records scored again (no API calls) against the label snapshot kept with each answer; with reviewed=True,
    against that label with the blind review decisions applied (review.label_after_review). Returns copies."""
    from ..labeling.lanes import contested_lane_actions
    from ..evaluation.review import decisions_by_image, label_after_review, load_decisions
    lc = lane_cfg(cfg)
    schema, table = lane_schema_values(cfg), lane_rule_table(cfg)
    dec = decisions_by_image(load_decisions(cfg)) if reviewed else {}
    ids: dict[str, set] = {}
    out = []
    for r in records:
        r = dict(r)
        if reviewed:
            r["label"] = label_after_review(r["label"], dec.get(r["image_id"]))
        if r.get("answer"):
            rr = rules_region(lc, r["test"], r["region"]) or r["region"]
            ids.setdefault(rr, {p["rule_id"] for p in lane_passages(lc, rr)})
            r["score"] = score_lane(r["answer"], r["label"], r["test"], ids[rr],
                                    contested_lane_actions(table, schema, r["region"], r["label"]), schema)
        out.append(r)
    return out


def rescore_lane_run(cfg: dict, run_id: str, reviewed: bool = False) -> dict:
    """Score the saved answers of a lane run again (no API calls). reviewed=False rewrites results.jsonl, scores.json and
    summary.md; reviewed=True writes scores_reviewed.json and summary_reviewed.md and keeps the original scores."""
    run = load_lane_run(cfg, run_id)
    records = rescore_records(cfg, run["records"], reviewed)
    d = _runs(cfg) / run_id
    if not reviewed:
        with open(d / "results.jsonl", "w", encoding="utf-8") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    res = summarize_lane_records(cfg, records)
    res["summary"]["elapsed_s"] = ((run["scores"] or {}).get("summary") or {}).get("elapsed_s")
    res["summary"]["rescored_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if reviewed:
        from ..evaluation.review import load_decisions
        res["summary"]["review_decisions"] = len(load_decisions(cfg))
    suffix = "_reviewed" if reviewed else ""
    (d / f"scores{suffix}.json").write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    write_lane_summary(d / f"summary{suffix}.md", run["manifest"], res["summary"], reviewed)
    return res["summary"]


# ------------------------------------------------------------------ trace and tables

def _wrap(label: str, text: str, indent: int = 0, width: int = 24) -> list[str]:
    import textwrap
    head = (" " * indent + label).ljust(width)
    body = textwrap.wrap(str(text), 110 - len(head)) or [""]
    return [(head + body[0]).rstrip()] + [(" " * len(head) + b).rstrip() for b in body[1:]]


def lane_trace_text(rec: dict, passage_map: dict | None = None) -> str:
    resp = rec.get("response") or {}
    head = f"{rec.get('image_id', '')} | lane | Test {rec.get('test', '')} | {resp.get('model') or 'no answer'}" + \
        (" | from cache" if rec.get("cached") else "") + (" | MOCK" if rec.get("mock") else "")
    out = [head, "-" * min(110, len(head))]
    if rec.get("error"):
        return "\n".join(out + _wrap("Error", rec["error"]))
    a = rec.get("answer")
    if not a:
        return "\n".join(out + _wrap("Unreadable answer", f"{rec.get('parse_error', '')}: {rec.get('text', '')[:300]}"))
    out += _wrap("Step 1  Scene", f"{a.get('scene', '')} (lanes {a.get('lane_count')}, mine {a.get('ego_lane_index')}, {a.get('scene_evidence')})")
    for side in ("left", "right"):
        b = a.get(f"{side}_boundary") or {}
        out += _wrap(f"Step 2  {side.capitalize()}", b.get("observation", ""))
        out += _wrap("", f"{b.get('color')} {b.get('pattern')}" + (f" (near line {b.get('near_line')})" if b.get("pattern") == "solid_dashed" else "")
                     + f", curb {b.get('curb')}, {b.get('role')}, evidence {b.get('evidence')}", 4)
    marks = a.get("lane_markings") or []
    out += _wrap("Step 3  Markings", "; ".join(f"{m.get('marking')} ({m.get('evidence')}): {m.get('observation')}" for m in marks) or "none")
    cc = a.get("cross_check") or {}
    out += _wrap("Step 4  Cross-check", " | ".join(f"{k}: {v}" for k, v in cc.items()))
    for e in a.get("element_rules") or []:
        rid = e.get("rule_id")
        p = (passage_map or {}).get(rid) if rid else None
        cite = f" [{rid}]" + (f' "{(p.get("text_en") or p.get("text_zh") or "")[:160]}"' if p else "") if rid else ""
        out += _wrap("Step 5  Rule", f"{e.get('element')}: {e.get('meaning')}{cite}")
    reasons, acts = a.get("action_reasons") or {}, a.get("actions") or {}
    sc = rec.get("score") or {}
    lab = rec.get("label") or {}
    for act in ACTIONS:
        mark = ""
        if act in (sc.get("actions") or {}):
            mark = " (correct)" if sc["actions"][act] else f" (WRONG, label {lab.get('act_' + act)})"
        elif act in (sc.get("contested") or {}):
            mark = " (contested, " + ("correct)" if sc["contested"][act] else f"label {lab.get('act_' + act)})")
        out += _wrap(f"Step 6  {act}", f"{acts.get(act)}{mark}: {reasons.get(act, '')}")
    out += _wrap("Step 7  Reflect", a.get("decision_check", ""))
    out += _wrap("Advice", a.get("advice", ""))
    if resp.get("reasoning_summary"):
        out += _wrap("Model's summary", resp["reasoning_summary"])
    if sc:
        sides = {s: (sc.get("sides", {}).get(s) or {}).get("all") for s in ("left", "right")}
        out += _wrap("Score", f"lane {sc.get('lane')}, boundaries {sides}, markings "
                     f"{(sc.get('markings') or {}).get('exact')} (added {(sc.get('markings') or {}).get('added')}, missed {(sc.get('markings') or {}).get('missed')}), "
                     f"actions {sc.get('output2')}, unsafe {sc.get('unsafe')}, citation {sc.get('citation')}, contradictions {sc.get('consistency')}")
    u = resp.get("usage") or {}
    if u:
        out += _wrap("Tokens", f"in {u.get('input_tokens', 0)}, out {u.get('output_tokens', 0)}, {resp.get('latency_s')} s")
    return "\n".join(out)


def write_lane_trace(cfg: dict, run_id: str) -> Path:
    run = load_lane_run(cfg, run_id)
    lc = lane_cfg(cfg)
    pm = {p["rule_id"]: p for p in lane_passages(lc, run["manifest"]["region"])}
    text = "\n\n".join(lane_trace_text(r, pm) for r in sorted(run["records"], key=lambda r: r["image_id"]))
    p = _runs(cfg) / run_id / "trace.md"
    p.write_text(f"# Reasoning of lane run {run_id}\n\n```text\n{text}\n```\n", encoding="utf-8")
    return p


def lane_table_markdown(cfg: dict, rows: list[tuple[str, str, str]]) -> str:
    """rows: (variant, run_id, settings). One line per run."""
    head = ["Variant", "Run", "Settings", "Lane identified", "Without lines across", "Lane actions", "Left", "Right", "Markings exact",
            "Markings added", "Unsafe", "Prohibited kept", "Contradictions", "Cost ($)"]
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for name, rid, st in rows:
        s = (load_lane_run(cfg, rid)["scores"] or {}).get("summary", {})
        lines.append("| " + " | ".join([name, rid, st, _pct(s.get("lane")), _pct(s.get("lane_core")), _pct(s.get("output2")), _pct(s.get("left_boundary")),
                                         _pct(s.get("right_boundary")), _pct(s.get("markings_exact")), str(s.get("markings_added", "")),
                                         str(s.get("unsafe_errors", "")), _pct(s.get("prohibited_recall")), str(s.get("inconsistent_answers", "")),
                                         str(s.get("cost_usd", ""))]) + " |")
    return "\n".join(lines)
