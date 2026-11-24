/* Labeling guide (Chinese and English) with drawings. Used by the local app and the offline helper page.
   LANE_GUIDE.render(lang, ctx) returns HTML; ctx = {regions: ["US"], tables: {US: {...}}, owner: bool}
   (or the older {region, table}). The actions table is built from the rule table, so it always matches the tool. */
"use strict";
(function () {
  const C = { road: "#3b3e44", white: "#f2f2f2", yellow: "#f4c430", me: "#4fb3ff", other: "#9aa0a8", box: "#36e0c8",
    priv: "#ff5ec4", text: "#d5dbe1", muted: "#8f98a2", curb: "#6c727b", bad: "#ff6b6b", good: "#39c27a" };
  const LW = 40; // lane width in drawings

  // ---------------------------------------------------------------- drawing helpers
  function svg(w, h, body, label) {
    return `<svg class="gsvg" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" role="img" aria-label="${label || ""}">${body}</svg>`;
  }
  function solid(x, col, h, wd) { return `<rect x="${x - (wd || 3) / 2}" y="0" width="${wd || 3}" height="${h}" fill="${col}"/>`; }
  function dashed(x, col, h, opts) {
    const o = opts || {}, seg = o.seg || 14, gap = o.gap || 26, wd = o.wd || 3;
    let s = "";
    for (let y = o.offset || 4; y < h; y += seg + gap) s += `<rect x="${x - wd / 2}" y="${y}" width="${wd}" height="${Math.min(seg, h - y)}" fill="${col}" opacity="${o.opacity ?? 1}"/>`;
    return s;
  }
  function line(x, spec, h) {
    const col = spec.kind === "yellow" ? C.yellow : C.white;
    switch (spec.style) {
      case "solid": return solid(x, col, h);
      case "dashed": return dashed(x, col, h, spec);
      case "double": return solid(x - 4, col, h) + solid(x + 4, col, h);
      case "solid_dashed": // spec.dashedSide: "left" or "right" of the pair
        return spec.dashedSide === "left" ? dashed(x - 4, col, h) + solid(x + 4, col, h) : solid(x - 4, col, h) + dashed(x + 4, col, h);
      case "edge": return solid(x, C.curb, h, 2);
      default: return "";
    }
  }
  function car(cx, cy, dir, me, label) {
    const col = me ? C.me : C.other;
    const tri = dir === "down" ? `${cx - 5},${cy + 8} ${cx + 5},${cy + 8} ${cx},${cy + 15}` : `${cx - 5},${cy - 8} ${cx + 5},${cy - 8} ${cx},${cy - 15}`;
    return `<rect x="${cx - 9}" y="${cy - 14}" width="18" height="28" rx="5" fill="${col}"/>` +
      `<polygon points="${tri}" fill="#0b0d10" opacity=".6"/>` +
      (label ? `<text x="${cx}" y="${cy + 6}" text-anchor="middle" font-size="${label.length > 1 ? 7.5 : 9}" fill="#06243a" font-weight="700">${label}</text>` : "");
  }
  function head(x, y, ang, col, sc) { // arrow head pointing at angle (deg, 0 = up)
    sc = sc || 1;
    const r = (a) => (a * Math.PI) / 180, p = (dx, dy) => {
      const c = Math.cos(r(ang)), s = Math.sin(r(ang));
      dx *= sc; dy *= sc;
      return `${(x + dx * c - dy * s).toFixed(1)},${(y + dx * s + dy * c).toFixed(1)}`;
    };
    return `<polygon points="${p(0, -8)} ${p(-6, 2)} ${p(6, 2)}" fill="${col}"/>`;
  }
  function glyph(type, cx, cy, sc, col) { // lane-use arrow, drawn pointing up, centred at cx, cy
    col = col || C.white; sc = sc || 1;
    const st = `stroke="${col}" stroke-width="${4 * sc}" fill="none" stroke-linecap="butt" stroke-linejoin="round"`;
    const P = (d) => `<path d="${d}" ${st}/>`;
    const X = (v) => cx + v * sc, Y = (v) => cy + v * sc;
    const H = (x, y, a) => head(X(x), Y(y), a, col, sc);
    const straight = P(`M${X(0)} ${Y(18)} V${Y(-12)}`) + H(0, -14, 0);
    const left = P(`M${X(0)} ${Y(18)} V${Y(2)} Q${X(0)} ${Y(-8)} ${X(-10)} ${Y(-8)}`) + H(-12, -8, -90);
    const right = P(`M${X(0)} ${Y(18)} V${Y(2)} Q${X(0)} ${Y(-8)} ${X(10)} ${Y(-8)}`) + H(12, -8, 90);
    const uturn = P(`M${X(4)} ${Y(18)} V${Y(-6)} A${6 * sc} ${6 * sc} 0 0 0 ${X(-8)} ${Y(-6)} V${Y(6)}`) + H(-8, 8, 180);
    switch (type) {
      case "straight": return straight;
      case "left": return left;
      case "right": return right;
      case "straight_left": return straight + P(`M${X(0)} ${Y(8)} Q${X(0)} ${Y(0)} ${X(-10)} ${Y(0)}`) + H(-12, 0, -90);
      case "straight_right": return straight + P(`M${X(0)} ${Y(8)} Q${X(0)} ${Y(0)} ${X(10)} ${Y(0)}`) + H(12, 0, 90);
      case "left_right": return left + P(`M${X(0)} ${Y(2)} Q${X(0)} ${Y(-8)} ${X(10)} ${Y(-8)}`) + H(12, -8, 90);
      case "u_turn": return uturn;
      case "left_u_turn": return leftUturn(cx, cy, sc, col);
      case "straight_u_turn": return P(`M${X(4)} ${Y(18)} V${Y(-14)}`) + H(4, -16, 0) + P(`M${X(4)} ${Y(4)} A${6 * sc} ${6 * sc} 0 0 0 ${X(-8)} ${Y(4)} V${Y(12)}`) + H(-8, 14, 180);
      default: return "";
    }
  }
  function leftUturn(cx, cy, sc, col) {
    col = col || C.white; sc = sc || 1;
    const st = `stroke="${col}" stroke-width="${4 * sc}" fill="none"`;
    const X = (v) => cx + v * sc, Y = (v) => cy + v * sc;
    return `<path d="M${X(6)} ${Y(18)} V${Y(-2)} Q${X(6)} ${Y(-10)} ${X(-4)} ${Y(-10)}" ${st}/>` + head(X(-6), Y(-10), -90, col, sc) +
      `<path d="M${X(6)} ${Y(6)} A${5 * sc} ${5 * sc} 0 0 0 ${X(-4)} ${Y(6)} V${Y(14)}" ${st}/>` + head(X(-4), Y(16), 180, col, sc);
  }
  function arrowSvg(type, label) {
    const body = `<rect width="60" height="64" rx="6" fill="${C.road}"/>` + (type === "left_u_turn" ? leftUturn(30, 30, 1.1) : glyph(type, 30, 30, 1.1));
    return `<figure class="gfig small">${svg(60, 64, body, label)}<figcaption>${label}</figcaption></figure>`;
  }
  function tbox(x, y, w, h, lbl) {
    return `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="none" stroke="${C.box}" stroke-width="2.5"/>` +
      (lbl ? `<text x="${x + 2}" y="${y - 3}" font-size="9" fill="${C.box}" font-weight="700">${lbl}</text>` : "");
  }
  function txt(x, y, s, col, anchor, size) {
    return `<text x="${x}" y="${y}" font-size="${size || 9.5}" fill="${col || C.text}" text-anchor="${anchor || "middle"}">${s}</text>`;
  }
  /* road scene, top-down, travel direction up. lines: [{at, kind, style, ...}] where at = boundary index 0..lanes */
  function scene(o) {
    const w = o.w || 200, h = o.h || 150, n = o.lanes, x0 = (w - n * LW) / 2;
    const bx = (i) => x0 + i * LW, lx = (i) => x0 + i * LW + LW / 2;
    let s = `<rect x="0" y="0" width="${w}" height="${h}" fill="#1c1f24"/><rect x="${x0}" y="0" width="${n * LW}" height="${h}" fill="${C.road}"/>`;
    for (const l of o.lines || []) s += line(bx(l.at), l, h);
    for (const a of o.arrows || []) s += a.type === "left_u_turn" ? leftUturn(lx(a.lane), a.y || 60, 0.9) :
      (a.dir === "down" ? `<g transform="rotate(180 ${lx(a.lane)} ${a.y || 60})">${glyph(a.type, lx(a.lane), a.y || 60, 0.9)}</g>` : glyph(a.type, lx(a.lane), a.y || 60, 0.9));
    for (const c of o.cars || []) s += car(lx(c.lane), c.y || (c.dir === "down" ? 30 : 118), c.dir || "up", c.me, c.label);
    for (const b of o.boxes || []) s += tbox(b.x, b.y, b.w, b.h, b.label);
    for (const t of o.texts || []) s += txt(t.x, t.y, t.s, t.col, t.anchor, t.size);
    s += o.extra || "";
    return svg(w, h, s, o.label || "");
  }
  function fig(svgStr, cap, cls) { return `<figure class="gfig ${cls || ""}">${svgStr}<figcaption>${cap}</figcaption></figure>`; }

  // ---------------------------------------------------------------- data from the tool
  function regionsOf(ctx) {
    if (ctx.regions && ctx.regions.length) return ctx.regions;
    return [ctx.region || "US"];
  }
  function tableOf(ctx, region) {
    if (ctx.tables && ctx.tables[region]) return ctx.tables[region];
    return region === (ctx.region || "US") ? (ctx.table || {}) : {};
  }
  const ORDER = ["white_dashed", "white_solid", "white_double_solid", "yellow_dashed", "yellow_solid", "yellow_double_solid",
    "yellow_solid_dashed|ego_side", "yellow_solid_dashed|far_side", "two_way_left_turn_lane", "arrow|straight", "arrow|left", "arrow|right",
    "arrow|straight_left", "arrow|straight_right", "arrow|left_right", "arrow|u_turn", "arrow|left_u_turn", "arrow|straight_u_turn", "other", "none_visible"];
  const ACTS = ["cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_center_lane_to_wait"];

  function actionsTable(lang, table) {
    const O = window.LANE_I18N.OPT[lang];
    const T = (zh, en) => (lang === "zh" ? zh : en);
    const keyName = (k) => {
      const [mt, sub] = k.split("|");
      if (mt === "arrow") return `${O.marking.arrow} · ${O.arrow[sub] || sub}`;
      if (sub) return `${O.marking[mt]} · ${O.dashed[sub] || sub}`;
      return O.marking[mt] || mt;
    };
    const cell = (v, contested) => {
      const d = contested ? ` <span class="ctd" title="${T("有争议：答案来自项目约定", "Contested: the answer comes from a project convention")}">◆</span>` : "";
      if (v === "allowed") return `<td class="ok">✓ ${O.actv.allowed}${d}</td>`;
      if (v === "prohibited") return `<td class="no">✗ ${O.actv.prohibited}${d}</td>`;
      if (v === "not_determined") return `<td class="nd">? ${O.actv.not_determined}${d}</td>`;
      if (v === "not_applicable") return `<td class="na">— </td>`;
      return `<td class="tbd">${T("待定 ●", "TBD ●")}</td>`;
    };
    const keys = ORDER.filter((k) => table[k]).concat(Object.keys(table).filter((k) => !ORDER.includes(k)));
    if (!keys.length) return `<p class="muted">${T("（没有规则表）", "(no rule table)")}</p>`;
    let h = `<div class="gtable-wrap"><table class="gtable"><tr><th>${T("标线", "Marking")}</th>${ACTS.map((a) => `<th>${O.act[a]}</th>`).join("")}<th>${T("建议的规则", "Suggested rules")}</th></tr>`;
    for (const k of keys) {
      const e = table[k];
      const note = (lang === "zh" ? e.note_zh : e.note) || e.note || "";
      h += `<tr><td class="kn">${keyName(k)}${note ? `<div class="knote">${note}</div>` : ""}</td>${ACTS.map((a) => cell(e.actions[a], (e.contested || []).includes(a))).join("")}` +
        `<td class="ids">${(e.rule_ids || []).join("<br>") || "—"}</td></tr>`;
    }
    return h + "</table></div>";
  }
  function answerTable(lang, rows) {
    const O = window.LANE_I18N.OPT[lang];
    const T = (zh, en) => (lang === "zh" ? zh : en);
    const v = (k, x) => {
      if (!x) return "—";
      const map = { marking_type: O.marking, arrow_type: O.arrow, position: O.position, dashed_side: O.dashed, visibility: O.vis, behavior_decidable: O.decide };
      if (map[k]) return map[k][x] || x;
      return O.actv[x] || x;
    };
    let h = `<table class="gans"><tr><th>${T("项目", "Field")}</th><th>${T("答案", "Answer")}</th></tr>`;
    for (const [k, x] of rows) {
      const name = k === "rules" ? O.field.accepted_rule_ids : (O.field[k] || O.act[k] || k);
      h += `<tr><td>${name}</td><td>${k === "rules" ? x : v(k, x)}</td></tr>`;
    }
    return h + "</table>";
  }

  // ---------------------------------------------------------------- the guide
  function render(lang, ctx) {
    ctx = ctx || {};
    const T = (zh, en) => (lang === "zh" ? zh : en);
    const O = window.LANE_I18N.OPT[lang];
    const me = T("我", "Me");
    const regions = regionsOf(ctx);
    const owner = !!ctx.owner;
    const sec = (id, title, body) => `<section class="gsec" id="${id}"><h3>${title}</h3>${body}</section>`;
    const toc = [
      ["g-start", T("1. 五分钟快速上手", "1. Five-minute start")],
      ["g-what", T("2. 我们在做什么", "2. What this is for")],
      ["g-ui", T("3. 界面说明", "3. The screen")],
      ["g-privacy", T("4. 隐私（很重要）", "4. Privacy (important)")],
      ["g-basics", T("5. 基础知识：车道、颜色、线型", "5. Basics: lanes, colours, line patterns")],
      ["g-box", T("6. 目标框：只看框里的那一条", "6. The target box: judge only what is inside")],
      ["g-types", T("7. 标线类型图鉴", "7. Marking types, one by one")],
      ["g-position", T("8. 位置怎么选", "8. Choosing the position")],
      ["g-vis", T("9. 可见性 V2 / V1 / V0", "9. Visibility V2 / V1 / V0")],
      ["g-actions", T("10. 动作怎么选", "10. Choosing the actions")],
      ["g-rules", T("11. 适用规则怎么勾", "11. Ticking the rules")],
      ["g-unsure", T("12. 不确定和备注", "12. Unsure and notes")],
      ["g-examples", T("13. 完整示例", "13. Worked examples")],
      ["g-mistakes", T("14. 常见错误清单", "14. Common mistakes")],
      ["g-save", T("15. 保存、导出和提交", "15. Saving, exporting, sending back")],
      ["g-faq", T("16. 常见问题", "16. Questions")],
      ["g-glossary", T("17. 术语表（中英对照）", "17. Glossary (Chinese / English)")],
    ];
    let h = `<h2>${T("道路标线标注说明", "Lane marking labeling guide")}</h2>` +
      `<p class="glead">${T("第一次标注请从头读到尾，大约 15 分钟。标注时遇到问题，回来查对应的章节。",
        "Read it all once before you start (about 15 minutes). Come back to the matching section whenever you are unsure.")}</p>` +
      `<nav class="gtoc"><b>${T("目录", "Contents")}</b><ol>${toc.map(([id, n]) => `<li><a href="#${id}">${n}</a></li>`).join("")}</ol></nav>`;

    // 1
    h += sec("g-start", toc[0][1], `<ol class="gsteps">
<li>${T("先做左边列表最上面的<b>练习题</b>，每题做完点“检查答案”，看参考答案和你哪里不一样。",
      "Do the <b>practice items</b> at the top of the list first; after each, click \"Check answer\" to compare with the reference.")}</li>
<li>${T("点列表里的一张图。图上的<b class='cyan'>青色框</b>就是这道题：只判断框里的那一条标线（或那一个箭头）。",
      "Click an image in the list. The <b class='cyan'>cyan box</b> is the question: judge only the one marking (or arrow) inside it.")}</li>
<li>${T("右边从上往下选：<b>标线类型 →（箭头类型 / 虚线在哪侧）→ 位置 → 可见性 → 检查动作 → 勾适用规则</b>。动作和规则会自动预填，你要逐项核对。",
      "On the right, go top to bottom: <b>marking type → (arrow type / broken-line side) → position → visibility → check the actions → tick the rules</b>. Actions and rules are prefilled; check every one.")}</li>
<li>${T("用<b class='pink'>隐私框（快捷键 P）</b>把看得清的车牌和人脸框住。",
      "Use <b class='pink'>privacy boxes (shortcut P)</b> to cover readable licence plates and faces.")}</li>
<li>${T("点“完成 ✓ 下一张”。拿不准就勾“不确定”写一句原因，再点完成。",
      "Click \"Done ✓ next\". If you are not sure, tick \"Unsure\", write one sentence, then click Done.")}</li>
<li>${T("<b>每天至少点一次右上角“导出结果”</b>，全部做完后把下载的 <code>results_….json</code> 发回给项目负责人。",
      "<b>Click \"Export results\" (top right) at least once a day</b>, and send the downloaded <code>results_….json</code> to the project owner when you finish.")}</li></ol>`);

    // 2
    h += sec("g-what", toc[1][1], `<p>${T(
      "这个项目测试 AI 模型能不能看懂不同国家的道路标线，比如“这条线能不能跨越”“这个箭头允许怎么走”。你的标注就是<b>标准答案</b>，用来给模型打分，所以要按<b>图片本身</b>和<b>当地交通规则</b>认真判断。",
      "The project tests whether an AI model understands road markings in different countries, such as \"may I cross this line\" or \"which way does this arrow allow\". Your labels are the <b>answer key</b> used to score the model, so judge from <b>the image</b> and <b>the local traffic rules</b>.")}</p>
<ul><li>${T("每张图由<b>两个人独立</b>标注，最后比较两人的答案。<b>请不要和别人商量</b>，也不要看别人的答案。",
      "Two people label every image <b>independently</b> and the answers are compared. <b>Do not discuss answers</b> and do not look at anyone else's.")}</li>
<li>${T("<b>不要用 ChatGPT 等 AI 工具或上网搜答案。</b>答案必须是人的判断，否则就失去了测试的意义。",
      "<b>Do not ask ChatGPT or any AI tool, and do not search the web for answers.</b> The answer key must be human judgement, or the test means nothing.")}</li>
<li>${T("图片可能来自<b>美国</b>或<b>中国</b>。每张图上方会写地区，规则按那个地区的来。两国规则有不同的地方（比如单黄实线），这正是项目要测的。",
      "Images come from the <b>United States</b> or <b>China</b>. The region is shown above each image; use that region's rules. The two countries differ in places (for example a single solid yellow line), which is exactly what the project measures.")}</li></ul>`);

    // 3 UI map
    const uiMap = (() => {
      const W = 520, H = 250;
      let s = `<rect width="${W}" height="${H}" rx="8" fill="#15181c" stroke="#313741"/>`;
      s += `<rect x="0" y="0" width="${W}" height="26" fill="#1b1e23"/>`;
      s += `<rect x="330" y="5" width="44" height="16" rx="3" fill="#23272e" stroke="#4a5260"/>${txt(352, 16, T("English", "中文"), C.text, "middle", 8)}`;
      s += `<rect x="378" y="5" width="44" height="16" rx="3" fill="#23272e" stroke="#4a5260"/>${txt(400, 16, T("说明", "Guide"), C.text, "middle", 8)}`;
      s += `<rect x="440" y="5" width="70" height="16" rx="3" fill="${C.me}"/>${txt(475, 16, T("导出结果", "Export"), "#06243a", "middle", 8)}`;
      s += `<rect x="6" y="32" width="86" height="210" rx="4" fill="#1b1e23"/>`;
      for (let i = 0; i < 5; i++) s += `<rect x="12" y="${42 + i * 38}" width="30" height="20" fill="#2b2f36"/><rect x="46" y="${44 + i * 38}" width="40" height="6" fill="#39404b"/><rect x="46" y="${54 + i * 38}" width="26" height="6" fill="${i < 2 ? C.good : "#39404b"}"/>`;
      s += `<rect x="98" y="32" width="250" height="150" fill="#000"/><rect x="98" y="110" width="250" height="72" fill="${C.road}"/>`;
      s += `<line x1="150" y1="182" x2="215" y2="110" stroke="${C.yellow}" stroke-width="3"/><line x1="300" y1="182" x2="235" y2="110" stroke="${C.white}" stroke-width="3" stroke-dasharray="10 12"/>`;
      s += tbox(262, 128, 34, 40, "") + `<rect x="210" y="118" width="22" height="10" fill="none" stroke="${C.priv}" stroke-width="2"/>`;
      s += `<rect x="354" y="32" width="160" height="210" rx="4" fill="#1b1e23"/>`;
      const rows = [T("标线类型", "Marking type"), T("位置", "Position"), T("可见性", "Visibility"), T("动作", "Actions"), T("适用规则", "Rules")];
      rows.forEach((r, i) => { s += `<rect x="360" y="${38 + i * 34}" width="148" height="28" rx="3" fill="#23272e"/>${txt(366, 50 + i * 34, r, C.text, "start", 8)}`; });
      s += `<rect x="360" y="214" width="70" height="20" rx="3" fill="${C.me}"/>${txt(395, 227, T("完成 ✓", "Done ✓"), "#06243a", "middle", 8)}`;
      const num = (x, y, n) => `<circle cx="${x}" cy="${y}" r="9" fill="#ffd166"/>${txt(x, y + 3.5, n, "#1b1300", "middle", 10)}`;
      s += num(14, 236, "1") + num(110, 44, "2") + num(278, 120, "3") + num(220, 108, "4") + num(366, 36, "5") + num(442, 224, "6") + num(475, 34, "7") + num(352, 36, "8");
      return svg(W, H, s, T("界面示意图", "Screen layout"));
    })();
    h += sec("g-ui", toc[2][1], fig(uiMap, T("界面示意（数字对应下面的说明）", "Screen layout (numbers match the list below)"), "wide") + `<ol class="gnum">
<li>${T("<b>图片列表</b>：上面是练习题，下面是要标的图。绿色 = 已完成，橙色 = 草稿，灰色 = 未开始。左上角可以筛选“未完成 / 全部 / 已完成”。",
      "<b>Image list</b>: practice items first, then the images to label. Green = done, orange = draft, grey = not started. Filter \"To do / All / Done\" at the top.")}</li>
<li>${T("<b>图片</b>：鼠标放上去会出现<b>放大镜</b>；夜间画面可以拖动顶部的“画面增亮”。",
      "<b>Image</b>: hovering shows a <b>magnifier</b>; for night images drag \"Brighten\" at the top.")}</li>
<li>${T("<b class='cyan'>青色目标框</b>：这道题问的标线。框是固定的，你不能改。",
      "<b class='cyan'>Cyan target box</b>: the marking this question is about. It is fixed; you cannot change it.")}</li>
<li>${T("<b class='pink'>粉色隐私框</b>：你自己画的，盖住车牌和人脸。在图上按住鼠标拖动即可画；点一下选中，按 Delete 删除。",
      "<b class='pink'>Pink privacy boxes</b>: you draw them over plates and faces. Press and drag on the image; click one to select it, Delete removes it.")}</li>
<li>${T("<b>答题区</b>：从上往下填。灰色按钮是没选，蓝色是已选；再点一次已选的“箭头类型 / 虚线侧 / 能否决定”可以取消。",
      "<b>Answer panel</b>: fill it top to bottom. Grey buttons are unselected, blue are selected; clicking a selected arrow type / broken-line side / decides again clears it.")}</li>
<li>${T("<b>完成 ✓ 下一张</b>（⌘/Ctrl + Enter）。还没填完会提示缺什么，并先存成草稿。“存草稿”可以先保存、以后再改。",
      "<b>Done ✓ next</b> (⌘/Ctrl + Enter). If something is missing it tells you what and saves a draft. \"Save draft\" keeps your work to finish later.")}</li>
<li>${T("<b>导出结果</b>：下载结果文件，发回给负责人。", "<b>Export results</b>: downloads your results file to send back.")}</li>
<li>${T("<b>中文 / English</b>：随时切换语言，你的答案不受影响。", "<b>中文 / English</b>: switch the language at any time; your answers stay.")}</li></ol>`);

    // 4
    h += sec("g-privacy", toc[3][1], `<ul>
<li>${T("图片来自真实道路，可能拍到别人的<b>车牌</b>和<b>人脸</b>。用<b class='pink'>隐私框</b>把<b>看得清的</b>车牌和人脸都框出来：车牌框住整块牌子，人脸框住整个头部。它们会在任何报告图片里被打码。远处看不清的不用框。",
      "The images show real roads and may show other people's <b>licence plates</b> and <b>faces</b>. Draw a <b class='pink'>privacy box</b> over every <b>readable</b> plate (the whole plate) and face (the whole head). They are blurred in every report image. Far-away, unreadable ones need no box.")}</li>
<li>${T("隐私框和标线答案无关，框不框都不影响题目本身；但请认真画，这是对路人的尊重。",
      "Privacy boxes do not affect the marking answer, but please draw them carefully out of respect for the people in the images.")}</li>
<li>${T("<b>不要截图、转发或上传这些图片</b>，不要发到群里。标完后删除整个文件夹，只把导出的结果文件发回。",
      "<b>Do not screenshot, forward or upload the images</b>, and do not post them in group chats. Delete the whole folder when you finish; send back only the exported results file.")}</li></ul>`);

    // 5 basics
    const basics = scene({ lanes: 3, w: 220, h: 160,
      lines: [{ at: 0, kind: "yellow", style: "solid" }, { at: 1, kind: "white", style: "dashed" }, { at: 2, kind: "white", style: "dashed" }, { at: 3, kind: "white", style: "solid" }],
      cars: [{ lane: 1, me: true, label: me }],
      texts: [{ x: 110, y: 12, s: T("↑ 前进方向", "↑ direction of travel") }, { x: 110, y: 152, s: T("我的车道", "my lane"), col: C.me }] });
    h += sec("g-basics", toc[4][1], fig(basics, T("俯视示意：画面上方是前方，蓝色是“我的车”", "Top view: forward is up; the blue car is \"our car\"")) + `<ul>
<li>${T("<b>我的车</b>：拍摄这段视频的车（摄像头所在的车）。画面底部常能看到它的车头。<b>位置</b>和<b>动作</b>都相对我的车来说。",
      "<b>Our car</b> (\"my car\"): the car that recorded the video. Its bonnet is often visible at the bottom. <b>Position</b> and <b>actions</b> are always relative to it.")}</li>
<li>${T("<b>我的车道</b>：我的车正在走的那条车道，也就是左右两条边界线之间的那一条。",
      "<b>My lane</b> (\"our lane\"): the lane our car is driving in, between its left and right boundary lines.")}</li>
<li>${T("<b>白色线</b>：分隔<b>同一方向</b>的车流（两边的车都朝同一个方向开），也用作道路右侧边线。",
      "<b>White lines</b> separate traffic going <b>the same way</b>, and mark the right edge of the road.")}</li>
<li>${T("<b>黄色线</b>：分隔<b>相反方向</b>的车流（线的另一边是对向来车）。在美国，黄线还用作单行道、匝道和中间有隔离带的道路的<b>左侧边线</b>，以及双向左转车道的边线。",
      "<b>Yellow lines</b> separate traffic going <b>opposite ways</b> (oncoming traffic on the other side). In the US, yellow also marks the <b>left edge</b> of one-way roads, ramps and divided highways, and the edges of two-way left-turn lanes.")}</li>
<li>${T("<b>虚线</b>（一段一段的）：一般表示<b>可以跨越</b>。美国的虚线标准是 10 英尺线段 + 30 英尺间隔，所以照片里<b>间隔明显比线段长</b>。",
      "<b>Broken (dashed) lines</b>: usually <b>crossing is permitted</b>. The US standard is 10-foot segments with 30-foot gaps, so in photos <b>the gaps are much longer than the segments</b>.")}</li>
<li>${T("<b>实线</b>（连续不断）：不鼓励或禁止跨越（具体看线的种类和地区）。<b>双线</b>：最严格的限制。",
      "<b>Solid lines</b> (unbroken): crossing is discouraged or prohibited (depends on the line and the region). <b>Double lines</b>: the strongest restriction.")}</li>
<li>${T("<b>夜间分颜色</b>：车灯下黄色常显得发橙、发暗，白色显得更亮、发白或略带蓝。先拉“画面增亮”，再和同一画面里已经确定颜色的线比较。实在分不清，见第 9 节（V1）。",
      "<b>Colour at night</b>: under headlights yellow often looks orange or dull, white looks brighter and whiter or slightly blue. Raise \"Brighten\", then compare with a line in the same image whose colour you are sure of. If you still cannot tell, see section 9 (V1).")}</li></ul>`);

    // 6 target box
    const boxGood1 = scene({ lanes: 2, w: 150, h: 140, lines: [{ at: 1, kind: "white", style: "dashed" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }],
      cars: [{ lane: 0, me: true, label: me, y: 115 }], boxes: [{ x: 66, y: 40, w: 18, h: 62 }] });
    const boxBad1 = scene({ lanes: 2, w: 150, h: 140, lines: [{ at: 1, kind: "white", style: "dashed" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }],
      cars: [{ lane: 0, me: true, label: me, y: 115 }], boxes: [{ x: 66, y: 40, w: 18, h: 16 }] });
    const boxGood2 = scene({ lanes: 2, w: 150, h: 140, lines: [{ at: 1, kind: "yellow", style: "double" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }],
      cars: [{ lane: 1, me: true, label: me, y: 115 }, { lane: 0, dir: "down", y: 30 }], boxes: [{ x: 62, y: 40, w: 26, h: 60 }] });
    const boxBad2 = scene({ lanes: 2, w: 150, h: 140, lines: [{ at: 1, kind: "yellow", style: "double" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }],
      cars: [{ lane: 1, me: true, label: me, y: 115 }, { lane: 0, dir: "down", y: 30 }], boxes: [{ x: 64, y: 40, w: 10, h: 60 }] });
    const boxGood3 = scene({ lanes: 2, w: 150, h: 140, lines: [{ at: 1, kind: "white", style: "solid" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }],
      arrows: [{ lane: 1, type: "straight_right", y: 55 }], cars: [{ lane: 1, me: true, label: me, y: 118 }], boxes: [{ x: 89, y: 32, w: 42, h: 48 }] });
    const boxBad3 = scene({ lanes: 2, w: 150, h: 140, lines: [{ at: 1, kind: "white", style: "solid" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }],
      arrows: [{ lane: 1, type: "straight_right", y: 55 }], cars: [{ lane: 1, me: true, label: me, y: 118 }], boxes: [{ x: 89, y: 56, w: 42, h: 24 }] });
    h += sec("g-box", toc[5][1], `<p>${T(
      "一张图里通常有好几条线。<b>每道题只问青色框里的那一条</b>（或那一个箭头）。框外的线、箭头、车都只是背景，不要因为它们改变答案。",
      "An image usually shows several markings. <b>Each question is only about the one marking inside the cyan box</b> (or the one arrow). Lines, arrows and cars outside the box are background; do not let them change your answer.")}</p>
<p>${T("框是项目负责人按下面的规则画的。如果你发现框不符合规则（比如框里有两种不同的线、框住的不是标线、框只框到半个箭头头部），<b>勾“不确定”并写明原因</b>，不要自己猜框的是哪条。",
      "The project owner draws the box following the rules below. If a box breaks them (two different markings inside, no marking inside, half an arrow head cut off), <b>tick \"Unsure\" and say why</b>; do not guess which marking was meant.")}</p>
<div class="gfigs">${fig(boxGood1, T("✓ 虚线：至少一整段线 + 一个间隔", "✓ Dashed: at least one full dash and one gap"))}${fig(boxBad1, T("✗ 只框了一小段：看不出是虚线还是实线", "✗ Only a short piece: dashed or solid?"), "bad")}
${fig(boxGood2, T("✓ 双线：两条都在框里", "✓ Double line: both lines inside"))}${fig(boxBad2, T("✗ 只框了一条：可能被当成单线", "✗ Only one line: looks like a single line"), "bad")}
${fig(boxGood3, T("✓ 箭头：整个箭头，含所有头部", "✓ Arrow: the whole arrow, every head"))}${fig(boxBad3, T("✗ 切掉了箭头头部", "✗ Arrow heads cut off"), "bad")}</div>
<ul><li>${T("实线：框住离车最近、最清楚的一段，长度要超过“一段虚线 + 一个间隔”，这样才能确认它真的是连续的。",
      "Solid line: the stretch nearest the car where it is clearest, longer than one dash plus one gap, so that it is clearly unbroken.")}</li>
<li>${T("双向左转车道：框住靠我方一侧的那对边线（一实一虚），能看到成对箭头时一起框进去。",
      "Two-way left-turn lane: the pair of edge lines on our side (one solid, one broken), plus the pair of arrows when visible.")}</li>
<li>${T("几乎看不到标线（V0）时，框表示标线本应在的位置。", "When almost nothing is visible (V0), the box shows where the marking should be.")}</li>
<li>${T("框住的应该是车道线、中心线、导向箭头或双向左转车道。如果框住的是<b>路边线</b>（外侧是路肩或路缘）、<b>自行车道线</b>或人行横道，勾“不确定”并写明。",
      "The box should hold a lane line, a centre line, an arrow or a two-way left-turn lane. If it holds a <b>road edge line</b> (shoulder or curb beyond it), a <b>bike lane line</b> or a crosswalk, tick \"Unsure\" and say so.")}</li>
${owner ? `<li><b>${T("给负责人：", "For the owner: ")}</b>${T("框要留几个像素的余量，但不要把旁边的线框进来；同一个实际标线只保存一帧；不要框路边线（道路最外侧、旁边是路肩或路缘的线）和自行车道线（旁边是窄的自行车道，常有自行车图案）；美国的黄色左侧边线可以框。",
      "leave a few pixels of margin but keep neighbouring lines out; keep one frame per physical marking; do not box road edge lines (the outermost line next to the shoulder or curb) or bike lane lines (next to a narrow lane, often with a bicycle symbol); the US yellow left edge line is fine.")}</li>` : ""}</ul>`);

    // 7 types
    const tw = 170, th = 132;
    const typeCards = [
      ["white_dashed", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "white", style: "dashed" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 0, me: true, label: me, y: 108 }, { lane: 1, y: 40 }] }),
        T("同方向两条车道之间的白色虚线。可以在安全时变道。<br><b>美国</b>：不鼓励也不禁止谨慎越线（3B.06）。<b>中国</b>：可跨越同向车行道分界线（5.2）。",
          "White broken line between two lanes going the same way. You may change lanes when safe.<br><b>US</b>: crossing with care is neither discouraged nor prohibited (3B.06). <b>China</b>: crossable lane line (5.2).")],
      ["white_solid", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "white", style: "solid" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 0, me: true, label: me, y: 108 }, { lane: 1, y: 40 }] }),
        T("同方向车道之间的白色实线，常见于路口前（分隔直行和转弯车道）。<br><b>美国</b>：“不鼓励”越线，不是禁止（3B.06）。项目约定：越线 = <b>允许</b> ◆。只用于两条同向车道之间的线；路边线、自行车道线不作为目标。<b>中国</b>：禁止跨越（6.2.1）。",
          "White solid line between lanes going the same way, common before intersections (separating through and turn lanes).<br><b>US</b>: crossing is <i>discouraged</i>, not prohibited (3B.06). Project convention: crossing = <b>Allowed</b> ◆. Only for a line between two lanes going our way; road edge lines and bike lane lines are not targets. <b>China</b>: no crossing (6.2.1).")],
      ["white_double_solid", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "white", style: "double" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 0, me: true, label: me, y: 108 }, { lane: 1, y: 40 }] }),
        T("两条白色实线并排。禁止越线（美国 3B.06 ¶12）。", "Two white solid lines side by side. Crossing is prohibited (US 3B.06 ¶12).")],
      ["yellow_dashed", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "yellow", style: "dashed" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 1, me: true, label: me, y: 108 }, { lane: 0, dir: "down", y: 34 }] }),
        T("双向道路中间的黄色虚线（另一边是对向来车）。可以在安全时越线超车。<br><b>美国</b>：双向允许超车区（3B.01 ¶04 A）。<b>中国</b>：可跨越对向车行道分界线（5.1）。",
          "Yellow broken line in the middle of a two-way road (oncoming traffic on the other side). You may cross to overtake when safe.<br><b>US</b>: two-direction passing zone (3B.01 ¶04 A). <b>China</b>: crossable centre line (5.1).")],
      ["yellow_solid", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 0, kind: "yellow", style: "solid" }, { at: 1, kind: "white", style: "dashed" }, { at: 2, kind: "white", style: "solid" }], cars: [{ lane: 0, me: true, label: me, y: 108 }, { lane: 1, y: 40 }] }),
        T("<b>一条</b>黄色实线。两国含义不同：<br><b>美国</b>：不能用作双向道路的中心线（3B.01 ¶05），通常是<b>单行道、匝道或有中央隔离带道路的左侧边线</b>（左边没有对向车道）。<b>中国</b>：禁止双方向越线的中心线（6.1.4）。美国：越线 = <b>禁止</b>（3B.09 ¶03：左侧边线表示它左侧的行驶或超车限制）。",
          "<b>One</b> solid yellow line. The meaning differs:<br><b>US</b>: shall not be a centre line on a two-way road (3B.01 ¶05); it is usually the <b>left edge of a one-way road, ramp or divided highway</b> (no oncoming lane beyond it). <b>China</b>: no-crossing centre line for both directions (6.1.4). US: crossing = <b>Prohibited</b> (3B.09 ¶03: a left edge line indicates driving or passing restrictions left of it).")],
      ["yellow_double_solid", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "yellow", style: "double" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 1, me: true, label: me, y: 108 }, { lane: 0, dir: "down", y: 34 }] }),
        T("两条黄色实线并排。双方向都禁止越线（美国 3B.01 ¶04 C；中国 6.1.2）。", "Two solid yellow lines side by side. No crossing in either direction (US 3B.01 ¶04 C; China 6.1.2).")],
      ["yellow_solid_dashed", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "yellow", style: "solid_dashed", dashedSide: "right" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 1, me: true, label: me, y: 108 }, { lane: 0, dir: "down", y: 34 }] }),
        T("一实一虚两条黄线并排。<b>靠近我的车的那一条</b>决定能不能越线：图中靠近“我”的是虚线 → 选“虚线在我这一侧”，越线 = 允许；如果靠近我的是实线 → 选“实线在我这一侧”，越线 = 禁止（美国 3B.01 ¶04 B；中国 6.1.3）。",
          "One solid and one broken yellow line side by side. <b>The line nearer our car</b> decides: here the broken line is on our side → \"Broken line on my side\", crossing allowed; if the solid line is on our side → \"Solid line on my side\", crossing prohibited (US 3B.01 ¶04 B; China 6.1.3).")],
      ["two_way_left_turn_lane", scene({ lanes: 3, w: tw + 20, h: th,
        lines: [{ at: 1, kind: "yellow", style: "solid_dashed", dashedSide: "right" }, { at: 2, kind: "yellow", style: "solid_dashed", dashedSide: "left" }, { at: 0, style: "edge" }, { at: 3, style: "edge" }],
        arrows: [{ lane: 1, type: "left", y: 42 }, { lane: 1, type: "left", dir: "down", y: 92 }], cars: [{ lane: 2, me: true, label: me, y: 108 }, { lane: 0, dir: "down", y: 30 }] }),
        T("美国常见的<b>中间车道</b>：两侧边线都是“外侧黄实线 + 内侧黄虚线”，车道里有<b>方向相反的成对白色左转箭头</b>。两个方向的车都可以在左转时使用这条车道（MUTCD 3B.05 ¶01），所以“进中间车道等左转”和“左转”都是允许。如果我的车就在这条车道里，位置选“在我的车道里”。框住这条车道里的箭头时，也选“双向左转车道”，<b>不要</b>选“导向箭头”。",
          "A US <b>centre lane</b>: each edge is a solid yellow line on the outside and a broken yellow line on the inside, with <b>pairs of white left-turn arrows pointing opposite ways</b>. Traffic from both directions may use it as part of a left turn (MUTCD 3B.05 ¶01), so \"enter the centre lane to wait\" and \"turn left\" are both allowed. If our car is in this lane, choose position \"In our lane\". If the box holds an arrow inside this lane, still choose \"Two-way left-turn lane\", <b>not</b> \"Arrow\".")],
      ["arrow", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "white", style: "solid" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], arrows: [{ lane: 0, type: "left", y: 50 }, { lane: 1, type: "straight_right", y: 50 }], cars: [{ lane: 1, me: true, label: me, y: 110 }] }),
        T("车道里的白色箭头，表示<b>从这条车道</b>可以怎么走（美国 3B.23；中国 5.13）。箭头画出的方向 = 允许；没画出的方向 = 禁止。例外：左转类箭头（左转、直行+左转、左转+右转）的车道，掉头 = <b>允许</b> ◆（美国的项目约定）。下面有全部箭头类型。",
          "White arrows painted in a lane show the movements allowed <b>from that lane</b> (US 3B.23; China 5.13). Directions drawn = allowed; directions not drawn = prohibited. Exception: in a lane with a left-type arrow (left, straight + left, left + right), U-turn = <b>Allowed</b> ◆ (US project convention). All arrow types are shown below.")],
      ["other", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "white", style: "dashed" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }],
        extra: [0, 1, 2, 3, 4, 5, 6].map((i) => `<rect x="${47 + i * 11}" y="38" width="6" height="26" fill="${C.white}"/>`).join("") + `<rect x="45" y="78" width="80" height="4" fill="${C.white}"/>`,
        cars: [{ lane: 1, me: true, label: me, y: 110 }] }),
        T("人行横道、停止线、让行线、路面文字（ONLY、STOP 等）、自行车标志、导流线、路缘等。不评判任何动作，动作全部选“不适用”。",
          "Crosswalks, stop and yield lines, words on the road (ONLY, STOP …), bike symbols, gore chevrons, curbs and so on. No action is scored: every action is N/A.")],
      ["none_visible", scene({ lanes: 2, w: tw, h: th, lines: [{ at: 1, kind: "white", style: "dashed", opacity: 0.12 }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 0, me: true, label: me, y: 108 }], boxes: [{ x: 76, y: 30, w: 18, h: 60 }] }),
        T("框里几乎看不到任何标线（太暗、全被遮住、完全磨掉）。只能配 V0，动作全部“无法确定”。", "Almost nothing visible in the box (too dark, fully covered, worn away). Goes with V0 only; every action is Undetermined.")],
    ];
    h += sec("g-types", toc[6][1], `<p>${T("下面每张图都是俯视示意，蓝色是我的车。括号里是规则条文的章节号，可以在答题区的“适用规则”里找到原文和译文。",
      "Each drawing is a top view; the blue car is ours. Section numbers in brackets point to the rule passages, whose original text and translation are in the Rules part of the answer panel.")}</p>` +
      `<div class="gcards">${typeCards.map(([k, s, d]) => `<div class="gcard"><div class="gcard-h">${O.marking[k]} <code>${k}</code></div>${s}<p>${d}</p></div>`).join("")}</div>` +
      `<h4>${T("全部箭头类型", "All arrow types")}</h4><div class="gfigs">${Object.keys(O.arrow).map((k) => arrowSvg(k, O.arrow[k])).join("")}</div>` +
      `<p class="muted">${T("组合箭头选对应的组合，例如一个箭头同时指向前方和右方 → “直行+右转”。看不到箭头头部时不能确定类型，见第 9 节。",
        "Choose the combination for combined arrows, e.g. one arrow pointing ahead and right → \"Straight + right\". Without the arrow head the type cannot be decided; see section 9.")}</p>`);

    // 8 position
    const pos = scene({ lanes: 3, w: 240, h: 170,
      lines: [{ at: 0, kind: "white", style: "solid" }, { at: 1, kind: "white", style: "dashed" }, { at: 2, kind: "white", style: "dashed" }, { at: 3, kind: "white", style: "solid" }],
      arrows: [{ lane: 1, type: "straight", y: 60 }, { lane: 2, type: "right", y: 60 }], cars: [{ lane: 1, me: true, label: me, y: 130 }],
      texts: [{ x: 60, y: 14, s: "left", col: "#ffd166" }, { x: 100, y: 14, s: "left", col: "#ffd166" }, { x: 140, y: 14, s: "right", col: "#ffd166" },
        { x: 180, y: 14, s: "right", col: "#ffd166" }, { x: 120, y: 92, s: "in_ego_lane", col: "#ffd166" }, { x: 160, y: 92, s: "right", col: "#ffd166" }] });
    h += sec("g-position", toc[7][1], fig(pos, T("黄色字是每条线 / 每个箭头的位置", "Yellow text: the position of each line / arrow"), "wide") + `<ul>
<li>${T("<b>我的左边</b> left：标线在我的车的左侧，包括我的车道的左边界线，以及更左边的线。",
      "<b>Left of our car</b> (left): the marking is on our car's left, including the left boundary of our lane and anything further left.")}</li>
<li>${T("<b>我的右边</b> right：同理，在右侧。", "<b>Right of our car</b> (right): the same on the right.")}</li>
<li>${T("<b>在我的车道里</b> in_ego_lane：标线在我的车道的两条边界线之间，通常是箭头、文字。车正好压在一条线上（正在变道）时，也选这一项。",
      "<b>In our lane</b> (in_ego_lane): the marking lies between our lane's two boundary lines, usually an arrow or a word. If our car is straddling a line (changing lanes), choose this too.")}</li>
<li>${T("箭头在旁边车道里时，位置选 left / right，动作仍然描述<b>那条车道</b>的车能怎么走。",
      "When the arrow is in a neighbouring lane, choose left / right; the actions still describe what traffic in <b>that lane</b> may do.")}</li></ul>`);

    // 9 visibility
    const vp = (lbl, body) => fig(svg(110, 120, `<rect width="110" height="120" fill="${C.road}"/>${body}`, lbl), lbl);
    const visFigs = vp(T("V2 清晰", "V2 clear"), dashed(55, C.white, 120, { seg: 14, gap: 26 }) + tbox(42, 8, 26, 100)) +
      vp(T("V1 · 能决定：有磨损，但能看到一整段线 + 一个间隔", "V1 · decides: worn, but one full dash and one gap visible"),
        dashed(55, C.white, 120, { seg: 14, gap: 26, opacity: 0.45 }) + `<rect x="40" y="60" width="30" height="40" fill="${C.road}" opacity=".85"/>` + tbox(42, 8, 26, 100)) +
      vp(T("V1 · 不能：只看到一小段，分不出虚实", "V1 · does not: only a fragment, dashed or solid?"),
        `<rect x="53.5" y="44" width="3" height="12" fill="${C.white}" opacity=".7"/><rect x="20" y="62" width="70" height="50" rx="6" fill="${C.other}"/>` + txt(55, 92, T("被车挡住", "covered"), "#111", "middle", 9) + tbox(42, 8, 26, 100)) +
      vp(T("V0：几乎看不到", "V0: almost nothing"), dashed(55, C.white, 120, { seg: 14, gap: 26, opacity: 0.08 }) + tbox(42, 8, 26, 100));
    h += sec("g-vis", toc[8][1], `<div class="gfigs">${visFigs}</div>
<p><b>${T("按顺序回答三个问题：", "Answer three questions in order:")}</b></p><ol class="gsteps">
<li>${T("框里能看到标线吗？<b>看不到 → V0</b>，标线类型选“看不到”。", "Can you see any marking in the box? <b>No → V0</b>, marking type \"None visible\".")}</li>
<li>${T("整条标线都清楚吗（没有磨损、遮挡，也不是太暗）？<b>是 → V2</b>。", "Is the whole marking clear (not worn, covered or too dark)? <b>Yes → V2</b>.")}</li>
<li>${T("否则是 <b>V1</b>。再回答“<b>可见部分能决定行为吗？</b>”：", "Otherwise it is <b>V1</b>. Then answer \"<b>Does the visible part decide the behavior?</b>\":")}
<ul><li>${T("线：要能看出<b>颜色</b>和<b>线型</b>。虚线至少看到一整段线和一个间隔；实线连续长度要超过一段线加一个间隔；双线两条都要看得到。",
      "Line: its <b>colour</b> and <b>pattern</b> must be visible. Dashed: at least one full dash and one gap; solid: unbroken for longer than a dash plus a gap; double: both lines visible.")}</li>
<li>${T("箭头：要能看到<b>箭头头部</b>（看不到头部就不知道指向哪里）。", "Arrow: the <b>arrow head</b> must be visible (without it you cannot tell where it points).")}</li>
<li>${T("黄虚实线：两条线都要看清，才能知道哪一侧是虚线。", "Yellow solid + dashed: both lines must be clear to know which side is broken.")}</li>
<li>${T("都满足 → “能决定”（期望证据 = full，正常回答动作）。缺一样 → “不能”（期望证据 = partial）。", "All met → \"Decides\" (expected evidence full; answer the actions normally). Anything missing → \"Does not\" (expected evidence partial).")}</li></ul></li></ol>
<ul><li>${T("<b>“不能”时怎么填：</b>标线类型选你能确定的那个；箭头类型、虚线侧<b>可以留空</b>；本来由这条标线决定的动作选“无法确定”，其他的选“不适用”（页面会自动帮你预填）。",
      "<b>When it does not decide:</b> choose the marking type you can be sure of; the arrow type and broken-line side <b>may stay empty</b>; actions this marking would decide are Undetermined, the rest N/A (the page prefills this).")}</li>
<li>${T("如果连颜色或虚实都看不出、导致标线类型也定不了：选最接近你看到的类型，勾“不确定”，写明“看不出虚实 / 颜色”。",
      "If you cannot even tell the colour or the pattern, so the type itself is unclear: choose the type closest to what you see, tick \"Unsure\" and write \"cannot tell dashed / colour\".")}</li>
<li>${T("V0 时：类型选“看不到”，所有动作“无法确定”，不用勾规则。", "V0: type \"None visible\", every action Undetermined, no rules needed.")}</li></ul>`);

    // 10 actions
    h += sec("g-actions", toc[9][1], `<p>${T("六个动作都要选。每个动作有四种答案：", "Set all six actions. Each has four possible answers:")}</p>
<table class="gans"><tr><td class="ok">✓ ${O.actv.allowed}</td><td>${T("这条标线管这个动作，而且规则<b>没有禁止</b>它。“不鼓励”（discouraged）也算允许。", "This marking governs the action and the rules <b>do not prohibit</b> it. \"Discouraged\" still counts as allowed.")}</td></tr>
<tr><td class="no">✗ ${O.actv.prohibited}</td><td>${T("规则<b>明确禁止</b>这个动作（例如双实线不许越线）；或者是箭头<b>没有画出</b>的方向。", "The rules <b>clearly prohibit</b> the action (e.g. no crossing a double solid line), or it is a direction the arrow <b>does not show</b>.")}</td></tr>
<tr><td class="nd">? ${O.actv.not_determined}</td><td>${T("这条标线<b>本来管</b>这个动作，但图片看不清（V1 选了“不能”，或 V0）。", "This marking <b>would govern</b> the action, but the image does not show enough (V1 \"Does not\", or V0).")}</td></tr>
<tr><td class="na">— ${O.actv.not_applicable}</td><td>${T("这条标线<b>不管</b>这个动作。例如车道线不管左转，箭头不管越线。", "This marking <b>does not govern</b> the action. A lane line says nothing about left turns; an arrow says nothing about crossing a line.")}</td></tr></table>
<div class="gex"><b>${T("判断原则（规则没写清楚时怎么办）", "The default when the rules are silent")}</b><ul>
<li>${T("<b>车道线、中心线：法无禁止即可为。</b>只有条文明确禁止（双实线、实线在我这一侧等）才选“禁止”；条文只说“不鼓励”或没有提到，就选“允许”。", "<b>Lane lines and centre lines: what is not prohibited is allowed.</b> Choose Prohibited only when a passage prohibits it (double solid line, solid line on my side ...). If a passage only says \"discouraged\", or says nothing, choose Allowed.")}</li>
<li>${T("<b>导向箭头：画出的方向允许，没画出的方向禁止。</b>唯一例外：左转类箭头（左转、直行+左转、左转+右转）的车道可以掉头。", "<b>Arrows: the directions shown are allowed, the others are prohibited.</b> One exception: a lane with a left-type arrow (left, straight + left, left + right) also allows a U-turn.")}</li>
<li>${T("规则表里带 <span class='ctd'>◆</span> 的格子是<b>有争议</b>的：条文本身没有直接写，答案来自上面的项目约定。照约定标就行，不用勾“不确定”；评估模型时这些格子会单独统计。", "Cells marked <span class='ctd'>◆</span> in the rule table are <b>contested</b>: the passages do not say it in words and the answer comes from the conventions above. Label them as the convention says (no need to tick Unsure); when models are scored these cells are reported separately.")}</li></ul></div>
<p><b>${T("每种标线管哪些动作：", "Which actions each marking governs:")}</b></p><ul>
<li>${T("车道线、中心线（白 / 黄，实 / 虚 / 双线）：只管<b>越线</b>（变道或越线超车）。", "Lane lines and centre lines (white / yellow, solid / broken / double): only <b>crossing the line</b> (changing lanes or overtaking across it).")}</li>
<li>${T("导向箭头：管<b>直行、左转、右转、掉头</b>（指在下一个路口从这条车道怎么走）。", "Arrows: <b>straight, left, right, U-turn</b> (what traffic in that lane may do at the next intersection).")}</li>
<li>${T("双向左转车道：管<b>进中间车道等左转</b>和<b>左转</b>。", "Two-way left-turn lane: <b>entering the centre lane to wait for a left turn</b> and <b>turning left</b>.")}</li>
<li>${T("其他标线：什么都不管，全部“不适用”。", "Other markings: nothing; all N/A.")}</li></ul>
<p>${T("选好类型后，页面会按下面的规则表<b>自动预填</b>动作。请对照图片和规则逐项检查：",
      "After you choose the type, the page <b>prefills</b> the actions from the rule table below. Check each one against the image and the rules:")}</p><ul>
<li>${T("动作名后面有 <span class='dot'>●</span>：规则表没有预填（规则条文本身没说清楚）。看<b>黄色提示框</b>里的项目约定来选；如果提示里也没有答案，勾“不确定”。",
      "A <span class='dot'>●</span> after the action name: not prefilled (the rule text itself is unclear). Use the project convention in the <b>yellow note</b>; if the note gives no answer, tick \"Unsure\".")}</li>
<li>${T("你选的和规则表不同时会显示“≠表”。如果你确定（比如图片里有特殊情况），可以保留；否则改回来。",
      "\"≠table\" appears when your choice differs from the table. Keep it if you are sure (something special in the image); otherwise change it back.")}</li></ul>` +
      regions.map((r) => `<h4>${T("规则表", "Rule table")} · ${O.region[r] || r}</h4>${actionsTable(lang, tableOf(ctx, r))}`).join("") +
      `<p class="muted">${T("◆ = 有争议的格子（答案来自项目约定）。“待定 ●”= 还没有约定的格子。", "◆ = contested cell (the answer comes from a project convention). \"TBD ●\" = no convention yet.")}</p>`);

    // 11 rules
    h += sec("g-rules", toc[10][1], `<ul>
<li>${T("答题区最下面是这张图所在地区的规则条文。每条都显示<b>原文</b>和<b>译文</b>：美国条文是英文原文 + 中文译文，中国条文是中文原文 + 英文译文。<b>译文仅供参考，以原文为准。</b>点“展开全文”看完整内容。",
      "The bottom of the answer panel lists the rule passages of the image's region, each with the <b>original</b> and a <b>translation</b>: US passages are English originals with a Chinese translation; Chinese passages are Chinese originals with an English translation. <b>Translations are for reference; the original counts.</b> Click \"Show all\" for the full text.")}</li>
<li>${T("选好标线类型后，相关的条文会标“建议”并自动勾上。请读一遍，确认它<b>明确写到了这个行为</b>（能不能越线、能不能转向），并支持你的答案。",
      "After you choose the type, related passages are marked \"suggested\" and ticked. Read them and confirm each one <b>explicitly states the behavior</b> (whether you may cross, whether you may turn) and supports your answer.")}</li>
<li>${T("<b>只勾明确写出这个行为的条文。</b>只讲颜色、线长、一般定义而没说这个行为的，可以不勾。至少勾一条（期望证据为 full、类型不是“其他 / 看不到”时）。",
      "<b>Tick only passages that state the behavior.</b> Passages only about colour, line length or general definitions may stay unticked. Tick at least one when the expected evidence is full and the type is not Other / None visible.")}</li>
<li>${T("证据为 partial 或 insufficient 时不需要勾规则。", "With partial or insufficient evidence no rule is needed.")}</li></ul>`);

    // 12 unsure
    h += sec("g-unsure", toc[11][1], `<p>${T("出现下面任何一种情况，勾“不确定”并写一句原因，然后照常点“完成”。这张图会交给项目负责人裁决，<b>不算你错</b>：",
      "Tick \"Unsure\" and write one sentence in any of these cases, then click Done as usual. The project owner will decide; <b>it does not count against you</b>:")}</p><ul>
<li>${T("目标框有问题（框里有两种线、框住的不是标线、切掉了箭头头部）。", "The target box is wrong (two markings inside, no marking, arrow heads cut off).")}</li>
<li>${T("看不出颜色或虚实，导致类型定不了。", "You cannot tell the colour or pattern, so the type is unclear.")}</li>
<li>${T("规则表没有预填、黄色提示里也没有约定。", "An action is not prefilled and the yellow note gives no convention.")}</li>
<li>${T("你觉得这是路边线、施工临时标线等特殊情况。", "You think it is a road edge line, temporary work-zone marking or another special case.")}</li></ul>
<p>${T("原因写具体一点，例如“框里同时有黄实线和白虚线”“放大后仍看不出间隔”。<b>不要写具体地址或人名。</b>",
      "Be specific, e.g. \"the box holds a yellow solid and a white dashed line\", \"no gap visible even when zoomed\". <b>Do not write addresses or names.</b>")}</p>`);

    // 13 examples
    const ex = [];
    ex.push([T("例 1：右边的白虚线", "Example 1: white dashed line on the right"),
      scene({ lanes: 2, w: 190, h: 140, lines: [{ at: 1, kind: "white", style: "dashed" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 0, me: true, label: me, y: 115 }], boxes: [{ x: 86, y: 30, w: 18, h: 66, label: T("目标", "Target") }] }),
      T("我的车在左车道，框住的是我右边的白虚线，很清楚。", "Our car is in the left lane; the box holds the white broken line on our right, clearly visible."),
      [["marking_type", "white_dashed"], ["position", "right"], ["visibility", "V2"], ["cross_line", "allowed"], ["go_straight", "not_applicable"], ["turn_left", "not_applicable"],
        ["turn_right", "not_applicable"], ["u_turn", "not_applicable"], ["enter_center_lane_to_wait", "not_applicable"], ["rules", "US-3A.04-01, US-3B.06-05-06"]]]);
    ex.push([T("例 2：左边的双黄实线", "Example 2: double yellow line on the left"),
      scene({ lanes: 2, w: 190, h: 140, lines: [{ at: 1, kind: "yellow", style: "double" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], cars: [{ lane: 1, me: true, label: me, y: 115 }, { lane: 0, dir: "down", y: 20 }], boxes: [{ x: 80, y: 48, w: 30, h: 56, label: T("目标", "Target") }] }),
      T("双向道路，框住中间两条黄色实线，在我的左边。", "Two-way road; the box holds the two solid yellow lines in the middle, on our left."),
      [["marking_type", "yellow_double_solid"], ["position", "left"], ["visibility", "V2"], ["cross_line", "prohibited"], ["go_straight", "not_applicable"], ["turn_left", "not_applicable"],
        ["turn_right", "not_applicable"], ["u_turn", "not_applicable"], ["enter_center_lane_to_wait", "not_applicable"], ["rules", "US-3B.01-04"]]]);
    ex.push([T("例 3：我的车道里的直行+右转箭头", "Example 3: straight-and-right arrow in our lane"),
      scene({ lanes: 2, w: 190, h: 140, lines: [{ at: 1, kind: "white", style: "solid" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }], arrows: [{ lane: 1, type: "straight_right", y: 55 }], cars: [{ lane: 1, me: true, label: me, y: 118 }], boxes: [{ x: 99, y: 30, w: 42, h: 50, label: T("目标", "Target") }] }),
      T("箭头同时指向前方和右方，整个箭头都清楚。", "The arrow points ahead and right; the whole arrow is clear."),
      [["marking_type", "arrow"], ["arrow_type", "straight_right"], ["position", "in_ego_lane"], ["visibility", "V2"], ["cross_line", "not_applicable"], ["go_straight", "allowed"],
        ["turn_left", "prohibited"], ["turn_right", "allowed"], ["u_turn", "prohibited"], ["enter_center_lane_to_wait", "not_applicable"], ["rules", "US-3B.23-01, US-3B.23-08"]]]);
    ex.push([T("例 4：左边的双向左转车道", "Example 4: two-way left-turn lane on the left"),
      scene({ lanes: 3, w: 200, h: 140, lines: [{ at: 1, kind: "yellow", style: "solid_dashed", dashedSide: "right" }, { at: 2, kind: "yellow", style: "solid_dashed", dashedSide: "left" }, { at: 0, style: "edge" }, { at: 3, style: "edge" }],
        arrows: [{ lane: 1, type: "left", y: 40 }, { lane: 1, type: "left", dir: "down", y: 92 }], cars: [{ lane: 2, me: true, label: me, y: 115 }], boxes: [{ x: 60, y: 18, w: 66, h: 96, label: T("目标", "Target") }] }),
      T("中间车道两侧是“外实内虚”的黄线，里面有方向相反的左转箭头；我在它右边的车道。", "The centre lane has yellow edges (solid outside, broken inside) and opposite left-turn arrows; we are in the lane to its right."),
      [["marking_type", "two_way_left_turn_lane"], ["position", "left"], ["visibility", "V2"], ["cross_line", "not_applicable"], ["go_straight", "not_applicable"], ["turn_left", "allowed"],
        ["turn_right", "not_applicable"], ["u_turn", "not_applicable"], ["enter_center_lane_to_wait", "allowed"], ["rules", "US-3B.05-01, US-3B.23-01"]]]);
    ex.push([T("例 5：箭头头部被车挡住（V1，不能决定）", "Example 5: arrow head hidden by a car (V1, does not decide)"),
      scene({ lanes: 2, w: 190, h: 140, lines: [{ at: 1, kind: "white", style: "solid" }, { at: 0, style: "edge" }, { at: 2, style: "edge" }],
        extra: `<path d="M120 100 V70" stroke="${C.white}" stroke-width="4"/><rect x="100" y="30" width="40" height="44" rx="6" fill="${C.other}"/>`, cars: [{ lane: 1, me: true, label: me, y: 122 }], boxes: [{ x: 99, y: 28, w: 42, h: 76, label: T("目标", "Target") }] }),
      T("能看到这是一个箭头的杆，但头部被前车挡住，不知道指向哪里。", "You can see the shaft of an arrow, but its head is hidden by the car ahead, so you cannot tell where it points."),
      [["marking_type", "arrow"], ["arrow_type", ""], ["position", "in_ego_lane"], ["visibility", "V1"], ["behavior_decidable", "no"], ["cross_line", "not_applicable"],
        ["go_straight", "not_determined"], ["turn_left", "not_determined"], ["turn_right", "not_determined"], ["u_turn", "not_determined"], ["enter_center_lane_to_wait", "not_applicable"],
        ["rules", T("不用勾（证据为 partial）", "none needed (partial evidence)")]]]);
    h += sec("g-examples", toc[12][1], `<p>${T("下面是美国的例子（规则 ID 以页面上的建议为准）。", "These are US examples (rule IDs follow the suggestions on the page).")}</p>` +
      ex.map(([title, s, desc, rows]) => `<div class="gex"><h4>${title}</h4><div class="gex-row">${s}<div><p>${desc}</p>${answerTable(lang, rows)}</div></div></div>`).join(""));

    // 14 mistakes
    h += sec("g-mistakes", toc[13][1], `<ol class="gnum">
<li>${T("标了框外的线（比如框里是白虚线，却因为旁边有双黄线而选了禁止）。", "Labeling a line outside the box (e.g. the box holds a white dashed line, but you chose prohibited because of a double yellow line nearby).")}</li>
<li>${T("夜里把黄色看成白色，或反过来。先增亮，再和同画面里确定的线比较。", "Mixing up yellow and white at night. Brighten first, then compare with a line you are sure of.")}</li>
<li>${T("黄虚实线选错侧：看的是<b>靠近我的车</b>的那一条。", "Wrong side on a yellow solid + dashed line: what matters is the line <b>nearer our car</b>.")}</li>
<li>${T("双向左转车道里的箭头选成了“导向箭头”。", "Choosing \"Arrow\" for an arrow inside a two-way left-turn lane.")}</li>
<li>${T("V1 时忘了回答“能否决定”。", "Forgetting \"Does the visible part decide\" for V1.")}</li>
<li>${T("证据不足（partial / V0）时还选了允许或禁止。", "Choosing Allowed or Prohibited with partial evidence or V0.")}</li>
<li>${T("没检查预填就点了完成。预填只是建议，要对照图片确认。", "Clicking Done without checking the prefill. The prefill is only a suggestion; confirm it against the image.")}</li>
<li>${T("忘了画隐私框。", "Forgetting privacy boxes.")}</li>
<li>${T("和别人商量答案，或用 AI 工具查答案（都不允许）。", "Discussing answers with others or asking an AI tool (both not allowed).")}</li>
<li>${T("忘了导出结果，或清理了浏览器数据导致进度丢失。", "Forgetting to export, or clearing browser data and losing progress.")}</li></ol>`);

    // 15 save
    h += sec("g-save", toc[14][1], `<ul>
<li>${T("你的进度<b>自动保存在当前电脑的当前浏览器</b>里，关掉页面再打开 index.html 会自动恢复。", "Your progress is <b>saved automatically in this browser on this computer</b>; reopening index.html restores it.")}</li>
<li>${T("换电脑、换浏览器、使用无痕模式或清理浏览器数据，都会看不到之前的进度。所以<b>每天至少点一次“导出结果”</b>。需要接着做时，用“导入进度”把导出的文件读回来。",
      "A different computer or browser, private mode, or clearing browser data hides earlier progress. So <b>click \"Export results\" at least once a day</b>; use \"Import progress\" to load an exported file and continue.")}</li>
<li>${T("如果页面顶部出现红色提示，说明这个浏览器不能自动保存，要更频繁地导出。", "A red banner at the top means this browser cannot save automatically; export more often.")}</li>
<li>${T("全部做完后点“导出结果”，把下载的 <code>results_….json</code>（在“下载”文件夹里）通过微信 / 邮件 / 网盘发给项目负责人，然后删除整个标注文件夹。",
      "When everything is done, click \"Export results\" and send the downloaded <code>results_….json</code> (in your Downloads folder) to the project owner by WeChat / email / cloud drive, then delete the whole labeling folder.")}</li></ul>`);

    // 16 faq
    h += sec("g-faq", toc[15][1], `<dl class="gfaq">
<dt>${T("打开 index.html 后图片显示不出来？", "Images do not show after opening index.html?")}</dt><dd>${T("你可能是在压缩包里面直接打开的。先完整解压（Windows：右键 → 全部解压缩），再打开解压后文件夹里的 index.html。",
      "You probably opened it inside the zip. Unzip it fully first (Windows: right-click → Extract All), then open index.html in the unzipped folder.")}</dd>
<dt>${T("可以用手机标吗？", "Can I use a phone?")}</dt><dd>${T("不行，需要电脑和鼠标（画隐私框、放大镜）。Chrome、Edge、Safari、Firefox 都可以。", "No; you need a computer and a mouse (privacy boxes, magnifier). Chrome, Edge, Safari and Firefox all work.")}</dd>
<dt>${T("两张图看起来很像？", "Two images look alike?")}</dt><dd>${T("每张单独判断即可，答案可以相同。", "Judge each one on its own; the answers may be the same.")}</dd>
<dt>${T("练习题做错了有影响吗？", "Does a wrong practice answer matter?")}</dt><dd>${T("没有，练习只是帮你熟悉规则。看清楚参考答案为什么那样选。", "No. Practice only helps you learn; read why the reference answer is what it is.")}</dd>
<dt>${T("一张图大概要多久？", "How long per image?")}</dt><dd>${T("熟悉以后大约 1 分钟。前几张慢一点没关系。", "About a minute once you are used to it. The first few may take longer.")}</dd>
<dt>${T("点了完成后想改？", "Want to change an answer after Done?")}</dt><dd>${T("在列表里把筛选改成“全部”，点那张图，改完再点完成。", "Set the list filter to \"All\", click the image, change it, and click Done again.")}</dd></dl>`);

    // 17 glossary
    const gl = [["车道", "lane"], ["我的车道", "our lane / ego lane"], ["车道线（同向分界线）", "lane line"], ["中心线（对向分界线）", "centre line / center line"],
      ["实线", "solid line"], ["虚线", "broken line / dashed line"], ["双实线", "double solid line"], ["虚实线", "solid-dashed (broken-solid) line"],
      ["导向箭头", "lane-use arrow / turn-guide arrow"], ["双向左转车道", "two-way left-turn lane (TWLTL)"], ["越线 / 变道 / 超车", "cross the line / change lanes / overtake"],
      ["掉头", "U-turn"], ["路边线", "edge line"], ["人行横道", "crosswalk"], ["停止线", "stop line"], ["可见性", "visibility"], ["期望证据", "expected evidence"],
      ["适用规则", "accepted rule (passage)"], ["隐私框", "privacy box"], ["目标框", "target box"]];
    h += sec("g-glossary", toc[16][1], `<table class="gans">${gl.map(([a, b]) => `<tr><td>${a}</td><td>${b}</td></tr>`).join("")}</table>`);
    return h;
  }

  const PRINT_CSS = `body{font:14px/1.6 -apple-system,"PingFang SC","Segoe UI",sans-serif;color:#1d232a;background:#fff;max-width:900px;margin:24px auto;padding:0 18px}
h2{margin-top:0}h3{margin-top:28px;border-bottom:1px solid #ddd;padding-bottom:4px}h4{margin:16px 0 6px}code{font-size:12px;color:#555}
.gtoc ol{columns:2;list-style:none;padding-left:0}.gfigs,.gcards{display:flex;flex-wrap:wrap;gap:12px}.gfig{margin:0;width:180px;font-size:12px;text-align:center}.gfig.wide{width:auto}.gfig.small{width:76px}
.gcard{width:260px;border:1px solid #ddd;border-radius:8px;padding:8px;break-inside:avoid}.gcard p{font-size:12.5px}.gcard-h{font-weight:700;margin-bottom:6px}
table{border-collapse:collapse;font-size:12.5px;margin:8px 0}td,th{border:1px solid #ccc;padding:4px 6px;vertical-align:top}.ok{color:#137a3e}.no{color:#b3261e}.nd{color:#8a5a00}.na{color:#888}.tbd{background:#fff3cd}.ctd{color:#8a5a00;font-weight:700}
.knote{font-size:11px;color:#8a5a00}.gex{border:1px solid #ddd;border-radius:8px;padding:10px;margin:10px 0;break-inside:avoid}.gex-row{display:flex;gap:14px;flex-wrap:wrap}
.cyan{color:#0f8f80}.pink{color:#c2187a}.muted{color:#666}svg{background:#1c1f24;border-radius:6px}.gfaq dt{font-weight:700;margin-top:8px}`;
  function openPrintable(lang, ctx) {
    const w = window.open("", "_blank");
    if (!w) return;
    w.document.write(`<!doctype html><html lang="${lang === "zh" ? "zh-CN" : "en"}"><head><meta charset="utf-8"><title>${lang === "zh" ? "道路标线标注说明" : "Lane marking labeling guide"}</title><style>${PRINT_CSS}</style></head><body>${render(lang, ctx)}</body></html>`);
    w.document.close();
  }

  window.LANE_GUIDE = { render, openPrintable };
})();
