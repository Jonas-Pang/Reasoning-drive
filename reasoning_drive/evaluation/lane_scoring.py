"""Evaluation of the lane-level task: compare one answer per image with the FINAL lane label.

Per image:
  * scene: lane count and position of my lane (when the label gives them);
  * boundaries: colour, pattern (with the line nearer my lane for a solid-and-broken pair) and curb per side, the
    role separately; a side is "correct" when colour, pattern and curb all match;
  * markings: the set of marking tokens in my lane; exact set match, and the tokens the answer added (a direct
    hallucination count, with the evidence level the answer gave them) or missed; the same without the lines across
    the lane (stop and yield lines, crosswalks), whose extent in "my lane" is the least clear part of the definition;
  * lane identification: both sides and the marking set correct (the lane-level Output 1), also without the lines
    across the lane;
  * actions (the lane-level Output 2): every action the label decides matches; contested cells (project
    conventions) are scored separately; unsafe errors (label prohibited, answer allowed or stop_first; label stop_first, answer allowed), over-cautious errors,
    and the share of prohibited cells the answer also prohibits;
  * citations (Test B and the control Test C; IDs written with brackets are counted, then read without them), and
    contradictions inside the answer found without the label.

An image whose answer is missing or unreadable counts as wrong in every measure the label defines (score_failed),
so a failed request cannot make a test look better; the comparisons pair every image of both runs.
"""
from __future__ import annotations

import json
from collections import Counter

import math

from .scoring import mcnemar_exact

SIDES = ["left", "right"]
ACTIONS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"]
MOVES = ["go_straight", "turn_left", "turn_right", "u_turn"]
PHYSICAL = ["color", "pattern", "curb"]
CITING_TESTS = ("B", "C")


def transverse(token: str) -> bool:
    """A line across the lane (stop line, yield line, crosswalk)."""
    return str(token).startswith("line:")


def norm_rule_id(rule_id) -> str:
    """A cited ID as listed: without surrounding brackets, parentheses or spaces ("[CN-5.2.3]" -> "CN-5.2.3")."""
    return str(rule_id or "").strip().strip("[]()【】 ").strip()


def tokens_of(text) -> set:
    if isinstance(text, (list, tuple, set)):
        return {t for t in text if t}
    return {t.strip() for t in str(text or "").replace(",", ";").split(";") if t.strip()}


def parse_lane(text: str) -> tuple[dict | None, str]:
    try:
        ans = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None, "not JSON"
    if not isinstance(ans, dict):
        return None, "not a JSON object"
    for k in ("left_boundary", "right_boundary", "lane_markings", "actions"):
        if k not in ans:
            return None, f"missing {k}"
    if not all(isinstance(ans[k], dict) for k in ("left_boundary", "right_boundary", "actions")) or not isinstance(ans["lane_markings"], list):
        return None, "bad structure"
    return ans, ""


def answer_tokens(ans: dict) -> set:
    return {m.get("marking") for m in ans.get("lane_markings") or [] if isinstance(m, dict) and m.get("marking")}


def _pattern(attrs: dict) -> str:
    p = attrs.get("pattern") or ""
    if p == "solid_dashed":
        return f"solid_dashed/{attrs.get('near_line') or '?'}"
    return p


def label_side(label: dict, side: str) -> dict:
    return {f: label.get(f"{side}_{f}", "") for f in ("color", "pattern", "near_line", "curb", "role", "evidence")}


def _int(v):
    try:
        return int(str(v))
    except (TypeError, ValueError):
        return None


