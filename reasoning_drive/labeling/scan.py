"""Scan a video once and decide which moments are worth looking at.

Nothing is written as images. For every sample (default 2 per second) it records:
  motion      how much the road area in front changed since the previous sample
  stationary  the car stood still for a while (red light, traffic jam) -> hidden
  dup         too little change since the last shown sample (crawling in traffic) -> hidden
  brightness  mean brightness of the road area (0-255), a hint for very dark frames
  sharpness   variance of the Laplacian of the road area, a hint for motion blur
  paint       share of bright thin structures in the road area (painted lines catch the headlights)
  yellow      share of yellow pixels in the road area (yellow lines, two-way left-turn lanes)
Hidden samples are not deleted: the labeling tool can show them with "show all".
"""
from __future__ import annotations

import time

import cv2
import numpy as np

from .core import Paths, ToolError, Trip, utc_now, write_csv
from .video import VideoReader, apply_masks

SCAN_COLUMNS = [
    "sample", "frame_index", "time_s", "motion", "motion_smooth", "stationary", "dup",
    "dhash", "brightness", "sharpness", "paint", "yellow", "dark", "blurry", "candidate",
]

DEFAULT_ROI = {"x1": 0.15, "x2": 0.85, "y1": 0.50, "y2": 0.92}


def _dhash(gray: np.ndarray) -> int:
    g = cv2.resize(gray, (9, 8), interpolation=cv2.INTER_AREA).astype(np.int16)
    bits = (g[:, 1:] > g[:, :-1]).ravel()
    v = 0
    for b in bits:
        v = (v << 1) | int(b)
    return v


def _roi(img: np.ndarray, roi: dict) -> np.ndarray:
    h, w = img.shape[:2]
    return img[int(h * roi["y1"]): int(h * roi["y2"]), int(w * roi["x1"]): int(w * roi["x2"])]


_TOPHAT_KERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))


