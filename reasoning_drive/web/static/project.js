// The project page: overview, results with evaluation, regulations (extract a new standard), CARLA simulation.
"use strict";

const T = {
  zh: {
    project: "项目", tab_overview: "概览", tab_results: "结果与评估", tab_regulations: "法规", tab_carla: "CARLA 仿真",
    link_demo: "运行模型（推理窗口）", link_review: "盲审", ov_settings: "当前设置", ov_layout: "项目结构",
    ov_settings_note: "改设置：configs/api.yaml（模型）、configs/experiment.yaml（实验）、configs/carla.yaml（仿真），或在运行模型页面的设置对话框里改。",
    ov_countries: "国家（regulations/<代码>/）", ov_countries_note: "新国家：复制 regulations/_template/，或在“法规”页从 PDF 提取。",
    ov_datasets: "数据集（datasets/<代码>/）", kind: "类型", all: "全部", r_hint: "点一行看评估；按住 Shift 点第二行做对比",
    rg_countries: "已有国家", rg_new: "从 PDF 提取新国家的法规", rg_new_note: "把标准的 PDF 放进 regulations/inbox/（或在这里上传），先估算请求数和费用，再提取。结果是草稿，读过后再“接受”。",
    rg_pdf: "PDF", rg_upload: "上传 PDF", rg_code: "代码", rg_name: "名称（写进提示词）", rg_side: "行驶方向", right: "靠右", left: "靠左",
    rg_title: "标准名称和版本", rg_pages: "页码", rg_all: "所有有文字的页", rg_real: "真实 API（花钱）", rg_estimate: "估算",
    rg_extract: "提取", rg_draft: "草稿", rg_accept: "接受草稿", jobs: "后台任务",
    ca_server: "CARLA 服务器", ca_start: "启动 CARLA", ca_route: "路线", ca_mock: "模拟回答（不花钱）", ca_preview: "只预览站点",
    ca_run: "开始行驶", ca_note: "需要一个装了 carla 包的 Python（configs/carla.yaml 的 server.python）。也可以在命令行运行：python main.py carla route route1 --record",
    settings_model: "模型", settings_mode: "模式", mock: "模拟（不调用 API）", real: "真实 API", key: "API key", set: "已设置", notset: "未设置",
    test: "实验", region: "国家", prompt: "提示词", lane_prompt: "车道任务提示词", split: "数据划分", routes: "仿真路线",
    code: "代码", name: "名称", side: "方向", standard: "标准", passages: "条文", tables: "规则表", draft: "草稿",
    collections: "集合", rows_marking: "单标线标签", rows_lane: "车道标签", source: "来源",
    cells: "动作格", acc: "准确率", macro: "宏平均 F1", unsafe: "不安全错误", over: "过度谨慎", cm: "混淆矩阵（行=标签，列=回答）",
    actions_h: "动作（标签确定的格子，不含有争议的格子）", o1_h: "Output 1：标线类型", bd_h: "车道两侧边界", mk_h: "车道内标记（token）",
    sub_h: "按组合难度（L1–L3）和规则敏感性分组的车道动作", sub_correct: "动作全对", sub_unsafe: "不安全错误",
    ri: "Test D：回答里说的国家（提示词没给）", ppp: "Test R：每个提示词里的条文数",
    per_action: "每个动作的“禁止”召回率", compare_h: "两次运行对比", reachable: "可连接", not_reachable: "未运行", python: "Python（有 carla）",
    no_draft: "没有草稿", verified: "引文在原页", stops: "站点", intent: "导航意图", did: "车的动作", video: "回放视频",
    est: "估算", pages_read: "要读的页", requests: "请求数", cost: "约", none: "无", problems_none: "所有国家的文件都符合模板。"
  },
  en: {
    project: "project", tab_overview: "Overview", tab_results: "Results & evaluation", tab_regulations: "Regulations", tab_carla: "CARLA simulation",
    link_demo: "Run the model (reasoning window)", link_review: "Blind review", ov_settings: "Current settings", ov_layout: "Project layout",
    ov_settings_note: "Change settings in configs/api.yaml (model), configs/experiment.yaml (experiment), configs/carla.yaml (simulation), or in the settings dialog of the model page.",
    ov_countries: "Countries (regulations/<CODE>/)", ov_countries_note: "A new country: copy regulations/_template/, or extract it from a PDF on the Regulations tab.",
    ov_datasets: "Datasets (datasets/<CODE>/)", kind: "Kind", all: "all", r_hint: "click a row for its evaluation; Shift+click a second row to compare",
    rg_countries: "Countries", rg_new: "A new country's rules from its PDF", rg_new_note: "Put the standard's PDF in regulations/inbox/ (or upload it here), estimate the requests and the cost, then extract. The result is a draft; accept it after reading it.",
    rg_pdf: "PDF", rg_upload: "Upload PDF", rg_code: "Code", rg_name: "Name (goes into the prompt)", rg_side: "Traffic drives on the", right: "right", left: "left",
    rg_title: "Title and edition", rg_pages: "Pages", rg_all: "every page with text", rg_real: "real API (costs money)", rg_estimate: "Estimate",
    rg_extract: "Extract", rg_draft: "Draft", rg_accept: "Accept draft", jobs: "Background jobs",
    ca_server: "CARLA server", ca_start: "Start CARLA", ca_route: "Route", ca_mock: "made-up answers (free)", ca_preview: "preview the stops only",
    ca_run: "Drive", ca_note: "Needs a Python with the carla package (server.python in configs/carla.yaml). From the command line: python main.py carla route route1 --record",
    settings_model: "Model", settings_mode: "Mode", mock: "mock (no API calls)", real: "real API", key: "API key", set: "set", notset: "not set",
    test: "Test", region: "Country", prompt: "Prompt", lane_prompt: "Lane prompt", split: "Split", routes: "Routes",
    code: "Code", name: "Name", side: "Side", standard: "Standard", passages: "Passages", tables: "Rule tables", draft: "Draft",
    collections: "Collections", rows_marking: "marking labels", rows_lane: "lane labels", source: "Source",
    cells: "action cells", acc: "accuracy", macro: "macro-F1", unsafe: "unsafe errors", over: "over-cautious", cm: "Confusion matrix (rows = label, columns = answer)",
    actions_h: "Actions (cells the label decides, contested cells left out)", o1_h: "Output 1: marking type", bd_h: "Boundaries of my lane", mk_h: "Markings in my lane (tokens)",
    sub_h: "Lane actions by composition level (L1-L3) and rule sensitivity", sub_correct: "all actions right", sub_unsafe: "unsafe errors",
    ri: "Test D: country named in the answer (not given in the prompt)", ppp: "Test R: passages per prompt",
    per_action: "recall of prohibited per action", compare_h: "Two runs side by side", reachable: "reachable", not_reachable: "not running", python: "Python with carla",
    no_draft: "no draft", verified: "quote on its page", stops: "Stops", intent: "Navigation intent", did: "What the car did", video: "replay video",
    est: "Estimate", pages_read: "pages to read", requests: "requests", cost: "about", none: "none", problems_none: "Every country's files fit the template."
  }
};
let LANG = localStorage.getItem("rd_lang") || "zh";
const t = (k) => (T[LANG] && T[LANG][k]) || T.en[k] || k;
const $ = (s) => document.querySelector(s);
const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const fmt = (x) => (x === null || x === undefined ? "–" : typeof x === "number" && !Number.isInteger(x) ? x.toFixed(3) : x);

