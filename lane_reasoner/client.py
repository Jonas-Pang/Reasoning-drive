"""Reasoning (DiLu): one request to the model through the OpenAI Responses API, or a mock answer.

Uses only the Python standard library (no SDK version to pin). The request is
  POST {base_url}/responses
  {"model", "input": [instructions message, user message with text + image], "text": {"format": json_schema},
   "reasoning": {"effort", "summary"}, "temperature", "max_output_tokens", "store"}
and the answer is the output_text of the message in "output". When model.reasoning_summary is set, the
"reasoning" items of the output carry the model's own summary of its hidden reasoning; it is kept with the
answer and shown in the trace.
"""
from __future__ import annotations

import base64
import json
import random
import time
import urllib.error
import urllib.request

from .config import api_key


class ApiError(Exception):
    def __init__(self, message: str, status: int | None = None, retry: bool = False):
        super().__init__(message)
        self.status = status
        self.retry = retry


def build_payload(cfg: dict, parts: dict, jpeg: bytes) -> dict:
    a = cfg["api"]
    image_url = "data:image/jpeg;base64," + base64.b64encode(jpeg).decode("ascii")
    payload = {
        "model": a["model"],
        "input": [
            {"role": a.get("instruction_role", "developer"), "content": [{"type": "input_text", "text": parts["instructions"]}]},
            {"role": "user", "content": [
                {"type": "input_text", "text": parts["user_text"]},
                {"type": "input_image", "image_url": image_url, "detail": a.get("image_detail", "high")},
            ]},
        ],
        "text": {"format": {"type": "json_schema", "name": "lane_marking_answer", "schema": parts["schema"], "strict": True}},
        "max_output_tokens": int(a.get("max_output_tokens", 400)),
    }
    _reasoning(payload, a)
    if a.get("temperature") is not None:
        payload["temperature"] = a["temperature"]
    if a.get("store") is not None:
        payload["store"] = bool(a["store"])
    return payload


def _reasoning(payload: dict, a: dict) -> None:
    r = {}
    if a.get("reasoning_effort") not in (None, ""):
        r["effort"] = a["reasoning_effort"]
    if a.get("reasoning_summary"):
        r["summary"] = a["reasoning_summary"]
    if r:
        payload["reasoning"] = r


def settings_of(cfg: dict) -> dict:
    """The request settings saved with every result (the same in both tests)."""
    a = cfg["api"]
    out = {k: a.get(k) for k in ("base_url", "model", "reasoning_effort", "temperature", "image_detail",
                                 "max_output_tokens", "instruction_role", "store")}
    if a.get("reasoning_summary"):
        out["reasoning_summary"] = a["reasoning_summary"]
    return out


def _output_text(data: dict) -> tuple[str, str, str]:
    text, refusal, summary = [], [], []
    for item in data.get("output", []) or []:
        if item.get("type") == "reasoning":
            summary += [s.get("text", "") for s in item.get("summary", []) or [] if s.get("text")]
            continue
        if item.get("type") != "message":
            continue
        for c in item.get("content", []) or []:
            if c.get("type") == "output_text":
                text.append(c.get("text", ""))
            elif c.get("type") == "refusal":
                refusal.append(c.get("refusal", ""))
    if not text and isinstance(data.get("output_text"), str):
        text.append(data["output_text"])
    return "".join(text), " ".join(refusal), "\n\n".join(summary)


def call(cfg: dict, payload: dict) -> dict:
    """Send one request; retry on rate limits, server errors and timeouts. Returns text, model, usage, latency."""
    a = cfg["api"]
    key = api_key(cfg)
    if not key:
        raise ApiError(f"No API key: set {a.get('api_key_env', 'OPENAI_API_KEY')} in the .env file (see the notebook), or use mock mode.")
    url = a["base_url"].rstrip("/") + "/responses"
    body = json.dumps(payload).encode("utf-8")
    tries = int(a.get("max_retries", 4)) + 1
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, data=body, method="POST",
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=float(a.get("timeout_s", 90))) as r:
                data = json.loads(r.read().decode("utf-8"))
            text, refusal, summary = _output_text(data)
            status = data.get("status", "")
            if status and status != "completed":
                reason = (data.get("incomplete_details") or {}).get("reason", "")
                raise ApiError(f"The answer is {status}" + (f" ({reason})" if reason else "") +
                               (". Raise api.max_output_tokens." if reason == "max_output_tokens" else "."))
            if refusal and not text:
                raise ApiError("The model refused: " + refusal)
            return {"text": text, "model": data.get("model", ""), "usage": data.get("usage") or {},
                    "latency_s": round(time.time() - t0, 2), "response_id": data.get("id", ""), "attempts": attempt + 1,
                    "reasoning_summary": summary}
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", "replace")
            try:
                err = json.loads(raw).get("error", {})
                msg = err.get("message") or raw[:300]
                if err.get("param"):
                    msg += f" (parameter: {err['param']})"
            except json.JSONDecodeError:
                msg = raw[:300]
            retry = e.code == 429 or e.code >= 500
            last = ApiError(f"HTTP {e.code}: {msg}", e.code, retry)
            if not retry:
                raise last from None
            wait = float(e.headers.get("retry-after") or 0) or min(30, 2 ** attempt + random.random())
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = ApiError(f"Network problem: {getattr(e, 'reason', e)}", None, True)
            wait = min(30, 2 ** attempt + random.random())
        if attempt < tries - 1:
            time.sleep(wait)
    raise last or ApiError("Request failed.")


