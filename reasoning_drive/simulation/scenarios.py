"""Scenario tests of the Reasoning-drive lane reasoner in CARLA: turn arrows, two-way left-turn lanes, lane lines.

The car is placed before each target and follows the lane with a simple steering controller in synchronous mode
(the Traffic Manager crashes on Town03 in this CARLA build, and a own controller carries out every decision exactly). When the target is about 12 m
ahead, the camera frame is sent to the model with a cyan box around the target, in Test A (image only) and/or
Test B (image + rule passages). The answer of --drive-with then decides what the car does:

  arrows   the car wants to go straight, left or right at the next junction; it takes that movement only if the
           answer allows it, otherwise an allowed one (route set in the Traffic Manager), and the movement it
           really made is measured after the junction
  twltl    (Town03) the car wants to turn left soon; it asks about the two-way left-turn lane (box over the centre
           lane) and about the yellow line on its left
  lanes    the car wants to change lane; it asks about its left and right boundary lines

Ground truth: arrow type and position from the map's OpenDRIVE objects, lane types and lines from the map, and
the expected actions from the project's rule table (regulations/<CODE>/action_rules.json), the same table used for labeling.

The live window shows the camera picture, the decision and, on the right, the model's reasoning as each answer
arrives. With --record the window is saved as live_view.mp4, and a picture of it is saved at every decision.

Example (Town10HD for arrows, Town03 for twltl; the server map is not switched):
    python -m reasoning_drive.simulation.scenarios --scenario arrows --decisions 3 --record
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
from .loop import (CAM_X, CAM_Z, FOV, H, W, LiveView, Reasoner, boundary_points,  # noqa: E402
                                 boxed_jpeg, ground_truth)

ACTIONS = ["cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_center_lane_to_wait"]
RELEVANT = {"arrow": ["go_straight", "turn_left", "turn_right", "u_turn"],
            "twltl": ["enter_center_lane_to_wait", "turn_left"],
            "line": ["cross_line"]}
ROUTE = {"go_straight": "Straight", "turn_left": "Left", "turn_right": "Right"}
SHORT = {"cross_line": "cross", "go_straight": "straight", "turn_left": "left", "turn_right": "right",
         "u_turn": "U-turn", "enter_center_lane_to_wait": "enter centre lane"}


# ---------------------------------------------------------------- geometry

def project(points, cam_tf) -> list:
    w2c = np.array(cam_tf.get_inverse_matrix())
    f = W / (2.0 * math.tan(math.radians(FOV) / 2.0))
    uv = []
    for x, y, z in points:
        c = w2c @ np.array([x, y, z, 1.0])
        cx, cy, cz = c[1], -c[2], c[0]
        if cz < 1.0:
            continue
        u, v = f * cx / cz + W / 2.0, f * cy / cz + H / 2.0
        if -50 <= u < W + 50 and -50 <= v < H + 50:
            uv.append((min(max(u, 0), W - 1), min(max(v, 0), H - 1)))
    return uv


def bbox(uv, pad=(10, 8), min_wh=(40, 30)):
    if len(uv) < 2:
        return None
    us, vs = [p[0] for p in uv], [p[1] for p in uv]
    x1, x2, y1, y2 = min(us) - pad[0], max(us) + pad[0], min(vs) - pad[1], max(vs) + pad[1]
    if x2 - x1 < min_wh[0]:
        c = (x1 + x2) / 2
        x1, x2 = c - min_wh[0] / 2, c + min_wh[0] / 2
    if y2 - y1 < min_wh[1]:
        c = (y1 + y2) / 2
        y1, y2 = c - min_wh[1] / 2, c + min_wh[1] / 2
    return [int(max(0, x1)), int(max(0, y1)), int(min(W - 1, x2)), int(min(H - 1, y2))]


def offset(wp, along: float, lateral: float):
    tf = wp.transform
    fv, rv, loc = tf.get_forward_vector(), tf.get_right_vector(), tf.location
    return (loc.x + fv.x * along + rv.x * lateral, loc.y + fv.y * along + rv.y * lateral, loc.z + 0.02)


def arrow_box(arrow_wp, cam_tf):
    half_w = min(1.2, arrow_wp.lane_width * 0.35)
    pts = [offset(arrow_wp, a, l) for a in (-3.5, -1.5, 0.0, 1.5, 3.5) for l in (-half_w, half_w)]
    return bbox(project(pts, cam_tf))


def line_box(wp, side, cam_tf):
    return bbox(project(boundary_points(wp, side, 6, 18), cam_tf))


def yaw_delta(a, b):
    return (b - a + 180.0) % 360.0 - 180.0


def movement_of(dyaw):
    if abs(dyaw) < 30:
        return "go_straight"
    if abs(dyaw) > 150:
        return "u_turn"
    return "turn_right" if dyaw > 0 else "turn_left"


def junction_moves(wp, look=60.0, step=2.0):
    """Movements the map connects this lane to at the next junction (a second reference for arrows)."""
    cur, travelled = wp, 0.0
    while travelled < look:
        nxt = cur.next(step)
        if not nxt:
            return set()
        if len(nxt) > 1 or nxt[0].is_junction:
            moves = set()
            for br in nxt:
                end = br
                for _ in range(200):
                    if not end.is_junction:
                        break
                    n = end.next(step)
                    if not n:
                        break
                    end = n[0]
                moves.add(movement_of(yaw_delta(cur.transform.rotation.yaw, end.transform.rotation.yaw)))
            return moves
        cur = nxt[0]
        travelled += step
    return set()


# ---------------------------------------------------------------- targets from the map

def lane_at(cmap, road: int, s: float, t: float):
    """Driving lane that contains the point at (s, t) of `road`: the reference line point at s is found from the
    first lane on either side, the point is moved by t along the road's left normal, then snapped to a lane."""
    for lane in (-1, 1):
        try:
            w = cmap.get_waypoint_xodr(road, lane, s)
        except RuntimeError:
            w = None
        if w is None:
            continue
        r, c, half = w.transform.get_right_vector(), w.transform.location, w.lane_width / 2.0
        ref = (c.x - r.x * half, c.y - r.y * half, c.z)
        # left normal of the road direction: -right for lane -1 (driving with s), +right for lane 1 (against s)
        k = -1.0 if lane == -1 else 1.0
        p = carla.Location(ref[0] + k * r.x * t, ref[1] + k * r.y * t, ref[2])
        wp = cmap.get_waypoint(p, project_to_road=True, lane_type=carla.LaneType.Driving)
        if wp is not None and wp.transform.location.distance(p) < 2.0:
            return wp
    return None


