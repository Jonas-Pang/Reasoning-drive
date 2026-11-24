/* Offline labeling page for helpers. Runs from index.html inside an unzipped package; no server.
   Data: window.LANE_PACKAGE (data.js). Progress: localStorage. Output: results_<annotator>_<package>.json */
"use strict";

const P = window.LANE_PACKAGE;
const $ = (id) => document.getElementById(id);
const KEY = "lane-labels:" + P.package_id;
const ACTIONS = P.schema.actions;

const TXT = {
  zh: {
    brighten: "画面增亮", guide: "标注说明", import: "导入进度", export: "导出结果",
    storage_warn: "这个浏览器不能自动保存进度，请经常点“导出结果”，关闭页面前一定要导出。",
    f_todo: "未完成", f_all: "全部", f_done: "已完成",
    privacy_tool: "▨ 隐私框 (P)", delete_sel: "删除选中", loupe: "放大镜",
    stage_hint: "青色框是要判断的标线（不能修改）。在图上拖动鼠标画隐私框，盖住看得清的车牌和人脸；点一下隐私框可以选中，按 Delete 删除。",
    pick_item: "从左边选一张图开始。建议先做练习。",
    practice_bar: "练习题：做完点“检查答案”，会显示参考答案。练习不计入结果。",
    marking_type: "标线类型", arrow_type: "箭头类型", dashed_side: "虚线在哪一侧", position: "位置（相对我的车）",
    visibility: "可见性", decidable_q: "可见部分能决定行为吗？", evidence: "期望证据",
    actions: "动作", prefill: "按规则表重新预填", rules: "适用规则",
    expand_all: "全部展开", collapse_all: "全部收起", guide_print: "在新窗口打开（可打印）",
    unsure: "不确定（请写一句原因）", comment_ph: "原因或备注（可选）",
    save_done: "完成 ✓ 下一张", check_answer: "检查答案", save_draft: "存草稿",
    ack: "我已阅读标注说明和隐私须知", start: "开始", close: "关闭",
    saved_at: "已自动保存 {t}", exported: "上次导出 {t}", never_exported: "还没导出过",
    progress: "完成 <b>{d}</b>/{n}", practice_progress: "练习 {d}/{n}",
    st_todo: "未开始", st_draft: "草稿", st_done: "完成", st_unsure: "不确定", st_checked: "已检查",
    sec_practice: "练习", sec_items: "标注",
    e_marking: "请选择标线类型。", e_arrow: "请选择箭头类型。", e_position: "请选择位置。", e_dashed: "请选择虚线在哪一侧。",
    e_vis: "请选择可见性。", e_dec: "V1 需要判断可见部分能否决定行为。", e_none: "“看不到”只能配 V0。",
    e_actions: "还有动作没选：{x}。", e_partial: "证据为 {ev} 时，动作不能是“允许”或“禁止”：{x}。",
    e_rules: "请至少勾选一条适用规则。", e_unsure: "勾选“不确定”时请写原因。", w_v0: "V0 一般配“看不到”。",
    saved_draft: "已存草稿。", saved_done: "已完成。", not_done: "还不能算完成，已存为草稿：",
    all_done: "全部完成了！请点右上角“导出结果”，把下载的文件发回给项目负责人。",
    export_done: "已导出 {f}。请把这个文件发回给项目负责人。", export_none: "还没有任何结果可以导出。",
    import_ok: "已读入 {n} 张图的进度。", import_bad: "这个文件不属于这个标注包（{p}）。",
    pr_title: "你的答案和参考答案", pr_all: "全部一致 ✓", pr_some: "{m}/{n} 项一致", field: "项目", yours: "你的", ref: "参考",
    rule_ids: "适用规则", note_unset: "规则表没有预填：{x}。请按图片和规则自己判断。",
    target: "目标", privacy: "隐私", translation: "译文", original: "原文", suggested: "建议",
    region_US: "美国", region_CN: "中国", diff_table: "≠表", leave_warn: "还有没导出的结果。确定离开吗？",
    vis_tip: "V2 清晰：整条标线都看得清。\nV1 部分可见：有磨损、遮挡或太暗。线要能看出颜色和线型（虚线至少一整段线加一个间隔；实线连续长度超过一段线加一个间隔；双线两条都可见），箭头要能看到箭头头部，才算“能决定”。\nV0 没有可用证据：几乎看不到标线。",
  },
  en: {
    brighten: "Brighten", guide: "Guide", import: "Import progress", export: "Export results",
    storage_warn: "This browser cannot save your progress automatically. Export your results often, and always before closing the page.",
    f_todo: "To do", f_all: "All", f_done: "Done",
    privacy_tool: "▨ Privacy box (P)", delete_sel: "Delete selected", loupe: "Magnifier",
    stage_hint: "The cyan box is the marking to judge (fixed). Drag on the image to draw privacy boxes over readable plates and faces; click a privacy box to select it, Delete removes it.",
    pick_item: "Pick an image on the left. Start with the practice items.",
    practice_bar: "Practice: click \"Check answer\" to see the reference answer. Practice does not count.",
    marking_type: "Marking type", arrow_type: "Arrow type", dashed_side: "Broken-line side", position: "Position (relative to our car)",
    visibility: "Visibility", decidable_q: "Does the visible part decide the behavior?", evidence: "Expected evidence",
    actions: "Actions", prefill: "Prefill from rule table", rules: "Rules",
    expand_all: "Expand all", collapse_all: "Collapse all", guide_print: "Open in a new window (printable)",
    unsure: "Unsure (write one sentence why)", comment_ph: "Reason or note (optional)",
    save_done: "Done ✓ next", check_answer: "Check answer", save_draft: "Save draft",
    ack: "I have read the guide and the privacy note", start: "Start", close: "Close",
    saved_at: "Saved in this browser {t}", exported: "Last export {t}", never_exported: "Not exported yet",
    progress: "Done <b>{d}</b>/{n}", practice_progress: "Practice {d}/{n}",
    st_todo: "Not started", st_draft: "Draft", st_done: "Done", st_unsure: "Unsure", st_checked: "Checked",
    sec_practice: "Practice", sec_items: "To label",
    e_marking: "Choose the marking type.", e_arrow: "Choose the arrow type.", e_position: "Choose the position.", e_dashed: "Choose the broken-line side.",
    e_vis: "Choose the visibility.", e_dec: "For V1, say whether the visible part decides the behavior.", e_none: "\"None visible\" goes with V0 only.",
    e_actions: "Set every action: {x}.", e_partial: "With {ev} evidence no action can be allowed or prohibited: {x}.",
    e_rules: "Tick at least one rule.", e_unsure: "Write a reason when you tick Unsure.", w_v0: "V0 usually goes with \"none visible\".",
    saved_draft: "Draft saved.", saved_done: "Done.", not_done: "Not done yet, saved as draft:",
    all_done: "All done! Click \"Export results\" (top right) and send the downloaded file to the project owner.",
    export_done: "Exported {f}. Send this file to the project owner.", export_none: "Nothing to export yet.",
    import_ok: "Loaded progress for {n} images.", import_bad: "This file does not belong to this package ({p}).",
    pr_title: "Your answer vs the reference", pr_all: "All fields match ✓", pr_some: "{m} of {n} fields match", field: "Field", yours: "Yours", ref: "Reference",
    rule_ids: "Rules", note_unset: "Not prefilled: {x}. Judge from the image and the rules.",
    target: "Target", privacy: "Privacy", translation: "translation", original: "original", suggested: "suggested",
    region_US: "United States", region_CN: "China", diff_table: "≠table", leave_warn: "Some results are not exported yet. Leave anyway?",
    vis_tip: "V2 clear: the whole marking is easy to see.\nV1 partly visible: worn, covered or too dark. It decides the behavior only if a line shows its colour and pattern (dashed: one full dash and one gap; solid: unbroken for longer than a dash plus a gap; double: both lines), or an arrow shows its head.\nV0 no usable evidence: almost nothing visible.",
  },
};
const L = window.LANE_I18N;
const OPT = L.OPT;
const FIELD_NAMES = { zh: OPT.zh.field, en: OPT.en.field };
const S = {
  lang: "", ack: false, results: {}, practice: {}, lastExport: null, lastSaved: null, dirtySinceExport: false,
  sel: null, form: null, privacy: [], privSel: -1, drawing: null, storageOk: true, bright: 1.8,
};
const ALL = new Map();
for (const it of P.practice || []) ALL.set(it.image_id, { ...it, kind: "practice" });
for (const it of P.items || []) if (!ALL.has(it.image_id)) ALL.set(it.image_id, { ...it, kind: "item" });

