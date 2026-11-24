"""Candidate frames for new countries from GeoDrive-Bench (Ma, Xiao and Jiang, 2026; github.com/gray311/CulturalDrive-Bench).

GeoDrive-Bench asks questions about frames of six public driving datasets: ONCE (China), Waymo (US), LingoQA (UK),
CoVLA (Japan), nuScenes (Singapore) and IDD (India). Its questions that mention lane markings point to frames where
markings are visible. This writes, per country, the paths of those frames relative to the dataset's own folder, so
`python main.py label images init <collection>` marks them as 'listed' when picking images to label. Only paths are kept:
no question, answer or image of the benchmark is copied.

    git clone https://github.com/gray311/CulturalDrive-Bench
    python main.py label geodrive CulturalDrive-Bench/culturebenchmark_eval.json
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

from .. import paths as P

# benchmark country -> (our code, the dataset folder in its paths, our collection name)
COUNTRIES = {"cn": ("CN", "once/", "once"), "us": ("US", "waymo/", "waymo"), "uk": ("UK", "lingoqa/", "lingoqa"),
             "jp": ("JP", "CoVLA-Dataset/", "covla"), "sg": ("SG", "nuscenes/", "nuscenes_sg"), "ind": ("IN", "idd_multimodal/", "idd")}
LANE_WORDS = re.compile(r"lane (line|marking)s?|road marking|solid (white|yellow)|white line|yellow line|dashed|broken line|"
                        r"double (yellow|white|solid)|zig.?zag|hatched|chevron|box junction|(turn|direction|lane) arrow|"
                        r"arrow marking|cent(re|er) line|lane divider|bus lane|give way line|stop line|edge line|"
                        r"cross (the )?(line|lane)|lane change|overtak", re.I)


def candidates(bench_json: str | Path, repo=None, log=print) -> dict:
    repo = Path(repo or P.REPO)
    items = json.loads(Path(bench_json).read_text(encoding="utf-8"))
    rows: dict[str, dict] = {}
    for it in items:
        c = COUNTRIES.get(str(it.get("country", "")).lower())
        text = " ".join([it.get("question", "")] + list(it.get("options") or []))
        if not c or not LANE_WORDS.search(text):
            continue
        code, root, coll = c
        for path in it.get("image_path") or []:
            i = path.find(root)
            if i < 0:
                continue
            rel = path[i + len(root):]
            key = (code, rel)
            r = rows.setdefault(key, {"region": code, "collection": coll, "rel": rel, "items": 0, "categories": set(), "words": set()})
            r["items"] += 1
            r["categories"].add(it.get("question_category", ""))
            r["words"] |= {m.group(0).lower() for m in LANE_WORDS.finditer(text)}
    written = {}
    for code in sorted({k[0] for k in rows}):
        out = repo / P.DATASETS / code / "candidates_geodrive.csv"
        out.parent.mkdir(parents=True, exist_ok=True)
        rs = sorted((r for (c, _), r in rows.items() if c == code), key=lambda r: r["rel"])
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["rel", "collection", "items", "categories", "lane_words"])
            for r in rs:
                w.writerow([r["rel"], r["collection"], r["items"], ";".join(sorted(r["categories"])), ";".join(sorted(r["words"]))])
        written[code] = len(rs)
        log(f"{out}: {len(rs)} frames")
    log("Frames per country: " + ", ".join(f"{k} {v}" for k, v in Counter(written).items()))
    return written
