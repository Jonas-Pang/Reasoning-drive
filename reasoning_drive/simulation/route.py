"""A continuous drive through every kind of lane marking on one map, answered by the Reasoning-drive system itself.

A route (configs/carla.yaml, under routes) lists stops: lane lines of each type, a roundabout, a two-way left-turn lane and lane-use
arrows. Before driving, the navigation plan is worked out and shown: the order of the stops, the intent at each
stop and the turn-by-turn directions of every leg. The car then drives one loop through all stops without leaving
the simulation (CARLA's GlobalRoutePlanner plans each leg, a pure-pursuit controller drives it); the live window
shows the planned route on a small map and the next navigation instruction all the time.

At every stop the simulation waits. The camera picture is saved as an image and given to the project exactly as a
labeled image would be (reasoning_drive.data.Item with the target box and a label from the country's rule table),
and reasoning_drive.agent.runner.ask is called once per experiment (configs/carla.yaml, experiments):

    A  Test A, region US: image only
    B  Test B, region US: image + MUTCD passages
    C  Test B, region CN: the same US road, with the GB 5768.3 passages (the photo is said to be from China)

So the project's own prompt builder, image preparation, API client, parser, scoring (contested cells kept apart)
and cache are used, and reasoning_drive.agent.trace.trace_text prints each answer's reasoning step by step: look, rule
(with the cited passage), decide (one reason per action), check, the model's summary of its hidden reasoning,
the result against the label, tokens and cost. The live window shows A, B and C one after another.

The model is never told what the car wants. The navigation route gives the intent; the car checks it against the
B answer: allowed -> it does it, prohibited -> it does not (at an arrow it takes a movement the answer allows and
the route is planned again). What C would have done is recorded. An answer for exactly the same target from an
earlier run (results/carla/answer_cache.json) is reused instead of asking again.

    python main.py carla route route1 --record [--mock] [--preview]

Needs the carla package of the server's version (0.9.15) and the CARLA folder set in configs/carla.yaml (server.carla_root),
whose PythonAPI/carla holds the route planner.
"""
from __future__ import annotations

import argparse
import itertools
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
from types import SimpleNamespace

import carla
import cv2
import numpy as np

from ..imageio import imread, imwrite
from .. import paths as P  # noqa: E402
from .settings import add_agents_path, load_settings  # noqa: E402

SETTINGS = load_settings(P.REPO)
add_agents_path(SETTINGS)
from agents.navigation.global_route_planner import GlobalRoutePlanner  # noqa: E402
from agents.navigation.local_planner import RoadOption  # noqa: E402
from .loop import CAM_X, CAM_Z, FOV, H, W, LiveView, ground_truth, project_marking  # noqa: E402
from .scenarios import (ACTIONS, Driver, arrow_box, bbox, build_plan, centre_lane_box_for,  # noqa: E402
                             junction_moves, map_twltl_starts, movement_of, project, yaw_delta)
from . import suite as carla_suite  # noqa: E402
from .suite import (Counter, find_line_cases, line_points, map_arrows, marking, neighbour,  # noqa: E402
                         neighbour_rel)

EXPS = {k: (v["region"], v["test"]) for k, v in (SETTINGS.get("experiments") or {}).items()} or \
    {"A": ("US", "A"), "B": ("US", "B"), "C": ("CN", "B")}
EXP_LABEL = {"A": "A  Test A, US (image only)", "B": "B  Test B, US (image + MUTCD)", "C": "C  Test B, CN rules on a US road"}
RELEVANT = {"arrow": ["go_straight", "turn_left", "turn_right", "u_turn"], "line": ["cross_line"],
            "twltl": ["enter_center_lane_to_wait", "turn_left"]}
SHORT = {"cross_line": "cross", "go_straight": "straight", "turn_left": "left", "turn_right": "right",
         "u_turn": "U-turn", "enter_center_lane_to_wait": "enter centre lane"}
CN_ACT = {"go_straight": "直行", "turn_left": "左转", "turn_right": "右转", "u_turn": "掉头", "cross_line": "越线"}
NAV_CN = {RoadOption.LEFT: "路口左转", RoadOption.RIGHT: "路口右转", RoadOption.STRAIGHT: "路口直行",
          RoadOption.CHANGELANELEFT: "向左变道", RoadOption.CHANGELANERIGHT: "向右变道"}
NAV_EN = {v: k for k, v in {"turn left at the junction": "路口左转", "turn right at the junction": "路口右转",
                            "straight on at the junction": "路口直行", "change to the left lane": "向左变道",
                            "change to the right lane": "向右变道"}.items()}   # the panel font has no Chinese
LABEL_CN = {
    "broken white lane line": "白虚线", "double solid yellow centre line": "双黄实线",
    "solid + broken yellow centre line": "黄虚实线（我侧虚线）", "solid + broken yellow centre line (solid on my side)": "黄虚实线（我侧实线）",
    "single solid yellow line on the left": "左侧单黄实线", "two-way left-turn lane": "双向左转中心车道",
    "roundabout: line between the circulating lanes": "环岛内的车道线",
    "junction approach: left-turn arrow and the line to the right lane": "路口前：左转箭头+右侧白实线",
    "right-turn arrow": "右转箭头"}
INTENT_CN = {
    "change lane across the line": "越线变道", "overtake across the centre line": "越过中心线超车",
    "cross the yellow line to the left": "向左越过黄线", "enter the centre lane to wait for a left turn": "进中心车道等左转",
    "move to the outer lane to leave the roundabout": "并到外侧车道出环岛", "turn_right": "在路口右转",
    "turn_left": "在路口左转", "go_straight": "在路口直行"}
ROUNDABOUT = {"Town03": ((0.0, 0.0), 18.8, 21.0)}  # centre and radius band of the inner circulating lane (m)
carla_suite.ROUNDABOUT.update(ROUNDABOUT)


# ---------------------------------------------------------------- the project, used as it is

