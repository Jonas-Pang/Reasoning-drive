"""Written by Claude: finish the lane labels of the China (MapDR) and US (BDD100K) sets after model-assisted labeling.
Stop the labeling tools first.   python scripts/claude_finalize.py [--dry-run]

1. Backup of both sets' lane files in results/claude_logs/backup_finalize_<time>/.
2. Removes the working prefix "Claude 预标，待审..." from the comments of lane_annotations.csv (the note text stays).
3. Marks a draft "done" when it is confident: validate_lane finds no error, unsure is 0, no evidence is insufficient,
   markings evidence is not partial, no side is a special lane line, and the comment asks for no confirmation.
   Every other draft stays a draft for the owner's review.
4. One lane annotator per image (lane_annotators_required = {"dev": 1, "test": 1}), then merge again.
5. Writes the internal record (NOT part of the dataset):
     results/claude_logs/provenance_labels.csv   who produced each lane annotation and what happened to it
     results/claude_logs/review_drafts.csv       drafts left for review, with the reason
     results/claude_logs/spot_check.csv          a seeded random 20 % of the model-produced finished labels
     results/claude_logs/spot_check.html         the same list with the images, to open in a browser
"""
import html, json, os, random, re, shutil, sys
from collections import Counter
from datetime import datetime
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo))
from reasoning_drive.labeling.core import Paths, Trip, write_csv
from reasoning_drive.labeling.lanes import (LaneAnnotationStore, LaneStore, lane_annotations_csv, lanes_csv,
                                            load_lane_schema, merge_lanes, validate_lane)

DRY = "--dry-run" in sys.argv
SEED = 20261116
SHARE = 0.20
OWNER_ONLY_BEFORE = "2026-11-15"   # annotations saved before this day are the owner's own work
PREFIX = re.compile(r"^\s*Claude\s*预标[，,]\s*待审\s*[：:；;]?\s*")
ASKS = re.compile(r"确认|不确定|疑|难辨|待定|看不清|[?？]")

logs = repo / "results" / "claude_logs"
logs.mkdir(parents=True, exist_ok=True)
log = open(logs / "finalize.log", "a", encoding="utf-8")


def say(m=""):
    print(m, flush=True)
    log.write(m + "\n")
    log.flush()


def datasets_root() -> Path:
    v = os.environ.get("DATASETS_ROOT", "")
    if not v:
        for line in (repo / ".env").read_text(encoding="utf-8").splitlines():
            k, _, val = line.partition("=")
            if k.strip() == "DATASETS_ROOT":
                v = val.strip().strip('"')
    p = Path(v)
    return p if p.is_absolute() else (repo / p).resolve()


def uncertain_reason(a: dict, schema: dict) -> str:
    errors, _ = validate_lane(a, schema)
    if errors:
        return "check: " + "; ".join(errors)[:200]
    why = []
    if a.get("unsure") == "1":
        why.append("marked unsure")
    if "insufficient" in (a.get("scene_evidence"), a.get("left_evidence"), a.get("right_evidence"),
                          a.get("markings_evidence")):
        why.append("evidence insufficient")
    if a.get("markings_evidence") == "partial":
        why.append("markings partly visible")
    if "special_lane_line" in (a.get("left_role"), a.get("right_role")):
        why.append("special lane next to my lane")
    if ASKS.search(a.get("comment") or ""):
        why.append("comment asks to confirm")
    return "; ".join(why)


root = datasets_root()
schema = load_lane_schema(repo)
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = logs / f"backup_finalize_{stamp}"
say(f"=== {stamp} {'(dry run)' if DRY else ''}  datasets root: {root}")

prov, review, finished_by_model = [], [], []
for region, ws, sid in (("CN", "mapdr_ws", "mapdr"), ("US", "bdd100k", "bdd100k_val")):
    paths = Paths.discover(repo, root / ws)
    trip = Trip(paths, sid)
    ann_f, lanes_f, meta_f = lane_annotations_csv(paths, sid), lanes_csv(paths, sid), paths.trip_json(sid)
    if not DRY:
        for f in (ann_f, lanes_f, meta_f):
            dst = backup / region / f.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst)
    anns = LaneAnnotationStore(ann_f)
    items = LaneStore(lanes_f).rows
    picks = {}
    labels_f = lanes_f.with_name(f"{sid}.labels.csv")
    if labels_f.exists():
        import csv
        with open(labels_f, encoding="utf-8-sig", newline="") as fh:
            picks = {r["image_id"]: r.get("pick_group", "") for r in csv.DictReader(fh)}
    c = Counter()
    for a in anns.all():
        by_model = a.get("saved_utc", "") >= OWNER_ONLY_BEFORE
        before = a["status"]
        new_comment = PREFIX.sub("", a.get("comment") or "")
        if new_comment != (a.get("comment") or ""):
            c["prefix removed"] += 1
        a["comment"] = new_comment
        reason = uncertain_reason(a, schema) if by_model else ""
        if by_model and before == "draft" and not reason:
            a["status"] = "done"
            c["draft -> done"] += 1
        elif by_model and before == "draft":
            c["left as draft"] += 1
        anns.put(a)
        item = items.get(a["image_id"], {})
        row = {"region": region, "set_id": sid, "image_id": a["image_id"], "split": item.get("split", ""),
               "pick_group": picks.get(a["image_id"], ""), "labeled_by": "model" if by_model else "owner",
               "first_saved_utc": a.get("saved_utc", ""), "status_before": before, "status_after": a["status"],
               "uncertain_reason": reason, "spot_check": "", "spot_check_result": "",
               "image": str(root / ws / item.get("source_path", "")) if item.get("source_path") else ""}
        prov.append(row)
        if a["status"] == "draft":
            review.append({**row, "comment": a["comment"]})
        if by_model and a["status"] == "done":
            finished_by_model.append((row, a))
    say(f"{region} {sid}: {dict(c)}")
    if DRY:
        continue
    anns.save()
    meta = json.loads(meta_f.read_text(encoding="utf-8"))
    meta["lane_annotators_required"] = {"dev": 1, "test": 1}
    meta_f.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    say(f"{region} {sid} lane status after merge: {dict(merge_lanes(paths, trip))}")

