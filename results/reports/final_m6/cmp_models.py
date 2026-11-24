"""v3 vs v4 vs v4c (gemma4:31b) on the test images, current labels; for each prompt only finished runs without errors,
merged per image (latest wins). usage: python cmp_v4c.py <repo> [tests]"""
import collections, csv, json, os, sys
from pathlib import Path
repo = Path(sys.argv[1]).resolve(); tests = sys.argv[2] if len(sys.argv) > 2 else "A"
COMBOS = [("gemma4:31b", "lane_v3"), ("gemma4:31b", "lane_v4"), ("gemma4:31b", "lane_v4c"), ("gemma4:12b", "lane_v3"), ("gemma4:12b", "lane_v4c"), ("gemma4:e4b", "lane_v3"), ("gemma4:e4b", "lane_v4c")]
sys.path.insert(0, str(repo)); os.chdir(repo)
from reasoning_drive import config as C
from reasoning_drive.agent import lane as LA
from reasoning_drive.labeling import lanes as L
cfg = C.load(repo); cur = {}
for f in ["datasets/CN/mapdr/mapdr.lanes.csv", "datasets/US/bdd100k/bdd100k_val.lanes.csv", "datasets/UK/lingoqa/lingoqa.lanes.csv", "datasets/IN/idd/idd.lanes.csv"]:
    for r in csv.DictReader(open(repo / f, encoding="utf-8")):
        if r.get("lane_status") == "done": cur[r["image_id"]] = r
KEY4 = ["change_left", "change_right", "turn_left", "turn_right"]; allow = lambda v: v in ("allowed", "stop_first")
runs = collections.defaultdict(list)
for d in sorted((repo / "results" / "runs").glob("*_lane*")):
    try: man = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    except Exception: continue
    pd = (man.get("prompt_hashes") or {}).get("prompt_dir", "").split("/")[-1]
    if man.get("mock") or (man["settings"].get("model"), pd) not in COMBOS or man.get("split") != "test" or not (d / "scores.json").exists(): continue
    sc = json.loads((d / "scores.json").read_text(encoding="utf-8")).get("summary", {})
    pass  # runs with some failed requests are kept; only answered images are used
    runs[((man["settings"].get("model"), pd), man["test"])].append(d.name)
res = {}
for (pd, t), rids in runs.items():
    if t not in tests: continue
    per = {}
    for rid in rids:
        for r in LA.rescore_records(cfg, [dict(r, label=dict(cur[r["image_id"]])) for r in LA.load_lane_run(cfg, rid)["records"] if r["image_id"] in cur and r.get("answer")]):
            per[r["image_id"]] = r
    res[(pd, t)] = per
for t in tests:
    common = None
    for pd in COMBOS:
        if (pd, t) in res: common = set(res[(pd, t)]) if common is None else common & set(res[(pd, t)])
    if not common: continue
    print(f"=== Test {t}, {len(common)} images in common")
    for pd in COMBOS:
        if (pd, t) not in res: continue
        c = collections.Counter(); per = res[(pd, t)]
        for i in common:
            r = per[i]; a, lab, sc = r["answer"], r["label"], r.get("score") or {}
            got = a.get("actions") or {}
            dec = [x for x in KEY4 if lab.get("act_" + x) in ("allowed", "prohibited", "stop_first", "not_applicable")]
            c["key4"] += all(allow(lab.get("act_" + x)) == allow(got.get(x)) for x in dec)
            c["acts"] += bool(sc.get("output2")); c["unsafe"] += len(sc.get("unsafe") or [])
            for u in sc.get("unsafe") or []: c["U:" + (u if isinstance(u, str) else str(u.get("action", u)))] += 1
            c["lines"] += all((a.get(s + "_boundary") or {}).get("color") == lab.get(s + "_color") and (a.get(s + "_boundary") or {}).get("pattern") == lab.get(s + "_pattern") for s in L.SIDES)
            c["nd"] += sum(v == "not_determined" for v in got.values())
            for x in ("turn_left", "turn_right", "u_turn", "go_straight", "change_left", "change_right"):
                lv = lab.get("act_" + x)
                if lv in ("allowed", "prohibited", "stop_first", "not_applicable"):
                    c[x + "_n"] += 1; c[x] += got.get(x) == lv
        n = len(common)
        print(f"{pd[0][7:]:4s} {pd[1]:8s} key4 {c['key4']/n:.3f}  acts {c['acts']/n:.3f}  lines {c['lines']/n:.3f}  unsafe {c['unsafe']}  not_determined {c['nd']}  | " + "  ".join(f"{x} {c[x]/max(1,c[x+'_n']):.2f}" for x in ("change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn")))
        print("         unsafe by action:", {k[2:]: v for k, v in sorted(c.items()) if k.startswith("U:")})
