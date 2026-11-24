"use strict";
// Blind review of the lane answers that disagree with the label (reasoning_drive/review.py).
// The page shows the values of the label and of the answers as options without saying where they come from.
const LANG_KEY = "lane-demo-lang", REVIEWER_KEY = "lane-review-reviewer";
const T = {
  zh: {
    title: "盲审", region: "地区", only_open: "只看未审", reviewer: "审核人", back: "回到演示页", lang: "English",
    intro: "这里列出模型答案和标签不一致的地方。每个选项来自标签或某次模型回答，顺序打乱，不显示来源。只按照片判断；看不清就选“看不清”。决定保存在 results/runs/review/lane_review.csv，标签文件本身不改。",
    keys: "数字键选择 · 0 看不清 · ← → 换题", progress: "进度", effect: "盲审前 → 盲审后", effect_btn: "计算",
    effect_help: "用已保存的决定重新评分（不调用 API）。", list: "全部题目", saved: "已保存", none: "这个地区没有需要审的地方。",
    q_boundary: "本车道{side}侧的边界是哪一种线？", q_marking: "本车道内（从画面底部到停止线或车道尽头）画着「{tok}」吗？",
    q_action: "按{region}的标线规则，本车道的「{act}」应该是？",
    h_boundary: "看颜色、线型（实线/虚线/虚实线时哪条靠本车道）和有没有路缘，只看能看到的油漆。",
    h_marking: "只算本车道里的；停止线之后的人行横道不算在本车道内。", h_action: "边界只决定该侧变道，车道内箭头决定四个方向；画面里没有标线管这个动作就是“不适用”。",
    left: "左", right: "右", yes: "有", no: "没有", cannot: "看不清 / 无法判断",
    decided: "已审 {d} / {n}，{i} 张图", kind_boundary: "边界", kind_marking: "标线", kind_action: "动作",
    near: "靠本车道一侧：{x}", curb: "有路缘", no_curb: "无路缘", run: "运行", test: "测试", before: "前", after: "后",
    m_lane: "车道识别", m_core: "不算横向线", m_actions: "动作", m_unsafe: "不安全", err: "出错：", n_decisions: "已保存的决定：{n}",
    CN: "中国", US: "美国",
  },
  en: {
    title: "blind review", region: "Region", only_open: "open only", reviewer: "Reviewer", back: "back to the demo", lang: "中文",
    intro: "Each item is a place where a model answer and the label disagree. The options come from the label or from model answers, in a shuffled order, without their source. Judge from the photo only; choose \"cannot tell\" when the photo does not show it. Decisions go to results/runs/review/lane_review.csv; the label files are not changed.",
    keys: "number keys choose · 0 cannot tell · ← → move", progress: "Progress", effect: "Before → after the review", effect_btn: "Compute",
    effect_help: "Scores again with the saved decisions (no API calls).", list: "All items", saved: "saved", none: "Nothing to review in this region.",
    q_boundary: "Which line forms the {side} boundary of my lane?", q_marking: "Is there a \"{tok}\" painted in my lane (from the bottom of the photo to its stop line or end)?",
    q_action: "Under the marking rules of {region}, what does my lane allow for \"{act}\"?",
    h_boundary: "Colour, pattern (for a solid-and-broken pair: which line is nearer my lane) and curb, from the paint you can see.",
    h_marking: "Only markings in my lane count; a crosswalk beyond the stop line is not in my lane.", h_action: "A boundary decides only the lane change on its side, arrows in my lane decide the four movements; nothing in view that governs it means not applicable.",
    left: "left", right: "right", yes: "yes", no: "no", cannot: "cannot tell from the photo",
    decided: "{d} / {n} decided, {i} images", kind_boundary: "boundaries", kind_marking: "markings", kind_action: "actions",
    near: "nearer my lane: {x}", curb: "curb", no_curb: "no curb", run: "Run", test: "Test", before: "before", after: "after",
    m_lane: "Lane identified", m_core: "without lines across", m_actions: "Actions", m_unsafe: "Unsafe", err: "Error: ", n_decisions: "saved decisions: {n}",
    CN: "China", US: "the United States",
  },
};
const V = {
  zh: { white: "白色", yellow: "黄色", other: "其他颜色", none: "无", solid: "实线", dashed: "虚线", dotted: "短虚线/密虚线", double_solid: "双实线",
    double_dashed: "双虚线", solid_dashed: "虚实线", allowed: "允许", prohibited: "禁止", not_determined: "无法判断", not_applicable: "不适用",
    change_left: "向左越线/变道", change_right: "向右越线/变道", go_straight: "直行", turn_left: "左转", turn_right: "右转", u_turn: "掉头",
    enter_waiting_area: "进入待转区/双向左转车道",
    "arrow:straight": "直行箭头", "arrow:left": "左转箭头", "arrow:right": "右转箭头", "arrow:straight_left": "直行或左转箭头", "arrow:straight_right": "直行或右转箭头",
    "arrow:left_right": "左右转箭头", "arrow:u_turn": "掉头箭头", "arrow:left_u_turn": "左转或掉头箭头", "arrow:straight_u_turn": "直行或掉头箭头",
    "arrow:merge_left": "向左合流箭头", "arrow:merge_right": "向右合流箭头", "arrow:two_way_left": "双向左转车道箭头",
    "no_turn:u_turn": "禁止掉头标记", "no_turn:left": "禁止左转标记", "no_turn:right": "禁止右转标记", "text:only": "ONLY 字样", "text:bus": "公交 / BUS",
    "text:hov": "多乘员 / HOV", "text:stop": "STOP / 停", "text:keep_clear": "KEEP CLEAR / 勿停", "text:speed_limit": "限速数字", "text:other": "其他文字",
    "symbol:hov_diamond": "菱形（HOV）", "symbol:bike": "自行车图形", "symbol:other": "其他图形", "area:left_turn_waiting": "左弯待转区",
    "area:two_way_left_turn_lane": "左侧的双向左转车道", "area:grid": "网状线/禁停区", "area:channelizing": "导流线/斜纹区",
    "line:stop_line": "停止线", "line:yield_line": "让行线", "line:stop_yield": "停车让行线（停）", "line:crosswalk": "人行横道" },
  en: { solid_dashed: "solid + broken", double_solid: "double solid", double_dashed: "double broken", dashed: "broken (dashed)", "line:crosswalk": "crosswalk",
    "line:stop_line": "stop line", "line:yield_line": "yield line", "text:only": "ONLY", "area:left_turn_waiting": "left-turn waiting area" },
};
const S = { lang: "zh", region: "", items: [], idx: 0, regions: {} };
try { S.lang = localStorage.getItem(LANG_KEY) || "zh"; } catch (e) { /* storage not available */ }
const $ = (id) => document.getElementById(id);
const t = (k, p) => { let s = (T[S.lang] && T[S.lang][k]) || T.en[k] || k; for (const [a, b] of Object.entries(p || {})) s = s.replace("{" + a + "}", b); return s; };
const v = (k) => (V[S.lang] && V[S.lang][k]) || (V.en[k]) || String(k).replace(/^[a-z_]+:/, "").replace(/_/g, " ");
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