def consistency_issues(ans: dict, schema: dict) -> list[str]:
    """Contradictions inside one answer, found without the label (a hallucination indicator).

    Structural checks that hold in every region: the position of my lane against the lane count and the boundary
    roles, a crossing allowed over a curb or a double solid line, an undecided action with full evidence on what
    governs it, movements that disagree with the arrows the answer itself reported, ONLY with a two-movement arrow,
    and a waiting area entered without one."""
    out = []
    acts = ans.get("actions") or {}
    n, k = _int(ans.get("lane_count")), _int(ans.get("ego_lane_index"))
    if n is not None and k is not None and not 1 <= k <= n:
        out.append(f"my lane position {k} outside 1..{n}")
    lb, rb = ans.get("left_boundary") or {}, ans.get("right_boundary") or {}
    if k == 1 and lb.get("role") == "lane_line":
        out.append("leftmost lane, but a lane line on the left")
    if n is not None and k == n and rb.get("role") == "lane_line":
        out.append("rightmost lane, but a lane line on the right")
    for side, b in (("left", lb), ("right", rb)):
        act = acts.get(f"change_{side}")
        curb = b.get("curb") == "yes"
        if curb and act == "allowed":
            out.append(f"change_{side} allowed across a curb")
        if b.get("pattern") == "double_solid" and act == "allowed":
            out.append(f"change_{side} allowed across a double solid line")
        if b.get("evidence") == "full" and act == "not_determined":
            out.append(f"change_{side} not_determined with full evidence")
        if b.get("pattern") == "none" and not curb and act in ("allowed", "prohibited") and b.get("evidence") == "full":
            out.append(f"change_{side} decided with nothing marked on that side")
        if b.get("evidence") == "insufficient" and act in ("allowed", "prohibited"):
            out.append(f"change_{side} decided although that side cannot be seen")
        # both standards: a broken line may be crossed, the solid line of a solid-and-broken pair may not
        if b.get("pattern") == "solid_dashed" and b.get("near_line") == "solid" and act == "allowed":
            out.append(f"change_{side} allowed with the solid line of a solid-and-broken pair nearer my lane")
        if b.get("pattern") == "solid_dashed" and b.get("near_line") == "dashed" and not curb and act == "prohibited" and b.get("evidence") == "full":
            out.append(f"change_{side} prohibited with the broken line of a solid-and-broken pair nearer my lane")
        if b.get("pattern") == "dashed" and b.get("role") == "lane_line" and not curb and act == "prohibited" and b.get("evidence") == "full":
            out.append(f"change_{side} prohibited across a broken lane line")
    toks = answer_tokens(ans)
    arrows = [t for t in toks if t in schema.get("movement_arrows", {})]
    no_turn = {schema["no_turn"][t] for t in toks if t in schema.get("no_turn", {})}
    full = all((m.get("evidence") == "full") for m in ans.get("lane_markings") or [] if m.get("marking") in arrows)
    if arrows and full:
        shown = {m for t in arrows for m in schema["movement_arrows"][t]}
        for m in MOVES:
            v = acts.get(m)
            if m in shown and m not in no_turn and v in ("prohibited", "not_applicable"):
                out.append(f"{m} {v} although an arrow shows it")
            if m not in shown and m != "u_turn" and v in ("allowed", "stop_first"):
                out.append(f"{m} {v} although no arrow shows it")
    readable = [m for m in ans.get("lane_markings") or [] if m.get("marking") in arrows and m.get("evidence") != "insufficient"]
    if arrows and not readable:
        decided = [m for m in MOVES if acts.get(m) in ("allowed", "prohibited")]
        if decided:
            out.append(f"{', '.join(decided)} decided from an arrow that cannot be read")
    if not arrows and not no_turn and "arrow:two_way_left" not in toks:
        # going straight without an arrow is allowed (lane_v3 convention); the turns and the U-turn stay undecided
        decided = [m for m in MOVES if acts.get(m) in ("allowed", "stop_first", "prohibited") and not (m == "go_straight" and acts.get(m) != "prohibited")]
        if decided:
            out.append(f"{', '.join(decided)} decided without an arrow or prohibited-movement marking")
    if set(schema.get("stop_tokens", [])) & toks:
        going = [m for m in MOVES if acts.get(m) == "allowed"]
        if going:
            out.append(f"{', '.join(going)} allowed without the stop that the STOP or 停 marking in my lane requires")
    for m in no_turn:
        if acts.get(m) == "allowed":
            out.append(f"{m} allowed although a prohibited-movement marking forbids it")
    if "text:only" in toks and any(len(schema["movement_arrows"][t]) > 1 for t in arrows):
        out.append("ONLY with an arrow that shows two movements")
    if acts.get("enter_waiting_area") == "allowed" and not ({"area:left_turn_waiting", "area:two_way_left_turn_lane"} & toks):
        out.append("enter_waiting_area allowed without a waiting area or two-way left-turn lane")
    return out