def map_arrows(cmap) -> list:
    root = ET.fromstring(cmap.to_opendrive())
    out = []
    for road in root.iter("road"):
        if road.get("junction") not in (None, "-1"):
            continue
        for o in road.iter("object"):
            name = o.get("name") or ""
            if "Arrow" not in name:
                continue
            wp = lane_at(cmap, int(road.get("id")), float(o.get("s")), float(o.get("t")))
            if wp is not None:
                out.append({"road": int(road.get("id")), "s": float(o.get("s")), "t": float(o.get("t")),
                            "arrow_type": "right" if name.endswith("R") else "left", "name": name, "wp": wp})
    return out


def map_twltl_starts(cmap) -> list:
    """Start points next to a two-way left-turn lane: lane -1 (driving with s) and lane 2 (against s)."""
    root = ET.fromstring(cmap.to_opendrive())
    out = []
    for road in root.iter("road"):
        L = float(road.get("length"))
        if road.get("junction") not in (None, "-1") or L < 60:
            continue
        if not any(ln.get("type") == "bidirectional" for ln in road.iter("lane")):
            continue
        rid = int(road.get("id"))
        for lane, s in ((-1, 8.0), (2, L - 8.0)):
            try:
                wp = cmap.get_waypoint_xodr(rid, lane, s)
            except RuntimeError:
                wp = None
            if wp is not None and wp.lane_type == carla.LaneType.Driving:
                out.append({"road": rid, "lane": lane, "length": L, "wp": wp})
    return out


# ---------------------------------------------------------------- reasoner with prompt choice and summary