function applyLang() {
  document.querySelectorAll("[data-t]").forEach((el) => { el.textContent = t(el.dataset.t); });
  $("#lang-btn").textContent = LANG === "zh" ? "English" : "中文";
}
function toast(msg, err) {
  const el = $("#toast"); el.textContent = msg; el.className = "toast" + (err ? " err" : "");
  clearTimeout(toast.h); toast.h = setTimeout(() => el.classList.add("hidden"), err ? 9000 : 4000);
}
async function api(path, body) {
  const r = await fetch("/api/project/" + path, body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {});
  const j = await r.json();
  if (!r.ok || j.error) throw new Error(j.error || r.statusText);
  return j;
}
function table(el, head, rows) {
  el.innerHTML = "<tr>" + head.map((h) => `<th>${esc(h)}</th>`).join("") + "</tr>" +
    rows.map((r) => "<tr>" + r.map((c) => `<td>${c}</td>`).join("") + "</tr>").join("");
}

// ------------------------------------------------------------------ tabs
function show(tab) {
  document.querySelectorAll("#tabs button").forEach((b) => b.classList.toggle("on", b.dataset.tab === tab));
  document.querySelectorAll(".page").forEach((p) => p.classList.toggle("hidden", p.id !== "p-" + tab));
  location.hash = tab;
  ({ overview: loadOverview, results: loadResults, regulations: loadRegulations, carla: loadCarla })[tab]();
}