class ProjectSystem:
    """The project itself: settings from configs/, labels from the countries' rule tables (regulations/<CODE>/),
    requests through agent.runner.ask, reasoning through agent.trace.trace_text."""

    def __init__(self, repo: Path, mock: bool, summary: str):
        from .. import config as C
        from ..agent import runner as R
        from ..agent.trace import passage_map, trace_text
        from ..data import Item
        from ..evaluation.scoring import contested_actions, score_one
        from ..labeling.core import load_action_rules, prefill
        self.R, self.Item, self.trace_text, self.prefill = R, Item, trace_text, prefill
        self.score_one, self.contested_actions = score_one, contested_actions
        self.cfg = C.load(repo)
        self.cfg["mock"] = mock
        if summary:
            self.cfg["api"]["reasoning_summary"] = summary
        if not mock and not C.api_key(self.cfg):
            raise SystemExit("No OPENAI_API_KEY in .env. Add it, or run with --mock.")
        self.table = load_action_rules(SimpleNamespace(repo=repo))
        self.ctx = {t: R.Context(self.cfg, t, mock) for t in ("A", "B")}
        self.pmap = {reg: passage_map(self.cfg, reg) for reg in sorted({r for r, _ in EXPS.values()})}
        self.mock = mock

    def label(self, region, mt, at="", ds="", position=""):
        """A label as the labeling tool fills it in from the rule table ('' = the table leaves the cell open)."""
        sug = self.prefill(self.table, region, mt, at or "", ds or "", "full") or {}
        acts = sug.get("actions") or {}
        lab = {"marking_type": mt, "arrow_type": at or "", "position": position, "dashed_side": ds or "", "visibility": "V1",
               "behavior_decidable": "", "expected_evidence": "full", "accepted_rule_ids": ";".join(sug.get("rule_ids", []))}
        for a in ACTIONS:
            lab["act_" + a] = acts[a] if a in acts else ("not_applicable" if acts else "")
        return lab

    def truth(self, lab):
        return {a: (lab.get("act_" + a) or "undecided") for a in ACTIONS}

    def ask(self, frame, box, region, test, lab, image_id):
        item = self.Item(image_id, "carla", region, "carla_town03", "sim", Path(frame), list(box), W, H, lab)
        rec = self.R.ask(self.cfg, item, test, 0, self.mock, use_cache=True, ctx=self.ctx[test])
        usage = (rec.get("response") or {}).get("usage") or {}
        rec["cost"] = 0.0 if rec.get("cached") else self.R.cost_of(self.cfg, usage)
        rec["trace"] = self.trace_text(rec, self.pmap[region], rec["cost"])
        return rec

    def reuse(self, old, lab, region, test, image_id):
        """An earlier answer for the same target, scored again against this label."""
        rec = json.loads(json.dumps(old, default=str))
        rec.update(image_id=image_id, region=region, test=test, cached=True, label=lab, cost=0.0)
        if rec.get("answer"):
            _, ids = self.ctx[test].for_region(region)
            rec["score"] = self.score_one(rec["answer"], lab, test, ids, self.contested_actions(self.table, region, lab))
        rec["trace"] = self.trace_text(rec, self.pmap[region], 0.0)
        return rec


# ---------------------------------------------------------------- resolving the stops of a route

def lane_wps(w, length, same=True, step=2.0):
    out, cur = [], w
    for _ in range(int(length / step)):
        n = cur.next(step) if same else cur.previous(step)
        if not n:
            break
        cur = n[0]
        out.append(cur)
    return out


def paint_dashed_side(wp, side):
    """For a solid + broken yellow centre line: which line faces my car, from the paint. OpenDRIVE "broken solid" is
    broken on the left-lane side (positive lane ids) and solid on the right-lane side; checked against the rendered
    paint in Town03 (CARLA's lane-change flag disagrees with the paint there, so it is not used)."""
    m = marking(wp, side)
    words = ("broken", "solid") if m.type == carla.LaneMarkingType.BrokenSolid else ("solid", "broken")
    near = words[1] if wp.lane_id < 0 else words[0]
    return "ego_side" if near == "broken" else "far_side"


def resolve_stops(route, cmap, root, map_name, seed):
    wps = cmap.generate_waypoints(3.0)
    arrows = map_arrows(cmap, root)
    stops = []
    for i, st in enumerate(route["stops"]):
        rng = random.Random(f"{seed}:{i}:{st['type']}")
        s = dict(st, index=i)
        t = st["type"]
        if t in ("line", "roundabout"):
            case = {"marking": st.get("marking", "white_dashed"), "side": st.get("side"),
                    "neighbour": st.get("neighbour", "same"), "roundabout": t == "roundabout"}
            if st.get("min_run"):
                case["min_run"] = st["min_run"]
            cands = find_line_cases(cmap, case, map_name, wps)
            cands = [c for c in cands if c["wp"].road_id not in st.get("exclude_roads", [])
                     and [c["wp"].road_id, c["wp"].lane_id] not in st.get("exclude", [])]
            if t == "roundabout":
                def dashed_ahead(c):
                    ws = lane_wps(c["wp"], 20)
                    return len(ws) >= 9 and all(project_marking(marking(x, c["side"])) == "white_dashed" for x in ws[2:9])
                cands = [c for c in cands if dashed_ahead(c)]
            if "dashed_side" in st:
                cands = [c for c in cands if paint_dashed_side(c["wp"], c["side"]) == st["dashed_side"]]
            if not cands:
                print(f"stop {i} ({st.get('label', t)}): no place on this map, left out", flush=True)
                continue
            c = cands[st["pick"] % len(cands)] if isinstance(st.get("pick"), int) else rng.choice(cands)
            s.update(kind="line", D=c["wp"], side=c["side"], n_cands=len(cands))
        elif t == "twltl":
            cands = []
            for c in map_twltl_starts(cmap):
                if c["road"] in st.get("exclude_roads", []):
                    continue
                n = c["wp"].next(14.0)
                if n and all((x.get_left_lane() is not None and x.get_left_lane().lane_type == carla.LaneType.Bidirectional)
                             for x in [n[0]] + lane_wps(n[0], 22)):
                    cands.append(n[0])
            if not cands:
                print(f"stop {i}: no two-way left-turn lane, left out", flush=True)
                continue
            s.update(kind="twltl", D=rng.choice(cands), n_cands=len(cands))
        elif t in ("arrow", "approach"):
            cands = [a for a in arrows if a["arrow_type"] == st.get("arrow_type", a["arrow_type"])
                     and a["road"] not in st.get("exclude_roads", [])
                     and ("road" not in st or a["road"] == st["road"]) and ("lane" not in st or a["lane"] == st["lane"])]
            if not cands:
                print(f"stop {i}: no such arrow, left out", flush=True)
                continue
            a = rng.choice(cands)
            prev = a["wp"].previous(11.0)
            s.update(kind="arrow" if t == "arrow" else "approach", D=prev[0] if prev else a["wp"], arrow=a, n_cands=len(cands))
        stops.append(s)
    return stops


def route_length(grp, a, b):
    r = grp.trace_route(a, b)
    return sum(r[k][0].transform.location.distance(r[k + 1][0].transform.location) for k in range(len(r) - 1)) or 1e9


def order_stops(stops, grp, how):
    if how != "shortest" or len(stops) < 3:
        return stops
    n = len(stops)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                L[i][j] = route_length(grp, stops[i]["D"].transform.location, stops[j]["D"].transform.location)
    best, best_p = 1e18, None
    for p in itertools.permutations(range(1, n)):
        seq = (0,) + p + (0,)
        d = sum(L[seq[k]][seq[k + 1]] for k in range(n))
        if d < best:
            best, best_p = d, seq[:-1]
    print(f"loop length about {best / 1000:.2f} km", flush=True)
    return [stops[k] for k in best_p]


def directions(route):
    """Turn-by-turn directions of a planned leg: [(metres from the start, instruction)], and its length."""
    out, d, last = [], 0.0, None
    for k, (w, opt) in enumerate(route):
        if k:
            d += w.transform.location.distance(route[k - 1][0].transform.location)
        if opt in NAV_CN and opt != last:
            out.append((round(d), NAV_CN[opt]))
        last = opt
    return out, round(d)


