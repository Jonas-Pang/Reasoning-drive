"""Evaluation: compare answers with the FINAL labels (Milestone 3, requirements 3–6).

Output 1 is correct when the marking type (and the arrow type for arrows) matches.
Output 2 is correct when every action the marking decides (label not "not_applicable") matches; actions in a
"contested" cell of the rule table are left out of the main score and reported separately.
"""
from __future__ import annotations

import json
import math
from collections import Counter, defaultdict

ACTIONS = ["cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_center_lane_to_wait"]


def parse(text: str) -> tuple[dict | None, str]:
    try:
        ans = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None, "not JSON"
    if not isinstance(ans, dict):
        return None, "not a JSON object"
    for k in ("evidence", "marking", "actions"):
        if k not in ans:
            return None, f"missing {k}"
    if not isinstance(ans["marking"], dict) or not isinstance(ans["actions"], dict):
        return None, "bad structure"
    return ans, ""


def contested_actions(table: dict, region: str, label: dict) -> set:
    from video_tool.core import rule_key
    key = rule_key(label.get("marking_type", ""), label.get("arrow_type", ""), label.get("dashed_side", ""))
    return set((table.get(region, {}).get(key) or {}).get("contested", []))


def evidence_group(ans: dict, label: dict, o1: bool, o2: bool | None) -> str:
    """The five evidence groups."""
    want, got = label.get("expected_evidence", ""), ans.get("evidence", "")
    if want == "full":
        if got in ("partial", "insufficient"):
            return "over_withholding"
        return "correct" if o1 and o2 is not False else "wrong"
    if want == "partial":
        if got == "full":
            return "unsupported_guess"
        if got == "insufficient":
            return "over_withholding"
        return "appropriate_withholding" if o1 else "wrong"
    if want == "insufficient":
        return "appropriate_withholding" if got == "insufficient" else "unsupported_guess"
    return "wrong"


MOVES = ["go_straight", "turn_left", "turn_right", "u_turn"]
GOVERNS = {"line": {"cross_line"}, "arrow": set(MOVES), "two_way_left_turn_lane": {"enter_center_lane_to_wait", "turn_left"},
           "other": set(), "none_visible": set()}


def governed(marking_type: str) -> set:
    """The actions a marking class governs (task definition shared by the labeling guide and prompt v2)."""
    if marking_type.startswith(("white_", "yellow_")):
        return GOVERNS["line"]
    return GOVERNS.get(marking_type, set())


def consistency_issues(ans: dict) -> list[str]:
    """Contradictions inside one answer, found without the label: a hallucination indicator.

    The answer claims something its own description of the marking cannot support: an action set for a marking
    class that does not govern it, not_determined although the evidence is called full, an arrow without
    directions, or directions on something that is not an arrow."""
    m, acts = ans.get("marking") or {}, ans.get("actions") or {}
    mt, ev = m.get("marking_type") or "", ans.get("evidence")
    out = []
    extra = [a for a in ACTIONS if a not in governed(mt) and acts.get(a) not in (None, "not_applicable")]
    if extra:
        out.append(f"{mt} does not govern {', '.join(extra)}")
    if ev == "full" and any(acts.get(a) == "not_determined" for a in governed(mt)):
        out.append("not_determined with full evidence")
    if mt == "arrow" and ev == "full" and not m.get("arrow_type"):
        out.append("arrow without directions")
    if mt != "arrow" and m.get("arrow_type"):
        out.append("arrow directions on a non-arrow")
    return out


def score_one(ans: dict, label: dict, test: str, region_rule_ids: set, contested: set) -> dict:
    m = ans.get("marking") or {}
    mt_ok = m.get("marking_type") == label.get("marking_type")
    at_ok = label.get("marking_type") != "arrow" or (m.get("arrow_type") or "") == (label.get("arrow_type") or "")
    o1 = bool(mt_ok and at_ok)
    per = {}
    for a in ACTIONS:
        want = label.get("act_" + a, "")
        if want in ("", "not_applicable"):
            continue
        per[a] = (ans.get("actions") or {}).get(a) == want
    main = {a: ok for a, ok in per.items() if a not in contested}
    cont = {a: ok for a, ok in per.items() if a in contested}
    o2 = all(main.values()) if main else None
    got = ans.get("actions") or {}
    unsafe_all = [a for a in ACTIONS if label.get("act_" + a) == "prohibited" and got.get(a) == "allowed"]
    cautious_all = [a for a in ACTIONS if label.get("act_" + a) == "allowed" and got.get(a) in ("prohibited", "not_determined")]
    cite = None
    if test == "B":
        cid = ans.get("cited_rule_id")
        accepted = {i for i in (label.get("accepted_rule_ids") or "").split(";") if i}
        if not cid:
            cite = "none" if accepted else "none_needed"  # e.g. a crosswalk: no passage in the pack, so no citation is right
        elif cid in accepted:
            cite = "accepted"
        elif cid in region_rule_ids:
            cite = "in_pack_not_accepted"
        else:
            cite = "unlisted"
    return {"output1": o1, "output2": o2, "actions": per, "contested": cont, "position": m.get("position") == label.get("position"),
            "evidence_group": evidence_group(ans, label, o1, o2), "citation": cite, "consistency": consistency_issues(ans),
            # contested cells are kept out of the main error counts, like out of the main score
            "unsafe": [a for a in unsafe_all if a not in contested], "over_cautious": [a for a in cautious_all if a not in contested],
            "contested_unsafe": [a for a in unsafe_all if a in contested],
            "contested_over_cautious": [a for a in cautious_all if a in contested],
            "o1_answer": m.get("marking_type", "") + (f"/{m['arrow_type']}" if m.get("arrow_type") else ""),
            "o1_label": label.get("marking_type", "") + (f"/{label['arrow_type']}" if label.get("arrow_type") else "")}


