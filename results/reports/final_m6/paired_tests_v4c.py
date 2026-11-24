import collections, csv, json, os, sys, math
from pathlib import Path
repo = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(repo)); os.chdir(repo)
from reasoning_drive import config as C
from reasoning_drive.agent import lane as LA
from reasoning_drive.labeling import lanes as L
cfg = C.load(repo); cur = {}; reg = {}
for f, rg in [("datasets/CN/mapdr/mapdr.lanes.csv","CN"), ("datasets/US/bdd100k/bdd100k_val.lanes.csv","US"), ("datasets/UK/lingoqa/lingoqa.lanes.csv","UK"), ("datasets/IN/idd/idd.lanes.csv","IN")]:
    for r in csv.DictReader(open(repo / f, encoding="utf-8")):
        if r.get("lane_status") == "done": cur[r["image_id"]] = r; reg[r["image_id"]] = rg
KEY4 = ["change_left", "change_right", "turn_left", "turn_right"]; allow = lambda v: v in ("allowed", "stop_first")
want = {("gemma4:31b","lane_v4c")}
runs = collections.defaultdict(list)
for d in sorted((repo / "results" / "runs").glob("*_lane*")):
    try: man = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    except Exception: continue
    pd = (man.get("prompt_hashes") or {}).get("prompt_dir", "").split("/")[-1]
    if man.get("mock") or (man["settings"].get("model"), pd) not in want or man.get("split") != "test" or not (d / "scores.json").exists(): continue
    runs[man["test"]].append(d.name)
res = {}
for t, rids in runs.items():
    per = {}
    for rid in rids:
        for r in LA.rescore_records(cfg, [dict(r, label=dict(cur[r["image_id"]])) for r in LA.load_lane_run(cfg, rid)["records"] if r["image_id"] in cur and r.get("answer")]):
            per[r["image_id"]] = r
    res[t] = per
def k4(r):
    a, lab = r["answer"], r["label"]; got = a.get("actions") or {}
    dec = [x for x in KEY4 if lab.get("act_" + x) in ("allowed", "prohibited", "stop_first", "not_applicable")]
    return all(allow(lab.get("act_" + x)) == allow(got.get(x)) for x in dec)
def lines(r):
    a, lab = r["answer"], r["label"]
    return all((a.get(s + "_boundary") or {}).get("color") == lab.get(s + "_color") and (a.get(s + "_boundary") or {}).get("pattern") == lab.get(s + "_pattern") for s in L.SIDES)
def mcn(b, c):
    n = b + c
    if n == 0: return 1.0
    k = min(b, c); p = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return min(1.0, 2 * p)
print({t: len(v) for t, v in res.items()}, {t: runs[t] for t in runs})
for t1, t2 in [("A","B"), ("A","C")]:
    if t1 not in res or t2 not in res: continue
    com = sorted(set(res[t1]) & set(res[t2]))
    for name, f in [("key4", k4), ("lines", lines), ("acts", lambda r: bool((r.get("score") or {}).get("output2")))]:
        b = sum(f(res[t1][i]) and not f(res[t2][i]) for i in com); c = sum(not f(res[t1][i]) and f(res[t2][i]) for i in com)
        print(f"{t1} vs {t2} {name}: n={len(com)} right_only_{t1}={b} right_only_{t2}={c} p={mcn(b,c):.4f} {t1}={sum(f(res[t1][i]) for i in com)/len(com):.3f} {t2}={sum(f(res[t2][i]) for i in com)/len(com):.3f}")
    for rg in ["CN","US","UK","IN"]:
        cc = [i for i in com if reg[i]==rg]
        if not cc: continue
        b = sum(k4(res[t1][i]) and not k4(res[t2][i]) for i in cc); c = sum(not k4(res[t1][i]) and k4(res[t2][i]) for i in cc)
        print(f"   {rg} n={len(cc)} key4 {t1}={sum(k4(res[t1][i]) for i in cc)/len(cc):.3f} {t2}={sum(k4(res[t2][i]) for i in cc)/len(cc):.3f} only{t1}={b} only{t2}={c} p={mcn(b,c):.3f}")
# per region Test A summary
if "A" in res:
    for rg in ["CN","US","UK","IN"]:
        cc=[i for i in res["A"] if reg[i]==rg]
        print("A", rg, len(cc), "key4", round(sum(k4(res["A"][i]) for i in cc)/len(cc),3), "lines", round(sum(lines(res["A"][i]) for i in cc)/len(cc),3), "acts", round(sum(bool((res["A"][i].get("score") or {}).get("output2")) for i in cc)/len(cc),3), "unsafe", sum(len((res["A"][i].get("score") or {}).get("unsafe") or []) for i in cc))
