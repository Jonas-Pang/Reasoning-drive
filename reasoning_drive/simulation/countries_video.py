"""Video of a countries run (simulation/countries.py): what was done, the full prompts, then for every country and scene
the drive to the place, the photo as sent, the reasoning of Test A and Test B step by step, the decision and what the
car did, and the results table at the end.

    python main.py carla countries-video results/carla/<run>     writes <run>/countries_video.mp4

Left-hand countries are shown flipped left to right, as their model saw them. The prompts are shown in full once:
the developer message of Test A, the answer schema, and for each country its user message and what Test B adds
(the rule passages and the steps that use them). Uses ffmpeg (H.264) when it is on the PATH, else OpenCV's MPEG-4.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CW, CH, FPS = 1920, 1080, 25
FONTS = {False: ["C:/Windows/Fonts/msyh.ttc", "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", "C:/Windows/Fonts/simhei.ttf",
                 "/System/Library/Fonts/PingFang.ttc"],
         True: ["C:/Windows/Fonts/msyhbd.ttc", "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", "C:/Windows/Fonts/simhei.ttf",
                "/System/Library/Fonts/PingFang.ttc"]}
BG, PANEL = (18, 20, 24), (30, 33, 40)
WHITE, GREY, GREEN, RED, YEL, BLUE, AMBER = (235, 235, 235), (150, 150, 150), (90, 220, 120), (255, 110, 110), (255, 215, 70), \
    (120, 190, 255), (230, 190, 120)
NAME_CN = {"US": "美国", "CN": "中国", "UK": "英国", "JP": "日本", "IN": "印度", "SG": "新加坡"}
VAL_CN = {"allowed": "允许", "prohibited": "禁止", "not_determined": "无法确定", "not_applicable": "不适用"}
ACT_CN = {"change_left": "向左变道", "change_right": "向右变道", "go_straight": "直行", "turn_left": "左转", "turn_right": "右转",
          "u_turn": "掉头", "enter_waiting_area": "进入待转区"}
SECONDS = {"title": 6, "prompt_page": 6, "trace_page": 9, "photo": 4, "decision": 7, "country": 5, "results": 12}


def _font(size, bold=False):
    for f in FONTS[bold]:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


F = {k: _font(*v) for k, v in {"h1": (44, True), "h2": (32, True), "h3": (24, True), "mid": (24, False), "txt": (20, False),
                                "small": (17, False), "code": (16, False)}.items()}


def wrap(text: str, font, width: int) -> list[str]:
    """Lines no wider than width pixels; breaks at spaces, and anywhere inside Chinese or Japanese text."""
    out = []
    for para in text.split("\n"):
        if not para.strip():
            out.append("")
            continue
        indent = len(para) - len(para.lstrip(" "))
        line, word = "", ""
        tokens, cur = [], ""
        for ch in para:
            if ch == " " or ord(ch) > 0x2E80:
                if cur:
                    tokens.append(cur)
                    cur = ""
                tokens.append(ch)
            else:
                cur += ch
        if cur:
            tokens.append(cur)
        for t in tokens:
            if font.getlength(line + t) <= width or not line.strip():
                line += t
                while font.getlength(line) > width and len(line) > 1:  # one very long token
                    cut = len(line) - 1
                    while cut > 1 and font.getlength(line[:cut]) > width:
                        cut -= 1
                    out.append(line[:cut])
                    line = " " * indent + line[cut:]
            else:
                out.append(line.rstrip())
                line = " " * indent + (t.lstrip() if t == " " else t)
        out.append(line.rstrip())
        del word
    return out


def canvas():
    img = Image.new("RGB", (CW, CH), BG)
    return img, ImageDraw.Draw(img)


def to_bgr(img: Image.Image) -> np.ndarray:
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


class Video:
    def __init__(self, path: Path):
        self.path = path
        self.tmp = path.with_suffix(".raw.mp4")
        self.w = cv2.VideoWriter(str(self.tmp), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (CW, CH))
        self.frames = 0

    def still(self, img: Image.Image, seconds: float):
        f = to_bgr(img)
        for _ in range(int(seconds * FPS)):
            self.w.write(f)
        self.frames += int(seconds * FPS)

    def frame(self, bgr: np.ndarray):
        self.w.write(bgr)
        self.frames += 1

    def close(self) -> Path:
        self.w.release()
        ff = shutil.which("ffmpeg")
        if ff:
            r = subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(self.tmp), "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
                                "-pix_fmt", "yuv420p", str(self.path)])
            if r.returncode == 0:
                self.tmp.unlink()
                return self.path
        self.tmp.replace(self.path)
        return self.path


def text_pages(title: str, subtitle: str, body: str, font=None, colour=WHITE) -> list[Image.Image]:
    font = font or F["code"]
    width, top, line_h = CW - 120, 150, int(font.size * 1.45)
    lines = wrap(body, font, width)
    per = (CH - top - 50) // line_h
    pages = [lines[i:i + per] for i in range(0, len(lines), per)] or [[]]
    out = []
    for k, chunk in enumerate(pages, 1):
        img, d = canvas()
        d.text((60, 36), title + (f"  ({k}/{len(pages)})" if len(pages) > 1 else ""), font=F["h2"], fill=YEL)
        d.text((60, 90), subtitle, font=F["small"], fill=GREY)
        d.rectangle([40, top - 14, CW - 40, CH - 30], fill=PANEL)
        y = top
        for ln in chunk:
            d.text((60, y), ln, font=font, fill=colour)
            y += line_h
        out.append(img)
    return out


def compact_json(x, ind=0) -> str:
    """JSON with one key per line, lists of plain values on one line (the schema on few pages)."""
    pad = "  " * ind
    flat = json.dumps(x, ensure_ascii=False)
    if isinstance(x, (dict, list)) and len(flat) <= 90 and flat.count("{") <= 2:
        return flat
    if isinstance(x, dict):
        if not x:
            return "{}"
        inner = ",\n".join(f"{pad}  {json.dumps(k)}: {compact_json(v, ind + 1)}" for k, v in x.items())
        return "{\n" + inner + "\n" + pad + "}"
    if isinstance(x, list) and all(not isinstance(i, (dict, list)) for i in x):
        return json.dumps(x, ensure_ascii=False)
    if isinstance(x, list):
        return "[\n" + ",\n".join(pad + "  " + compact_json(i, ind + 1) for i in x) + "\n" + pad + "]"
    return json.dumps(x, ensure_ascii=False)


def added_lines(a: str, b: str) -> str:
    """The lines of b that a does not have, in b's order (what Test B adds to the Test A developer message)."""
    have = set(a.splitlines())
    return "\n".join(ln for ln in b.splitlines() if ln not in have).strip()