function t(key, vars) {
  let s = (TXT[S.lang] && TXT[S.lang][key]) ?? TXT.en[key] ?? key;
  for (const [k, v] of Object.entries(vars || {})) s = s.split("{" + k + "}").join(v);
  return s;
}
const opt = (group) => OPT[S.lang][group];
function nowIso() { return new Date().toISOString().replace(/\.\d+Z$/, "Z"); }
function hhmm(iso) { if (!iso) return ""; const d = new Date(iso); return d.toLocaleString(S.lang === "zh" ? "zh-CN" : "en-US", { month: "numeric", day: "numeric", hour: "2-digit", minute: "2-digit" }); }
function esc(s) { return String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])); }

// ------------------------------------------------------------------ storage
function load() {
  try {
    const raw = localStorage.getItem(KEY);
    if (raw) Object.assign(S, JSON.parse(raw), { sel: null, form: null, drawing: null });
    localStorage.setItem(KEY + ":probe", "1");
    localStorage.removeItem(KEY + ":probe");
  } catch (e) {
    S.storageOk = false;
  }
  if (!S.storageOk) $("storage-warn").classList.remove("hidden");
  if (!S.lang || !TXT[S.lang]) S.lang = (navigator.language || "").toLowerCase().startsWith("zh") ? "zh" : "en";
}
function persist() {
  S.lastSaved = nowIso();
  const keep = { lang: S.lang, ack: S.ack, results: S.results, practice: S.practice, lastExport: S.lastExport,
    lastSaved: S.lastSaved, dirtySinceExport: S.dirtySinceExport, bright: S.bright };
  try { localStorage.setItem(KEY, JSON.stringify(keep)); S.storageOk = true; }
  catch (e) { S.storageOk = false; $("storage-warn").classList.remove("hidden"); }
  renderSaveState();
}
function renderSaveState() {
  const el = $("savestate");
  const parts = [];
  if (S.storageOk && S.lastSaved) parts.push(t("saved_at", { t: hhmm(S.lastSaved) }));
  parts.push(S.lastExport ? t("exported", { t: hhmm(S.lastExport) }) : t("never_exported"));
  el.textContent = parts.join(" · ");
  el.classList.toggle("warn", !S.lastExport || S.dirtySinceExport);
}