def score_lane(ans: dict, label: dict, test: str, rule_ids: set, contested: set, schema: dict) -> dict:
    sc: dict = {"scene": {}, "sides": {}, "role": {}}
    lc, ei = _int(label.get("lane_count")), _int(label.get("ego_index"))
    if lc is not None:
        sc["scene"]["lane_count"] = _int(ans.get("lane_count")) == lc
    if ei is not None:
        sc["scene"]["ego_index"] = _int(ans.get("ego_lane_index")) == ei
    sides_ok = []
    for side in SIDES:
        want, got = label_side(label, side), ans.get(f"{side}_boundary") or {}
        if want["evidence"] == "insufficient" or not want["color"]:
            sc["sides"][side] = None
            continue
        per = {"color": got.get("color") == want["color"], "pattern": _pattern(got) == _pattern(want),
               "curb": got.get("curb") == want["curb"]}
        per["all"] = all(per.values())
        sc["sides"][side] = per
        sc["role"][side] = got.get("role") == want["role"]
        sides_ok.append(per["all"])
    # markings_optional: tokens the blind review could not decide; they count neither way
    opt = tokens_of(label.get("markings_optional", ""))
    lt, at_all = tokens_of(label.get("markings", "")) - opt, answer_tokens(ans)
    at = at_all - opt
    if label.get("markings_evidence") == "insufficient":
        sc["markings"] = None
    else:
        ev = {m.get("marking"): m.get("evidence") for m in ans.get("lane_markings") or [] if isinstance(m, dict)}
        core = lambda ts: {t for t in ts if not transverse(t)}  # noqa: E731
        sc["markings"] = {"exact": lt == at, "core_exact": core(lt) == core(at), "added": sorted(at - lt), "missed": sorted(lt - at),
                          "added_evidence": {t: ev.get(t) for t in sorted(at - lt)}, "label": sorted(lt), "answer": sorted(at_all)}
    parts = sides_ok + ([sc["markings"]["exact"]] if sc["markings"] else [])
    sc["lane"] = all(parts) if parts else None
    core_parts = sides_ok + ([sc["markings"]["core_exact"]] if sc["markings"] else [])
    sc["lane_core"] = all(core_parts) if core_parts else None
    got = ans.get("actions") or {}
    per_act = {}
    for a in ACTIONS:
        want = label.get("act_" + a, "")
        if want in ("", "not_applicable"):
            continue
        per_act[a] = got.get(a) == want
    main = {a: ok for a, ok in per_act.items() if a not in contested}
    sc["actions"] = main
    sc["contested"] = {a: ok for a, ok in per_act.items() if a in contested}
    sc["output2"] = all(main.values()) if main else None
    # unsafe: going although the label prohibits it, or going without the stop the label requires (stop_first)
    unsafe = [a for a in ACTIONS if (label.get("act_" + a) == "prohibited" and got.get(a) in ("allowed", "stop_first"))
              or (label.get("act_" + a) == "stop_first" and got.get(a) == "allowed")]
    cautious = [a for a in ACTIONS if (label.get("act_" + a) == "allowed" and got.get(a) in ("prohibited", "not_determined", "stop_first"))
                or (label.get("act_" + a) == "stop_first" and got.get(a) in ("prohibited", "not_determined"))]
    sc["unsafe"] = [a for a in unsafe if a not in contested]
    sc["over_cautious"] = [a for a in cautious if a not in contested]
    sc["contested_unsafe"] = [a for a in unsafe if a in contested]
    sc["prohibited"] = {a: got.get(a) == "prohibited" for a in ACTIONS if label.get("act_" + a) == "prohibited" and a not in contested}
    sc["extra_decisions"] = [a for a in ACTIONS if label.get("act_" + a) == "not_applicable" and got.get(a) in ("allowed", "stop_first", "prohibited")]
    cite = None
    if test in CITING_TESTS:
        raw = [str(e.get("rule_id")) for e in ans.get("element_rules") or [] if isinstance(e, dict) and e.get("rule_id")]
        cited = {norm_rule_id(i) for i in raw} - {""}
        sc["cite_format_fixed"] = sum(1 for i in raw if norm_rule_id(i) != i)
        accepted = {norm_rule_id(i) for i in (label.get("accepted_rule_ids") or "").split(";") if i}
        if cited - rule_ids:
            cite = "unlisted"
        elif not cited:
            cite = "none" if accepted else "none_needed"
        elif cited & accepted:
            cite = "accepted"
        else:
            cite = "in_pack_not_accepted"
        sc["cited"] = sorted(cited)
    sc["citation"] = cite
    sc["consistency"] = consistency_issues(ans, schema)
    sc["evidence"] = {side: [label_side(label, side)["evidence"], (ans.get(f"{side}_boundary") or {}).get("evidence")] for side in SIDES}
    return sc