class ScenarioReasoner(Reasoner):
    def __init__(self, repo, region, mock, seed, prompt=None, summary=False):
        super().__init__(repo, region, mock, seed)
        from ..agent.prompts import prompt_parts
        if prompt:
            self.cfg["prompt"]["dir"] = f"prompts/{prompt}"
        if summary:
            self.cfg["api"]["reasoning_summary"] = "auto"
        self.parts = {t: prompt_parts(self.cfg, t, region) for t in ("A", "B")}

    def ask(self, jpeg, test, gt, key):
        t0 = time.time()
        rec = {"test": test, "mock": self.mock, "answer": None, "error": "", "usage": {}, "latency_s": 0.0,
               "cost": 0.0, "summary": ""}
        try:
            if self.mock:
                rec["answer"] = self._mock_answer(test, gt, key)
            else:
                resp = self.call(self.cfg, self.build_payload(self.cfg, self.parts[test], jpeg))
                ans, err = self.parse(resp["text"])
                u = resp.get("usage") or {}
                rec.update(answer=ans, error=err, usage=u, latency_s=resp.get("latency_s", 0.0),
                           summary=resp.get("reasoning_summary", "") or resp.get("reasoning_summary_note", ""),
                           cost=(u.get("input_tokens", 0) * self.price_in + u.get("output_tokens", 0) * self.price_out) / 1e6)
        except Exception as e:
            rec["error"] = f"{type(e).__name__}: {e}"
        if not rec["latency_s"]:
            rec["latency_s"] = round(time.time() - t0, 2)
        return rec

    def _mock_answer(self, test, gt, key):
        rng = random.Random(f"{self.seed}:{key}:{test}")
        mt, at = gt["marking_type"], gt.get("arrow_type", "")
        if mt == "arrow" and rng.random() < (0.3 if test == "A" else 0.1):
            at = {"right": "straight_right", "left": "straight_left"}.get(at, at)
        sug = self.prefill(self.table, self.region, mt, at, gt.get("dashed_side", ""), "full") or {}
        acts = {a: (sug.get("actions") or {}).get(a, "not_applicable") for a in ACTIONS}
        return {"description": "(mock answer)", "evidence": "full",
                "marking": {"marking_type": mt, "arrow_type": at or None, "position": gt.get("position", "left")},
                "rule_reasoning": "(mock)", "cited_rule_id": (sug.get("rule_ids") or [None])[0] if test == "B" else None,
                "action_reasons": {}, "self_check": "(mock)", "actions": acts}


def truth_for(kind, table, region, prefill, mt, arrow_type="", dashed_side=""):
    sug = prefill(table, region, mt, arrow_type, dashed_side, "full") or {}
    return {a: (sug.get("actions") or {}).get(a, "not_applicable") for a in ACTIONS}, sug.get("rule_ids", [])


# ---------------------------------------------------------------- live view with the reasoning of every target

class ScenarioView(LiveView):
    def set_targets(self, n, res, targets, tests, elapsed, title_extra=""):
        P = [("title", f"LLM reasoning, decision #{n}  ({elapsed:.1f} s){title_extra}")]
        for name, tg in targets.items():
            for t in sorted(tests, key=lambda x: x != self.drive_with):
                r = res.get((t, name))
                head = f"Test {t} ({'image + rules' if t == 'B' else 'image only'}), {tg['label']}"
                if r is None:
                    P.append(("head", head + "  ... waiting"))
                    continue
                a = r.get("answer") or {}
                if not a:
                    P.append(("head", head + "  error"))
                    P.append(("text", (r.get("error") or "no answer")[:200]))
                    continue
                m, acts = a.get("marking") or {}, a.get("actions") or {}
                mt = m.get("marking_type")
                if m.get("arrow_type"):
                    mt += f" ({m.get('arrow_type')})"
                rel = RELEVANT[tg["kind"]]
                wrong = [x for x in rel if acts.get(x) != tg["truth"][x]]
                P.append(("head", f"{head}  {r.get('latency_s', 0):.1f} s"))
                P.append(("bad" if wrong else "ok", "-> " + mt + ": " + ", ".join(f"{SHORT[x]} {acts.get(x)}" for x in rel)))
                if wrong:
                    P.append(("bad", "   truth: " + ", ".join(f"{SHORT[x]} {tg['truth'][x]}" for x in wrong)))
                if t == self.drive_with or wrong:
                    reasons = a.get("action_reasons") or {}
                    rs = "; ".join(f"{SHORT[x]}: {reasons[x]}" for x in rel if reasons.get(x))
                    for label, txt in (("look", a.get("description")), ("rule", a.get("rule_reasoning")),
                                       ("cited", a.get("cited_rule_id")), ("decide", rs), ("check", a.get("self_check")),
                                       ("reasoning", a.get("reasoning")), ("model summary", r.get("summary"))):
                        if txt:
                            P.append(("text", f"{label}: {txt}"))
        self.panel = P

    def snapshot(self, path):
        self.pg.image.save(self.screen, str(path))


