"""A small synthetic night drive, used by `python -m video_tool selftest`.

0-15 s driving, 15-25 s stopped at a red light, 25-60 s driving again with a straight-or-right
arrow passing at 30-36 s. A car with a lit plate drives ahead during 0-25 s. A burned-in
dash-cam overlay sits in the bottom-left corner.
"""
from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np

W, H, FPS = 1280, 720, 30
VP = (640, 400)          # vanishing point
STOP = (15.0, 25.0)      # stopped between these times
ARROW = (30.0, 36.0)
OVERLAY_BOX = [20, 660, 520, 705]
PLATE_BOX_AT_20S = None  # filled in by make_video for the self test


def _speed(t: float) -> float:
    if STOP[0] <= t < STOP[1]:
        return 0.0
    if STOP[0] - 2 <= t < STOP[0]:
        return (STOP[0] - t) / 2       # braking
    if STOP[1] <= t < STOP[1] + 2:
        return (t - STOP[1]) / 2       # pulling away
    return 1.0


def _road_point(x_bottom: float, s: float) -> tuple[int, int]:
    """Point on a straight line that meets the bottom of the frame at x_bottom; s=0 bottom, s=1 horizon."""
    x = x_bottom + (VP[0] - x_bottom) * s
    y = H + (VP[1] - H) * s
    return int(x), int(y)


def _depth_to_s(d: float) -> float:
    return 1.0 - 1.0 / (1.0 + d / 6.0)  # simple perspective: near distances spread out


_CACHE: dict = {}


def _background() -> np.ndarray:
    if "bg" not in _CACHE:
        img = np.zeros((H, W, 3), np.float32)
        img[: VP[1]] = (12, 10, 8)
        yy, xx = np.mgrid[VP[1]:H, 0:W]
        beam = np.exp(-(((xx - W / 2) / 420.0) ** 2)) * ((yy - VP[1]) / (H - VP[1])) ** 0.7
        road = 18 + 45 * beam
        img[VP[1]:] = np.dstack([road, road, road * 1.05])
        _CACHE["bg"] = np.clip(img, 0, 255).astype(np.uint8)
    return _CACHE["bg"].copy()


def _noise(i: int, rng: np.random.Generator) -> np.ndarray:
    if "noise" not in _CACHE:
        _CACHE["noise"] = [rng.normal(0, 3.0, (H, W, 3)).astype(np.int16) for _ in range(6)]
    return _CACHE["noise"][i % 6]


def _frame(t: float, dist: float, rng: np.random.Generator, i: int = 0) -> np.ndarray:
    img = _background()
    # lane edges: yellow double solid on the left, white dashed on the right
    for xb, col in ((70, (40, 200, 230)), (100, (40, 200, 230))):
        cv2.line(img, _road_point(xb, 0.0), _road_point(xb, 0.97), col, 4, cv2.LINE_AA)
    for k in range(40):
        d0 = k * 4.0 - (dist % 4.0)
        d1 = d0 + 1.5
        if d1 <= 0:
            continue
        p0 = _road_point(1150, _depth_to_s(max(d0, 0)))
        p1 = _road_point(1150, _depth_to_s(d1))
        cv2.line(img, p0, p1, (215, 215, 215), 6, cv2.LINE_AA)
    # arrow painted in the ego lane, moving towards the camera while driving
    if ARROW[0] <= t < ARROW[1]:
        d = 30.0 - (t - ARROW[0]) * 5.0
        if d > 0:
            s = _depth_to_s(d)
            cx, cy = _road_point(640, s)
            sc = (1 - s) * 2.2
            shaft = [(cx, int(cy + 40 * sc)), (cx, int(cy - 40 * sc))]
            cv2.line(img, *shaft, (220, 220, 220), max(2, int(8 * sc)))
            cv2.fillConvexPoly(img, np.array([[cx - int(18 * sc), int(cy - 40 * sc)], [cx + int(18 * sc), int(cy - 40 * sc)], [cx, int(cy - 70 * sc)]]), (220, 220, 220))
            cv2.line(img, (cx, int(cy)), (cx + int(35 * sc), int(cy - 25 * sc)), (220, 220, 220), max(2, int(8 * sc)))
    # car ahead with tail lights and a lit plate
    if t < STOP[1]:
        cx, cy = 640, 470
        cv2.rectangle(img, (cx - 110, cy - 60), (cx + 110, cy + 40), (25, 25, 30), -1)
        cv2.circle(img, (cx - 85, cy - 20), 14, (30, 30, 255), -1)
        cv2.circle(img, (cx + 85, cy - 20), 14, (30, 30, 255), -1)
        cv2.rectangle(img, (cx - 45, cy - 5), (cx + 45, cy + 25), (210, 210, 220), -1)
        cv2.putText(img, "ABC 123", (cx - 40, cy + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (20, 20, 20), 2)
    if STOP[0] - 2 <= t < STOP[1]:
        cv2.circle(img, (900, 140), 16, (40, 40, 255), -1)
    img = np.clip(img.astype(np.int16) + _noise(i, rng), 0, 255).astype(np.uint8)
    hh, mm, ss = 21, 30 + int(t) // 60, int(t) % 60
    cv2.rectangle(img, tuple(OVERLAY_BOX[:2]), tuple(OVERLAY_BOX[2:]), (0, 0, 0), -1)
    cv2.putText(img, f"2026/10/16 {hh}:{mm:02d}:{ss:02d}  {int(30 * _speed(t))} MPH  N29.65 W82.32",
                (28, 692), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    return img


def make_video(path: Path, seconds: float = 60.0) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(str(path), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (W, H))
    if not writer.isOpened():
        raise RuntimeError("OpenCV could not write the test video.")
    rng = np.random.default_rng(6216)
    dist = 0.0
    for i in range(int(seconds * FPS)):
        t = i / FPS
        dist += 0.6 * _speed(t)
        writer.write(_frame(t, dist, rng, i))
    writer.release()
    return path