def score_failed(label: dict, test: str, contested: set, reason: str = "") -> dict:
    """The score of an image without a readable answer: wrong in every measure the label defines, no tokens and
    no unsafe error counted (there is no answer to count them in), excluded from the unsafe comparison."""
    sc: dict = {"failed": reason or "no readable answer", "scene": {}, "sides": {}, "role": {}}
    if _int(label.get("lane_count")) is not None:
        sc["scene"]["lane_count"] = False
    if _int(label.get("ego_index")) is not None:
        sc["scene"]["ego_index"] = False
    parts = []
    for side in SIDES:
        want = label_side(label, side)
        if want["evidence"] == "insufficient" or not want["color"]:
            sc["sides"][side] = None
            continue
        sc["sides"][side] = {"color": False, "pattern": False, "curb": False, "all": False}
        sc["role"][side] = False
        parts.append(False)
    lt = tokens_of(label.get("markings", "")) - tokens_of(label.get("markings_optional", ""))
    if label.get("markings_evidence") == "insufficient":
        sc["markings"] = None
    else:
        sc["markings"] = {"exact": False, "core_exact": False, "added": [], "missed": [], "added_evidence": {}, "label": sorted(lt), "answer": []}
        parts.append(False)
    sc["lane"] = False if parts else None
    sc["lane_core"] = sc["lane"]
    decided = [a for a in ACTIONS if label.get("act_" + a, "") not in ("", "not_applicable")]
    sc["actions"] = {a: False for a in decided if a not in contested}
    sc["contested"] = {a: False for a in decided if a in contested}
    sc["output2"] = False if sc["actions"] else None
    sc.update({"unsafe": [], "over_cautious": [], "contested_unsafe": [], "extra_decisions": [], "consistency": [],
               "prohibited": {a: False for a in ACTIONS if label.get("act_" + a) == "prohibited" and a not in contested},
               "citation": "no_answer" if test in CITING_TESTS else None,
               "evidence": {side: [label_side(label, side)["evidence"], None] for side in SIDES}})
    return sc