// ------------------------------------------------------------------ overview
const TREE = `main.py                 one entry point (python main.py ...)
configs/                api.yaml · experiment.yaml · carla.yaml · experiments.yaml · schemas/
prompts/                v1–v4 (one marking) · lane_v1 (my lane) · regulation_extraction/
regulations/            <CODE>/ region.yaml, passages, rule tables · _template/ · _common/ · inbox/
datasets/               <CODE>/ dataset.yaml + label collections · _template/ · splits/
results/                runs/ (model runs) · carla/ (simulation runs) · reports/ · index.csv
reasoning_drive/        the code
  agent/                prompts, API client, the two tasks, reasoning trace
  evaluation/           scoring, metrics (F1, confusion), experiments, review, results index
  regulations/          country files, PDF -> rule passages
  labeling/             the labeling tool
  simulation/           CARLA routes and their videos
  web/                  this page and the model page
  tests/                self-tests
docs/ · notebooks/ · deploy/ (Docker, Prometheus, Grafana)`;

async function loadOverview() {
  const o = await api("overview");
  $("#ov-tree").textContent = TREE;
  table($("#ov-settings"), ["", ""], [
    [t("settings_model"), `${esc(o.model)} · effort ${esc(o.reasoning_effort)}`],
    [t("settings_mode"), o.mock ? t("mock") : t("real")],
    [t("key"), o.api_key_set ? `<span class="yes">${t("set")}</span>` : `<span class="no">${t("notset")}</span>`],
    [t("test"), esc(o.test)], [t("region"), esc(o.region)], [t("prompt"), esc(o.prompt)], [t("lane_prompt"), esc(o.lane_prompt)],
    [t("split"), esc(o.split)], [t("routes"), esc(o.routes.join(", "))]]);
  $("#ov-settings").classList.add("kv");
  table($("#ov-countries"), [t("code"), t("name"), t("side"), t("passages"), t("tables"), t("draft"), t("standard")],
    o.countries.map((c) => [esc(c.code), esc(c.name), esc(c.driving_side), c.passages,
      (c.rule_table_marking ? "marking " : "") + (c.rule_table_lane ? "lane" : ""), esc(c.status || "") + (c.draft ? " · draft ✓" : ""), esc(c.standard)]));
  const rows = [];
  o.datasets.forEach((d) => d.collections.forEach((c) => rows.push([esc(d.code), esc(c.name), esc(c.kind), c.marking_rows, c.lane_rows, esc(c.source)])));
  table($("#ov-datasets"), [t("code"), t("collections"), t("kind"), t("rows_marking"), t("rows_lane"), t("source")], rows);
}