// ------------------------------------------------------------------ static text and language
function applyText() {
  document.documentElement.lang = S.lang === "zh" ? "zh-CN" : "en";
  for (const el of document.querySelectorAll("[data-t]")) el.textContent = t(el.dataset.t);
  $("lang-btn").textContent = S.lang === "zh" ? "English" : "中文";
  $("welcome-lang").textContent = S.lang === "zh" ? "English" : "中文";
  $("f-comment").placeholder = t("comment_ph");
  $("orig-btn").textContent = t("expand_all");
  $("vis-help").title = t("vis_tip");
  $("pkginfo").textContent = `${P.annotator_name || P.annotator} · ${P.package_id}`;
  $("guide-lang").textContent = S.lang === "zh" ? "English" : "中文";
  if (!$("guide").classList.contains("hidden")) renderGuide();
  renderWelcome();
  buildForm();
  renderList();
  renderProgress();
  renderSaveState();
  if (S.sel) openItem(S.sel, true, true);
}
function setLang(l) { S.lang = l; persist(); applyText(); }

function renderWelcome() {
  const zh = S.lang === "zh";
  const n = (P.items || []).length, np = (P.practice || []).length;
  const notices = (P.notices || []).map((x) => `<p class="notice">${esc(x)}</p>`).join("");
  $("welcome-body").innerHTML = zh ? `
<div class="welcome"><h2>你好，${esc(P.annotator_name || "")}！</h2>
<p>谢谢你帮忙标注道路标线。这个包里有 <b>${n}</b> 张图要标，另有 <b>${np}</b> 道练习题。每张图大约需要 1 分钟。</p>
<div class="privacy"><b>隐私须知</b><ul>
<li>图片来自真实道路，可能拍到别人的车牌和人脸。请用隐私框把<b>看得清的车牌和人脸</b>框出来，以后在任何报告里都会被打码。</li>
<li>请不要截图、转发或上传这些图片。标完后请删除整个文件夹。</li></ul></div>
<ul><li>先读“标注说明”，再做练习题。</li>
<li>进度会自动保存在这个浏览器里。请<b>每天至少点一次“导出结果”</b>，做完后把下载的 <code>results_….json</code> 文件发回。</li></ul>
${notices}</div>` : `
<div class="welcome"><h2>Hi ${esc(P.annotator_name || "")}!</h2>
<p>Thank you for helping label road markings. This package has <b>${n}</b> images to label and <b>${np}</b> practice items. Each image takes about a minute.</p>
<div class="privacy"><b>Privacy note</b><ul>
<li>The images show real roads and may show other people's licence plates and faces. Draw privacy boxes over every <b>readable plate and face</b>; they are blurred in every report.</li>
<li>Please do not screenshot, forward or upload the images. Delete the whole folder when you finish.</li></ul></div>
<ul><li>Read the guide first, then do the practice items.</li>
<li>Your work is saved in this browser automatically. <b>Click "Export results" at least once a day</b> and send back the downloaded <code>results_….json</code> file at the end.</li></ul>
${notices}</div>`;
}

function guideCtx() {
  const regions = [...new Set([...(P.items || []), ...(P.practice || [])].map((x) => x.region))];
  return { regions: regions.length ? regions : ["US"], tables: P.rules_tables || {}, owner: false };
}
function renderGuide() { $("guide-body").innerHTML = window.LANE_GUIDE ? window.LANE_GUIDE.render(S.lang, guideCtx()) : ""; }
function openGuide() { renderGuide(); $("guide").classList.remove("hidden"); $("guide-body").parentElement.scrollTop = 0; }

// ------------------------------------------------------------------ list
function itemState(id) {
  const it = ALL.get(id);
  if (it.kind === "practice") {
    const p = S.practice[id];
    return p && p.checked ? "checked" : p ? "draft" : "todo";
  }
  const r = S.results[id];
  if (!r) return "todo";
  if (r.status === "done") return r.unsure ? "unsure" : "done";
  return "draft";
}
function isTodo(id) { const s = itemState(id); return s === "todo" || s === "draft"; }
function orderedIds() {
  const pr = (P.practice || []).map((x) => x.image_id), it = (P.items || []).map((x) => x.image_id);
  return { pr, it };
}
function renderList() {
  const ol = $("items"), filter = $("filter").value;
  const { pr, it } = orderedIds();
  ol.innerHTML = "";
  const add = (title, ids) => {
    const shown = ids.filter((id) => filter === "all" || (filter === "done" ? !isTodo(id) : isTodo(id)));
    if (!ids.length) return;
    const h = document.createElement("li"); h.className = "section"; h.textContent = `${title} (${shown.length}/${ids.length})`; ol.appendChild(h);
    for (const id of shown) {
      const x = ALL.get(id), st = itemState(id);
      const li = document.createElement("li");
      li.dataset.id = id;
      li.classList.toggle("sel", id === S.sel);
      const mt = (x.kind === "practice" ? (S.practice[id] || {}).fields : (S.results[id] || {}).fields) || {};
      li.innerHTML = `<img loading="lazy" alt="" src="${esc(x.file)}"><div class="meta">${t("region_" + x.region)} · ${esc(x.dataset)}<br>` +
        `<span class="pill ${st}">${t("st_" + st)}</span> ${esc(mt.marking_type ? opt("marking")[mt.marking_type] || "" : "")}</div>`;
      li.addEventListener("click", () => openItem(id));
      ol.appendChild(li);
    }
  };
  add(t("sec_practice"), pr);
  add(t("sec_items"), it);
}
function renderProgress() {
  const it = (P.items || []).map((x) => x.image_id);
  const d = it.filter((id) => !isTodo(id)).length;
  const pr = (P.practice || []).map((x) => x.image_id);
  const pd = pr.filter((id) => (S.practice[id] || {}).checked).length;
  $("progress").innerHTML = t("progress", { d, n: it.length }) + (pr.length ? " · " + t("practice_progress", { d: pd, n: pr.length }) : "");
}

