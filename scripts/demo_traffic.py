"""Send real traffic through the running lane advisor, the way users would: analyze photos, then rate the answers.

Every request goes over HTTP to the service (the same endpoints the page uses), so the whole path is exercised:
/api/app/predict -> verification -> audit log -> Prometheus metrics, and /api/feedback -> feedback.csv -> metrics ->
Grafana panels and alert rules. The ratings come from the final labels (a careful reviewer) and are sent with
source = "simulated_reviewer", so they stay apart from real user feedback everywhere.

With the default --mode saved no model is called (the answers of the frozen test run are replayed), so it is free
and works without a key. With --mode live each photo costs one model call.

usage: python scripts/demo_traffic.py [--url http://localhost:8770] [--per-region 40] [--mode saved|live] [--delay 0.2]
Added by Claude, 2026-11-18.
"""
from __future__ import annotations

import argparse
import json
import time
import urllib.request

ACTIONS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"]


def call(url: str, path: str, body: dict | None = None):
    req = urllib.request.Request(url + path, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://localhost:8770")
    ap.add_argument("--per-region", type=int, default=40)
    ap.add_argument("--mode", default="saved", choices=["saved", "live"])
    ap.add_argument("--test", default="B", choices=["A", "B"])
    ap.add_argument("--delay", type=float, default=0.2, help="seconds between requests")
    args = ap.parse_args()
    info = call(args.url, "/api/app/info")
    print(f"service: {info['model']} · {info['prompt']} · mode {args.mode}")
    n = bad = flagged = 0
    for region in info["regions"]:
        examples = call(args.url, f"/api/app/examples?region={region}")[: args.per_region]
        if not examples:
            print(f"{region}: no examples on this machine, skipped")
            continue
        for ex in examples:
            r = call(args.url, "/api/app/predict", {"image_id": ex["image_id"], "test": args.test, "mode": args.mode})
            got, lab = (r.get("answer") or {}).get("actions") or {}, r.get("label_actions") or {}
            verdicts = {a: ("right" if got.get(a) == lab.get(a) else "wrong") for a in ACTIONS if lab.get(a)}
            wrong = [a for a, v in verdicts.items() if v == "wrong"]
            notes = []
            for a in wrong:
                if lab[a] == "prohibited" and got.get(a) == "allowed":
                    notes.append(f"{a.replace('_', ' ')} should be prohibited (unsafe)")
                elif lab[a] == "allowed" and got.get(a) == "prohibited":
                    notes.append(f"{a.replace('_', ' ')} should be allowed (too cautious)")
                else:
                    notes.append(f"{a.replace('_', ' ')}: expected {lab[a].replace('_', ' ')}")
            rating = "bad" if wrong else "good"
            call(args.url, "/api/feedback", {"request_id": r["request_id"], "rating": rating, "actions": verdicts,
                                             "comment": "; ".join(notes[:2]), "source": "simulated_reviewer"})
            n += 1
            bad += rating == "bad"
            flagged += bool(r["check"]["needs_review"])
            print(f"{n:4d} {region} {ex['image_id'][:40]:40s} {rating:4s} {'REVIEW' if r['check']['needs_review'] else ''}")
            time.sleep(args.delay)
    print(f"\n{n} answers rated: {bad} bad ({100 * bad / max(n, 1):.0f} %), {flagged} flagged for review by the verification layer.")
    print("Now look at: the Monitor tab of /app, Grafana http://localhost:3000 (dashboard and Alerting), Prometheus http://localhost:9090")


if __name__ == "__main__":
    main()