def call_with_fallback(cfg: dict, payload: dict) -> dict:
    """call(), but if the API refuses the reasoning summary (some models and organisations cannot get one), the
    request is sent again without it and the answer notes why the summary is missing."""
    try:
        return call(cfg, payload)
    except ApiError as e:
        if e.status != 400 or "summary" not in str(e).lower() or "summary" not in (payload.get("reasoning") or {}):
            raise
        p2 = json.loads(json.dumps(payload))
        p2["reasoning"].pop("summary")
        if not p2["reasoning"]:
            p2.pop("reasoning")
        out = call(cfg, p2)
        out["reasoning_summary_note"] = f"reasoning summary not available: {e}"
        return out


def ping(cfg: dict) -> dict:
    """One tiny text request with the same model and settings as the real runs (no image, no schema).

    Checks the key, the model name and that the model accepts reasoning_effort / temperature. Costs a few tokens."""
    a = cfg["api"]
    payload = {"model": a["model"], "input": [{"role": "user", "content": [{"type": "input_text", "text": "Reply with the single word OK."}]}],
               "max_output_tokens": max(64, int(a.get("max_output_tokens", 400)) // 4)}
    _reasoning(payload, a)
    if a.get("temperature") is not None:
        payload["temperature"] = a["temperature"]
    if a.get("store") is not None:
        payload["store"] = bool(a["store"])
    return call_with_fallback(cfg, payload)


# ------------------------------------------------------------------ mock answers

def mock_answer(cfg: dict, item, test: str, repeat: int = 0) -> dict:
    """A made-up answer for trying the pipeline without the API: the label, with deterministic mistakes.

    Test A makes more mistakes than Test B on purpose, so the report and the comparison have something to show.
    It says nothing about the real model."""
    from video_tool.core import load_action_rules, prefill
    from types import SimpleNamespace
    lab = item.label
    rng = random.Random(f"{item.image_id}:{test}:{repeat}")
    err = 0.25 if test == "A" else 0.10
    mt, at = lab.get("marking_type", "other"), lab.get("arrow_type") or None
    acts = {a: lab.get("act_" + a, "not_applicable") for a in ("cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_center_lane_to_wait")}
    swap = {"white_dashed": "white_solid", "white_solid": "white_dashed", "yellow_solid": "yellow_double_solid",
            "yellow_double_solid": "yellow_solid", "yellow_dashed": "yellow_solid", "two_way_left_turn_lane": "yellow_solid_dashed"}
    if rng.random() < err and mt in swap:
        mt = swap[mt]
        table = load_action_rules(SimpleNamespace(repo=__import__("pathlib").Path(cfg["_repo"])))
        sug = prefill(table, item.region, mt, at or "", "", "full")
        acts.update(sug.get("actions", {}))
    elif rng.random() < err:
        flip = {"allowed": "prohibited", "prohibited": "allowed"}
        decided = [a for a, v in acts.items() if v in flip]
        if decided:
            a = rng.choice(decided)
            acts[a] = flip[acts[a]]
    ids = [i for i in (lab.get("accepted_rule_ids") or "").split(";") if i]
    ans = {
        "description": f"(mock) {mt.replace('_', ' ')} inside the box.",
        "evidence": lab.get("expected_evidence") or "full",
        "marking": {"marking_type": mt, "arrow_type": at if mt == "arrow" else None, "position": lab.get("position") or "left"},
        "actions": acts,
        "cited_rule_id": (ids[0] if ids else None) if test == "B" else None,
        "rule_reasoning": "(mock) the rule of this marking type",
        "action_reasons": {k: "(mock)" for k in acts},
        "self_check": "(mock) consistent",
        "reasoning": "(mock answer: no model was called)",
    }
    usage = {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}  # no request is sent
    return {"text": json.dumps(ans), "model": "mock", "usage": usage, "latency_s": 0.0, "response_id": "", "attempts": 0}
