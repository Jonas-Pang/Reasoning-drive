"""Video of one route run (simulation/route.py): explanation, route map, then for every stop the drive to it (4x speed),
the answers arriving, what the car did, and a card with the full reasoning of A, B and C (the project's trace), then
the results. Needs ffmpeg on the PATH.

    python main.py carla video <run folder> [findings.json]      writes <run folder>/route_replay.mp4
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CW, CH, FPS = 1920, 1080, 25
CJK = {False: ["/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", "C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf",
               "/System/Library/Fonts/PingFang.ttc"],
       True: ["/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", "C:/Windows/Fonts/msyhbd.ttc", "C:/Windows/Fonts/simhei.ttf",
              "/System/Library/Fonts/PingFang.ttc"]}
MONO = ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", "C:/Windows/Fonts/consola.ttf", "/System/Library/Fonts/Menlo.ttc"]


def _first(paths, size):
    for f in paths:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    raise SystemExit(f"No font found ({paths[0]} ...): install a CJK font")


def font(size, bold=False):
    return _first(CJK[bold], size)


f_h1, f_h2, f_h3 = font(42, True), font(30, True), font(22, True)
f_mid, f_txt, f_small, f_tiny = font(22), font(18), font(16), font(15)
f_mono = _first(MONO, 13)
REPO = Path(__file__).resolve().parents[2]


def project_traces():
    """The project's trace (agent.trace), re-wrapped narrower for three columns."""
    from .. import config as C
    from ..agent import trace as T
    cfg = C.load(REPO)
    T.WIDTH = 72
    pm = {reg: T.passage_map(cfg, reg) for reg in ("US", "CN")}
    def tr(row, lab=None):
        if lab is not None and not isinstance(row.get("label"), dict):
            row = dict(row, label=lab)      # older answers.jsonl put the stop's name in "label"
        return T.trace_text(row, pm["CN" if row.get("experiment") == "C" else "US"], row.get("cost"))
    return tr
BG, PANEL = (18, 20, 24), (30, 33, 40)
GREEN, RED, YEL, WHITE, GREY, BLUE, CYAN, AMBER = ((90, 220, 120), (255, 110, 110), (255, 215, 70), (235, 235, 235),
                                                   (150, 150, 150), (120, 190, 255), (90, 220, 230), (230, 190, 120))
ACT = {"cross_line": "越线", "go_straight": "直行", "turn_left": "左转", "turn_right": "右转", "u_turn": "掉头",
       "enter_center_lane_to_wait": "进中心车道等待"}
VAL = {"allowed": "允许", "prohibited": "禁止", "not_determined": "无法判断", "not_applicable": "不适用", "undecided": "未定",
       None: "—", "error": "无答案"}
MARK = {"arrow": "箭头", "yellow_double_solid": "双黄实线", "yellow_solid": "黄单实线", "white_dashed": "白虚线",
        "white_solid": "白实线", "yellow_dashed": "黄虚线", "yellow_solid_dashed": "黄虚实线", "white_double_solid": "双白实线",
        "two_way_left_turn_lane": "双向左转车道", "other": "其他", "none_visible": "看不到"}
ARROW = {"left": "左", "right": "右", "straight": "直", "straight_left": "直左", "straight_right": "直右"}
RELEVANT = {"arrow": ["go_straight", "turn_left", "turn_right", "u_turn"], "line": ["cross_line"],
            "twltl": ["enter_center_lane_to_wait", "turn_left"]}
LABEL = {
    "broken white lane line": "白虚线（同向车道分界线）",
    "double solid yellow centre line": "双黄实线（中心线）",
    "solid + broken yellow centre line": "黄色虚实线（中心线，我这侧是虚线）",
    "solid + broken yellow centre line (solid on my side)": "黄色虚实线（中心线，我这侧是实线）",
    "single solid yellow line on the left": "单黄实线（车左侧的边线）",
    "two-way left-turn lane": "双向左转中心车道",
    "roundabout: line between the circulating lanes": "环岛：两条环行车道之间的线",
    "junction approach: left-turn arrow and the line to the right lane": "路口前：左转箭头 + 与右车道之间的白实线",
    "right-turn arrow": "右转箭头",
}
INTENT = {
    "change lane across the line": "越线变道", "overtake across the centre line": "越过中心线超车",
    "cross the yellow line to the left": "向左越过黄线", "enter the centre lane to wait for a left turn": "进入中心车道等待左转",
    "move to the outer lane to leave the roundabout": "并到外侧车道准备出环岛",
    "turn_right": "在路口右转", "turn_left": "在路口左转", "go_straight": "在路口直行",
}
EXP = {"A": "A  只看图（美国）", "B": "B  图 + 美国规则", "C": "C  图 + 中国规则（美国道路）"}