// ------------------------------------------------------------------ results and evaluation
let RUNS = [], SEL = [];
async function loadResults() {
  RUNS = await api("results");
  const kinds = [...new Set(RUNS.map((r) => r.kind))];
  const sel = $("#r-kind"), cur = sel.value;
  sel.innerHTML = `<option value="">${t("all")}</option>` + kinds.map((k) => `<option>${esc(k)}</option>`).join("");
  sel.value = cur;
  drawRuns();
}
function drawRuns() {
  const k = $("#r-kind").value, rows = RUNS.filter((r) => !k || r.kind === k);
  $("#r-count").textContent = rows.length + " runs · results/index.csv";
  const head = ["run_id", "kind", "test", "region", "prompt", "model", "images", "main_metric", "unsafe", "cost_usd", "experiments"];
  $("#r-table").innerHTML = "<tr>" + head.map((h) => `<th>${h}</th>`).join("") + "</tr>" +
    rows.map((r) => `<tr data-id="${esc(r.run_id)}" data-kind="${esc(r.kind)}" class="${SEL.includes(r.run_id) ? "sel" : ""}">` +
      head.map((h) => `<td>${esc(r[h])}</td>`).join("") + "</tr>").join("");
  document.querySelectorAll("#r-table tr[data-id]").forEach((tr) => tr.onclick = (ev) => pickRun(tr.dataset.id, tr.dataset.kind, ev.shiftKey));
}
async function pickRun(id, kind, add) {
  if (kind.startsWith("carla")) { show("carla"); return; }
  SEL = add && SEL.length === 1 && SEL[0] !== id ? [SEL[0], id] : [id];
  drawRuns();
  const out = $("#r-eval"); out.innerHTML = '<div class="card muted">…</div>';
  try {
    const e = await api("evaluate?run=" + encodeURIComponent(SEL[0]) + (SEL[1] ? "&other=" + encodeURIComponent(SEL[1]) : ""));
    out.innerHTML = (e.table ? `<div class="card"><h3>${t("compare_h")}</h3>${mdTable(e.table)}</div>` : "") +
      `<div class="metrics">${evalCard(e.run)}${e.other ? evalCard(e.other) : ""}</div>`;
  } catch (err) { out.innerHTML = `<div class="card no">${esc(err.message)}</div>`; }
}
function mdTable(md) {
  const lines = md.trim().split("\n").filter((l) => !/^\|[-| ]+\|$/.test(l));
  const cells = (l) => l.split("|").slice(1, -1).map((c) => c.trim());
  return "<table>" + lines.map((l, i) => "<tr>" + cells(l).map((c) => i ? `<td>${esc(c)}</td>` : `<th>${esc(c)}</th>`).join("") + "</tr>").join("") + "</table>";
}
function cmTable(cm) {
  const c = cm.classes;
  return '<table class="cm"><tr><th>label \\ answer</th>' + c.map((x) => `<th>${esc(x)}</th>`).join("") + "</tr>" +
    cm.matrix.map((row, i) => `<tr><th>${esc(c[i])}</th>` + row.map((v, j) =>
      `<td class="${v === 0 ? "zero" : i === j ? "diag" : "off"}">${v}</td>`).join("") + "</tr>").join("") + "</table>";
}
function prfRows(o) {
  return Object.entries(o).map(([k, v]) => [esc(k), v.support, fmt(v.precision), fmt(v.recall), fmt(v.f1)]);
}
function evalCard(e) {
  const a = e.actions;
  let h = `<div class="card"><h3>${esc(e.run_id)}</h3><div class="small muted">${esc(e.task)} · Test ${esc(e.test)} · ${esc(e.region)} · ${esc(e.prompt)} · ${esc(e.model)} · ${e.images} images × ${e.repeats}</div>
    <h4>${t("actions_h")}</h4>
    <div class="score"><span class="tag">${t("cells")} ${a.cells}</span><span class="tag">${t("acc")} ${fmt(a.accuracy)}</span>
    <span class="tag">${t("macro")} ${fmt(a.macro_f1)}</span><span class="tag ${a.unsafe ? "bad" : "ok"}">${t("unsafe")} ${a.unsafe}</span>
    <span class="tag ${a.over_cautious ? "warn" : "ok"}">${t("over")} ${a.over_cautious}</span></div>`;
  const tb = document.createElement("table");
  table(tb, ["class", "support", "precision", "recall", "F1", "TP", "FP", "FN"],
    ["prohibited", "allowed"].map((c) => [c, a[c].support, fmt(a[c].precision), fmt(a[c].recall), fmt(a[c].f1), a[c].tp, a[c].fp, a[c].fn]));
  h += tb.outerHTML + `<div class="small muted">${t("per_action")}: ` +
    Object.entries(a.prohibited_recall_by_action).map(([k, v]) => `${esc(k)} ${fmt(v)}`).join(" · ") + "</div>";
  h += `<h4>${t("cm")}</h4>` + cmTable(a.confusion);
  if (e.output1) {
    const t1 = document.createElement("table");
    table(t1, ["class", "support", "precision", "recall", "F1"], prfRows(e.output1.per_class));
    h += `<h4>${t("o1_h")} · ${t("acc")} ${fmt(e.output1.accuracy)} · ${t("macro")} ${fmt(e.output1.macro_f1)}</h4>` + t1.outerHTML + cmTable(e.output1.confusion);
  }
  if (e.boundaries) {
    const t2 = document.createElement("table");
    table(t2, ["", "n", t("acc"), t("macro")], Object.entries(e.boundaries).map(([k, v]) => [esc(k), v.n, fmt(v.accuracy), fmt(v.macro_f1)]));
    h += `<h4>${t("bd_h")}</h4>` + t2.outerHTML;
    ["left_pattern", "right_pattern"].forEach((k) => { h += `<div class="small muted">${k}</div>` + cmTable(e.boundaries[k].confusion); });
    h += `<h4>${t("mk_h")}</h4><div>precision ${fmt(e.markings.precision)} · recall ${fmt(e.markings.recall)} · F1 ${fmt(e.markings.f1)}</div>`;
  }
  if (e.subsets && Object.keys(e.subsets).length) {
    const t3 = document.createElement("table");
    table(t3, ["", "n", t("sub_correct"), t("acc"), t("sub_unsafe")], Object.entries(e.subsets).map(([k, v]) => [esc(k), v.n, v.correct, fmt(v.accuracy), v.unsafe]));
    h += `<h4>${t("sub_h")}</h4>` + t3.outerHTML;
  }
  if (e.region_inference) h += `<div class="small">${t("ri")}: ${esc(JSON.stringify(e.region_inference.named))} · ${e.region_inference.correct}/${e.region_inference.n}</div>`;
  if (e.passages_per_prompt) h += `<div class="small">${t("ppp")}: ${esc(JSON.stringify(e.passages_per_prompt))}</div>`;
  return h + "</div>";
}

