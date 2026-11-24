"""Closed-loop test of the Reasoning-drive lane reasoner in CARLA.

The car drives on autopilot in synchronous mode (the simulation waits while the model answers). Every few
seconds it would like to change lane. At that moment the camera frame is sent to the lane reasoner with a cyan
box around the left lane boundary and, separately, around the right one, in Test A (image only) and/or Test B
(image + rule passages). The lane change is carried out only if the test chosen with --drive-with says that
crossing the line on that side is allowed.

Ground truth: the boundary type and colour come from the CARLA map and are mapped to the project's marking
types; the expected actions come from the project's rule table (regulations/<CODE>/action_rules.json), the same table used
for labeling. CARLA's own lane-change flag is kept as a second reference.

Outputs in --out: frames/, annotated/, answers.jsonl, decisions.jsonl, invasions.jsonl, summary.json, summary.md

Example:
    python -m reasoning_drive.simulation.loop --tests AB --drive-with B --decisions 20
    python -m reasoning_drive.simulation.loop --mock          (made-up answers, no API calls, to test the loop)
"""
from __future__ import annotations

import argparse
import json
import math
import queue
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import carla
import cv2
import numpy as np
from ..imageio import imread, imwrite

W, H, FOV = 1280, 720, 90.0
CAM_X, CAM_Z = 0.8, 1.4
SIDES = ("left", "right")
LMT, LMC = carla.LaneMarkingType, carla.LaneMarkingColor


# ---------------------------------------------------------------- ground truth from the map

def project_marking(m) -> str:
    """CARLA lane marking -> the project's marking_type (configs/schemas/label_schema.json)."""
    if m.type == LMT.NONE:
        return "none_visible"
    if m.color == LMC.Yellow:
        colour = "yellow"
    elif m.color in (LMC.Standard, LMC.White):
        colour = "white"
    else:
        return "other"
    if m.type == LMT.Solid:
        return colour + "_solid"
    if m.type == LMT.Broken:
        return colour + "_dashed"
    if m.type == LMT.SolidSolid:
        return colour + "_double_solid"
    if m.type in (LMT.SolidBroken, LMT.BrokenSolid) and colour == "yellow":
        return "yellow_solid_dashed"
    return "other"  # curb, grass, Botts' dots, white solid-dashed, double dashed: not in the label set


def lane_change_flags(wp) -> dict:
    lc = wp.lane_change
    return {"left": lc in (carla.LaneChange.Left, carla.LaneChange.Both),
            "right": lc in (carla.LaneChange.Right, carla.LaneChange.Both)}


def ground_truth(wp, side: str, table: dict, region: str, prefill) -> dict:
    m = wp.left_lane_marking if side == "left" else wp.right_lane_marking
    mt = project_marking(m)
    flags = lane_change_flags(wp)
    dashed_side = ""
    if mt == "yellow_solid_dashed":
        # which line of the pair faces my car follows from CARLA's lane-change flag for that side
        dashed_side = "ego_side" if flags[side] else "far_side"
    sug = prefill(table, region, mt, "", dashed_side, "full") or {}
    cross = (sug.get("actions") or {}).get("cross_line", "not_applicable")
    return {"marking_type": mt, "dashed_side": dashed_side, "cross_line": cross,
            "rule_ids": sug.get("rule_ids", []), "carla_allows": flags[side],
            "carla_type": str(m.type), "carla_color": str(m.color),
            "scored": cross in ("allowed", "prohibited")}


def same_direction_lanes(wp) -> tuple:
    def same(o):
        return o is not None and o.lane_type == carla.LaneType.Driving and (o.lane_id > 0) == (wp.lane_id > 0)
    left, w = 0, wp.get_left_lane()
    while same(w) and left < 10:
        left, w = left + 1, w.get_left_lane()
    right, w = 0, wp.get_right_lane()
    while same(w) and right < 10:
        right, w = right + 1, w.get_right_lane()
    return left + right + 1, left + 1, left > 0, right > 0


# ---------------------------------------------------------------- target box from the boundary line

def boundary_points(wp, side: str, d0: int = 6, d1: int = 18) -> list:
    """World points on the lane boundary on one side, d0 to d1 m ahead."""
    pts = []
    for d in range(d0, d1 + 1):
        nxt = wp.next(float(d))
        if not nxt or nxt[0].is_junction:
            break
        w = nxt[0]
        rv, loc, half = w.transform.get_right_vector(), w.transform.location, w.lane_width / 2.0
        s = -half if side == "left" else half
        pts.append((loc.x + rv.x * s, loc.y + rv.y * s, loc.z + rv.z * s))
    return pts


