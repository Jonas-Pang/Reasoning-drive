"""Prediction log and user feedback of the lane advisor (page /app).

results/app/predictions.jsonl  one line per answer given on /app: request id, time, region, test, model, prompt,
                               actions, lines, verification result, latency. No photo is stored (uploads are deleted
                               when the page stops); this is the audit log of what the system told whom it told.
results/app/feedback.csv       one line per feedback: the request it is about, an overall rating, a verdict per action
                               (right / wrong / unsure), a verdict per line, and a comment. source = "user" for the
                               page, "simulated_reviewer" for scripts/replay_feedback.py (labels replayed as feedback).

summary() feeds the Monitor tab; scripts/feedback_report.py analyses the same files (frequency + themes).
Added by Claude, 2026-11-18.
"""
from __future__ import annotations

import csv
import json
import os
import re
import threading
import time
import uuid
from collections import Counter, defaultdict
from pathlib import Path

ACTIONS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"]
VERDICTS = ("right", "wrong", "unsure")
FIELDS = ["time_utc", "request_id", "source", "region", "test", "model", "image_id", "rating", "left_line", "right_line",
          *[f"act_{a}" for a in ACTIONS], "comment", "themes"]

# Theme coding of the comments (qualitative analysis, first pass by keywords; English and Chinese).
THEMES = {
    "solid_vs_dashed": r"solid|dash|broken|虚|实",
    "line_color": r"yellow|white|colou?r|黄|白",
    "arrow_or_turn": r"arrow|turn|u-?turn|箭头|转|掉头",
    "bus_or_special_lane": r"bus|special|hov|carpool|公交|专用",
    "wrong_lane_position": r"wrong lane|lane count|which lane|position|车道数|哪条",
    "visibility_night_weather": r"night|dark|rain|glare|occlu|hidden|blur|夜|雨|挡|看不清",
    "too_cautious": r"cautious|too strict|should be allowed|保守|应该允许",
    "unsafe": r"unsafe|danger|should be prohibited|not allowed|危险|应该禁止",
    "slow": r"slow|latency|took long|慢",
}


def themes_of(text: str) -> list[str]:
    t = (text or "").lower()
    return [k for k, rx in THEMES.items() if re.search(rx, t)]