// ------------------------------------------------------------------ form
function segment(container, options, onPick, withCode = true) {
  container.innerHTML = "";
  for (const [value, text] of Object.entries(options)) {
    const b = document.createElement("button");
    b.type = "button"; b.dataset.value = value;
    b.innerHTML = esc(text) + (withCode ? `<small>${esc(value)}</small>` : "");
    b.setAttribute("aria-pressed", "false");
    b.addEventListener("click", () => onPick(value));
    container.appendChild(b);
  }
}
function setSeg(container, value) {
  for (const b of container.querySelectorAll("button")) {
    const on = b.dataset.value === value;
    b.classList.toggle("on", on); b.setAttribute("aria-pressed", String(on));
  }
}
function only(keys, dict) { return Object.fromEntries(keys.filter((k) => k in dict).map((k) => [k, dict[k]])); }
function buildForm() {
  const sc = P.schema;
  segment($("f-marking"), only(sc.marking_type, opt("marking")), (v) => setField("marking_type", v));
  segment($("f-arrow"), only(sc.arrow_type, opt("arrow")), (v) => setField("arrow_type", v));
  segment($("f-dashed"), only(sc.dashed_side, opt("dashed")), (v) => setField("dashed_side", v));
  segment($("f-position"), only(sc.position, opt("position")), (v) => setField("position", v));
  segment($("f-visibility"), only(sc.visibility, opt("vis")), (v) => setField("visibility", v));
  segment($("f-decidable"), opt("decide"), (v) => setField("behavior_decidable", v));
  $("f-visibility").title = t("vis_tip");
  const tbl = $("f-actions");
  tbl.innerHTML = "";
  for (const a of ACTIONS) {
    const tr = document.createElement("tr"); tr.dataset.action = a;
    const td1 = document.createElement("td"); td1.textContent = opt("act")[a] || a; td1.title = a;
    const td2 = document.createElement("td");
    const seg = document.createElement("div"); seg.className = "seg";
    segment(seg, only(sc.action_values, opt("actv")), (v) => { S.form.actions[a] = v; renderForm(); }, false);
    td2.appendChild(seg); tr.append(td1, td2); tbl.appendChild(tr);
  }
}
function buildRules(region) {
  L.renderPassages($("f-rules"), P.passages[region] || [], S.lang, (id, on) => {
    const set = new Set(S.form.rule_ids);
    if (on) set.add(id); else set.delete(id);
    S.form.rule_ids = [...set];
    L.syncPassages($("f-rules"), S.form.rule_ids, (suggestion(S.form, cur().region) || {}).rule_ids);
  });
  $("orig-btn").textContent = t("expand_all");
}
const evidenceOf = L.evidenceOf;
function suggestion(f, region) { return L.suggestion((P.rules_tables || {})[region], f, S.lang); }
function cur() { return S.sel ? ALL.get(S.sel) : null; }
function applySuggestion(withRules) {
  const it = cur(); if (!it) return;
  const sug = suggestion(S.form, it.region);
  for (const a of ACTIONS) S.form.actions[a] = sug ? sug.actions[a] || "" : "";
  if (sug && withRules) S.form.rule_ids = sug.rule_ids.filter((id) => (P.passages[it.region] || []).some((p) => p.rule_id === id));
}
function setField(k, v) {
  const f = S.form;
  f[k] = f[k] === v && (k === "arrow_type" || k === "dashed_side" || k === "behavior_decidable") ? "" : v;
  if (k === "marking_type") {
    if (v !== "arrow") f.arrow_type = "";
    if (v !== "yellow_solid_dashed") f.dashed_side = "";
    if (v === "arrow" && !f.position) f.position = "in_ego_lane";
    if (v === "none_visible") f.visibility = "V0";
  }
  if (k === "visibility" && v !== "V1") f.behavior_decidable = "";
  if (["marking_type", "arrow_type", "dashed_side", "visibility", "behavior_decidable"].includes(k)) applySuggestion(["marking_type", "arrow_type", "dashed_side"].includes(k));
  renderForm();
}
function renderForm() {
  const f = S.form, it = cur();
  if (!f || !it) return;
  setSeg($("f-marking"), f.marking_type); setSeg($("f-arrow"), f.arrow_type); setSeg($("f-dashed"), f.dashed_side);
  setSeg($("f-position"), f.position); setSeg($("f-visibility"), f.visibility); setSeg($("f-decidable"), f.behavior_decidable);
  $("fs-arrow").classList.toggle("hidden", f.marking_type !== "arrow");
  $("fs-dashed").classList.toggle("hidden", !(P.schema.needs_dashed_side || []).includes(f.marking_type));
  $("fs-decidable").classList.toggle("hidden", f.visibility !== "V1");
  const ev = evidenceOf(f.visibility, f.behavior_decidable);
  $("f-evidence").textContent = opt("evid")[ev] || "—";
  const sug = suggestion(f, it.region);
  for (const tr of $("f-actions").querySelectorAll("tr")) {
    const a = tr.dataset.action, v = f.actions[a] || "";
    setSeg(tr.querySelector(".seg"), v);
    tr.classList.toggle("unset", !v);
    tr.classList.toggle("suggested-diff", !!(sug && sug.actions[a] && v && sug.actions[a] !== v));
  }
  const empty = sug ? Object.entries(sug.actions).filter(([, v]) => !v).map(([a]) => opt("act")[a]) : [];
  const parts = [];
  if (sug && sug.note) parts.push(sug.note);
  if (empty.length) parts.push(t("note_unset", { x: empty.join(S.lang === "zh" ? "、" : ", ") }));
  $("rule-note").textContent = parts.join(" ");
  $("rule-note").classList.toggle("hidden", !parts.length);
  L.syncPassages($("f-rules"), f.rule_ids, sug ? sug.rule_ids : []);
  $("f-unsure").checked = !!f.unsure;
  $("f-comment").value = f.comment || "";
}
function blankForm() {
  return { marking_type: "", arrow_type: "", position: "", dashed_side: "", visibility: "", behavior_decidable: "",
    actions: Object.fromEntries(ACTIONS.map((a) => [a, ""])), rule_ids: [], unsure: false, comment: "" };
}
function validate(f) {
  const sc = P.schema, errors = [], warnings = [];
  if (!sc.marking_type.includes(f.marking_type)) errors.push(t("e_marking"));
  const evPre = evidenceOf(f.visibility, f.behavior_decidable);
  const detailOptional = evPre === "partial" || evPre === "insufficient";
  if (f.marking_type === "arrow" && !sc.arrow_type.includes(f.arrow_type) && !(detailOptional && !f.arrow_type)) errors.push(t("e_arrow"));
  if (!sc.position.includes(f.position)) errors.push(t("e_position"));
  if ((sc.needs_dashed_side || []).includes(f.marking_type) && !sc.dashed_side.includes(f.dashed_side) && !(detailOptional && !f.dashed_side)) errors.push(t("e_dashed"));
  if (!sc.visibility.includes(f.visibility)) errors.push(t("e_vis"));
  if (f.visibility === "V1" && !["yes", "no"].includes(f.behavior_decidable)) errors.push(t("e_dec"));
  if (f.marking_type === "none_visible" && f.visibility !== "V0") errors.push(t("e_none"));
  if (f.visibility === "V0" && f.marking_type && f.marking_type !== "none_visible") warnings.push(t("w_v0"));
  const ev = evidenceOf(f.visibility, f.behavior_decidable);
  const missing = ACTIONS.filter((a) => !sc.action_values.includes(f.actions[a]));
  if (missing.length) errors.push(t("e_actions", { x: missing.map((a) => opt("act")[a]).join(S.lang === "zh" ? "、" : ", ") }));
  if (ev === "partial" || ev === "insufficient") {
    const bad = ACTIONS.filter((a) => ["allowed", "prohibited"].includes(f.actions[a]));
    if (bad.length) errors.push(t("e_partial", { ev, x: bad.map((a) => opt("act")[a]).join(S.lang === "zh" ? "、" : ", ") }));
  } else if (ev === "full" && !(sc.no_rule_needed || []).includes(f.marking_type) && !(f.rule_ids || []).length) {
    errors.push(t("e_rules"));
  }
  if (f.unsure && !(f.comment || "").trim()) errors.push(t("e_unsure"));
  return { errors, warnings };
}