# ---------------------------------------------------------------- a simple driver (no Traffic Manager)

def lane_step(w, d, same_dir=True):
    """Move d metres along lane `w` in the car's direction (lanes against the car use previous())."""
    n = w.next(d) if same_dir else w.previous(d)
    return n


def build_plan(wp, length=110.0, choice=None, shift=None, step=2.0):
    """Points the car will follow: along its lane, at the next junction the branch of `choice`
    (go_straight / turn_left / turn_right), or after 12 m in the neighbour lane on side `shift`."""
    pts, cur, same, travelled = [], wp, True, 0.0
    if shift:
        nb = wp.get_left_lane() if shift == "left" else wp.get_right_lane()
        if nb is not None and nb.lane_type in (carla.LaneType.Driving, carla.LaneType.Bidirectional):
            same = (nb.lane_id > 0) == (wp.lane_id > 0)
            for d in (2.0, 4.0):
                n = wp.next(d)
                if n:
                    pts.append(n[0].transform.location)
            n = lane_step(nb, 12.0, same)
            if n:
                cur, travelled = n[0], 12.0
    while travelled < length:
        nxt = lane_step(cur, step, same)
        if not nxt:
            break
        if (len(nxt) > 1 or nxt[0].is_junction) and choice:
            best = nxt[0]
            for br in nxt:
                end = br
                for _ in range(200):
                    if not end.is_junction:
                        break
                    n2 = end.next(step)
                    if not n2:
                        break
                    end = n2[0]
                if movement_of(yaw_delta(cur.transform.rotation.yaw, end.transform.rotation.yaw)) == choice:
                    best = br
                    break
            nxt = [best]
        cur = nxt[0]
        pts.append(cur.transform.location)
        travelled += step
    return pts


