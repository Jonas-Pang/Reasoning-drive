"""The same map and the same places, asked and driven as four countries: the United States, China, the United Kingdom and
Japan (configs/carla.yaml, under countries).

For every country and every scene the car drives to the place, stops, and the camera photo goes to the project's lane
task (prompt folder lane_v2 by default) twice: Test A (the photo and the country) and Test B (the photo, the country and
the country's rule passages). The car then does what the navigation intent asks only if the Test B answer allows it,
and drives on, so the answer decides what happens next (closed loop). What Test A would have done is recorded.

Left-hand traffic: the CARLA towns are right-hand traffic. For a left-hand country the photo is flipped left to right
before it is sent (a mirror world: the car keeps to the left, a left-turn arrow becomes a right-turn arrow), the answer's
left and right are flipped back to drive, and the video shows that country's drive flipped too. The countries'
passages may still be drafts (regulations/<CODE>/passages_draft.yaml); this is said in the results.

    python main.py carla countries [--countries US,CN,UK,JP] [--scenes lane_change,arrow_lane] [--mock]
    python main.py carla countries-video results/carla/<run>

Every run folder holds, per country and scene, the photos (as taken and as sent), the camera frames of the drive (front
and chase), the answers (answers.jsonl), the reasoning of each answer (traces), the full prompts (prompts.md) and the
results (results.json, summary.md). Answers already given for the same photo and prompt come from the project's cache.
"""
from __future__ import annotations

import argparse
import json
import math
import queue
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from .. import paths as P
from .settings import load_settings

VAL_CN = {"allowed": "允许", "prohibited": "禁止", "not_determined": "无法确定", "not_applicable": "不适用"}
ACT_CN = {"change_left": "向左变道", "change_right": "向右变道", "go_straight": "直行", "turn_left": "左转", "turn_right": "右转",
          "u_turn": "掉头", "enter_waiting_area": "进入待转区"}
SWAP = {"change_left": "change_right", "change_right": "change_left", "turn_left": "turn_right", "turn_right": "turn_left"}
SIDE = {"change_left": "left", "change_right": "right"}
DEFAULT_SCENES = {
    "lane_change": {"label": "solid white line between two lanes of my direction, double yellow centre line on the other side",
                    "road": 20, "lane": 1, "s": 126.6, "intent": "change_right", "intent_text": "change to the right lane"},
    "arrow_lane": {"label": "left-turn arrow in my lane, solid white line to the lane on the right", "road": 44, "lane": -4, "s": 9.0,
                   "intent": "turn_right", "intent_text": "turn right at the junction"}}


def flip(action: str, mirror: bool) -> str:
    return SWAP.get(action, action) if mirror else action


def in_picture(actions: dict, mirror: bool) -> dict:
    """The answer is about the photo as sent; for a mirrored country the car's left and right are the other way round."""
    return {flip(k, mirror): v for k, v in (actions or {}).items()}


def decide(intent: str, acts: dict) -> dict:
    """What the car does with an answer's actions (all in the frame of the photo the model saw).
    change_<side>: change lanes if allowed, else stay. turn_<dir>: turn if allowed from this lane; else change lanes towards
    that side first if allowed; else take the movement this lane allows."""
    acts = acts or {}
    ok = lambda a: acts.get(a) == "allowed"  # noqa: E731
    v = lambda a: VAL_CN.get(acts.get(a), "无答案")  # noqa: E731
    if intent in SIDE:
        if ok(intent):
            return {"shift": SIDE[intent], "choice": None, "text": f"{intent.replace('_', ' ')} (allowed)",
                    "text_cn": f"{ACT_CN[intent]}（允许）", "does_intent": True}
        return {"shift": None, "choice": None, "text": f"stays in its lane ({intent.replace('_', ' ')}: {acts.get(intent, 'no answer')})",
                "text_cn": f"保持本车道（{ACT_CN[intent]}：{v(intent)}）", "does_intent": False}
    side = "right" if intent.endswith("right") else "left"
    ch = f"change_{side}"
    if ok(intent):
        return {"shift": None, "choice": intent, "text": f"{intent.replace('_', ' ')} from this lane (allowed)",
                "text_cn": f"从本车道{ACT_CN[intent]}（允许）", "does_intent": True}
    if ok(ch):
        return {"shift": side, "choice": intent, "text": f"{intent.replace('_', ' ')} not allowed from this lane; changes to the {side} "
                f"lane first (allowed), then turns", "text_cn": f"本车道不能{ACT_CN[intent]}（{v(intent)}），先{ACT_CN[ch]}（允许），"
                f"再{ACT_CN[intent]}", "does_intent": True}
    other = next((a for a in ("go_straight", "turn_left", "turn_right") if ok(a)), None)
    return {"shift": None, "choice": other, "text": f"{intent.replace('_', ' ')}: {acts.get(intent, 'no answer')}, {ch}: "
            f"{acts.get(ch, 'no answer')} -> follows the lane" + (f" ({other.replace('_', ' ')})" if other else ""),
            "text_cn": f"{ACT_CN[intent]}：{v(intent)}，{ACT_CN[ch]}：{v(ch)} → 按本车道走" + (f"（{ACT_CN[other]}）" if other else ""),
            "does_intent": False}


