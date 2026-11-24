"""Written by Claude: apply the convention "going straight without an arrow in my lane is allowed" (owner's decision,
2026-11-15; see prompts/lane_v3/README.md) to the lane labels made before it.
For every lane label and lane annotation whose lane has no movement arrow (and does not end in a merge and is not a
two-way left-turn lane) and whose act_go_straight is not_applicable: allowed, or not_determined when the markings were
only partly visible; and with a STOP word or the 停 stop-and-yield line in the lane, every allowed movement becomes
stop_first. Nothing else changes. A copy of every file is kept in results/claude_logs/backup_straight_<time>/.
Stop the labeling tools first: they keep the files in memory and would write the old values back.
Run:  python scripts/claude_migrate_straight.py          (add --dry-run to only count)"""
import csv, io, json, shutil, sys
from datetime import datetime
from pathlib import Path
repo = Path(__file__).resolve().parent.parent
schema = json.loads((repo / "configs" / "schemas" / "lane_schema.json").read_text(encoding="utf-8"))
ARROWS = set(schema["movement_arrows"])
ENDS = {"arrow:merge_left", "arrow:merge_right", "arrow:two_way_left"}
STOPS = set(schema.get("stop_tokens", ["text:stop", "line:stop_yield"]))
MOVES = ["go_straight", "turn_left", "turn_right", "u_turn"]
dry = "--dry-run" in sys.argv
logp = repo / "results" / "claude_logs" / "migrate_straight.log"
logp.parent.mkdir(parents=True, exist_ok=True)
log = open(logp, "a", encoding="utf-8")
def say(m=""):
    print(m, flush=True); log.write(m + "\n"); log.flush()
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = repo / "results" / "claude_logs" / f"backup_straight_{stamp}"
say(f"=== {stamp} {'(dry run)' if dry else ''}")
files = sorted(p for p in (repo / "datasets").glob("*/*/*.csv")
               if not p.name.startswith("._") and (p.name.endswith(".lanes.csv") or p.name.endswith(".lane_annotations.csv")))
total = 0
for f in files:
    raw = f.read_bytes()
    text = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in text else "\n"
    rows = list(csv.DictReader(io.StringIO(text, newline="")))
    if not rows or "act_go_straight" not in rows[0]:
        continue
    cols = list(rows[0].keys())
    changed, stop_rows = {}, []
    for r in rows:
        toks = [t for t in (r.get("markings") or "").split(";") if t]
        hidden = r.get("markings_evidence") in ("partial", "insufficient")
        before = {m: r.get("act_" + m, "") for m in MOVES}
        if r.get("act_go_straight") == "not_applicable" and not any(t in ARROWS or t in ENDS for t in toks):
            r["act_go_straight"] = "not_determined" if hidden else "allowed"
        if any(t in STOPS for t in toks):  # STOP word or 停 line: the allowed movements need a full stop first
            for m in MOVES:
                if r.get("act_" + m) == "allowed":
                    r["act_" + m] = "stop_first"
        diff = [m for m in MOVES if r.get("act_" + m, "") != before[m]]
        if diff:
            st = r.get("lane_status") or r.get("status") or "?"
            changed[st] = changed.get(st, 0) + 1
            stop_rows.extend([r.get("image_id", "?")] if any(r.get("act_" + m) == "stop_first" for m in diff) else [])
    n = sum(changed.values())
    total += n
    say(f"{f.relative_to(repo)}: {len(rows)} rows, {n} changed {changed if n else ''}"
        + (f"; stop_first in {len(stop_rows)}: {', '.join(stop_rows)}" if stop_rows else ""))
    if n and not dry:
        dst = backup / f.relative_to(repo)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dst)
        out = io.StringIO(newline="")
        w = csv.DictWriter(out, fieldnames=cols, lineterminator=nl)
        w.writeheader(); w.writerows(rows)
        data = out.getvalue().encode("utf-8")
        f.write_bytes((b"\xef\xbb\xbf" if raw.startswith(b"\xef\xbb\xbf") else b"") + data)
say(f"Total changed: {total}" + ("" if dry or not total else f"   (backup: {backup.relative_to(repo)})"))