// ------------------------------------------------------------------ open / save
function openItem(id, keepMsgs, keepForm) {
  const it = ALL.get(id);
  if (!it) return;
  const saved = it.kind === "practice" ? S.practice[id] : S.results[id];
  if (!(keepForm && S.sel === id && S.form)) {
    S.form = saved ? JSON.parse(JSON.stringify({ ...blankForm(), ...saved.fields, unsure: !!saved.unsure, comment: saved.comment || "" })) : blankForm();
    if (!S.form.actions) S.form.actions = blankForm().actions;
    S.privacy = saved && saved.privacy_boxes ? JSON.parse(JSON.stringify(saved.privacy_boxes)) : [];
    S.privSel = -1; S.drawing = null;
  }
  S.sel = id;
  $("form-empty").classList.add("hidden");
  $("form-body").classList.remove("hidden");
  $("practice-bar").classList.toggle("hidden", it.kind !== "practice");
  $("save-done").textContent = it.kind === "practice" ? t("check_answer") : t("save_done");
  $("save-draft").classList.toggle("hidden", it.kind === "practice");
  $("img-title").textContent = `${t("region_" + it.region)} · ${it.dataset} · ${it.time_of_day || ""} · ${id}`;
  buildRules(it.region);
  renderForm();
  if (!keepMsgs) $("form-msgs").innerHTML = "";
  if (it.kind === "practice" && saved && saved.checked && !keepForm) showPracticeResult(it, saved);
  const img = $("img");
  img.onload = () => { layout(); draw(); };
  if (img.getAttribute("src") !== it.file) img.src = it.file; else { layout(); draw(); }
  for (const li of $("items").querySelectorAll("li[data-id]")) li.classList.toggle("sel", li.dataset.id === id);
  const sel = $("items").querySelector("li.sel");
  if (sel) sel.scrollIntoView({ block: "nearest" });
}
function snapshot() {
  const f = S.form;
  return {
    fields: { marking_type: f.marking_type, arrow_type: f.arrow_type, position: f.position, dashed_side: f.dashed_side,
      visibility: f.visibility, behavior_decidable: f.behavior_decidable, actions: { ...f.actions }, rule_ids: [...(f.rule_ids || [])] },
    privacy_boxes: S.privacy.map((b) => b.map(Math.round)), unsure: !!f.unsure, comment: (f.comment || "").trim(), saved_utc: nowIso(),
  };
}
function save(status) {
  const it = cur(); if (!it) return;
  S.form.comment = $("f-comment").value;
  S.form.unsure = $("f-unsure").checked;
  const snap = snapshot();
  const box = $("form-msgs");
  if (it.kind === "practice") {
    const res = scorePractice(it, snap.fields);
    S.practice[it.image_id] = { ...snap, checked: true, ...res };
    persist(); renderList(); renderProgress();
    showPracticeResult(it, S.practice[it.image_id]);
    return;
  }
  const { errors, warnings } = validate(S.form);
  let st = status;
  if (status === "done" && errors.length && !S.form.unsure) st = "draft";
  if (status === "done" && S.form.unsure && !(S.form.comment || "").trim()) st = "draft";
  S.results[it.image_id] = { ...snap, status: st };
  S.dirtySinceExport = true;
  persist(); renderList(); renderProgress();
  const parts = [];
  if (status === "done" && st !== "done") {
    parts.push(`<div class="e">${esc(t("not_done"))}</div>`);
    for (const e of errors) parts.push(`<div class="e">✗ ${esc(e)}</div>`);
    box.innerHTML = parts.join("");
    return;
  }
  for (const w of warnings) parts.push(`<div class="w">! ${esc(w)}</div>`);
  parts.unshift(`<div class="ok">${esc(st === "done" ? t("saved_done") : t("saved_draft"))}</div>`);
  if (st === "done") {
    const next = nextTodo(it.image_id);
    if (next) { openItem(next); $("form-msgs").innerHTML = parts.join(""); }
    else box.innerHTML = parts.join("") + `<div class="ok">${esc(t("all_done"))}</div>`;
  } else box.innerHTML = parts.join("");
}
function nextTodo(fromId) {
  const { pr, it } = orderedIds();
  const all = [...pr, ...it];
  const i = all.indexOf(fromId);
  return all.slice(i + 1).find(isTodo) || all.slice(0, Math.max(0, i)).find(isTodo) || null;
}
function moveSel(d) {
  const ids = [...$("items").querySelectorAll("li[data-id]")].map((li) => li.dataset.id);
  if (!ids.length) return;
  const i = ids.indexOf(S.sel);
  openItem(ids[Math.max(0, Math.min(ids.length - 1, i < 0 ? 0 : i + d))]);
}

