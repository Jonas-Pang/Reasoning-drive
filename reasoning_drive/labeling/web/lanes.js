/* Lane labeling page. Works with a local server (the owner: inside tabs ② and ③ of the main labeling tool, or on its
   own with python main.py label lanes) or offline from a package (helpers). Server addresses are relative ("api/..."), so the
   page works both at / and at /lanes/. URL parameters: embedded=1 (inside the main tool), lang, filter, id.
   The form records the fields of configs/schemas/lane_schema.json; colour and pattern are offered together as one line type,
   the role, the actions and the rule IDs are filled in as the label grows and can be changed. */
(function () {
  "use strict";
  const PKG = window.LANE_TASK_PACKAGE || null;
  const URLP = new URLSearchParams(PKG ? "" : location.search);
  const EMBED = URLP.get("embedded") === "1" && window.parent !== window;
  const SIDES = ["left", "right"];
  const ACTIONS = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"];
  const MOVES = ["go_straight", "turn_left", "turn_right", "u_turn"];
  // the usual painted lines, colour and pattern in one click ("other colour or pattern" opens the full choice)
  const LINE_TYPES = [["white", "dashed"], ["white", "solid"], ["white", "solid_dashed"], ["white", "double_solid"],
    ["yellow", "solid"], ["yellow", "dashed"], ["yellow", "double_solid"], ["yellow", "solid_dashed"], ["none", "none"]];
  const COMMON_TOKENS = ["arrow:straight", "arrow:left", "arrow:right", "arrow:straight_left", "arrow:straight_right", "arrow:u_turn",
    "arrow:left_u_turn", "text:only", "area:left_turn_waiting", "line:stop_line", "line:crosswalk"];
  const T = {
    en: {
      title: "Lane labeling", f_todo: "To do", f_all: "All", f_conflict: "Disagreements", f_done: "Final", export: "Export results",
      remove: "Remove image", confirm_remove: "Remove this image and every lane label of it from the set? You can pick it again later.",
      guide_title: "How to label (read once)", hide_lines: "Hide lines (H)", show_lines: "Show lines (H)", loupe: "Magnifier",
      draw: "Draw (optional):", draw_left: "Left line", draw_right: "Right line", draw_stop: "Stop", clear_lines: "Clear",
      scene: "1. Where my lane is", lane_count: "Lanes of my direction", ego_index: "My lane (1 = leftmost)", cant_count: "can't tell",
      sides: "2. Both boundaries of my lane", left: "Left boundary", right: "Right boundary", line: "Line", more_types: "other colour or pattern",
      colour: "Colour", pattern: "Pattern", near_line: "Line on my side", curb: "a curb forms this side", role: "Role", evidence: "Can you see it?",
      markings: "3. Markings in my lane (up to its stop line or end)", no_markings: "Nothing ticked: nothing is painted in my lane.",
      more_markings: "All markings (words, symbols, areas, prohibitions, more arrows)",
      actions: "4. What it means for my car", acts_help: "Filled in from the rule table as you label; click to change. A changed value stays.",
      reset_acts: "Back to the rule table", rules: "Rule passages", add_rule: "+ add a passage", auto: "auto", changed: "changed",
      unsure: "I am not sure (the owner will decide)", comment: "Comment", save_draft: "Save draft", save_done: "Done, next image",
      saved: "Saved.", not_saved: "Not saved as done:", warn: "Check:", sug_from: "Suggestion from",
      sug_applied: "Prefilled from the dataset's lane labels; check every value.", contested: "contested",
      look_first: "Count the lanes of my direction first and click my lane (or \"can't tell\"): that is how a label is checked against the photo.",
      none_left: "Nothing left in this view. Choose another view at the top right, or pick or keep more images.",
      adj_title: "The annotations disagree. Choose the final label:", take: "Take", exclude: "Exclude image", note: "Reason",
      exported: "Results file downloaded. Send it back.", status: "status", keys: "← → image · H lines · Ctrl/⌘+Enter done",
    },
    zh: {
      title: "车道标注", f_todo: "待标注", f_all: "全部", f_conflict: "有分歧", f_done: "已定稿", export: "导出结果",
      remove: "删除此图", confirm_remove: "从图片集中删除这张图和它的所有车道标注？之后可以重新挑选。",
      guide_title: "标注说明（请先读一遍）", hide_lines: "隐藏画线 (H)", show_lines: "显示画线 (H)", loupe: "放大镜",
      draw: "画线（可选）：", draw_left: "左边界", draw_right: "右边界", draw_stop: "停止", clear_lines: "清除",
      scene: "1. 本车道在哪", lane_count: "同向车道数", ego_index: "本车道是第几条（从左数）", cant_count: "数不清",
      sides: "2. 本车道两侧边界", left: "左边界", right: "右边界", line: "线", more_types: "其他颜色或线型",
      colour: "颜色", pattern: "线型", near_line: "靠我这侧的是", curb: "这一侧是路缘（马路牙子）", role: "作用", evidence: "看得清吗",
      markings: "3. 本车道内的标线（到停止线或车道尽头）", no_markings: "没有勾选：本车道内没有标线。",
      more_markings: "全部标线（文字、图形、区域、禁止标记、更多箭头）",
      actions: "4. 对本车意味着什么", acts_help: "按规则表随填随算；点一下可以改，改过的值不会再被自动覆盖。",
      reset_acts: "恢复规则表建议", rules: "依据条文", add_rule: "+ 添加条文", auto: "自动", changed: "已改",
      unsure: "我不确定（由负责人裁决）", comment: "备注", save_draft: "保存草稿", save_done: "完成，下一张",
      saved: "已保存。", not_saved: "不能标为完成：", warn: "请检查：", sug_from: "建议来源",
      sug_applied: "已按数据集标注预填，请逐项核对。", contested: "有争议的格子",
      look_first: "先数同向车道数并点出本车道（数不清就点“数不清”），确认看过这张图再完成。",
      none_left: "当前筛选下没有图片了。可以在右上角换一个筛选，或者先去挑选 / 保存更多图片。",
      adj_title: "两位标注者不一致，请选择最终标签：", take: "采用", exclude: "排除此图", note: "理由",
      exported: "结果文件已下载，请发回。", status: "状态", keys: "← → 换图 · H 画线 · Ctrl/⌘+Enter 完成",
    },
  };
  const V = {
    zh: {
      white: "白色", yellow: "黄色", other: "其他", none: "无", solid: "实线", dashed: "虚线", dotted: "短虚线/密虚线", double_solid: "双实线",
      double_dashed: "双虚线", solid_dashed: "虚实线", not_applicable: "不涉及", yes: "有", no: "无", lane_line: "同向分界",
      center_line: "中心线（对向分界）", edge_line: "道路边缘", special_lane_line: "专用车道（公交/多乘员/潮汐/可变）", unknown: "不确定",
      full: "清楚", partial: "部分看清", insufficient: "看不清", allowed: "允许", stop_first: "先停车再走", prohibited: "禁止", not_determined: "无法判断",
      change_left: "向左越线/变道", change_right: "向右越线/变道", go_straight: "直行", turn_left: "左转", turn_right: "右转", u_turn: "掉头",
      enter_waiting_area: "进入待转区/双向左转车道",
      "arrow:straight": "直行箭头", "arrow:left": "左转箭头", "arrow:right": "右转箭头", "arrow:straight_left": "直行或左转", "arrow:straight_right": "直行或右转",
      "arrow:left_right": "左右转", "arrow:u_turn": "掉头", "arrow:left_u_turn": "左转或掉头", "arrow:straight_u_turn": "直行或掉头",
      "arrow:merge_left": "向左合流", "arrow:merge_right": "向右合流", "arrow:two_way_left": "双向左转车道箭头（本车在其中）",
      "no_turn:u_turn": "禁止掉头标记", "no_turn:left": "禁止左转标记", "no_turn:right": "禁止右转标记", "text:only": "ONLY 字样", "text:bus": "公交 / BUS",
      "text:hov": "多乘员 / HOV", "text:stop": "STOP / 停", "text:keep_clear": "KEEP CLEAR / 勿停", "text:speed_limit": "限速数字", "text:other": "其他文字",
      "symbol:hov_diamond": "菱形（HOV）", "symbol:bike": "自行车/非机动车图形", "symbol:other": "其他图形", "area:left_turn_waiting": "左弯待转区",
      "area:two_way_left_turn_lane": "左侧是双向左转车道", "area:grid": "网状线/禁停区", "area:channelizing": "导流线/斜纹区",
      "line:stop_line": "停止线", "line:yield_line": "让行线", "line:stop_yield": "停车让行线（停）", "line:crosswalk": "人行横道",
      arrow: "箭头", no_turn: "禁止", text: "文字", symbol: "图形", area: "区域", line: "横线",
    },
    en: { arrow: "Arrows", no_turn: "Prohibited", text: "Words", symbol: "Symbols", area: "Areas", line: "Across the lane",
      full: "clear", partial: "partly", insufficient: "can't see" },
  };
  const GUIDE = {
    en: `<p>Label <b>my lane</b>: the lane straight ahead of the car that took the photo. Left and right are as seen from that car. Hover the photo for the magnifier; H hides the drawn lines so the paint is not covered.</p>
<ol><li>Where my lane is: count the lanes of my direction near the bottom of the photo and click which one is mine; "can't tell" if you cannot count.</li>
<li>Each boundary: click the line as painted. A solid line next to a broken one is "solid + dashed"; then say which line is on my side. Tick the curb box if a curb forms that side. The role is suggested from the line and the lane position; change it if it is wrong. Judge colour and pattern from the paint you can see, never from where the line is.</li>
<li>Markings: tick everything painted in my lane up to its stop line or end (read an arrow from its head). The usual ones are shown; "All markings" has the rest. Nothing ticked means nothing is painted.</li>
<li>The actions and rule passages fill themselves from the rule table. Check each one: a boundary decides only the lane change on its side, arrows decide the four movements. <i>not applicable</i> = nothing in view governs it; <i>not determined</i> = the deciding feature is hidden. Without an arrow, going straight is <i>not applicable</i> too, like the turns: the road lets you drive on, but no marking says so (a straight arrow means straight only). Keep the suggested passages unless one you read says otherwise.</li>
<li>"Can you see it?" starts at clear; change it where the paint is worn, hidden or too dark. Tick unsure rather than guess.</li></ol>`,
    zh: `<p>标注<b>本车道</b>：拍摄车辆正前方所在的车道。左右以拍摄车辆为准。鼠标放在图上会出现放大镜；按 H 隐藏画线，看清油漆本身。</p>
<ol><li>本车道在哪：在画面底部数同向车道数，点出本车道是第几条；数不清就点“数不清”。</li>
<li>每一侧边界：点画着的那种线。实线和虚线并排时选“虚实线”，再说明靠本车道一侧是实线还是虚线。由路缘构成就勾上路缘。作用会按线和车道位置自动建议，不对就改。颜色和线型只看能看到的油漆，不要根据位置推测。</li>
<li>车道内标线：勾选本车道内（到停止线或车道尽头）画着的所有标线，箭头看箭头头部。常用的直接列出，其余在“全部标线”里。一个都不勾 = 车道内没有标线。</li>
<li>动作和依据条文按规则表自动填好，逐项检查：边界只决定该侧变道；箭头决定四个行驶方向。“不涉及”= 画面中没有标线管这个动作；“无法判断”= 决定它的特征看不清。没有箭头时，直行选“允许”（沿本车道往前开没有标线限制；两侧实线只管变道），左转、右转、掉头选“不涉及”；本车道到头要并线或是双向左转车道时除外。车道里有 STOP 字样或带“停”字的停车让行线时，允许的方向都改成“先停车再走”。边界作用是“专用车道线”时：本车是普通车、看不到专用时段，所以朝公交/多乘员/潮汐车道变道选“禁止”；本车就在专用车道里（车道内有公交/多乘员字样）时，离开按线型判断。除非你读到的条文另有规定，保留建议的条文。</li>
<li>“看得清吗”默认是清楚；油漆磨损、被挡住或太暗的地方改一下。拿不准时勾选“不确定”，不要猜。</li></ol>`,
  };
  let lang = "en";
  try { lang = localStorage.getItem("lane_lang") || (navigator.language || "").startsWith("zh") && "zh" || "en"; } catch (e) { /* storage blocked */ }
  if (["en", "zh"].includes(URLP.get("lang"))) lang = URLP.get("lang");
  const S = { items: [], idx: 0, item: null, fields: {}, schema: null, rules: null, passages: {}, img: null, drawing: "", sug: {}, extra: null,
    manual: null, showLines: true, openRule: "", moreTypes: { left: false, right: false }, notes: [], looked: new Set() };
  const $ = (id) => document.getElementById(id);
  const t = (k) => (T[lang] && T[lang][k]) || T.en[k] || k;
  const v = (k) => (V[lang] && V[lang][k]) || (lang === "en" ? k.replace(/_/g, " ") : k);

  // ------------------------------------------------------------ rule table (same logic as reasoning_drive/labeling/lanes.py)
  function splitTokens(x) { return [...new Set(String(x || "").replace(/,/g, ";").split(";").map((s) => s.trim()).filter(Boolean))].sort(); }
  function match(when, a) { return Object.entries(when || {}).every(([k, w]) => (Array.isArray(w) ? w : [w]).includes(a[k] || "")); }
  function sideAttrs(f, s) { const o = {}; ["color", "pattern", "near_line", "curb", "role", "evidence"].forEach((k) => { o[k] = f[`${s}_${k}`] || ""; }); return o; }
  function lanePrefill(region, f) {
    const acts = {}; ACTIONS.forEach((a) => { acts[a] = ""; });
    const ids = [], notes = [], contested = [];
    const add = (xs) => (xs || []).forEach((x) => { if (!ids.includes(x)) ids.push(x); });
    const table = (S.rules[region] || {});
    SIDES.forEach((s) => {
      const a = sideAttrs(f, s);
      if (!a.pattern && a.curb !== "yes") return;
      const row = (table.boundary || []).find((r) => match(r.when, a)) || { change: "", rule_ids: [] };
      const act = `change_${s}`;
      acts[act] = row.change || "";
      add(row.rule_ids);
      if (row.note) notes.push(`${s}: ${row.note}`);
      if (row.contested) contested.push(act);
      if (a.role === "special_lane_line" && !acts[act]) {
        // ordinary car, reserved time not visible: changing into a bus/HOV/tidal lane is prohibited (contested);
        // leaving the special lane my car is in follows the line type
        const inSpecial = splitTokens(f.markings).some((x) => ["text:bus", "text:hov", "symbol:hov_diamond"].includes(x));
        if (inSpecial) { const a2 = Object.assign({}, a, { role: "lane_line" }); acts[act] = ((table.boundary || []).find((r) => match(r.when, a2)) || {}).change || ""; }
        else acts[act] = "prohibited";
        if (!contested.includes(act)) contested.push(act);
      }
      if (["partial", "insufficient"].includes(a.evidence) && ["allowed", "prohibited"].includes(acts[act])) acts[act] = "not_determined";
    });
    const toks = splitTokens(f.markings);
    const rules = table.markings || {};
    const arrows = toks.filter((x) => S.schema.movement_arrows[x]);
    const noTurn = toks.filter((x) => S.schema.no_turn[x]);
    if (arrows.length) {
      const shown = new Set(arrows.flatMap((x) => S.schema.movement_arrows[x]));
      MOVES.forEach((m) => { acts[m] = shown.has(m) ? "allowed" : "prohibited"; });
      if (arrows.length === 1 && rules[arrows[0]]) {
        Object.entries(rules[arrows[0]].actions || {}).forEach(([m, val]) => { if (MOVES.includes(m)) acts[m] = val; });
        (rules[arrows[0]].contested || []).forEach((c) => { if (!contested.includes(c)) contested.push(c); });
      }
    }
    toks.forEach((tk) => {
      const r = rules[tk]; if (!r) return;
      add(r.rule_ids); if (r.note) notes.push(`${tk}: ${r.note}`);
      Object.entries(r.actions || {}).forEach(([m, val]) => { if (S.schema.no_turn[tk] || !arrows.length || !MOVES.includes(m)) acts[m] = val; });
    });
    // no arrow: going straight along my lane is allowed (project convention, contested), unless my lane ends or is a two-way left-turn lane
    const endsOrTurnOnly = toks.some((x) => ["arrow:merge_left", "arrow:merge_right", "arrow:two_way_left"].includes(x));
    MOVES.forEach((m) => {
      if (acts[m]) return;
      if (m === "go_straight" && !arrows.length && !endsOrTurnOnly) { acts[m] = "allowed"; if (!contested.includes(m)) contested.push(m); }
      else if (!arrows.length && !noTurn.length) acts[m] = "not_applicable";
    });
    if (!acts.enter_waiting_area) acts.enter_waiting_area = "not_applicable";
    // a STOP word or the 停 stop-and-yield line in my lane: every allowed movement needs a full stop first
    if (toks.some((x) => (S.schema.stop_tokens || []).includes(x))) MOVES.forEach((m) => { if (acts[m] === "allowed") acts[m] = "stop_first"; });
    if (["partial", "insufficient"].includes(f.markings_evidence)) [...MOVES, "enter_waiting_area"].forEach((m) => { if (["allowed", "stop_first", "prohibited"].includes(acts[m])) acts[m] = "not_determined"; });
    return { actions: acts, rule_ids: ids, notes, contested };
  }
  function validate(f, region) {
    const errors = [], warnings = [], b = S.schema.boundary;
    SIDES.forEach((s) => {
      const a = sideAttrs(f, s);
      [["color", b.color], ["pattern", b.pattern], ["curb", b.curb], ["role", b.role], ["evidence", S.schema.evidence]].forEach(([k, allowed]) => {
        if (!allowed.includes(a[k])) errors.push(`${t(s)}: ${k === "color" || k === "pattern" ? t("line") : t(k)}`);
      });
      if (a.pattern === "solid_dashed" && !["solid", "dashed"].includes(a.near_line)) errors.push(`${t(s)}: ${t("near_line")}`);
      if ((a.pattern === "none") !== (a.color === "none") && b.pattern.includes(a.pattern)) errors.push(`${t(s)}: ${t("line")} (none = none)`);
    });
    const lc = f.lane_count, ei = f.ego_index;
    if (lc && ei && Number(ei) > Number(lc)) errors.push(`${t("ego_index")} > ${t("lane_count")}`);
    if (!S.schema.evidence.includes(f.scene_evidence)) errors.push(`${t("scene")}: ${t("evidence")}`);
    if (!S.schema.evidence.includes(f.markings_evidence)) errors.push(`${t("markings")}: ${t("evidence")}`);
    ACTIONS.forEach((a) => { if (!S.schema.action_values.includes(f["act_" + a])) errors.push(v(a)); });
    if (String(ei) === "1" && f.left_role === "lane_line") warnings.push("leftmost lane with a lane line on the left / 最左车道但左侧是同向分界线");
    if (lc && String(ei) === String(lc) && f.right_role === "lane_line") warnings.push("rightmost lane with a lane line on the right / 最右车道但右侧是同向分界线");
    const toks = splitTokens(f.markings);
    if (toks.includes("text:only") && toks.some((x) => (S.schema.movement_arrows[x] || []).length > 1)) warnings.push("ONLY with a two-movement arrow (MUTCD 3B.21 ¶08)");
    const known = new Set((S.passages[region] || []).map((p) => p.rule_id));
    const bad = splitTokens(f.accepted_rule_ids).filter((x) => !known.has(x));
    if (bad.length) errors.push("rule IDs: " + bad.join(", "));
    return { errors, warnings };
  }
  // role from the line and the lane position (a suggestion; a click on another role keeps that one)
  function suggestRole(s, f) {
    const c = f[`${s}_color`], p = f[`${s}_pattern`], curb = f[`${s}_curb`] === "yes";
    if (!c && !p) return curb ? "edge_line" : "";
    if (c === "none" || p === "none") return curb ? "edge_line" : "unknown";
    if (c === "yellow") return "center_line";
    if (c !== "white") return "";
    const lc = Number(f.lane_count), ei = Number(f.ego_index), solid = p === "solid" || p === "double_solid";
    if (solid && ((s === "right" && lc && ei === lc) || (s === "left" && ei === 1))) return "edge_line";
    return "lane_line";
  }

  // ------------------------------------------------------------ data access (server or package)
  const store = {
    key: () => `lane_task_results_${PKG && PKG.package_id}`,
    load() { try { return JSON.parse(localStorage.getItem(this.key()) || "{}"); } catch (e) { return S.mem || {}; } },
    save(all) { S.mem = all; try { localStorage.setItem(this.key(), JSON.stringify(all)); } catch (e) { /* kept in memory */ } },
  };
  async function api(path, body) {
    const r = await fetch(path.replace(/^\//, ""), body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {});
    const j = await r.json();
    if (j.error) throw new Error(j.error);
    return j;
  }
  async function loadState() {
    if (PKG) {
      document.body.classList.add("offline");
      const saved = store.load();
      S.items = PKG.items.map((it) => ({ ...it, status: (saved[it.image_id] || {}).status || "", mine: (saved[it.image_id] || {}).status || "" }));
      Object.assign(S, { schema: PKG.schema, rules: PKG.rules, passages: PKG.passages, annotator: PKG.annotator });
      $("notices").innerHTML = (PKG.notices || []).map((n) => `<div>${esc(n)}</div>`).join("");
    } else {
      document.body.classList.add("server");
      const st = await api("/api/state");
      Object.assign(S, { items: st.items, schema: st.schema, rules: st.rules, passages: st.passages, annotator: st.annotator });
      document.body.classList.toggle("can-remove", !!st.can_remove);
      tellParent(st);
    }
    if (EMBED) document.body.classList.add("embedded");
    if (["todo", "all", "conflict", "done"].includes(URLP.get("filter"))) $("filter").value = URLP.get("filter");
    $("who").textContent = `${S.annotator || ""}`;
  }
  function visible() {
    const f = $("filter").value;
    return S.items.filter((it) => f === "all" || (f === "todo" && it.mine !== "done" && !["done", "excluded"].includes(it.status))
      || (f === "conflict" && it.status === "conflict") || (f === "done" && it.status === "done"));
  }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }

  // ------------------------------------------------------------ form
  function lineName(c, p) {
    if (c === "none" || p === "none") return lang === "zh" ? "无标线" : "no line";
    if (lang === "zh") {
      const col = { white: "白", yellow: "黄", other: "其他色" }[c] || "";
      return p === "double_solid" ? `双${col}实线` : p === "double_dashed" ? `双${col}虚线` : col + v(p);
    }
    return `${p.startsWith("double_") ? "double " : ""}${c} ${p.replace("double_", "").replace("solid_dashed", "solid + dashed")}`;
  }
  function tokenName(x) {
    if (lang === "zh") return v(x);
    const [g, n] = x.split(":");
    return (g === "arrow" ? "arrow " : g === "no_turn" ? "no " : "") + n.replace(/_/g, " ");
  }
  function btn(label, data, onclick) {
    const b = document.createElement("button"); b.type = "button"; b.textContent = label;
    Object.entries(data).forEach(([k, val]) => { b.dataset[k] = val; });
    b.onclick = onclick; return b;
  }
  function optRow(container, name, field, values, labelOf) {
    const div = document.createElement("div"); div.className = "opts";
    if (name) div.innerHTML = `<span class="name">${esc(name)}</span>`;
    values.forEach((val) => div.appendChild(btn(labelOf ? labelOf(val) : v(val), { field, value: val }, () => setField(field, val))));
    container.appendChild(div);
    return div;
  }
  function setField(field, val) {
    S.fields[field] = val;
    const side = (field.match(/^(left|right)_role$/) || [])[1];
    if (side) S.manual.role.add(side);
    if (field.startsWith("act_")) S.manual.acts.add(field.slice(4));
    if (field === "lane_count" && val && Number(S.fields.ego_index) > Number(val)) S.fields.ego_index = "";
    if (field === "lane_count" || field === "ego_index") S.looked.add(field);
    refresh();
  }
  function toggleToken(x) {
    const cur = splitTokens(S.fields.markings);
    S.fields.markings = (cur.includes(x) ? cur.filter((y) => y !== x) : [...cur, x]).join(";");
    refresh();
  }
  function buildForm() {
    const b = S.schema.boundary, nums = ["1", "2", "3", "4", "5", "6", "7", "8"];
    $("lane_count_opts").innerHTML = ""; $("ego_index_opts").innerHTML = "";
    [...nums, ""].forEach((n) => {
      $("lane_count_opts").appendChild(btn(n || t("cant_count"), { field: "lane_count", value: n }, () => setField("lane_count", n)));
      $("ego_index_opts").appendChild(btn(n || t("cant_count"), { field: "ego_index", value: n }, () => setField("ego_index", n)));
    });
    $("scene_evidence").innerHTML = ""; optRow($("scene_evidence"), t("evidence"), "scene_evidence", S.schema.evidence);
    SIDES.forEach((s) => {
      const box = $(`fs_${s}`); box.querySelectorAll(":scope > :not(h3)").forEach((x) => x.remove());
      const types = document.createElement("div"); types.className = "opts linetypes";
      LINE_TYPES.forEach(([c, p]) => types.appendChild(btn(lineName(c, p), { side: s, color: c, pattern: p }, () => {
        S.fields[`${s}_color`] = c; S.fields[`${s}_pattern`] = p; refresh();
      })));
      types.appendChild(btn(t("more_types"), { more: s }, () => { S.moreTypes[s] = !S.moreTypes[s]; refresh(); }));
      box.appendChild(types);
      const more = document.createElement("div"); more.className = "more"; more.id = `${s}_more`;
      optRow(more, t("colour"), `${s}_color`, b.color);
      optRow(more, t("pattern"), `${s}_pattern`, b.pattern);
      box.appendChild(more);
      optRow(box, t("near_line"), `${s}_near_line`, ["solid", "dashed"]).id = `${s}_near_row`;
      const curb = document.createElement("label"); curb.className = "check";
      curb.innerHTML = `<input type="checkbox" data-curb="${s}"> <span>${esc(t("curb"))}</span>`;
      curb.querySelector("input").onchange = (e) => { S.fields[`${s}_curb`] = e.target.checked ? "yes" : "no"; refresh(); };
      box.appendChild(curb);
      const role = optRow(box, t("role"), `${s}_role`, b.role);
      role.insertAdjacentHTML("beforeend", `<span class="tag" id="${s}_role_tag"></span>`);
      optRow(box, t("evidence"), `${s}_evidence`, S.schema.evidence);
    });
    $("tokens_common").innerHTML = "";
    COMMON_TOKENS.filter((x) => S.schema.marking_tokens.includes(x)).forEach((x) => $("tokens_common").appendChild(btn(tokenName(x), { token: x }, () => toggleToken(x))));
    const tk = $("tokens"); tk.innerHTML = "";
    const groups = {};
    S.schema.marking_tokens.forEach((x) => { const g = x.split(":")[0]; (groups[g] = groups[g] || []).push(x); });
    Object.entries(groups).forEach(([g, list]) => {
      const div = document.createElement("div"); div.className = "group opts";
      div.innerHTML = `<b title="${esc(S.schema.marking_groups[g] || "")}">${esc(v(g))}</b>`;
      list.forEach((x) => div.appendChild(btn(tokenName(x), { token: x }, () => toggleToken(x))));
      tk.appendChild(div);
    });
    $("markings_evidence").innerHTML = ""; optRow($("markings_evidence"), t("evidence"), "markings_evidence", S.schema.evidence);
    const tb = $("acts"); tb.innerHTML = "";
    ACTIONS.forEach((a) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `<td>${esc(v(a))}</td><td></td><td class="tag" id="tag_${a}"></td>`;
      optRow(tr.children[1], "", "act_" + a, S.schema.action_values);
      tb.appendChild(tr);
    });
  }
  // role, actions and rule IDs follow the label unless the annotator changed them
  function autoFill() {
    if (!S.item || !S.manual) return;
    SIDES.forEach((s) => { if (!S.manual.role.has(s)) { const r = suggestRole(s, S.fields); if (r) S.fields[`${s}_role`] = r; } });
    const f = { ...S.fields };
    SIDES.forEach((s) => { if (f[`${s}_pattern`] !== "solid_dashed") f[`${s}_near_line`] = "not_applicable"; });
    const p = lanePrefill(S.item.region, f);
    ACTIONS.forEach((a) => { if (!S.manual.acts.has(a)) S.fields["act_" + a] = p.actions[a] || ""; });
    const ids = p.rule_ids.filter((x) => !S.manual.rem.has(x));
    S.manual.add.forEach((x) => { if (!ids.includes(x)) ids.push(x); });
    S.fields.accepted_rule_ids = ids.join(";");
    S.prefill = p;
  }
  function refresh() {
    autoFill();
    const f = S.fields;
    document.querySelectorAll("button[data-field]").forEach((b) => {
      const scene = b.dataset.field === "lane_count" || b.dataset.field === "ego_index";  // "can't tell" is on only once clicked
      b.classList.toggle("on", (f[b.dataset.field] || "") === b.dataset.value && (!scene || b.dataset.value !== "" || S.looked.has(b.dataset.field)));
    });
    document.querySelectorAll("button[data-color]").forEach((b) => {
      const s = b.dataset.side, on = f[`${s}_color`] === b.dataset.color && f[`${s}_pattern`] === b.dataset.pattern;
      b.classList.toggle("on", on);
      b.classList.toggle("sug", !on && S.sug[`${s}_color`] === b.dataset.color && S.sug[`${s}_pattern`] === b.dataset.pattern);
    });
    SIDES.forEach((s) => {
      const known = LINE_TYPES.some(([c, p]) => c === f[`${s}_color`] && p === f[`${s}_pattern`]);
      const open = S.moreTypes[s] || (!!(f[`${s}_color`] || f[`${s}_pattern`]) && !known);
      $(`${s}_more`).style.display = open ? "" : "none";
      $(`${s}_near_row`).style.display = f[`${s}_pattern`] === "solid_dashed" ? "" : "none";
      document.querySelector(`input[data-curb="${s}"]`).checked = f[`${s}_curb`] === "yes";
      $(`${s}_role_tag`).textContent = S.manual && !S.manual.role.has(s) && f[`${s}_role`] ? t("auto") : "";
    });
    const lc = Number(f.lane_count) || 8;
    document.querySelectorAll('#ego_index_opts button').forEach((b) => { b.style.display = b.dataset.value && Number(b.dataset.value) > lc ? "none" : ""; });
    const toks = splitTokens(f.markings);
    document.querySelectorAll("button[data-token]").forEach((b) => b.classList.toggle("on", toks.includes(b.dataset.token)));
    $("tokens_none").style.display = toks.length ? "none" : "";
    if (toks.some((x) => !COMMON_TOKENS.includes(x))) $("tokens_more").open = true;
    ACTIONS.forEach((a) => {
      const el = $("tag_" + a); if (!el) return;
      const manual = S.manual && S.manual.acts.has(a);
      el.textContent = manual ? t("changed") : f["act_" + a] ? t("auto") : "";
      el.classList.toggle("changed", !!manual);
    });
    const p = S.prefill || { notes: [], contested: [] };
    $("prefill_notes").textContent = [...p.notes, ...(p.contested.length ? [`${t("contested")}: ${p.contested.map(v).join(", ")}`] : [])].join(" | ");
    showPassages(); draw();
  }
  function showPassages() {
    const region = S.item && S.item.region;
    const all = S.passages[region] || [];
    const by = Object.fromEntries(all.map((p) => [p.rule_id, p]));
    const ids = splitTokens(S.fields.accepted_rule_ids);
    $("passages").innerHTML = ids.map((id) => {
      const p = by[id];
      if (!p) return `<div class="p"><span class="id">[${esc(id)}]</span> ? <button class="x" data-rm="${esc(id)}">×</button></div>`;
      const orig = p.en_is_translation ? p.text_zh : p.text_en, tr = p.en_is_translation ? p.text_en : p.text_zh;
      const first = lang === "zh" ? (p.text_zh || p.text_en) : (p.text_en || p.text_zh);
      const second = lang === "zh" ? (p.text_zh ? (p.zh_is_translation ? `(original) ${p.text_en}` : "") : "") : (orig !== first ? orig : tr);
      const open = S.openRule === id;
      return `<div class="p${open ? " open" : ""}" data-open="${esc(id)}"><span class="id">[${esc(id)}]</span> <span class="muted">${esc(p.section || "")}</span>`
        + ` <button class="x" data-rm="${esc(id)}" title="remove">×</button><div class="txt">${esc(first)}${open && second ? `<div class="tr">${esc(second)}</div>` : ""}</div></div>`;
    }).join("");
    $("passages").querySelectorAll("[data-open]").forEach((el) => { el.onclick = (e) => { if (e.target.dataset.rm) return; S.openRule = S.openRule === el.dataset.open ? "" : el.dataset.open; showPassages(); }; });
    $("passages").querySelectorAll("button[data-rm]").forEach((b) => { b.onclick = () => {
      const id = b.dataset.rm; if (S.manual.add.has(id)) S.manual.add.delete(id); else S.manual.rem.add(id); refresh(); }; });
    const sel = $("rule_add");
    sel.innerHTML = `<option value="">${esc(t("add_rule"))}</option>` + all.filter((p) => !ids.includes(p.rule_id))
      .map((p) => `<option value="${esc(p.rule_id)}">${esc(p.rule_id)}  ${esc((lang === "zh" ? p.text_zh || p.text_en : p.text_en || p.text_zh).slice(0, 60))}</option>`).join("");
  }

  // ------------------------------------------------------------ image, lines and magnifier
  const cv = $("canvas"), ctx = cv.getContext("2d"), lp = $("loupe"), lctx = lp.getContext("2d");
  function pts(field) { try { const p = JSON.parse(S.fields[field] || "null"); return Array.isArray(p) ? p : []; } catch (e) { return []; } }
  function draw() {
    if (!S.img || !S.img.naturalWidth) return;
    cv.width = S.img.naturalWidth; cv.height = S.img.naturalHeight;
    ctx.drawImage(S.img, 0, 0);
    $("toggle_lines").textContent = S.showLines ? t("hide_lines") : t("show_lines");
    if (!S.showLines && !S.drawing) return;
    const lw = Math.max(1.5, cv.width / 700);
    ctx.globalAlpha = 0.7;
    const line = (p, color, dash) => { if (p.length < 2) { p.forEach(([x, y]) => { ctx.fillStyle = color; ctx.beginPath(); ctx.arc(x, y, lw * 2, 0, 7); ctx.fill(); }); return; }
      ctx.setLineDash(dash ? [lw * 4, lw * 3] : []); ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.beginPath(); p.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y))); ctx.stroke(); };
    SIDES.forEach((s) => {
      try { const sp = JSON.parse(S.sug[`${s}_line`] || "[]"); if (sp.length && !S.fields[`${s}_line`]) line(sp, "#f79009", true); } catch (e) { /* bad suggestion */ }
      line(pts(`${s}_line`), s === "left" ? "#ff4d6d" : "#3ddc97", false);
    });
    ctx.globalAlpha = 1; ctx.setLineDash([]);
  }
  cv.addEventListener("click", (e) => {
    if (!S.drawing) return;
    const r = cv.getBoundingClientRect();
    const x = Math.round((e.clientX - r.left) * cv.width / r.width), y = Math.round((e.clientY - r.top) * cv.height / r.height);
    const f = `${S.drawing}_line`; const p = pts(f); p.push([x, y]); S.fields[f] = JSON.stringify(p); draw();
  });
  cv.addEventListener("mousemove", (e) => {
    if (!$("loupe_on").checked || !S.img || !S.img.naturalWidth) { lp.style.display = "none"; return; }
    const r = cv.getBoundingClientRect(), ds = r.width / S.img.naturalWidth;
    const x = (e.clientX - r.left) / ds, y = (e.clientY - r.top) / ds, sw = lp.width / (3 * ds);
    lctx.fillStyle = "#000"; lctx.fillRect(0, 0, lp.width, lp.height);
    lctx.drawImage(S.img, x - sw / 2, y - sw / 2, sw, sw, 0, 0, lp.width, lp.height);  // the photo only, without drawn lines
    lctx.strokeStyle = "rgba(255,255,255,.6)"; lctx.lineWidth = 1;
    lctx.beginPath(); lctx.moveTo(lp.width / 2, lp.height / 2 - 10); lctx.lineTo(lp.width / 2, lp.height / 2 + 10);
    lctx.moveTo(lp.width / 2 - 10, lp.height / 2); lctx.lineTo(lp.width / 2 + 10, lp.height / 2); lctx.stroke();
    const leftHalf = e.clientX - r.left < r.width / 2;
    lp.style.left = leftHalf ? "auto" : "8px"; lp.style.right = leftHalf ? "8px" : "auto";
    lp.style.display = "block";
  });
  cv.addEventListener("mouseleave", () => { lp.style.display = "none"; });
  function setDrawing(side) {
    S.drawing = side; cv.classList.toggle("drawing", !!side);
    $("draw_left").classList.toggle("on", side === "left"); $("draw_right").classList.toggle("on", side === "right"); draw();
  }

  // ------------------------------------------------------------ items
  async function openItem(i) {
    const list = visible();
    document.body.classList.toggle("empty", !list.length);
    if (!list.length) { $("pos").textContent = "0/0"; $("msgs").innerHTML = ""; window.scrollTo(0, 0); return; }
    S.idx = Math.max(0, Math.min(i, list.length - 1));
    S.item = list[S.idx];
    $("pos").textContent = `${S.idx + 1}/${list.length}`;
    $("msgs").innerHTML = ""; setDrawing(""); S.openRule = ""; S.moreTypes = { left: false, right: false };
    let mine = null, final = null, extra = {};
    if (PKG) { mine = (store.load()[S.item.image_id] || {}); S.sug = S.item.suggestion || {}; }
    else { extra = await api("/api/item?id=" + encodeURIComponent(S.item.image_id)); mine = extra.mine; final = extra.final; S.sug = extra.suggestion || {}; }
    S.extra = extra;
    const src = (mine && (mine.fields || mine)) || {};
    const keys = ["lane_count", "ego_index", "scene_evidence", "markings", "markings_evidence", "accepted_rule_ids", "left_line", "right_line",
      ...SIDES.flatMap((s) => ["color", "pattern", "near_line", "curb", "role", "evidence"].map((k) => `${s}_${k}`)), ...ACTIONS.map((a) => "act_" + a)];
    const saved = keys.some((k) => src[k]);
    S.fields = {};
    keys.forEach((k) => { S.fields[k] = src[k] || ""; });
    SIDES.forEach((s) => { if (S.fields[`${s}_near_line`] === "not_applicable") S.fields[`${s}_near_line`] = ""; });
    S.manual = { acts: new Set(), role: new Set(), add: new Set(), rem: new Set() };
    S.looked = new Set(saved ? ["lane_count", "ego_index"] : []);  // a new label needs one look at the lanes before it can be done
    let note = S.sug.prefill_source ? `${t("sug_from")}: ${S.sug.prefill_source}` : "";
    if (saved) {
      // what the annotator set differently from the suggestions stays as it is
      const f = { ...S.fields };
      SIDES.forEach((s) => { if (f[`${s}_pattern`] !== "solid_dashed") f[`${s}_near_line`] = "not_applicable"; });
      const p = lanePrefill(S.item.region, f);
      ACTIONS.forEach((a) => { if (S.fields["act_" + a] && S.fields["act_" + a] !== (p.actions[a] || "")) S.manual.acts.add(a); });
      SIDES.forEach((s) => { if (S.fields[`${s}_role`] && S.fields[`${s}_role`] !== suggestRole(s, S.fields)) S.manual.role.add(s); });
      const ids = splitTokens(S.fields.accepted_rule_ids);
      ids.forEach((x) => { if (!p.rule_ids.includes(x)) S.manual.add.add(x); });
      if (S.fields.accepted_rule_ids) p.rule_ids.forEach((x) => { if (!ids.includes(x)) S.manual.rem.add(x); });
    } else {
      // a new label starts from the usual case and from the dataset's own lane labels
      SIDES.forEach((s) => { S.fields[`${s}_curb`] = "no"; S.fields[`${s}_evidence`] = "full"; });
      S.fields.scene_evidence = "full"; S.fields.markings_evidence = "full";
      let used = false;
      Object.entries(S.sug || {}).forEach(([k, val]) => { if (k !== "prefill_source" && val && k in S.fields) { S.fields[k] = val; used = true; } });
      if (used) note = `${t("sug_applied")} (${S.sug.prefill_source})`;
    }
    $("unsure").checked = (mine && (mine.unsure === "1" || mine.unsure === true)) || false;
    $("comment").value = (mine && mine.comment) || "";
    $("sug_note").textContent = note;
    $("meta").textContent = `${S.item.image_id}, ${S.item.region}, ${S.item.dataset || ""}, ${S.item.split || ""}` +
      (final ? `, ${t("status")}: ${final.lane_status}` : "") + (S.item.marking_hint ? `, ${S.item.marking_hint}` : "") + `  ·  ${t("keys")}`;
    renderAdjudication(final, extra);
    S.img = new Image();
    S.img.onload = () => refresh();
    S.img.src = PKG ? S.item.file : "api/image?id=" + encodeURIComponent(S.item.image_id);
    refresh();
    progress();
  }
  function progress() {
    const done = S.items.filter((x) => x.mine === "done").length;
    $("progress").textContent = `${done}/${S.items.length} ${lang === "zh" ? "已完成" : "done"}`;
  }
  function renderAdjudication(final, extra) {
    const box = $("adjudicate"); box.innerHTML = "";
    if (PKG || !final || final.lane_status !== "conflict" || !extra.others) return;
    const all = [...(extra.mine ? [extra.mine] : []), ...extra.others.filter((o) => o.image_id)];
    const diff = new Set(extra.differences || []);
    let h = `<p><b>${t("adj_title")}</b></p><table><tr><th></th>${all.map((a) => `<th>${esc(a.annotator)}</th>`).join("")}</tr>`;
    [...diff].forEach((f) => { h += `<tr class="diff"><td>${esc(f)}</td>${all.map((a) => `<td>${esc(a[f])}</td>`).join("")}</tr>`; });
    h += `</table><input id="adj_note" placeholder="${t("note")}"> ` + all.map((a) => `<button data-take="${esc(a.annotator)}">${t("take")} ${esc(a.annotator)}</button>`).join(" ")
      + ` <button data-take="exclude">${t("exclude")}</button>`;
    box.innerHTML = h;
    box.querySelectorAll("button[data-take]").forEach((b) => { b.onclick = async () => {
      try { await api("/api/adjudicate", { image_id: S.item.image_id, choice: b.dataset.take, note: $("adj_note").value }); await reloadServer(); openItem(S.idx); }
      catch (e) { $("msgs").innerHTML = `<div class="err">${esc(e.message)}</div>`; } }; });
  }
  async function reloadServer() { if (!PKG) { const st = await api("/api/state"); S.items = st.items; tellParent(st); } }
  function tellParent(st) { if (EMBED) window.parent.postMessage({ type: "lane-counts", counts: st.counts || {} }, location.origin); }
  function openById(id) {
    let i = visible().findIndex((x) => x.image_id === id);
    if (i < 0 && id && S.items.some((x) => x.image_id === id)) { $("filter").value = "all"; i = visible().findIndex((x) => x.image_id === id); }
    return openItem(i >= 0 ? i : 0);
  }
  async function removeImage() {
    if (PKG || !S.item || !window.confirm(t("confirm_remove"))) return;
    try { await api("/api/remove", { image_id: S.item.image_id }); await reloadServer(); openItem(S.idx); }
    catch (e) { $("msgs").innerHTML = `<div class="err">${esc(e.message)}</div>`; }
  }
  function readInputs() {
    S.fields.markings = splitTokens(S.fields.markings).join(";");
    SIDES.forEach((s) => { if (S.fields[`${s}_pattern`] !== "solid_dashed") S.fields[`${s}_near_line`] = "not_applicable"; });
  }
  async function save(status) {
    if (!S.item) return;
    readInputs();
    const chk = validate(S.fields, S.item.region);
    const msgs = [];
    if (status === "done" && !S.looked.has("lane_count") && !$("unsure").checked) chk.errors.unshift(t("look_first"));
    if (status === "done" && chk.errors.length && !$("unsure").checked) {
      $("msgs").innerHTML = `<div class="err">${t("not_saved")} ${esc(chk.errors.join("; "))}</div>`; return;
    }
    if (chk.warnings.length) msgs.push(`<div class="warn">${t("warn")} ${esc(chk.warnings.join("; "))}</div>`);
    try {
      if (PKG) {
        const all = store.load();
        all[S.item.image_id] = { image_id: S.item.image_id, fields: { ...S.fields }, status, unsure: $("unsure").checked, comment: $("comment").value, saved_utc: new Date().toISOString().replace(/\.\d+Z$/, "Z") };
        store.save(all);
        S.item.mine = status; S.item.status = status;
      } else {
        const r = await api("/api/save", { image_id: S.item.image_id, fields: S.fields, status, unsure: $("unsure").checked, comment: $("comment").value });
        (r.warnings || []).forEach((w) => msgs.push(`<div class="warn">${esc(w)}</div>`));
        await reloadServer();
      }
      msgs.unshift(`<div class="ok">${t("saved")}</div>`);
      $("msgs").innerHTML = msgs.join("");
      progress();
      if (status === "done") { const list = visible(); const nextIdx = list.findIndex((x) => x.image_id === S.item.image_id); openItem(nextIdx >= 0 ? nextIdx + 1 : S.idx); }
    } catch (e) { $("msgs").innerHTML = `<div class="err">${esc(e.message)}</div>`; }
  }
  function exportResults() {
    const all = store.load();
    const out = { format: "lane-task-results-v1", package_id: PKG.package_id, annotator: PKG.annotator, exported_utc: new Date().toISOString().replace(/\.\d+Z$/, "Z"), results: Object.values(all) };
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([JSON.stringify(out, null, 1)], { type: "application/json" }));
    a.download = `results_${PKG.package_id}.json`; a.click();
    $("msgs").innerHTML = `<div class="ok">${t("exported")}</div>`;
  }
  function applyLang() {
    document.documentElement.lang = lang;
    document.querySelectorAll("[data-t]").forEach((el) => { el.textContent = t(el.dataset.t); });
    document.querySelectorAll("[data-tp]").forEach((el) => { el.placeholder = t(el.dataset.tp); });
    $("lang").textContent = lang === "zh" ? "English" : "中文";
    $("guide_body").innerHTML = GUIDE[lang];
    if (S.schema) { buildForm(); refresh(); progress(); }
  }

  // ------------------------------------------------------------ wiring
  $("lang").onclick = () => { lang = lang === "zh" ? "en" : "zh"; try { localStorage.setItem("lane_lang", lang); } catch (e) { /* ignore */ } applyLang(); };
  $("prev").onclick = () => openItem(S.idx - 1);
  $("next").onclick = () => openItem(S.idx + 1);
  $("filter").onchange = async () => { await reloadServer(); openItem(0); };
  $("toggle_lines").onclick = () => { S.showLines = !S.showLines; draw(); };
  $("draw_left").onclick = () => setDrawing("left");
  $("draw_right").onclick = () => setDrawing("right");
  $("draw_stop").onclick = () => setDrawing("");
  $("clear_lines").onclick = () => { S.fields.left_line = ""; S.fields.right_line = ""; draw(); };
  $("reset_acts").onclick = () => { if (S.manual) { S.manual.acts.clear(); S.manual.add.clear(); S.manual.rem.clear(); } refresh(); };
  $("rule_add").onchange = (e) => { const id = e.target.value; e.target.blur(); if (id && S.manual) { S.manual.add.add(id); S.manual.rem.delete(id); refresh(); } };
  $("save_draft").onclick = () => save("draft");
  $("save_done").onclick = () => save("done");
  $("export").onclick = exportResults;
  $("remove").onclick = removeImage;
  // inside the main labeling tool: it switches language, filter and image by message
  window.addEventListener("message", async (e) => {
    if (e.origin !== location.origin || !e.data || typeof e.data !== "object") return;
    const m = e.data;
    if (m.type === "lane-lang" && ["en", "zh"].includes(m.lang) && m.lang !== lang) { lang = m.lang; applyLang(); }
    if (m.type === "lane-open") {
      if (!ready) { pendingOpen = m; return; }
      try { await reloadServer(); } catch (err) { return; }
      if (["todo", "all", "conflict", "done"].includes(m.filter)) $("filter").value = m.filter;
      openById(m.id || "");
    }
  });
  let ready = false, pendingOpen = null;
  document.addEventListener("keydown", (e) => {
    const mod = e.metaKey || e.ctrlKey;
    if (mod && e.key === "Enter") { e.preventDefault(); save("done"); return; }
    if (mod && (e.key === "s" || e.key === "S")) { e.preventDefault(); save("draft"); return; }
    if (["INPUT", "SELECT", "TEXTAREA"].includes(e.target.tagName) || mod) return;
    if (e.key === "ArrowRight") openItem(S.idx + 1);
    else if (e.key === "ArrowLeft") openItem(S.idx - 1);
    else if (e.key === "h" || e.key === "H") { S.showLines = !S.showLines; draw(); }
  });
  window.LaneLogic = { lanePrefill, validate, splitTokens, suggestRole, state: S };
  loadState().then(() => {
    applyLang(); ready = true;
    const m = pendingOpen; pendingOpen = null;
    if (m && ["todo", "all", "conflict", "done"].includes(m.filter)) $("filter").value = m.filter;
    openById(m ? m.id || "" : URLP.get("id") || "");
  }).catch((e) => { document.body.insertAdjacentHTML("afterbegin", `<p style="color:red">${esc(e.message)}</p>`); });
})();
