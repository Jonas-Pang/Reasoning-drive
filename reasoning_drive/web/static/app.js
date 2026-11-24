// Lane Rule Advisor (/app): analyze a photo, verify the answer, collect feedback, show monitoring. Claude, 2026-11-18.
const $ = (s) => document.querySelector(s);
const ACTIONS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"];
const NAMES = {change_left: "Change lane left", change_right: "Change lane right", go_straight: "Go straight", turn_left: "Turn left",
  turn_right: "Turn right", u_turn: "U-turn", enter_waiting_area: "Enter waiting area / TWLTL"};
const state = {src: "example", mode: "live", info: null, last: null, uploadId: null};
const REGION_NAMES = {US: "United States", CN: "China", UK: "United Kingdom", IN: "India"};

// One id per browser tab: the service keeps a key you typed under it (memory only). Claude, 2026-11-18.
const SID = (() => { const make = () => (crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2) + Date.now()).replace(/-/g, "");
  try { let s = sessionStorage.getItem("rd_sid"); if (!s) { s = make(); sessionStorage.setItem("rd_sid", s); } return s; } catch (e) { return make(); } })();
async function api(path, body) {
  if (!body) path += (path.includes("?") ? "&" : "?") + "session=" + SID;
  const r = await fetch(path, body ? {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({...body, session: SID})} : {});
  const j = await r.json();
  if (!r.ok || j.error) throw new Error(j.error || r.statusText);
  return j;
}
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
function seg(id, cb) {
  document.querySelectorAll(`${id} button`).forEach((b) => b.onclick = () => {
    document.querySelectorAll(`${id} button`).forEach((x) => x.classList.toggle("on", x === b)); cb(b.dataset);
  });
}

// ---------------------------------------------------------------- tabs
document.querySelectorAll("#tabs button").forEach((b) => b.onclick = () => {
  document.querySelectorAll("#tabs button").forEach((x) => x.classList.toggle("on", x === b));
  document.querySelectorAll(".tab").forEach((t) => t.classList.toggle("hidden", t.id !== "tab-" + b.dataset.tab));
  if (b.dataset.tab === "monitor" || b.dataset.tab === "feedback") loadSummary();
  if (b.dataset.tab === "video") fillVideoOptions();
});

// ---------------------------------------------------------------- input
seg("#src-seg", (d) => { state.src = d.src; $("#src-example").classList.toggle("hidden", d.src !== "example");
  $("#src-upload").classList.toggle("hidden", d.src !== "upload");
  if (d.src === "upload" && $("#model").value === "saved") $("#model").value = firstLiveModel(); setMode(); showImage(); });