# ---------------------------------------------------------------- text helpers

def _tokens(s):
    out, cur = [], ""
    for ch in s:
        if ord(ch) > 0x2E80:
            if cur:
                out.append(cur)
                cur = ""
            out.append(ch)
        elif ch == " ":
            out.append(cur + " ")
            cur = ""
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def wrap(d, text, f, width):
    lines = []
    for p in str(text).split("\n"):
        cur = ""
        for tok in _tokens(p):
            t = cur + tok
            if d.textlength(t, font=f) <= width or not cur:
                cur = t
            else:
                lines.append(cur.rstrip())
                cur = tok.lstrip()
        lines.append(cur.rstrip())
    return lines


def para(d, x, y, width, text, f=f_mid, fill=WHITE, max_lines=99, gap=6):
    lines = wrap(d, text, f, width)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max(0, len(lines[-1]) - 2)] + " …"
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += f.size + gap
    return y


def labelled(d, x, y, width, label, text, colour=WHITE, max_lines=4, f=f_tiny, lf=f_small, gap=4):
    d.text((x, y - 1), label, font=lf, fill=GREY)
    lw = d.textlength(label + " ", font=lf)
    lines = wrap(d, text, f, width - lw)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max(0, len(lines[-1]) - 2)] + " …"
    for ln in lines:
        d.text((x + lw, y), ln, font=f, fill=colour)
        y += f.size + gap
    return y + 4


def canvas():
    im = Image.new("RGB", (CW, CH), BG)
    return im, ImageDraw.Draw(im)


def still(img, seconds, tmp, name):
    png = tmp / f"{name}.png"
    img.save(png)
    mp4 = tmp / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(png), "-t", str(seconds), "-r", str(FPS),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", str(mp4)], check=True)
    return mp4


def clip(run, tmp, name, f0, f1, speed, title, note):
    """Frames f0..f1 of live_view.mp4 (10 fps) on a captioned background, played `speed` times faster."""
    if f1 <= f0 + 2:
        return None
    bg, d = canvas()
    d.text((70, 40), title, font=f_h2, fill=YEL)
    para(d, 70, 92, CW - 140, note, f=f_txt, fill=WHITE, max_lines=2)
    if speed != 1:
        d.text((CW - 260, 44), f"{speed}× 快放", font=f_h3, fill=AMBER)
    png = tmp / f"{name}_bg.png"
    bg.save(png)
    mp4 = tmp / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(png), "-ss", f"{f0 / 10:.2f}", "-to", f"{f1 / 10:.2f}",
                    "-i", str(run / "live_view.mp4"), "-filter_complex",
                    f"[1]setpts=(PTS-STARTPTS)/{speed},scale=1680:-2[v];[0][v]overlay=(W-w)/2:160:shortest=1,fps={FPS},format=yuv420p",
                    "-c:v", "libx264", "-crf", "20", str(mp4)], check=True)
    return mp4


# ---------------------------------------------------------------- what the car did, in Chinese

def car_cn(r):
    k = r["kind"]
    says = VAL.get(r.get("system_says"), r.get("system_says"))
    if k == "line":
        a = r.get("action", "")
        if a.startswith("changes"):
            act = "变道"
        elif a.startswith("overtakes"):
            act = "越线超车后回到原车道"
        elif a.startswith("would cross"):
            act = "那一侧是隔离带、没有车道，车没动（但这个“允许”是不安全的答案）"
        else:
            act = "不越线，保持车道"
        c = "越线" if r.get("would_do_with_C") == "cross" else "不越线"
        return f"B 说 越线 = {says} → {act}", f"若按 C（中国规则）：{c}"
    if k == "twltl":
        act = "进入中心车道等待左转（这里没有可转入的路口，之后回到原车道）" if r.get("system_says") == "allowed" else "保持车道"
        cs = r.get("c_says")
        c = {"allowed": "进入中心车道", "prohibited": "不进入"}.get(cs, f"中国规则里没有这种车道（C 答：{VAL.get(cs, cs)}）")
        return f"B 说 进中心车道等待 = {says} → {act}", f"若按 C：{c}"
    intent, choice = r.get("intent"), r.get("choice")
    if r.get("system_says") == "allowed":
        act = f"执行{ACT[intent]}"
    elif k == "approach" and choice == intent:
        act = f"本车道不能{ACT[intent]}；B 说右侧的线可以越过（{VAL.get(r.get('line_says'))}）→ 先变道到右车道，再{ACT[intent]}"
    else:
        act = f"本车道不能{ACT[intent]} → 改为{ACT.get(choice, '停车')}，再重新规划路线"
    obs = r.get("observed")
    tail = f"；车实际：{ACT.get(obs, obs)}" if obs in ACT else ""
    wc = r.get("would_do_with_C", "")
    if k == "approach":
        c = (f"C 说这条线 越线 = {VAL.get(r.get('line_c_says'))} → "
             + ("先变道再右转" if wc.startswith("change") else "不能变道，只能走本车道允许的方向"))
    else:
        c = f"C 说 {ACT[intent]} = {VAL.get(r.get('c_says'))}"
    return f"B 说 {ACT[intent]} = {says} → {act}{tail}", "若按 C：" + c


