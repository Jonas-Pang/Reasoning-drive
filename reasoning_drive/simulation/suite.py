"""One decision point per scenario, answered for the United States and for China, then driven with fixed intents.

Cases (each is skipped when the current map does not have it):
  arrow_left     left-turn arrow in my lane        intents: go straight, turn left, turn right
  arrow_right    right-turn arrow in my lane       intents: go straight, turn left, turn right
  yellow_double  double solid yellow centre line   intent: cross it to the left (overtake)
  yellow_solid   single solid yellow line on the left (left edge line in the US)   intent: cross it
  white_dashed   broken white line between two lanes going my way                  intent: change lane
  white_solid    solid white line between two lanes going my way (Town04)          intent: change lane
  roundabout     broken white line between the two circulating lanes (Town03)      intent: move out to exit

At each decision point the simulation waits while the same picture (cyan box around the target) is sent four
times: US Test A, US Test B, CN Test A, CN Test B. The model is never told what the car wants to do; it only says
what the marking allows. The car's intent comes from the route (here set on purpose) and is checked against the
answer: allowed -> the car does it; prohibited -> it does not (at an arrow it takes a movement the answer allows).
The car is put back to the same spot for every intent, so one answer serves all intents of a case.

Ground truth: the marking from the map (OpenDRIVE arrows and lane marks), the expected actions from the project's
rule table (regulations/<CODE>/action_rules.json) for each region. The car follows the US Test B answer (the maps are US
roads); where the US and China answers or rules differ, it also drives once with the China Test B answer.

    python -m reasoning_drive.simulation.suite --record [--mock] [--cases arrow_left,roundabout]
"""
from __future__ import annotations

import argparse
import json
import math
import queue
import random
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import carla
import cv2
import numpy as np

from ..imageio import imread, imwrite
from .loop import CAM_X, CAM_Z, FOV, H, W, LiveView, boxed_jpeg, project_marking  # noqa: E402
from .scenarios import (ACTIONS, Driver, ScenarioReasoner, arrow_box, bbox, build_plan,  # noqa: E402
                             junction_moves, movement_of, project, yaw_delta)

SHORT = {"cross_line": "cross", "go_straight": "straight", "turn_left": "left", "turn_right": "right",
         "u_turn": "U-turn", "enter_center_lane_to_wait": "enter centre lane"}
RELEVANT = {"arrow": ["go_straight", "turn_left", "turn_right", "u_turn"], "line": ["cross_line"]}
INTENTS = ["go_straight", "turn_left", "turn_right"]
ASKS = [("US", "B"), ("US", "A"), ("CN", "B"), ("CN", "A")]
CASES = {
    "arrow_left": {"kind": "arrow", "arrow_type": "left", "title": "left-turn arrow"},
    "arrow_right": {"kind": "arrow", "arrow_type": "right", "title": "right-turn arrow"},
    "yellow_double": {"kind": "line", "marking": "yellow_double_solid", "side": "left", "neighbour": "opposite",
                      "title": "double solid yellow centre line"},
    "yellow_solid": {"kind": "line", "marking": "yellow_solid", "side": "left", "neighbour": "none",
                     "title": "single solid yellow line on the left"},
    "white_dashed": {"kind": "line", "marking": "white_dashed", "side": None, "neighbour": "same",
                     "title": "broken white lane line"},
    "white_solid": {"kind": "line", "marking": "white_solid", "side": None, "neighbour": "same",
                    "title": "solid white lane line", "min_run": 20, "pick": "longest", "quick": True},
    "roundabout": {"kind": "line", "marking": "white_dashed", "side": "right", "neighbour": "same", "roundabout": True,
                   "title": "roundabout: line between the circulating lanes"},
}
ROUNDABOUT = {"Town03": ((0.0, 0.0), 18.8, 21.0)}  # centre and radius band of the inner circulating lane (m)


# ---------------------------------------------------------------- map helpers

def _poly(recs, x, key):
    best = None
    for r in recs:
        if float(r.get(key, 0)) <= x + 1e-6:
            best = r
    if best is None:
        return 0.0
    d = x - float(best.get(key, 0))
    a, b, c, e = (float(best.get(k, 0)) for k in ("a", "b", "c", "d"))
    return a + b * d + c * d * d + e * d * d * d