// Rules: none (Test A), the road's own region (Test B) or another region (Test C). Model: saved answer or a live model.
function rulesOptions(region, sel) {
  const regs = (state.info && state.info.regions) || ["US", "CN", "UK", "IN"];
  const opts = [[region, `${REGION_NAMES[region] || region} rules (Test B)`], ["none", "No rules, photo only (Test A)"],
    ...regs.filter((r) => r !== region).map((r) => [r, `${REGION_NAMES[r] || r} rules on this road (Test C)`])];
  $(sel).innerHTML = opts.map(([v, t]) => `<option value="${v}">${esc(t)}</option>`).join("");
}
function modelOptions(sel, withSaved) {
  const ms = (state.info && state.info.models) || [];
  $(sel).innerHTML = (withSaved ? [`<option value="saved">Saved answer of the frozen test run (offline)</option>`] : []).concat(
    ms.map((m) => `<option value="${m.id}" ${m.key_set ? "" : "disabled"}>${esc(m.label)}${m.key_set ? "" : ` — ${esc(m.key_env || "key")} not set in .env`}</option>`)).join("");
}
function firstLiveModel() { const m = ((state.info && state.info.models) || []).find((x) => x.key_set && !x.mock); return m ? m.id : "mock"; }
function setMode() {
  const m = $("#model").value; state.mode = m === "saved" ? "saved" : "live";
  const info = ((state.info && state.info.models) || []).find((x) => x.id === m);
  $("#mode-hint").textContent = m === "saved"
    ? "Shows the answer the main configuration (gemma4:31b, lane_v4c) gave in the frozen test run: no model call, works offline. Test-set examples only, Test A or B."
    : m === "mock" ? "Made-up answer, no model call: checks the pipeline only."
    : m === "mykey" && info ? `Calls ${info.model} with your key (${info.hint}) now (about 10–60 s).`
    : `Calls ${info ? info.model : "the model"} through ${info ? info.provider : "the API"} now (about 10–60 s).`;
}
$("#model").onchange = setMode;
$("#region").onchange = () => { rulesOptions($("#region").value, "#rules"); loadExamples(); };
$("#example").onchange = showImage;
$("#file").onchange = async () => {
  const f = $("#file").files[0]; if (!f) return;
  const data = await new Promise((ok) => { const r = new FileReader(); r.onload = () => ok(r.result); r.readAsDataURL(f); });
  $("#msg").textContent = "Checking the photo…";
  try {
    const u = await api("/api/upload", {data, region: $("#region").value, name: f.name});
    state.uploadId = u.image_id; $("#msg").textContent = ""; showImage();
  } catch (e) { $("#msg").textContent = "✗ " + e.message; state.uploadId = null; }
};
async function loadExamples() {
  const ex = await api("/api/app/examples?region=" + $("#region").value).catch(() => []);
  $("#example").innerHTML = ex.map((e, i) => `<option value="${e.image_id}">#${i + 1} · ${esc(e.dataset)} · ${esc(e.image_id.split("__").pop())}</option>`).join("");
  $("#ex-count").textContent = ex.length ? `${ex.length} test photos with a saved answer of the main configuration` : "No labeled photos for this region on this machine — upload one.";
  showImage();
}
function currentId() { return state.src === "upload" ? state.uploadId : $("#example").value; }
function showImage() {
  const id = currentId();
  $("#img").src = id ? `/api/image?task=lane&w=900&id=${encodeURIComponent(id)}` : "";
}

// ---------------------------------------------------------------- analyze
$("#go").onclick = async () => {
  const id = currentId();
  if (!id) { $("#msg").textContent = "Choose or upload a photo first."; return; }
  $("#go").disabled = true; $("#msg").textContent = state.mode === "live" ? "Asking the model…" : "Loading the saved answer…";
  const t0 = performance.now();
  try {
    const rules = $("#rules").value;
    if (state.mode === "saved" && rules !== "none" && rules !== $("#region").value) throw new Error("Saved answers exist for Test A and Test B only; choose a live model for Test C.");
    const r = await api("/api/app/predict", {image_id: id, test: rules === "none" ? "A" : "B", rules, mode: state.mode, model: $("#model").value});
    state.last = r; render(r, (performance.now() - t0) / 1000); buildFeedback(r); $("#msg").textContent = "";
  } catch (e) { $("#msg").textContent = "✗ " + e.message; }
  $("#go").disabled = false;
};