# ---------------------------------------------------------------- cards

def mark_cn(a):
    m = (a or {}).get("marking") or {}
    mt = m.get("marking_type")
    if mt == "arrow":
        return ARROW.get(m.get("arrow_type"), m.get("arrow_type") or "?") + "箭头"
    return MARK.get(mt, mt or "?")


def stop_card(run, rec, ans, n_stops):
    im, d = canvas()
    k = rec["stop"]
    d.text((50, 20), f"站点 {k}/{n_stops}：{LABEL.get(rec['label'], rec['label'])}", font=f_h2, fill=YEL)
    d.text((50, 64), f"{rec['map']} road {rec['road_id']} lane {rec['lane_id']}   ·   路线意图（模型不知道）：{INTENT.get(rec.get('intent'), rec.get('intent'))}",
           font=f_small, fill=GREY)
    fr = Image.open(run / "frames" / f"{k:02d}.png").convert("RGB")
    dr = ImageDraw.Draw(fr)
    for t in rec["targets"]:
        dr.rectangle(t["box"], outline=(0, 255, 255), width=4)
    im.paste(fr.resize((640, 360)), (50, 96))

    # truth and answers table
    x0, y = 720, 98
    cols = [x0, x0 + 150, x0 + 300, x0 + 420, x0 + 540, x0 + 660, x0 + 800, x0 + 920]
    for c, h in zip(cols, ["目标", "动作", "美国真值", "A", "B", "中国真值", "C"]):
        d.text((c, y), h, font=f_small, fill=CYAN if "真值" in h else GREY)
    y += 30
    for t in rec["targets"]:
        tname = "箭头" if t["kind"] == "arrow" else ("中心车道" if t["kind"] == "twltl" else "这条线")
        cached = any(a.get("cached") for a in ans if a["target"] == t["name"])
        for x in RELEVANT[t["kind"]]:
            d.text((cols[0], y), tname + ("（沿用）" if cached else ""), font=f_small, fill=AMBER if cached else WHITE)
            d.text((cols[1], y), ACT[x], font=f_small, fill=WHITE)
            for ci, e, tk in ((2, None, "B"), (3, "A", "B"), (4, "B", "B"), (5, None, "C"), (6, "C", "C")):
                tr = t["truth"][tk][x]
                if e is None:
                    d.text((cols[ci], y), VAL.get(tr, tr), font=f_small, fill=CYAN)
                    continue
                a = next((a for a in ans if a["target"] == t["name"] and a["experiment"] == e), {})
                v = ((a.get("answer") or {}).get("actions") or {}).get(x)
                if tr in ("allowed", "prohibited"):
                    d.text((cols[ci], y), ("✓" if v == tr else "×") + VAL.get(v, v), font=f_small, fill=GREEN if v == tr else RED)
                else:
                    d.text((cols[ci], y), VAL.get(v, v), font=f_small, fill=AMBER)
            y += 26
        d.text((cols[0], y), "识别为", font=f_tiny, fill=GREY)
        for ci, e in ((3, "A"), (4, "B"), (6, "C")):
            a = next((a for a in ans if a["target"] == t["name"] and a["experiment"] == e), {})
            d.text((cols[ci], y), mark_cn(a.get("answer")), font=f_tiny, fill=WHITE)
        y += 30
    if any(t.get("override_note") for t in rec["targets"]):
        y = para(d, x0, y, CW - 60 - x0, "注：地图数据把这条线标成黄实线，但画面上是白实线（我目测核对过），真值按白实线算。", f=f_tiny, fill=AMBER) + 4
    if any(t["truth"]["C"].get(x) == "undecided" for t in rec["targets"] for x in RELEVANT[t["kind"]]):
        y = para(d, x0, y, CW - 60 - x0, "“未定”：你的中国规则表里这一格没有给值（GB 5768.3 规则文件里没有这种标线或这种动作），C 的答案不计分。",
                 f=f_tiny, fill=AMBER) + 4
    d.rounded_rectangle([x0 - 10, max(y, 330), CW - 50, 456], radius=8, fill=PANEL)
    b, c = car_cn(rec)
    if rec.get("action_cn"):
        b = rec["action_cn"]
    yy = max(y, 330) + 10
    d.text((x0, yy), "车怎么做（按 B）", font=f_small, fill=YEL)
    yy = para(d, x0 + 150, yy, CW - 70 - x0 - 150, b, f=f_small, fill=WHITE, max_lines=2, gap=3)
    para(d, x0 + 150, yy + 2, CW - 70 - x0 - 150, c, f=f_small, fill=GREY, max_lines=2, gap=3)

    # Step 2 of A, B, C in one line each (the full traces follow on their own card)
    y = 476
    d.text((50, y), "Step 2 Rule（各实验的规则推理，原文；完整推理过程见下一张）", font=f_h3, fill=CYAN)
    y += 40
    for t in rec["targets"]:
        if len(rec["targets"]) > 1:
            d.text((50, y), "箭头" if t["kind"] == "arrow" else "这条线", font=f_small, fill=YEL)
            y += 26
        for e in "ABC":
            a = next((a for a in ans if a["target"] == t["name"] and a["experiment"] == e), {})
            an = a.get("answer") or {}
            cid = an.get("cited_rule_id")
            txt = (an.get("rule_reasoning") or "—") + (f"   [cited {cid}]" if cid else ("   [no citation]" if e != "A" else ""))
            d.text((50, y), e, font=f_h3, fill=BLUE)
            y = para(d, 90, y + 2, CW - 150, txt, f=f_txt, fill=WHITE, max_lines=2, gap=4) + 8
    return im