// practice
const CMP = ["marking_type", "arrow_type", "position", "dashed_side", "visibility", "behavior_decidable"];
function scorePractice(it, f) {
  const ref = it.reference;
  let m = 0, n = 0;
  for (const k of CMP) { n++; if ((f[k] || "") === (ref[k] || "")) m++; }
  for (const a of ACTIONS) { n++; if ((f.actions[a] || "") === (ref.actions[a] || "")) m++; }
  return { matched: m, total: n, correct: m === n };
}
function fmtVal(k, v) {
  if (!v) return "—";
  const map = { marking_type: "marking", arrow_type: "arrow", position: "position", dashed_side: "dashed", visibility: "vis", behavior_decidable: "decide" }[k];
  return map ? (opt(map)[v] || v) : (opt("actv")[v] || v);
}
function showPracticeResult(it, saved) {
  const ref = it.reference, f = saved.fields;
  const rows = [];
  for (const k of CMP) {
    if (!f[k] && !ref[k]) continue;
    const ok = (f[k] || "") === (ref[k] || "");
    rows.push(`<tr class="${ok ? "good" : "bad"}"><td>${esc(FIELD_NAMES[S.lang][k])}</td><td>${esc(fmtVal(k, f[k]))}</td><td>${esc(fmtVal(k, ref[k]))}</td></tr>`);
  }
  for (const a of ACTIONS) {
    const ok = (f.actions[a] || "") === (ref.actions[a] || "");
    rows.push(`<tr class="${ok ? "good" : "bad"}"><td>${esc(opt("act")[a])}</td><td>${esc(fmtVal("act", f.actions[a]))}</td><td>${esc(fmtVal("act", ref.actions[a]))}</td></tr>`);
  }
  rows.push(`<tr><td>${esc(t("rule_ids"))}</td><td>${esc((f.rule_ids || []).join(", ") || "—")}</td><td>${esc((ref.accepted_rule_ids || []).join(", ") || "—")}</td></tr>`);
  const head = saved.correct ? t("pr_all") : t("pr_some", { m: saved.matched, n: saved.total });
  $("form-msgs").innerHTML = `<div class="${saved.correct ? "ok" : "w"}"><b>${esc(t("pr_title"))}: ${esc(head)}</b></div>` +
    `<table class="cmp"><tr><th>${esc(t("field"))}</th><th>${esc(t("yours"))}</th><th>${esc(t("ref"))}</th></tr>${rows.join("")}</table>`;
}

// ------------------------------------------------------------------ export / import
function download(name, text) {
  const blob = new Blob([text], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob); a.download = name;
  document.body.appendChild(a); a.click();
  setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
}
function exportResults() {
  const ids = Object.keys(S.results);
  if (!ids.length && !Object.keys(S.practice).length) { $("form-msgs").innerHTML = `<div class="w">${esc(t("export_none"))}</div>`; return; }
  const checked = Object.values(S.practice).filter((p) => p.checked);
  const out = {
    format: "lane-label-results-v1", package_id: P.package_id, annotator: P.annotator, exported_utc: nowIso(),
    tool_version: P.tool_version, language: S.lang,
    practice_score: checked.length ? `${checked.filter((p) => p.correct).length}/${checked.length}` : null,
    results: ids.filter((id) => ALL.has(id) && ALL.get(id).kind === "item").map((id) => {
      const r = S.results[id], it = ALL.get(id);
      return { image_id: id, set_id: it.set_id, status: r.status, unsure: !!r.unsure, comment: r.comment || "",
        fields: { ...r.fields, accepted_rule_ids: r.fields.rule_ids || [] }, privacy_boxes: r.privacy_boxes || [], saved_utc: r.saved_utc };
    }),
    practice: Object.entries(S.practice).map(([id, p]) => ({ image_id: id, matched: p.matched, total: p.total, correct: !!p.correct })),
  };
  const name = `results_${P.annotator}_${P.package_id}.json`;
  download(name, JSON.stringify(out, null, 1));
  S.lastExport = nowIso(); S.dirtySinceExport = false; persist();
  $("form-msgs").innerHTML = `<div class="ok">${esc(t("export_done", { f: name }))}</div>`;
}
function importProgress(file) {
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const data = JSON.parse(reader.result);
      if (data.format !== "lane-label-results-v1" || data.package_id !== P.package_id) throw new Error("bad");
      let n = 0;
      for (const r of data.results || []) {
        if (!ALL.has(r.image_id)) continue;
        const old = S.results[r.image_id];
        if (old && old.saved_utc >= r.saved_utc) continue;
        const fields = { ...r.fields, rule_ids: r.fields.accepted_rule_ids || r.fields.rule_ids || [] };
        delete fields.accepted_rule_ids;
        S.results[r.image_id] = { fields, privacy_boxes: r.privacy_boxes || [], unsure: !!r.unsure, comment: r.comment || "", saved_utc: r.saved_utc, status: r.status };
        n++;
      }
      persist(); renderList(); renderProgress();
      $("form-msgs").innerHTML = `<div class="ok">${esc(t("import_ok", { n }))}</div>`;
    } catch (e) {
      $("form-msgs").innerHTML = `<div class="e">${esc(t("import_bad", { p: P.package_id }))}</div>`;
    }
  };
  reader.readAsText(file);
}