function lineCard(side, b) {
  b = b || {};
  const style = `${esc(b.color || "?")} ${esc(String(b.pattern || "?").replaceAll("_", "-"))}`;
  return `<div class="line"><div class="lh">${side} line</div><div class="lv">${style}</div>
    <div class="lm">${esc(String(b.role || "").replaceAll("_", " "))}${b.curb === "yes" ? " · curb" : ""} · visible: ${esc(b.evidence || "?")}</div></div>`;
}
function render(r, secs) {
  const a = r.answer || {}, c = r.check || {}, rc = c.rule_check || {};
  const ok = !c.needs_review;
  const agree = rc.agreement == null ? "n/a" : `${rc.agree}/${rc.checked}`;
  const acts = a.actions || {};
  const lab = r.label_actions;
  const chips = ACTIONS.map((k) => {
    const v = acts[k] || "—"; const cls = v === "allowed" ? "ok" : v === "prohibited" ? "no" : v === "stop_first" ? "warn" : "na";
    const dis = (rc.disagreements || []).find((d) => d.action === k);
    const l = lab ? (lab[k] === v ? `<span class="lab good" title="label: ${esc(lab[k])}">✓ label</span>` : `<span class="lab bad" title="label: ${esc(lab[k])}">✗ label: ${esc(lab[k])}</span>`) : "";
    return `<div class="act ${cls}"><div class="an">${NAMES[k]}</div><div class="av">${esc(v.replace("_", " "))}</div>
      ${dis ? `<div class="ad">rule table: ${esc(dis.rules)}</div>` : ""}${l}</div>`;
  }).join("");
  const rules = (a.element_rules || []).filter((e) => e && e.rule_id).map((e) => {
    const p = (r.passages || {})[e.rule_id] || {};
    return `<li><b>${esc(e.rule_id)}</b> — ${esc(e.meaning || "")}${p.text_en ? `<div class="quote">${esc(p.text_en.slice(0, 260))}${p.text_en.length > 260 ? "…" : ""}</div>` : ""}</li>`;
  }).join("");
  $("#out").innerHTML = `
    <div class="verdict ${ok ? "pass" : "review"}">
      <div class="vt">${ok ? "✔ Verified" : "⚠ Needs human review"}</div>
      <div class="vd">Rule check: model and rule table agree on <b>${agree}</b> decided actions${rc.agreement != null ? ` (${Math.round(rc.agreement * 100)} %)` : ""}.
        ${(c.reasons || []).length ? "<br>" + c.reasons.map(esc).join("<br>") : ""}</div>
    </div>
    <h3>What the model sees</h3>
    <div class="scene">${esc(a.scene || "")}</div>
    <div class="lines">${lineCard("Left", a.left_boundary)}${lineCard("Right", a.right_boundary)}</div>
    ${(a.lane_markings || []).length ? `<div class="hint">Markings in my lane: ${a.lane_markings.map((m) => esc(m.marking || m)).join(", ")}</div>` : ""}
    <h3>What my car may do</h3>
    <div class="acts">${chips}</div>
    ${a.advice ? `<div class="advice">💬 ${esc(a.advice)}</div>` : ""}
    ${rules ? `<details open><summary>Rules cited</summary><ul class="rules">${rules}</ul></details>` : ""}
    <div class="meta">request ${esc(r.request_id)} · road ${esc(r.region)} · Test ${esc(r.test)}${r.rules && r.rules !== r.region ? ` (rules of ${esc(r.rules)})` : ""} · ${esc(r.model || "")}${r.cached ? " · from cache" : ""}
      ${r.from_run ? ` · saved answer from run ${esc(r.from_run.run_id)} (${esc(r.from_run.prompt)})` : ` · ${secs.toFixed(1)} s`}
      ${r.error ? `<br>error: ${esc(r.error)}` : ""}</div>
    <div class="row"><span class="grow"></span><button class="primary" onclick="document.querySelector('[data-tab=feedback]').click()">Give feedback →</button></div>`;
}