def paired_difference(n10: int, n01: int, n11: int, n00: int, z: float = 1.959964) -> dict:
    """Difference of two paired proportions (second minus first) with Newcombe's 95% score interval (method 10,
    Statistics in Medicine 1998). n10: only the first right, n01: only the second right, n11: both, n00: neither."""
    n = n10 + n01 + n11 + n00
    if not n:
        return {"diff": None, "ci95": [None, None]}
    p1, p2 = (n11 + n10) / n, (n11 + n01) / n

    def wilson(k):
        p = k / n
        c = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
        return ((p + z * z / (2 * n) - c) / (1 + z * z / n), (p + z * z / (2 * n) + c) / (1 + z * z / n))

    l1, u1 = wilson(n11 + n10)
    l2, u2 = wilson(n11 + n01)
    den = (n11 + n10) * (n01 + n00) * (n11 + n01) * (n10 + n00)
    cross = n11 * n00 - n10 * n01
    cross = cross - n / 2 if cross > n / 2 else 0 if cross >= 0 else cross  # Newcombe's correction of the correlation
    phi = cross / math.sqrt(den) if den else 0.0
    d = p1 - p2  # Newcombe's direction; reported as p2 - p1
    lo = d - math.sqrt(max(0.0, (p1 - l1) ** 2 - 2 * phi * (p1 - l1) * (u2 - p2) + (u2 - p2) ** 2))
    hi = d + math.sqrt(max(0.0, (u1 - p1) ** 2 - 2 * phi * (u1 - p1) * (p2 - l2) + (p2 - l2) ** 2))
    return {"diff": round(-d, 4), "ci95": [round(-hi, 4), round(-lo, 4)]}


def _acc(vals: list) -> dict:
    vals = [v for v in vals if v is not None]
    return {"correct": sum(1 for v in vals if v), "n": len(vals), "acc": round(sum(1 for v in vals if v) / len(vals), 3) if vals else None}


def summarize_lane(scored: list[dict]) -> dict:
    """scored: [{'image_id', 'score'}] (one answer per image)."""
    n = len(scored)
    if not n:
        return {"n": 0}
    S = [x["score"] for x in scored]
    out = {"n": n,
           "lane": _acc([s["lane"] for s in S]),
           "output2": _acc([s["output2"] for s in S]),
           "lane_count": _acc([s["scene"].get("lane_count") for s in S]),
           "ego_index": _acc([s["scene"].get("ego_index") for s in S]),
           "markings_exact": _acc([s["markings"]["exact"] if s["markings"] else None for s in S]),
           "lane_core": _acc([s.get("lane_core", s["lane"]) for s in S]),
           "markings_core_exact": _acc([s["markings"].get("core_exact", s["markings"]["exact"]) if s["markings"] else None for s in S]),
           "failed": sum(1 for s in S if s.get("failed"))}
    for side in SIDES:
        out[f"{side}_boundary"] = _acc([(s["sides"].get(side) or {}).get("all") if s["sides"].get(side) else None for s in S])
        for f in PHYSICAL:
            out[f"{side}_{f}"] = _acc([(s["sides"].get(side) or {}).get(f) if s["sides"].get(side) else None for s in S])
        out[f"{side}_role"] = _acc([s["role"].get(side) for s in S])
    both = [(s["sides"]["left"] or {}).get("all", True) and (s["sides"]["right"] or {}).get("all", True)
            if (s["sides"]["left"] or s["sides"]["right"]) else None for s in S]
    out["both_boundaries"] = _acc(both)
    added = Counter(t for s in S if s["markings"] for t in s["markings"]["added"])
    missed = Counter(t for s in S if s["markings"] for t in s["markings"]["missed"])
    lab_n = sum(len(s["markings"]["label"]) for s in S if s["markings"])
    ans_n = sum(len(s["markings"]["answer"]) for s in S if s["markings"])
    out["markings_added"] = sum(added.values())
    out["markings_missed"] = sum(missed.values())
    out["markings_precision"] = round(1 - sum(added.values()) / ans_n, 3) if ans_n else None
    out["markings_recall"] = round(1 - sum(missed.values()) / lab_n, 3) if lab_n else None
    out["added_by_token"] = dict(added.most_common())
    out["added_transverse"] = sum(v for t, v in added.items() if transverse(t))
    out["added_by_evidence"] = dict(Counter(str(e) for s in S if s["markings"] for e in (s["markings"].get("added_evidence") or {}).values()))
    out["missed_by_token"] = dict(missed.most_common())
    per = {}
    for a in ACTIONS:
        vals = [s["actions"][a] for s in S if a in s["actions"]]
        if vals:
            per[a] = {"n": len(vals), "correct": sum(vals)}
    out["actions"] = per
    cont = [ok for s in S for ok in s["contested"].values()]
    out["contested"] = {"n": len(cont), "correct": sum(cont)}
    out["unsafe_errors"] = sum(len(s["unsafe"]) for s in S)
    out["unsafe_by_action"] = dict(Counter(a for s in S for a in s["unsafe"]))
    out["over_cautious_errors"] = sum(len(s["over_cautious"]) for s in S)
    out["contested_unsafe_errors"] = sum(len(s["contested_unsafe"]) for s in S)
    pro = [ok for s in S for ok in s["prohibited"].values()]
    out["prohibited_recall"] = _acc(pro)
    out["extra_decisions"] = sum(len(s["extra_decisions"]) for s in S)
    out["citations"] = dict(Counter(s["citation"] for s in S if s["citation"] is not None))
    out["citation_ids_with_brackets"] = sum(s.get("cite_format_fixed", 0) for s in S)
    out["inconsistent_answers"] = sum(1 for s in S if s["consistency"])
    out["consistency_kinds"] = dict(Counter(i.split(" although")[0].split(" with ")[0] for s in S for i in s["consistency"]).most_common(8))
    ev = Counter()
    for s in S:
        for side in SIDES:
            want, got = s["evidence"][side]
            if want == "full" and got in ("partial", "insufficient"):
                ev["over_withholding"] += 1
            elif want in ("partial", "insufficient") and got == "full":
                ev["unsupported_guess"] += 1
            elif want and want == got:
                ev["same"] += 1
            elif want:
                ev["other"] += 1
    out["boundary_evidence"] = dict(ev)
    return out


