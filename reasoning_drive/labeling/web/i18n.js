/* Shared Chinese / English labels and the bilingual rule-passage list.
   Used by the local app (app.js) and the offline helper page (offline.js). */
"use strict";
(function () {
  const OPT = {
    zh: {
      marking: { white_dashed: "白虚线", white_solid: "白实线", white_double_solid: "双白实线", yellow_dashed: "黄虚线",
        yellow_solid: "单黄实线", yellow_double_solid: "双黄实线", yellow_solid_dashed: "黄虚实线（一虚一实）",
        two_way_left_turn_lane: "双向左转车道", arrow: "导向箭头", other: "其他标线", none_visible: "看不到 (V0)" },
      arrow: { straight: "↑ 直行", left: "↰ 左转", right: "↱ 右转", straight_left: "↑↰ 直行+左转", straight_right: "↑↱ 直行+右转",
        left_right: "↰↱ 左转+右转", u_turn: "⟲ 掉头", left_u_turn: "↰⟲ 左转+掉头", straight_u_turn: "↑⟲ 直行+掉头" },
      position: { left: "我的左边", in_ego_lane: "在我的车道里", right: "我的右边" },
      dashed: { ego_side: "虚线在我这一侧", far_side: "实线在我这一侧" },
      vis: { V2: "V2 清晰", V1: "V1 部分可见", V0: "V0 无可用证据" },
      decide: { yes: "能决定", no: "不能（只说类型）" },
      act: { cross_line: "越线（变道/超车）", go_straight: "直行", turn_left: "左转", turn_right: "右转", u_turn: "掉头",
        enter_center_lane_to_wait: "进中间车道等左转" },
      actv: { allowed: "允许", prohibited: "禁止", not_determined: "无法确定", not_applicable: "不适用" },
      evid: { full: "full · 完整回答", partial: "partial · 只说类型，行为不判断", insufficient: "insufficient · 证据不足" },
      field: { marking_type: "标线类型", arrow_type: "箭头类型", position: "位置", dashed_side: "虚线在哪一侧",
        visibility: "可见性", behavior_decidable: "能否决定行为", accepted_rule_ids: "适用规则" },
      region: { US: "美国", CN: "中国" },
    },
    en: {
      marking: { white_dashed: "White dashed", white_solid: "White solid", white_double_solid: "Double white solid",
        yellow_dashed: "Yellow dashed", yellow_solid: "Single yellow solid", yellow_double_solid: "Double yellow solid",
        yellow_solid_dashed: "Yellow solid + dashed", two_way_left_turn_lane: "Two-way left-turn lane", arrow: "Arrow",
        other: "Other marking", none_visible: "None visible (V0)" },
      arrow: { straight: "↑ Straight", left: "↰ Left", right: "↱ Right", straight_left: "↑↰ Straight + left",
        straight_right: "↑↱ Straight + right", left_right: "↰↱ Left + right", u_turn: "⟲ U-turn", left_u_turn: "↰⟲ Left + U-turn",
        straight_u_turn: "↑⟲ Straight + U-turn" },
      position: { left: "Left of our car", in_ego_lane: "In our lane", right: "Right of our car" },
      dashed: { ego_side: "Broken line on my side", far_side: "Solid line on my side" },
      vis: { V2: "V2 clear", V1: "V1 partly visible", V0: "V0 no usable evidence" },
      decide: { yes: "Decides", no: "Does not (type only)" },
      act: { cross_line: "Cross the line (change lane / overtake)", go_straight: "Go straight", turn_left: "Turn left",
        turn_right: "Turn right", u_turn: "U-turn", enter_center_lane_to_wait: "Enter centre lane to wait for a left turn" },
      actv: { allowed: "Allowed", prohibited: "Prohibited", not_determined: "Undetermined", not_applicable: "N/A" },
      evid: { full: "full · complete answer", partial: "partial · type only, behavior held back", insufficient: "insufficient · not enough evidence" },
      field: { marking_type: "Marking type", arrow_type: "Arrow type", position: "Position", dashed_side: "Broken-line side",
        visibility: "Visibility", behavior_decidable: "Decides behavior", accepted_rule_ids: "Rules" },
      region: { US: "United States", CN: "China" },
    },
  };

  const RULE_TXT = {
    zh: { suggested: "建议", original: "原文", translation: "译文（仅供参考）", more: "展开全文", less: "收起",
      lang_en: "English", lang_zh: "中文", expand_all: "全部展开", collapse_all: "全部收起" },
    en: { suggested: "suggested", original: "Original", translation: "Translation (reference only)", more: "Show all",
      less: "Show less", lang_en: "English", lang_zh: "Chinese", expand_all: "Expand all", collapse_all: "Collapse all" },
  };

  function esc(s) {
    return String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  }

  /* passages: [{rule_id, source, section, marking_type, marking_type_zh, text_en, text_zh, en_is_translation, zh_is_translation}]
     Renders every passage with its original text and its translation, one under the other. */
  function renderPassages(container, passages, lang, onToggle) {
    const R = RULE_TXT[lang] || RULE_TXT.en;
    container.innerHTML = "";
    for (const p of passages || []) {
      // the text in the page language first, the other language under it; each is marked original or translation
      const zh = { text: p.text_zh, lang: R.lang_zh, tr: !!p.zh_is_translation };
      const en = { text: p.text_en, lang: R.lang_en, tr: !!p.en_is_translation };
      const [first, second] = lang === "zh" ? [zh, en] : [en, zh];
      const type = lang === "zh" ? (p.marking_type_zh || p.marking_type) : p.marking_type;
      const div = document.createElement("div");
      div.className = "rule";
      div.dataset.rule = p.rule_id;
      div.innerHTML =
        `<label class="rhead"><input type="checkbox" value="${esc(p.rule_id)}"> <span class="rid">${esc(p.rule_id)}</span>` +
        `<span class="sug hidden">${esc(R.suggested)}</span></label>` +
        `<div class="rmeta">${esc(p.source || "")} ${esc(p.section || "")} · ${esc(type || "")}</div>` +
        (first.text ? `<div class="rtext"><span class="rtag">${esc(first.tr ? R.translation : R.original)} · ${esc(first.lang)}</span>${esc(first.text)}</div>` : "") +
        (second.text ? `<div class="rtext tr"><span class="rtag">${esc(second.tr ? R.translation : R.original)} · ${esc(second.lang)}</span>${esc(second.text)}</div>` : "") +
        `<button type="button" class="link rmore">${esc(R.more)}</button>`;
      const btn = div.querySelector(".rmore");
      btn.addEventListener("click", () => {
        const open = div.classList.toggle("open");
        btn.textContent = open ? R.less : R.more;
      });
      div.querySelector("input").addEventListener("change", (e) => onToggle && onToggle(p.rule_id, e.target.checked));
      container.appendChild(div);
    }
  }
  function syncPassages(container, ruleIds, suggestedIds) {
    const sel = new Set(ruleIds || []), sug = new Set(suggestedIds || []);
    for (const div of container.querySelectorAll(".rule")) {
      const id = div.dataset.rule;
      div.querySelector("input").checked = sel.has(id);
      div.querySelector(".sug").classList.toggle("hidden", !sug.has(id));
      div.classList.toggle("checked", sel.has(id));
    }
  }

  function loadLang(key, fallback) {
    try { const v = localStorage.getItem(key); if (v === "zh" || v === "en") return v; } catch (e) { /* no storage */ }
    return fallback || ((navigator.language || "").toLowerCase().startsWith("zh") ? "zh" : "en");
  }
  function saveLang(key, lang) { try { localStorage.setItem(key, lang); } catch (e) { /* no storage */ } }

  /* actions when the type is known but its detail is hidden (same as core.UNKNOWN_SUBTYPE) */
  const UNKNOWN_SUBTYPE = {
    arrow: { cross_line: "not_applicable", go_straight: "not_determined", turn_left: "not_determined", turn_right: "not_determined",
      u_turn: "not_determined", enter_center_lane_to_wait: "not_applicable" },
    yellow_solid_dashed: { cross_line: "not_determined", go_straight: "not_applicable", turn_left: "not_applicable",
      turn_right: "not_applicable", u_turn: "not_applicable", enter_center_lane_to_wait: "not_applicable" },
  };
  function evidenceOf(vis, dec) {
    if (vis === "V2") return "full";
    if (vis === "V1") return dec === "yes" ? "full" : dec === "no" ? "partial" : "";
    if (vis === "V0") return "insufficient";
    return "";
  }
  function ruleKey(f) {
    if (f.marking_type === "arrow") return f.arrow_type ? "arrow|" + f.arrow_type : "";
    if (f.marking_type === "yellow_solid_dashed") return f.dashed_side ? f.marking_type + "|" + f.dashed_side : "";
    return f.marking_type || "";
  }
  /* rule-table suggestion: {actions, rule_ids, note} or null */
  function suggestion(table, f, lang) {
    const ev = evidenceOf(f.visibility, f.behavior_decidable);
    const e = (table || {})[ruleKey(f)];
    if (!e) {
      if ((ev === "partial" || ev === "insufficient") && UNKNOWN_SUBTYPE[f.marking_type]) {
        return { actions: { ...UNKNOWN_SUBTYPE[f.marking_type] }, rule_ids: [], note: "" };
      }
      return null;
    }
    const acts = {};
    for (const [a, v] of Object.entries(e.actions)) acts[a] = (ev === "partial" || ev === "insufficient") && v !== "not_applicable" ? "not_determined" : v;
    return { actions: acts, rule_ids: e.rule_ids || [], note: (lang === "zh" ? e.note_zh : e.note) || e.note || "" };
  }

  window.LANE_I18N = { OPT, RULE_TXT, esc, renderPassages, syncPassages, loadLang, saveLang, evidenceOf, ruleKey, suggestion };
})();