// ---------------------------------------------------------------- feedback
function verdictSeg(name, label, extra) {
  return `<div class="fb-row"><span>${label}${extra ? `<small>${extra}</small>` : ""}</span><div class="seg" data-name="${name}">
    <button type="button" data-v="right">Right</button><button type="button" data-v="wrong">Wrong</button><button type="button" data-v="unsure">Unsure</button></div></div>`;
}
function buildFeedback(r) {
  const a = r.answer || {};
  $("#fb-target").innerHTML = `About request <b>${esc(r.request_id)}</b> · ${esc(r.region)} · Test ${esc(r.test)} · ${esc(r.image_id)}`;
  $("#fb-lines").innerHTML = ["left", "right"].map((s) => { const b = a[s + "_boundary"] || {};
    return verdictSeg("line_" + s, s[0].toUpperCase() + s.slice(1) + " line", `${b.color || "?"} ${String(b.pattern || "?").replaceAll("_", "-")}`); }).join("");
  $("#fb-actions").innerHTML = ACTIONS.map((k) => verdictSeg("act_" + k, NAMES[k], ((a.actions || {})[k] || "").replace("_", " "))).join("");
  $("#fb-form").classList.remove("hidden");
  document.querySelectorAll("#fb-form .seg").forEach((s) => s.querySelectorAll("button").forEach((b) => b.onclick = () => {
    const was = b.classList.contains("on"); s.querySelectorAll("button").forEach((x) => x.classList.remove("on")); if (!was) b.classList.add("on"); }));
  $("#fb-msg").textContent = "";
}
const pick = (name) => { const b = document.querySelector(`#fb-form .seg[data-name="${name}"] button.on`); return b ? b.dataset.v : ""; };
$("#fb-clear").onclick = () => { document.querySelectorAll("#fb-form .seg button").forEach((x) => x.classList.remove("on")); $("#fb-comment").value = ""; };
$("#fb-form").onsubmit = async (ev) => {
  ev.preventDefault();
  if (!state.last) return;
  const body = {request_id: state.last.request_id, rating: pick("rating"), comment: $("#fb-comment").value,
    lines: {left: pick("line_left"), right: pick("line_right")}, actions: Object.fromEntries(ACTIONS.map((k) => [k, pick("act_" + k)]))};
  try {
    const r = await api("/api/feedback", body);
    $("#fb-msg").textContent = "✔ Thank you — saved" + (r.themes ? ` (themes: ${r.themes.replaceAll(";", ", ")})` : "") + ".";
    loadSummary();
  } catch (e) { $("#fb-msg").textContent = "✗ " + e.message; }
};

// ---------------------------------------------------------------- monitor
async function loadSummary() {
  const s = await api("/api/app/summary").catch(() => null); if (!s) return;
  const pct = (x) => x == null ? "—" : Math.round(x * 100) + " %";
  const bad = (s.ratings.bad || 0), rated = bad + (s.ratings.good || 0);
  $("#kpis").innerHTML = [
    ["Answers given", s.predictions], ["Needs review", s.predictions ? `${s.needs_review} (${pct(s.needs_review / s.predictions)})` : "—"],
    ["Mean rule agreement", s.rule_agreement_mean == null ? "—" : s.rule_agreement_mean.toFixed(2)],
    ["Latency p50 / p90", s.latency_p50 == null ? "—" : `${s.latency_p50.toFixed(1)} / ${s.latency_p90.toFixed(1)} s`],
    [`Feedback<br><small>${Object.entries(s.feedback_by_source).map(([k, v]) => `${v} ${k.replaceAll("_", " ")}`).join(" · ")}</small>`, s.feedback],
    ["Rated bad", rated ? `${bad} / ${rated} (${pct(bad / rated)})` : "—"],
  ].map(([k, v]) => `<div class="kpi"><div class="kv">${v}</div><div class="kk">${k}</div></div>`).join("");
  $("#bars").innerHTML = ACTIONS.map((k) => { const w = s.action_wrong_rate[k]; const c = s.per_action[k] || {};
    return `<div class="bar"><span class="bl">${NAMES[k]}</span><span class="bt"><span style="width:${(w || 0) * 100}%"></span></span>
      <span class="bv">${w == null ? "—" : pct(w)} <small>(${(c.wrong || 0)}/${(c.right || 0) + (c.wrong || 0)})</small></span></div>`; }).join("");
  $("#themes").innerHTML = s.themes.length ? s.themes.map(([t, n]) => `<span class="tag">${esc(t.replaceAll("_", " "))} <b>${n}</b></span>`).join(" ") : "<span class='hint'>no comments yet</span>";
  $("#fb-recent").innerHTML = s.recent_comments.length ? s.recent_comments.map((c) => `<div class="cm"><span class="pill ${c.rating}">${esc(c.rating || "–")}</span> <b>${esc(c.region)}</b> ${esc(c.comment)}</div>`).join("") : "—";
  if (state.info) { $("#lnk-grafana").href = state.info.grafana; $("#lnk-prom").href = state.info.prometheus; }
}

