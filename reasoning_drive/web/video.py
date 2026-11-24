"""Video input of the lane advisor (page /app, tab "Video"). Added by Claude, 2026-11-18.

A dash-cam clip (or a CARLA recording) goes through the same pipeline as a photo, frame by frame:

  upload (raw bytes, at most MAX_MB)                        POST /api/app/video/upload
  -> sample frames: one every `every` seconds, near-identical frames (car standing, still frames) skipped,
     the last frame always kept (the decision point of a clip), at most `max_frames`
  -> evidence frames for the ego manoeuvres of an optional event file (CARLA log): `lead` seconds before each event
  -> every frame: lane prompt (lane_v4c) + the chosen rules + the chosen model, then the verification layer (guard.py)
  -> segments: consecutive frames with the same two lines and arrows are one segment; per action the majority value,
     a tie goes to the more restrictive value; a line that flips A-B-A within three frames marks the segment for review
  -> intent check (optional, the navigation intent is never shown to the model): the intended manoeuvre against the
     last segment
  -> event check (optional): each executed manoeuvre against its evidence frame; with a ground-truth value in the event
     (CARLA map), the error is attributed to the perception layer or the decision layer
                                                            POST /api/app/video/start, GET /api/app/video/status
  -> annotated output (render.py): the original video drawn over (what the system read at each moment, the lane
     timeline, a red frame and banner while a problem is on screen) and one short clip per problem
                                                            GET /api/app/video/file
The uploaded video, its frames and the annotated videos stay in a temporary folder until the service stops or the user
deletes them (POST /api/app/video/delete); the same upload can be analysed again with other rules or another model. Frame answers go through Demo.app_answer (prediction log, Prometheus metrics, cache), so the same clip uploaded
again is answered from the cache without a model call.

Event file (optional): a JSON list, {"events": [...]}, or one JSON object per line, each with
  t       seconds from the start of the clip when the manoeuvre starts (also: time, time_s, t_s)
  action  one of ACTIONS or an alias below (also: maneuver, manoeuvre, executed)
  truth   optional: "allowed" / "prohibited" for that action at that moment (e.g. from the CARLA map and the rule table)
  note    optional text
"""
from __future__ import annotations

import atexit
import hashlib
import json
import shutil
import tempfile
import threading
import time
import traceback
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import cv2
import numpy as np

ACTIONS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"]
ALIASES = {
    "lane_change_left": "change_left", "change_lane_left": "change_left", "left_lane_change": "change_left",
    "cross_left": "change_left", "overtake": "change_left", "overtake_left": "change_left",
    "cross_the_centre_line": "change_left", "cross_the_center_line": "change_left",
    "lane_change_right": "change_right", "change_lane_right": "change_right", "right_lane_change": "change_right",
    "cross_right": "change_right",
    "straight": "go_straight", "go_straight_at_the_junction": "go_straight",
    "left": "turn_left", "left_turn": "turn_left", "right": "turn_right", "right_turn": "turn_right",
    "uturn": "u_turn", "u-turn": "u_turn",
    "enter_center_lane_to_wait": "enter_waiting_area", "enter_centre_lane_to_wait": "enter_waiting_area",
    "enter_waiting": "enter_waiting_area", "twltl": "enter_waiting_area",
}
MAX_MB = 500
MAX_SECONDS = 300
MAX_FRAMES = 40
SAME_FRAME = 2.0          # mean absolute difference (0-255) of a 64x36 grey thumbnail below which a frame is a repeat
RESTRICT = {"prohibited": 4, "stop_first": 3, "allowed": 2, "not_applicable": 1}


def norm_action(a) -> str:
    a = str(a or "").strip().lower().replace(" ", "_")
    a = ALIASES.get(a, a)
    if a not in ACTIONS:
        raise ValueError(f"Unknown action {a!r} in the event file; use one of {', '.join(ACTIONS)}.")
    return a