def trace_card(rec, ans, n_stops, ti):
    """The project's trace (agent.trace) of A, B and C for one target, full height."""
    im, d = canvas()
    main = rec["targets"][ti]
    what = "箭头" if main["kind"] == "arrow" else ("中心车道" if main["kind"] == "twltl" else "这条线")
    d.text((50, 18), f"站点 {rec['stop']}/{n_stops}：{LABEL.get(rec['label'], rec['label'])} · {what}的推理过程"
           f"（项目 trace 原样输出）", font=f_h2, fill=YEL)
    pw = (CW - 100 - 2 * 20) // 3
    for i, e in enumerate("ABC"):
        px, py = 50 + i * (pw + 20), 70
        d.rounded_rectangle([px, py, px + pw, CH - 12], radius=8, fill=PANEL)
        a = next((a for a in ans if a["target"] == main["name"] and a["experiment"] == e), {})
        d.text((px + 12, py + 8), EXP[e] + ("（沿用）" if a.get("reused") else ""), font=f_h3, fill=BLUE)
        text = TRACE(a, main["labels"][e]) if a else "no answer"
        y = py + 44
        for ln in text.split("\n"):
            if y > CH - 30:
                d.text((px + 12, y), "…", font=f_mono, fill=GREY)
                break
            bad = "UNSAFE" in ln or " wrong" in ln
            col = RED if bad else ((120, 200, 255) if ln.startswith(("Step", "Result", "Model's")) else (215, 215, 215))
            d.text((px + 12, y), ln, font=f_mono, fill=col)
            y += 16
    return im