// ------------------------------------------------------------------ canvas
function sizeCanvas(c, w, h) {
  const dpr = window.devicePixelRatio || 1;
  c.width = Math.round(w * dpr); c.height = Math.round(h * dpr);
  c.style.width = w + "px"; c.style.height = h + "px";
  c.getContext("2d").setTransform(dpr, 0, 0, dpr, 0, 0);
}
function layout() {
  const it = cur(); if (!it) return;
  const work = document.querySelector(".work");
  const maxW = work.clientWidth - 20;
  const maxH = work.clientHeight - document.querySelector(".work .toolbar").offsetHeight - document.querySelector(".work .hint").offsetHeight - 24;
  const r = Math.min(maxW / it.width, maxH / it.height);
  const w = Math.max(100, Math.floor(it.width * r)), h = Math.max(60, Math.floor(it.height * r));
  const st = $("stage"); st.style.width = w + "px"; st.style.height = h + "px";
  sizeCanvas($("overlay"), w, h);
}
function toImg(ev) {
  const it = cur(), c = $("overlay"), rect = c.getBoundingClientRect();
  const x = ((ev.clientX - rect.left) / rect.width) * it.width, y = ((ev.clientY - rect.top) / rect.height) * it.height;
  return [Math.max(0, Math.min(it.width, x)), Math.max(0, Math.min(it.height, y))];
}
function normRect(a, b) { return [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[0], b[0]), Math.max(a[1], b[1])]; }
function inRect(p, r) { return p[0] >= r[0] && p[0] <= r[2] && p[1] >= r[1] && p[1] <= r[3]; }
function draw() {
  const it = cur(), c = $("overlay"), ctx = c.getContext("2d");
  const w = c.clientWidth, h = c.clientHeight;
  ctx.clearRect(0, 0, w, h);
  if (!it) return;
  const sx = w / it.width, sy = h / it.height;
  const R = (r) => [r[0] * sx, r[1] * sy, (r[2] - r[0]) * sx, (r[3] - r[1]) * sy];
  S.privacy.forEach((r, i) => {
    ctx.fillStyle = "rgba(255, 94, 196, .28)"; ctx.fillRect(...R(r));
    ctx.strokeStyle = i === S.privSel ? "#fff" : "#ff5ec4"; ctx.lineWidth = i === S.privSel ? 3 : 2; ctx.strokeRect(...R(r));
    ctx.fillStyle = "#ff5ec4"; ctx.font = "11px sans-serif"; ctx.fillText(t("privacy"), r[0] * sx + 3, r[1] * sy - 3);
  });
  ctx.strokeStyle = "#36e0c8"; ctx.lineWidth = 2.5; ctx.strokeRect(...R(it.box));
  ctx.fillStyle = "#36e0c8"; ctx.font = "bold 11px sans-serif"; ctx.fillText(t("target"), it.box[0] * sx + 3, it.box[1] * sy - 4);
  if (S.drawing) {
    ctx.setLineDash([6, 4]); ctx.lineWidth = 2; ctx.strokeStyle = "#ff5ec4";
    ctx.strokeRect(...R(S.drawing.rect)); ctx.setLineDash([]);
  }
}
function drawLoupe(p) {
  const lp = $("loupe"), it = cur();
  if (!$("loupe-on").checked || !p || !it) { lp.classList.add("hidden"); return; }
  lp.classList.remove("hidden");
  const ctx = lp.getContext("2d"), z = 70, k = 220 / z;
  ctx.imageSmoothingEnabled = false;
  ctx.fillStyle = "#000"; ctx.fillRect(0, 0, 220, 220);
  const sx = p[0] - z / 2, sy = p[1] - z / 2;
  try { ctx.drawImage($("img"), sx, sy, z, z, 0, 0, 220, 220); } catch (e) { /* not loaded */ }
  ctx.strokeStyle = "#36e0c8"; ctx.lineWidth = 1.5;
  ctx.strokeRect((it.box[0] - sx) * k, (it.box[1] - sy) * k, (it.box[2] - it.box[0]) * k, (it.box[3] - it.box[1]) * k);
  ctx.strokeStyle = "rgba(255,255,255,.7)"; ctx.lineWidth = 1;
  ctx.beginPath(); ctx.moveTo(110, 0); ctx.lineTo(110, 220); ctx.moveTo(0, 110); ctx.lineTo(220, 110); ctx.stroke();
  const stage = $("stage").getBoundingClientRect(), mx = (p[0] / it.width) * stage.width;
  lp.style.right = mx > stage.width - 250 ? "auto" : "8px"; lp.style.left = mx > stage.width - 250 ? "8px" : "auto";
}
function deleteSelected() { if (S.privSel >= 0) { S.privacy.splice(S.privSel, 1); S.privSel = -1; draw(); } }