// ------------------------------------------------------------------ regulations
async function loadRegulations() {
  const r = await api("regulations");
  table($("#rg-countries"), [t("code"), t("name"), t("side"), t("passages"), t("tables"), t("draft"), t("standard")],
    r.countries.map((c) => [esc(c.code), esc(c.name), esc(c.driving_side), c.passages,
      (c.rule_table_marking ? "marking " : "") + (c.rule_table_lane ? "lane" : ""), esc(c.status || "") + (c.draft ? " · draft ✓" : ""), esc(c.standard)]));
  $("#rg-problems").innerHTML = r.problems.length ? r.problems.map((p) => `<div class="no">${esc(p)}</div>`).join("") : `<span class="yes">${t("problems_none")}</span>`;
  const f = $("#rg-file"), cur = f.value;
  f.innerHTML = r.inbox.map((x) => `<option>${esc(x)}</option>`).join("") || `<option value="">(regulations/inbox/)</option>`;
  if (cur) f.value = cur;
  const drafts = r.countries.filter((c) => c.draft).map((c) => c.code);
  const d = $("#rg-draft-code"), dc = d.value;
  d.innerHTML = drafts.map((c) => `<option>${esc(c)}</option>`).join("") || `<option value="">${t("no_draft")}</option>`;
  if (dc && drafts.includes(dc)) d.value = dc;
  loadDraft();
  pollJobs();
}
function regBody() {
  return { file: $("#rg-file").value, code: $("#rg-code").value.trim().toUpperCase(), name: $("#rg-name").value.trim(),
    driving_side: $("#rg-side").value, title: $("#rg-title").value.trim(), first: $("#rg-first").value || null,
    last: $("#rg-last").value || null, all_pages: $("#rg-all").checked, real: $("#rg-real").checked };
}
async function loadDraft() {
  const code = $("#rg-draft-code").value;
  if (!code) { $("#rg-draft").innerHTML = ""; $("#rg-draft-log").textContent = ""; return; }
  const d = await api("draft?code=" + encodeURIComponent(code));
  const l = d.log || {};
  $("#rg-draft-log").textContent = l.pdf ? `${l.pdf}: ${l.passages} passages, ${l.verified_quotes} ${t("verified")} · ${l.mock ? "mock" : "$" + l.cost_usd} · ${l.time_utc}` : "";
  table($("#rg-draft"), ["rule_id", "page", "marking_type", "element", "text_original", "text_en", t("verified"), "actions_stated"],
    d.passages.map((p) => [esc(p.rule_id), p.page, esc(p.marking_type), esc(p.element), esc(p.text_original), esc(p.text_en),
      p.verified_quote ? '<span class="yes">✓</span>' : '<span class="no">✗</span>', esc(JSON.stringify(p.actions_stated || {}))]));
}