# ---------------------------------------------------------------- live view: navigation and the reasoning steps

class RouteView(LiveView):
    VW, VH, PW, BH = 640, 360, 760, 300

    def __init__(self, world, mock, drive_with, record_path, lanes):
        super().__init__(world, mock, drive_with, record_path)
        self.cn = self._font(r"C:\Windows\Fonts\msyh.ttc", 15)
        self.cn_b = self._font(r"C:\Windows\Fonts\msyhbd.ttc", 16)
        self.mono = self._font(r"C:\Windows\Fonts\consola.ttf", 12)
        xs, ys = [p[0] for p in lanes], [p[1] for p in lanes]
        self.bounds = (min(xs), max(xs), min(ys), max(ys))
        self.map_rect = (6, self.VH + 40, 252, 252)
        self.map_bg = self.pg.Surface((self.map_rect[2], self.map_rect[3]))
        self.map_bg.fill((22, 22, 22))
        for p in lanes:
            q = self._m(p, origin=False)
            self.map_bg.set_at((int(q[0]), int(q[1])), (80, 80, 80))
        self.nav_path, self.nav_stops, self.nav_lines, self.trace, self.car_xy = [], [], [], None, None

    def _m(self, p, origin=True):
        x0, x1, y0, y1 = self.bounds
        mx, my, mw, mh = self.map_rect
        sc = min((mw - 8) / max(1.0, x1 - x0), (mh - 8) / max(1.0, y1 - y0))
        q = (4 + (p[0] - x0) * sc, 4 + (p[1] - y0) * sc)
        return (mx + q[0], my + q[1]) if origin else (min(mw - 1, q[0]), min(mh - 1, q[1]))

    def _wrap_cn(self, text, font, width):
        out, cur = [], ""
        for ch in str(text):
            if font.size(cur + ch)[0] > width and cur:
                out.append(cur)
                cur = ch
            else:
                cur += ch
        return out + ([cur] if cur else [])

    def show(self, bgr, ego=None, throttle=True):
        pg = self.pg
        self.events()
        if ego is not None:
            self.follow(ego)
            loc = ego.get_location()
            self.car_xy = (loc.x, loc.y)
        rgb = cv2.cvtColor(cv2.resize(bgr, (self.VW, self.VH)), cv2.COLOR_BGR2RGB)
        self.screen.blit(pg.image.frombuffer(rgb.tobytes(), (self.VW, self.VH), "RGB"), (0, 0))
        k = self.VW / W
        for name, box in self.boxes.items():
            if box:
                col = self.box_colours.get(name, (0, 229, 255))
                pg.draw.rect(self.screen, col, pg.Rect(box[0] * k, box[1] * k, (box[2] - box[0]) * k, (box[3] - box[1]) * k), 2)
        # bottom: status, a small map with the planned route, the navigation instructions
        pg.draw.rect(self.screen, (15, 15, 15), pg.Rect(0, self.VH, self.VW, self.BH))
        for i, ln in enumerate(self._wrap(self.status, self.bold, self.VW - 16, 2)):
            self.screen.blit(self.bold.render(ln, True, (255, 220, 60)), (8, self.VH + 4 + 16 * i))
        mx, my, mw, mh = self.map_rect
        self.screen.blit(self.map_bg, (mx, my))
        if len(self.nav_path) > 1:
            pg.draw.lines(self.screen, (60, 200, 255), False, [self._m(p) for p in self.nav_path], 3)
        for s in self.nav_stops:
            q = self._m(s["xy"])
            pg.draw.circle(self.screen, (120, 120, 120) if s.get("done") else (255, 210, 60), (int(q[0]), int(q[1])), 7)
            self.screen.blit(self.small.render(str(s["n"]), True, (0, 0, 0)), (q[0] - 4, q[1] - 7))
        if self.car_xy:
            q = self._m(self.car_xy)
            pg.draw.circle(self.screen, (255, 70, 70), (int(q[0]), int(q[1])), 5)
        y = my
        for kind, ln in self.nav_lines:
            f = self.cn_b if kind == "head" else self.cn
            col = {"head": (255, 220, 60), "now": (120, 220, 255), "done": (130, 130, 130)}.get(kind, (225, 225, 225))
            for part in self._wrap_cn(ln, f, self.VW - mx - mw - 18):
                if y > self.VH + self.BH - 18:
                    break
                self.screen.blit(f.render(part, True, col), (mx + mw + 10, y))
                y += f.get_linesize()
        if self.mock:
            tag = self.big.render("MOCK ANSWERS - no model called", True, (255, 80, 80))
            pg.draw.rect(self.screen, (0, 0, 0), pg.Rect(6, 6, tag.get_width() + 12, tag.get_height() + 8))
            self.screen.blit(tag, (12, 10))
        if self.trace:
            self._draw_trace()
        else:
            self._draw_panel()
        pg.display.flip()
        self.frame_i += 1
        if self.writer is not None and (not throttle or self.frame_i % 2 == 0):
            arr = pg.surfarray.array3d(self.screen).swapaxes(0, 1)
            self.writer.write(cv2.cvtColor(arr, cv2.COLOR_RGB2BGR))
        if throttle:
            dt = time.time() - self.t_last
            if dt < 0.05:
                time.sleep(0.05 - dt)
            self.t_last = time.time()

    def _draw_trace(self):
        """The project's reasoning trace of one answer (agent.trace.trace_text), as the project prints it."""
        pg, x0 = self.pg, self.VW + 8
        pg.draw.rect(self.screen, (24, 26, 30), pg.Rect(self.VW, 0, self.PW, self.VH + self.BH))
        title, text, colour = self.trace
        self.screen.blit(self.bold.render(title, True, colour), (x0, 6))
        y = 28
        for ln in text.split("\n"):
            if y > self.VH + self.BH - 14:
                break
            bad = "UNSAFE" in ln or " wrong" in ln
            c = (255, 120, 120) if bad else ((120, 200, 255) if ln.startswith(("Step", "Result", "Model's")) else (215, 215, 215))
            self.screen.blit(self.mono.render(ln, True, c), (x0, y))
            y += 14

    def snapshot(self, path):
        self.pg.image.save(self.screen, str(path))


def verdict_panel(title, res, targets, elapsed):
    P = [("title", f"{title}  ({elapsed:.1f} s)")]
    for tg in targets:
        rel = RELEVANT[tg["kind"]]
        if len(targets) > 1:
            P.append(("title", f"target: {tg['label']}"))
        for e in "ABC":
            r = res.get((e, tg["name"]))
            if r is None:
                P.append(("head", EXP_LABEL[e] + "  ... waiting"))
                continue
            a = r.get("answer") or {}
            if not a:
                P.append(("head", EXP_LABEL[e] + "  error"))
                P.append(("text", (r.get("error") or r.get("parse_error") or "no answer")[:160]))
                continue
            tr = tg["truth"][e]
            m, acts = a.get("marking") or {}, a.get("actions") or {}
            mt = (m.get("marking_type") or "?") + (f" ({m['arrow_type']})" if m.get("arrow_type") else "")
            wrong = [x for x in rel if tr[x] in ("allowed", "prohibited") and acts.get(x) != tr[x]]
            src = "earlier answer, not asked again" if r.get("reused") else f"{(r.get('response') or {}).get('latency_s') or 0:.1f} s"
            P.append(("head", f"{EXP_LABEL[e]}  [{src}]"))
            P.append(("bad" if wrong else "ok", "-> " + mt + ": " + ", ".join(f"{SHORT[x]} {acts.get(x)}" for x in rel)
                      + (("   label: " + ", ".join(f"{SHORT[x]} {tr[x]}" for x in wrong)) if wrong else "")))
            P.append(("text", f"rule: {a.get('rule_reasoning', '')}  [cited {a.get('cited_rule_id')}]"))
    return P