// ------------------------------------------------------------------ events
function setBright(v) {
  S.bright = v;
  $("bright").value = v;
  document.documentElement.style.setProperty("--imgfilter", `brightness(${v}) contrast(${1 + (v - 1) * 0.15})`);
}
function bind() {
  $("lang-btn").addEventListener("click", () => setLang(S.lang === "zh" ? "en" : "zh"));
  $("welcome-lang").addEventListener("click", () => setLang(S.lang === "zh" ? "en" : "zh"));
  $("guide-btn").addEventListener("click", openGuide);
  $("welcome-guide").addEventListener("click", openGuide);
  $("guide-lang").addEventListener("click", () => setLang(S.lang === "zh" ? "en" : "zh"));
  $("guide-print").addEventListener("click", () => window.LANE_GUIDE.openPrintable(S.lang, guideCtx()));
  $("guide-close").addEventListener("click", () => $("guide").classList.add("hidden"));
  $("ack").addEventListener("change", (e) => { $("welcome-start").disabled = !e.target.checked; });
  $("welcome-start").addEventListener("click", () => {
    S.ack = true; persist(); $("welcome").classList.add("hidden");
    const first = nextTodo(null) || (P.items[0] || {}).image_id;
    if (first) openItem(first);
  });
  $("export-btn").addEventListener("click", exportResults);
  $("import-btn").addEventListener("click", () => $("import-file").click());
  $("import-file").addEventListener("change", (e) => { if (e.target.files[0]) importProgress(e.target.files[0]); e.target.value = ""; });
  $("filter").addEventListener("change", renderList);
  $("bright").addEventListener("input", (e) => { setBright(Number(e.target.value)); persist(); });
  $("del-box").addEventListener("click", deleteSelected);
  $("tool-privacy").addEventListener("click", () => {});
  $("prefill-btn").addEventListener("click", () => { applySuggestion(true); renderForm(); });
  $("orig-btn").addEventListener("click", () => {
    const rules = [...$("f-rules").querySelectorAll(".rule")];
    const open = !rules.every((r) => r.classList.contains("open"));
    for (const r of rules) { r.classList.toggle("open", open); r.querySelector(".rmore").textContent = open ? L.RULE_TXT[S.lang].less : L.RULE_TXT[S.lang].more; }
    $("orig-btn").textContent = open ? t("collapse_all") : t("expand_all");
  });
  $("f-unsure").addEventListener("change", (e) => { if (S.form) S.form.unsure = e.target.checked; });
  $("f-comment").addEventListener("input", (e) => { if (S.form) S.form.comment = e.target.value; });
  $("save-done").addEventListener("click", () => save("done"));
  $("save-draft").addEventListener("click", () => save("draft"));
  $("vis-help").addEventListener("click", () => alert(t("vis_tip")));

  const ov = $("overlay");
  ov.addEventListener("mousedown", (e) => {
    if (!cur()) return;
    const p = toImg(e);
    const hit = S.privacy.findIndex((r) => inRect(p, r));
    if (hit >= 0) { S.privSel = hit; draw(); return; }
    S.privSel = -1;
    S.drawing = { start: p, rect: [p[0], p[1], p[0], p[1]] };
  });
  ov.addEventListener("mousemove", (e) => { if (cur()) drawLoupe(toImg(e)); });
  ov.addEventListener("mouseleave", () => drawLoupe(null));
  window.addEventListener("mousemove", (e) => {
    if (S.drawing) { const p = toImg(e); S.drawing.rect = normRect(S.drawing.start, p); draw(); drawLoupe(p); }
  });
  window.addEventListener("mouseup", () => {
    if (!S.drawing) return;
    const r = S.drawing.rect.map(Math.round); S.drawing = null;
    if (r[2] - r[0] >= 4 && r[3] - r[1] >= 4) { S.privacy.push(r); S.privSel = S.privacy.length - 1; }
    draw();
  });
  window.addEventListener("resize", () => { layout(); draw(); });
  window.addEventListener("beforeunload", (e) => { if (S.dirtySinceExport && !S.storageOk) { e.preventDefault(); e.returnValue = t("leave_warn"); } });
  document.addEventListener("keydown", (e) => {
    const mod = e.metaKey || e.ctrlKey;
    if (!$("guide").classList.contains("hidden")) { if (e.key === "Escape") $("guide").classList.add("hidden"); return; }
    if (!$("welcome").classList.contains("hidden")) return;
    if (mod && e.key === "Enter") { e.preventDefault(); save("done"); return; }
    if (mod && (e.key === "s" || e.key === "S")) { e.preventDefault(); save("draft"); return; }
    const tg = e.target;
    if (tg && (tg.tagName === "TEXTAREA" || tg.tagName === "SELECT" || (tg.tagName === "INPUT" && tg.type === "text"))) return;
    if (e.key === "Escape") { S.drawing = null; S.privSel = -1; draw(); }
    else if (e.key === "Delete" || e.key === "Backspace") { e.preventDefault(); deleteSelected(); }
    else if (e.key === "[") moveSel(-1);
    else if (e.key === "]") moveSel(1);
  });
}

function boot() {
  if (!P || P.format !== "lane-label-package-v1") {
    document.body.innerHTML = "<p style='padding:30px;font:16px sans-serif'>data.js is missing or damaged. 数据文件缺失或损坏。</p>";
    return;
  }
  load();
  bind();
  setBright(S.bright || 1.8);
  applyText();
  if (!S.ack) $("welcome").classList.remove("hidden");
  else { const first = nextTodo(null) || ((P.practice[0] || P.items[0]) || {}).image_id; if (first) openItem(first); }
}
boot();