// ------------------------------------------------------------------ jobs (extraction and CARLA)
let SINCE = {}, JOBLOG = {};
async function pollJobs() {
  try {
    const jobs = await api("jobs?since=" + encodeURIComponent(JSON.stringify(SINCE)));
    let running = false;
    jobs.forEach((j) => {
      JOBLOG[j.id] = (JOBLOG[j.id] || []).concat(j.log); SINCE[j.id] = j.log_total;
      JOBLOG[j.id + ":meta"] = j; running = running || j.running;
    });
    ["extract", "carla"].forEach((kind) => {
      const el = kind === "extract" ? $("#rg-jobs") : $("#ca-jobs");
      el.innerHTML = jobs.filter((j) => j.kind === kind).map((j) => `<div class="job"><b>${esc(j.title)}</b>
        <span class="tag ${j.running ? "warn" : j.error ? "bad" : "ok"}">${j.running ? "…" : j.error ? "error" : "done"}</span>
        ${j.error ? `<div class="no">${esc(j.error)}</div>` : ""}<pre>${esc(JOBLOG[j.id].slice(-200).join("\n"))}</pre></div>`).join("");
    });
    if (running) setTimeout(pollJobs, 1500);
    else if (jobs.some((j) => !j.running && !JOBLOG[j.id + ":seen"])) {
      jobs.forEach((j) => { JOBLOG[j.id + ":seen"] = true; });
      if (!$("#p-regulations").classList.contains("hidden")) loadRegulations();
    }
  } catch (e) { toast(e.message, true); }
}

// ------------------------------------------------------------------ CARLA
let CARLA = null;
async function loadCarla() {
  CARLA = await api("carla");
  const s = CARLA.server;
  table($("#ca-server"), ["", ""], [["host:port", `${esc(s.host)}:${esc(s.port)} · ${CARLA.reachable ? `<span class="yes">${t("reachable")}</span>` : `<span class="no">${t("not_reachable")}</span>`}`],
    ["carla_root", esc(s.carla_root)], ["version", esc(s.version)],
    [t("python"), (CARLA.carla_in_this_python ? "(this Python) " : esc(s.python) + " ") + (CARLA.python_ok ? '<span class="yes">✓</span>' : '<span class="no">✗</span>')]]);
  $("#ca-server").classList.add("kv");
  const sel = $("#ca-route"), cur = sel.value;
  sel.innerHTML = Object.keys(CARLA.routes).map((k) => `<option>${esc(k)}</option>`).join("");
  if (cur) sel.value = cur;
  routeStops();
  $("#ca-run").disabled = !CARLA.python_ok;
  $("#ca-runs").innerHTML = CARLA.runs.map(runCard).join("");
  document.querySelectorAll(".thumbs img").forEach((img) => img.onclick = () => window.open(img.src, "_blank"));
  pollJobs();
}
function routeStops() {
  const r = CARLA && CARLA.routes[$("#ca-route").value];
  if (!r) return;
  $("#ca-route-stops").innerHTML = `${esc(r.map)} · ${esc(r.weather)}${r.night ? " · night" : ""}<ol>` +
    r.stops.map((s) => `<li>${esc(s.label)} → <span class="muted">${esc(s.intent)}</span></li>`).join("") + "</ol>";
}
function runCard(r) {
  const m = r.meta || {};
  const pe = Object.entries(r.per_experiment || {});
  const tb = document.createElement("table");
  const keys = pe.length ? Object.keys(pe[0][1]).filter((k) => typeof pe[0][1][k] !== "object") : [];
  table(tb, [""].concat(keys), pe.map(([k, v]) => [esc(k)].concat(keys.map((x) => esc(fmt(v[x]))))));
  const imgs = (kind, names) => names.map((n) => `<figure><img loading="lazy" src="/api/project/carla_image?run=${encodeURIComponent(r.run)}&kind=${kind}&name=${encodeURIComponent(n)}">
    <figcaption>${kind} ${esc(n)}</figcaption></figure>`).join("");
  const stops = r.stops.length ? (() => { const s = document.createElement("table");
    table(s, ["#", t("stops"), t("intent"), t("did")], r.stops.map((x) => [x.stop, esc(x.label), esc(x.intent), esc(x.action || x.system_says || "")])); return s.outerHTML; })() : "";
  return `<div class="card"><h3>${esc(r.run)} <span class="muted small">${esc(m.map || "")} · ${esc(m.weather || "")} · ${esc(m.prompt || "")} · ${esc(m.model || "")} ${m.mock ? "· mock" : ""} · $${fmt(r.cost_usd)}</span>
    ${r.video ? `<a class="small" href="/api/project/carla_video?run=${encodeURIComponent(r.run)}" target="_blank">${t("video")}</a>` : ""}</h3>
    ${tb.outerHTML}${(r.findings || []).map((f) => `<div class="finding ${esc(f[1])}">${esc(f[0])}</div>`).join("")}${stops}
    <div class="thumbs">${imgs("decisions", r.decisions)}</div></div>`;
}