def intro_card(meta, n_stops):
    im, d = canvas()
    d.text((80, 50), "Reasoning-drive × CARLA：一条连贯的导航路线，经过所有道线", font=f_h1, fill=YEL)
    y = 135
    blocks = [
        ("直接用项目本身（configs/experiment.yaml 里选的提示词版本）", [
            "每到一站，相机画面存成一张图，像一张标注好的图片一样交给项目的 agent.runner.ask：你的提示词、画框方式、API 调用、解析、打分（有争议的格子单独算）都不改。",
            "标签由各国规则表 regulations/<国家>/action_rules.json 填出；推理过程用项目的 trace 原样打印：Step 1 Look → Step 2 Rule（含引用条文）→ Step 3 Decide（每个动作一条理由）→ Step 4 Check → Result。"]),
        ("每站各问一次", [
            "A：Test A，美国，只看图。   B：Test B，美国，图 + MUTCD 条文。   C：Test B，中国条文 GB 5768.3，用的还是美国道路的图（提示里写“拍摄于中国”）。",
            "以前问过的同一个目标不再问（同一条路、同一条车道、同一段），直接沿用之前的回答并用你的打分重新算分；画面上标“沿用”。"]),
        ("先有导航，再有动作", [
            f"出发前先算好整条循环路线（{n_stops} 站，约 {meta.get('loop_m', 0) / 1000:.1f} km）和每站的意图；开车时小地图一直显示导航路线和下一条指令。",
            "模型不知道意图，只回答“这条标线允许什么”。导航意图 + B 的答案 → 执行或拒绝；拒绝时改走允许的方向并重新规划路线。C 的答案只记录“在中国会怎么做”。",
            "环岛：你的提示词还没有环岛的设计，这里只问环岛里的车道线（白虚线），不涉及让行、出环规则。"]),
    ]
    for head, lines in blocks:
        d.text((80, y), head, font=f_h3, fill=CYAN)
        y += 40
        for ln in lines:
            y = para(d, 110, y, CW - 220, ln, f=f_txt, fill=WHITE) + 6
        y += 12
    d.text((80, CH - 60), f"{meta['map']} · 天气 {meta['weather']}{' 夜间' if meta.get('night') else ''} · 模型 {meta['model']} · "
           f"reasoning effort {meta['reasoning_effort']} · reasoning summary {meta.get('reasoning_summary')}", font=f_small, fill=GREY)
    return im


def map_card(run, recs):
    im, d = canvas()
    d.text((80, 36), "导航路线（出发前规划）：灰点 = 车道，蓝线 = 规划路线，数字 = 站点", font=f_h2, fill=YEL)
    data = json.loads((run / "route.json").read_text(encoding="utf-8"))
    plan = json.loads((run / "nav_plan.json").read_text(encoding="utf-8"))
    path = plan.get("path") or data["track"]
    pts = data["lanes"] + path
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    box = (60, 100, 1000, CH - 30)
    sc = min((box[2] - box[0]) / (x1 - x0), (box[3] - box[1]) / (y1 - y0))

    def P(p):
        return (box[0] + (p[0] - x0) * sc, box[1] + (p[1] - y0) * sc)
    for p in data["lanes"]:
        d.point(P(p), fill=(85, 85, 85))
    if len(path) > 1:
        d.line([P(p) for p in path], fill=(90, 200, 240), width=4)
    for st in plan["stops"]:
        q = P(st["xy"])
        d.ellipse([q[0] - 16, q[1] - 16, q[0] + 16, q[1] + 16], fill=YEL)
        d.text((q[0] - 7, q[1] - 13), str(st["stop"]), font=f_h3, fill=(0, 0, 0))
    y = 100
    for st in plan["stops"]:
        d.text((1040, y), f"{st['stop']}", font=f_h3, fill=YEL)
        y = para(d, 1080, y, 790, f"{st['label_cn']} → 意图：{st['intent_cn']}", f=f_txt, fill=WHITE, max_lines=1)
        dirs = "，".join(f"{dd} 米后{t}" for dd, t in st["directions"][:5]) or "沿车道行驶"
        y = para(d, 1080, y, 790, f"本段 {st['leg_m']} 米：{dirs}", f=f_tiny, fill=GREY, max_lines=2) + 8
    d.text((1040, y + 4), f"全程约 {plan['total_m'] / 1000:.2f} km，最后回到起点", font=f_small, fill=CYAN)
    return im


