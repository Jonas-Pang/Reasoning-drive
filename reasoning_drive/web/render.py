"""Annotated output videos of the Video tab (Claude, 2026-11-18).

After a clip is analysed, the original video is drawn over and written out again:
  annotated.mp4    the whole clip: what the system read at every moment (top panel), the lane timeline with the
                   events and the play head (bottom bar), a red frame and banner while a problem is on screen
  problem_<k>.mp4  one short clip per problem: the intended manoeuvre that is prohibited at the end of the clip, or
                   an executed manoeuvre that broke the rule (a few seconds before and after it)
Encoding: ffmpeg with H.264 when it is installed (the Docker image has it), so every browser plays the files; else
OpenCV (avc1, then mp4v: the file may only play after download).
"""
from __future__ import annotations

import shutil
import subprocess
from functools import lru_cache
from pathlib import Path

import cv2
import numpy as np

ACTIONS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"]
SHORT = {"change_left": "Chg L", "change_right": "Chg R", "go_straight": "Straight", "turn_left": "Left",
         "turn_right": "Right", "u_turn": "U-turn", "enter_waiting_area": "Wait area"}
NAME = {"change_left": "CHANGE LANE LEFT", "change_right": "CHANGE LANE RIGHT", "go_straight": "GO STRAIGHT",
        "turn_left": "TURN LEFT", "turn_right": "TURN RIGHT", "u_turn": "U-TURN", "enter_waiting_area": "ENTER WAITING AREA"}
# BGR
GREEN, RED, ORANGE, GREY, WHITE, YELLOW, DARK = (75, 160, 31), (40, 35, 200), (20, 130, 230), (150, 150, 150), (245, 245, 245), (40, 200, 240), (40, 27, 15)
VALUE_COLOR = {"allowed": GREEN, "prohibited": RED, "stop_first": ORANGE}
FONT = cv2.FONT_HERSHEY_SIMPLEX
MAX_W = 1280


@lru_cache(maxsize=1)
def _ffmpeg() -> str:
    ff = shutil.which("ffmpeg")
    if not ff:
        return ""
    try:
        enc = subprocess.run([ff, "-hide_banner", "-encoders"], capture_output=True, text=True, timeout=20).stdout
    except (OSError, subprocess.SubprocessError):
        return ""
    return ff if "libx264" in enc else ""


