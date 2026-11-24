"""Written by Claude: switch the China (MapDR) and US (BDD100K) image sets to one lane annotator per image
(lane_annotators_required = {"dev": 1, "test": 1}; the owner's decision of 2026-11-15: one label per image, checked by
a random spot-check instead of a second annotator), then merge again so finished labels become final.
Stop the labeling tools first.   python scripts/claude_single_annotator.py"""
import json, os, sys
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo))
from reasoning_drive.labeling.core import Paths, Trip
from reasoning_drive.labeling.lanes import merge_lanes
root = Path(os.environ.get("DATASETS_ROOT") or "")
if not root.is_dir():
    for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
        k, _, v = line.partition("=")
        if k.strip() == "DATASETS_ROOT":
            root = (repo / v.strip().strip('"')).resolve()
for ws, sid in (("mapdr_ws", "mapdr"), ("bdd100k", "bdd100k_val")):
    paths = Paths.discover(repo, root / ws)
    f = paths.trip_json(sid)
    meta = json.loads(f.read_text(encoding="utf-8"))
    meta["lane_annotators_required"] = {"dev": 1, "test": 1}
    f.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    c = merge_lanes(paths, Trip(paths, sid))
    print(sid, f, dict(c), flush=True)
