"""Written by Claude: fill the empty lane-change cells next to a special lane (bus, HOV, tidal) with the convention of
2026-11-15 (see prompts/lane_v3/README.md): changing into the special lane is prohibited; leaving it, when my own lane is
the special lane, follows the line type. Only empty change_left / change_right cells whose side has the role
special_lane_line are filled; nothing else changes. Backup in results/claude_logs/backup_special_<time>/.
Stop the labeling tools first.   python scripts/claude_fill_special.py [--dry-run]"""
import csv, io, shutil, sys
from datetime import datetime
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo))
from reasoning_drive.labeling.lanes import lane_prefill, load_lane_rules, load_lane_schema
table, schema = load_lane_rules(repo), load_lane_schema(repo)
dry = "--dry-run" in sys.argv
logp = repo / "results" / "claude_logs" / "fill_special.log"
logp.parent.mkdir(parents=True, exist_ok=True)
log = open(logp, "a", encoding="utf-8")
def say(m=""):
    print(m, flush=True); log.write(m + "\n"); log.flush()
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = repo / "results" / "claude_logs" / f"backup_special_{stamp}"
say(f"=== {stamp} {'(dry run)' if dry else ''}")
total = 0
for f in sorted(p for p in (repo / "datasets").glob("*/*/*.csv") if not p.name.startswith("._")
                and (p.name.endswith(".lanes.csv") or p.name.endswith(".lane_annotations.csv"))):
    raw = f.read_bytes(); text = raw.decode("utf-8-sig"); nl = "\r\n" if "\r\n" in text else "\n"
    rows = list(csv.DictReader(io.StringIO(text, newline="")))
    if not rows or "act_change_left" not in rows[0]:
        continue
    region = f.parent.parent.name
    cols, n, filled = list(rows[0].keys()), 0, []
    for r in rows:
        sug = None
        for side in ("left", "right"):
            if r.get(f"act_change_{side}", "") == "" and r.get(f"{side}_role") == "special_lane_line":
                sug = sug or lane_prefill(table, schema, r.get("region") or region, r)["actions"]
                if sug.get(f"change_{side}"):
                    r[f"act_change_{side}"] = sug[f"change_{side}"]; n += 1
                    filled.append(f"{r.get('image_id')}:{side}={sug[f'change_{side}']}")
    total += n
    say(f"{f.relative_to(repo)}: {n} cells filled" + (f"  ({'; '.join(filled)})" if filled else ""))
    if n and not dry:
        dst = backup / f.relative_to(repo); dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(f, dst)
        out = io.StringIO(newline=""); w = csv.DictWriter(out, fieldnames=cols, lineterminator=nl)
        w.writeheader(); w.writerows(rows)
        f.write_bytes((b"\xef\xbb\xbf" if raw.startswith(b"\xef\xbb\xbf") else b"") + out.getvalue().encode("utf-8"))
say(f"Total filled: {total}" + ("" if dry or not total else f"   (backup: {backup.relative_to(repo)})"))
