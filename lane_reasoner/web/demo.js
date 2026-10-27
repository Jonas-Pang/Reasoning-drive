/* Reasoning Driving demo page */
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const LANG_KEY = "lane-demo-lang";
const ACTS = ["cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_center_lane_to_wait"];

const TXT = {
  zh: {
    region: "地区", mode_mock: "模拟", mode_real: "真实 API", settings: "模型设置", lang: "English", images: "已标注的图",
    all_types: "全部类型", use_cache: "相同请求用缓存（不重复花钱）", tab_prompt: "提示词", tab_batch: "批量运行", tab_io: "输入 / 输出设计",
    ask: "问模型 · Test {t}", ask_both: "A 和 B 都问", asking: "正在问模型（Test {t}）…", test_A: "Test A · 只有图片", test_B: "Test B · 图片 + 法规",
    key_ok: "API key 已设置 {h}", key_missing: "没有 API key", banner_mock: "模拟模式：答案是程序编的（Test A 故意多错一些），没有调用模型，也不花钱。演示真实结果请切到“真实 API”。",
    banner_nokey: "真实 API 模式需要 API key：在 notebook 里运行“设置 API key”那一格（key 只存在仓库的 .env 文件里，Git 不会上传）。",
    prompt_help: "这是发给模型的完整文字（图片另外附上）。Test B 只比 Test A 多了下面的法规条文，以及指令里标蓝的两行；其余部分两组完全一样。",
    p_instructions: "① 指令（developer 消息）。两组只有标蓝的两行不同",
    p_rules: "①′ 法规条文：只在 Test B，接在指令后面（同一条 developer 消息）", p_user: "② 用户消息（后面附上画了青色框的图片）", p_schema: "③ 输出格式（JSON schema，严格模式）",
    batch_help: "对当前地区所有已标注的图跑一遍（选 A + B 时两组同时跑，跑完自动比较），结果存在 runs/ 里（只有文字，没有图片和 key）。0 = 全部。勾选了“用缓存”时，问过的相同请求直接用旧答案（不花钱）。",
    limit: "张数", repeats: "重复次数", run: "开始运行", runs: "运行记录（点两条再比较）", compare: "比较选中的两次", compare_help: "McNemar 配对检验",
    cancel: "取消", apply: "应用", save_default: "同时保存为默认设置（写入 config/experiment.json）",
    settings_help: "这些设置对 Test A 和 Test B 完全一样。API key 不在这里，放在 .env 里。",
    field: "项目", label: "标注（标准答案）", answer: "模型回答", o1: "输出 1", o2: "输出 2", cite: "引用",
    marking_type: "标线类型", arrow_type: "箭头类型", position: "位置", evidence: "证据", cited_rule_id: "引用的条文",
    description: "描述", reasoning: "理由", cited_passage: "引用条文原文", tokens: "tokens", latency: "耗时", cost: "费用", cached: "缓存", mock: "模拟",
    running: "运行中 {d}/{n}…", finished: "完成：{id}", none: "—", err: "出错：",
    eg_correct: "正确", eg_wrong: "错误", eg_unsupported_guess: "无依据猜测", eg_appropriate_withholding: "恰当保留", eg_over_withholding: "过度保留",
    c_accepted: "引用正确", c_in_pack_not_accepted: "引用了不支持答案的条文", c_unlisted: "编造的编号", c_none: "没有引用", c_none_needed: "无需引用（正确）",
    unsafe: "不安全错误", cautious: "过度保守", contested: "有争议的格子（单独统计）",
    cmp_n: "共同的图", cmp_acc: "{x} 准确率", cmp_only: "只有 {x} 对", cmp_p: "p 值", cmp_same: "两次设置相同、共同的提示词部分相同",
    no_items: "这个地区还没有已完成的标注。", pick_two: "先在列表里点选两次运行。", run_n: "运行", r_errors: "出错", r_readable: "可读的回答",
  },
  en: {
    region: "Region", mode_mock: "Mock", mode_real: "Real API", settings: "Model settings", lang: "中文", images: "Labeled images",
    all_types: "All types", use_cache: "Reuse cached answers for identical requests", tab_prompt: "Prompt", tab_batch: "Batch run", tab_io: "Input / output design",
    ask: "Ask the model · Test {t}", ask_both: "Ask A and B", asking: "Asking the model (Test {t}) …", test_A: "Test A · image only", test_B: "Test B · image + rules",
    key_ok: "API key set {h}", key_missing: "No API key", banner_mock: "Mock mode: the answers are made up by the program (Test A makes more mistakes on purpose); no model is called and nothing is paid. Switch to Real API for real results.",
    banner_nokey: "Real API mode needs an API key: run the 'Set the API key' cell in the notebook (the key is stored only in the repository's .env file, which Git ignores).",
    prompt_help: "The full text sent to the model (the image is attached separately). Test B only adds the rule passages below and changes the two highlighted lines; everything else is identical in both tests.",
    p_instructions: "① Instructions (developer message). Only the two highlighted lines differ between the tests",
    p_rules: "①′ Rule passages: Test B only, appended to the instructions (same developer message)", p_user: "② User message (followed by the image with the cyan box)", p_schema: "③ Output format (JSON schema, strict)",
    batch_help: "Run every labeled image of the current region (A + B runs both tests at the same time and compares them); results go to runs/ (text only: no images, no key). 0 = all. With 'reuse cached answers' ticked, identical requests asked before are not paid again.",
    limit: "Images", repeats: "Repeats", run: "Run", runs: "Runs (click two to compare)", compare: "Compare the two selected", compare_help: "McNemar paired test",
    cancel: "Cancel", apply: "Apply", save_default: "Also save as default (config/experiment.json)",
    settings_help: "These settings are identical for Test A and Test B. The API key is not here; it lives in .env.",
    field: "Field", label: "Label (ground truth)", answer: "Model answer", o1: "Output 1", o2: "Output 2", cite: "Citation",
    marking_type: "Marking type", arrow_type: "Arrow type", position: "Position", evidence: "Evidence", cited_rule_id: "Cited rule",
    description: "Description", reasoning: "Reasoning", cited_passage: "Cited passage", tokens: "tokens", latency: "time", cost: "cost", cached: "cached", mock: "mock",
    running: "Running {d}/{n} …", finished: "Finished: {id}", none: "—", err: "Error: ",
    eg_correct: "correct", eg_wrong: "wrong", eg_unsupported_guess: "unsupported guess", eg_appropriate_withholding: "appropriate withholding", eg_over_withholding: "over-withholding",
    c_accepted: "citation accepted", c_in_pack_not_accepted: "cited a passage that does not support it", c_unlisted: "made-up ID", c_none: "no citation", c_none_needed: "no passage applies (right)",
    unsafe: "unsafe errors", cautious: "over-cautious", contested: "contested cells (separate)",
    cmp_n: "Shared images", cmp_acc: "{x} accuracy", cmp_only: "only {x} right", cmp_p: "p-value", cmp_same: "same settings and same shared prompt parts",
    no_items: "No finished labels for this region yet.", pick_two: "Click two runs in the list first.", run_n: "run", r_errors: "errors", r_readable: "readable answers",
  },
};
const IO = {
  zh: `<h4>输入</h4><ul>
<li><b>图片</b>：标注时画的目标框用青色画在图片的副本上，原图不改。和指令一起发给模型（高清，<code>detail: high</code>）。</li>
<li><b>地区</b>：一句话“This photo was taken in the United States / China”，两组都有。</li>
<li><b>指令</b>：任务、三步推理（描述 → 匹配规则 → 判断）和每个输出字段的含义。<b>只定义题目，不含任何地区的规则。</b></li>
<li><b>Test B 额外加上</b>：这个地区的全部法规条文（来自 <code>rules/rule_passages.json</code>），每条带编号、出处、章节和页码。只能引用这些编号。</li></ul>
<h4>输出（固定格式，严格 JSON schema）</h4><ul>
<li><code>description</code>：第一步，描述框里的标线</li>
<li><code>evidence</code>：full / partial / insufficient</li>
<li><code>marking</code>：输出 1，标线类型、箭头类型、位置</li>
<li><code>actions</code>：输出 2，6 个动作各自 allowed / prohibited / not_determined / not_applicable</li>
<li><code>cited_rule_id</code>：Test B 引用的条文编号（Test A 为 null）</li>
<li><code>reasoning</code>：一两句理由（只给人看，程序不读）</li></ul>
<h4>怎么调用 API</h4><ul>
<li>OpenAI Responses API：<code>POST https://api.openai.com/v1/responses</code>，用标准库发请求，不依赖 SDK。</li>
<li>设置在 <code>config/experiment.json</code>：模型、reasoning_effort、temperature、图片清晰度、最大输出长度。两组完全相同。</li>
<li>API key 只从环境变量（<code>.env</code> 文件）读取，不写进任何会上传的文件；每次运行只保存“有没有 key”。</li>
<li>每次运行在 <code>runs/&lt;运行编号&gt;/</code> 保存设置、提示词哈希、模型返回的版本号、原始回答、评分和 token 用量。</li></ul>
<h4>评分</h4><ul>
<li>输出 1：类型（箭头再加箭头类型）和标注相同才算对。</li>
<li>输出 2：标线管的每个动作都对才算对；有争议的格子单独统计。</li>
<li>还会统计：五组证据、引用检查（Test B）、不安全 / 过度保守错误，以及 A 对 B 的 McNemar 配对检验。</li></ul>
<h4>加一个新国家</h4><ol>
<li>在 <code>config/experiment.json</code> 的 <code>regions</code> 里加一项（名称、规则文件里的地区代码、法规名称）。</li>
<li>把这个国家的条文加进 <code>rules/rule_passages.json</code>（同一个地区代码）。</li>
<li>用标注工具标好这个国家的图。页面上的地区选择就会出现它。</li></ol>`,
  en: `<h4>Input</h4><ul>
<li><b>Image</b>: a copy with the labeled target box drawn in cyan (the original is not changed), sent with <code>detail: high</code>.</li>
<li><b>Region</b>: one sentence, "This photo was taken in the United States / China", in both tests.</li>
<li><b>Instructions</b>: the task, three reasoning steps (describe → match a rule → decide) and the meaning of every field. <b>They define the task only; no region's rules are in them.</b></li>
<li><b>Test B adds</b>: every rule passage of the region (from <code>rules/rule_passages.json</code>) with its ID, source, section and page. Only these IDs may be cited.</li></ul>
<h4>Output (fixed, strict JSON schema)</h4><ul>
<li><code>description</code>: step 1, the marking in the box</li>
<li><code>evidence</code>: full / partial / insufficient</li>
<li><code>marking</code>: Output 1, marking type, arrow type, position</li>
<li><code>actions</code>: Output 2, six actions, each allowed / prohibited / not_determined / not_applicable</li>
<li><code>cited_rule_id</code>: the passage cited in Test B (null in Test A)</li>
<li><code>reasoning</code>: one or two sentences (for people; not scored)</li></ul>
<h4>How the API is called</h4><ul>
<li>OpenAI Responses API, <code>POST https://api.openai.com/v1/responses</code>, with the Python standard library (no SDK).</li>
<li>Settings in <code>config/experiment.json</code>: model, reasoning_effort, temperature, image detail, max output tokens; identical in both tests.</li>
<li>The key is read only from the environment (<code>.env</code>), never written to a tracked file; a run records only whether a key was set.</li>
<li>Every run keeps settings, prompt hashes, the model ID returned, raw answers, scores and token use in <code>runs/&lt;run_id&gt;/</code>.</li></ul>
<h4>Scoring</h4><ul>
<li>Output 1: the type (and arrow type for arrows) matches the label.</li>
<li>Output 2: every action the marking decides matches; contested cells are counted separately.</li>
<li>Also: the five evidence groups, the citation check (Test B), unsafe vs over-cautious errors, and McNemar between A and B.</li></ul>
<h4>Adding a country</h4><ol>
<li>Add an entry under <code>regions</code> in <code>config/experiment.json</code> (name, region code in the rule file, rules title).</li>
<li>Add its passages to <code>rules/rule_passages.json</code> with that region code.</li>
<li>Label its images with the labeling tool; the region then appears in the selector.</li></ol>`,
};
const S = { lang: "zh", runs: [], cfg: null, test: "A", region: "US", items: [], sel: null, results: {}, prompt: null, runsSel: [], poll: null };
try { S.lang = localStorage.getItem(LANG_KEY) || "zh"; } catch (e) { /* storage not available */ }
const t = (k, v) => { let s = (TXT[S.lang] || TXT.zh)[k] ?? TXT.zh[k] ?? k; for (const [a, b] of Object.entries(v || {})) s = s.split("{" + a + "}").join(b); return s; };