def lane_from_t(road, s, t):
    """Lane id that contains lateral position t (from the reference line, as OpenDRIVE objects give it)."""
    off = _poly(road.findall("lanes/laneOffset"), s, "s")
    secs = road.findall("lanes/laneSection")
    sec = [x for x in secs if float(x.get("s")) <= s + 1e-6][-1]
    ds = s - float(sec.get("s"))
    tt = t - off
    side = sec.find("left" if tt > 0 else "right")
    if side is None:
        return None
    acc = 0.0
    for ln in sorted(side.findall("lane"), key=lambda e: abs(int(e.get("id")))):
        w = _poly(ln.findall("width"), ds, "sOffset")
        if acc <= abs(tt) < acc + w:
            return int(ln.get("id"))
        acc += w
    return None


def map_arrows(cmap, root):
    out = []
    for road in root.iter("road"):
        if road.get("junction") not in (None, "-1"):
            continue
        for o in road.iter("object"):
            name = o.get("name") or ""
            if not name.startswith("Stencil_Arrow"):
                continue
            s, t = float(o.get("s")), float(o.get("t"))
            lid = lane_from_t(road, s, t)
            if lid is None:
                continue
            try:
                wp = cmap.get_waypoint_xodr(int(road.get("id")), lid, s)
            except RuntimeError:
                wp = None
            if wp is None or wp.lane_type != carla.LaneType.Driving:
                continue
            out.append({"road": int(road.get("id")), "lane": lid, "s": s, "t": t, "name": name, "wp": wp,
                        "arrow_type": "right" if name.endswith("R") else "left"})
    return out


def marking(w, side):
    return w.left_lane_marking if side == "left" else w.right_lane_marking


def neighbour(w, side):
    return w.get_left_lane() if side == "left" else w.get_right_lane()


def neighbour_rel(w, nb):
    if nb is None or nb.lane_type not in (carla.LaneType.Driving, carla.LaneType.Bidirectional):
        return "none"
    return "same" if (nb.lane_id > 0) == (w.lane_id > 0) and nb.road_id == w.road_id else "opposite"


def in_band(loc, band):
    (cx, cy), r0, r1 = band
    return r0 <= math.hypot(loc.x - cx, loc.y - cy) <= r1


def run_length(w, side, mt, band=None, limit=40.0, step=2.0):
    """Metres ahead over which the lane keeps the same marking on `side`, stays straight and out of junctions
    (in a roundabout: stays in the ring instead)."""
    cur, d, yaw0 = w, 0.0, w.transform.rotation.yaw
    while d < limit:
        n = cur.next(step)
        if not n:
            break
        cur = n[0]
        if band:
            if not in_band(cur.transform.location, band):
                break
        else:
            if cur.is_junction or abs(yaw_delta(yaw0, cur.transform.rotation.yaw)) > 8:
                break
            if project_marking(marking(cur, side)) != mt:
                break
        d += step
    return d


def find_line_cases(cmap, case, map_name, wps):
    band = ROUNDABOUT.get(map_name) if case.get("roundabout") else None
    if case.get("roundabout") and not band:
        return []
    sides = [case["side"]] if case["side"] else ["left", "right"]
    out = []
    for w in wps:
        if w.lane_type != carla.LaneType.Driving:
            continue
        if band:
            if not in_band(w.transform.location, band):
                continue
        elif w.is_junction:
            continue
        for side in sides:
            m = project_marking(marking(w, side))
            if m != case["marking"] and not (band and m == "none_visible"):
                continue
            if neighbour_rel(w, neighbour(w, side)) != case["neighbour"]:
                continue
            run = run_length(w, side, case["marking"], band)
            if run >= case.get("min_run", 30 if band else 40):
                out.append({"wp": w, "side": side, "run": run, "carla_mark": m})
    out.sort(key=lambda c: (c["wp"].road_id, c["wp"].lane_id, round(c["wp"].s)))
    return out


def line_points(wp, side, d0=6, d1=18):
    pts = []
    for d in range(d0, d1 + 1):
        n = wp.next(float(d))
        if not n:
            break
        w = n[0]
        rv, loc, half = w.transform.get_right_vector(), w.transform.location, w.lane_width / 2.0
        k = -half if side == "left" else half
        pts.append((loc.x + rv.x * k, loc.y + rv.y * k, loc.z + 0.02))
    return pts