async function api(path, body) {
  const r = await fetch(path, body === undefined ? {} : { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
  const j = await r.json().catch(() => ({ error: "HTTP " + r.status }));
  if (!r.ok || j.error) throw new Error(j.error || "HTTP " + r.status);
  return j;
}

function boundaryText(val) {
  const [color, pattern, near, curb] = (val + "|||").split("|");
  const parts = [color === "none" && pattern === "none" ? v("none") : `${v(color)} ${v(pattern)}`];
  if (near) parts.push(t("near", { x: v(near) }));
  parts.push(curb === "yes" ? t("curb") : t("no_curb"));
  return parts.join(" · ");
}
function optionText(it, val) {
  if (it.kind === "boundary") return boundaryText(val);
  if (it.kind === "marking") return t(val);
  return v(val);
}
function question(it) {
  if (it.kind === "boundary") return t("q_boundary", { side: t(it.key) });
  if (it.kind === "marking") return t("q_marking", { tok: v(it.key) });
  return t("q_action", { region: t(it.region), act: v(it.key) });
}
function shortId(id) { return String(id).replace(/^[a-z0-9]+_(val|test|train)__/, ""); }
function visible() { return $("only-open").checked ? S.items.filter((i) => !i.decided || i === S.items[S.idx]) : S.items; }

function render() {
  const it = S.items[S.idx];
  const d = S.items.filter((i) => i.decided).length;
  $("count").textContent = t("decided", { d, n: S.items.length, i: new Set(S.items.map((i) => i.image_id)).size });
  $("bar").style.width = (S.items.length ? (100 * d / S.items.length) : 0) + "%";
  const kinds = {};
  S.items.forEach((i) => { const k = kinds[i.kind] || (kinds[i.kind] = [0, 0]); k[1] += 1; if (i.decided) k[0] += 1; });
  $("progress-text").textContent = Object.entries(kinds).map(([k, [a, b]]) => `${t("kind_" + k)} ${a}/${b}`).join(" · ");
  $("list").innerHTML = visible().map((i) => `<li data-id="${esc(i.item_id)}" class="${i.decided ? "done" : ""} ${i === it ? "sel" : ""}"><span class="d"></span>${esc(shortId(i.image_id))} · ${esc(t("kind_" + i.kind))}: ${esc(i.kind === "boundary" ? t(i.key) : v(i.key))}</li>`).join("");
  for (const li of $("list").querySelectorAll("li")) li.addEventListener("click", () => { S.idx = S.items.findIndex((x) => x.item_id === li.dataset.id); render(); });
  if (!it) {
    $("question").textContent = t("none"); $("options").innerHTML = ""; $("img").removeAttribute("src"); $("meta").textContent = ""; $("hint").textContent = "";
    return;
  }
  const src = `/api/image?task=lane&id=${encodeURIComponent(it.image_id)}&w=1280`;
  if ($("img").getAttribute("src") !== src) $("img").src = src;
  $("meta").textContent = `${it.image_id} · ${S.idx + 1} / ${S.items.length}`;
  $("question").textContent = question(it);
  $("hint").textContent = t("h_" + it.kind);
  const opts = it.options.map((val, n) => `<button data-v="${esc(val)}" class="${it.decided && it.decided.decision === "option" && it.decided.value === val ? "chosen" : ""}"><span class="k">${n + 1}</span>${esc(optionText(it, val))}</button>`);
  opts.push(`<button data-c="1" class="cannot ${it.decided && it.decided.decision === "cannot_tell" ? "chosen" : ""}"><span class="k">0</span>${esc(t("cannot"))}</button>`);
  $("options").innerHTML = opts.join("");
  for (const b of $("options").querySelectorAll("button")) b.addEventListener("click", () => decide(b.dataset.c ? "cannot_tell" : "option", b.dataset.v || ""));
}

async function decide(decision, value) {
  const it = S.items[S.idx];
  if (!it) return;
  try {
    await api("/api/review/decide", { item_id: it.item_id, decision, value, reviewer: $("reviewer").value });
    it.decided = { decision, value };
    $("msg").className = "msg ok"; $("msg").textContent = t("saved");
    const next = S.items.findIndex((x, n) => n > S.idx && !x.decided);
    if (next >= 0) S.idx = next;
    render();
  } catch (e) { $("msg").className = "msg err"; $("msg").textContent = t("err") + e.message; }
}

async function load() {
  try {
    const r = await api(`/api/review/items?region=${encodeURIComponent(S.region)}`);
    S.items = r.items;
    const open = S.items.findIndex((i) => !i.decided);
    S.idx = open >= 0 ? open : 0;
    render();
  } catch (e) { $("question").textContent = t("err") + e.message; }
}

async function effect() {
  $("effect").textContent = "…";
  try {
    const r = await api(`/api/review/effect?region=${encodeURIComponent(S.region)}`);
    const f = (x) => (x && x.n ? `${x.correct}/${x.n}` : "—");
    const row = (e) => `<tr><td>${esc(e.test)} <span class="muted">${esc(e.run_id.slice(4, 8))}</span></td><td>${f(e.before.lane)} → ${f(e.after.lane)}</td><td>${f(e.before.lane_core)} → ${f(e.after.lane_core)}</td><td>${f(e.before.output2)} → ${f(e.after.output2)}</td><td>${e.before.unsafe_errors} → ${e.after.unsafe_errors}</td></tr>`;
    $("effect").innerHTML = `<table><tr><th>${t("test")}</th><th>${t("m_lane")}</th><th>${t("m_core")}</th><th>${t("m_actions")}</th><th>${t("m_unsafe")}</th></tr>${r.runs.map(row).join("")}</table>
      <p class="small muted">${esc(t("n_decisions", { n: r.decisions }))}</p>`;
  } catch (e) { $("effect").textContent = t("err") + e.message; }
}

function applyStatic() {
  for (const el of document.querySelectorAll("[data-t]")) el.textContent = t(el.dataset.t);
  $("lang-btn").textContent = t("lang");
  document.documentElement.lang = S.lang === "zh" ? "zh-CN" : "en";
}

async function init() {
  applyStatic();
  try { $("reviewer").value = localStorage.getItem(REVIEWER_KEY) || ""; } catch (e) { /* ignore */ }
  const c = await api("/api/config");
  S.regions = c.config.regions;
  const counts = c.lane_items_per_region || {};
  $("region").innerHTML = Object.keys(S.regions).map((code) => `<option value="${esc(code)}">${esc(code)}</option>`).join("");
  S.region = Object.keys(S.regions).find((code) => (counts[code] || {}).any) || Object.keys(S.regions)[0];
  $("region").value = S.region;
  $("region").addEventListener("change", () => { S.region = $("region").value; $("effect").innerHTML = ""; load(); });
  $("only-open").addEventListener("change", render);
  $("reviewer").addEventListener("change", () => { try { localStorage.setItem(REVIEWER_KEY, $("reviewer").value); } catch (e) { /* ignore */ } });
  $("prev").addEventListener("click", () => { if (S.idx > 0) { S.idx -= 1; render(); } });
  $("next").addEventListener("click", () => { if (S.idx < S.items.length - 1) { S.idx += 1; render(); } });
  $("effect-btn").addEventListener("click", effect);
  $("lang-btn").addEventListener("click", () => { S.lang = S.lang === "zh" ? "en" : "zh"; try { localStorage.setItem(LANG_KEY, S.lang); } catch (e) { /* ignore */ } applyStatic(); render(); });
  document.addEventListener("keydown", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT") return;
    const it = S.items[S.idx];
    if (e.key === "ArrowLeft") $("prev").click();
    else if (e.key === "ArrowRight") $("next").click();
    else if (it && e.key === "0") decide("cannot_tell", "");
    else if (it && /^[1-9]$/.test(e.key) && it.options[Number(e.key) - 1] !== undefined) decide("option", it.options[Number(e.key) - 1]);
  });
  load();
}
init();