COMPARE_KEYS = {"lane": lambda s: s["lane"], "output2": lambda s: s["output2"],
                "both_boundaries": lambda s: (None if not (s["sides"]["left"] or s["sides"]["right"]) else
                                              (s["sides"]["left"] or {}).get("all", True) and (s["sides"]["right"] or {}).get("all", True)),
                "markings": lambda s: s["markings"]["exact"] if s["markings"] else None,
                "lane_core": lambda s: s.get("lane_core", s["lane"]),
                "no_unsafe": lambda s: None if s.get("failed") else not s["unsafe"]}


def compare_lane(a_scored: dict, b_scored: dict) -> dict:
    """Paired comparison (first run "A", second run "B", whatever their tests): exact McNemar per measure and the
    difference in accuracy (second minus first) with a 95% interval. Every image of a finished run has a score (a failed
    answer as well, see score_failed); images that are in only one of the runs are not paired and are counted."""
    ids = sorted(set(a_scored) & set(b_scored))
    out = {"n": len(ids), "only_in_one_run": len(set(a_scored) ^ set(b_scored))}
    for key, f in COMPARE_KEYS.items():
        pairs = [(f(a_scored[i]["score"]), f(b_scored[i]["score"])) for i in ids]
        pairs = [(x, y) for x, y in pairs if x is not None and y is not None]
        b = sum(1 for x, y in pairs if not x and y)
        c = sum(1 for x, y in pairs if x and not y)
        both = sum(1 for x, y in pairs if x and y)
        out[key] = {"n": len(pairs), "acc_A": round(sum(bool(x) for x, _ in pairs) / len(pairs), 3) if pairs else None,
                    "acc_B": round(sum(bool(y) for _, y in pairs) / len(pairs), 3) if pairs else None,
                    "only_B_right": b, "only_A_right": c, "p_value": mcnemar_exact(b, c),
                    **paired_difference(c, b, both, len(pairs) - b - c - both)}
    ua = sum(len(a_scored[i]["score"]["unsafe"]) for i in ids)
    ub = sum(len(b_scored[i]["score"]["unsafe"]) for i in ids)
    out["unsafe_errors"] = {"A": ua, "B": ub}
    return out