def to_car(dec: dict, mirror: bool) -> dict:
    """A decision in the photo's frame, as the car in the (right-hand) CARLA world must drive it."""
    if not mirror:
        return dec
    other = {"left": "right", "right": "left"}
    return dict(dec, shift=other.get(dec["shift"]), choice=flip(dec["choice"], True) if dec["choice"] else None)


def setup(repo: Path, prompt: str, mock: bool, summary: str | None):
    from .. import config as C
    cfg = C.load(repo, drafts=True)
    cfg["mock"] = mock
    cfg["lane"]["prompt_dir"] = f"prompts/{prompt}"
    if summary:
        cfg["api"]["reasoning_summary"] = summary
    if not mock and not C.api_key(cfg):
        raise SystemExit("No OPENAI_API_KEY in .env. Add it, or run with --mock.")
    return cfg


def prompts_text(cfg: dict, countries: list[str], tests: list[str]) -> tuple[str, dict]:
    """The full prompts: the developer message, the user message and the answer schema of every country and test."""
    from ..agent import lane as L
    lc = L.lane_cfg(cfg)
    parts = {(c, t): L.lane_prompt_parts(lc, t, c) for c in countries for t in tests}
    lines = [f"# The prompts ({cfg['lane']['prompt_dir']})", ""]
    for (c, t), p in parts.items():
        rc = cfg["regions"][c]
        lines += [f"## {rc['name']} ({c}), Test {t}" + (" - passages from the DRAFT" if rc.get("draft") and t == "B" else ""), "",
                  "### Developer message (instructions)", "", "```", p["instructions"], "```", "",
                  "### User message (followed by the photo)", "", "```", p["user_text"], "```", ""]
    first = next(iter(parts.values()))
    lines += ["## Answer schema (structured output, the same for every country and test)", "", "```json",
              json.dumps(first["schema"], indent=1, ensure_ascii=False), "```", ""]
    return "\n".join(lines), {f"{c}|{t}": {"instructions": p["instructions"], "user_text": p["user_text"],
                                          "rules_block": p["rules_block"], "hashes": p["hashes"]} for (c, t), p in parts.items()}


