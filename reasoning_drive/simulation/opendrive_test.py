"""An OpenDRIVE road in CARLA's standalone mode, once as right-hand traffic and once as left-hand traffic (CARLA 0.9.16
reads the road attribute rule="LHT"). It answers two questions before a left-hand map is used for the lane task:
does the generated road show its lane markings in the camera, and do the Traffic Manager's cars keep to the side the
road says? If the markings are missing, the same lines are drawn on the road with the debug helper and photographed
again, to see whether that is a usable substitute.

    python main.py carla opendrive-test            writes results/carla/<time>_opendrive/ (photos, info.json)

The road: 300 m straight, two lanes each way and a sidewalk on both sides; a double solid yellow centre line; between
the two lanes of each direction a solid white line for the first 150 m and a broken one after; solid white edge lines.
Loading an OpenDRIVE world replaces the running map: start CARLA again afterwards for the towns.
"""
from __future__ import annotations

import argparse
import json
import queue
import time
from datetime import datetime

from .. import paths as P
from .settings import load_settings


def xodr(rule: str, length: float = 300.0, split: float = 150.0) -> str:
    """The test road as an OpenDRIVE 1.5 string (rule RHT or LHT)."""
    def lane(i, typ, width, marks):
        rm = "".join(f'<roadMark sOffset="{s}" type="{t}" weight="standard" color="{c}" width="0.15" laneChange="{lc}"/>' for s, t, c, lc in marks)
        return (f'<lane id="{i}" type="{typ}" level="false"><link/><width sOffset="0" a="{width}" b="0" c="0" d="0"/>{rm}</lane>')
    inner = [(0, "solid", "white", "none"), (split, "broken", "white", "both")]
    edge = [(0, "solid", "white", "none")]
    none = [(0, "none", "standard", "none")]
    left = lane(3, "sidewalk", 2.0, none) + lane(2, "driving", 3.5, edge) + lane(1, "driving", 3.5, inner)
    right = lane(-1, "driving", 3.5, inner) + lane(-2, "driving", 3.5, edge) + lane(-3, "sidewalk", 2.0, none)
    centre = '<lane id="0" type="none" level="false"><link/><roadMark sOffset="0" type="solid solid" weight="standard" color="yellow" width="0.15" laneChange="none"/></lane>'
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<OpenDRIVE>
  <header revMajor="1" revMinor="5" name="lane_test_{rule}" version="1.0" north="0" south="0" east="0" west="0"/>
  <road name="test" length="{length}" id="1" junction="-1" rule="{rule}">
    <link/>
    <type s="0" type="town"><speed max="50" unit="km/h"/></type>
    <planView><geometry s="0" x="0" y="0" hdg="0" length="{length}"><line/></geometry></planView>
    <elevationProfile><elevation s="0" a="0" b="0" c="0" d="0"/></elevationProfile>
    <lateralProfile/>
    <lanes>
      <laneOffset s="0" a="0" b="0" c="0" d="0"/>
      <laneSection s="0">
        <left>{left}</left>
        <center>{centre}</center>
        <right>{right}</right>
      </laneSection>
    </lanes>
    <objects/>
    <signals/>
  </road>