def results_card(summary, recs, findings):
    im, d = canvas()
    d.text((80, 44), f"结果：{summary['meta']['route']}（{len(recs)} 个站点，一条循环路线，你的系统原样打分）", font=f_h1, fill=YEL)
    y = 130
    cols = [80, 470, 660, 880, 1020, 1200, 1400, 1580]
    for c, h in zip(cols, ["", "Output 1", "Output 2", "不安全", "过度保守", "有争议格子不一致", "引用被接受", "新问/沿用/费用"]):
        d.text((c, y), h, font=f_h3, fill=GREY)
    y += 44
    for e in "ABC":
        p = summary["per_experiment"][e]
        d.text((cols[0], y), EXP[e], font=f_mid, fill=WHITE)
        d.text((cols[1], y), f"{p['output1_correct']}/{p['answers']}", font=f_mid, fill=GREEN if p["output1_correct"] == p["answers"] else RED)
        d.text((cols[2], y), f"{p['output2_correct']}/{p['output2_scored']}", font=f_mid,
               fill=GREEN if p["output2_correct"] == p["output2_scored"] else RED)
        d.text((cols[3], y), str(p["unsafe"]), font=f_mid, fill=RED if p["unsafe"] else GREEN)
        d.text((cols[4], y), str(p["over_cautious"]), font=f_mid, fill=AMBER if p["over_cautious"] else GREEN)
        d.text((cols[5], y), str(p["contested_disagree"]), font=f_mid, fill=AMBER if p["contested_disagree"] else GREEN)
        cit = p.get("citations") or {}
        d.text((cols[6], y), f"{cit.get('accepted', 0)}/{sum(cit.values())}" if cit else "—", font=f_mid, fill=WHITE)
        d.text((cols[7], y), f"{p['asked_now']}/{p['reused']}/${p['cost_usd']:.3f}", font=f_mid, fill=WHITE)
        y += 40
    y += 10
    d.text((80, y), "Output 2 只算标签确定、且不是有争议格子的动作（和你 README 的打分一样）；C 在双向左转车道上中国表留空，不计分。", font=f_small, fill=GREY)
    y += 40
    for txt, col in findings:
        y = para(d, 80, y, CW - 160, "• " + txt, f=f_txt, fill={"red": RED, "green": GREEN, "amber": AMBER}.get(col, WHITE)) + 8
    return im


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        raise SystemExit("usage: python main.py carla video <run folder> [findings.json] [--out file.mp4]")
    run = Path(argv[0])
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else run / "route_replay.mp4"
    rest = [a for i, a in enumerate(argv[1:], 1) if a != "--out" and argv[i - 1] != "--out"]
    f = Path(rest[0]) if rest else run / "findings.json"
    findings = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    tmp = Path(tempfile.mkdtemp())
    summary = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    recs = [json.loads(l) for l in open(run / "stops.jsonl", encoding="utf-8")]
    ans = [json.loads(l) for l in open(run / "answers.jsonl", encoding="utf-8")]
    marks = json.loads((run / "markers.json").read_text(encoding="utf-8"))
    mk = {m["stop"]: m for m in marks}
    recs = [r for r in recs if r["stop"] in mk]
    global TRACE
    TRACE = project_traces()
    parts = [still(intro_card(summary["meta"], len(recs)), 22, tmp, "intro"), still(map_card(run, recs), 16, tmp, "map")]
    if "plan" in mk:
        p = clip(run, tmp, "plan", mk["plan"]["start"], mk["plan"]["end"], 1, "出发前：导航路线", "实时窗口先显示整条导航路线和每一站的意图，然后才开车。")
        if p:
            parts.append(p)
    for r in recs:
        k, m = r["stop"], mk[r["stop"]]
        name = LABEL.get(r["label"], r["label"])
        for p in (clip(run, tmp, f"drive{k}", m["drive_start"], m["ask"], 4, f"站点 {k}：按导航开往 {name}",
                       "下方小地图：蓝线 = 导航路线，红点 = 车，黄点 = 站点；右侧：下一条导航指令和到站后的意图。"),
                  clip(run, tmp, f"ask{k}", m["ask"], m["answered"] + 10, 1, f"站点 {k}：{name} · 仿真暂停，用你的系统问 A、B、C",
                       "agent.runner.ask：A = Test A（美国），B = Test B（美国 MUTCD），C = Test B（中国 GB 5768.3，美国道路）。"),
                  clip(run, tmp, f"act{k}", m.get("traces_done", m["answered"]), m["maneuver_end"], 1, f"站点 {k}：导航意图 vs B 的答案 → 执行",
                       "导航意图：" + INTENT.get(r.get("intent"), r.get("intent") or "") + "    " + (r.get("action_cn") or "")),
                  still(stop_card(run, r, [a for a in ans if a["stop"] == k], len(recs)), 12, tmp, f"card{k}"),
                  *[still(trace_card(r, [a for a in ans if a["stop"] == k], len(recs), ti), 24, tmp, f"trace{k}_{ti}")
                    for ti in range(len(r["targets"]))]):
            if p:
                parts.append(p)
    if "loop" in mk:
        p = clip(run, tmp, "loop", mk["loop"]["drive_start"], mk["loop"]["drive_end"], 4, "回到起点：路线闭合", "")
        if p:
            parts.append(p)
    parts.append(still(results_card(summary, recs, findings), 26, tmp, "results"))
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                    "-movflags", "+faststart", str(out)], check=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