// ---------------------------------------------------------------- start
(async () => {
  try {
    state.info = await api("/api/app/info");
    const keys = (state.info.models || []).filter((m) => !m.mock).map((m) => `${m.id}: ${m.key_set ? "key set" : "no key"}`).join(" · ");
    $("#model-pill").textContent = `${String(state.info.prompt || "").replace("prompts/", "")} · ${keys}`;
  } catch (e) { $("#model-pill").textContent = "service not reachable"; }
  rulesOptions($("#region").value, "#rules"); modelOptions("#model", true);
  $("#model").value = "saved"; setMode();
  await loadExamples();
})();

// ---------------------------------------------------------------- video (Claude 2026-11-18)
const vstate = {videoId: null, job: null, sel: null, timer: null, events: ""};
function fillVideoOptions() {
  if (!$("#v-model").options.length) { modelOptions("#v-model", false); $("#v-model").value = firstLiveModel(); }
  if (!$("#v-rules").options.length) rulesOptions($("#v-region").value, "#v-rules");
  if ($("#v-intent").options.length < 2) $("#v-intent").innerHTML += ACTIONS.map((k) => `<option value="${k}">${NAMES[k]}</option>`).join("");
}
$("#v-region").onchange = () => rulesOptions($("#v-region").value, "#v-rules");
$("#v-file").onchange = async () => {
  const f = $("#v-file").files[0]; if (!f) return;
  $("#v-go").disabled = true; vstate.videoId = null;
  $("#v-player").src = URL.createObjectURL(f); $("#v-player").classList.remove("hidden");
  $("#v-info").textContent = `Uploading ${f.name} (${(f.size / 1e6).toFixed(1)} MB)…`;
  try {
    const r = await fetch("/api/app/video/upload?name=" + encodeURIComponent(f.name), {method: "POST", headers: {"Content-Type": "application/octet-stream"}, body: f});
    const j = await r.json(); if (!r.ok || j.error) throw new Error(j.error || r.statusText);
    vstate.videoId = j.video_id;
    $("#v-info").textContent = `✔ ${j.duration_s} s · ${j.width}×${j.height} · ${j.fps} fps`;
    $("#v-go").disabled = false;
  } catch (e) { $("#v-info").textContent = "✗ " + e.message; }
};
$("#v-events").onchange = async () => { const f = $("#v-events").files[0]; vstate.events = f ? await f.text() : ""; };
$("#v-go").onclick = async () => {
  if (!vstate.videoId) { $("#v-msg").textContent = "Upload a video first."; return; }
  $("#v-go").disabled = true; $("#v-msg").textContent = "Taking frames…"; $("#v-prog").classList.remove("hidden");
  try {
    const j = await api("/api/app/video/start", {video_id: vstate.videoId, region: $("#v-region").value, rules: $("#v-rules").value,
      model: $("#v-model").value, intent: $("#v-intent").value, events: vstate.events,
      every: parseFloat($("#v-every").value) || 1, max_frames: parseInt($("#v-max").value) || 20});
    vstate.jobId = j.job_id;   // the video stays on the server: change rules or model and press Analyze again
    pollVideo(j.job_id);
  } catch (e) { $("#v-msg").textContent = "✗ " + e.message; $("#v-go").disabled = false; }
};
async function pollVideo(id) {
  clearTimeout(vstate.timer);
  const j = await api("/api/app/video/status?job=" + id).catch((e) => ({state: "error", error: e.message}));
  const pct = j.total ? Math.round(100 * j.done / j.total) : 3;
  $("#v-prog span").style.width = pct + "%";
  $("#v-msg").textContent = j.state === "analysing" ? `Analysing frame ${j.done} / ${j.total}…` : j.state === "sampling" ? "Taking frames…"
    : j.state === "rendering" ? `Drawing the annotated video… ${j.render_pct || 0} %` : j.state === "error" ? "✗ " + j.error : "";
  if (j.state === "done") { vstate.job = j; renderVideo(j); $("#v-prog").classList.add("hidden"); $("#v-go").disabled = false; return; }
  if (j.state === "error") { $("#v-prog").classList.add("hidden"); return; }
  vstate.timer = setTimeout(() => pollVideo(id), 1500);
}
const CHANGE = ["change_left", "change_right"];
function segClass(s) {
  const v = CHANGE.map((k) => s.actions[k]);
  if (v.every((x) => x === "prohibited")) return "no";
  if (v.every((x) => x === "allowed")) return "ok";
  if (v.every((x) => !x || x === "not_applicable")) return "na";
  return "mix";
}
const fmtS = (t) => `${Number(t).toFixed(1)} s`;
function renderVideo(j) {
  const dur = j.video.duration_s;
  const tl = j.segments.map((s, i) => `<div class="sg ${segClass(s)}" data-i="${i}" style="flex:${Math.max(0.02, (s.end_s - s.start_s) / dur)}"
      title="${fmtS(s.start_s)}–${fmtS(s.end_s)}: left ${esc(s.left)}, right ${esc(s.right)}">${esc(s.left.split(" ")[1] || "")} | ${esc(s.right.split(" ")[1] || "")}</div>`).join("");
  let banner = "";
  if (j.intent_check) {
    const ic = j.intent_check;
    const words = {violation: "✗ Not allowed here", ok: "✔ Allowed", conditional: "⚠ Allowed only after stopping / yielding", not_governed: "– Not governed by the markings"};
    banner = `<div class="banner ${ic.verdict}"><b>Navigation intent: ${NAMES[ic.action]}</b> at ${fmtS(ic.at_s)} → ${words[ic.verdict]}
      (${esc(ic.value || "no answer")}).${ic.reason ? `<br><small>${esc(ic.reason)}</small>` : ""}</div>`;
  }
  const evs = j.event_checks.length ? `<h3>Executed manoeuvres</h3><table class="ev"><tr><th>Time</th><th>Manoeuvre</th><th>Perception says</th><th>Ground truth</th><th>Verdict / fault</th></tr>
    ${j.event_checks.map((e) => `<tr><td>${fmtS(e.t)}</td><td>${NAMES[e.action]}${e.note ? `<br><small>${esc(e.note)}</small>` : ""}</td>
      <td><a href="#" data-f="${e.frame}">${esc(e.value || "—")}</a> <small>(frame at ${e.evidence_t == null ? "—" : fmtS(e.evidence_t)})</small></td>
      <td>${esc(e.truth || "—")}</td><td><b>${esc(e.verdict.replace("_", " "))}</b>${e.attribution ? `<br>${esc(e.attribution.replaceAll("_", " "))}: <small>${esc(e.explanation)}</small>` : ""}</td></tr>`).join("")}</table>` : "";
  const strip = j.frames.map((f) => `<div class="fr ${f.kind === "evidence" ? "ev" : ""}" data-f="${f.n}">
      <img src="/api/image?task=lane&w=240&id=${encodeURIComponent(f.image_id)}">${fmtS(f.t)}${f.kind === "evidence" ? " · event" : ""}${f.error ? " ⚠" : ""}</div>`).join("");
  const out = j.outputs, fileUrl = (n, dl) => `/api/app/video/file?job=${j.job_id}&name=${encodeURIComponent(n)}${dl ? "&download=1" : ""}`;
  const player = out ? `<h3>Annotated video <small class="small">(${esc(out.codec)}; red frame = problem on screen)</small></h3>
    <video id="v-anno" controls preload="metadata" src="${fileUrl(out.annotated)}"></video>
    <div class="clips"><button type="button" class="on" data-src="${out.annotated}">Whole clip</button>
      ${out.problems.map((p) => `<button type="button" class="bad" data-src="${p.file}" title="${esc(p.label)}">▶ Problem ${p.k}: ${NAMES[p.action]} (${fmtS(p.start_s)}–${fmtS(p.end_s)})</button>`).join("")}</div>
    <div class="vrow small">${out.problems.length ? `${out.problems.length} problem clip(s) · ` : "No problem found · "}
      <a href="${fileUrl(out.annotated, 1)}">download annotated video</a>
      ${out.problems.map((p) => ` · <a href="${fileUrl(p.file, 1)}">problem ${p.k}</a>`).join("")}
      · <a href="#" id="v-del">delete this video and its results</a></div>`
    : `<div class="hint">${j.render_error ? "Annotated video not made: " + esc(j.render_error) : ""}</div>`;
  $("#v-out").innerHTML = `${banner}${player}
    <h3>Lane along the clip <small class="small">(green: both lane changes allowed · red: both prohibited · orange: one side only · grey: not governed)</small></h3>
    <div class="timeline">${tl}</div><div class="tl-axis"><span>0 s</span><span>${fmtS(dur)}</span></div>
    ${evs}
    <h3>Frames <small class="small">${j.frames.length} analysed · ${j.sampling ? j.sampling.skipped_repeats_or_thinned : 0} repeats skipped · Test ${esc(j.test)}${j.rules && j.rules !== j.region ? ` (rules of ${esc(j.rules)})` : ""} · ${esc(j.model)} · ${j.seconds} s</small></h3>
    <div class="frames">${strip}</div>
    <div id="v-detail"></div>`;
  document.querySelectorAll("#v-out .sg").forEach((d) => d.onclick = () => { const s = j.segments[+d.dataset.i]; showFrame(s.frames[s.frames.length - 1], +d.dataset.i); seekAnno(s.start_s); });
  document.querySelectorAll("#v-out .clips button").forEach((b) => b.onclick = () => {
    document.querySelectorAll("#v-out .clips button").forEach((x) => x.classList.toggle("on", x === b));
    const v = $("#v-anno"); v.src = fileUrl(b.dataset.src); v.play().catch(() => {}); });
  const del = $("#v-del"); if (del) del.onclick = async (ev) => { ev.preventDefault();
    if (!confirm("Delete the uploaded video, its frames and the annotated videos from this computer?")) return;
    try { await api("/api/app/video/delete", {job_id: j.job_id}); $("#v-out").innerHTML = `<div class="empty">Deleted.</div>`;
      vstate.videoId = null; vstate.job = null; $("#v-go").disabled = true; $("#v-info").textContent = "Deleted — upload a video to start again."; }
    catch (e) { $("#v-msg").textContent = "✗ " + e.message; } };
  document.querySelectorAll("#v-out [data-f]").forEach((d) => d.onclick = (ev) => { ev.preventDefault(); showFrame(+d.dataset.f); seekAnno(j.frames[+d.dataset.f].t); });
  const last = j.segments.length ? j.segments[j.segments.length - 1] : null;
  if (j.event_checks.length && j.event_checks[0].frame != null) showFrame(j.event_checks[0].frame); else if (last) showFrame(last.frames[last.frames.length - 1], j.segments.length - 1);
}
function seekAnno(t) { const v = $("#v-anno"); if (!v) return;
  const on = document.querySelector("#v-out .clips button.on"); if (on && on.dataset.src !== vstate.job.outputs.annotated) document.querySelector("#v-out .clips button").click();
  setTimeout(() => { try { v.currentTime = t; } catch (e) {} }, 150); }