def main(argv=None):
    import carla
    from ..agent import lane as L
    from ..agent.runner import cost_of
    from ..imageio import imwrite
    from .loop import CAM_X, CAM_Z, FOV, H, W
    from .scenarios import Driver, build_plan, movement_of, yaw_delta
    from .settings import add_agents_path

    settings = load_settings(P.REPO)
    conf = settings.get("countries") or {}
    srv = settings.get("server") or {}
    ap = argparse.ArgumentParser(prog="python main.py carla countries")
    ap.add_argument("--countries", default=",".join(conf.get("countries") or ["US", "CN", "UK", "JP"]))
    ap.add_argument("--scenes", default=",".join(conf.get("scenes") or DEFAULT_SCENES))
    ap.add_argument("--prompt", default=conf.get("prompt", "lane_v2"))
    ap.add_argument("--repo", default=str(P.REPO))
    ap.add_argument("--host", default=srv.get("host", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(srv.get("port", 2000)))
    ap.add_argument("--mock", action="store_true")
    args = ap.parse_args(argv)

    repo = Path(args.repo)
    cfg = setup(repo, args.prompt, args.mock, conf.get("reasoning_summary", "auto"))
    scenes_cfg = {**DEFAULT_SCENES, **(conf.get("scenes") if isinstance(conf.get("scenes"), dict) else {})}
    countries = [c.strip() for c in args.countries.split(",") if c.strip()]
    scenes = [s.strip() for s in args.scenes.split(",") if s.strip()]
    for c in countries:
        if c not in cfg["regions"]:
            raise SystemExit(f"No country {c} (regulations/{c}/ needs passages, accepted or a draft).")
    tests, drive_with = list(conf.get("tests") or ["A", "B"]), conf.get("drive_with", "B")
    approach = float(conf.get("approach_m", 40.0))

    client = carla.Client(args.host, args.port)
    client.set_timeout(float(srv.get("timeout_s", 120)))
    world = client.get_world()
    cmap = world.get_map()
    map_name = cmap.name.split("/")[-1].replace("_Opt", "")
    if conf.get("map") and map_name != conf["map"]:
        raise SystemExit(f"The scenes are on {conf['map']}; the server runs {map_name} (python main.py carla map {conf['map']}_Opt, "
                         "then start CARLA again).")
    world.set_weather(getattr(carla.WeatherParameters, conf.get("weather", "ClearNoon")))
    version = client.get_server_version()
    add_agents_path(settings)
    try:
        from agents.navigation.global_route_planner import GlobalRoutePlanner
        grp = GlobalRoutePlanner(cmap, 2.0)
    except Exception as e:  # noqa: BLE001
        print(f"route planner not available ({e}); turns follow the lane graph only", flush=True)
        grp = None
    DRIVABLE = (carla.LaneType.Driving, carla.LaneType.Bidirectional)
    SIDE_OK = DRIVABLE + (carla.LaneType.Parking, carla.LaneType.Shoulder, carla.LaneType.Border)

    def neighbour(wp, side):
        return wp.get_right_lane() if side == "right" else wp.get_left_lane()

    def offset_plan(wp, side, width, length=60.0, start=4.0, ramp=14.0):
        """Points along my lane that move sideways by one lane width (a lane change into a lane the map does not mark as a
        driving lane, e.g. a parking lane, which the photo shows as a lane)."""
        pts, cur, s_ = [], wp, 0.0
        sign = 1.0 if side == "right" else -1.0
        while s_ < length:
            n = cur.next(2.0)
            if not n:
                break
            cur, s_ = n[0], s_ + 2.0
            f = 0.0 if s_ < start else min(1.0, (s_ - start) / ramp)
            rv = cur.transform.get_right_vector()
            pts.append(cur.transform.location + carla.Location(rv.x * width * f * sign, rv.y * width * f * sign, 0.0))
        return pts

    def junction_exit(wp, movement):
        """The exit of the next junction that the movement leads to, from the entries in my driving direction near wp."""
        cur = wp
        for _ in range(60):
            n = cur.next(2.0)
            if not n:
                return None
            cur = n[0]
            if cur.is_junction:
                break
        else:
            return None
        yaw0, best = wp.transform.rotation.yaw, None
        for a, b in cur.get_junction().get_waypoints(carla.LaneType.Driving):
            if abs(yaw_delta(yaw0, a.transform.rotation.yaw)) > 35:
                continue
            d = a.transform.location.distance(cur.transform.location)
            if d > 12.0:
                continue
            mv = movement_of(yaw_delta(a.transform.rotation.yaw, b.transform.rotation.yaw))
            if mv == movement and (best is None or d < best[0]):
                best = (d, b)
        return best[1] if best else None

    def manoeuvre(wp, car):
        """Points for the decision (car frame) and a note on how it was driven."""
        shift, choice = car.get("shift"), car.get("choice")
        start, pts, note = wp, [], ""
        if shift:
            nb = neighbour(wp, shift)
            if nb is not None and nb.lane_type in DRIVABLE:
                head = [p for p in (wp.next(2.0)[:1] + wp.next(4.0)[:1])]
                ahead = nb.next(12.0) if (nb.lane_id > 0) == (wp.lane_id > 0) else nb.previous(12.0)
                start = ahead[0] if ahead else nb
                pts = [h.transform.location for h in head] + [start.transform.location]
                note = f"lane change into the {shift} lane"
            elif nb is not None and nb.lane_type in SIDE_OK:
                pts = offset_plan(wp, shift, nb.lane_width or 3.0)
                note = f"lane change into the {shift} lane (the map calls it {nb.lane_type}; the photo shows a lane)"
                return pts, note
            else:
                note = f"no lane on the {shift} side in the map; stays"
        if choice and grp is not None:
            ex = junction_exit(start, choice)
            if ex is not None:
                dest = ex.next(15.0)
                dest = dest[0] if dest else ex
                route = grp.trace_route(start.transform.location, dest.transform.location)
                if route and len(route) < 120:
                    return pts + [w.transform.location for w, _ in route], (note + "; " if note else "") + f"{choice.replace('_', ' ')} at the junction"
            note = (note + "; " if note else "") + f"no {choice.replace('_', ' ')} exit found, follows the lane"
        if pts:
            return pts + build_plan(start, 60.0, choice=choice), note
        return build_plan(wp, 70.0, choice=choice, shift=None), note or "follows its lane"

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = repo / settings.get("output", "results/carla") / f"{stamp}_countries{'_mock' if args.mock else ''}"
    out.mkdir(parents=True, exist_ok=True)
    text, parts = prompts_text(cfg, countries, tests)
    (out / "prompts.md").write_text(text, encoding="utf-8")
    (out / "prompts.json").write_text(json.dumps(parts, indent=1, ensure_ascii=False), encoding="utf-8")
    lc = L.lane_cfg(cfg)
    pmaps = {}
    for c in countries:
        try:
            pmaps[c] = {p["rule_id"]: p for p in L.lane_passages(lc, c)}
        except Exception:  # noqa: BLE001
            pmaps[c] = {}
    meta = {"map": map_name, "carla_server": version, "carla_client": getattr(carla, "__version__", ""), "weather": conf.get("weather", "ClearNoon"),
            "prompt": cfg["lane"]["prompt_dir"], "model": cfg["api"]["model"], "reasoning_effort": cfg["api"].get("reasoning_effort"),
            "tests": tests, "drive_with": drive_with, "mock": args.mock, "started": stamp,
            "countries": {c: {"name": cfg["regions"][c]["name"], "driving_side": cfg["regions"][c]["driving_side"],
                              "mirrored": cfg["regions"][c]["driving_side"] == "left", "draft_passages": bool(cfg["regions"][c].get("draft")),
                              "passages": len(pmaps[c])} for c in countries},
            "scenes": {s: scenes_cfg[s] for s in scenes}}
    print(f"CARLA server {version}, map {map_name}; countries {countries}; scenes {scenes}", flush=True)

    original = world.get_settings()
    st = world.get_settings()
    st.synchronous_mode, st.fixed_delta_seconds = True, 0.05
    world.apply_settings(st)
    lib = world.get_blueprint_library()
    actors, records = [], []
    pool = ThreadPoolExecutor(max_workers=4)
    try:
        first = cmap.get_waypoint_xodr(scenes_cfg[scenes[0]]["road"], scenes_cfg[scenes[0]]["lane"], scenes_cfg[scenes[0]]["s"])
        ego = world.try_spawn_actor(lib.find("vehicle.tesla.model3"), carla.Transform(
            first.transform.location + carla.Location(z=0.5), first.transform.rotation)) or world.spawn_actor(
            lib.find("vehicle.tesla.model3"), cmap.get_spawn_points()[0])
        actors.append(ego)
        cams, qs = {}, {}
        for name, (w, h, tf) in {"front": (W, H, carla.Transform(carla.Location(x=CAM_X, z=CAM_Z))),
                                 "chase": (960, 540, carla.Transform(carla.Location(x=-6.5, z=3.2), carla.Rotation(pitch=-13)))}.items():
            bp = lib.find("sensor.camera.rgb")
            for k, v in (("image_size_x", w), ("image_size_y", h), ("fov", FOV)):
                bp.set_attribute(k, str(v))
            cams[name] = world.spawn_actor(bp, tf, attach_to=ego)
            qs[name] = queue.Queue()
            cams[name].listen(qs[name].put)
            actors.append(cams[name])
        driver = Driver(ego, speed=7.0)
        import cv2
        import numpy as np

        def tick(store=None, k=[0]):
            driver.step()
            fr = world.tick()
            imgs = {}
            for name, q in qs.items():
                img = q.get(timeout=10.0)
                while img.frame < fr:
                    img = q.get(timeout=10.0)
                imgs[name] = np.ascontiguousarray(np.frombuffer(img.raw_data, dtype=np.uint8).reshape((img.height, img.width, 4))[:, :, :3])
            k[0] += 1
            if store is not None and k[0] % 2 == 0:  # 10 frames a second
                n = len(store["frames"])
                for name, im in imgs.items():
                    cv2.imwrite(str(store["dir"] / f"{name}_{n:05d}.jpg"), im, [cv2.IMWRITE_JPEG_QUALITY, 85])
                store["frames"].append(round(math.hypot(ego.get_velocity().x, ego.get_velocity().y), 2))
            return imgs

        def place(tf):
            ego.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0))
            ego.set_target_velocity(carla.Vector3D(0, 0, 0))
            ego.set_transform(carla.Transform(tf.location + carla.Location(z=0.3), tf.rotation))
            driver.set_plan([])
            for _ in range(15):
                tick()

        def lane_points(wp, metres, step=2.0):
            pts, cur = [], wp
            for _ in range(int(metres / step)):
                n = cur.next(step)
                if not n:
                    break
                cur = n[0]
                pts.append(cur.transform.location)
            return pts

        for c in countries:
            info = meta["countries"][c]
            mirror = info["mirrored"]
            for sname in scenes:
                sc = scenes_cfg[sname]
                D = cmap.get_waypoint_xodr(sc["road"], sc["lane"], sc["s"])
                if D is None:
                    print(f"{c} {sname}: no waypoint road {sc['road']} lane {sc['lane']} s {sc['s']} on {map_name}; left out", flush=True)
                    continue
                d = out / c / sname
                d.mkdir(parents=True, exist_ok=True)
                approach_store = {"dir": d, "frames": []}
                back = D.previous(approach)
                place((back[0] if back else D).transform)
                driver.set_plan(lane_points(back[0] if back else D, approach) + [D.transform.location])
                driver.speed = 7.0
                t0 = len(approach_store["frames"])
                for n_tick in range(1200):
                    tick(approach_store)
                    loc, dl = ego.get_location(), D.transform.location
                    still = math.hypot(ego.get_velocity().x, ego.get_velocity().y) < 0.3
                    if n_tick > 40 and still and (loc.distance(dl) < 4.5 or driver.i >= len(driver.plan) - 1):
                        break
                    if loc.distance(dl) < 8.0:
                        driver.speed = 2.5
                for _ in range(10):
                    tick(approach_store)
                imgs = tick(approach_store)
                photo = imgs["front"]
                imwrite(str(d / "photo.png"), photo)
                sent = cv2.flip(photo, 1) if mirror else photo
                imwrite(str(d / "photo_sent.png"), sent)
                stop_frame = len(approach_store["frames"])
                item = L.LaneItem(f"carla_{map_name}_{sname}{'_mirrored' if mirror else ''}", "carla", c, "carla", "sim",
                                  d / "photo_sent.png", W, H, {})
                t_ask = time.time()
                futs = {t: pool.submit(L.ask_lane, cfg, item, t, args.mock, True) for t in tests}
                recs = {t: f.result() for t, f in futs.items()}
                ask_s = round(time.time() - t_ask, 1)
                acts = {t: ((r.get("answer") or {}).get("actions") or {}) for t, r in recs.items()}
                intent_pic = flip(sc["intent"], mirror)
                decisions = {t: decide(intent_pic, acts[t]) for t in tests}
                dec = decisions[drive_with]
                car = to_car(dec, mirror)
                wp = cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Driving)
                pts, how = manoeuvre(wp, car)
                driver.set_plan(pts)
                driver.speed = 6.0
                act_from = len(approach_store["frames"])
                for _ in range(260):
                    tick(approach_store)
                    if driver.i >= len(driver.plan) - 2:
                        break
                end_wp = cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Driving)
                cost = sum(cost_of(cfg, (r.get("response") or {}).get("usage") or {}, (r.get("response") or {}).get("model"))
                           for r in recs.values() if r.get("response") and not r.get("cached") and not r.get("mock"))
                rec = {"country": c, "scene": sname, "mirrored": mirror, "label": sc["label"], "intent": sc["intent"],
                       "intent_text": sc.get("intent_text", sc["intent"]), "intent_in_photo": intent_pic,
                       "road": D.road_id, "lane": D.lane_id, "s": round(D.s, 1), "frames": len(approach_store["frames"]),
                       "first_frame": t0, "stop_frame": stop_frame, "act_frame": act_from, "ask_seconds": ask_s,
                       "actions": acts, "decisions": decisions, "drove": dec, "car": car, "manoeuvre": how,
                       "end": {"road": end_wp.road_id, "lane": end_wp.lane_id} if end_wp else None,
                       "cost_usd": round(cost, 4), "cached": {t: bool(r.get("cached")) for t, r in recs.items()},
                       "errors": {t: r.get("error") or r.get("parse_error") or "" for t, r in recs.items()}}
                records.append(rec)
                with open(out / "answers.jsonl", "a", encoding="utf-8") as f:
                    for t, r in recs.items():
                        f.write(json.dumps(dict(r, country=c, scene=sname, mirrored=mirror), ensure_ascii=False) + "\n")
                for t, r in recs.items():
                    (d / f"trace_{t}.txt").write_text(L.lane_trace_text(r, pmaps[c]), encoding="utf-8")
                print(f"{c} {sname}: A {acts.get('A', {})} | B {acts.get('B', {})} -> {dec['text']} [{how}; ends on road "
                      f"{rec['end']}]  (${rec['cost_usd']}, {ask_s} s)", flush=True)
        (out / "results.json").write_text(json.dumps({"meta": meta, "records": records}, indent=1, ensure_ascii=False), encoding="utf-8")
        (out / "summary.md").write_text(summary_md(meta, records), encoding="utf-8")
        print(f"Saved in {out}", flush=True)
    finally:
        world.apply_settings(original)
        for a in reversed(actors):
            try:
                if hasattr(a, "stop"):
                    a.stop()
                a.destroy()
            except Exception:  # noqa: BLE001
                pass
        pool.shutdown(wait=False)