</OpenDRIVE>
"""


def main(argv=None):
    import carla
    import cv2
    import numpy as np
    from .loop import CAM_X, CAM_Z, FOV, H, W

    settings = load_settings(P.REPO)
    srv = settings.get("server") or {}
    ap = argparse.ArgumentParser(prog="python main.py carla opendrive-test")
    ap.add_argument("--rules", default="RHT,LHT")
    ap.add_argument("--traffic", action="store_true", help="also let Traffic Manager cars drive (synchronous mode)")
    ap.add_argument("--host", default=srv.get("host", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(srv.get("port", 2000)))
    args = ap.parse_args(argv)
    out = P.REPO / settings.get("output", "results/carla") / f"{datetime.now():%Y%m%d_%H%M%S}_opendrive"
    out.mkdir(parents=True, exist_ok=True)
    client = carla.Client(args.host, args.port)
    client.set_timeout(300.0)
    w0 = client.get_world()
    st0 = w0.get_settings()
    if st0.synchronous_mode:  # a client that stopped in synchronous mode leaves the server waiting for ticks
        st0.synchronous_mode, st0.fixed_delta_seconds = False, None
        w0.apply_settings(st0)
    info = {"server": client.get_server_version(), "client": getattr(carla, "__version__", ""), "rules": {}}
    for rule in [r.strip() for r in args.rules.split(",") if r.strip()]:
        text = xodr(rule)
        (out / f"road_{rule}.xodr").write_text(text, encoding="utf-8")
        t0 = time.time()
        world = client.generate_opendrive_world(text, carla.OpendriveGenerationParameters(
            vertex_distance=2.0, max_road_length=50.0, wall_height=0.0, additional_width=0.6, smooth_junctions=True,
            enable_mesh_visibility=True))
        res = {"load_s": round(time.time() - t0, 1), "lanes": {}, "cars": [], "photos": []}
        cmap = world.get_map()
        for lid in (2, 1, -1, -2):
            wp = cmap.get_waypoint_xodr(1, lid, 60.0)
            if wp is None:
                continue
            nxt = wp.next(5.0)
            dx = (nxt[0].transform.location.x - wp.transform.location.x) if nxt else 0.0
            res["lanes"][lid] = {"travels": "+x" if dx > 0 else "-x", "yaw": round(wp.transform.rotation.yaw, 1),
                                 "left_marking": f"{wp.left_lane_marking.color} {wp.left_lane_marking.type}",
                                 "right_marking": f"{wp.right_lane_marking.color} {wp.right_lane_marking.type}",
                                 "lane_change": str(wp.lane_change)}
        original = world.get_settings()
        tm = client.get_trafficmanager() if args.traffic else None
        if args.traffic:
            st = world.get_settings()
            st.synchronous_mode, st.fixed_delta_seconds = True, 0.05
            world.apply_settings(st)
            tm.set_synchronous_mode(True)

        def step():
            if args.traffic:
                world.tick()
            else:
                world.wait_for_tick()
        lib = world.get_blueprint_library()
        actors = []
        try:
            for sp in (cmap.get_spawn_points()[:6] if args.traffic else []):
                car = world.try_spawn_actor(lib.find("vehicle.audi.a2"), sp)
                if car:
                    car.set_autopilot(True, tm.get_port())
                    actors.append(car)
            for _ in range(200 if args.traffic else 0):
                step()
            for car in actors:
                loc, v = car.get_location(), car.get_velocity()
                wp = cmap.get_waypoint(loc)
                res["cars"].append({"lane": wp.lane_id if wp else None, "x": round(loc.x, 1), "y": round(loc.y, 1),
                                    "moving": "+x" if v.x > 0.3 else ("-x" if v.x < -0.3 else "stopped")})
            # photos from a car in the lane that travels in +x on the left (LHT) or right (RHT) of the centre line
            lid = next((k for k, v in res["lanes"].items() if v["travels"] == "+x" and abs(int(k)) == 1), -1)
            tf0 = cmap.get_waypoint_xodr(1, int(lid), 20.0).transform
            if res["lanes"][lid]["travels"] == "-x":
                tf0.rotation.yaw += 180
            ego = world.spawn_actor(lib.find("vehicle.tesla.model3"), carla.Transform(tf0.location + carla.Location(z=0.6), tf0.rotation))
            actors.append(ego)
            bp = lib.find("sensor.camera.rgb")
            for k, v in (("image_size_x", W), ("image_size_y", H), ("fov", FOV)):
                bp.set_attribute(k, str(v))
            cam = world.spawn_actor(bp, carla.Transform(carla.Location(x=CAM_X, z=CAM_Z)), attach_to=ego)
            actors.append(cam)
            q = queue.Queue()
            cam.listen(q.put)

            def shot(name, s):
                wp = cmap.get_waypoint_xodr(1, int(lid), s)
                tf = wp.transform
                if res["lanes"][lid]["travels"] == "-x":
                    tf.rotation.yaw += 180
                ego.set_transform(carla.Transform(tf.location + carla.Location(z=0.6), tf.rotation))
                for _ in range(10):
                    step()
                img = q.get(timeout=10)
                while not q.empty():
                    img = q.get()
                bgr = np.frombuffer(img.raw_data, dtype=np.uint8).reshape((img.height, img.width, 4))[:, :, :3]
                path = out / f"{rule}_{name}.png"
                cv2.imwrite(str(path), bgr)
                res["photos"].append(path.name)

            shot("solid_section", 60.0)
            shot("broken_section", 190.0)
            # the same lines drawn with the debug helper (stays until the world is replaced)
            dbg = world.debug
            white, yellow = carla.Color(240, 240, 240), carla.Color(230, 190, 20)
            z = 0.03
            for k in range(0, 300, 1):
                a, b = carla.Location(k, 0, z), carla.Location(k + 1, 0, z)
                for off in (-0.12, 0.12):
                    dbg.draw_line(carla.Location(a.x, off, z), carla.Location(b.x, off, z), thickness=0.1, color=yellow, life_time=0.0)
            for y in (-3.5, 3.5):
                for k in range(0, 300, 1):
                    if k >= 150 and k % 12 >= 3:
                        continue  # broken: 3 m painted, 9 m gap
                    dbg.draw_line(carla.Location(k, y, z), carla.Location(k + 1, y, z), thickness=0.12, color=white, life_time=0.0)
            for y in (-7.0, 7.0):
                dbg.draw_line(carla.Location(0, y, z), carla.Location(300, y, z), thickness=0.12, color=white, life_time=0.0)
            shot("solid_section_debug_lines", 60.0)
            shot("broken_section_debug_lines", 190.0)
        finally:
            if args.traffic:
                world.apply_settings(original)
                tm.set_synchronous_mode(False)
            for a in reversed(actors):
                try:
                    if hasattr(a, "stop"):
                        a.stop()
                    a.destroy()
                except Exception:  # noqa: BLE001
                    pass
        info["rules"][rule] = res
        print(rule, json.dumps(res), flush=True)
    (out / "info.json").write_text(json.dumps(info, indent=1), encoding="utf-8")
    print(f"Saved in {out}", flush=True)