async function api(path, body) {
  const r = await fetch(path, body === undefined ? {} : { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
  const j = await r.json().catch(() => ({ error: "HTTP " + r.status }));
  if (!r.ok || j.error) throw new Error(j.error || "HTTP " + r.status);
  return j;
}
function applyStatic() {
  for (const el of document.querySelectorAll("[data-t]")) el.textContent = t(el.dataset.t);
  $("lang-btn").textContent = t("lang");
  for (const b of $("test-seg").querySelectorAll("button")) b.textContent = t("test_" + b.dataset.test);
  $("ask-a").textContent = t("ask", { t: "A" }); $("ask-b").textContent = t("ask", { t: "B" }); $("ask-both").textContent = t("ask_both");
  $("io-text").innerHTML = IO[S.lang];
}
function renderTop() {
  const c = S.cfg.config;
  for (const b of $("test-seg").querySelectorAll("button")) b.classList.toggle("on", b.dataset.test === S.test);
  for (const b of $("mode-seg").querySelectorAll("button")) b.classList.toggle("on", (b.dataset.mock === "1") === !!c.mock);
  const k = $("keyinfo");
  k.textContent = c.api.api_key_set ? t("key_ok", { h: c.api.api_key_hint }) : t("key_missing");
  k.className = "pill " + (c.api.api_key_set ? "ok" : "bad");
  $("modelinfo").textContent = `${c.api.model} · effort ${c.api.reasoning_effort ?? "—"} · T ${c.api.temperature ?? "—"}`;
  const ban = $("banner");
  if (c.mock) { ban.textContent = t("banner_mock"); ban.classList.remove("hidden"); }
  else if (!c.api.api_key_set) { ban.textContent = t("banner_nokey"); ban.classList.remove("hidden"); }
  else ban.classList.add("hidden");
  $("region").innerHTML = Object.entries(c.regions).map(([code, r]) =>
    `<option value="${esc(code)}"${code === S.region ? " selected" : ""}>${esc(S.lang === "zh" ? (r.name_zh || r.name) : r.name)} (${esc(code)}) · ${S.cfg.items_per_region[code] || 0}</option>`).join("");
}
async function setCfg(changes) { S.cfg = await api("/api/config", changes); renderTop(); }

async function loadItems() {
  S.items = await api("/api/items?region=" + encodeURIComponent(S.region));
  $("type-filter").value = "";
  renderFilter();
  renderItems();
  if (S.items.length) select(S.items[0].image_id); else { $("img").removeAttribute("src"); $("imgmeta").textContent = t("no_items"); $("results").innerHTML = ""; }
}
function renderFilter() {
  const cur = $("type-filter").value;
  const types = [...new Set(S.items.map((i) => i.marking))].sort();
  $("type-filter").innerHTML = `<option value="">${esc(t("all_types"))} (${S.items.length})</option>` +
    types.map((x) => `<option${x === cur ? " selected" : ""}>${esc(x)}</option>`).join("");
}
function renderItems() {
  const f = $("type-filter").value;
  const rows = S.items.filter((i) => !f || i.marking === f);
  $("count").textContent = rows.length;
  $("items").innerHTML = rows.map((i) => `<li data-id="${esc(i.image_id)}" class="${i.image_id === S.sel ? "sel" : ""}">
    <img loading="lazy" src="/api/image?id=${encodeURIComponent(i.image_id)}&w=200" alt=""><div class="m"><b>${esc(i.marking)}</b><br>${esc(i.visibility)} · ${esc(i.collection)} · ${esc(i.split)}<br><span class="muted">${esc(i.image_id.slice(-12))}</span></div></li>`).join("");
  for (const li of $("items").querySelectorAll("li")) li.addEventListener("click", () => select(li.dataset.id));
}
function select(id) {
  S.sel = id; S.results = {};
  for (const li of $("items").querySelectorAll("li")) li.classList.toggle("sel", li.dataset.id === id);
  const it = S.items.find((i) => i.image_id === id);
  $("img").src = "/api/image?id=" + encodeURIComponent(id);
  $("imgmeta").textContent = `${id} · ${it.dataset} · ${it.width}×${it.height}`;
  $("results").innerHTML = ""; $("ask-msg").textContent = "";
}
async function loadPrompt() {
  S.prompt = await api(`/api/prompt?test=${S.test}&region=${encodeURIComponent(S.region)}`);
  const rb = S.prompt.rules_block || "";
  let ins = S.prompt.instructions;
  if (rb) ins = ins.replace(rb, "").replace(/\n+$/, "");
  ins = esc(ins);
  for (const slot of Object.values(S.prompt.slots || {})) ins = ins.replace(esc(slot), `<mark>${esc(slot)}</mark>`);
  $("p-instructions").innerHTML = ins;
  $("p-rules").textContent = rb;
  $("p-rules-wrap").classList.toggle("hidden", !rb);
  $("p-user").textContent = S.prompt.user_text + "\n[image: the photo with the cyan box]";
  $("p-schema").textContent = JSON.stringify(S.prompt.schema, null, 2);
  const h = S.prompt.hashes;
  $("p-hashes").textContent = `instructions ${h.instructions} · shared parts ${h.shared_parts} · rules file ${h.rules_file} · ${h.prompt_dir}`;
}

const cls = (ok) => ok === true ? "ok" : ok === false ? "bad" : "na";
const mark = (ok) => ok === true ? " ✓" : ok === false ? " ✗" : "";
function tags(rec) {
  const sc = rec.score;
  let h = (rec.mock ? `<span class="tag warn">${t("mock")}</span>` : "") + (rec.cached ? `<span class="tag">${t("cached")}</span>` : "");
  if (!sc) return h;
  return h + `<div class="score"><span class="tag ${cls(sc.output1)}">${t("o1")}${mark(sc.output1)}</span>` +
    `<span class="tag ${cls(sc.output2)}">${t("o2")}${sc.output2 === null ? " —" : mark(sc.output2)}</span>` +
    `<span class="tag">${esc(t("eg_" + sc.evidence_group))}</span>` +
    (sc.citation ? `<span class="tag ${["accepted", "none_needed"].includes(sc.citation) ? "ok" : "bad"}">${esc(t("c_" + sc.citation))}</span>` : "") +
    (sc.unsafe.length ? `<span class="tag bad">${t("unsafe")}: ${sc.unsafe.join(", ")}</span>` : "") + `</div>`;
}
function renderResults() {
  const tests = ["A", "B"].filter((x) => S.results[x]);
  if (!tests.length) { $("results").innerHTML = ""; return; }
  const L = S.results[tests[0]].label;
  const recs = tests.map((x) => S.results[x]);
  const ans = (r) => r.answer || null;
  const anyArrow = L.marking_type === "arrow" || recs.some((r) => ans(r) && ans(r).marking.arrow_type);
  const contested = new Set(recs.flatMap((r) => r.score ? Object.keys(r.score.contested) : []));
  const cell = (r, get, okf) => {
    const a = ans(r);
    if (!a) return `<td class="na">—</td>`;
    const v = get(a), ok = okf(a, v);
    return `<td class="${cls(ok)}">${esc(v ?? "null")}${mark(ok)}</td>`;
  };
  const row = (name, lab, get, okf) => `<tr><td>${esc(name)}</td><td>${esc(lab || "—")}</td>${recs.map((r) => cell(r, get, okf(r))).join("")}</tr>`;
  const w = tests.length === 2 ? `<col style="width:22%"><col style="width:22%"><col><col>` : `<col style="width:30%"><col style="width:30%"><col>`;
  let h = `<div class="card"><table class="cmp"><colgroup>${w}</colgroup><tr><th>${t("field")}</th><th>${t("label")}</th>` +
    tests.map((x) => `<th class="test">${esc(t("test_" + x))}</th>`).join("") + `</tr>` +
    `<tr class="scores"><td></td><td></td>${recs.map((r) => `<td>${tags(r)}${r.error || (!r.answer && r.parse_error) ? `<div class="msg err">${esc(t("err") + (r.error || r.parse_error))}</div>` : ""}</td>`).join("")}</tr>` +
    row(t("marking_type"), L.marking_type, (a) => a.marking.marking_type, () => (a, v) => v === L.marking_type);
  if (anyArrow) h += row(t("arrow_type"), L.arrow_type, (a) => a.marking.arrow_type, () => (a, v) => (v || "") === (L.arrow_type || ""));
  h += row(t("position"), L.position, (a) => a.marking.position, (r) => () => r.score ? r.score.position : null);
  h += row(t("evidence"), L.expected_evidence, (a) => a.evidence, () => (a, v) => v === L.expected_evidence);
  for (const k of ACTS) {
    h += row(k + (contested.has(k) ? " ◆" : ""), L["act_" + k], (a) => (a.actions || {})[k],
      (r) => () => !r.score ? null : k in r.score.actions ? r.score.actions[k] : k in r.score.contested ? r.score.contested[k] : null);
  }
  if (tests.includes("B")) {
    h += row(t("cited_rule_id"), (L.accepted_rule_ids || "").split(";").join(", "), (a) => a.cited_rule_id,
      (r) => () => r.test === "B" && r.score ? ["accepted", "none_needed"].includes(r.score.citation) : null);
  }
  h += `</table>${contested.size ? `<p class="small muted">◆ ${t("contested")}</p>` : ""}</div><div class="details">`;
  for (const r of recs) {
    const a = ans(r);
    h += `<div class="card"><h3>${esc(t("test_" + r.test))}</h3>`;
    if (a) {
      h += `<p class="small"><b>${t("description")}:</b> ${esc(a.description)}<br><b>${t("reasoning")}:</b> ${esc(a.reasoning)}</p>`;
      if (r.cited_passage) {
        const p = r.cited_passage;
        h += `<div class="quote"><b>${esc(a.cited_rule_id)}</b> ${esc(p.section)}<br>${esc(S.lang === "zh" && p.text_zh ? p.text_zh : p.text_en)}</div>`;
      }
    } else if (r.text) h += `<pre class="prompt">${esc(r.text)}</pre>`;
    const u = (r.response || {}).usage || {};
    if (r.response) h += `<div class="small muted">${esc(r.response.model || "")} · ${t("tokens")} ${u.input_tokens ?? "?"} / ${u.output_tokens ?? "?"} · ${t("latency")} ${r.response.latency_s ?? "?"} s · ${t("cost")} $${r.cost_usd ?? 0}</div>`;
    h += `</div>`;
  }
  $("results").innerHTML = h + `</div>`;
}
async function askModels(tests) {  // several tests are asked at the same time
  if (!S.sel) return;
  const id = S.sel;
  $("ask-msg").textContent = t("asking", { t: tests.join(S.lang === "zh" ? "、" : " + ") }); $("ask-msg").className = "msg";
  const errs = [];
  await Promise.all(tests.map(async (test) => {
    try {
      const rec = await api("/api/ask", { image_id: id, test, cache: $("use-cache").checked });
      if (S.sel !== id) return;
      S.results[test] = rec; renderResults();
    } catch (e) { errs.push(`Test ${test}: ${e.message}`); }
  }));
  if (S.sel !== id) return;
  $("ask-msg").textContent = errs.length ? t("err") + errs.join(" · ") : "";
  $("ask-msg").className = errs.length ? "msg err" : "msg";
}

// ---- batch
async function startRun() {
  try {
    await api("/api/run", { test: $("b-test").value, region: S.region, limit: Number($("b-limit").value || 0), repeats: Number($("b-repeats").value || 1), cache: $("use-cache").checked });
    pollRun();
  } catch (e) { $("b-status").textContent = t("err") + e.message; }
}
function pollRun() {
  clearInterval(S.poll);
  S.poll = setInterval(async () => {
    const p = await api("/api/progress");
    $("b-bar").style.width = p.total ? (100 * p.done / p.total) + "%" : "0";
    const ids = Object.values(p.run_ids || {});
    $("b-status").textContent = p.running ? t("running", { d: p.done, n: p.total || "?" }) : (ids.length ? t("finished", { id: ids.join(" · ") }) : "") + (p.error ? "  " + t("err") + p.error : "");
    if (!p.running) {
      clearInterval(S.poll);
      if (p.run_ids && p.run_ids.A && p.run_ids.B) {  // both tests ran together: compare them right away
        S.runsSel = [p.run_ids.A, p.run_ids.B];
        await loadRuns(); compareRuns(); showRun(p.run_ids.B);
      } else { await loadRuns(); if (p.run_id) showRun(p.run_id); }
    }
  }, 800);
}
async function loadRuns() {
  const runs = S.runs = await api("/api/runs");
  const pct = (x) => x === null || x === undefined ? "—" : Math.round(x * 100) + "%";
  $("runs").innerHTML = `<table class="runs"><tr><th>run</th><th>Test</th><th>n</th><th>${t("o1")}</th><th>${t("o2")}</th><th>$</th></tr>` +
    runs.map((r) => `<tr data-id="${esc(r.run_id)}" class="${S.runsSel.includes(r.run_id) ? "sel" : ""}"><td>${esc(r.run_id.slice(0, 15))}${r.mock ? " (mock)" : ""}</td><td>${r.test}</td><td>${r.n_items}×${r.repeats}</td><td>${pct(r.output1)}</td><td>${pct(r.output2)}</td><td>${r.cost_usd ?? "—"}</td></tr>`).join("") + "</table>";
  for (const tr of $("runs").querySelectorAll("tr[data-id]")) tr.addEventListener("click", () => {
    const id = tr.dataset.id;
    S.runsSel = S.runsSel.includes(id) ? S.runsSel.filter((x) => x !== id) : [...S.runsSel, id].slice(-2);
    loadRuns(); showRun(id);
  });
}
async function showRun(id) {
  const r = await api("/api/run?id=" + encodeURIComponent(id));
  const s = r.summary || {};
  const f = (d) => d && d.n ? `${d.correct}/${d.n} (${Math.round(100 * d.correct / d.n)}%)` : "—";
  const groups = Object.entries(s.evidence_groups || {}).map(([k, v]) => `${t("eg_" + k)} ${v}`).join(" · ");
  const cites = Object.entries(s.citations || {}).map(([k, v]) => `${t("c_" + k)} ${v}`).join(" · ");
  $("run-detail").innerHTML = `<div class="card"><h3>${esc(id)}</h3><table>
    <tr><td>${t("o1")}</td><td>${f(s.output1)}</td></tr><tr><td>${t("o2")}</td><td>${f(s.output2)}</td></tr>
    <tr><td>${t("contested")}</td><td>${f(s.contested)}</td></tr>
    <tr><td>${t("unsafe")} / ${t("cautious")}</td><td>${s.unsafe_errors ?? 0} / ${s.over_cautious_errors ?? 0} <span class="muted">(◆ ${s.contested_unsafe_errors ?? 0} / ${s.contested_over_cautious_errors ?? 0})</span></td></tr>
    <tr><td>${t("evidence")}</td><td>${esc(groups)}</td></tr>${cites ? `<tr><td>${t("cite")}</td><td>${esc(cites)}</td></tr>` : ""}
    <tr><td>${t("tokens")} / ${t("cost")}</td><td>${(s.usage || {}).input_tokens ?? 0} / ${(s.usage || {}).output_tokens ?? 0} · $${s.cost_usd ?? 0}</td></tr>
    <tr><td>${t("r_errors")}</td><td>${s.errors ?? 0} · ${t("r_readable")} ${(s.readable || {}).n ?? 0}/${(s.readable || {}).of ?? 0} · ${t("cached")} ${s.cached ?? 0}</td></tr></table></div>`;
}
async function compareRuns() {
  if (S.runsSel.length !== 2) { $("compare-out").textContent = t("pick_two"); return; }
  try {
    const testOf = (id) => (S.runs.find((r) => r.run_id === id) || {}).test || "";
    const [ra, rb] = [...S.runsSel].sort((x, y) => testOf(x).localeCompare(testOf(y)) || x.localeCompare(y));  // Test A first
    const c = await api(`/api/compare?a=${encodeURIComponent(ra)}&b=${encodeURIComponent(rb)}`);
    const same = c.tests[0] === c.tests[1];
    const n1 = "Test " + c.tests[0] + (same ? " (" + t("run_n") + " 1)" : ""), n2 = "Test " + c.tests[1] + (same ? " (" + t("run_n") + " 2)" : "");
    const pct = (x) => x === null || x === undefined ? "—" : Math.round(x * 100) + "%";
    const row = (k) => { const d = c[k]; return `<tr><td>${t(k === "output1" ? "o1" : "o2")}</td><td>${d.n}</td><td>${pct(d.acc_A)}</td><td>${pct(d.acc_B)}</td><td>${d.only_B_right}</td><td>${d.only_A_right}</td><td>${d.p_value === null ? "—" : d.p_value.toFixed(3)}</td></tr>`; };
    $("compare-out").innerHTML = `<div class="card"><table><tr><th></th><th>${t("cmp_n")}</th><th>${esc(t("cmp_acc", { x: n1 }))}</th><th>${esc(t("cmp_acc", { x: n2 }))}</th><th>${esc(t("cmp_only", { x: n2 }))}</th><th>${esc(t("cmp_only", { x: n1 }))}</th><th>${t("cmp_p")}</th></tr>${row("output1")}${row("output2")}</table>
      <p class="small ${c.same_settings && c.same_shared_prompt ? "" : "msg err"}">${t("cmp_same")}: ${c.same_settings && c.same_shared_prompt ? "✓" : "✗"}</p></div>`;
  } catch (e) { $("compare-out").textContent = t("err") + e.message; }
}

// ---- settings
function openSettings() {
  const a = S.cfg.config.api;
  $("s-model").value = a.model; $("s-effort").value = a.reasoning_effort ?? ""; $("s-temp").value = a.temperature ?? "";
  $("s-detail").value = a.image_detail; $("s-max").value = a.max_output_tokens; $("s-par").value = a.parallel; $("s-save").checked = false;
  $("settings").classList.remove("hidden");
}
async function applySettings() {
  try {
    await setCfg({ "api.model": $("s-model").value.trim(), "api.reasoning_effort": $("s-effort").value.trim(), "api.temperature": $("s-temp").value.trim(),
      "api.image_detail": $("s-detail").value, "api.max_output_tokens": Number($("s-max").value), "api.parallel": Number($("s-par").value), save: $("s-save").checked });
    $("settings").classList.add("hidden"); loadPrompt();
  } catch (e) { alert(e.message); }
}

async function boot() {
  applyStatic();
  S.cfg = await api("/api/config");
  S.test = S.cfg.config.run.test; S.region = S.cfg.config.run.region;
  renderTop();
  for (const b of $("test-seg").querySelectorAll("button")) b.addEventListener("click", async () => { S.test = b.dataset.test; await setCfg({ "run.test": S.test }); loadPrompt(); });
  for (const b of $("mode-seg").querySelectorAll("button")) b.addEventListener("click", () => setCfg({ mock: b.dataset.mock === "1" }));
  $("region").addEventListener("change", async () => { S.region = $("region").value; await setCfg({ "run.region": S.region }); loadItems(); loadPrompt(); });
  $("type-filter").addEventListener("change", renderItems);
  $("ask-a").addEventListener("click", () => askModels(["A"]));
  $("ask-b").addEventListener("click", () => askModels(["B"]));
  $("ask-both").addEventListener("click", () => askModels(["A", "B"]));
  for (const b of document.querySelectorAll(".tab")) b.addEventListener("click", () => {
    for (const x of document.querySelectorAll(".tab")) x.classList.toggle("active", x === b);
    for (const p of ["prompt", "batch", "io"]) $("pane-" + p).classList.toggle("hidden", p !== b.dataset.tab);
    if (b.dataset.tab === "batch") loadRuns();
  });
  $("b-run").addEventListener("click", startRun);
  $("b-compare").addEventListener("click", compareRuns);
  $("settings-btn").addEventListener("click", openSettings);
  $("s-cancel").addEventListener("click", () => $("settings").classList.add("hidden"));
  $("s-ok").addEventListener("click", applySettings);
  $("lang-btn").addEventListener("click", () => { S.lang = S.lang === "zh" ? "en" : "zh"; try { localStorage.setItem(LANG_KEY, S.lang); } catch (e) { /* ignore */ } applyStatic(); renderTop(); renderResults(); renderFilter(); renderItems(); if (S.prompt) loadPrompt(); });
  await loadItems();
  await loadPrompt();
  const p = await api("/api/progress"); if (p.running) pollRun();
}
boot().catch((e) => { document.body.innerHTML = `<div style="padding:30px;color:#ff6b6b">${esc(e.message)}</div>`; });