SHORT = {"allowed": "yes", "prohibited": "NO", "not_determined": "?", "not_applicable": "-"}


def summary_md(meta: dict, records: list[dict]) -> str:
    lines = [f"# Same map, four countries ({meta['map']}, CARLA {meta.get('carla_server', '')})", "",
             f"Prompt {meta['prompt']}, model {meta['model']}, tests {', '.join(meta['tests'])}, the car drives with Test {meta['drive_with']}"
             + (" (MOCK ANSWERS)" if meta["mock"] else "") + ".", "",
             "Left-hand countries see the photo flipped left to right (mirror world); the actions below are as in the photo they saw.", "",
             "| Country | Scene | Intent (in the photo) | Test A: change_left / change_right / turn_left / turn_right | Test B: same | The car (Test B) | A would |",
             "|---|---|---|---|---|---|---|"]
    for r in records:
        f = lambda a: " / ".join(SHORT.get(a.get(x), str(a.get(x) or "")) for x in ("change_left", "change_right", "turn_left", "turn_right"))  # noqa: E731
        lines.append(f"| {r['country']}{' (mirrored)' if r['mirrored'] else ''} | {r['scene']} | {r['intent_in_photo']} | "
                     f"{f(r['actions'].get('A', {}))} | {f(r['actions'].get('B', {}))} | {r['drove']['text']} | "
                     f"{(r['decisions'].get('A') or {}).get('text', '')} |")
    lines += ["", f"Cost about ${sum(r['cost_usd'] for r in records):.4f}."]
    for c, i in meta["countries"].items():
        if i["draft_passages"]:
            lines.append(f"{c}: the passages are a draft that has not been reviewed.")
    return "\n".join(lines) + "\n"