def compare_lane_repeated(a_runs: dict, b_runs: dict, resamples: int = 4000, seed: int = 6216) -> dict:
    """Paired comparison when an image was answered more than once per test (repeated runs).

    a_runs, b_runs: {image key: [score, ...]} over all runs of each test. Per image and measure, the share of correct
    answers of each test; the difference (second minus first) is averaged over images, with a 95% interval from a
    paired bootstrap over images; the exact sign test counts the images where one test was right more often."""
    import random
    ids = sorted(k for k in set(a_runs) & set(b_runs) if a_runs[k] and b_runs[k])
    out = {"n": len(ids), "answers": [sum(len(a_runs[k]) for k in ids), sum(len(b_runs[k]) for k in ids)], "repeated": True}
    rng = random.Random(seed)
    for key, f in COMPARE_KEYS.items():
        rows = []
        for k in ids:
            xa = [f(s) for s in a_runs[k] if f(s) is not None]
            xb = [f(s) for s in b_runs[k] if f(s) is not None]
            if xa and xb:
                rows.append((sum(map(bool, xa)) / len(xa), sum(map(bool, xb)) / len(xb)))
        if not rows:
            out[key] = {"n": 0, "acc_A": None, "acc_B": None, "only_A_right": 0, "only_B_right": 0, "p_value": None, "diff": None, "ci95": [None, None]}
            continue
        d = [b - a for a, b in rows]
        boots = sorted(sum(d[rng.randrange(len(d))] for _ in d) / len(d) for _ in range(resamples))
        better_b, better_a = sum(1 for x in d if x > 0), sum(1 for x in d if x < 0)
        out[key] = {"n": len(rows), "acc_A": round(sum(a for a, _ in rows) / len(rows), 3), "acc_B": round(sum(b for _, b in rows) / len(rows), 3),
                    "only_B_right": better_b, "only_A_right": better_a, "p_value": mcnemar_exact(better_b, better_a),
                    "diff": round(sum(d) / len(d), 4), "ci95": [round(boots[int(0.025 * resamples)], 4), round(boots[int(0.975 * resamples) - 1], 4)]}
    ua = sum(len(s["unsafe"]) for k in ids for s in a_runs[k]) / max(1, max(len(a_runs[k]) for k in ids)) if ids else 0
    ub = sum(len(s["unsafe"]) for k in ids for s in b_runs[k]) / max(1, max(len(b_runs[k]) for k in ids)) if ids else 0
    out["unsafe_errors"] = {"A": round(ua, 1), "B": round(ub, 1)}
    return out


def per_element_rows(scored: list[dict]) -> list[dict]:
    """One row per image for tables: which parts were right."""
    rows = []
    for x in scored:
        s = x["score"]
        rows.append({"image_id": x["image_id"], "lane": s["lane"], "left": (s["sides"]["left"] or {}).get("all"),
                     "right": (s["sides"]["right"] or {}).get("all"), "markings": s["markings"]["exact"] if s["markings"] else None,
                     "actions": s["output2"], "unsafe": ";".join(s["unsafe"]), "added": ";".join((s["markings"] or {}).get("added", [])),
                     "missed": ";".join((s["markings"] or {}).get("missed", [])), "inconsistent": "; ".join(s["consistency"])})
    return rows


__all__ = ["parse_lane", "score_lane", "score_failed", "summarize_lane", "compare_lane", "compare_lane_repeated", "paired_difference", "consistency_issues",
           "per_element_rows", "norm_rule_id", "transverse", "ACTIONS"]
