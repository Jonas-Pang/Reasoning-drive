"""Image files read and written through bytes, so paths with non-ASCII characters (F:\\数据集\\...) work on Windows,
where cv2.imread and cv2.imwrite cannot open them."""
from __future__ import annotations

from pathlib import Path


def imread(path, flags=None):
    """Like cv2.imread: the image, or None if the file is missing or not an image."""
    import cv2
    import numpy as np
    try:
        data = np.fromfile(str(path), dtype=np.uint8)
    except (OSError, ValueError):
        return None
    if data.size == 0:
        return None
    return cv2.imdecode(data, cv2.IMREAD_COLOR if flags is None else flags)


def imwrite(path, img, params=None) -> bool:
    """Like cv2.imwrite; the format follows the file extension."""
    import cv2
    ok, buf = cv2.imencode(Path(path).suffix or ".png", img, params or [])
    if ok:
        buf.tofile(str(path))
    return bool(ok)