# seeded random spot-check, 20 % of the model-produced finished labels in each region
rng = random.Random(SEED)
chosen = []
for region in ("CN", "US"):
    pool = sorted((x for x in finished_by_model if x[0]["region"] == region), key=lambda x: x[0]["image_id"])
    k = max(1, round(len(pool) * SHARE)) if pool else 0
    chosen += rng.sample(pool, k)
    say(f"{region}: {len(pool)} model-produced finished labels, {k} drawn for the spot-check")
ids = {(r["region"], r["image_id"]) for r, _ in chosen}
for r in prov:
    r["spot_check"] = "yes" if (r["region"], r["image_id"]) in ids else ""


def side(a, s):
    near = f" ({a[s + '_near_line']} on my side)" if a.get(s + "_near_line") not in ("", "not_applicable") else ""
    curb = " + curb" if a.get(s + "_curb") == "yes" else ""
    return f"{a[s + '_color']} {a[s + '_pattern']}{near}{curb}, {a[s + '_role']} [{a[s + '_evidence']}]"


ACTS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"]
spot = []
for r, a in sorted(chosen, key=lambda x: (x[0]["region"], x[0]["split"], x[0]["pick_group"], x[0]["image_id"])):
    spot.append({"region": r["region"], "image_id": r["image_id"], "split": r["split"], "pick_group": r["pick_group"],
                 "left": side(a, "left"), "right": side(a, "right"),
                 "markings": f"{a['markings'] or '-'} [{a['markings_evidence']}]",
                 "actions": "; ".join(f"{x}={a['act_' + x]}" for x in ACTS), "comment": a["comment"],
                 "verdict (ok / wrong)": "", "what is wrong": "", "image": r["image"]})

if not DRY:
    pcols = ["region", "set_id", "image_id", "split", "pick_group", "labeled_by", "first_saved_utc", "status_before",
             "status_after", "uncertain_reason", "spot_check", "spot_check_result", "image"]
    write_csv(logs / "provenance_labels.csv", prov, pcols)
    write_csv(logs / "review_drafts.csv", review, pcols + ["comment"])
    write_csv(logs / "spot_check.csv", spot, list(spot[0].keys()) if spot else ["region"])
    cards = []
    for i, s in enumerate(spot, 1):
        uri = Path(s["image"]).as_uri() if s["image"] else ""
        cards.append(
            f'<div class="c"><img src="{html.escape(uri)}" loading="lazy"><div class="t"><b>{i}. {s["region"]} '
            f'{s["split"]} / {html.escape(s["pick_group"])}</b> <code>{html.escape(s["image_id"])}</code><br>'
            f'Left: {html.escape(s["left"])}<br>Right: {html.escape(s["right"])}<br>'
            f'Markings: {html.escape(s["markings"])}<br>Actions: {html.escape(s["actions"])}<br>'
            f'<i>{html.escape(s["comment"])}</i></div></div>')
    (logs / "spot_check.html").write_text(
        "<!DOCTYPE html><meta charset='utf-8'><title>Lane label spot-check</title><style>"
        "body{font:14px sans-serif;margin:16px;background:#f6f6f6}.c{display:flex;gap:12px;background:#fff;"
        "margin:0 0 12px;padding:8px;border-radius:6px}img{width:560px;flex:none}.t{line-height:1.6}</style>"
        f"<h2>Spot-check: {len(spot)} labels (seed {SEED}, {int(SHARE * 100)} % per region)</h2>"
        "<p>Write ok / wrong per row in spot_check.csv. Fix a wrong label in the labeling tool.</p>"
        + "".join(cards), encoding="utf-8")
say(f"provenance rows {len(prov)}, drafts for review {len(review)}, spot-check {len(spot)}"
    + ("" if DRY else f"   (backup: {backup.relative_to(repo)})"))
