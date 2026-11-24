"""Reading frames straight from the video file (no frame dump), and saving the ones you keep."""
from __future__ import annotations

import math
import threading
from pathlib import Path

import cv2
import numpy as np

from .core import ToolError


class VideoReader:
    """Thread-safe frame access. Reading forward is cheap; jumping back or far ahead seeks."""

    MAX_FORWARD = 150  # frames; reading this many forward is faster than a seek

    def __init__(self, path: str | Path):
        self.path = str(path)
        self.cap = cv2.VideoCapture(self.path)
        if not self.cap.isOpened():
            raise ToolError(f"OpenCV could not open {self.path}. Is it a video file (mp4/mov/avi)?")
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.fps = float(fps) if fps and math.isfinite(fps) and fps > 0 else 30.0
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        self.lock = threading.RLock()
        self.pos = 0  # index of the next frame read() returns
        first = self.read_at(0)
        if first is None:
            raise ToolError(f"Could not decode the first frame of {self.path}.")
        self.height, self.width = first.shape[:2]
        fourcc = int(self.cap.get(cv2.CAP_PROP_FOURCC) or 0)
        self.codec = "".join(chr((fourcc >> (8 * i)) & 0xFF) for i in range(4)).strip("\x00 ") or "unknown"

    def info(self) -> dict:
        n = self.frame_count
        return {
            "width": self.width, "height": self.height, "fps": round(self.fps, 3),
            "frame_count": n, "duration_s": round(n / self.fps, 2) if n else None, "codec": self.codec,
        }

    def read_at(self, idx: int) -> np.ndarray | None:
        with self.lock:
            idx = max(0, int(idx))
            if idx < self.pos or idx - self.pos > self.MAX_FORWARD:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
                self.pos = idx
            while self.pos < idx:
                if not self.cap.grab():
                    return None
                self.pos += 1
            ok, frame = self.cap.read()
            if not ok:
                return None
            self.pos = idx + 1
            return frame

    def iter_frames(self, start: int, end: int | None, step: int):
        """Read sequentially (accurate and fast); yield (index, frame) every `step` frames."""
        with self.lock:
            if self.pos != start:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, start)
            self.pos = idx = start
            while end is None or idx < end:
                if not self.cap.grab():
                    break
                self.pos = idx + 1
                if (idx - start) % step == 0:
                    ok, frame = self.cap.retrieve()
                    if ok:
                        yield idx, frame
                idx += 1

    def close(self) -> None:
        with self.lock:
            self.cap.release()


def apply_masks(frame: np.ndarray, masks: list) -> np.ndarray:
    """Black out burned-in overlays (date, GPS, speed) given in source-pixel coordinates."""
    if not masks:
        return frame
    out = frame.copy()
    h, w = out.shape[:2]
    for m in masks:
        x1, y1, x2, y2 = (int(round(v)) for v in m)
        x1, x2 = sorted((max(0, min(w, x1)), max(0, min(w, x2))))
        y1, y2 = sorted((max(0, min(h, y1)), max(0, min(h, y2))))
        out[y1:y2, x1:x2] = 0
    return out


def output_size(src_w: int, src_h: int, out_width: int | None) -> tuple[int, int]:
    if not out_width or out_width >= src_w:
        return src_w, src_h
    h = int(round(src_h * out_width / src_w / 2.0)) * 2
    return int(out_width), h


def resize(frame: np.ndarray, size: tuple[int, int]) -> np.ndarray:
    if (frame.shape[1], frame.shape[0]) == tuple(size):
        return frame
    return cv2.resize(frame, size, interpolation=cv2.INTER_AREA)


def encode_jpeg(frame: np.ndarray, quality: int = 90) -> bytes:
    ok, buf = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), int(quality)])
    if not ok:
        raise ToolError("JPEG encoding failed.")
    return buf.tobytes()


def write_jpeg(path: Path, frame: np.ndarray, quality: int = 95) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(".tmp_" + path.name)
    tmp.write_bytes(encode_jpeg(frame, quality))
    tmp.replace(path)


def read_image(path: Path) -> np.ndarray:
    data = np.frombuffer(Path(path).read_bytes(), dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if img is None:
        raise ToolError(f"Could not read image {path}")
    return img


def blur_boxes(img: np.ndarray, boxes: list, block: int = 10) -> np.ndarray:
    """Pixelate, then blur, each box. Pixelation throws the detail away, so it cannot be undone."""
    out = img.copy()
    h, w = out.shape[:2]
    for b in boxes:
        x1, y1, x2, y2 = (int(round(v)) for v in b)
        x1, x2 = sorted((max(0, min(w, x1)), max(0, min(w, x2))))
        y1, y2 = sorted((max(0, min(h, y1)), max(0, min(h, y2))))
        if x2 - x1 < 2 or y2 - y1 < 2:
            continue
        roi = out[y1:y2, x1:x2]
        small = cv2.resize(roi, (max(1, (x2 - x1) // block), max(1, (y2 - y1) // block)), interpolation=cv2.INTER_AREA)
        pix = cv2.resize(small, (x2 - x1, y2 - y1), interpolation=cv2.INTER_NEAREST)
        k = max(3, (min(x2 - x1, y2 - y1) // 4) | 1)
        out[y1:y2, x1:x2] = cv2.GaussianBlur(pix, (k, k), 0)
    return out


def render_frame(reader: VideoReader, frame_index: int, masks: list, size: tuple[int, int]) -> np.ndarray:
    frame = reader.read_at(frame_index)
    if frame is None:
        raise ToolError(f"Frame {frame_index} could not be decoded.")
    return resize(apply_masks(frame, masks), size)
