"""Written by Claude, 2026-11-16: set up the small UK and India pilot in the SAME labeling tool as China and the US.

    python scripts/claude_pilot_ukin.py          (or double-click scripts/claude_pilot_ukin.bat)

What it does, without any API call:
 1. builds the labeling workspaces (once): DATASETS_ROOT/lingoqa_ws (UK, LingoQA frames under DATASETS_ROOT/lingoqa)
    and DATASETS_ROOT/idd_ws (India, IDD Multimodal frames under DATASETS_ROOT/idd);
 2. gives both image sets a small pilot quota and one lane annotator (the owner), as for China and the US;
 3. picks the frames listed in scripts/claude_pilot_drafts.json (chosen by Claude from the GeoDrive-Bench candidates,
    no near-duplicate scenes across dev and test) into their quota cells, using the tool's own picking code;
 4. saves Claude's lane label for each as the OWNER'S DRAFT (status draft): the owner opens the labeling window
    (scripts/label_all.bat, country switch UK / India), checks every image and saves it as done. Actions and rule IDs are
    the tool's own suggestion from regulations/<CODE>/lane_action_rules.json (lane_prefill), plus the few overrides in the
    drafts file (a hidden side is not_determined);
 5. records where each draft came from in results/claude_logs/provenance_labels.csv (internal; not in the labels).
Running it again changes nothing that is already there; with --redo-drafts it saves the drafts file again over the
owner's labels that are still drafts (never over a label saved as done).
"""
import csv
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo))
os.chdir(repo)
LOG = repo / "results" / "claude_logs" / "pilot_ukin.log"
REDO = "--redo-drafts" in sys.argv
LOG.parent.mkdir(parents=True, exist_ok=True)
log = open(LOG, "a", encoding="utf-8")


def say(msg=""):
    print(msg, flush=True)
    log.write(msg + "\n")
    log.flush()


root = os.environ.get("DATASETS_ROOT", "")
for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
    k, _, v = line.partition("=")
    if k.strip() == "DATASETS_ROOT" and v.strip() and not root:
        root = v.strip().strip('"')
if not root:
    say("DATASETS_ROOT is not set in .env")
    sys.exit(1)
root = (repo / root).resolve()

from reasoning_drive.labeling.core import OWNER, LabelStore, Paths, Trip  # noqa: E402
from reasoning_drive.labeling.imagesets import Picker, init_workspace  # noqa: E402
from reasoning_drive.labeling.lane_app import LaneApp  # noqa: E402
from reasoning_drive.labeling.lanes import (LANE_ACTIONS, lane_prefill, load_lane_rules, load_lane_schema,  # noqa: E402
                                            seed_lane_rows)

PILOT = [  # region, workspace folder, collection (datasets/<CODE>/dataset.yaml), images folder under DATASETS_ROOT
    ("UK", "lingoqa_ws", "lingoqa", "lingoqa"),
    ("IN", "idd_ws", "idd", "idd"),
]
QUOTA = {"dev": {"solid": 2, "dashed": 2, "yellow": 2, "arrow": 2, "degraded": 2},
         "test": {"solid": 4, "dashed": 4, "yellow": 4, "arrow": 4, "degraded": 4}}
drafts = json.loads((repo / "scripts" / "claude_pilot_drafts.json").read_text(encoding="utf-8"))
schema, table = load_lane_schema(repo), load_lane_rules(repo)
prov_file = repo / "results" / "claude_logs" / "provenance_labels.csv"
prov_rows = list(csv.DictReader(open(prov_file, encoding="utf-8-sig"))) if prov_file.exists() else []
have_prov = {r["image_id"] for r in prov_rows}
new_prov = []
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

for region, ws, coll, images in PILOT:
    say(f"=== {region}: workspace {root / ws}, images {root / images}")
    if not (root / images).is_dir():
        say(f"  images not found in {root / images}; skipped")
        continue
    paths = init_workspace(repo, root / ws, coll, str(root / images), log=lambda m: say("  " + m))
    paths = Paths.discover(repo, root / ws)
    trip = Trip(paths, coll)
    trip.meta["quota"] = QUOTA
    trip.meta["annotators_required"] = 1
    trip.meta["lane_annotators_required"] = {"dev": 1, "test": 1}
    trip.meta["pilot"] = "small UK/India pilot, 2026-11-16: model-drafted lane labels, every one reviewed by the owner"
    trip.save()
    picker = Picker(paths, trip)
    labels = LabelStore(paths.labels_csv(trip.id))
    picked = {}
    for rel, d in drafts[region].items():
        cand = re.sub(r"[^A-Za-z0-9]+", "_", rel.rsplit(".", 1)[0]).strip("_")
        if cand not in picker.by_id:
            say(f"  not in the index: {rel}")
            continue
        res = picker.pick(labels, cand, d["group"], OWNER)
        row = res["row"]
        picked[row["image_id"]] = (rel, d, row)
        say(f"  {'kept   ' if res['existing'] else 'picked '} {row['split']:4s} {d['group']:8s} {row['image_id']}")
    seed_lane_rows(paths, trip.id)
    app = LaneApp(paths, annotator=OWNER, set_ids=[trip.id])
    from reasoning_drive.labeling.lanes import LaneAnnotationStore, lane_annotations_csv
    anns = LaneAnnotationStore(lane_annotations_csv(paths, trip.id))
    for iid, (rel, d, row) in picked.items():
        old = anns.get(iid, OWNER)
        if old and not (REDO and old.get("status") == "draft"):
            say(f"  already has a label, left as it is: {iid}")
            continue
        f = dict(d["fields"])
        pre = lane_prefill(table, schema, region, f)
        for a in LANE_ACTIONS:
            f[f"act_{a}"] = pre["actions"].get(a, "")
        f.update(d.get("override") or {})
        f["accepted_rule_ids"] = ";".join(pre["rule_ids"])
        r = app.save(iid, f, "draft", comment="")
        say(f"  draft saved  {iid}  ({r['status']})" + (f"  warnings: {r['warnings']}" if r.get("warnings") else ""))
        if iid not in have_prov and not any(x["image_id"] == iid for x in new_prov):
            new_prov.append({"region": region, "set_id": trip.id, "image_id": iid, "split": row["split"], "pick_group": d["group"],
                             "labeled_by": "model", "first_saved_utc": now, "status_before": "", "status_after": "draft",
                             "uncertain_reason": d.get("note", ""), "spot_check": "", "spot_check_result": "",
                             "owner_review": "pending (every pilot image)", "owner_changed_fields": "", "lane_status_now": r["status"],
                             "image": str(paths.data / row["source_path"])})

if new_prov:
    cols = list(prov_rows[0].keys()) if prov_rows else list(new_prov[0].keys())
    with open(prov_file, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(prov_rows + new_prov)
say(f"Provenance: {len(new_prov)} rows added to {prov_file}")
say("Done. Open the labeling window (scripts/label_all.bat) and switch to UK / India to review the drafts.")