// ------------------------------------------------------------------ events
document.querySelectorAll("#tabs button").forEach((b) => b.onclick = () => show(b.dataset.tab));
$("#lang-btn").onclick = () => { LANG = LANG === "zh" ? "en" : "zh"; localStorage.setItem("rd_lang", LANG); applyLang(); show((location.hash || "#overview").slice(1)); };
$("#r-kind").onchange = drawRuns;
$("#rg-draft-code").onchange = loadDraft;
$("#rg-upload-btn").onclick = () => $("#rg-upload").click();
$("#rg-upload").onchange = async (ev) => {
  const f = ev.target.files[0]; if (!f) return;
  const b64 = await new Promise((res) => { const r = new FileReader(); r.onload = () => res(r.result.split(",")[1]); r.readAsDataURL(f); });
  try { const r = await api("upload", { filename: f.name, pdf_base64: b64 }); toast("regulations/inbox/" + r.file); await loadRegulations(); $("#rg-file").value = r.file; }
  catch (e) { toast(e.message, true); }
};
$("#rg-estimate").onclick = async () => {
  try { const e = await api("estimate", regBody());
    $("#rg-est").textContent = `${e.file}: ${e.pages} pages (${e.pages_with_text} with text) · ${t("pages_read")} ${e.pages_read} · ${t("requests")} ${e.requests} · ${t("cost")} $${e.cost_usd} (${e.model})`; }
  catch (e) { toast(e.message, true); }
};
$("#rg-extract").onclick = async () => {
  const b = regBody();
  if (b.real && !confirm(LANG === "zh" ? "用真实 API 提取会产生费用（先点“估算”看看）。继续吗？" : "Extracting with the real API costs money (see Estimate first). Go on?")) return;
  try { await api("extract", b); SINCE = {}; pollJobs(); } catch (e) { toast(e.message, true); }
};
$("#rg-accept").onclick = async () => {
  const code = $("#rg-draft-code").value; if (!code) return;
  if (!confirm((LANG === "zh" ? "接受草稿：它将成为 " : "Accept the draft: it becomes the passages of ") + code + (LANG === "zh" ? " 的条文。确认读过了吗？" : ". Read it already?"))) return;
  try { const r = await api("accept", { code }); toast(r.file); loadRegulations(); } catch (e) { toast(e.message, true); }
};
$("#ca-route").onchange = routeStops;
$("#ca-start").onclick = async () => { try { const r = await api("start_carla", {}); toast(r.note); setTimeout(loadCarla, 5000); } catch (e) { toast(e.message, true); } };
$("#ca-run").onclick = async () => {
  const mock = $("#ca-mock").checked;
  if (!mock && !confirm(LANG === "zh" ? "真实 API：每站 A/B/C 各问一次，会产生费用。继续吗？" : "Real API: A, B and C are asked once per stop, which costs money. Go on?")) return;
  try { await api("run_route", { route: $("#ca-route").value, mock, preview: $("#ca-preview").checked }); pollJobs(); } catch (e) { toast(e.message, true); }
};

applyLang();
show((location.hash || "#overview").slice(1) || "overview");