def parse_events(text: str) -> list[dict]:
    text = (text or "").strip()
    if not text:
        return []
    try:
        data = json.loads(text)
        rows = data.get("events", []) if isinstance(data, dict) else data
    except ValueError:
        rows = [json.loads(line) for line in text.splitlines() if line.strip()]
    out = []
    for i, r in enumerate(rows):
        t = next((r[k] for k in ("t", "time", "time_s", "t_s") if k in r), None)
        act = next((r[k] for k in ("action", "maneuver", "manoeuvre", "executed") if k in r), None)
        if t is None or act is None:
            raise ValueError(f"Event {i + 1} needs a time (t) and an action.")
        truth = r.get("truth")
        if isinstance(truth, dict) and not any(k.isupper() for k in truth):   # {"turn_right": "prohibited"}
            truth = truth.get(norm_action(act))
        if isinstance(truth, dict):                                         # {"US": "prohibited", "CN": ...}: by the rules chosen
            truth = {k.upper(): str(v).lower() for k, v in truth.items() if str(v).lower() in ("allowed", "prohibited")}
        else:
            truth = str(truth).lower() if truth else ""
            if truth not in ("allowed", "prohibited"):
                truth = ""
        out.append({"i": i, "t": float(t), "action": norm_action(act), "truth": truth, "note": str(r.get("note") or "")[:200]})
    return sorted(out, key=lambda e: e["t"])


def probe(path: Path) -> dict:
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise ValueError("OpenCV cannot open this file. Use an MP4 (H.264 or HEVC), MOV or AVI video.")
    fps = cap.get(cv2.CAP_PROP_FPS) or 0
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
    ok, first = cap.read()
    cap.release()
    if not ok or first is None:
        raise ValueError("The video has no readable frame.")
    fps = fps if fps and fps < 1000 else 25.0
    dur = n / fps if n > 0 else 0.0
    if dur <= 0:
        raise ValueError("Cannot read the length of the video.")
    return {"fps": round(fps, 3), "frames": n, "duration_s": round(dur, 2), "width": w or first.shape[1], "height": h or first.shape[0]}


def _read_at(cap, t: float):
    cap.set(cv2.CAP_PROP_POS_MSEC, max(0.0, t) * 1000.0)
    ok, f = cap.read()
    return f if ok else None


def _thumb(img) -> np.ndarray:
    return cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (64, 36), interpolation=cv2.INTER_AREA).astype(np.float32)


def select_frames(path: Path, info: dict, every: float = 1.0, max_frames: int = 20, events: list | None = None,
                  lead: float = 1.0) -> tuple[list[dict], dict]:
    """The frames to analyse: timeline frames (every `every` s, repeats skipped, the last frame always kept, thinned
    evenly to max_frames) and one evidence frame `lead` s before each event."""
    dur = info["duration_s"]
    every = max(0.25, float(every))
    times = [round(t, 3) for t in np.arange(min(0.5, dur / 2), dur, every)]
    last_t = round(max(0.0, dur - 0.1), 3)
    if not times or last_t - times[-1] > 0.3:
        times.append(last_t)
    cap = cv2.VideoCapture(str(path))
    kept, skipped, prev = [], 0, None
    for t in times:
        f = _read_at(cap, t)
        if f is None:
            continue
        th = _thumb(f)
        if prev is not None and float(np.abs(th - prev).mean()) < SAME_FRAME and t != times[-1]:
            skipped += 1
            continue
        prev = th
        kept.append({"t": t, "kind": "timeline", "img": f})
    if len(kept) > max_frames:   # thin evenly, keep the first and the last
        idx = sorted({round(i * (len(kept) - 1) / (max_frames - 1)) for i in range(max_frames)})
        skipped += len(kept) - len(idx)
        kept = [kept[i] for i in idx]
    for e in events or []:
        te = min(max(0.0, e["t"] - lead), last_t)
        f = _read_at(cap, te)
        if f is not None:
            kept.append({"t": round(te, 3), "kind": "evidence", "event": e["i"], "img": f})
    cap.release()
    kept.sort(key=lambda x: (x["t"], x["kind"] != "timeline"))
    return kept, {"sampled": len(times), "skipped_repeats_or_thinned": skipped}


# ------------------------------------------------------------------ from frame answers to segments and verdicts