class Driver:
    """Pure-pursuit steering and a speed controller along the planned points."""

    def __init__(self, ego, speed=7.0):
        self.ego, self.speed, self.plan, self.i = ego, speed, [], 0

    def set_plan(self, pts):
        self.plan, self.i = pts, 0

    def step(self):
        tf = self.ego.get_transform()
        loc, yaw = tf.location, math.radians(tf.rotation.yaw)
        v = self.ego.get_velocity()
        speed = math.hypot(v.x, v.y)
        if not self.plan or self.i >= len(self.plan):
            self.ego.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0))
            return False
        ld = max(4.5, 0.8 * speed + 3.0)
        while self.i < len(self.plan) - 1:
            p = self.plan[self.i]
            dx, dy = p.x - loc.x, p.y - loc.y
            ahead = math.cos(yaw) * dx + math.sin(yaw) * dy
            if ahead < 0 or math.hypot(dx, dy) < ld:
                self.i += 1
            else:
                break
        p = self.plan[self.i]
        dx, dy = p.x - loc.x, p.y - loc.y
        lat = -math.sin(yaw) * dx + math.cos(yaw) * dy
        dist = max(1.0, math.hypot(dx, dy))
        steer = math.atan(2.9 * 2.0 * lat / (dist * dist)) / 1.22
        if self.i >= len(self.plan) - 1 and dist < 3.0:
            self.ego.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0, steer=0.0))
            return False
        if speed < self.speed:
            ctl = carla.VehicleControl(throttle=min(0.75, 0.25 + 0.4 * (self.speed - speed)), steer=max(-1, min(1, steer)))
        else:
            ctl = carla.VehicleControl(throttle=0.0, brake=min(0.5, 0.2 * (speed - self.speed)), steer=max(-1, min(1, steer)))
        self.ego.apply_control(ctl)
        return True


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--scenario", choices=["arrows", "twltl", "lanes"], default="arrows")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=2000)
    ap.add_argument("--region", default="US")
    ap.add_argument("--tests", default="AB")
    ap.add_argument("--drive-with", default="B")
    ap.add_argument("--prompt", default="", help="prompt version folder, e.g. v2 or v3 (default: the one in experiment.yaml)")
    ap.add_argument("--summary", action="store_true", help="also ask for the model's summary of its hidden reasoning")
    ap.add_argument("--decisions", type=int, default=3)
    ap.add_argument("--weather", default="ClearNoon")
    ap.add_argument("--night", action="store_true")
    ap.add_argument("--seed", type=int, default=6216)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    tests = [t for t in "AB" if t in args.tests.upper()]
    drive_with = args.drive_with.upper() if args.drive_with.upper() in tests else tests[-1]
    rng = random.Random(args.seed)
    repo = Path(args.repo)
    reasoner = ScenarioReasoner(repo, args.region, args.mock, args.seed, args.prompt or None, args.summary)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(args.out or (Path(__file__).resolve().parent / "scenario_runs" /
                            f"{stamp}_{args.scenario}{'_mock' if args.mock else ''}"))
    for sub in ("frames", "decisions"):
        (out / sub).mkdir(parents=True, exist_ok=True)

    client = carla.Client(args.host, args.port)
    client.set_timeout(120.0)
    world = client.get_world()
    cmap = world.get_map()
    map_name = cmap.name.split("/")[-1]
    print(f"server map: {map_name}", flush=True)
    weather = getattr(carla.WeatherParameters, args.weather)
    if args.night:
        weather.sun_altitude_angle = -30.0
    world.set_weather(weather)

    if args.scenario == "arrows":
        starts = map_arrows(cmap)
        rng.shuffle(starts)
        print(f"{len(starts)} arrows on this map", flush=True)
        for a in starts:
            print(f"    road {a['road']} s {a['s']:.1f} t {a['t']:.2f} {a['arrow_type']} -> lane {a['wp'].lane_id}", flush=True)
    elif args.scenario == "twltl":
        starts = map_twltl_starts(cmap)
        rng.shuffle(starts)
        print(f"{len(starts)} start points next to a two-way left-turn lane", flush=True)
        if not starts:
            raise SystemExit("this map has no two-way left-turn lane (use Town03)")
    else:
        starts = [{"wp": cmap.get_waypoint(sp.location)} for sp in cmap.get_spawn_points()]
        rng.shuffle(starts)

    original = world.get_settings()
    st = world.get_settings()
    st.synchronous_mode, st.fixed_delta_seconds = True, 0.05
    world.apply_settings(st)

    meta = {"map": map_name, "scenario": args.scenario, "weather": args.weather + (" night" if args.night else ""),
            "region": args.region, "prompt": reasoner.cfg["prompt"]["dir"], "model": reasoner.cfg["api"]["model"],
            "reasoning_effort": reasoner.cfg["api"].get("reasoning_effort"),
            "reasoning_summary": reasoner.cfg["api"].get("reasoning_summary"), "tests": tests,
            "drive_with": drive_with, "seed": args.seed, "started": stamp, "mock": args.mock}
    answers, decisions = [], []
    camera = ego = view = driver = None
    pool = ThreadPoolExecutor(max_workers=4)
    images = queue.Queue()

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

    def place(wp, back=0.0):
        """Put the car on `wp` (or `back` metres before it) and plan along its lane."""
        start = wp
        if back:
            prev = wp.previous(back)
            if prev:
                start = prev[0]
        tf = start.transform
        ego.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0))
        ego.set_target_velocity(carla.Vector3D(0, 0, 0))
        ego.set_transform(carla.Transform(carla.Location(tf.location.x, tf.location.y, tf.location.z + 0.3), tf.rotation))
        driver.set_plan([])
        for _ in range(10):
            tick(drive=False)
        driver.set_plan(build_plan(start))

    try:
        lib = world.get_blueprint_library()
        for sp in cmap.get_spawn_points():
            ego = world.try_spawn_actor(lib.find("vehicle.tesla.model3"), sp)
            if ego is not None:
                break
        driver = Driver(ego)
        cam_bp = lib.find("sensor.camera.rgb")
        cam_bp.set_attribute("image_size_x", str(W))
        cam_bp.set_attribute("image_size_y", str(H))
        cam_bp.set_attribute("fov", str(FOV))
        camera = world.spawn_actor(cam_bp, carla.Transform(carla.Location(x=CAM_X, z=CAM_Z)), attach_to=ego)
        camera.listen(images.put)
        view = ScenarioView(world, args.mock, drive_with, (out / "live_view.mp4") if args.record else None)
        view.panel = [("title", f"Scenario: {args.scenario} on {map_name}"), ("text", f"prompt {meta['prompt']}, "
                      f"tests {', '.join(tests)}, decisions by Test {drive_with}")]

        for start in starts:
            if len(decisions) >= args.decisions or view.quit:
                break
            n = len(decisions) + 1
            # ---------------------------------------------------- drive up to the target
            place(start["wp"], back=35.0 if args.scenario == "arrows" else 0.0)
            view.status, view.boxes, view.lines = f"#{n}: driving to the target", {}, []
            ready, img, bgr = False, None, None
            for k in range(500):
                img, bgr = tick()
                if view.quit:
                    break
                loc = ego.get_location()
                wp = cmap.get_waypoint(loc, project_to_road=True, lane_type=carla.LaneType.Driving)
                if args.scenario == "arrows":
                    a = start["wp"].transform.location
                    fv = ego.get_transform().get_forward_vector()
                    dx, dy = a.x - loc.x, a.y - loc.y
                    ahead, lateral = dx * fv.x + dy * fv.y, abs(-dx * fv.y + dy * fv.x)
                    if ahead < 8:
                        break
                    if ahead <= 14 and lateral < 2.0:
                        ready = True
                        break
                elif args.scenario == "twltl":
                    if k > 40 and wp and not wp.is_junction:
                        left = wp.get_left_lane()
                        if left is not None and left.lane_type == carla.LaneType.Bidirectional:
                            ready = True
                            break
                else:
                    if k > 60 and wp and not wp.is_junction:
                        ready = True
                        break
            if not ready:
                print("    skipped a start point (target not reached)", flush=True)
                continue

            # ---------------------------------------------------- targets, truth and boxes
            wp = cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Driving)
            targets = {}
            if args.scenario == "arrows":
                at = start["arrow_type"]
                truth, rids = truth_for("arrow", reasoner.table, args.region, reasoner.prefill, "arrow", at)
                targets["arrow"] = {"kind": "arrow", "label": "arrow in my lane", "box": arrow_box(start["wp"], img.transform),
                                    "marking_type": "arrow", "arrow_type": at, "position": "in_ego_lane",
                                    "truth": truth, "rule_ids": rids, "map_moves": sorted(junction_moves(wp))}
            elif args.scenario == "twltl":
                centre = wp.get_left_lane()
                truth, rids = truth_for("twltl", reasoner.table, args.region, reasoner.prefill, "two_way_left_turn_lane")
                targets["centre"] = {"kind": "twltl", "label": "centre lane", "box": centre_lane_box_for(wp, centre, img.transform),
                                     "marking_type": "two_way_left_turn_lane", "position": "left", "truth": truth, "rule_ids": rids}
                # The yellow line between the car's lane and the centre lane is not asked about on its own: from
                # the through lane its solid side faces the car (no passing), yet entering the centre lane to turn
                # left is allowed, so a label for "cross this line" would be ambiguous.
            else:
                for side in ("left", "right"):
                    g = ground_truth(wp, side, reasoner.table, args.region, reasoner.prefill)
                    if not g["scored"]:
                        continue
                    lt, lr = truth_for("line", reasoner.table, args.region, reasoner.prefill, g["marking_type"], "", g["dashed_side"])
                    targets[side] = {"kind": "line", "label": f"{side} line", "box": line_box(wp, side, img.transform),
                                     "marking_type": g["marking_type"], "dashed_side": g["dashed_side"], "position": side,
                                     "truth": lt, "rule_ids": lr, "carla_allows": g["carla_allows"]}
            targets = {k: v for k, v in targets.items() if v["box"]}
            if not targets:
                print("    skipped: target not in the picture", flush=True)
                continue
            imwrite(str(out / "frames" / f"{n:03d}.png"), bgr)

            # ---------------------------------------------------- ask (the simulation waits), each answer shown as it arrives
            ego.apply_control(carla.VehicleControl(throttle=0.0, brake=0.0))
            jobs = {(t, name): pool.submit(reasoner.ask, boxed_jpeg(bgr, tg["box"], reasoner.cfg["prompt"]), t, tg, f"{n}:{name}")
                    for t in tests for name, tg in targets.items()}
            view.boxes = {name: tg["box"] for name, tg in targets.items()}
            view.box_colours = {}
            t0 = time.time()
            while not view.quit:
                partial = {k: (f.result() if f.done() else None) for k, f in jobs.items()}
                view.set_targets(n, partial, targets, tests, time.time() - t0)
                view.status = f"#{n}: asking the model (Test {' and '.join(tests)})  {time.time() - t0:4.1f} s"
                view.show(bgr, None, throttle=False)
                if all(f.done() for f in jobs.values()):
                    break
                time.sleep(0.1)
            res = {k: f.result() for k, f in jobs.items()}

            # ---------------------------------------------------- decide and act
            def says(name, action):
                a = (res.get((drive_with, name)) or {}).get("answer") or {}
                return (a.get("actions") or {}).get(action, "error")

            dec = {"n": n, "scenario": args.scenario, "road_id": wp.road_id, "lane_id": wp.lane_id,
                   "targets": {k: dict(v) for k, v in targets.items()}, "drive_with": drive_with}
            yaw0 = ego.get_transform().rotation.yaw
            if args.scenario == "arrows":
                tg = targets["arrow"]
                desire = rng.choice(["go_straight", "turn_left", "turn_right"])
                order = [desire] + [m for m in ("go_straight", "turn_right", "turn_left") if m != desire]
                choice = next((m for m in order if says("arrow", m) == "allowed"), None)
                driver.set_plan(build_plan(wp, 90.0, choice=choice) if choice else [])
                view.status = (f"#{n}: wants {SHORT[desire]}; {drive_with} says {says('arrow', desire)}"
                               f" -> goes {SHORT[choice] if choice else 'nowhere: stops'}")
                view.lines = [f"arrow truth: {tg['arrow_type']} | map connects this lane to: "
                              f"{', '.join(SHORT[m] for m in tg['map_moves']) or '-'}",
                              "truth: " + ", ".join(f"{SHORT[x]} {tg['truth'][x]}" for x in RELEVANT['arrow'])]
                dec.update(desire=desire, system_says=says("arrow", desire), truth=tg["truth"][desire], choice=choice,
                           choice_truth=tg["truth"].get(choice) if choice else None)
            elif args.scenario == "twltl":
                desire = "enter_center_lane_to_wait"
                s_centre = says("centre", desire) if "centre" in targets else "not asked"
                if s_centre == "allowed":
                    driver.set_plan(build_plan(wp, 60.0, shift="left"))
                view.status = (f"#{n}: wants to turn left soon; {drive_with}: enter centre lane {s_centre}"
                               f" -> {'MOVES INTO THE CENTRE LANE' if s_centre == 'allowed' else 'stays in lane'}")
                view.lines = ["truth: centre lane = two_way_left_turn_lane: enter centre lane "
                              f"{targets.get('centre', {}).get('truth', {}).get(desire, '-')}, turn left "
                              f"{targets.get('centre', {}).get('truth', {}).get('turn_left', '-')}"]
                dec.update(desire=desire, system_says=s_centre, truth=targets.get("centre", {}).get("truth", {}).get(desire))
            else:
                side = rng.choice(list(targets))
                s_line = says(side, "cross_line")
                if s_line == "allowed":
                    driver.set_plan(build_plan(wp, 60.0, shift=side))
                view.status = f"#{n}: wants to change lane {side}; {drive_with} says {s_line}"
                view.lines = [f"{k} line truth: {v['marking_type']} cross {v['truth']['cross_line']}" for k, v in targets.items()]
                dec.update(desire=f"cross_{side}", system_says=s_line, truth=targets[side]["truth"]["cross_line"])
            rgb = {"allowed": (0, 200, 0), "prohibited": (230, 40, 40)}
            view.box_colours = {name: rgb.get(says(name, dec.get("desire") if tg["kind"] == "arrow" else RELEVANT[tg["kind"]][0]),
                                              (255, 200, 0)) for name, tg in targets.items()}
            view.set_targets(n, res, targets, tests, max(r.get("latency_s") or 0 for r in res.values()))
            view.show(bgr, None, throttle=False)
            view.snapshot(out / "decisions" / f"{n:03d}.png")

            for (t, name), rec in res.items():
                answers.append(dict(rec, n=n, target=name, kind=targets[name]["kind"],
                                    truth={k: v for k, v in targets[name].items() if k != "box"}, box=targets[name]["box"]))
            print(f"[{n}/{args.decisions}] " + "  ".join(
                f"{t}/{name}:" + ",".join(f"{SHORT[x]}={((res[(t, name)].get('answer') or {}).get('actions') or {}).get(x, 'err')}"
                                          for x in RELEVANT[targets[name]['kind']]) for t in tests for name in targets) +
                  f"  -> {view.status}", flush=True)

            # ---------------------------------------------------- watch what the car does
            in_junction, moved, lane_type_end = False, None, None
            for _ in range(260):
                tick()
                w2 = cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Any)
                if args.scenario == "arrows" and w2 is not None:
                    if w2.is_junction:
                        in_junction = True
                    elif in_junction:
                        for _ in range(20):
                            tick()
                        moved = movement_of(yaw_delta(yaw0, ego.get_transform().rotation.yaw))
                        break
                if w2 is not None:
                    lane_type_end = str(w2.lane_type)
            if args.scenario == "arrows":
                dec["observed_movement"] = moved
                view.status = f"#{n}: the car went {SHORT.get(moved, 'not through the junction')}"
                print(f"    the car went {moved}", flush=True)
            else:
                dec["lane_type_after"] = lane_type_end
            decisions.append(dec)
    finally:
        try:
            with open(out / "answers.jsonl", "w", encoding="utf-8") as f:
                for r in answers:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
            with open(out / "decisions.jsonl", "w", encoding="utf-8") as f:
                for d in decisions:
                    f.write(json.dumps(d, ensure_ascii=False) + "\n")
            s = summarize(answers, decisions, tests, meta)
            (out / "summary.json").write_text(json.dumps(s, indent=2), encoding="utf-8")
            print(json.dumps(s["per_test"], indent=1), flush=True)
            print(json.dumps(s["closed_loop"], indent=1), flush=True)
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


