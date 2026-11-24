"""Written by Claude: correct a pre-labeling mistake. In Claude's drafts, the line between my lane and a bicycle /
non-motorized lane was given the role special_lane_line; by the schema it is edge_line ("the boundary to a shoulder,
a bicycle or non-motorized lane"). Only draft annotations by Claude whose comment says the side is a bicycle or
non-motorized lane are changed: the role becomes edge_line and that side's lane change is suggested again from the rule
table. Backup in results/claude_logs/backup_bikerole_<time>/.   python scripts/claude_fix_bike_role.py [--dry-run]"""
import csv, io, shutil, sys
from datetime import datetime
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo))
from reasoning_drive.labeling.lanes import lane_prefill, load_lane_rules, load_lane_schema
table, schema = load_lane_rules(repo), load_lane_schema(repo)
dry = "--dry-run" in sys.argv
WORDS = {"left": ("左侧为自行车", "左侧为绿色自行车", "左侧实线外为自行车", "左侧为非机动", "左侧实线外为非机动", "左侧白实线外是非机动"),
         "right": ("右侧为自行车", "右侧实线外为自行车", "右侧为非机动", "右侧实线外为非机动", "右侧实线外疑为非机动",
                   "右侧白实线外是非机动", "右侧红色非机动")}
logp = repo / "results" / "claude_logs" / "fix_bike_role.log"
log = open(logp, "a", encoding="utf-8")
def say(m=""):
    print(m, flush=True); log.write(m + "\n"); log.flush()
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = repo / "results" / "claude_logs" / f"backup_bikerole_{stamp}"
say(f"=== {stamp} {'(dry run)' if dry else ''}")
for f in sorted(p for p in (repo / "datasets").glob("*/*/*.lane_annotations.csv") if not p.name.startswith("._")):
    raw = f.read_bytes(); text = raw.decode("utf-8-sig"); nl = "\r\n" if "\r\n" in text else "\n"
    rows = list(csv.DictReader(io.StringIO(text, newline="")))
    if not rows or "comment" not in rows[0]:
        continue
    cols, done = list(rows[0].keys()), []
    for r in rows:
        if r.get("status") != "draft" or "Claude 预标" not in (r.get("comment") or ""):
            continue
        for side in ("left", "right"):
            if r.get(f"{side}_role") == "special_lane_line" and any(w in r["comment"] for w in WORDS[side]):
                r[f"{side}_role"] = "edge_line"
                new = lane_prefill(table, schema, r.get("region") or f.parent.parent.name, r)["actions"].get(f"change_{side}", "")
                done.append(f"{r['image_id']}:{side} {r.get('act_change_' + side)}->{new}")
                r[f"act_change_{side}"] = new
    say(f"{f.relative_to(repo)}: {len(done)} sides corrected" + ("".join(f"\n   {d}" for d in done)))
    if done and not dry:
        dst = backup / f.relative_to(repo); dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(f, dst)
        out = io.StringIO(newline=""); w = csv.DictWriter(out, fieldnames=cols, lineterminator=nl)
        w.writeheader(); w.writerows(rows)
        f.write_bytes((b"\xef\xbb\xbf" if raw.startswith(b"\xef\xbb\xbf") else b"") + out.getvalue().encode("utf-8"))