def _line(b: dict | None) -> str:
    b = b or {}
    return f"{b.get('color') or '?'} {str(b.get('pattern') or '?').replace('_', '-')}"


def _arrows(ans: dict) -> tuple:
    out = []
    for m in ans.get("lane_markings") or []:
        tok = m.get("marking") if isinstance(m, dict) else m
        if isinstance(tok, str) and (tok.startswith("arrow:") or tok.startswith("no_turn:")):
            out.append(tok)
    return tuple(sorted(set(out)))


def signature(ans: dict | None) -> tuple | None:
    if not ans:
        return None
    return (_line(ans.get("left_boundary")), _line(ans.get("right_boundary")), _arrows(ans))


def restrictive_majority(values: list[str]) -> str:
    vals = [v for v in values if v]
    if not vals:
        return ""
    counts: dict = {}
    for v in vals:
        counts[v] = counts.get(v, 0) + 1
    top = max(counts.values())
    return max((v for v, c in counts.items() if c == top), key=lambda v: RESTRICT.get(v, 0))


def build_segments(frames: list[dict], duration: float) -> list[dict]:
    tl = [f for f in frames if f["kind"] == "timeline" and f.get("answer")]
    sigs = [signature(f["answer"]) for f in tl]
    segs: list[dict] = []
    for i, f in enumerate(tl):
        if segs and segs[-1]["sig"] == sigs[i]:
            segs[-1]["frames"].append(f["n"])
        else:
            segs.append({"sig": sigs[i], "start_s": f["t"], "frames": [f["n"]]})
    if segs:
        segs[0]["start_s"] = 0.0      # the first segment covers the clip from its start
    by_n = {f["n"]: f for f in tl}
    for k, s in enumerate(segs):
        s["end_s"] = segs[k + 1]["start_s"] if k + 1 < len(segs) else duration
        s["left"], s["right"], arrows = s["sig"][0], s["sig"][1], s["sig"][2]
        s["arrows"] = list(arrows)
        s["actions"] = {a: restrictive_majority([(by_n[n]["answer"].get("actions") or {}).get(a, "") for n in s["frames"]]) for a in ACTIONS}
        s["needs_review"] = any(by_n[n]["check"].get("needs_review") for n in s["frames"])
        s["flags"] = []
    for k in range(1, len(segs) - 1):   # A-B-A with a one-frame B: the line flickers -> unsure perception
        if len(segs[k]["frames"]) == 1 and segs[k - 1]["sig"] == segs[k + 1]["sig"]:
            for j in (k - 1, k, k + 1):
                if "line_flicker" not in segs[j]["flags"]:
                    segs[j]["flags"].append("line_flicker")
                segs[j]["needs_review"] = True
    for s in segs:
        s.pop("sig")
    return segs


def attribute(truth: str, model_value: str) -> tuple[str, str]:
    """Who is at fault for an executed manoeuvre, given the ground truth and what the perception layer said."""
    if truth == "prohibited" and model_value == "prohibited":
        return "decision_layer", "Perception said prohibited and was right; the decision layer executed the manoeuvre anyway."
    if truth == "prohibited":
        return "perception_layer", f"Perception said {model_value or 'nothing'} but the manoeuvre is prohibited; the decision layer was misled."
    if truth == "allowed" and model_value == "prohibited":
        return "perception_over_cautious", "The manoeuvre is allowed, but perception said prohibited (false alarm)."
    if truth == "allowed" and model_value in ("allowed", "stop_first"):
        return "compliant", "Allowed, and perception agreed."
    if truth == "allowed":
        return "compliant", f"Allowed; perception gave no decision ({model_value or 'no answer'})."
    return "", ""


def check_value(v: str) -> str:
    return {"prohibited": "violation", "stop_first": "conditional", "allowed": "ok"}.get(v or "", "not_governed")


# ------------------------------------------------------------------ jobs