def card(title: str, rows: list[tuple[str, str]], colour=WHITE) -> Image.Image:
    img, d = canvas()
    d.text((80, 70), title, font=F["h1"], fill=YEL)
    y = 170
    for kind, text in rows:
        f = {"h": F["h3"], "t": F["mid"], "s": F["small"]}[kind]
        for ln in wrap(text, f, CW - 180):
            d.text((90 if kind == "h" else 110, y), ln, font=f, fill=BLUE if kind == "h" else (GREY if kind == "s" else colour))
            y += int(f.size * 1.5)
        y += 10 if kind != "h" else 4
    return img


def load_frame(d: Path, name: str, k: int, mirror: bool):
    p = d / f"{name}_{k:05d}.jpg"
    img = cv2.imread(str(p)) if p.exists() else None
    if img is not None and mirror:
        img = cv2.flip(img, 1)
    return img


def compose(front, chase, lines: list[tuple[str, tuple]], big: tuple[str, tuple] | None = None) -> np.ndarray:
    base = np.full((CH, CW, 3), BG[::-1], np.uint8)
    if front is not None:
        base[0:720, 0:1280] = cv2.resize(front, (1280, 720))
    if chase is not None:
        base[0:360, 1280:1920] = cv2.resize(chase, (640, 360))
    img = Image.fromarray(cv2.cvtColor(base, cv2.COLOR_BGR2RGB))
    d = ImageDraw.Draw(img)
    d.rectangle([1280, 360, 1920, 1080], fill=PANEL)
    d.rectangle([0, 720, 1280, 1080], fill=PANEL)
    d.text((1296, 372), "跟车视角 chase camera", font=F["small"], fill=GREY)
    if big:
        yb = 745
        for ln in wrap(big[0], F["h2"], 1220)[:7]:
            d.text((30, yb), ln, font=F["h2"], fill=big[1])
            yb += 46
    y = 400
    for text, colour in lines:
        for ln in wrap(text, F["txt"], 600):
            d.text((1296, y), ln, font=F["txt"], fill=colour)
            y += 30
        y += 6
    return to_bgr(img)