class AppLog:
    def __init__(self, repo: str | Path):
        self.dir = Path(os.environ.get("RD_APP_DIR") or Path(repo) / "results" / "app")   # RD_APP_DIR: another folder
        self.pred = self.dir / "predictions.jsonl"
        self.fb = self.dir / "feedback.csv"
        self.lock = threading.Lock()
        # in-memory mirror of both files (read once at start, then appended to): the page never re-reads the disk
        self._preds = self._read_preds()
        self._fb = self._read_fb()

    def _read_preds(self) -> list[dict]:
        out = []
        try:
            for ln in self.pred.read_text(encoding="utf-8").splitlines():
                try:
                    out.append(json.loads(ln))
                except json.JSONDecodeError:
                    continue
        except OSError:
            pass
        return out

    def _read_fb(self) -> list[dict]:
        try:
            with self.fb.open(encoding="utf-8", newline="") as f:
                return list(csv.DictReader(f))
        except OSError:
            return []

    # ------------------------------------------------------------------ predictions
    def log_prediction(self, rec: dict, check: dict, cfg: dict, mode: str) -> str:
        rid = uuid.uuid4().hex[:12]
        ans = rec.get("answer") or {}
        line = {
            "request_id": rid, "time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "mode": mode,
            "image_id": rec.get("image_id"), "upload": str(rec.get("image_id", "")).startswith("upload_"),
            "region": rec.get("region"), "test": rec.get("test"),
            "model": (rec.get("response") or {}).get("model") or cfg["api"].get("model"),
            "prompt": (rec.get("from_run") or {}).get("prompt") or cfg.get("lane", {}).get("prompt_dir"),
            "latency_s": (rec.get("response") or {}).get("latency_s"),
            "actions": ans.get("actions"),
            "left": {k: (ans.get("left_boundary") or {}).get(k) for k in ("color", "pattern", "role", "evidence")},
            "right": {k: (ans.get("right_boundary") or {}).get(k) for k in ("color", "pattern", "role", "evidence")},
            "rule_agreement": check["rule_check"]["agreement"], "needs_review": check["needs_review"],
            "reasons": check["reasons"], "image": check.get("image", {}),
            "error": (rec.get("error") or rec.get("parse_error") or "")[:200],
        }
        with self.lock:
            self.dir.mkdir(parents=True, exist_ok=True)
            with self.pred.open("a", encoding="utf-8") as f:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")
            self._preds.append(line)
        return rid

    def predictions(self) -> list[dict]:
        with self.lock:
            return list(self._preds)

    def prediction(self, request_id: str) -> dict | None:
        return next((p for p in self.predictions() if p["request_id"] == request_id), None)

    # ------------------------------------------------------------------ feedback
    def add_feedback(self, body: dict, source: str = "user") -> dict:
        rid = str(body.get("request_id") or "")
        pred = self.prediction(rid) if rid else None
        rating = str(body.get("rating") or "")
        if rating not in ("good", "bad", ""):
            raise ValueError("rating must be good or bad")
        acts = body.get("actions") or {}
        lines = body.get("lines") or {}
        for v in list(acts.values()) + list(lines.values()):
            if v and v not in VERDICTS:
                raise ValueError(f"verdict must be one of {VERDICTS}")
        comment = re.sub(r"\s+", " ", str(body.get("comment") or ""))[:500]
        row = {
            "time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "request_id": rid, "source": source,
            "region": (pred or {}).get("region") or body.get("region", ""), "test": (pred or {}).get("test") or body.get("test", ""),
            "model": (pred or {}).get("model") or body.get("model", ""), "image_id": (pred or {}).get("image_id") or body.get("image_id", ""),
            "rating": rating, "left_line": lines.get("left", ""), "right_line": lines.get("right", ""),
            **{f"act_{a}": acts.get(a, "") for a in ACTIONS}, "comment": comment, "themes": ";".join(themes_of(comment)),
        }
        with self.lock:
            self.dir.mkdir(parents=True, exist_ok=True)
            new = (not self.fb.exists() or self.fb.stat().st_size == 0) and not self._fb
            with self.fb.open("a", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=FIELDS)
                if new:
                    w.writeheader()
                w.writerow(row)
            self._fb.append(row)
        return row

    def feedback(self) -> list[dict]:
        with self.lock:
            return list(self._fb)

    # ------------------------------------------------------------------ monitor tab
    def summary(self) -> dict:
        preds, fb = self.predictions(), self.feedback()
        agr = [p["rule_agreement"] for p in preds if p.get("rule_agreement") is not None]
        lat = sorted(p["latency_s"] for p in preds if p.get("latency_s"))
        per_action = {a: Counter(r.get(f"act_{a}") for r in fb if r.get(f"act_{a}")) for a in ACTIONS}
        per_line = {s: Counter(r.get(f"{s}_line") for r in fb if r.get(f"{s}_line")) for s in ("left", "right")}
        by_region = defaultdict(lambda: Counter())
        for r in fb:
            by_region[r.get("region") or "?"][r.get("rating") or "none"] += 1
        themes = Counter(t for r in fb for t in (r.get("themes") or "").split(";") if t)
        return {
            "predictions": len(preds),
            "needs_review": sum(1 for p in preds if p.get("needs_review")),
            "rule_agreement_mean": round(sum(agr) / len(agr), 3) if agr else None,
            "latency_p50": lat[len(lat) // 2] if lat else None,
            "latency_p90": lat[int(len(lat) * 0.9)] if lat else None,
            "feedback": len(fb),
            "feedback_by_source": dict(Counter(r.get("source") for r in fb)),
            "ratings": dict(Counter(r.get("rating") or "none" for r in fb)),
            "per_action": {a: dict(c) for a, c in per_action.items()},
            "action_wrong_rate": {a: round(c["wrong"] / (c["right"] + c["wrong"]), 3) if (c["right"] + c["wrong"]) else None
                                  for a, c in per_action.items()},
            "per_line": {s: dict(c) for s, c in per_line.items()},
            "by_region": {k: dict(v) for k, v in by_region.items()},
            "themes": themes.most_common(),
            "recent_comments": [{"time_utc": r["time_utc"], "region": r["region"], "rating": r["rating"], "comment": r["comment"]}
                                for r in fb[::-1] if r.get("comment")][:8],
        }