def boundary_box(wp, side: str, cam_tf, d0: int = 6, d1: int = 18):
    """Pixel box around the lane boundary on one side, 6 to 18 m ahead (projected from the map)."""
    pts = boundary_points(wp, side, d0, d1)
    w2c = np.array(cam_tf.get_inverse_matrix())
    f = W / (2.0 * math.tan(math.radians(FOV) / 2.0))
    uv = []
    for x, y, z in pts:
        c = w2c @ np.array([x, y, z, 1.0])
        cx, cy, cz = c[1], -c[2], c[0]  # UE camera axes -> image axes
        if cz < 1.0:
            continue
        u, v = f * cx / cz + W / 2.0, f * cy / cz + H / 2.0
        if 0 <= u < W and 0 <= v < H:
            uv.append((u, v))
    if len(uv) < 3:
        return None
    us, vs = [p[0] for p in uv], [p[1] for p in uv]
    x1, x2, y1, y2 = min(us) - 10, max(us) + 10, min(vs) - 8, max(vs) + 8
    if x2 - x1 < 40:
        cx = (x1 + x2) / 2
        x1, x2 = cx - 20, cx + 20
    if y2 - y1 < 30:
        cy = (y1 + y2) / 2
        y1, y2 = cy - 15, cy + 15
    return [int(max(0, x1)), int(max(0, y1)), int(min(W - 1, x2)), int(min(H - 1, y2))]


def boxed_jpeg(bgr, box, pc: dict) -> bytes:
    """Same drawing as reasoning_drive.data.boxed_jpeg: cyan box with the project's margin, width and quality."""
    img = bgr.copy()
    m = int(pc.get("box_margin", 6))
    x1, y1, x2, y2 = box
    x1, y1, x2, y2 = max(0, x1 - m), max(0, y1 - m), min(W - 1, x2 + m), min(H - 1, y2 + m)
    r, g, b = pc.get("box_color_rgb", [0, 229, 255])
    thick = max(2, round(int(pc.get("box_width", 3)) * W / 1280))
    cv2.rectangle(img, (x1, y1), (x2, y2), (int(b), int(g), int(r)), thick)
    ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, int(pc.get("jpeg_quality", 92))])
    if not ok:
        raise RuntimeError("could not encode the image")
    return buf.tobytes()


# ---------------------------------------------------------------- the reasoner

class Reasoner:
    def __init__(self, repo: Path, region: str, mock: bool, seed: int):
        from .. import config as C
        from .. import paths as P
        from ..agent.client import build_payload, call_with_fallback
        from ..agent.prompts import passages, prompt_parts
        from ..evaluation.scoring import parse
        from ..labeling.core import prefill
        self.cfg = C.load(repo)
        self.region, self.mock, self.seed = region, mock, seed
        self.build_payload, self.call, self.parse, self.prefill = build_payload, call_with_fallback, parse, prefill
        self.table = P.action_rules(repo)
        if not mock and not C.api_key(self.cfg):
            raise SystemExit("No OPENAI_API_KEY in .env. Add it, or run with --mock.")
        self.parts = {t: prompt_parts(self.cfg, t, region) for t in ("A", "B")}
        self.rule_ids = {p["rule_id"] for p in passages(self.cfg, region)}
        price = self.cfg["api"].get("price_per_million_tokens", {})
        self.price_in, self.price_out = float(price.get("input", 0)), float(price.get("output", 0))

    def ask(self, jpeg: bytes, test: str, gt: dict, key: str) -> dict:
        t0 = time.time()
        rec = {"test": test, "mock": self.mock, "answer": None, "error": "", "usage": {}, "latency_s": 0.0, "cost": 0.0}
        try:
            if self.mock:
                rec["answer"] = self._mock(test, gt, key)
            else:
                resp = self.call(self.cfg, self.build_payload(self.cfg, self.parts[test], jpeg))
                ans, err = self.parse(resp["text"])
                rec.update(answer=ans, error=err, usage=resp.get("usage") or {}, latency_s=resp.get("latency_s", 0.0),
                           response_id=resp.get("response_id", ""))
                u = rec["usage"]
                rec["cost"] = (u.get("input_tokens", 0) * self.price_in + u.get("output_tokens", 0) * self.price_out) / 1e6
        except Exception as e:  # keep driving; the error is recorded
            rec["error"] = f"{type(e).__name__}: {e}"
        if not rec["latency_s"]:
            rec["latency_s"] = round(time.time() - t0, 2)
        return rec

    def _mock(self, test: str, gt: dict, key: str) -> dict:
        """Made-up answer: the ground truth with deterministic mistakes (more in A). Says nothing about the model."""
        rng = random.Random(f"{self.seed}:{key}:{test}")
        mt = gt["marking_type"]
        swap = {"white_dashed": "white_solid", "white_solid": "white_dashed", "yellow_double_solid": "yellow_solid",
                "yellow_solid": "yellow_double_solid", "yellow_dashed": "yellow_solid"}
        if rng.random() < (0.2 if test == "A" else 0.08) and mt in swap:
            mt = swap[mt]
        sug = self.prefill(self.table, self.region, mt, "", gt.get("dashed_side", ""), "full") or {}
        acts = sug.get("actions") or {"cross_line": "not_applicable"}
        return {"description": "(mock)", "evidence": "full",
                "marking": {"marking_type": mt, "arrow_type": None, "position": "left"},
                "actions": acts, "cited_rule_id": (sug.get("rule_ids") or [None])[0] if test == "B" else None}


# ---------------------------------------------------------------- drawing