function showFrame(n, segIdx) {
  const j = vstate.job, f = j.frames[n]; if (!f) return;
  document.querySelectorAll("#v-out .fr").forEach((d) => d.classList.toggle("sel", +d.dataset.f === n));
  document.querySelectorAll("#v-out .sg").forEach((d) => d.classList.toggle("sel", segIdx != null && +d.dataset.i === segIdx));
  const r = {request_id: f.request_id, region: j.region, test: j.test, rules: j.rules, image_id: f.image_id, model: j.model,
    answer: f.answer || {}, check: f.check || {}, passages: f.passages || {}, error: f.error, cached: f.cached};
  const tmp = document.createElement("div"); const keep = $("#out").innerHTML;
  render(r, f.latency_s || 0); tmp.innerHTML = $("#out").innerHTML; $("#out").innerHTML = keep;
  $("#v-detail").innerHTML = `<h3>Frame at ${fmtS(f.t)}${f.kind === "evidence" ? " (evidence frame of an event)" : ""}</h3>
    <div class="imgbox"><img src="/api/image?task=lane&w=900&id=${encodeURIComponent(f.image_id)}"></div>` + tmp.innerHTML;
  const b = $("#v-detail button.primary"); if (b) b.onclick = () => { state.last = r; buildFeedback(r); document.querySelector("[data-tab=feedback]").click(); };
}