# ---------------------------------------------------------------- main

def main(argv=None):
    srv = SETTINGS.get("server") or {}
    ap = argparse.ArgumentParser(prog="python main.py carla route", description="one continuous route of configs/carla.yaml")
    ap.add_argument("route", nargs="?", default="route1", help="a route name under routes in configs/carla.yaml")
    ap.add_argument("--repo", default=str(P.REPO))
    ap.add_argument("--cache", default=str(P.REPO / SETTINGS.get("answer_cache", "results/carla/answer_cache.json")))
    ap.add_argument("--host", default=srv.get("host", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(srv.get("port", 2000)))
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--max-stops", type=int, default=0)
    ap.add_argument("--preview", action="store_true", help="only drive the last 25 m to each stop and save its picture (no model)")
    ap.add_argument("--trace-seconds", type=float, default=float(SETTINGS.get("trace_seconds", 5.0)),
                    help="how long each answer's reasoning stays on screen")
    args = ap.parse_args(argv)
    args.route = args.route

    routes = SETTINGS.get("routes") or {}
    if args.route not in routes:
        raise SystemExit(f"No route {args.route} in configs/carla.yaml; there are: {', '.join(routes)}")
    route = routes[args.route]
    seed = route.get("seed", 6216)
    drive_with = route.get("drive_with", "B")
    sysm = ProjectSystem(Path(args.repo), args.mock, route.get("reasoning_summary", "auto"))
    cache_path = Path(args.cache)
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}

    client = carla.Client(args.host, args.port)
    client.set_timeout(float(srv.get("timeout_s", 120)))
    world = client.get_world()
    cmap = world.get_map()
    map_name = cmap.name.split("/")[-1].replace("_Opt", "")
    print(f"server map: {cmap.name.split('/')[-1]}", flush=True)
    if map_name != route["map"]:
        raise SystemExit(f"{args.route} needs {route['map']}; the server runs {map_name} (python main.py carla map {route['map']})")
    weather = getattr(carla.WeatherParameters, route.get("weather", "ClearNoon"))
    if route.get("night"):
        weather.sun_altitude_angle = -30.0
    world.set_weather(weather)
    root = ET.fromstring(cmap.to_opendrive())
    grp = GlobalRoutePlanner(cmap, 2.0)

    stops = resolve_stops(route, cmap, root, map_name, seed)
    stops = order_stops(stops, grp, route.get("order", "shortest"))
    if args.max_stops:
        stops = stops[:args.max_stops]

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(args.repo) / SETTINGS.get("output", "results/carla") / f"{stamp}_{args.route}{'_preview' if args.preview else ''}{'_mock' if args.mock else ''}"
    for sub in ("frames", "decisions"):
        (out / sub).mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------- the navigation plan, worked out before driving
    first = stops[0]["D"]
    back = first.previous(25.0)
    start_tf = (back[0] if back else first).transform
    plan_rows, legs, prev = [], [], start_tf.location
    for k, s in enumerate(stops, 1):
        leg = grp.trace_route(prev, s["D"].transform.location)
        legs.append(leg)
        dirs, dist = directions(leg)
        plan_rows.append({"stop": k, "label": s.get("label", s["type"]), "label_cn": LABEL_CN.get(s.get("label"), s.get("label")),
                          "intent": s.get("intent"), "intent_cn": INTENT_CN.get(s.get("intent"), s.get("intent")),
                          "road": s["D"].road_id, "lane": s["D"].lane_id, "leg_m": dist, "directions": dirs,
                          "xy": [round(s["D"].transform.location.x, 1), round(s["D"].transform.location.y, 1)]})
        prev = s["D"].transform.location
    back_leg = grp.trace_route(prev, start_tf.location)
    legs.append(back_leg)
    total = sum(r["leg_m"] for r in plan_rows) + directions(back_leg)[1]
    (out / "nav_plan.json").write_text(json.dumps({"route": args.route, "map": map_name, "total_m": total, "stops": plan_rows,
                                                   "path": [[round(w.transform.location.x, 1), round(w.transform.location.y, 1)]
                                                            for leg in legs for w, _ in leg]},
                                                  ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"navigation plan ({total / 1000:.2f} km loop):", flush=True)
    for r in plan_rows:
        print(f"  {r['stop']}. {r['label']}  (road {r['road']} lane {r['lane']}), intent: {r['intent']}, leg {r['leg_m']} m: "
              + ", ".join(f"{d} m {t}" for d, t in r["directions"]), flush=True)

    original = world.get_settings()
    st = world.get_settings()
    st.synchronous_mode, st.fixed_delta_seconds = True, 0.05
    world.apply_settings(st)

    meta = {"route": args.route, "map": map_name, "weather": route.get("weather", "ClearNoon"), "night": bool(route.get("night")),
            "prompt": sysm.cfg["prompt"]["dir"], "model": sysm.cfg["api"]["model"],
            "reasoning_effort": sysm.cfg["api"].get("reasoning_effort"), "reasoning_summary": sysm.cfg["api"].get("reasoning_summary"),
            "experiments": EXPS, "drive_with": drive_with, "seed": seed, "started": stamp, "mock": args.mock, "loop_m": total}
    answers, records, markers, track = [], [], [], []
    camera = ego = view = driver = None
    pool = ThreadPoolExecutor(max_workers=6)
    images = queue.Queue()
    odo = {"m": 0.0, "last": None}
    nav = {"route": [], "i": 0, "stop": None}

    def frames():
        return view.writer.count if (view is not None and view.writer is not None) else 0

    def nav_header():
        rows = [("head", "导航路线（按顺序）")]
        for s in view.nav_stops:
            kind = "done" if s.get("done") else ("now" if nav["stop"] is s else "text")
            rows.append((kind, f"{s['n']}. {s['label_cn']} → {s['intent_cn']}"))
        return rows

    def nav_update():
        """The next instruction on the planned route, from the car's position."""
        r = nav["route"]
        if not r or nav["stop"] is None:
            return
        loc = ego.get_location()
        i = nav["i"]
        best = min(range(i, min(len(r), i + 40)), key=lambda j: loc.distance(r[j][0].transform.location), default=i)
        nav["i"] = best
        nxt, d = None, 0.0
        for j in range(best, len(r) - 1):
            d += r[j][0].transform.location.distance(r[j + 1][0].transform.location)
            if r[j + 1][1] in NAV_CN and r[j][1] != r[j + 1][1]:
                nxt = (round(d), NAV_CN[r[j + 1][1]])
                break
        left = sum(r[j][0].transform.location.distance(r[j + 1][0].transform.location) for j in range(best, len(r) - 1))
        s = nav["stop"]
        view.nav_lines = nav_header() + [
            ("now", f"导航：{nxt[0]} 米后{nxt[1]}" if nxt else "导航：沿当前车道行驶"),
            ("text", f"距站点 {s['n']}（{s['label_cn']}）约 {max(0, round(left) - 16)} 米，到站意图：{s['intent_cn']}（模型不知道）")]

    def tick(drive=True):
        if drive and driver is not None:
            driver.step()
        frame = world.tick()
        img = images.get(timeout=10.0)
        while img.frame < frame:
            img = images.get(timeout=10.0)
        bgr = np.ascontiguousarray(np.frombuffer(img.raw_data, dtype=np.uint8).reshape((H, W, 4))[:, :, :3])
        loc = ego.get_location()
        if odo["last"] is not None:
            odo["m"] += loc.distance(odo["last"])
        odo["last"] = loc
        if frame % 10 == 0:
            track.append([round(loc.x, 1), round(loc.y, 1)])
            if drive:
                nav_update()
        if view is not None:
            view.show(bgr, ego)
        return img, bgr

    def here():
        return cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Driving)

    def set_route(r):
        nav["route"], nav["i"] = r, 0
        view.nav_path = [(w.transform.location.x, w.transform.location.y) for w, _ in r]
        driver.set_plan([w.transform.location for w, _ in r])

    def plan_to(dest_wp):
        """Route to a stop: the planner's route ends 30 m before it and the last 30 m follow the stop's own lane, so any
        lane change happens before the stop; the plan goes on 16 m past the stop."""
        pre = dest_wp.previous(30.0)
        pre = pre[0] if pre else dest_wp
        r = grp.trace_route(ego.get_location(), pre.transform.location)
        set_route(r + [(w, RoadOption.LANEFOLLOW) for w in lane_wps(pre, 46)])

    def drive_plan(max_ticks, until=None, near=None):
        """Drive the current plan; 7 m/s, 5 m/s in junctions and within 25 m of `near`; stop when `until()` is true
        or the plan ends."""
        stuck = 0
        for _ in range(max_ticks):
            w = here()
            slow = (w is not None and w.is_junction) or (near is not None and ego.get_location().distance(near) < 25)
            driver.speed = 5.0 if slow else 7.0
            img, bgr = tick()
            if view.quit:
                return None, None, "quit"
            if until is not None:
                res = until()
                if res:
                    return img, bgr, res
            if driver.i >= len(driver.plan) - 2:
                return img, bgr, "plan end"
            v = ego.get_velocity()
            stuck = stuck + 1 if math.hypot(v.x, v.y) < 0.3 else 0
            if stuck > 200:
                return img, bgr, "stuck"
        return img, bgr, "timeout"

    def teleport(tf):
        ego.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0))
        ego.set_target_velocity(carla.Vector3D(0, 0, 0))
        ego.set_transform(carla.Transform(carla.Location(tf.location.x, tf.location.y, tf.location.z + 0.3), tf.rotation))
        driver.set_plan([])
        for _ in range(8):
            tick(drive=False)

    def hold(seconds, bgr):
        """Keep the simulation paused and the window (and the recording) running."""
        t_end = time.time() + seconds
        while time.time() < t_end and not view.quit:
            view.show(bgr, None, throttle=False)
            time.sleep(0.1)

    def cache_key(tg):
        if tg["kind"] == "arrow":
            return f"{map_name}|arrow|{tg['road']}|{tg['lane']}"
        return f"{map_name}|{tg['kind']}|{tg['road']}|{tg['lane']}|{tg.get('side', '')}|{int(tg['s'] // 10)}"

    try:
        lib = world.get_blueprint_library()
        ego = world.try_spawn_actor(lib.find("vehicle.tesla.model3"),
                                    carla.Transform(carla.Location(start_tf.location.x, start_tf.location.y, start_tf.location.z + 0.5),
                                                    start_tf.rotation))
        if ego is None:
            for sp in cmap.get_spawn_points():
                ego = world.try_spawn_actor(lib.find("vehicle.tesla.model3"), sp)
                if ego is not None:
                    break
        driver = Driver(ego, speed=7.0)
        cam_bp = lib.find("sensor.camera.rgb")
        for k, v in (("image_size_x", W), ("image_size_y", H), ("fov", FOV)):
            cam_bp.set_attribute(k, str(v))
        camera = world.spawn_actor(cam_bp, carla.Transform(carla.Location(x=CAM_X, z=CAM_Z)), attach_to=ego)
        camera.listen(images.put)
        lanes = [[w.transform.location.x, w.transform.location.y] for w in cmap.generate_waypoints(5.0)
                 if w.lane_type == carla.LaneType.Driving]
        view = RouteView(world, args.mock, drive_with, (out / "live_view.mp4") if args.record else None, lanes)
        if view.writer is not None:
            view.writer = Counter(view.writer)
        view.nav_stops = [{"n": r["stop"], "xy": r["xy"], "label_cn": r["label_cn"], "intent_cn": r["intent_cn"]} for r in plan_rows]
        teleport(start_tf)
        start_loc = ego.get_location()

        # the whole navigation plan on screen before driving
        img, bgr = tick(drive=False)
        view.nav_path = [(w.transform.location.x, w.transform.location.y) for leg in legs for w, _ in leg]
        view.nav_lines = nav_header()
        view.status = f"navigation plan: {len(stops)} stops in one {total / 1000:.2f} km loop, then back to the start"
        view.panel = [("title", f"{args.route} on {map_name}: the navigation plan")] + [
            ("head", f"{r['stop']}. {r['label']}  ->  intent: {r['intent']}") for r in plan_rows] + [
            ("text", f"leg to {r['stop']} ({r['leg_m']} m): " + (", ".join(f"after {d} m {NAV_EN.get(t, t)}" for d, t in r["directions"][:4])
                                                               or "follow the lane")) for r in plan_rows]
        mk0 = {"stop": "plan", "start": frames()}
        hold(0.5 if args.preview else 8.0, bgr)
        mk0["end"] = frames()
        markers.append(mk0)

        for k, s in enumerate(stops, 1):
            if view.quit:
                break
            D = s["D"]
            label = s.get("label", s["type"])
            nav["stop"] = view.nav_stops[k - 1]
            mk = {"stop": k, "label": label, "drive_start": frames()}
            view.boxes, view.box_colours, view.trace = {}, {}, None
            view.status = f"stop {k}/{len(stops)}: driving to {label}"
            view.panel = [("title", f"Next: stop {k}, {label}"),
                          ("text", f"intent at the stop (from the navigation route, not told to the model): {s.get('intent')}")]
            if args.preview:
                pre = D.previous(25.0)
                pre = pre[0] if pre else D
                teleport(pre.transform)
                set_route([(w, RoadOption.LANEFOLLOW) for w in lane_wps(pre, 45)])
            else:
                plan_to(D)

            def reached():
                loc, dl = ego.get_location(), D.transform.location
                fv = D.transform.get_forward_vector()
                along = (dl.x - loc.x) * fv.x + (dl.y - loc.y) * fv.y
                lateral = abs(-(dl.x - loc.x) * fv.y + (dl.y - loc.y) * fv.x)
                if along < 0.8 and lateral < 1.5 and loc.distance(dl) < 4.0:
                    return "reached"
                if along < -6.0 and loc.distance(dl) < 15.0:
                    return "passed"
                return None

            img, bgr, why = drive_plan(6000, reached, near=D.transform.location)
            if why != "reached":
                print(f"stop {k} ({label}): not reached ({why}), left out", flush=True)
                continue
            wp = here()
            if s["kind"] in ("line", "twltl") and (wp.road_id, wp.lane_id) != (D.road_id, D.lane_id):
                # where two roads overlap the map can put the car on the other one; the stop's own waypoint is the one whose
                # marking was checked when the stop was picked
                print(f"stop {k}: map puts the car on road {wp.road_id} lane {wp.lane_id}, using the stop's road {D.road_id} "
                      f"lane {D.lane_id}", flush=True)
                wp = D
            targets = []
            if s["kind"] == "line":
                side = s["side"]
                if s.get("truth_override"):
                    mt, ds = s["truth_override"], ""
                else:
                    g = ground_truth(wp, side, sysm.table, "US", sysm.prefill)
                    mt, ds = g["marking_type"], g["dashed_side"]
                    if mt == "yellow_solid_dashed":
                        ds = paint_dashed_side(wp, side)
                targets.append({"name": "line", "kind": "line", "label": f"{side} line", "side": side, "road": wp.road_id,
                                "lane": wp.lane_id, "s": wp.s, "box": bbox(project(line_points(wp, side), img.transform)),
                                "position": side, "marking_type": mt, "arrow_type": "", "dashed_side": ds,
                                "map_marking": project_marking(marking(wp, side))})
            elif s["kind"] == "twltl":
                targets.append({"name": "centre", "kind": "twltl", "label": "centre lane", "road": wp.road_id, "lane": wp.lane_id,
                                "s": wp.s, "box": centre_lane_box_for(wp, wp.get_left_lane(), img.transform), "position": "left",
                                "marking_type": "two_way_left_turn_lane", "arrow_type": "", "dashed_side": ""})
            if s["kind"] in ("arrow", "approach"):
                a = s["arrow"]
                if s["kind"] == "approach":
                    side = s.get("line_side", "right")
                    targets.append({"name": "line", "kind": "line", "label": f"{side} line", "side": side, "road": wp.road_id,
                                    "lane": wp.lane_id, "s": wp.s, "box": bbox(project(line_points(wp, side), img.transform)),
                                    "position": side, "marking_type": s.get("truth_override") or project_marking(marking(wp, side)),
                                    "arrow_type": "", "dashed_side": "", "map_marking": project_marking(marking(wp, side)),
                                    "override_note": s.get("note", "")})
                targets.append({"name": "arrow", "kind": "arrow", "label": f"{a['arrow_type']} arrow in my lane", "road": a["road"],
                                "lane": a["lane"], "s": a["s"], "box": arrow_box(a["wp"], img.transform), "position": "in_ego_lane",
                                "marking_type": "arrow", "arrow_type": a["arrow_type"], "dashed_side": "",
                                "map_moves": sorted(junction_moves(wp))})
            targets = [t for t in targets if t["box"]]
            if not targets:
                print(f"stop {k}: target not in the picture, left out", flush=True)
                continue
            for tg in targets:
                tg["labels"] = {e: sysm.label(reg, tg["marking_type"], tg["arrow_type"], tg["dashed_side"], tg["position"])
                                for e, (reg, _) in EXPS.items()}
                tg["truth"] = {e: sysm.truth(lab) for e, lab in tg["labels"].items()}
                tg["cache_key"] = cache_key(tg)
            frame_path = out / "frames" / f"{k:02d}.png"
            imwrite(str(frame_path), bgr)
            if args.preview:
                records.append({"stop": k, "label": label, "road_id": wp.road_id, "lane_id": wp.lane_id, "s": round(wp.s, 1),
                                "xy": plan_rows[k - 1]["xy"], "kind": s["kind"], "targets": targets})
                print(f"preview stop {k}: {label} road {wp.road_id} lane {wp.lane_id} " +
                      ", ".join(f"{t['name']}={t['marking_type']}/{t.get('dashed_side', '')} (map {t.get('map_marking')})" for t in targets), flush=True)
                view.nav_stops[k - 1]["done"] = True
                continue

            # ---------------------------------------------------- ask A, B, C through the project; reuse earlier answers
            mk["ask"] = frames()
            res, jobs = {}, {}
            for tg in targets:
                hit = cache.get(tg["cache_key"], {})
                for e, (reg, test) in EXPS.items():
                    iid = f"{args.route}_stop{k:02d}_{tg['name']}"
                    if e in hit and not args.mock:
                        res[(e, tg["name"])] = dict(sysm.reuse(hit[e], tg["labels"][e], reg, test, iid), reused=True)
                    else:
                        jobs[(e, tg["name"])] = pool.submit(sysm.ask, frame_path, tg["box"], reg, test, tg["labels"][e], iid)
            view.boxes = {tg["name"]: tg["box"] for tg in targets}
            view.box_colours = {}
            title = f"Stop {k}/{len(stops)}: {label}"
            t0 = time.time()
            while not view.quit:
                partial = dict(res)
                partial.update({kk: f.result() for kk, f in jobs.items() if f.done()})
                view.panel = verdict_panel(title, partial, targets, time.time() - t0)
                view.status = f"stop {k}/{len(stops)}: {label} - simulation paused, asking A, B, C  {time.time() - t0:4.1f} s"
                view.show(bgr, None, throttle=False)
                if all(f.done() for f in jobs.values()):
                    break
                time.sleep(0.1)
            res.update({kk: f.result() for kk, f in jobs.items()})
            mk["answered"] = frames()

            # the reasoning of every answer, step by step, as the project prints it
            view.status = f"stop {k}/{len(stops)}: reasoning of each answer, step by step (project trace)"
            for tg in targets:
                for e in "ABC":
                    r = res.get((e, tg["name"])) or {}
                    sc = r.get("score") or {}
                    bad = bool(sc.get("unsafe")) or sc.get("output2") is False
                    view.trace = (f"{EXP_LABEL[e]}  -  {tg['label']}" + ("  (earlier answer, reused)" if r.get("reused") else ""),
                                  r.get("trace") or r.get("error") or "no answer", (255, 120, 120) if bad else (120, 220, 140))
                    hold(min(2.0, args.trace_seconds) if r.get("reused") else args.trace_seconds, bgr)
            view.trace = None
            mk["traces_done"] = frames()

            def says(e, name, action):
                a = (res.get((e, name)) or {}).get("answer") or {}
                return (a.get("actions") or {}).get(action, "error")

            # ---------------------------------------------------- decide with the intent of the route, then act
            intent = s.get("intent")
            tmap = {t["name"]: t for t in targets}
            rec = {"stop": k, "label": label, "type": s["type"], "kind": s["kind"], "map": map_name, "road_id": wp.road_id,
                   "lane_id": wp.lane_id, "s": round(wp.s, 1), "intent": intent, "drive_with": drive_with, "note": s.get("note", ""),
                   "xy": plan_rows[k - 1]["xy"], "targets": targets}
            plan, action, would_c, nav_do = None, "", "", ""
            if s["kind"] == "line":
                side, tg = s["side"], tmap["line"]
                nb = neighbour(wp, side)
                rel = neighbour_rel(wp, nb)
                rec.update(system_says=says(drive_with, "line", "cross_line"), truth=tg["truth"][drive_with]["cross_line"],
                           c_says=says("C", "line", "cross_line"), truth_c=tg["truth"]["C"]["cross_line"], neighbour=rel)
                go = rec["system_says"] == "allowed"
                if go and rel == "same":
                    plan, action = build_plan(wp, 45.0, shift=side), f"changes to the {side} lane"
                    nav_do = f"执行：向{'左' if side == 'left' else '右'}变道"
                elif go and rel == "opposite":
                    own, opp = lane_wps(wp, 64), lane_wps(nb, 64, same=False)
                    plan = ([w.transform.location for w in own[:2]] + [w.transform.location for w in opp[6:15]] +
                            [w.transform.location for w in own[19:]])
                    action, nav_do = "overtakes across the line and comes back", "执行：越过中心线超车，再回到本车道"
                elif go:
                    action = "would cross, but there is no lane on that side (median), so it stays"
                    nav_do = "B 说可以越线，但左侧是隔离带，没有车道可去"
                else:
                    action, nav_do = "does not cross, stays in its lane", "不越线，保持车道"
                would_c = "cross" if rec["c_says"] == "allowed" else "not cross"
                view.status = f"wants to {intent}: {drive_with} says {rec['system_says']} -> {action}"
            elif s["kind"] == "twltl":
                tg = tmap["centre"]
                rec.update(system_says=says(drive_with, "centre", "enter_center_lane_to_wait"),
                           truth=tg["truth"][drive_with]["enter_center_lane_to_wait"], c_says=says("C", "centre", "enter_center_lane_to_wait"),
                           truth_c=tg["truth"]["C"]["enter_center_lane_to_wait"])
                if rec["system_says"] == "allowed":
                    cen = wp.get_left_lane()
                    own, cl = lane_wps(wp, 70), lane_wps(cen, 70, same=(cen.lane_id > 0) == (wp.lane_id > 0))
                    plan = ([w.transform.location for w in own[:2]] + [w.transform.location for w in cl[5:16]] +
                            [w.transform.location for w in own[21:]])
                    action = "enters the centre lane to wait for a left turn, then (no driveway here) moves back"
                    nav_do = "执行：进入中心车道等待左转（此处没有可转入的路口，之后回到原车道）"
                else:
                    action, nav_do = "stays in its lane", "不进入中心车道"
                would_c = {"allowed": "enter", "prohibited": "not enter"}.get(rec["c_says"], rec["c_says"])
                view.status = f"wants to turn left soon: {drive_with} says enter centre lane {rec['system_says']} -> {action}"
            else:
                ta = tmap["arrow"]
                arrow_says = {m: says(drive_with, "arrow", m) for m in ("go_straight", "turn_left", "turn_right")}
                rec.update(system_says=arrow_says.get(intent), truth=ta["truth"][drive_with][intent],
                           c_says=says("C", "arrow", intent), truth_c=ta["truth"]["C"][intent])
                choice, shift = None, None
                if arrow_says.get(intent) == "allowed":
                    choice, action = intent, f"goes {SHORT[intent]}"
                    nav_do = f"执行：{CN_ACT[intent]}（与导航一致）"
                elif s["kind"] == "approach":
                    side = s.get("line_side", "right")
                    lt = tmap.get("line")
                    line_ok = says(drive_with, "line", "cross_line") == "allowed"
                    nbw = neighbour(wp, side)
                    nb_arrow = cache.get(f"{map_name}|arrow|{wp.road_id}|{nbw.lane_id if nbw else 0}", {})
                    nb_ok = ((nb_arrow.get(drive_with) or {}).get("answer") or {}).get("actions", {}).get(intent) == "allowed"
                    rec.update(line_says=says(drive_with, "line", "cross_line"), neighbour_arrow_allows=nb_ok,
                               line_truth=lt["truth"][drive_with]["cross_line"] if lt else None,
                               line_truth_c=lt["truth"]["C"]["cross_line"] if lt else None, line_c_says=says("C", "line", "cross_line"))
                    if line_ok and nb_ok:
                        choice, shift = intent, side
                        action = f"{SHORT[intent]} not allowed from this lane; the {side} line may be crossed -> changes lane, then goes {SHORT[intent]}"
                        nav_do = f"本车道不能{CN_ACT[intent]}；B 说右侧的线可以越过 → 先向右变道，再{CN_ACT[intent]}"
                    c_line = says("C", "line", "cross_line") == "allowed"
                    would_c = ("change lane, then " + SHORT[intent]) if (c_line and nb_ok) else "stay in lane and take the lane's own movement"
                if not choice:
                    choice = next((m for m in ("go_straight", "turn_right", "turn_left") if arrow_says.get(m) == "allowed"), None)
                    action = f"{SHORT[intent]} not allowed -> goes {SHORT.get(choice, 'nowhere')} instead and re-plans"
                    nav_do = f"导航要{CN_ACT[intent]}，B 说禁止 → 改为{CN_ACT.get(choice, '停车')}，到下一站的路线重新规划"
                if s["kind"] == "arrow":
                    would_c = SHORT[intent] if rec["c_says"] == "allowed" else "not " + SHORT[intent]
                plan = build_plan(wp, 70.0, choice=choice, shift=shift) if choice else []
                rec["choice"] = choice
                view.status = f"wants to go {SHORT[intent]}: {drive_with} says {arrow_says.get(intent)} -> {action}"
            rec.update(action=action, would_do_with_C=would_c, action_cn=nav_do)
            colour = {"allowed": (0, 200, 0), "prohibited": (230, 40, 40)}
            view.box_colours = {tg["name"]: colour.get(says(drive_with, tg["name"], RELEVANT[tg["kind"]][0] if tg["kind"] != "arrow" else (intent or "go_straight")),
                                                       (255, 200, 0)) for tg in targets}
            view.nav_lines = nav_header() + [("now", f"站点 {k}：导航意图 = {INTENT_CN.get(intent, intent)}"), ("now", nav_do),
                                             ("text", f"若按 C（中国规则）：{would_c}")]
            view.panel = verdict_panel(title, res, targets, 0.0) + [("title", "decision"), ("ok", view.status)]
            view.show(bgr, None, throttle=False)
            view.snapshot(out / "decisions" / f"{k:02d}.png")
            hold(2.5, bgr)
            for (e, name), r in res.items():
                tg = tmap[name]
                row = {kk: v for kk, v in r.items() if kk != "request"}
                row.update(stop=k, stop_label=label, target=name, kind=tg["kind"], experiment=e, box=tg["box"], cache_key=tg["cache_key"],
                           truth=tg["truth"][e])
                answers.append(row)
                if not r.get("reused") and r.get("answer") and not args.mock:
                    cache.setdefault(tg["cache_key"], {})[e] = {kk: v for kk, v in r.items() if kk not in ("trace",)}
            print(f"[stop {k}] {label}: " + "  ".join(
                f"{e}/{t['name']}:" + ",".join(f"{SHORT[x]}={says(e, t['name'], x)}" for x in RELEVANT[t['kind']]) +
                ("(reused)" if (res.get((e, t['name'])) or {}).get("reused") else "") for t in targets for e in "ABC") +
                f"  -> {view.status}", flush=True)

            mk["maneuver_start"] = frames()
            if plan:
                driver.set_plan(plan)
                nav["route"] = []
                view.nav_path = [(p.x, p.y) for p in plan]
                yaw0 = ego.get_transform().rotation.yaw
                state = {"in_j": False, "moved": None}

                def done():
                    w2 = cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Any)
                    if s["kind"] in ("arrow", "approach") and w2 is not None:
                        if w2.is_junction:
                            state["in_j"] = True
                        elif state["in_j"]:
                            state["moved"] = movement_of(yaw_delta(yaw0, ego.get_transform().rotation.yaw))
                            return "through the junction"
                    return None

                drive_plan(1200, done)
                rec["observed"] = state["moved"] if s["kind"] in ("arrow", "approach") else "maneuver driven"
            else:
                rec["observed"] = "kept its lane"
            view.nav_stops[k - 1]["done"] = True
            mk["maneuver_end"] = frames()
            markers.append(mk)
            records.append(rec)

        # ---------------------------------------------------- close the loop
        if not view.quit and stops and not args.preview:
            nav["stop"] = None
            view.status, view.boxes = "back to the start: the loop is closed", {}
            view.nav_lines = nav_header() + [("now", "导航：返回起点，完成一圈")]
            mk = {"stop": "loop", "drive_start": frames()}
            set_route(grp.trace_route(ego.get_location(), start_loc))
            drive_plan(6000, lambda: "home" if ego.get_location().distance(start_loc) < 6 else None)
            mk["drive_end"] = frames()
            markers.append(mk)
    finally:
        try:
            for name, rows in (("answers.jsonl", answers), ("stops.jsonl", records)):
                with open(out / name, "w", encoding="utf-8") as f:
                    for r in rows:
                        f.write(json.dumps(r, ensure_ascii=False, default=str) + "\n")
            (out / "markers.json").write_text(json.dumps(markers, indent=1), encoding="utf-8")
            lanes2 = [[round(w.transform.location.x, 1), round(w.transform.location.y, 1)] for w in cmap.generate_waypoints(4.0)
                      if w.lane_type == carla.LaneType.Driving]
            (out / "route.json").write_text(json.dumps({"track": track, "lanes": lanes2, "stops": [
                {"stop": r["stop"], "label": r["label"], "xy": r["xy"]} for r in plan_rows]}), encoding="utf-8")
            s = summarize(answers, records, meta)
            (out / "summary.json").write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")
            write_reasoning(out / "reasoning.md", answers, records, meta)
            if not args.mock and not args.preview:
                cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
            print(json.dumps(s["per_experiment"], indent=1), flush=True)
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