def swap_lr(text: str) -> str:
    """Left and right exchanged, for the label of a scene as a mirrored country saw it."""
    import re
    return re.sub(r"\b(left|right)\b", lambda m: {"left": "right", "right": "left"}[m.group(1)], text)


def acts_text(acts: dict) -> str:
    keys = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn"]
    return "，".join(f"{ACT_CN[k]} {VAL_CN.get(acts.get(k), acts.get(k) or '—')}" for k in keys if k in acts) or "没有可读的答案"


def key_actions(r: dict) -> list[str]:
    """The actions that decide the scene, in the photo's frame: the intent, and for a turn also the lane change towards it."""
    i = r["intent_in_photo"]
    return [i] if i.startswith("change_") else [i, "change_right" if i.endswith("right") else "change_left"]


def results_table(meta: dict, recs: list[dict]) -> Image.Image:
    img, d = canvas()
    d.text((80, 50), "结果：同一张地图、同样的地方，四个国家", font=F["h1"], fill=YEL)
    cols = [(80, "国家"), (260, "场景"), (470, "意图（照片里）"), (700, "Test A"), (1060, "Test B"), (1420, "车（按 Test B）")]
    y = 140
    for x, t in cols:
        d.text((x, y), t, font=F["h3"], fill=BLUE)
    y += 50
    colour = {"allowed": GREEN, "prohibited": RED}
    for r in recs:
        d.text((80, y), NAME_CN.get(r["country"], r["country"]) + ("（镜像）" if r["mirrored"] else ""), font=F["txt"], fill=WHITE)
        d.text((260, y), r["scene"], font=F["txt"], fill=WHITE)
        d.text((470, y), ACT_CN.get(r["intent_in_photo"], r["intent_in_photo"]), font=F["txt"], fill=WHITE)
        for x, t in ((700, "A"), (1060, "B")):
            yy = y
            for a in key_actions(r):
                val = (r["actions"].get(t) or {}).get(a)
                d.text((x, yy), f"{ACT_CN.get(a, a)}：{VAL_CN.get(val, val or '—')}", font=F["txt"], fill=colour.get(val, AMBER))
                yy += 28
        for k, ln in enumerate(wrap(r["drove"].get("text_cn") or r["drove"]["text"], F["small"], 460)[:3]):
            d.text((1420, y + k * 24), ln, font=F["small"], fill=GREEN if r["drove"].get("does_intent") else AMBER)
        y += 70
    notes = [f"总花费约 ${sum(r['cost_usd'] for r in recs):.3f}；每个答案的完整推理见 answers.jsonl 和各场景的 trace_A/B.txt。"]
    notes += [f"{NAME_CN.get(c, c)}的规则条文是还没审核的草稿。" for c, i in meta["countries"].items() if i["draft_passages"]]
    for n in notes:
        d.text((80, y + 10), n, font=F["small"], fill=GREY)
        y += 30
    return img


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        raise SystemExit("python main.py carla countries-video <results/carla/run>")
    run = Path(argv[0])
    res = json.loads((run / "results.json").read_text(encoding="utf-8"))
    prompts = json.loads((run / "prompts.json").read_text(encoding="utf-8"))
    meta, recs = res["meta"], res["records"]
    countries = list(meta["countries"])
    out = run / "countries_video.mp4"
    v = Video(out)

    v.still(card("同一张地图，四个国家：" + "、".join(NAME_CN.get(c, c) for c in countries), [
        ("h", "做了什么"),
        ("t", f"CARLA {meta.get('carla_server', '')}，地图 {meta['map']}，天气 {meta.get('weather', '')}。同样的路口和路段，车开过去停下，"
              f"拍下的照片交给项目的车道任务（提示词 {meta['prompt']}，模型 {meta['model']}）。"),
        ("t", "每个地方问两次：Test A 只给照片和国家；Test B 再加上该国的规则条文。车按 Test B 的答案执行导航意图（允许才做），"
              "然后继续开，所以答案决定了后面发生的事（闭环）。Test A 会怎么做也记录下来。"),
        ("h", "左侧通行的国家"),
        ("t", "CARLA 的城镇都是右侧通行。英国、日本的照片先左右翻转再发给模型（镜像世界：车靠左行驶，左转箭头变成右转箭头），"
              "答案里的左右再翻回来驾驶；视频里这两个国家的画面也是翻转后的样子。"),
        ("h", "场景"),
        *[("t", f"{k}：{s['label']}；导航意图（右侧通行的画面里）：{s.get('intent_text', s['intent'])}") for k, s in meta["scenes"].items()],
        ("s", "规则条文：" + "；".join(f"{NAME_CN.get(c, c)} {i['passages']} 条" + ("（草稿，未审核）" if i["draft_passages"] else "")
                                  for c, i in meta["countries"].items()) + ("。答案为模拟（MOCK）" if meta.get("mock") else ""))]),
        SECONDS["title"] + 4)

    first = prompts[f"{countries[0]}|A"]
    v.still(card("提示词（完整打印）", [
        ("t", "下面先给出 Test A 的开发者消息（所有国家相同），然后是答案的 JSON 结构；每个国家再给出它的用户消息，"
              "以及 Test B 在开发者消息里加进去的内容（规则条文和使用条文的步骤）。完整文本也在 prompts.md 里。")]), 5)
    for page in text_pages("Test A 开发者消息（所有国家相同）", f"{meta['prompt']}  ·  developer message, then the user message and the photo",
                           first["instructions"]):
        v.still(page, SECONDS["prompt_page"])
    schema_path = run / "prompts.md"
    schema = ""
    if schema_path.exists():
        t = schema_path.read_text(encoding="utf-8")
        i = t.find("## Answer schema")
        schema = t[i:].split("```json", 1)[-1].split("```", 1)[0].strip() if i >= 0 else ""
    if schema:
        try:
            schema = compact_json(json.loads(schema))
        except ValueError:
            pass
        for page in text_pages("答案的 JSON 结构（structured output）", "the model must answer in exactly this structure",
                               schema, font=_font(15)):
            v.still(page, SECONDS["prompt_page"] - 1)

    for c in countries:
        info = meta["countries"][c]
        mirror = info["mirrored"]
        pa, pb = prompts.get(f"{c}|A"), prompts.get(f"{c}|B")
        v.still(card(f"{NAME_CN.get(c, c)}（{c}）", [
            ("t", f"{info['name']}，{'左' if info['driving_side'] == 'left' else '右'}侧通行"
                  + ("，画面左右翻转（镜像世界）" if mirror else "")),
            ("t", f"规则条文 {info['passages']} 条" + ("，来自还没审核的草稿" if info["draft_passages"] else "")),
            ("h", "用户消息（Test A 和 Test B 相同，后面跟照片）"),
            ("t", (pa or pb or {}).get("user_text", ""))]), SECONDS["country"])
        if pa and pb:
            for page in text_pages(f"{NAME_CN.get(c, c)}：Test B 在开发者消息里加的内容", "the rule passages and the steps that use them",
                                   added_lines(pa["instructions"], pb["instructions"])):
                v.still(page, SECONDS["prompt_page"])
        for r in [x for x in recs if x["country"] == c]:
            d = run / c / r["scene"]
            if mirror:
                r = dict(r, label=swap_lr(r["label"]), intent_text=swap_lr(r["intent_text"]))
            head = f"{NAME_CN.get(c, c)} · {r['scene']}：{r['label']}"
            intent = r["intent_in_photo"]
            for k in range(r["first_frame"], r["stop_frame"]):
                v.frame(compose(load_frame(d, "front", k, mirror), load_frame(d, "chase", k, mirror), [
                    (head, YEL), (f"导航意图（模型不知道）：{ACT_CN.get(intent, intent)}", WHITE),
                    ("开往这个地方，到了就停车拍照" + ("（画面已左右翻转）" if mirror else ""), GREY)],
                    (f"{NAME_CN.get(c, c)}{'（左侧通行，镜像）' if mirror else ''}：开往场景 {r['scene']}，"
                     f"到了停车，拍照问 Test A 和 Test B。导航意图：{ACT_CN.get(intent, intent)}", WHITE)))
            sent = cv2.imread(str(d / "photo_sent.png"))
            if sent is not None:
                img = Image.fromarray(cv2.cvtColor(cv2.resize(sent, (1536, 864)), cv2.COLOR_BGR2RGB))
                cv = Image.new("RGB", (CW, CH), BG)
                cv.paste(img, (192, 150))
                dd = ImageDraw.Draw(cv)
                dd.text((80, 50), f"{NAME_CN.get(c, c)} · {r['scene']}：发给模型的照片" + ("（左右翻转后）" if mirror else ""), font=F["h2"], fill=YEL)
                dd.text((80, 100), f"{r['label']}  ·  车停住，模拟暂停；同一张照片问 Test A 和 Test B", font=F["small"], fill=GREY)
                v.still(cv, SECONDS["photo"])
            for t in meta["tests"]:
                tp = d / f"trace_{t}.txt"
                if tp.exists():
                    sub = "photo and country only" if t == "A" else "photo, country and the rule passages"
                    for page in text_pages(f"{NAME_CN.get(c, c)} · {r['scene']}：Test {t} 的推理过程", sub, tp.read_text(encoding="utf-8"),
                                           font=F["code"]):
                        v.still(page, SECONDS["trace_page"])
            a, b = r["actions"].get("A", {}), r["actions"].get("B", {})
            colour = GREEN if r["drove"].get("does_intent") else AMBER
            v.still(card(f"{head}：决定", [
                ("h", "导航意图"), ("t", f"{ACT_CN.get(intent, intent)}（{r['intent_text']}" + ("，镜像后左右互换" if mirror else "") + "）"),
                ("h", "Test A（只看照片）"), ("t", acts_text(a)),
                ("h", "Test B（照片 + 规则条文）"), ("t", acts_text(b)),
                ("h", f"车按 Test {meta['drive_with']} 执行"), ("t", r["drove"].get("text_cn") or r["drove"]["text"]),
                ("s", "实际驾驶（CARLA 里车的动作，右侧通行的原始坐标）：" + (r.get("manoeuvre") or "")),
                ("s", "Test A 的话会：" + ((r["decisions"].get("A") or {}).get("text_cn") or (r["decisions"].get("A") or {}).get("text", "")) +
                 f"；花费约 ${r['cost_usd']}" + ("（答案来自缓存）" if all(r.get("cached", {}).values()) else ""))], colour),
                SECONDS["decision"])
            for k in range(r["act_frame"], r["frames"]):
                fr = compose(load_frame(d, "front", k, mirror), load_frame(d, "chase", k, mirror), [
                    (head, YEL), (f"Test B：{acts_text(b)}", WHITE)],
                    (f"执行（按 Test {meta['drive_with']}）：{r['drove'].get('text_cn') or r['drove']['text']}", colour))
                v.frame(fr)
                v.frame(fr)  # the manoeuvre at about real speed

    v.still(results_table(meta, recs), SECONDS["results"])
    path = v.close()
    print(f"Video: {path} ({v.frames / FPS:.0f} s)")
    return path


if __name__ == "__main__":
    main()
