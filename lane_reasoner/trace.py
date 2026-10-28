"""The reasoning behind one answer, step by step, as plain text.

The steps are the answer fields in the order the model wrote them (prompt v3: look, rule, decide, check, then
the actions), followed by the model's own summary of its hidden reasoning when the API returned one, the score
against the label, and tokens, time and cost. Used by `ask`, `run --trace`, `trace` and runs/<run_id>/trace.md.
"""
from __future__ import annotations

import textwrap

ACTIONS = ["cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_center_lane_to_wait"]
WIDTH = 110
LABEL_W = 22


def _block(label: str, text: str, indent: int = 0, width: int = LABEL_W) -> list[str]:
    head = (" " * indent + label).ljust(width)
    if not head.endswith(" "):
        head += " "
    body = textwrap.wrap(str(text), WIDTH - len(head)) or [""]
    return [(head + body[0]).rstrip()] + [(" " * len(head) + b).rstrip() for b in body[1:]]


def _mark(ok) -> str:
    return "correct" if ok else ("not scored" if ok is None else "wrong")


def trace_text(rec: dict, passage_map: dict | None = None, cost_usd: float | None = None) -> str:
    """rec: one record from runner.ask() or results.jsonl. passage_map: rule_id -> passage (for the cited text)."""
    out = []
    resp = rec.get("response") or {}
    head = f"{rec.get('image_id', '')} | Test {rec.get('test', '')} | {resp.get('model') or 'no answer'}"
    head += f" | repeat {rec.get('repeat', 0) + 1}" + (" | from cache" if rec.get("cached") else "") + (" | MOCK" if rec.get("mock") else "")
    out += [head, "-" * min(WIDTH, len(head))]
    out += _block("Input", "photo with the target marking in a cyan box, the instructions"
                  + (" and the rule passages of the region" if rec.get("test") == "B" else " (no rule passages)")
                  + f"; prompt {((rec.get('request') or {}).get('hashes') or {}).get('prompt_dir', '')}")
    if rec.get("error"):
        out += _block("Error", rec["error"])
        return "\n".join(out)
    a = rec.get("answer")
    if not a:
        out += _block("Unreadable answer", f"{rec.get('parse_error', '')}: {rec.get('text', '')[:300]}")
        return "\n".join(out)
    m = a.get("marking") or {}
    acts = a.get("actions") or {}
    reasons = a.get("action_reasons") or {}
    out += _block("Step 1  Look", a.get("description", ""))
    out += _block("Evidence", a.get("evidence", ""), 4)
    out += _block("Output 1", f"{m.get('marking_type', '')}" + (f" / {m['arrow_type']}" if m.get("arrow_type") else "")
                  + f", position {m.get('position', '')}", 4)
    if "rule_reasoning" in a:
        out += _block("Step 2  Rule", a.get("rule_reasoning", ""))
    else:
        out += _block("Step 2  Rule", "(not written separately in this prompt version)")
    cid = a.get("cited_rule_id")
    if rec.get("test") == "B":
        p = (passage_map or {}).get(cid) if cid else None
        text = f"{cid}" + (f': "{(p.get("text_en") or p.get("text_zh") or "")[:240]}"' if p else "") if cid else "none"
        out += _block("Cited passage", text, 4)
    out += _block("Step 3  Decide", "" if reasons else "(no reason per action in this prompt version)")
    for k in ACTIONS:
        if k not in acts:
            continue
        out += _block(f"{k:<26}{acts[k]}", reasons.get(k, "") if reasons else "", 4, 4 + 26 + 16)
    if "self_check" in a:
        out += _block("Step 4  Check", a.get("self_check", ""))
    if a.get("reasoning"):
        out += _block("Reasoning", a["reasoning"] + ("  (written after the actions)" if "self_check" not in a else ""))
    if resp.get("reasoning_summary"):
        out += _block("Model's summary", resp["reasoning_summary"])
    elif resp.get("reasoning_summary_note"):
        out += _block("Model's summary", resp["reasoning_summary_note"])
    s = rec.get("score")
    if s:
        lab = rec.get("label") or {}
        res = f"Output 1 {_mark(s.get('output1'))} (label {s.get('o1_label', '')}); Output 2 {_mark(s.get('output2'))}"
        wrong = [k for k, ok in (s.get("actions") or {}).items() if ok is False]
        if wrong:
            res += " (" + ", ".join(f"{k}: label {lab.get('act_' + k, '')}" for k in wrong) + ")"
        res += f"; evidence group {s.get('evidence_group', '')}"
        if s.get("unsafe"):
            res += f"; UNSAFE: {', '.join(s['unsafe'])}"
        if s.get("consistency"):
            res += f"; contradicts itself: {'; '.join(s['consistency'])}"
        if rec.get("test") == "B":
            res += f"; citation {s.get('citation', '')}"
        out += _block("Result", res)
    u = resp.get("usage") or {}
    if u:
        rt = (u.get("output_tokens_details") or {}).get("reasoning_tokens")
        cost = f" | ${cost_usd:.5f}" if cost_usd is not None else ""
        out += _block("Tokens", f"{u.get('input_tokens', 0)} input + {u.get('output_tokens', 0)} output"
                      + (f" (hidden reasoning {rt})" if rt is not None else "") + f" | {resp.get('latency_s', '')} s{cost}")
    return "\n".join(out)


def passage_map(cfg: dict, region: str) -> dict:
    from .prompts import passages
    return {p["rule_id"]: p for p in passages(cfg, region)}


def write_trace_file(cfg: dict, run_id: str) -> str:
    """runs/<run_id>/trace.md: the trace of every answer of a saved run."""
    from .runner import load_run, runs_dir
    run = load_run(cfg, run_id)
    maps: dict[str, dict] = {}
    parts = [f"# Reasoning trace of run {run_id}", ""]
    for r in sorted(run["records"], key=lambda r: (r["image_id"], r.get("repeat", 0))):
        if r["region"] not in maps:
            try:
                maps[r["region"]] = passage_map(cfg, r["region"])
            except Exception:  # noqa: BLE001
                maps[r["region"]] = {}
        parts += ["```", trace_text(r, maps[r["region"]]), "```", ""]
    path = runs_dir(cfg) / run_id / "trace.md"
    path.write_text("\n".join(parts), encoding="utf-8")
    return str(path)