def centre_lane_box_for(ego_wp, centre_wp, cam_tf, d0=8, d1=20):
    """Box over the two-way left-turn lane 8 to 20 m ahead, following the car's direction of travel."""
    pts = []
    for d in range(d0, d1 + 1, 2):
        nxt = ego_wp.next(float(d))
        if not nxt:
            break
        w = nxt[0]
        c = w.get_left_lane()
        if c is None or c.lane_type != carla.LaneType.Bidirectional:
            continue
        half = c.lane_width / 2.0
        # lateral offsets measured from the car's lane centre: its left edge, then the far edge of the centre lane
        pts += [offset(w, 0.0, -w.lane_width / 2.0), offset(w, 0.0, -(w.lane_width / 2.0 + 2 * half))]
    return bbox(project(pts, cam_tf))


def summarize(answers, decisions, tests, meta):
    per = {}
    for t in tests:
        rs = [a for a in answers if a["test"] == t]
        ok = [a for a in rs if a["answer"]]
        d = {"requests": len(rs), "answered": len(ok), "cost_usd": round(sum(a.get("cost", 0) for a in rs), 4),
             "mean_latency_s": round(sum(a["latency_s"] for a in rs) / len(rs), 2) if rs else 0, "by_kind": {}}
        for a in ok:
            k = a["kind"]
            st = d["by_kind"].setdefault(k, {"targets": 0, "marking_correct": 0, "actions_checked": 0, "actions_correct": 0,
                                             "unsafe": 0, "over_cautious": 0})
            st["targets"] += 1
            m = a["answer"].get("marking") or {}
            st["marking_correct"] += (m.get("marking_type") == a["truth"]["marking_type"] and
                                      (k != "arrow" or m.get("arrow_type") == a["truth"].get("arrow_type")))
            for x in RELEVANT[k]:
                g, w = a["truth"]["truth"][x], (a["answer"].get("actions") or {}).get(x)
                st["actions_checked"] += 1
                st["actions_correct"] += g == w
                st["unsafe"] += g == "prohibited" and w == "allowed"
                st["over_cautious"] += g == "allowed" and w != "allowed"
        per[t] = d
    loop = {"decision_points": len(decisions),
            "wanted_something_prohibited": sum(1 for d in decisions if d.get("truth") == "prohibited"),
            "blocked_by_system": sum(1 for d in decisions if d.get("truth") == "prohibited" and d.get("system_says") != "allowed"),
            "allowed_although_prohibited": sum(1 for d in decisions if d.get("truth") == "prohibited" and d.get("system_says") == "allowed")}
    if meta["scenario"] == "arrows":
        loop["chosen_movement_allowed_by_rules"] = sum(1 for d in decisions if d.get("choice_truth") == "allowed")
        loop["car_went_as_chosen"] = sum(1 for d in decisions if d.get("choice") and d.get("observed_movement") == d.get("choice"))
    return {"meta": meta, "per_test": per, "closed_loop": loop}


if __name__ == "__main__":
    main()
