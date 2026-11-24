"""Verification layer of the lane advisor: checks an answer without a label (works in production, where there is no
ground truth).

1. Rule check: the region's rule table (regulations/<CODE>/lane_action_rules.json, the same table the labels follow)
   is applied to the lines and markings the model itself reported. Each action the table decides is compared with the
   model's decision. agreement = share of decided actions on which the two agree. In the experiments the reasoning
   step agreed with the table 87-100 % of the time for GPT, so a low agreement means the answer contradicts itself.
2. Unsafe-direction disagreement: the model allows an action that the table prohibits for the lines it saw.
3. Evidence: the model says a boundary or the markings were only partly visible.
4. Input quality: brightness and size of the photo (data drift, e.g. more night photos than in the test set).

needs_review is True when any of these fires; the page shows it and Prometheus counts it (alert rule in Grafana).
Added by Claude, 2026-11-18.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

AGREEMENT_THRESHOLD = 0.85          # the alert threshold of deploy/grafana/provisioning/alerting/rules.yml
ALLOWS = ("allowed", "stop_first")


@lru_cache(maxsize=4)
def _tables(repo: str):
    from ..labeling import lanes as LL
    return LL.load_lane_rules(Path(repo)), LL.load_lane_schema(Path(repo))


def _row_from_answer(answer: dict) -> dict:
    from ..labeling import lanes as LL
    row = {}
    for side in LL.SIDES:
        b = answer.get(f"{side}_boundary") or {}
        for f in LL.BOUNDARY_FIELDS:
            row[f"{side}_{f}"] = str(b.get(f) or "")
    ms = [m for m in answer.get("lane_markings") or [] if isinstance(m, dict) and m.get("marking")]
    row["markings"] = ";".join(str(m["marking"]) for m in ms)
    order = {"full": 0, "partial": 1, "insufficient": 2}
    row["markings_evidence"] = max((str(m.get("evidence") or "full") for m in ms), key=lambda e: order.get(e, 0), default="full")
    return row


def rule_check(repo: str | Path, region: str, answer: dict | None) -> dict:
    """Compare the model's actions with the rule table applied to the model's own lines and markings."""
    if not answer or not isinstance(answer.get("actions"), dict):
        return {"checked": 0, "agree": 0, "agreement": None, "disagreements": [], "unsafe_direction": []}
    from ..labeling import lanes as LL
    table, schema = _tables(str(repo))
    derived = LL.lane_prefill(table, schema, region, _row_from_answer(answer))["actions"]
    got = answer["actions"]
    dis, unsafe, n = [], [], 0
    for act, rule_value in derived.items():
        if not rule_value:                      # the table does not decide this action for these lines
            continue
        n += 1
        model_value = str(got.get(act) or "")
        if model_value != rule_value:
            dis.append({"action": act, "model": model_value, "rules": rule_value})
            if model_value in ALLOWS and rule_value == "prohibited":
                unsafe.append(act)
    agree = n - len(dis)
    return {"checked": n, "agree": agree, "agreement": round(agree / n, 3) if n else None,
            "disagreements": dis, "unsafe_direction": unsafe}


def evidence_flags(answer: dict | None) -> list[str]:
    flags = []
    if not answer:
        return ["no_answer"]
    for side in ("left", "right"):
        ev = str((answer.get(f"{side}_boundary") or {}).get("evidence") or "")
        if ev and ev != "full":
            flags.append(f"{side}_line_{ev}")
    if str(answer.get("scene_evidence") or "") not in ("", "full"):
        flags.append(f"scene_{answer.get('scene_evidence')}")
    return flags


def image_stats(path: str | Path) -> dict:
    """Mean brightness (0-255) and size of the photo; used for the drift panels."""
    try:
        import cv2
        img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
        if img is None:
            return {}
        h, w = img.shape[:2]
        return {"brightness": round(float(img.mean()), 1), "width": int(w), "height": int(h)}
    except Exception:  # noqa: BLE001 - drift statistics are optional
        return {}


def verify(repo: str | Path, region: str, rec: dict, image_path: str | Path | None = None) -> dict:
    """Everything the page and the monitoring need about one answer."""
    ans = rec.get("answer")
    rc = rule_check(repo, region, ans)
    flags = evidence_flags(ans)
    if rec.get("error") or rec.get("parse_error"):
        flags.append("model_error")
    reasons = []
    if rc["agreement"] is not None and rc["agreement"] < AGREEMENT_THRESHOLD:
        reasons.append(f"rule agreement {rc['agreement']:.2f} < {AGREEMENT_THRESHOLD}")
    if rc["unsafe_direction"]:
        reasons.append("allows what the rules prohibit for the lines it saw: " + ", ".join(rc["unsafe_direction"]))
    reasons += [f for f in flags if f != "no_answer"]
    if not ans:
        reasons.append("no answer")
    out = {"rule_check": rc, "flags": flags, "needs_review": bool(reasons), "reasons": reasons}
    if image_path:
        out["image"] = image_stats(image_path)
    return out