def summarize(answers, records, meta):
    per = {}
    for e in "ABC":
        rows = [a for a in answers if a["experiment"] == e]
        d = {"answers": len(rows), "asked_now": sum(1 for a in rows if not a.get("reused")),
             "reused": sum(1 for a in rows if a.get("reused")), "cost_usd": round(sum(a.get("cost", 0) for a in rows), 4),
             "output1_correct": 0, "output2_scored": 0, "output2_correct": 0, "unsafe": 0, "over_cautious": 0,
             "contested_disagree": 0, "unscored_cells": 0, "citations": {}, "wrong": []}
        for a in rows:
            sc = a.get("score") or {}
            d["output1_correct"] += bool(sc.get("output1"))
            if sc.get("output2") is not None:
                d["output2_scored"] += 1
                d["output2_correct"] += bool(sc["output2"])
            d["unsafe"] += len(sc.get("unsafe") or [])
            d["over_cautious"] += len(sc.get("over_cautious") or [])
            d["contested_disagree"] += sum(1 for ok in (sc.get("contested") or {}).values() if not ok)
            d["unscored_cells"] += sum(1 for x in RELEVANT[a["kind"]] if a["truth"][x] == "undecided")
            if sc.get("citation"):
                d["citations"][sc["citation"]] = d["citations"].get(sc["citation"], 0) + 1
            for x, ok in (sc.get("actions") or {}).items():
                if not ok:
                    got = ((a.get("answer") or {}).get("actions") or {}).get(x)
                    d["wrong"].append(f"stop {a['stop']} {a['label']} / {a['target']}: {x} said {got}, label {a['truth'][x]}"
                                      + (" (contested cell)" if x in (sc.get("contested") or {}) else ""))
        per[e] = d
    loop = {"stops": len(records),
            "intent_prohibited": sum(1 for r in records if r.get("truth") == "prohibited"),
            "prohibited_intent_blocked": sum(1 for r in records if r.get("truth") == "prohibited" and r.get("system_says") != "allowed"),
            "prohibited_intent_allowed": sum(1 for r in records if r.get("truth") == "prohibited" and r.get("system_says") == "allowed")}
    return {"meta": meta, "per_experiment": per, "closed_loop": loop,
            "cost_usd": round(sum(v["cost_usd"] for v in per.values()), 4)}


def write_reasoning(path, answers, records, meta):
    L = [f"# Reasoning at every stop: {meta['route']} on {meta['map']}", "",
         f"Model {meta['model']}, reasoning effort {meta['reasoning_effort']}, prompt {meta['prompt']}. "
         "A = Test A US; B = Test B US (MUTCD); C = Test B with the China passages on the same US road.", ""]
    for r in records:
        L += [f"## Stop {r['stop']}: {r['label']}", "",
              f"Road {r.get('road_id')} lane {r.get('lane_id')}. Intent from the route: {r.get('intent')}. "
              f"The car ({r.get('drive_with')}): {r.get('action')}. With C it would: {r.get('would_do_with_C')}.", ""]
        for a in [a for a in answers if a["stop"] == r["stop"]]:
            L += [f"### {EXP_LABEL[a['experiment']]}, {a['target']}" + ("  (earlier answer, reused)" if a.get("reused") else ""), "",
                  "```", a.get("trace") or a.get("error") or "", "```", ""]
    path.write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