class VideoJobs:
    def __init__(self, demo):
        self.demo = demo
        self.lock = threading.RLock()
        self.videos: dict = {}
        self.jobs: dict = {}
        self.dir = Path(tempfile.mkdtemp(prefix="lane_video_"))
        atexit.register(shutil.rmtree, self.dir, True)   # frames are deleted when the service stops

    def receive(self, rfile, length: int, name: str = "") -> dict:
        if length <= 0:
            raise ValueError("Empty upload.")
        if length > MAX_MB * 1024 * 1024:
            raise ValueError(f"The video is larger than {MAX_MB} MB.")
        vid = uuid.uuid4().hex[:12]
        path = self.dir / f"{vid}.video"
        h = hashlib.sha256()
        left = length
        with path.open("wb") as f:
            while left > 0:
                chunk = rfile.read(min(1 << 20, left))
                if not chunk:
                    break
                f.write(chunk)
                h.update(chunk)
                left -= len(chunk)
        if left:
            path.unlink(missing_ok=True)
            raise ValueError("The upload stopped before the end of the file.")
        try:
            info = probe(path)
        except ValueError:
            path.unlink(missing_ok=True)
            raise
        if info["duration_s"] > MAX_SECONDS:
            path.unlink(missing_ok=True)
            raise ValueError(f"The video is {info['duration_s']:.0f} s long; at most {MAX_SECONDS} s.")
        info.update({"video_id": vid, "name": str(name or "")[:120], "bytes": length, "sha256": h.hexdigest()[:16]})
        with self.lock:
            self.videos[vid] = {"path": path, "info": info}
        return info

    def start(self, body: dict) -> dict:
        vid = str(body.get("video_id") or "")
        with self.lock:
            v = self.videos.get(vid)
        if not v:
            raise KeyError("Upload the video first (or it was already analysed: upload it again).")
        region = str(body.get("region") or "US")
        test, rules = self.demo.app_test_for(region, str(body.get("rules") or region))
        choice = str(body.get("model") or "navigator")
        session = str(body.get("session") or "")
        self.demo.app_cfg_for(choice, region, rules, session)  # fails early: unknown model, key not set
        intent = norm_action(body["intent"]) if body.get("intent") else ""
        events = parse_events(body.get("events") or "")
        for e in events:                     # ground truth per rule set: take the one of the rules given to the model
            if isinstance(e["truth"], dict):
                e["truth"] = e["truth"].get(rules or region, "")
        job = {"job_id": uuid.uuid4().hex[:12], "video_id": vid, "video": v["info"], "region": region, "rules": rules,
               "test": test, "model": choice, "intent": intent, "events": events,
               "every": float(body.get("every") or 1.0), "max_frames": min(MAX_FRAMES, int(body.get("max_frames") or 20)),
               "lead": float(body.get("lead") or 1.0), "state": "queued", "done": 0, "total": 0, "error": "",
               "frames": [], "segments": [], "intent_check": None, "event_checks": [], "started": time.time(),
               "outputs": None, "render_error": "", "render_pct": 0, "_session": session}
        with self.lock:
            self.jobs[job["job_id"]] = job
        threading.Thread(target=self._run, args=(job, v["path"]), daemon=True).start()
        return {"job_id": job["job_id"]}

    def _run(self, job: dict, path: Path) -> None:
        demo = self.demo
        try:
            job["state"] = "sampling"
            frames, stats = select_frames(path, job["video"], job["every"], job["max_frames"], job["events"], job["lead"])
            job["sampling"] = stats
            fdir = self.dir / job["job_id"]
            fdir.mkdir(parents=True, exist_ok=True)
            items = []
            for n, f in enumerate(frames):
                ok, png = cv2.imencode(".png", f["img"])
                sha = hashlib.sha256(png.tobytes()).hexdigest()[:12]
                p = fdir / f"f{n:03d}_{sha}.png"
                p.write_bytes(png.tobytes())
                h, w = f["img"].shape[:2]
                f.pop("img")
                f.update({"n": n, "image_id": f"video_{sha}", "answer": None, "check": {}, "error": ""})
                items.append(demo.register_frame(f["image_id"], job["region"], p, w, h))
            job["frames"], job["total"], job["state"] = frames, len(frames), "analysing"
            par = max(1, min(4, int(demo.app_cfg_for(job["model"], job["region"], job["rules"], job["_session"])[0]["api"].get("parallel") or 3)))

            def one(n):
                f, it = frames[n], items[n]
                try:
                    out = demo.app_answer(it, job["test"], job["model"], job["rules"], mode="video", session=job["_session"])
                    f.update({"answer": out["answer"], "check": out["check"], "request_id": out["request_id"],
                              "latency_s": out["latency_s"], "cached": out["cached"], "error": out["error"],
                              "passages": out["passages"]})
                except Exception as e:  # noqa: BLE001
                    f["error"] = str(e)[:300]
                with self.lock:
                    job["done"] += 1

            with ThreadPoolExecutor(par) as ex:
                list(ex.map(one, range(len(frames))))
            job["segments"] = build_segments(frames, job["video"]["duration_s"])
            if job["intent"] and job["segments"]:
                last = job["segments"][-1]
                v = last["actions"].get(job["intent"], "")
                fr = frames[last["frames"][-1]]
                job["intent_check"] = {"action": job["intent"], "value": v, "verdict": check_value(v),
                                       "at_s": fr["t"], "frame": fr["n"],
                                       "reason": ((fr.get("answer") or {}).get("action_reasons") or {}).get(job["intent"], "")}
            for e in job["events"]:
                fr = next((f for f in frames if f["kind"] == "evidence" and f.get("event") == e["i"]), None)
                v = ((fr or {}).get("answer") or {}).get("actions", {}).get(e["action"], "") if fr else ""
                who, why = attribute(e["truth"], v)
                job["event_checks"].append({**e, "frame": fr["n"] if fr else None, "evidence_t": fr["t"] if fr else None,
                                            "value": v, "verdict": check_value(v), "attribution": who, "explanation": why,
                                            "reason": ((fr or {}).get("answer") or {}).get("action_reasons", {}).get(e["action"], "") if fr else ""})
            job["state"] = "rendering"
            try:
                from .render import render_all
                dur = job["video"]["duration_s"] or 1.0
                job["outputs"] = render_all(path, self.dir / job["job_id"] / "out", job,
                                            progress=lambda t: job.__setitem__("render_pct", min(100, int(100 * t / dur))))
            except Exception as e:  # noqa: BLE001  (the analysis stands without the video)
                traceback.print_exc()
                job["render_error"] = str(e)[:300]
            job["state"] = "done"
        except Exception as e:  # noqa: BLE001
            traceback.print_exc()
            job["state"], job["error"] = "error", str(e)[:400]
        finally:
            job["seconds"] = round(time.time() - job["started"], 1)
            if demo.metrics:
                demo.metrics.video_job(job)

    def file(self, job_id: str, name: str) -> Path:
        """An annotated video of a finished job (only names the job wrote)."""
        with self.lock:
            job = self.jobs.get(job_id)
        out = (job or {}).get("outputs") or {}
        names = {out.get("annotated")} | {c["file"] for c in out.get("problems") or []}
        if not job or name not in names:
            raise KeyError("No such video file.")
        return self.dir / job_id / "out" / name

    def delete(self, body: dict) -> dict:
        """Delete an uploaded video with every analysis of it: frames, annotated videos, results."""
        jid, vid = str(body.get("job_id") or ""), str(body.get("video_id") or "")
        with self.lock:
            if jid and jid in self.jobs:
                vid = vid or self.jobs[jid]["video_id"]
            if self.jobs.get(jid, {}).get("state") in ("queued", "sampling", "analysing", "rendering"):
                raise ValueError("The analysis is still running; delete it when it has finished.")
            gone = [j for j, job in self.jobs.items() if job["video_id"] == vid or j == jid]
            for j in gone:
                shutil.rmtree(self.dir / j, ignore_errors=True)
                self.jobs.pop(j, None)
            v = self.videos.pop(vid, None)
        if v:
            Path(v["path"]).unlink(missing_ok=True)
        return {"deleted_jobs": gone, "deleted_video": bool(v)}

    def status(self, job_id: str) -> dict:
        with self.lock:
            job = self.jobs.get(job_id)
            if not job:
                raise KeyError("Unknown video job.")
            return json.loads(json.dumps({k: v for k, v in job.items() if not k.startswith("_")}, default=str))