// ---------------------------------------------------------------- your API key (Claude 2026-11-18)
function keyDefaults() {
  const p = $("#k-provider").value, ms = (state.info && state.info.models) || [];
  const m = ms.find((x) => x.id === p);
  $("#k-base").value = p === "custom" ? "https://" : (m && m.base_url) || (p === "openai" ? "https://api.openai.com/v1" : "https://api.navigator.ai.ufl.edu/v1");
  $("#k-model").value = p === "custom" ? "" : (m && m.model) || "";
}
$("#k-provider").onchange = keyDefaults;
const keyBody = () => ({provider: $("#k-provider").value, base_url: $("#k-base").value.trim(), model: $("#k-model").value.trim(), key: $("#k-key").value.trim()});
$("#k-check").onclick = async () => {
  $("#k-msg").textContent = "Checking…";
  try { const r = await api("/api/app/userkey/check", keyBody()); $("#k-msg").textContent = (r.ok ? "✔ " : "✗ ") + r.message; }
  catch (e) { $("#k-msg").textContent = "✗ " + e.message; }
};
async function refreshModels(select) {
  state.info = await api("/api/app/info");
  const a = $("#model").value, v = $("#v-model").value;
  modelOptions("#model", true); modelOptions("#v-model", false);
  const has = (state.info.models || []).some((m) => m.id === "mykey");
  $("#model").value = select && has ? "mykey" : ([...$("#model").options].some((o) => o.value === a) ? a : "saved");
  $("#v-model").value = select && has ? "mykey" : ([...$("#v-model").options].some((o) => o.value === v) ? v : firstLiveModel());
  setMode();
}
function showKeyState(k) {
  const on = k && k.model;
  $("#k-state").classList.toggle("hidden", !on); $("#k-forget").classList.toggle("hidden", !on);
  if (on) $("#k-state").innerHTML = `✔ Your key <b>${esc(k.hint)}</b> is in use: <b>${esc(k.model)}</b> via ${esc(k.base_url)} (${esc(k.provider_label)}), set at ${esc(k.set_utc)}.<br>
    Choose “Your key · ${esc(k.model)}” on Analyze or Video (already selected).`;
}
$("#k-use").onclick = async () => {
  $("#k-msg").textContent = "Saving in memory…";
  try { const k = await api("/api/app/userkey", keyBody()); $("#k-key").value = ""; $("#k-msg").textContent = "";
    showKeyState(k); await refreshModels(true); }
  catch (e) { $("#k-msg").textContent = "✗ " + e.message; }
};
$("#k-forget").onclick = async () => {
  await api("/api/app/userkey/clear", {}).catch(() => {}); showKeyState(null); $("#k-msg").textContent = "Forgotten."; await refreshModels(false);
};
(async () => { for (let i = 0; i < 20 && !state.info; i++) await new Promise((ok) => setTimeout(ok, 150));
  keyDefaults(); showKeyState(await api("/api/app/userkey").catch(() => null)); })();