def majority(records: list[dict]) -> dict:
    """Per image: the majority answer of the repeats for each output (requirement 6), and whether it was stable."""
    by = defaultdict(list)
    for r in records:
        if r.get("answer"):
            by[r["image_id"]].append(r)
    out = {}
    for iid, rs in by.items():
        o1s = Counter((r["answer"]["marking"].get("marking_type"), r["answer"]["marking"].get("arrow_type")) for r in rs)
        o2s = Counter(json.dumps(r["answer"]["actions"], sort_keys=True) for r in rs)
        top1, n1 = o1s.most_common(1)[0]
        top2, n2 = o2s.most_common(1)[0]
        pick = next(r for r in rs if (r["answer"]["marking"].get("marking_type"), r["answer"]["marking"].get("arrow_type")) == top1)
        pick2 = next(r for r in rs if json.dumps(r["answer"]["actions"], sort_keys=True) == top2)
        out[iid] = {"record": pick, "actions_record": pick2, "n": len(rs),
                    "stable_o1": len(o1s) == 1, "stable_o2": len(o2s) == 1,
                    "no_majority_o2": n2 * 2 <= len(rs) and len(rs) > 1}
    return out


def mcnemar_exact(b: int, c: int) -> float | None:
    """Two-sided exact McNemar test (binomial test on the discordant pairs)."""
    n = b + c
    if n == 0:
        return None
    k = min(b, c)
    p = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return min(1.0, 2 * p)


def summarize(scored: list[dict], usage: dict | None = None) -> dict:
    """scored: one dict per image (majority answer) with 'score' and label info."""
    n = len(scored)
    if not n:
        return {"n": 0}
    o1 = sum(1 for s in scored if s["score"]["output1"])
    o2_items = [s for s in scored if s["score"]["output2"] is not None]
    o2 = sum(1 for s in o2_items if s["score"]["output2"])
    per = {}
    for a in ACTIONS:
        vals = [s["score"]["actions"][a] for s in scored if a in s["score"]["actions"] and a not in s["score"]["contested"]]
        if vals:
            per[a] = {"n": len(vals), "correct": sum(vals)}
    cont = [ok for s in scored for ok in s["score"]["contested"].values()]
    groups = Counter(s["score"]["evidence_group"] for s in scored)
    cites = Counter(s["score"]["citation"] for s in scored if s["score"]["citation"] is not None)
    conf = Counter((s["score"]["o1_label"], s["score"]["o1_answer"]) for s in scored)
    by_type = defaultdict(lambda: [0, 0])
    for s in scored:
        by_type[s["score"]["o1_label"]][0] += 1
        by_type[s["score"]["o1_label"]][1] += int(s["score"]["output1"])
    return {
        "n": n,
        "output1": {"correct": o1, "n": n, "acc": round(o1 / n, 3)},
        "output2": {"correct": o2, "n": len(o2_items), "acc": round(o2 / len(o2_items), 3) if o2_items else None},
        "actions": per,
        "contested": {"n": len(cont), "correct": sum(cont)},
        "position": {"correct": sum(1 for s in scored if s["score"]["position"]), "n": n},
        "evidence_groups": dict(groups),
        "citations": dict(cites),
        "unsafe_errors": sum(len(s["score"]["unsafe"]) for s in scored),
        "over_cautious_errors": sum(len(s["score"]["over_cautious"]) for s in scored),
        "contested_unsafe_errors": sum(len(s["score"].get("contested_unsafe", [])) for s in scored),
        "inconsistent_answers": sum(1 for s in scored if s["score"].get("consistency")),
        "contested_over_cautious_errors": sum(len(s["score"].get("contested_over_cautious", [])) for s in scored),
        "output1_by_type": {k: {"n": v[0], "correct": v[1]} for k, v in sorted(by_type.items())},
        "confusion": [{"label": k[0], "answer": k[1], "count": v} for k, v in sorted(conf.items())],
        "usage": usage or {},
    }


def compare(a_scored: dict, b_scored: dict) -> dict:
    """Paired comparison on the images both runs answered (McNemar for each output)."""
    ids = sorted(set(a_scored) & set(b_scored))
    out = {"n": len(ids)}
    for key in ("output1", "output2"):
        pairs = [(a_scored[i]["score"][key], b_scored[i]["score"][key]) for i in ids
                 if a_scored[i]["score"][key] is not None and b_scored[i]["score"][key] is not None]
        b = sum(1 for x, y in pairs if not x and y)   # only B right
        c = sum(1 for x, y in pairs if x and not y)   # only A right
        out[key] = {"n": len(pairs), "acc_A": round(sum(x for x, _ in pairs) / len(pairs), 3) if pairs else None,
                    "acc_B": round(sum(y for _, y in pairs) / len(pairs), 3) if pairs else None,
                    "only_B_right": b, "only_A_right": c, "p_value": mcnemar_exact(b, c)}
    return out