def annotate(bgr, n: int, boxes: dict, gt: dict, res: dict, tests: list, decision: dict, mock: bool):
    img = bgr.copy()
    colours = {"left": (255, 229, 0), "right": (0, 200, 255)}
    for side, box in boxes.items():
        if box:
            cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), colours[side], 2)
            cv2.putText(img, side, (box[0], max(12, box[1] - 4)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colours[side], 1, cv2.LINE_AA)
    lines = [f"#{n}  {'MOCK ANSWERS' if mock else 'model answers'}"]
    for side in SIDES:
        if side not in gt:
            continue
        g = gt[side]
        parts = [f"{side:5s} truth: {g['marking_type']} -> cross {g['cross_line']}"]
        for t in tests:
            r = res.get((t, side))
            a = (r or {}).get("answer") or {}
            if a:
                parts.append(f"{t}: {a['marking'].get('marking_type')} -> {a['actions'].get('cross_line')}")
            elif r:
                parts.append(f"{t}: error")
        lines.append("   ".join(parts))
    lines.append(f"wants {decision['desire']}  |  {decision['drive_with']} says {decision['system_says']}  |  "
                 f"{'LANE CHANGE' if decision['executed'] else 'stays in lane'}")
    y = 10
    for ln in lines:
        (tw, th), _ = cv2.getTextSize(ln, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 1)
        cv2.rectangle(img, (6, y), (12 + tw, y + th + 10), (0, 0, 0), -1)
        cv2.putText(img, ln, (9, y + th + 4), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)
        y += th + 14
    return img


# ---------------------------------------------------------------- live view (--watch)

class LiveView:
    """One window: the camera picture with the latest decision on the left, the model's reasoning for each request
    on the right (shown as soon as each answer arrives), a chase camera in the CARLA window and the boundary lines
    drawn on the road in the colour of the system's answer (green allowed, red prohibited)."""
    VW, VH, PW, BH = 800, 450, 600, 130

    def __init__(self, world, mock: bool, drive_with: str, record_path=None):
        import pygame
        self.pg, self.world, self.mock, self.drive_with = pygame, world, mock, drive_with
        self.writer, self.frame_i = None, 0
        if record_path:
            # records the whole window (picture, decision and reasoning panel) at about 10 frames per second
            self.writer = cv2.VideoWriter(str(record_path), cv2.VideoWriter_fourcc(*"mp4v"), 10.0,
                                          (self.VW + self.PW, self.VH + self.BH))
        pygame.init()
        self.screen = pygame.display.set_mode((self.VW + self.PW, self.VH + self.BH))
        pygame.display.set_caption("Reasoning-drive in CARLA" + (" (mock answers)" if mock else ""))
        try:  # keep the window on top of the CARLA window (Windows only)
            import ctypes
            hwnd = pygame.display.get_wm_info()["window"]
            ctypes.windll.user32.SetWindowPos(hwnd, -1, 10, 40, 0, 0, 0x0001)
        except Exception:
            pass
        # SysFont reads the font registry, which fails on some Windows machines; load the files directly
        self.font = self._font(r"C:\Windows\Fonts\consola.ttf", 15)
        self.small = self._font(r"C:\Windows\Fonts\consola.ttf", 13)
        self.bold = self._font(r"C:\Windows\Fonts\consolab.ttf", 14)
        self.big = self._font(r"C:\Windows\Fonts\consolab.ttf", 22)
        self.lines, self.boxes, self.box_colours, self.status, self.quit = [], {}, {}, "driving", False
        self.panel = [("title", "LLM reasoning: waiting for the first decision point")]
        self.t_last = time.time()
        self.spectator = world.get_spectator()

    def _font(self, path: str, size: int):
        try:
            return self.pg.font.Font(path, size)
        except Exception:
            return self.pg.font.Font(None, int(size * 1.3))

    # ------------------------------------------------ reasoning panel
    def set_reasoning(self, n: int, res: dict, gt: dict, tests: list, sides: list, desire: str, elapsed: float):
        """res: {(test, side): record or None while pending}. The test that drives and the wanted side come first."""
        P = [("title", f"LLM reasoning, decision #{n}  ({elapsed:.1f} s)")]
        order = sorted(res.keys(), key=lambda k: (k[0] != self.drive_with, k[1] != desire, k[0], k[1]))
        for (t, sd) in order:
            r = res[(t, sd)]
            head = f"Test {t} ({'image + rules' if t == 'B' else 'image only'}), {sd} line"
            if r is None:
                P.append(("head", head + "  ... waiting"))
                continue
            a = r.get("answer") or {}
            if not a:
                P.append(("head", f"{head}  error"))
                P.append(("text", (r.get("error") or "no answer")[:200]))
                continue
            m, acts = a.get("marking") or {}, a.get("actions") or {}
            verdict = f"{m.get('marking_type')}  cross_line={acts.get('cross_line')}"
            truth = f"truth {gt[sd]['marking_type']}={gt[sd]['cross_line']}"
            ok = acts.get("cross_line") == gt[sd]["cross_line"]
            P.append(("head", f"{head}  {r.get('latency_s', 0):.1f} s"))
            P.append(("ok" if ok else "bad", f"-> {verdict}   ({truth})"))
            if (t, sd) == order[0] or (t == self.drive_with):
                reasons = (a.get("action_reasons") or {}).get("cross_line", "")
                for label, txt in (("look", a.get("description", "")), ("evidence", a.get("evidence", "")),
                                   ("rule", a.get("rule_reasoning", "")), ("cited", a.get("cited_rule_id") or "-"),
                                   ("cross_line", reasons), ("check", a.get("self_check", ""))):
                    if txt:
                        P.append(("text", f"{label}: {txt}"))
        self.panel = P

    def _wrap(self, text: str, font, width: int, max_lines: int = 4) -> list:
        words, out, cur = str(text).split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if font.size(t)[0] <= width:
                cur = t
            else:
                out.append(cur)
                cur = w
                if len(out) >= max_lines:
                    break
        if cur and len(out) < max_lines:
            out.append(cur)
        elif len(out) >= max_lines:
            out[-1] = out[-1][:max(0, len(out[-1]) - 3)] + "..."
        return out

    def _draw_panel(self):
        pg, x0, w = self.pg, self.VW + 10, self.PW - 20
        pg.draw.rect(self.screen, (24, 26, 30), pg.Rect(self.VW, 0, self.PW, self.VH + self.BH))
        y = 8
        colours = {"title": (255, 220, 60), "head": (120, 200, 255), "ok": (90, 220, 120), "bad": (255, 110, 110), "text": (220, 220, 220)}
        fonts = {"title": self.bold, "head": self.bold, "ok": self.font, "bad": self.font, "text": self.small}
        for kind, txt in self.panel:
            f = fonts[kind]
            if kind == "head":
                y += 6
            for ln in self._wrap(txt, f, w, 1 if kind in ("title", "head") else 4):
                if y > self.VH + self.BH - 18:
                    return
                self.screen.blit(f.render(ln, True, colours[kind]), (x0, y))
                y += f.get_linesize()

    # ------------------------------------------------ camera, road drawing, frame
    def follow(self, ego):
        tf = ego.get_transform()
        fv = tf.get_forward_vector()
        loc = carla.Location(tf.location.x - 9 * fv.x, tf.location.y - 9 * fv.y, tf.location.z + 4.5)
        self.spectator.set_transform(carla.Transform(loc, carla.Rotation(pitch=-15, yaw=tf.rotation.yaw)))

    def draw_on_road(self, wp, says_by_side: dict, label: str, ego):
        colour = {"allowed": carla.Color(0, 200, 0), "prohibited": carla.Color(230, 0, 0)}
        for side, says in says_by_side.items():
            # the car's camera also sees these lines: keep them thin, away from the hood and gone before the next
            # decision point, so the images sent to the model stay clean
            pts = boundary_points(wp, side, 10, 30)
            c = colour.get(says, carla.Color(255, 200, 0))
            for a, b in zip(pts, pts[1:]):
                self.world.debug.draw_line(carla.Location(a[0], a[1], a[2] + 0.05), carla.Location(b[0], b[1], b[2] + 0.05),
                                           thickness=0.06, color=c, life_time=2.5)
        loc = ego.get_location()
        self.world.debug.draw_string(carla.Location(loc.x, loc.y, loc.z + 2.5), label, color=carla.Color(255, 255, 255),
                                     life_time=2.5)

    def events(self):
        for e in self.pg.event.get():
            if e.type == self.pg.QUIT:
                self.quit = True

    def show(self, bgr, ego=None, throttle=True):
        pg = self.pg
        self.events()
        if ego is not None:
            self.follow(ego)
        rgb = cv2.cvtColor(cv2.resize(bgr, (self.VW, self.VH)), cv2.COLOR_BGR2RGB)
        self.screen.blit(pg.image.frombuffer(rgb.tobytes(), (self.VW, self.VH), "RGB"), (0, 0))
        k = self.VW / W
        for side, box in self.boxes.items():
            if box:
                col = self.box_colours.get(side, (0, 229, 255))
                pg.draw.rect(self.screen, col, pg.Rect(box[0] * k, box[1] * k, (box[2] - box[0]) * k, (box[3] - box[1]) * k), 2)
        pg.draw.rect(self.screen, (15, 15, 15), pg.Rect(0, self.VH, self.VW, self.BH))
        self.screen.blit(self.big.render(self.status, True, (255, 220, 60)), (10, self.VH + 6))
        for i, ln in enumerate(self.lines[:3]):
            self.screen.blit(self.font.render(ln, True, (235, 235, 235)), (10, self.VH + 40 + 22 * i))
        if self.mock:
            tag = self.big.render("MOCK ANSWERS - no model called", True, (255, 80, 80))
            pg.draw.rect(self.screen, (0, 0, 0), pg.Rect(6, 6, tag.get_width() + 12, tag.get_height() + 8))
            self.screen.blit(tag, (12, 10))
        self._draw_panel()
        pg.display.flip()
        self.frame_i += 1
        if self.writer is not None and (not throttle or self.frame_i % 2 == 0):
            # every second driving tick (0.1 s); every refresh while waiting for the model (also 0.1 s)
            arr = pg.surfarray.array3d(self.screen).swapaxes(0, 1)
            self.writer.write(cv2.cvtColor(arr, cv2.COLOR_RGB2BGR))
        if throttle:  # about real time: one tick = 0.05 s
            dt = time.time() - self.t_last
            if dt < 0.05:
                time.sleep(0.05 - dt)
            self.t_last = time.time()


# ---------------------------------------------------------------- summary

def summarize(decisions: list, answers: list, invasions: list, tests: list, drive_with: str, table: dict,
              region: str, prefill, mock: bool, meta: dict) -> dict:
    per_test = {}
    for t in tests:
        rs = [a for a in answers if a["test"] == t and a["gt"]["scored"]]
        ok = [a for a in rs if a["answer"]]
        type_ok = sum(1 for a in ok if a["answer"]["marking"].get("marking_type") == a["gt"]["marking_type"])
        cross = [(a["answer"]["actions"].get("cross_line"), a["gt"]["cross_line"]) for a in ok]
        by_type = {}
        for a in ok:
            k = a["gt"]["marking_type"]
            d = by_type.setdefault(k, {"n": 0, "type_ok": 0, "cross_ok": 0})
            d["n"] += 1
            d["type_ok"] += a["answer"]["marking"].get("marking_type") == k
            d["cross_ok"] += a["answer"]["actions"].get("cross_line") == a["gt"]["cross_line"]
        per_test[t] = {
            "requests": len(rs), "answered": len(ok), "errors": len(rs) - len(ok),
            "marking_type_correct": type_ok, "cross_line_correct": sum(1 for g, w in cross if g == w),
            "unsafe": sum(1 for g, w in cross if w == "prohibited" and g == "allowed"),
            "over_cautious": sum(1 for g, w in cross if w == "allowed" and g in ("prohibited", "not_determined")),
            "agrees_with_carla_flag": sum(1 for a in ok if (a["answer"]["actions"].get("cross_line") == "allowed") == a["gt"]["carla_allows"]),
            "mean_latency_s": round(sum(a["latency_s"] for a in rs) / len(rs), 2) if rs else 0.0,
            "tokens_in": sum((a.get("usage") or {}).get("input_tokens", 0) for a in rs),
            "tokens_out": sum((a.get("usage") or {}).get("output_tokens", 0) for a in rs),
            "cost_usd": round(sum(a.get("cost", 0.0) for a in rs), 4),
            "by_marking_type": by_type,
        }
    paired = None
    if "A" in tests and "B" in tests:
        idx = {}
        for a in answers:
            if a["gt"]["scored"] and a["answer"]:
                idx.setdefault((a["n"], a["side"]), {})[a["test"]] = a["answer"]["actions"].get("cross_line") == a["gt"]["cross_line"]
        both = [v for v in idx.values() if "A" in v and "B" in v]
        paired = {"pairs": len(both), "both_right": sum(1 for v in both if v["A"] and v["B"]),
                  "only_A_right": sum(1 for v in both if v["A"] and not v["B"]),
                  "only_B_right": sum(1 for v in both if v["B"] and not v["A"]),
                  "both_wrong": sum(1 for v in both if not v["A"] and not v["B"])}
    wants = [d for d in decisions if d["target_exists"]]
    loop = {
        "decision_points": len(decisions),
        "lane_change_wanted_with_lane_available": len(wants),
        "system_allowed": sum(1 for d in wants if d["system_says"] == "allowed"),
        "lane_changes_executed": sum(1 for d in decisions if d["executed"]),
        "lane_changes_completed": sum(1 for d in decisions if d.get("completed")),
        "blocked_although_allowed_by_rules": sum(1 for d in wants if d["system_says"] != "allowed" and d["truth"] == "allowed"),
        "allowed_although_prohibited_by_rules": sum(1 for d in decisions if d["system_says"] == "allowed" and d["truth"] == "prohibited"),
        "wanted_to_cross_a_prohibited_line": sum(1 for d in decisions if d["truth"] == "prohibited"),
        "blocked_prohibited_crossings": sum(1 for d in decisions if d["truth"] == "prohibited" and d["system_says"] != "allowed"),
    }
    crossed = []
    for ev in invasions:
        for m in ev["markings"]:
            crossed.append(m["marking_type"])
    prohibited_types = {k for k, v in table.get(region, {}).items() if (v.get("actions") or {}).get("cross_line") == "prohibited"}
    loop["lines_crossed"] = {k: crossed.count(k) for k in sorted(set(crossed))}
    loop["prohibited_lines_crossed"] = sum(1 for k in crossed if k in prohibited_types)
    return {"meta": meta, "mock": mock, "drive_with": drive_with, "per_test": per_test, "a_vs_b_cross_line": paired, "closed_loop": loop}


def write_markdown(s: dict, path: Path):
    L = ["# CARLA closed-loop run", ""]
    if s["mock"]:
        L += ["**Mock answers: no model was called. These numbers only check the pipeline.**", ""]
    m = s["meta"]
    L += [f"Map {m['map']}, weather {m['weather']}, region {m['region']}, prompt {m['prompt']}, model {m['model']}, "
          f"seed {m['seed']}, started {m['started']}.", ""]
    L += ["## Per test (one request = one boundary line in one frame)", "",
          "| Test | Requests | Answered | Marking type correct | Cross line correct | Unsafe | Over-cautious | Mean latency (s) | Cost (USD) |",
          "|---|---|---|---|---|---|---|---|---|"]
    for t, d in s["per_test"].items():
        L.append(f"| {t} | {d['requests']} | {d['answered']} | {d['marking_type_correct']}/{d['answered']} | "
                 f"{d['cross_line_correct']}/{d['answered']} | {d['unsafe']} | {d['over_cautious']} | {d['mean_latency_s']} | {d['cost_usd']} |")
    L.append("")
    for t, d in s["per_test"].items():
        L += [f"By marking type, Test {t}:", "", "| Marking (truth) | n | Type correct | Cross line correct |", "|---|---|---|---|"]
        for k, v in sorted(d["by_marking_type"].items()):
            L.append(f"| {k} | {v['n']} | {v['type_ok']} | {v['cross_ok']} |")
        L.append("")
    if s["a_vs_b_cross_line"]:
        p = s["a_vs_b_cross_line"]
        L += ["## Test A vs Test B on the same lines (cross line)", "",
              f"{p['pairs']} pairs: both right {p['both_right']}, only A right {p['only_A_right']}, "
              f"only B right {p['only_B_right']}, both wrong {p['both_wrong']}.", ""]
    c = s["closed_loop"]
    L += [f"## Closed loop (lane changes decided by Test {s['drive_with']})", "",
          f"- Decision points: {c['decision_points']}",
          f"- Lane change wanted and a lane available: {c['lane_change_wanted_with_lane_available']}",
          f"- Allowed by the system: {c['system_allowed']}; lane change started: {c['lane_changes_executed']}, "
          f"completed: {c['lane_changes_completed']}",
          f"- Blocked although the rules allow it: {c['blocked_although_allowed_by_rules']}",
          f"- Wanted to cross a prohibited line: {c['wanted_to_cross_a_prohibited_line']}; "
          f"blocked by the system: {c['blocked_prohibited_crossings']}",
          f"- Allowed although the rules prohibit it: {c['allowed_although_prohibited_by_rules']}",
          f"- Lines crossed (lane invasion sensor): {c['lines_crossed']}",
          f"- Prohibited lines crossed: {c['prohibited_lines_crossed']}", ""]
    path.write_text("\n".join(L), encoding="utf-8")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parents[2]), help="the project folder")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=2000)
    ap.add_argument("--tm-port", type=int, default=8000)
    ap.add_argument("--region", default="US")
    ap.add_argument("--tests", default="AB", help="A, B or AB")
    ap.add_argument("--drive-with", default="B", help="the test whose answer decides the lane change")
    ap.add_argument("--decisions", type=int, default=20)
    ap.add_argument("--spacing-ticks", type=int, default=120, help="ticks between decision points (0.05 s each)")
    ap.add_argument("--max-ticks", type=int, default=20000)
    ap.add_argument("--weather", default="ClearNoon")
    ap.add_argument("--night", action="store_true")
    ap.add_argument("--seed", type=int, default=6216)
    ap.add_argument("--tempt", type=float, default=0.3,
                    help="share of decision points where the car wants to cross the line on the side without a lane")
    ap.add_argument("--mock", action="store_true", help="made-up answers, no API calls")
    ap.add_argument("--watch", action="store_true", help="live window, chase camera and coloured lines on the road")
    ap.add_argument("--record", action="store_true", help="with --watch: save the live window as live_view.mp4 in --out")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    tests = [t for t in "AB" if t in args.tests.upper()]
    drive_with = args.drive_with.upper() if args.drive_with.upper() in tests else tests[-1]
    random.seed(args.seed)
    repo = Path(args.repo)
    reasoner = Reasoner(repo, args.region, args.mock, args.seed)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(args.out or (Path(__file__).resolve().parent / "loop_runs" / (stamp + ("_mock" if args.mock else ""))))
    for sub in ("frames", "annotated"):
        (out / sub).mkdir(parents=True, exist_ok=True)

    client = carla.Client(args.host, args.port)
    client.set_timeout(120.0)
    world = client.get_world()
    map_name = world.get_map().name.split("/")[-1]
    print(f"server map: {map_name} (not switching maps)", flush=True)
    weather = getattr(carla.WeatherParameters, args.weather)
    if args.night:
        weather.sun_altitude_angle = -30.0
    world.set_weather(weather)
    cmap = world.get_map()

    original = world.get_settings()
    st = world.get_settings()
    st.synchronous_mode, st.fixed_delta_seconds = True, 0.05
    world.apply_settings(st)
    tm = client.get_trafficmanager(args.tm_port)
    tm.set_synchronous_mode(True)
    tm.set_random_device_seed(args.seed)

    meta = {"map": map_name, "weather": args.weather + (" night" if args.night else ""), "region": args.region,
            "prompt": reasoner.cfg["prompt"]["dir"], "model": reasoner.cfg["api"]["model"],
            "reasoning_effort": reasoner.cfg["api"].get("reasoning_effort"), "seed": args.seed, "tests": tests,
            "started": stamp, "spacing_ticks": args.spacing_ticks, "tempt": args.tempt}
    decisions, answers, invasions = [], [], []
    inv_lock = threading.Lock()
    camera = ego = lane_sensor = None
    view = None
    pool = ThreadPoolExecutor(max_workers=4)
    f_ans = open(out / "answers.jsonl", "w", encoding="utf-8")
    f_dec = open(out / "decisions.jsonl", "w", encoding="utf-8")
    try:
        lib = world.get_blueprint_library()
        sps = cmap.get_spawn_points()
        random.shuffle(sps)
        for sp in sps:
            ego = world.try_spawn_actor(lib.find("vehicle.tesla.model3"), sp)
            if ego is not None:
                break
        if ego is None:
            raise RuntimeError("could not spawn the car")
        cam_bp = lib.find("sensor.camera.rgb")
        cam_bp.set_attribute("image_size_x", str(W))
        cam_bp.set_attribute("image_size_y", str(H))
        cam_bp.set_attribute("fov", str(FOV))
        camera = world.spawn_actor(cam_bp, carla.Transform(carla.Location(x=CAM_X, z=CAM_Z)), attach_to=ego)
        images = queue.Queue()
        camera.listen(images.put)
        lane_sensor = world.spawn_actor(lib.find("sensor.other.lane_invasion"), carla.Transform(), attach_to=ego)

        def on_invasion(ev):
            ms = [{"marking_type": project_marking(m), "type": str(m.type), "color": str(m.color)} for m in ev.crossed_lane_markings]
            with inv_lock:
                invasions.append({"frame": ev.frame, "markings": ms})
        lane_sensor.listen(on_invasion)

        ego.set_autopilot(True, tm.get_port())
        tm.auto_lane_change(ego, False)  # every lane change comes from the reasoner's decision
        view = LiveView(world, args.mock, drive_with, (out / "live_view.mp4") if args.record else None) if args.watch else None

        ticks, last = 0, -10 ** 9
        pending = None  # a lane change that was allowed and is being carried out
        while (len(decisions) < args.decisions or pending) and ticks < args.max_ticks:
            frame = world.tick()
            image = images.get(timeout=10.0)
            while image.frame < frame:
                image = images.get(timeout=10.0)
            ticks += 1
            if view is not None:
                if view.quit:
                    break
                if not pending and ticks - last > 60:
                    view.status, view.boxes = "driving", {}
                view.show(np.ascontiguousarray(np.frombuffer(image.raw_data, dtype=np.uint8).reshape((H, W, 4))[:, :, :3]), ego)
            if pending:
                with inv_lock:
                    crossed = len(invasions) > pending["invasions_before"]
                if crossed or ticks > pending["until"]:
                    pending["decision"]["completed"] = crossed
                    print(f"    lane change #{pending['decision']['n']} {'done' if crossed else 'not done within 5 s'}", flush=True)
                    pending = None
                else:
                    # TM checks a forced change only in the tick it is given, so repeat it until it happens
                    tm.force_lane_change(ego, pending["decision"]["desire"] == "right")
                    continue
            if len(decisions) >= args.decisions:
                continue
            if ticks < 60 or ticks - last < args.spacing_ticks:
                continue
            v = ego.get_velocity()
            if math.sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2) < 2.0:
                continue
            wp = cmap.get_waypoint(ego.get_location(), project_to_road=True, lane_type=carla.LaneType.Driving)
            if wp is None or wp.is_junction or ego.get_location().distance(wp.transform.location) > 0.8:
                continue  # in a junction or in the middle of a lane change
            gt = {s: ground_truth(wp, s, reasoner.table, args.region, reasoner.prefill) for s in SIDES}
            boxes = {s: boundary_box(wp, s, image.transform) for s in SIDES}
            ask_sides = [s for s in SIDES if boxes[s] and gt[s]["scored"]]
            if not ask_sides:
                continue
            last = ticks
            n = len(decisions) + 1
            bgr = np.frombuffer(image.raw_data, dtype=np.uint8).reshape((H, W, 4))[:, :, :3].copy()
            imwrite(str(out / "frames" / f"{n:03d}.png"), bgr)

            jobs = {}
            for t in tests:
                for s in ask_sides:
                    jpeg = boxed_jpeg(bgr, boxes[s], reasoner.cfg["prompt"])
                    jobs[(t, s)] = pool.submit(reasoner.ask, jpeg, t, gt[s], f"{n}:{s}")
            lanes, idx, has_left, has_right = same_direction_lanes(wp)
            if view is not None:
                view.boxes, view.box_colours = boxes, {}
                t0 = time.time()
                while not view.quit:
                    partial = {k: (f.result() if f.done() else None) for k, f in jobs.items()}
                    view.set_reasoning(n, partial, gt, tests, ask_sides, "right" if has_right and not has_left else
                                       "left" if has_left and not has_right else ask_sides[0], time.time() - t0)
                    view.status = f"asking the model (Test {' and '.join(tests)})  {time.time() - t0:4.1f} s"
                    view.show(bgr, None, throttle=False)
                    if all(f.done() for f in jobs.values()):
                        break
                    time.sleep(0.1)
            res = {k: f.result() for k, f in jobs.items()}

            if has_left != has_right and random.random() < args.tempt:
                # now and then the car wants to cross the line on the side without a lane of its own direction
                # (opposite traffic or road edge): the system should block it
                desire = "left" if has_right else "right"
            elif has_right and not has_left:
                desire = "right"
            elif has_left and not has_right:
                desire = "left"
            else:
                desire = random.choice(SIDES)
            target_exists = has_left if desire == "left" else has_right
            r = res.get((drive_with, desire))
            says = ((r or {}).get("answer") or {}).get("actions", {}).get("cross_line", "not asked") if r else "not asked"
            if r and not r.get("answer"):
                says = "error"
            executed = says == "allowed" and target_exists

            dec = {"n": n, "frame": frame, "tick": ticks, "road_id": wp.road_id, "lane_id": wp.lane_id,
                   "lanes_same_direction": lanes, "ego_lane_from_left": idx, "boxes": boxes, "truth_by_side": gt,
                   "desire": desire, "target_exists": target_exists, "drive_with": drive_with, "system_says": says,
                   "truth": gt[desire]["cross_line"], "executed": executed, "completed": False}
            decisions.append(dec)
            if view is not None:
                says_side = {}
                for sd in ask_sides:
                    a = (res.get((drive_with, sd)) or {}).get("answer") or {}
                    says_side[sd] = (a.get("actions") or {}).get("cross_line", "error")
                rgbc = {"allowed": (0, 200, 0), "prohibited": (230, 40, 40)}
                view.box_colours = {sd: rgbc.get(v, (255, 200, 0)) for sd, v in says_side.items()}
                view.status = (f"#{n}: wants {desire} -> {drive_with} says {says} -> "
                               f"{'LANE CHANGE ' + desire.upper() if executed else 'stays in lane'}")
                view.lines = []
                for sd in ask_sides:
                    parts = [f"{sd:5s} truth {gt[sd]['marking_type']}={gt[sd]['cross_line']}"]
                    for t in tests:
                        a = (res.get((t, sd)) or {}).get("answer") or {}
                        parts.append(f"{t} {(a.get('marking') or {}).get('marking_type', 'error')}="
                                     f"{(a.get('actions') or {}).get('cross_line', '-')}")
                    view.lines.append(" | ".join(parts))
                view.set_reasoning(n, res, gt, tests, ask_sides, desire, max((r.get("latency_s") or 0) for r in res.values()))
                view.draw_on_road(wp, says_side, f"{drive_with}: {desire} {says}", ego)
            if executed:
                tm.force_lane_change(ego, desire == "right")  # True = the lane on the right
                with inv_lock:
                    n_inv = len(invasions)
                pending = {"decision": dec, "invasions_before": n_inv, "until": ticks + 100}
            f_dec.write(json.dumps(dec) + "\n")
            f_dec.flush()
            for (t, s), rec in res.items():
                row = dict(rec, n=n, frame=frame, side=s, box=boxes[s], gt=gt[s])
                answers.append(row)
                f_ans.write(json.dumps(row, ensure_ascii=False) + "\n")
            f_ans.flush()
            imwrite(str(out / "annotated" / f"{n:03d}.jpg"),
                        annotate(bgr, n, boxes, {s: gt[s] for s in ask_sides}, res, tests, dec, args.mock),
                        [cv2.IMWRITE_JPEG_QUALITY, 88])
            brief = "  ".join(f"{t}/{s}:{((res[(t, s)].get('answer') or {}).get('actions') or {}).get('cross_line', 'err')}"
                              for t in tests for s in ask_sides)
            print(f"[{n}/{args.decisions}] L={gt['left']['marking_type']} R={gt['right']['marking_type']}  {brief}  "
                  f"wants {desire} -> {'CHANGE' if executed else 'stay'}", flush=True)
    finally:
        # results first: destroying sensors has crashed the client process on Windows
        try:
            f_ans.close()
            f_dec.close()
            with inv_lock:
                inv = list(invasions)
            with open(out / "invasions.jsonl", "w", encoding="utf-8") as f:
                for ev in inv:
                    f.write(json.dumps(ev) + "\n")
            with open(out / "decisions_final.jsonl", "w", encoding="utf-8") as f:
                for d in decisions:
                    f.write(json.dumps(d) + "\n")
            if decisions:
                s = summarize(decisions, answers, inv, tests, drive_with, reasoner.table, args.region,
                              reasoner.prefill, args.mock, meta)
                (out / "summary.json").write_text(json.dumps(s, indent=2), encoding="utf-8")
                write_markdown(s, out / "summary.md")
                print("summary:", out / "summary.md", flush=True)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("could not write the summary:", e, flush=True)
        pool.shutdown(wait=False)
        client.set_timeout(10.0)
        try:
            tm.set_synchronous_mode(False)
            world.apply_settings(original)
            for a in (lane_sensor, camera):
                if a is not None:
                    a.stop()
            for a in (lane_sensor, camera, ego):
                if a is not None:
                    a.destroy()
        except RuntimeError as e:
            print("cleanup skipped:", e, flush=True)
        if view is not None:
            if view.writer is not None:
                view.writer.release()
                print("video:", out / "live_view.mp4", flush=True)
            view.pg.quit()
        print("finished", flush=True)


if __name__ == "__main__":
    main()