def features(frame: np.ndarray, roi: dict) -> dict:
    h, w = frame.shape[:2]
    small = cv2.resize(frame, (640, max(2, int(round(h * 640 / w)))), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    tiny = cv2.GaussianBlur(cv2.resize(gray, (320, max(2, gray.shape[0] // 2)), interpolation=cv2.INTER_AREA), (5, 5), 0)
    road = _roi(gray, roi)
    road_tiny = _roi(tiny, roi)
    tophat = cv2.morphologyEx(road, cv2.MORPH_TOPHAT, _TOPHAT_KERNEL)
    hsv = cv2.cvtColor(_roi(small, roi), cv2.COLOR_BGR2HSV)
    yellow = (hsv[..., 0] >= 15) & (hsv[..., 0] <= 35) & (hsv[..., 1] >= 90) & (hsv[..., 2] >= 90)
    return {
        "road_tiny": road_tiny.astype(np.float32),
        "dhash": _dhash(gray),
        "brightness": float(road.mean()),
        "sharpness": float(cv2.Laplacian(road, cv2.CV_64F).var()),
        "paint": float((tophat > 40).mean()),
        "yellow": float(yellow.mean()),
    }


def _rolling_median(x: np.ndarray, k: int = 5) -> np.ndarray:
    out = np.empty_like(x)
    r = k // 2
    for i in range(len(x)):
        win = x[max(0, i - r): i + r + 1]
        win = win[np.isfinite(win)]
        out[i] = np.median(win) if len(win) else np.nan
    return out


def auto_threshold(motion_smooth: np.ndarray) -> float:
    """Noise level of a parked car, estimated from the quietest samples, capped well below typical driving."""
    m = motion_smooth[np.isfinite(motion_smooth)]
    if len(m) < 10:
        return 1.0
    p05, med = float(np.percentile(m, 5)), float(np.median(m))
    return float(min(max(2.5 * p05, 0.6), max(0.6, 0.4 * med)))


def classify(rows: list[dict], fps_samples: float, motion_threshold: float | None, min_stop_s: float) -> dict:
    motion = np.array([r["motion"] for r in rows], dtype=float)
    smooth = _rolling_median(motion, 5)
    thr = float(motion_threshold) if motion_threshold is not None else auto_threshold(smooth)
    low = np.where(np.isfinite(smooth), smooth < thr, False)
    if len(low) > 1 and not np.isfinite(smooth[0]):
        low[0] = low[1]
    stationary = np.zeros(len(rows), dtype=bool)
    min_len = max(1, int(round(min_stop_s * fps_samples)))
    i = 0
    while i < len(low):
        if low[i]:
            j = i
            while j < len(low) and low[j]:
                j += 1
            if j - i >= min_len:
                stationary[i:j] = True
            i = j
        else:
            i += 1
    sharp = np.array([r["sharpness"] for r in rows], dtype=float)
    blur_cut = 0.35 * float(np.median(sharp)) if len(sharp) else 0.0
    # Show a sample once the road in front has changed enough since the last shown one.
    # Normal driving changes more than the threshold every sample, so every sample is shown;
    # crawling shows fewer; standing still shows none. (The dHash is kept for the cross-split check.)
    acc, shown_since_stop = 0.0, False
    for k, r in enumerate(rows):
        r["motion_smooth"] = round(float(smooth[k]), 3) if np.isfinite(smooth[k]) else ""
        r["stationary"] = int(stationary[k])
        dup = False
        if stationary[k]:
            shown_since_stop = False
        elif not shown_since_stop:
            shown_since_stop, acc = True, 0.0
        else:
            acc += float(smooth[k]) if np.isfinite(smooth[k]) else thr
            if acc >= thr:
                acc = 0.0
            else:
                dup = True
        r["dup"] = int(dup)
        r["dark"] = int(r["brightness"] < 12)
        r["blurry"] = int(r["sharpness"] < blur_cut)
        r["candidate"] = int(not stationary[k] and not dup)
    return {"motion_threshold": round(thr, 3), "auto_threshold": motion_threshold is None}


def scan_trip(paths: Paths, trip: Trip, sample_fps: float = 2.0, start_s: float | None = None, end_s: float | None = None,
              motion_threshold: float | None = None, min_stop_s: float = 3.0, log=print) -> dict:
    video = trip.check_video()
    reader = VideoReader(video)
    fps = reader.fps
    trim = trip.meta.setdefault("trim", {})
    if start_s is not None:
        trim["start_s"] = float(start_s)
    if end_s is not None:
        trim["end_s"] = float(end_s)
    s0 = float(trim.get("start_s") or 0.0)
    s1 = trim.get("end_s")
    start = int(round(s0 * fps))
    end = int(round(float(s1) * fps)) if s1 else None
    step = max(1, int(round(fps / sample_fps)))
    roi = trip.meta.get("scan_roi", DEFAULT_ROI)
    masks = trip.meta.get("masks", [])
    total = ((end or reader.frame_count or 0) - start) or None

    log(f"Scanning {video.name}: {reader.width}x{reader.height}, {fps:.2f} fps, one sample every {step} frames ({fps / step:.2f} per second).")
    rows, prev, t0 = [], None, time.time()
    last_report = t0
    for n, (idx, frame) in enumerate(reader.iter_frames(start, end, step)):
        f = features(apply_masks(frame, masks), roi)
        motion = float(np.abs(f["road_tiny"] - prev).mean()) if prev is not None else float("nan")
        prev = f["road_tiny"]
        rows.append({
            "sample": n, "frame_index": idx, "time_s": round(idx / fps, 3), "motion": motion,
            "dhash": f["dhash"], "brightness": round(f["brightness"], 2), "sharpness": round(f["sharpness"], 1),
            "paint": round(f["paint"], 5), "yellow": round(f["yellow"], 5),
        })
        now = time.time()
        if total and now - last_report > 10 and idx > start:
            done = (idx - start) / total
            eta = (now - t0) / max(done, 1e-6) * (1 - done)
            log(f"  {done * 100:5.1f}%  video time {idx / fps / 60:5.1f} min   about {eta / 60:.1f} min left")
            last_report = now
    reader.close()
    if len(rows) < 2:
        raise ToolError("The video gave fewer than 2 samples. Check --start/--end.")

    info = classify(rows, fps / step, motion_threshold, min_stop_s)
    for r in rows:
        r["motion"] = round(r["motion"], 3) if np.isfinite(r["motion"]) else ""
        r["dhash"] = f"{r['dhash']:016x}"
    write_csv(paths.scan_csv(trip.id), rows, SCAN_COLUMNS)

    n = len(rows)
    n_stat = sum(r["stationary"] for r in rows)
    n_dup = sum(r["dup"] for r in rows)
    n_cand = sum(r["candidate"] for r in rows)
    summary = {
        "scanned_utc": utc_now(),
        "elapsed_s": round(time.time() - t0, 1),
        "sample_fps": round(fps / step, 3),
        "step_frames": step,
        "start_s": s0,
        "end_s": s1,
        "samples": n,
        "stationary_samples": n_stat,
        "stationary_minutes": round(n_stat * step / fps / 60, 2),
        "duplicate_samples": n_dup,
        "candidates": n_cand,
        "dark_candidates": sum(1 for r in rows if r["candidate"] and r["dark"]),
        "blurry_candidates": sum(1 for r in rows if r["candidate"] and r["blurry"]),
        "min_stop_s": min_stop_s,
        "roi": roi,
        **info,
    }
    trip.meta["scan"] = summary
    trip.save()
    log(f"Done in {summary['elapsed_s']:.0f} s. {n} samples: {n_stat} while stopped ({summary['stationary_minutes']} min), "
        f"{n_dup} while crawling, {n_cand} left to look at ({n_cand / max(n, 1) * 100:.0f}%).")
    log(f"Motion threshold {info['motion_threshold']} ({'automatic' if info['auto_threshold'] else 'set by you'}). "
        f"If stops are missed, rerun with a higher --motion-threshold; if driving is hidden, use a lower one.")
    return summary