def lane_path(w, length=60.0, step=2.0, same=True):
    pts, cur = [], w
    for _ in range(int(length / step)):
        n = cur.next(step) if same else cur.previous(step)
        if not n:
            break
        cur = n[0]
        pts.append(cur.transform.location)
    return pts


def nearest(p, pts):
    return min((p.distance(q) for q in pts), default=1e9)


# ---------------------------------------------------------------- truth

def truth(rs, mt, at="", ds=""):
    sug = rs.prefill(rs.table, rs.region, mt, at, ds, "full") or {}
    acts = sug.get("actions") or {}
    return ({a: (acts.get(a) or ("undecided" if a in acts else "not_applicable")) for a in ACTIONS},
            sug.get("rule_ids", []))


# ---------------------------------------------------------------- live view

class Counter:
    def __init__(self, writer):
        self.w, self.count = writer, 0

    def write(self, frame):
        self.w.write(frame)
        self.count += 1

    def release(self):
        self.w.release()


class SuiteView(LiveView):
    def set_answers(self, title, res, tgt, elapsed):
        rel = RELEVANT[tgt["kind"]]
        P = [("title", f"{title}  ({elapsed:.1f} s)")]
        for reg, t in ASKS:
            r = res.get((reg, t))
            head = f"{reg} Test {t} ({'image + rules' if t == 'B' else 'image only'})"
            if r is None:
                P.append(("head", head + "  ... waiting"))
                continue
            a = r.get("answer") or {}
            if not a:
                P.append(("head", head + "  error"))
                P.append(("text", (r.get("error") or "no answer")[:160]))
                continue
            tr = tgt["truth"][reg]
            m, acts = a.get("marking") or {}, a.get("actions") or {}
            mt = (m.get("marking_type") or "?") + (f" ({m['arrow_type']})" if m.get("arrow_type") else "")
            wrong = [x for x in rel if tr[x] in ("allowed", "prohibited") and acts.get(x) != tr[x]]
            P.append(("head", f"{head}  {r.get('latency_s', 0):.1f} s"))
            P.append(("bad" if wrong else "ok", "-> " + mt + ": " + ", ".join(f"{SHORT[x]} {acts.get(x)}" for x in rel)))
            if wrong:
                P.append(("bad", "   truth: " + ", ".join(f"{SHORT[x]} {tr[x]}" for x in wrong)))
        for reg in ("US", "CN"):
            a = ((res.get((reg, "B")) or {}).get("answer")) or {}
            if a:
                P.append(("head", f"{reg} Test B reasoning"))
                if reg == "US":
                    P.append(("text", f"look: {a.get('description', '')}"))
                P.append(("text", f"rule: {a.get('rule_reasoning', '')}"))
                P.append(("text", f"cited: {a.get('cited_rule_id')}   check: {a.get('self_check', '')}"))
        self.panel = P

    def snapshot(self, path):
        self.pg.image.save(self.screen, str(path))


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--cases", default=",".join(CASES))
    ap.add_argument("--pick", default="", help="candidate index per case, e.g. white_dashed=3,yellow_double=1")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=2000)
    ap.add_argument("--prompt", default="")
    ap.add_argument("--no-summary", action="store_true")
    ap.add_argument("--weather", default="ClearNoon")
    ap.add_argument("--seed", type=int, default=6216)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--record", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo)
    rs = {reg: ScenarioReasoner(repo, reg, args.mock, args.seed, args.prompt or None, not args.no_summary)
          for reg in ("US", "CN")}
    picks = {k: int(v) for k, v in (p.split("=") for p in args.pick.split(",") if "=" in p)}

    client = carla.Client(args.host, args.port)
    client.set_timeout(120.0)
    world = client.get_world()
    cmap = world.get_map()
    map_name = cmap.name.split("/")[-1].replace("_Opt", "")
    print(f"server map: {cmap.name.split('/')[-1]}", flush=True)
    world.set_weather(getattr(carla.WeatherParameters, args.weather))
    root = ET.fromstring(cmap.to_opendrive())

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(__file__).resolve().parent / "scenario_runs" / f"{stamp}_suite_{map_name}{'_mock' if args.mock else ''}"
    for sub in ("frames", "decisions"):
        (out / sub).mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------- find every case on this map
    plan_cases = []
    arrows = map_arrows(cmap, root)
    print(f"{len(arrows)} arrows: " + ", ".join(f"road {a['road']} lane {a['lane']} {a['arrow_type']}" for a in arrows), flush=True)
    by_road = {}
    for a in arrows:
        by_road.setdefault(a["road"], {})[a["arrow_type"]] = a
    both = [r for r, d in by_road.items() if len(d) == 2]
    wps = cmap.generate_waypoints(3.0)
    for name in [c.strip() for c in args.cases.split(",") if c.strip()]:
        case = dict(CASES[name], name=name)
        if case["kind"] == "arrow":
            pool_ = [by_road[r][case["arrow_type"]] for r in both] or [a for a in arrows if a["arrow_type"] == case["arrow_type"]]
            if not pool_:
                print(f"{name}: not on this map", flush=True)
                continue
            case["target"] = pool_[min(picks.get(name, 0), len(pool_) - 1)]
            print(f"{name}: road {case['target']['road']} lane {case['target']['lane']} s {case['target']['s']:.1f}", flush=True)
        else:
            cands = find_line_cases(cmap, case, map_name, wps)
            if not cands:
                print(f"{name}: not on this map", flush=True)
                continue
            if case.get("pick") == "longest":
                best = max(range(len(cands)), key=lambda j: cands[j]["run"])
                i = picks.get(name, best)
            else:
                i = picks.get(name, random.Random(f"{args.seed}:{name}").randrange(len(cands)))
            case["target"] = cands[min(i, len(cands) - 1)]
            w = case["target"]["wp"]
            print(f"{name}: {len(cands)} candidates, using #{i}: road {w.road_id} lane {w.lane_id} s {w.s:.0f} "
                  f"{case['target']['side']} side, CARLA mark {case['target']['carla_mark']}", flush=True)
        plan_cases.append(case)
    if not plan_cases:
        raise SystemExit("none of the cases is on this map")

    original = world.get_settings()
    st = world.get_settings()
    st.synchronous_mode, st.fixed_delta_seconds = True, 0.05
    world.apply_settings(st)

    meta = {"map": map_name, "weather": args.weather, "prompt": rs["US"].cfg["prompt"]["dir"],
            "model": rs["US"].cfg["api"]["model"], "reasoning_effort": rs["US"].cfg["api"].get("reasoning_effort"),
            "reasoning_summary": rs["US"].cfg["api"].get("reasoning_summary"), "asks": ASKS, "seed": args.seed,
            "started": stamp, "mock": args.mock}
    answers, decisions, markers = [], [], []
    camera = ego = view = driver = None
    pool = ThreadPoolExecutor(max_workers=4)
    images = queue.Queue()

    def frames():
        return view.writer.count if (view is not None and view.writer is not None) else 0

    def tick(drive=True):
        if drive and driver is not None:
            driver.step()
        frame = world.tick()
        img = images.get(timeout=10.0)
        while img.frame < frame:
            img = images.get(timeout=10.0)
        bgr = np.ascontiguousarray(np.frombuffer(img.raw_data, dtype=np.uint8).reshape((H, W, 4))[:, :, :3])
        if view is not None:
            view.show(bgr, ego)
        return img, bgr

    def teleport(tf, vel=None):
        ego.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0))
        ego.set_target_velocity(carla.Vector3D(0, 0, 0))
        ego.set_transform(carla.Transform(carla.Location(tf.location.x, tf.location.y, tf.location.z + 0.15), tf.rotation))
        driver.set_plan([])
        for _ in range(6):
            tick(drive=False)
        if vel is not None:
            ego.set_target_velocity(vel)

    try:
        lib = world.get_blueprint_library()
        for sp in cmap.get_spawn_points():
            ego = world.try_spawn_actor(lib.find("vehicle.tesla.model3"), sp)
            if ego is not None:
                break
        driver = Driver(ego)
        cam_bp = lib.find("sensor.camera.rgb")
        for k, v in (("image_size_x", W), ("image_size_y", H), ("fov", FOV)):
            cam_bp.set_attribute(k, str(v))
        camera = world.spawn_actor(cam_bp, carla.Transform(carla.Location(x=CAM_X, z=CAM_Z)), attach_to=ego)
        camera.listen(images.put)
        view = SuiteView(world, args.mock, "B", (out / "live_view.mp4") if args.record else None)
        if view.writer is not None:
            view.writer = Counter(view.writer)

        for ci, case in enumerate(plan_cases, 1):
            if view.quit:
                break
            name, tg0 = case["name"], case["target"]
            mk = {"case": name, "start": frames()}
            view.boxes, view.box_colours, view.lines = {}, {}, []
            view.panel = [("title", f"Case {ci}/{len(plan_cases)}: {case['title']}"),
                          ("text", "The car drives to the decision point; the model is then asked once per region and test.")]
            view.status = f"case {ci}: {case['title']} - driving"

            # ---------------------------------------------------- drive to the decision point
            if case["kind"] == "arrow":
                prev = tg0["wp"].previous(35.0)
                start = prev[0] if prev else tg0["wp"]
                teleport(start.transform)
                driver.set_plan(build_plan(start))
            else:
                fv0 = tg0["wp"].transform.get_forward_vector()
                # short solid segments: start rolling at 6 m/s on the segment and ask after 0.5 s
                teleport(tg0["wp"].transform, carla.Vector3D(fv0.x * 6, fv0.y * 6, 0) if case.get("quick") else None)
                driver.set_plan(build_plan(tg0["wp"], 80.0))
            ready, img, bgr, wp = False, None, None, None
            for k in range(500):
                img, bgr = tick()
                if view.quit:
                    break
                loc = ego.get_location()
                wp = cmap.get_waypoint(loc, project_to_road=True, lane_type=carla.LaneType.Driving)
                if case["kind"] == "arrow":
                    a = tg0["wp"].transform.location
                    fv = ego.get_transform().get_forward_vector()
                    dx, dy = a.x - loc.x, a.y - loc.y
                    ahead, lateral = dx * fv.x + dy * fv.y, abs(-dx * fv.y + dy * fv.x)
                    if ahead < 8:
                        break
                    if ahead <= 14 and lateral < 2.0:
                        ready = True
                        break
                elif k >= (10 if case.get("quick") else 40):
                    m = project_marking(marking(wp, tg0["side"]))
                    if m == case["marking"] or (case.get("roundabout") and m == "none_visible"):
                        ready = True
                        break
                    if k > 120:
                        break
            if not ready:
                print(f"{name}: decision point not reached, skipped", flush=True)
                continue

            # ---------------------------------------------------- target, truth for both regions, box
            tgt = {"kind": case["kind"], "case": name, "title": case["title"], "truth": {}, "rule_ids": {}}
            if case["kind"] == "arrow":
                at = tg0["arrow_type"]
                tgt.update(marking_type="arrow", arrow_type=at, position="in_ego_lane",
                           box=arrow_box(tg0["wp"], img.transform), map_moves=sorted(junction_moves(wp)))
                for reg in ("US", "CN"):
                    tgt["truth"][reg], tgt["rule_ids"][reg] = truth(rs[reg], "arrow", at)
            else:
                side = tg0["side"]
                mt = case["marking"]
                tgt.update(marking_type=mt, position=side, side=side, carla_mark=project_marking(marking(wp, side)),
                           box=bbox(project(line_points(wp, side), img.transform)))
                for reg in ("US", "CN"):
                    tgt["truth"][reg], tgt["rule_ids"][reg] = truth(rs[reg], mt)
            if not tgt["box"]:
                print(f"{name}: target not in the picture, skipped", flush=True)
                continue
            imwrite(str(out / "frames" / f"{name}.png"), bgr)
            cap_tf, cap_vel, cap_wp = ego.get_transform(), ego.get_velocity(), wp

            # ---------------------------------------------------- ask: 2 regions x 2 tests, the simulation waits
            mk["ask"] = frames()
            jpeg = boxed_jpeg(bgr, tgt["box"], rs["US"].cfg["prompt"])
            gt_for = {reg: {"marking_type": tgt["marking_type"], "arrow_type": tgt.get("arrow_type", ""), "position": tgt["position"]}
                      for reg in ("US", "CN")}
            jobs = {(reg, t): pool.submit(rs[reg].ask, jpeg, t, gt_for[reg], f"{name}:{reg}") for reg, t in ASKS}
            view.boxes, view.box_colours = {"t": tgt["box"]}, {}
            title = f"Case {ci}: {case['title']}"
            t0 = time.time()
            while not view.quit:
                partial = {k: (f.result() if f.done() else None) for k, f in jobs.items()}
                view.set_answers(title, partial, tgt, time.time() - t0)
                view.status = f"case {ci}: asking US/CN x Test A/B  {time.time() - t0:4.1f} s"
                view.show(bgr, None, throttle=False)
                if all(f.done() for f in jobs.values()):
                    break
                time.sleep(0.1)
            res = {k: f.result() for k, f in jobs.items()}
            view.set_answers(title, res, tgt, max(r.get("latency_s") or 0 for r in res.values()))
            view.status = f"case {ci}: answers in"
            view.show(bgr, None, throttle=False)
            view.snapshot(out / "decisions" / f"{name}.png")
            mk["answered"] = frames()
            for (reg, t), rec in res.items():
                answers.append(dict(rec, case=name, region=reg, kind=tgt["kind"], box=tgt["box"],
                                    truth={"marking_type": tgt["marking_type"], "arrow_type": tgt.get("arrow_type"),
                                           "truth": tgt["truth"][reg], "rule_ids": tgt["rule_ids"][reg]}))
            print(f"[{name}] " + "  ".join(
                f"{reg}-{t}:" + ",".join(f"{SHORT[x]}={((res[(reg, t)].get('answer') or {}).get('actions') or {}).get(x, 'err')}"
                                         for x in RELEVANT[tgt['kind']]) for reg, t in ASKS), flush=True)

            def says(reg, action):
                a = (res.get((reg, "B")) or {}).get("answer") or {}
                return (a.get("actions") or {}).get(action, "error")

            # ---------------------------------------------------- trials: fixed intents, back to the same spot each time
            if case["kind"] == "arrow":
                trials = [(m, "US") for m in INTENTS]
            else:
                trials = [("cross_line", "US")]
                if says("US", "cross_line") != says("CN", "cross_line") or tgt["truth"]["US"]["cross_line"] != tgt["truth"]["CN"]["cross_line"]:
                    trials.append(("cross_line", "CN"))
            dec = {"case": name, "title": case["title"], "map": map_name, "road_id": cap_wp.road_id, "lane_id": cap_wp.lane_id,
                   "s": round(cap_wp.s, 1), "target": {k: v for k, v in tgt.items() if k != "box"}, "box": tgt["box"], "trials": []}
            for ti, (intent, reg) in enumerate(trials, 1):
                if view.quit:
                    break
                if ti > 1:
                    teleport(cap_tf, cap_vel)
                tr = {"intent": intent, "policy": f"{reg}-B", "system_says": says(reg, intent),
                      "truth_US": tgt["truth"]["US"][intent], "truth_CN": tgt["truth"]["CN"][intent], "frame_start": frames()}
                yaw0 = ego.get_transform().rotation.yaw
                wp0 = cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Driving)
                if case["kind"] == "arrow":
                    if tr["system_says"] == "allowed":
                        choice = intent
                    else:
                        choice = next((m for m in ("go_straight", "turn_right", "turn_left") if says(reg, m) == "allowed"), None)
                    tr["action"] = choice
                    driver.set_plan(build_plan(wp0, 90.0, choice=choice) if choice else [])
                    view.status = (f"wants {SHORT[intent]}: {reg}-B says {tr['system_says']} -> "
                                   + (f"goes {SHORT[choice]}" if choice == intent else
                                      (f"refuses, goes {SHORT[choice]}" if choice else "refuses, stops")))
                    view.box_colours = {"t": (0, 200, 0) if tr["system_says"] == "allowed" else (230, 40, 40)}
                    view.lines = [f"trial {ti}/{len(trials)}: intent from the route = {SHORT[intent]} (the model is not told)",
                                  f"truth: US {tr['truth_US']}, China {tr['truth_CN']}"]
                    in_j, moved = False, None
                    for _ in range(300):
                        tick()
                        w2 = cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Any)
                        if w2 is None:
                            continue
                        if w2.is_junction:
                            in_j = True
                        elif in_j:
                            for _ in range(20):
                                tick()
                            moved = movement_of(yaw_delta(yaw0, ego.get_transform().rotation.yaw))
                            break
                    tr["observed"] = moved
                    print(f"    wants {intent}: {reg}-B {tr['system_says']} -> {choice}; car went {moved}", flush=True)
                else:
                    side = tg0["side"]
                    nb = neighbour(wp0, side)
                    rel = neighbour_rel(wp0, nb)
                    own = lane_path(wp0)
                    other = lane_path(nb, same=(rel == "same")) if rel != "none" else []
                    go = tr["system_says"] == "allowed"
                    tr["action"] = f"change to the {side} lane" if go and other else "stay in lane"
                    driver.set_plan(build_plan(wp0, 70.0, shift=side) if go and other else build_plan(wp0, 70.0))
                    what = {"roundabout": "move to the outer lane to exit"}.get(name, f"cross the {side} line")
                    view.status = f"wants to {what}: {reg}-B says {tr['system_says']} -> {tr['action']}"
                    view.box_colours = {"t": (0, 200, 0) if go else (230, 40, 40)}
                    view.lines = [f"trial {ti}/{len(trials)}: intent = {what} (the model is not told)",
                                  f"truth: US {tr['truth_US']}, China {tr['truth_CN']}"]
                    for _ in range(130):
                        tick()
                    p = ego.get_location()
                    tr["observed"] = ("in the neighbour lane" if other and nearest(p, other) < nearest(p, own)
                                      else "in its own lane")
                    print(f"    wants to cross {side}: {reg}-B {tr['system_says']} -> {tr['action']}; car is {tr['observed']}", flush=True)
                tr["frame_end"] = frames()
                dec["trials"].append(tr)
            mk["end"] = frames()
            markers.append(mk)
            decisions.append(dec)
    finally:
        try:
            with open(out / "answers.jsonl", "w", encoding="utf-8") as f:
                for r in answers:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
            with open(out / "decisions.jsonl", "w", encoding="utf-8") as f:
                for d in decisions:
                    f.write(json.dumps(d, ensure_ascii=False) + "\n")
            (out / "markers.json").write_text(json.dumps(markers, indent=1), encoding="utf-8")
            s = summarize(answers, decisions, meta)
            (out / "summary.json").write_text(json.dumps(s, indent=2), encoding="utf-8")
            print(json.dumps(s["per_ask"], indent=1), flush=True)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("could not write results:", e, flush=True)
        pool.shutdown(wait=False)
        client.set_timeout(10.0)
        try:
            world.apply_settings(original)
            if camera is not None:
                camera.stop()
            for a in (camera, ego):
                if a is not None:
                    a.destroy()
        except RuntimeError as e:
            print("cleanup skipped:", e, flush=True)
        if view is not None:
            if view.writer is not None:
                view.writer.release()
                print("video:", out / "live_view.mp4", flush=True)
            view.pg.quit()
        print("results:", out, flush=True)
        print("finished", flush=True)


