"""Run the CARLA violation clips through the web app's Video tab, one after another (Claude, 2026-11-18).

Each clip is uploaded with its events file (<clip>.events.json: when the car broke the rule and what the right
answer is under US and CN rules), analysed frame by frame, and rendered to annotated.mp4 + problem_k.mp4.
The answers go into the app's cache, so the same clip uploaded again in the browser comes back at once:
run this the evening before a demo.

  python scripts/run_violation_clips.py --model navigator          # UF NaviGator (needs NAVIGATOR_API_KEY in .env)
  python scripts/run_violation_clips.py --model openai             # OpenAI (paid: about 11 runs x 20 frames)
  python scripts/run_violation_clips.py --model mock               # no model, only checks the pipeline
  python scripts/run_violation_clips.py --only 04 08               # some clips only

Clip 08 is run twice: US rules (allowed) and CN rules (prohibited), the one clip where the country matters.
The road is always "United States" (a CARLA town), so 08 with China's rules is Test C. Use the same choices in the
browser (road United States, the same rules and model, sampling left at its defaults) or the cache is not hit.
Writes a summary to <clips>/runs_<model>.json. The app must be running (docker compose up -d).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]


def call(base: str, path: str, data=None, raw=False, timeout=900):
    if data is None:
        req = urllib.request.Request(base + path)
    else:
        body = data if raw else json.dumps(data).encode()
        req = urllib.request.Request(base + path, data=body, headers={
            "Content-Type": "application/octet-stream" if raw else "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="http://localhost:8770")
    ap.add_argument("--clips", default=str(HERE / "carla_violation_clips"))
    ap.add_argument("--model", default="navigator", help="navigator | openai | mock")
    ap.add_argument("--only", nargs="*", default=[], help="clip numbers, e.g. 04 08")
    a = ap.parse_args()

    clips = sorted(Path(a.clips).glob("*.mp4"))
    if a.only:
        clips = [c for c in clips if c.name[:2] in a.only]
    if not clips:
        print("no clips in", a.clips)
        return 1
    try:
        call(a.base, "/api/app/info")
    except Exception as e:  # noqa: BLE001
        print(f"the app is not reachable at {a.base}: {e}\nstart it first: docker compose up -d")
        return 1

    rows = []
    for clip in clips:
        ev_file = clip.with_name(clip.stem + ".events.json")
        events = ev_file.read_text() if ev_file.exists() else ""
        up = call(a.base, "/api/app/video/upload?name=" + clip.name, clip.read_bytes(), raw=True)
        for rules in (["US", "CN"] if clip.name.startswith("08") else ["US"]):
            t0 = time.time()
            job = call(a.base, "/api/app/video/start", {
                "video_id": up["video_id"], "region": "US", "rules": rules, "model": a.model,
                "intent": "", "events": events, "session": "batch-violation-clips"})
            while True:
                s = call(a.base, "/api/app/video/status?job=" + job["job_id"])
                if s["state"] in ("done", "error"):
                    break
                time.sleep(2)
            e = (s.get("event_checks") or [{}])[0]
            row = {"clip": clip.name, "rules": rules, "state": s["state"], "error": s.get("error") or s.get("render_error") or "",
                   "frames": len(s.get("frames") or []), "segments": len(s.get("segments") or []),
                   "action": e.get("action"), "at_s": e.get("t"), "evidence_s": e.get("evidence_t"),
                   "truth": e.get("truth"), "system_said": e.get("value"), "fault": e.get("attribution"),
                   "problems": len((s.get("outputs") or {}).get("problems") or []),
                   "seconds": round(time.time() - t0, 1), "job_id": job["job_id"]}
            rows.append(row)
            print(f"{clip.name[:2]} {rules}  {row['state']:5}  {row['action']} @ {row['at_s']}s  truth={row['truth']}  "
                  f"system={row['system_said']}  fault={row['fault']}  problems={row['problems']}  {row['seconds']}s"
                  + (f"  ERROR {row['error']}" if row["error"] else ""), flush=True)

    out = Path(a.clips) / f"runs_{a.model}.json"
    out.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    faults = {}
    for r in rows:
        faults[r["fault"]] = faults.get(r["fault"], 0) + 1
    print("\nfault counts:", faults, "\nsummary:", out)
    return 0 if all(r["state"] == "done" for r in rows) else 2


if __name__ == "__main__":
    sys.exit(main())