class Writer:
    def __init__(self, path: Path, fps: float, w: int, h: int):
        self.path, self.codec, self.proc, self.vw = Path(path), "", None, None
        ff = _ffmpeg()
        if ff:
            self.proc = subprocess.Popen([ff, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{w}x{h}",
                                          "-r", f"{fps:.3f}", "-i", "-", "-an", "-c:v", "libx264", "-preset", "veryfast",
                                          "-crf", "23", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(self.path)],
                                         stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            self.codec = "h264"
            return
        for fourcc, name in (("avc1", "h264"), ("mp4v", "mp4v")):
            vw = cv2.VideoWriter(str(self.path), cv2.VideoWriter_fourcc(*fourcc), fps, (w, h))
            if vw.isOpened():
                self.vw, self.codec = vw, name
                return
        raise RuntimeError("No video encoder: install ffmpeg (the Docker image has it).")

    def write(self, img) -> None:
        if self.proc:
            self.proc.stdin.write(np.ascontiguousarray(img).tobytes())
        else:
            self.vw.write(img)

    def close(self) -> str:
        if self.proc:
            self.proc.stdin.close()
            err = self.proc.stderr.read().decode("utf-8", "replace")
            if self.proc.wait() != 0:
                raise RuntimeError("ffmpeg failed: " + err[-300:])
        else:
            self.vw.release()
        return self.codec


# ------------------------------------------------------------------ what is a problem

def problems(job: dict) -> list[dict]:
    """Time windows to show in red: a prohibited navigation intent at the end of the clip, and executed manoeuvres
    that broke the rule (by the ground truth when the event file gives it, else by the system's own reading)."""
    dur = job["video"]["duration_s"]
    out = []
    ic = job.get("intent_check")
    if ic and ic.get("verdict") == "violation":
        out.append({"kind": "intent", "action": ic["action"], "at_s": ic["at_s"], "start_s": max(0.0, dur - 5.0), "end_s": dur,
                    "label": f"NAV INTENT {NAME[ic['action']]}: prohibited here", "frame": ic.get("frame")})
    for e in job.get("event_checks") or []:
        broke = e.get("truth") == "prohibited" or (not e.get("truth") and e.get("value") == "prohibited")
        if not broke:
            continue
        fault = (e.get("attribution") or "").replace("_", " ")
        out.append({"kind": "event", "action": e["action"], "at_s": e["t"], "start_s": max(0.0, e["t"] - 3.0),
                    "end_s": min(dur, e["t"] + 3.0), "frame": e.get("frame"), "evidence_t": e.get("evidence_t"),
                    "label": f"{NAME[e['action']]} at {e['t']:.1f}s broke the rule" + (f" | fault: {fault}" if fault else "")})
    for k, p in enumerate(out):
        p["k"] = k + 1
    return out


# ------------------------------------------------------------------ drawing

def _seg_at(segs: list, t: float) -> dict | None:
    for s in segs:
        if s["start_s"] <= t < s["end_s"]:
            return s
    return segs[-1] if segs else None


def _seg_color(s: dict):
    v = [s["actions"].get(a) for a in ("change_left", "change_right")]
    if all(x == "prohibited" for x in v):
        return RED
    if all(x == "allowed" for x in v):
        return GREEN
    if all((not x) or x == "not_applicable" for x in v):
        return GREY
    return ORANGE


def _text(img, txt, org, scale, color, thick=1):
    # drop shadow at the same weight: newer OpenCV draws a bolder (wider) glyph for a thicker stroke, so a thick
    # black outline no longer lines up with the text on top of it
    d = max(1, int(round(2 * scale)))
    cv2.putText(img, txt, (org[0] + d, org[1] + d), FONT, scale, (0, 0, 0), thick, cv2.LINE_AA)
    cv2.putText(img, txt, org, FONT, scale, color, thick, cv2.LINE_AA)


def overlay(img, t: float, job: dict, probs: list) -> np.ndarray:
    h, w = img.shape[:2]
    s = w / 1280.0
    segs, dur = job.get("segments") or [], job["video"]["duration_s"]
    seg = _seg_at(segs, t)
    # top panel
    ph = int(96 * s)
    band = img[:ph].copy()
    cv2.rectangle(band, (0, 0), (w, ph), DARK, -1)
    img[:ph] = cv2.addWeighted(band, 0.72, img[:ph], 0.28, 0)
    rules = job.get("rules") or "none"
    head = f"{t:5.1f}s   rules: {rules} (Test {job.get('test')})"
    if seg:
        head += f"   L: {seg['left']}   R: {seg['right']}" + (f"   {' '.join(a.split(':')[1] for a in seg['arrows'])} arrow" if seg["arrows"] else "")
    _text(img, head, (int(14 * s), int(32 * s)), 0.62 * s, WHITE, max(1, int(s)))
    if seg:
        x = int(14 * s)
        for a in ACTIONS:
            v = seg["actions"].get(a) or "-"
            col = VALUE_COLOR.get(v, GREY)
            mark = {"allowed": "yes", "prohibited": "NO", "stop_first": "stop"}.get(v, "-")
            label = f"{SHORT[a]} {mark}"
            (tw, th), _ = cv2.getTextSize(label, FONT, 0.58 * s, max(1, int(s)))
            cv2.rectangle(img, (x - int(6 * s), int(48 * s)), (x + tw + int(6 * s), int(80 * s)), col, -1)
            cv2.putText(img, label, (x, int(72 * s)), FONT, 0.58 * s, WHITE, max(1, int(s)), cv2.LINE_AA)
            x += tw + int(22 * s)
        if seg.get("needs_review"):
            _text(img, "NEEDS REVIEW" + (" (line flicker)" if "line_flicker" in seg.get("flags", []) else ""),
                  (x + int(6 * s), int(72 * s)), 0.58 * s, YELLOW, max(1, int(s)))
    # problem: red frame and banner
    active = [p for p in probs if p["start_s"] <= t <= p["end_s"]]
    if active:
        cv2.rectangle(img, (0, 0), (w - 1, h - 1), RED, int(10 * s))
        p = active[0]
        by = ph + int(8 * s)
        cv2.rectangle(img, (int(10 * s), by), (w - int(10 * s), by + int(44 * s)), RED, -1)
        cv2.putText(img, f"PROBLEM {p['k']}: {p['label']}", (int(22 * s), by + int(30 * s)), FONT, 0.72 * s, WHITE, max(2, int(2 * s)), cv2.LINE_AA)
        if p.get("evidence_t") is not None and abs(t - p["evidence_t"]) < 0.5:
            _text(img, "EVIDENCE FRAME (what the system read)", (int(22 * s), by + int(80 * s)), 0.62 * s, YELLOW, max(1, int(s)))
    # bottom timeline
    y0, bh, x0, x1 = h - int(30 * s), int(14 * s), int(14 * s), w - int(14 * s)
    cv2.rectangle(img, (x0 - 2, y0 - 2), (x1 + 2, y0 + bh + 2), DARK, -1)
    for sg in segs:
        a = x0 + int((x1 - x0) * sg["start_s"] / dur)
        b = x0 + int((x1 - x0) * sg["end_s"] / dur)
        cv2.rectangle(img, (a, y0), (max(a + 1, b - 1), y0 + bh), _seg_color(sg), -1)
    for p in probs:
        xm = x0 + int((x1 - x0) * min(p["at_s"], dur) / dur)
        cv2.rectangle(img, (xm - 2, y0 - int(8 * s)), (xm + 2, y0 + bh + int(8 * s)), RED, -1)
    xp = x0 + int((x1 - x0) * min(t, dur) / dur)
    cv2.rectangle(img, (xp - 1, y0 - int(10 * s)), (xp + 1, y0 + bh + int(10 * s)), WHITE, -1)
    return img


# ------------------------------------------------------------------ writing

def _size(w: int, h: int) -> tuple[int, int]:
    if w > MAX_W:
        h, w = int(round(h * MAX_W / w)), MAX_W
    return w - w % 2, h - h % 2


def render(src: Path, out: Path, job: dict, probs: list, t0: float = 0.0, t1: float | None = None, progress=None) -> str:
    cap = cv2.VideoCapture(str(src))
    if not cap.isOpened():
        raise RuntimeError("cannot open the uploaded video again")
    fps = cap.get(cv2.CAP_PROP_FPS) or job["video"]["fps"] or 25.0
    w, h = _size(job["video"]["width"], job["video"]["height"])
    t1 = job["video"]["duration_s"] if t1 is None else t1
    if t0 > 0:
        cap.set(cv2.CAP_PROP_POS_MSEC, t0 * 1000.0)
    wr = Writer(out, min(fps, 30.0), w, h)
    step = max(1, int(round(fps / 30.0)))     # e.g. 60 fps in -> every 2nd frame
    n = 0
    try:
        while True:
            ok, f = cap.read()
            if not ok:
                break
            t = (cap.get(cv2.CAP_PROP_POS_MSEC) or 0.0) / 1000.0
            if t > t1 + 1e-3:
                break
            n += 1
            if (n - 1) % step:
                continue
            if f.shape[1] != w or f.shape[0] != h:
                f = cv2.resize(f, (w, h), interpolation=cv2.INTER_AREA)
            wr.write(overlay(f, t, job, probs))
            if progress:
                progress(t)
    finally:
        cap.release()
        codec = wr.close()
    return codec


def render_all(src: Path, outdir: Path, job: dict, progress=None) -> dict:
    """annotated.mp4 for the whole clip, problem_<k>.mp4 for every problem window."""
    probs = problems(job)
    outdir.mkdir(parents=True, exist_ok=True)
    codec = render(src, outdir / "annotated.mp4", job, probs, progress=progress)
    clips = []
    for p in probs:
        name = f"problem_{p['k']}.mp4"
        render(src, outdir / name, job, probs, p["start_s"], p["end_s"])
        clips.append({**p, "file": name})
    return {"annotated": "annotated.mp4", "codec": codec, "problems": clips}