def summarize(answers, decisions, meta):
    per = {}
    for reg, t in ASKS:
        rs = [a for a in answers if a["region"] == reg and a["test"] == t]
        d = {"requests": len(rs), "answered": sum(1 for a in rs if a["answer"]),
             "cost_usd": round(sum(a.get("cost", 0) for a in rs), 4), "marking_correct": 0, "actions_checked": 0,
             "actions_correct": 0, "unsafe": 0, "over_cautious": 0, "wrong": []}
        for a in rs:
            ans = a["answer"] or {}
            m = ans.get("marking") or {}
            d["marking_correct"] += (m.get("marking_type") == a["truth"]["marking_type"] and
                                     (a["kind"] != "arrow" or m.get("arrow_type") == a["truth"].get("arrow_type")))
            for x in RELEVANT[a["kind"]]:
                g, w = a["truth"]["truth"][x], (ans.get("actions") or {}).get(x)
                if g not in ("allowed", "prohibited"):
                    continue
                d["actions_checked"] += 1
                d["actions_correct"] += g == w
                d["unsafe"] += g == "prohibited" and w == "allowed"
                d["over_cautious"] += g == "allowed" and w != "allowed"
                if g != w:
                    d["wrong"].append(f"{a['case']}:{x} said {w}, truth {g}")
        per[f"{reg}-{t}"] = d
    return {"meta": meta, "per_ask": per, "cost_usd": round(sum(a.get("cost", 0) for a in answers), 4)}


if __name__ == "__main__":
    main()
