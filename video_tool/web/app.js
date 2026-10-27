/* Lane Labeler (local app): screen a video, keep frames, draw target boxes, label, adjudicate, share with helpers.
   Talks to video_tool/server.py. Every visible text comes from TXT (Chinese / English). */
"use strict";

const $ = (id) => document.getElementById(id);
const L = window.LANE_I18N;
const esc = L.esc;
const LANG_KEY = "lane-labeler-lang";

const TXT = {
  zh: {
    // ① pick images (dataset workspaces)
    tab_pick: "① 挑选图片", help_pick: "① 挑选图片",
    unkeep_img: "删除此图", title_label_img: "已收入的图（{n}）", empty_list_img: "这一类里没有图", sh_c_kept_img: "已收入的图",
    confirm_unkeep_img: "删除这张图、它的目标框和所有人对它的标注？之后可以在“① 挑选图片”里重新收入。",
    help_keys_pick: [["← / →", "上一张 / 下一张候选图"], ["[ / ]", "上一页 / 下一页"], ["1 – 5", "收入为：实线 / 虚线 / 黄色中心线 / 导向箭头 / 看不清"], ["L", "去标注刚收入的图"]],
    counts_img: "候选 {c} · 已收入 {k} · 没画框 {nb} · 等待 {w} · 冲突 {cf} · 完成 {d}",
    pk_filters: "筛选", pk_pool: "数据池", pool_dev: "开发", pool_test: "测试", pool_: "—",
    pk_pool_help: "开发池的图用来调提示词，测试池的图只在最后的正式比较里用。哪张图属于哪个池按 M3 6.5 节的哈希规则固定好了，不能混用。",
    pk_hint: "原有标注的线索", pk_all: "全部", pk_tod: "时间", pk_hide: "隐藏已收入的", pk_shuffle: "换一种顺序",
    "tod_daytime": "白天", "tod_night": "夜晚", "tod_dawn/dusk": "黄昏 / 清晨", "tod_undefined": "未标注",
    pk_quota: "配额（已收入 / 目标）", pk_other: "另有 {n} 张是其他类型，不计入配额。",
    pk_quota_help: "先把开发池收满（每格 6 张），用于第一次实验；测试池以后再挑。已经标好类型的图按标注的类型计数。",
    g_solid: "实线", g_dashed: "虚线", g_yellow: "黄色中心线", g_arrow: "导向箭头", g_degraded: "看不清", g_other: "其他",
    pk_keep_as: "收入为：", pk_kept: "已收入 ✓", pk_goto_label: "去标注 (L)",
    pk_picked: "已收入（{g}，{p}）。按 L 去标注，或继续挑下一张。", pk_over: "注意：这一格已经够了，多收的图也会保存。",
    pk_page: "第 {p} / {n} 页 · 共 {t} 张", pk_none: "没有符合条件的图，换个筛选试试。", pk_pick_first: "先在左边选一张图。",
    pk_info_tod: "时间", pk_info_weather: "天气", pk_info_scene: "场景", pk_info_cat: "CULane 类别", pk_info_clip: "片段",
    pk_info_hints: "原有标注里有", pk_boxes_note: "彩色框是数据集原有标注的位置（只是线索，类型要你自己看）。收入后它们会作为目标框建议。",
    pk_culane_note: "CULane 只标了本车道附近最多 4 条线的位置，没有颜色和实虚，而且看不见的线也画了。",
    pk_clip_full: "这个片段已有 {n} 张测试图（6.5 节规定每个片段最多 2 张）。",
    pk_help: "← → 换图 · [ ] 翻页 · 1–5 收入 · L 去标注",
    hint_label_img: "虚线框是根据数据集原有标注建议的目标框：点一下框就采用，也可以按 B 自己重画。车牌和人脸用隐私框。",
    lbl_hint: "建议",
    h_white_solid: "白实线", h_white_dashed: "白虚线", h_white_double_solid: "双白实线", h_yellow_solid: "单黄实线",
    h_yellow_dashed: "黄虚线", h_yellow_double_solid: "双黄实线", h_yellow_solid_dashed: "黄色虚实线",
    h_crosswalk: "有人行横道（路口，常有箭头）", h_no_lane: "没有车道线标注（可能看不清）", h_lane: "本车道边界",
    h_cu_normal: "普通", h_cu_crowd: "拥挤", h_cu_hlight: "强光", h_cu_shadow: "阴影", h_cu_noline: "无线（看不清）",
    h_cu_arrow: "箭头", h_cu_curve: "弯道", h_cu_cross: "路口", h_cu_night: "夜晚",
    tab_screen: "① 筛选视频", tab_label: "② 标注", tab_adjudicate: "③ 合并与裁决", tab_share: "④ 分发给同学", tab_recheck: "⑤ 盲复查",
    brighten: "画面增亮", guide: "标注说明", shortcuts: "快捷键", lang_other: "English", close: "关闭", got_it: "知道了", cancel: "取消",
    guide_print: "在新窗口打开（可打印）",
    tt_prev: "上一个 (←)", tt_play: "播放 / 暂停 (空格)", tt_next: "下一个 (→)", tt_speed: "播放速度（每秒显示几个画面）",
    speed2: "2 张/秒", speed4: "4 张/秒", speed8: "8 张/秒", play: "▶ 播放", pause: "❚❚ 暂停",
    fback: "−1 帧", ffwd: "+1 帧", tt_fback: "后退 1 帧 (,)", tt_ffwd: "前进 1 帧 (.)",
    keep: "★ 保存这帧 (K)", tt_keep: "保存这一帧 (K)", label_now: "去标注 (L)", tt_label_now: "马上标注刚保存的帧 (L)",
    show_all: "显示全部（包括停车）", only_paint: "只看有标线迹象", mask: "遮挡水印区域", tt_mask: "把行车记录仪叠加的日期、车速、GPS 涂黑",
    mask_help: "在画面上拖动鼠标框出水印（日期 / 车速 / GPS），可以框多个；点击框可以选中，按 Delete 删除。", mask_save: "保存遮挡区域",
    b_frame: "帧 {n}", b_fine: "逐帧微调中", b_stop: "停车", b_crawl: "缓行（与上一张很像）", b_dark: "很暗", b_blur: "可能模糊",
    b_yellow: "有黄色", b_kept: "已保存 · {s}", b_near: "3 秒内已有保存的帧",
    tl_stop: "停车/缓行", tl_paint: "标线迹象", tl_yellow: "黄色", tl_kept: "已保存",
    no_frames: "没有可看的画面：试试勾选“显示全部”。",
    kept_ok: "已保存 {t}（{id}）。按 L 马上标注，或继续筛选。",
    kept_near: "已保存 {t}。注意：{near} 也保存过（3 秒内）。如果是同一个标线，到“② 标注”里删掉不清楚的那张。",
    kept_fail: "保存失败：", masks_ok: "遮挡区域已保存（{n} 个）。已保存的 {m} 帧也重新生成了。", masks_fail: "保存遮挡区域失败：",
    no_last: "还没有刚保存的帧：先按 K 保存。",
    tool_box: "▭ 目标框 (B)", tt_box: "画目标框：要问模型的那一条标线 (B)", tool_privacy: "▨ 隐私框 (P)", tt_privacy: "画隐私框：车牌、人脸 (P)",
    delete_sel: "删除选中", tt_del: "删除选中的隐私框 (Delete)", loupe: "放大镜",
    form_empty: "左边选一帧开始。先在“① 筛选视频”里按 K 保存帧。",
    lg_marking: "输出 1 · 标线类型", lg_arrow: "箭头类型", lg_dashed: "虚线在哪一侧", lg_position: "位置（相对我的车）",
    lg_visibility: "可见性", decidable_q: "可见部分能决定行为吗？", evidence: "期望证据", lg_actions: "输出 2 · 动作",
    prefill: "按规则表重新预填", lg_rules: "可接受的规则（原文 + 译文）", lg_notes: "备注（这一帧）", notes_ph: "不要写具体地址；公开仓库可见",
    expand_all: "全部展开", collapse_all: "全部收起",
    save_done: "完成 ✓ 下一张", save_final: "保存为最终答案", save_draft: "存草稿", save_box: "只存目标框", tt_save_box: "只保存目标框，交给同学标注",
    exclude: "排除", tt_exclude: "保留记录但不用于实验", unkeep: "删除此帧",
    note_unset: "规则表没有预填：{x}。请按标注说明里的项目约定选择。",
    st_kept: "没画框", st_waiting: "等待标注", st_conflict: "冲突", st_done: "最终完成", st_excluded: "排除", st_pending: "待复查", st_draft: "草稿",
    f_todo_box: "未画目标框", f_todo_mine: "我还没标", f_all: "全部", f_final: "最终完成", f_conflict: "冲突（待裁决）", f_waiting: "等待第二人",
    title_recheck: "复查样本（{n}）", title_adj: "裁决（{n}）", title_label: "已保存的帧（{n}）",
    li_nobox: "没画框", li_mine_done: "我：已标", li_mine_draft: "我：草稿", li_mine_none: "我：未标", li_anns: "{n} 份标注",
    empty_recheck: "没有复查样本", empty_list: "这一类里没有帧",
    counts: "可看 {c} · 已保存 {k} · 没画框 {nb} · 等待 {w} · 冲突 {cf} · 完成 {d}", counts_re: " · 复查 {a}/{b}",
    fin_waiting: "最终答案还需要独立标注（每张需要 {n} 份）。到“④ 分发给同学”生成标注包。",
    fin_conflict: "你的答案和同学的不一致（或有人标了“不确定”）→ 到“③ 合并与裁决”处理。",
    fin_agreed: "最终答案已确定：两人一致。", fin_single: "最终答案已确定。", fin_adj: "最终答案已确定（裁决）。",
    fin_kept: "还没有目标框。", fin_excluded: "这一帧已排除。",
    saved: "已保存。", saved_st: "已保存：{s}", not_done: "还不能算完成，已存为草稿：", warn_look: "有提醒，请看一眼。按 ] 去下一张。",
    save_fail: "保存失败：", all_done_cat: "这一类全部处理完了。",
    confirm_unkeep: "删除这一帧、它的目标框和所有人对它的标注？之后可以在筛选里重新保存。", del_fail: "删除失败：",
    you: "你", src: "来源：", src_agreed: "两人一致", src_single: "单人", src_adj: "你的裁决", no_ann: "还没有完成的标注。",
    n_drafts: "（有 {n} 份草稿）", more_drafts: "另有 {n} 份草稿未计入。", unsure: "不确定", item: "项目", rules_col: "规则 ID",
    adopt: "采用 {w}", adj_note: "裁决理由（会记录在标签文件里）", adj_note_ph: "例如：放大后能看到虚线间隔",
    adj_edit: "修改后采用", adj_exclude: "排除这一帧", adj_reopen: "撤销裁决",
    adj_excluded: "已排除。", adj_reopened: "已重新打开，按标注重新判断。", adj_edited: "已保存为最终答案。", adj_adopted: "已采用 {w} 的答案。",
    adj_edit_hint: "修改后点“保存为最终答案”（按 Esc 或“取消”返回比较）。",
    hint_recheck: "盲复查：只看图和目标框重新标一遍，不显示你之前的标签。完成后用 export 命令比较两次的一致率（风险 R2）。",
    hint_adj: "比较各人的独立标注：红色的行是不一致的地方。采用其中一份、修改后采用，或排除这一帧。同学只显示代号。",
    hint_label: "① 画目标框：框住要问模型的那一条标线或那个箭头（同学看到的就是这个框）。② 可以自己标注，也可以“只存目标框”交给同学。车牌和人脸用隐私框。",
    lbl_target: "目标", lbl_privacy: "隐私", boot_fail: "启动失败：{e}<br>请看终端里的提示。",
    // ④ share
    sh_title: "分发给同学", sh_intro: "每张图需要 2 个人独立标注（你自己标的算 1 份）。在这里生成每个同学的标注包、查看进度、导入他们发回的结果。",
    sh_flow: ["在“② 标注”里给每一帧画<b>目标框</b>；先自己完整标 6～10 张，它们会变成同学的<b>练习题</b>。",
      "填写同学名字，点<b>生成标注包</b>：每人一个 zip，工具会自动分配，保证每张图有 2 个不同的人标。",
      "通过微信 / 邮件 / 网盘把 zip <b>只发给对应的那个人</b>，附上下面的说明文字。",
      "同学解压后双击 <b>index.html</b> 标注，标完把 <b>results_….json</b> 发回给你。",
      "把收到的文件拖进下面的“收回结果”。一致的直接成为最终答案，不一致的到 <b>③ 合并与裁决</b> 处理。"],
    sh_c_kept: "已保存的帧", sh_c_boxed: "已画目标框", sh_c_need: "还需要的标注份数（未发出）", sh_c_out: "已发出、还没收回的份数",
    sh_c_mine: "你已标完（可做练习题）", sh_c_conflict: "冲突（待裁决）", sh_c_done: "最终完成",
    sh_warn_open: "<b>发包前请先定好这几处约定。</b>规则条文没有说清楚的地方，规则表没有预填；如果不统一，两个人很可能各标各的。请修改 <code>config/action_rules.json</code> 里对应的值和说明（note / note_zh），或告诉 Claude 你的决定：",
    sh_warn_nopractice: "你还没有自己完整标完任何一张，所以标注包里不会有练习题。建议先在“② 标注”里标 6～10 张（点“完成”）。",
    sh_warn_nobox: "还有 {n} 帧没有画目标框，它们不会被分发。",
    sh_make_h: "① 生成标注包", sh_names: "同学名字（用逗号或换行分隔；真名只保存在你的硬盘上，仓库里只用代号 ann01…）",
    sh_names_ph: "例如：Alice, Bob, 小陈", sh_practice: "每人练习题", sh_max: "每人最多几张", sh_max_ph: "不限", sh_make: "生成标注包",
    sh_known: "以前的同学：", sh_need_names: "请先填写至少一个同学名字。", sh_making: "正在生成…",
    sh_made_ok: "已生成 {n} 个标注包，在下面这个文件夹里：", sh_open_packages: "打开标注包文件夹", sh_made_none: "这次没有生成新的标注包。",
    sh_tmpl_h: "发给同学的说明（可以直接复制）：", sh_copy: "复制", sh_copied: "已复制",
    sh_tmpl: "嗨，能帮我标一下道路标线吗？大约 {m} 分钟。\n1. 先把 zip 解压（Windows：右键 → 全部解压缩）。\n2. 双击里面的 index.html，用电脑浏览器打开（不用联网、不用注册）。\n3. 先看“标注说明”，做完练习题再开始。右上角可以切换中文 / English。\n4. 标完点右上角“导出结果”，把下载的 results_….json 文件发给我。\n图片请不要转发，标完删掉文件夹。谢谢！\n\nHi! Could you help me label some road markings? About {m} minutes.\n1. Unzip the file (Windows: right-click → Extract All).\n2. Double-click index.html; it opens in your browser (no internet or account needed).\n3. Read the Guide and do the practice items first. The button at the top right switches between English and Chinese.\n4. When you finish, click \"Export results\" and send me the downloaded results_….json file.\nPlease don't share the images, and delete the folder afterwards. Thank you!",
    sh_sent_h: "② 已发出的标注包", sh_none_sent: "还没有发出任何标注包。",
    th_pkg: "标注包", th_helper: "同学", th_created: "生成时间", th_items: "张数", th_status: "状态", th_done: "已完成", th_unsure: "不确定", th_practice: "练习得分", th_file: "文件",
    ps_sent: "已发出", ps_partial: "部分收回", ps_complete: "已收回",
    sh_import_h: "③ 收回结果", sh_drop: "把同学发回的 results_….json 文件拖到这里，或", sh_pick: "选择文件",
    sh_import_folder: "导入 returned 文件夹里的全部文件", sh_open_returned: "打开 returned 文件夹", sh_log: "详细日志（英文）",
    sh_importing: "正在导入…", sh_imported: "导入完成：{f} 个文件。最终答案现在：完成 {d}，冲突 {c}，等待 {w}。",
    sh_imported_file: "{file}：{code} 完成 {done}，草稿 {draft}，不确定 {unsure}", sh_go_adj: "去处理冲突", sh_import_none: "没有找到可以导入的结果文件。",
    sh_open_fail: "没能自动打开文件夹，请在 Finder 里打开：", sh_not_json: "只能导入 .json 文件。",
    conv_key_arrow: "箭头 · {a}", conv_region: "{r}",
    help_title: "快捷键", help_screen: "① 筛选视频", help_label: "② 标注",
    help_keys_screen: [["← / →", "上一个 / 下一个画面"], ["Shift + ← / →", "后退 / 前进 10 秒"], [", / .", "后退 / 前进 1 帧（选最清楚的那一帧）"],
      ["空格", "播放 / 暂停"], ["K", "保存当前帧"], ["L", "马上去标注刚保存的帧"], ["A", "显示 / 隐藏停车片段"]],
    help_keys_label: [["B / P", "目标框 / 隐私框工具"], ["Delete", "删除选中的隐私框"], ["⌘/Ctrl + Enter", "完成并跳到下一张"],
      ["⌘/Ctrl + S", "存草稿"], ["[ / ]", "上一张 / 下一张"], ["Esc", "取消正在画的框"]],
    help_one: "同一个标线只保存一帧", help_one_p: "车开近一个箭头时它会连续出现好几秒。只保存看得最清楚的那一帧；3 秒内再保存会提醒你。",
    vis_tip: "V2 清晰：整条标线都看得清。\nV1 部分可见：有磨损、遮挡或太暗。线要能看出颜色和线型（虚线至少一整段线加一个间隔；实线连续长度超过一段线加一个间隔；双线两条都可见），箭头要能看到箭头头部，才算“能决定”。\nV0 没有可用证据：几乎看不到标线。",
  },
  en: {
    // ① pick images (dataset workspaces)
    tab_pick: "① Pick images", help_pick: "① Pick images",
    unkeep_img: "Remove image", title_label_img: "Picked images ({n})", empty_list_img: "No images in this group", sh_c_kept_img: "Picked images",
    confirm_unkeep_img: "Remove this image, its target box and everyone's labels for it? You can pick it again in ① Pick images.",
    help_keys_pick: [["← / →", "previous / next candidate"], ["[ / ]", "previous / next page"], ["1 – 5", "pick as solid / dashed / yellow centre line / arrow / degraded"], ["L", "label the image you just picked"]],
    counts_img: "Candidates {c} · picked {k} · no box {nb} · waiting {w} · conflicts {cf} · final {d}",
    pk_filters: "Filter", pk_pool: "Pool", pool_dev: "Dev", pool_test: "Test", pool_: "—",
    pk_pool_help: "Development images are for tuning the prompt; test images are only used in the final comparison. Each image's pool is fixed by the hash rule in Milestone 3, section 6.5.",
    pk_hint: "Hint from the dataset labels", pk_all: "All", pk_tod: "Time of day", pk_hide: "Hide picked images", pk_shuffle: "Shuffle",
    "tod_daytime": "Day", "tod_night": "Night", "tod_dawn/dusk": "Dawn / dusk", "tod_undefined": "Not labeled",
    pk_quota: "Quota (picked / target)", pk_other: "{n} more images are other types and do not count.",
    pk_quota_help: "Fill the development pool first (6 per cell) for the first experiment; pick test images later. Labeled images count under their labeled type.",
    g_solid: "Solid line", g_dashed: "Dashed line", g_yellow: "Yellow centre line", g_arrow: "Arrow", g_degraded: "Degraded", g_other: "Other",
    pk_keep_as: "Pick as:", pk_kept: "Picked ✓", pk_goto_label: "Label it (L)",
    pk_picked: "Picked ({g}, {p}). Press L to label it, or pick the next one.", pk_over: "Note: this cell is full already; the extra image is kept anyway.",
    pk_page: "Page {p} / {n} · {t} images", pk_none: "No image matches. Try another filter.", pk_pick_first: "Choose an image on the left.",
    pk_info_tod: "Time", pk_info_weather: "Weather", pk_info_scene: "Scene", pk_info_cat: "CULane category", pk_info_clip: "Clip",
    pk_info_hints: "Dataset labels contain", pk_boxes_note: "Coloured boxes show the dataset's own labels (hints only; judge the type yourself). After picking they become target-box suggestions.",
    pk_culane_note: "CULane only gives the positions of up to 4 lines near our lane, with no colour or pattern, and draws lines even where they cannot be seen.",
    pk_clip_full: "This clip already has {n} test images (section 6.5 allows at most 2 per clip).",
    pk_help: "← → change image · [ ] page · 1–5 pick · L label",
    hint_label_img: "Dashed boxes are target boxes suggested from the dataset's labels: click one to use it, or press B and draw your own. Use privacy boxes for plates and faces.",
    lbl_hint: "suggested",
    h_white_solid: "White solid", h_white_dashed: "White dashed", h_white_double_solid: "Double white solid", h_yellow_solid: "Single yellow solid",
    h_yellow_dashed: "Yellow dashed", h_yellow_double_solid: "Double yellow solid", h_yellow_solid_dashed: "Yellow solid + dashed",
    h_crosswalk: "Crosswalk (intersection, arrows likely)", h_no_lane: "No lane labels (maybe degraded)", h_lane: "Our lane's boundary",
    h_cu_normal: "Normal", h_cu_crowd: "Crowded", h_cu_hlight: "Glare", h_cu_shadow: "Shadow", h_cu_noline: "No line (degraded)",
    h_cu_arrow: "Arrow", h_cu_curve: "Curve", h_cu_cross: "Crossroad", h_cu_night: "Night",
    tab_screen: "① Screen video", tab_label: "② Label", tab_adjudicate: "③ Merge & decide", tab_share: "④ Share with helpers", tab_recheck: "⑤ Blind re-check",
    brighten: "Brighten", guide: "Guide", shortcuts: "Shortcuts", lang_other: "中文", close: "Close", got_it: "Got it", cancel: "Cancel",
    guide_print: "Open in a new window (printable)",
    tt_prev: "Previous (←)", tt_play: "Play / pause (Space)", tt_next: "Next (→)", tt_speed: "Playback speed (frames shown per second)",
    speed2: "2 / s", speed4: "4 / s", speed8: "8 / s", play: "▶ Play", pause: "❚❚ Pause",
    fback: "−1 frame", ffwd: "+1 frame", tt_fback: "Back one frame (,)", tt_ffwd: "Forward one frame (.)",
    keep: "★ Keep frame (K)", tt_keep: "Keep this frame (K)", label_now: "Label it (L)", tt_label_now: "Label the frame you just kept (L)",
    show_all: "Show all (incl. stops)", only_paint: "Only frames with paint", mask: "Mask overlay", tt_mask: "Black out the dash-cam date, speed and GPS overlay",
    mask_help: "Drag on the image to box the overlay (date / speed / GPS); several boxes are fine. Click a box to select it, Delete removes it.", mask_save: "Save masks",
    b_frame: "frame {n}", b_fine: "single-frame step", b_stop: "stopped", b_crawl: "crawling (like the last one)", b_dark: "very dark", b_blur: "maybe blurry",
    b_yellow: "yellow paint", b_kept: "kept · {s}", b_near: "a kept frame within 3 s",
    tl_stop: "stopped / crawling", tl_paint: "paint", tl_yellow: "yellow", tl_kept: "kept",
    no_frames: "Nothing to show: try \"Show all\".",
    kept_ok: "Kept {t} ({id}). Press L to label it now, or keep screening.",
    kept_near: "Kept {t}. Note: {near} was kept too (within 3 s). If it is the same marking, delete the less clear one in ② Label.",
    kept_fail: "Could not keep the frame: ", masks_ok: "Masks saved ({n}). The {m} kept frames were re-created.", masks_fail: "Could not save the masks: ",
    no_last: "No frame kept yet: press K first.",
    tool_box: "▭ Target box (B)", tt_box: "Draw the target box: the marking the model will be asked about (B)", tool_privacy: "▨ Privacy box (P)", tt_privacy: "Draw privacy boxes: plates, faces (P)",
    delete_sel: "Delete selected", tt_del: "Delete the selected privacy box (Delete)", loupe: "Magnifier",
    form_empty: "Pick a frame on the left. Keep frames first in ① Screen video (press K).",
    lg_marking: "Output 1 · Marking type", lg_arrow: "Arrow type", lg_dashed: "Broken-line side", lg_position: "Position (relative to our car)",
    lg_visibility: "Visibility", decidable_q: "Does the visible part decide the behavior?", evidence: "Expected evidence", lg_actions: "Output 2 · Actions",
    prefill: "Prefill from rule table", lg_rules: "Accepted rules (original + translation)", lg_notes: "Notes (this frame)", notes_ph: "No addresses; the repository is public",
    expand_all: "Expand all", collapse_all: "Collapse all",
    save_done: "Done ✓ next", save_final: "Save as final", save_draft: "Save draft", save_box: "Save box only", tt_save_box: "Save only the target box; helpers label it",
    exclude: "Exclude", tt_exclude: "Keep the record but leave it out of the experiment", unkeep: "Delete frame",
    note_unset: "Not prefilled: {x}. Use the project convention in the guide.",
    st_kept: "no box", st_waiting: "waiting", st_conflict: "conflict", st_done: "final", st_excluded: "excluded", st_pending: "to re-check", st_draft: "draft",
    f_todo_box: "No target box", f_todo_mine: "Not labeled by me", f_all: "All", f_final: "Final", f_conflict: "Conflicts (to decide)", f_waiting: "Waiting for a 2nd label",
    title_recheck: "Re-check sample ({n})", title_adj: "Decide ({n})", title_label: "Kept frames ({n})",
    li_nobox: "no box", li_mine_done: "me: done", li_mine_draft: "me: draft", li_mine_none: "me: —", li_anns: "{n} labels",
    empty_recheck: "No re-check sample", empty_list: "No frames in this group",
    counts: "To view {c} · kept {k} · no box {nb} · waiting {w} · conflicts {cf} · final {d}", counts_re: " · re-check {a}/{b}",
    fin_waiting: "The final label needs independent labels ({n} per frame). Make packages in ④ Share with helpers.",
    fin_conflict: "Your answer differs from a helper's (or someone was unsure) → decide it in ③ Merge & decide.",
    fin_agreed: "Final label set: both agree.", fin_single: "Final label set.", fin_adj: "Final label set (decided).",
    fin_kept: "No target box yet.", fin_excluded: "This frame is excluded.",
    saved: "Saved.", saved_st: "Saved: {s}", not_done: "Not done yet, saved as draft:", warn_look: "Please read the notes. Press ] for the next frame.",
    save_fail: "Could not save: ", all_done_cat: "Everything in this group is done.",
    confirm_unkeep: "Delete this frame, its target box and everyone's labels for it? You can keep it again while screening.", del_fail: "Could not delete: ",
    you: "you", src: "Source: ", src_agreed: "both agree", src_single: "single labeler", src_adj: "your decision", no_ann: "No finished labels yet.",
    n_drafts: " ({n} drafts)", more_drafts: "{n} more drafts are not counted.", unsure: "unsure", item: "Field", rules_col: "Rule IDs",
    adopt: "Use {w}", adj_note: "Reason (stored in the label file)", adj_note_ph: "e.g. the gaps are visible when zoomed in",
    adj_edit: "Edit, then use", adj_exclude: "Exclude this frame", adj_reopen: "Undo decision",
    adj_excluded: "Excluded.", adj_reopened: "Reopened; decided again from the labels.", adj_edited: "Saved as the final label.", adj_adopted: "Used {w}'s answer.",
    adj_edit_hint: "Edit, then click \"Save as final\" (Esc or Cancel goes back to the comparison).",
    hint_recheck: "Blind re-check: label again from the image and the target box only; your earlier labels are hidden. export compares the two (risk R2).",
    hint_adj: "Compare the independent labels: red rows differ. Use one of them, edit and use, or exclude the frame. Helpers are shown by code.",
    hint_label: "① Draw the target box around the one marking or arrow the model will be asked about (helpers see this box). ② Label it yourself, or \"Save box only\" for helpers. Plates and faces get privacy boxes.",
    lbl_target: "Target", lbl_privacy: "Privacy", boot_fail: "Could not start: {e}<br>See the terminal for details.",
    sh_title: "Share with helpers", sh_intro: "Every frame needs 2 independent labels (yours counts as one). Make each helper's package here, follow the progress, and import what they send back.",
    sh_flow: ["In ② Label draw a <b>target box</b> on every frame; label 6–10 frames yourself first: they become the helpers' <b>practice items</b>.",
      "Enter the helpers' names and click <b>Make packages</b>: one zip per person, assigned so every frame gets 2 different labelers.",
      "Send each zip <b>only to its helper</b> (WeChat / email / cloud drive) with the message below.",
      "The helper unzips it, double-clicks <b>index.html</b>, labels, and sends back <b>results_….json</b>.",
      "Drop the returned files below. Agreeing labels become final; differences go to <b>③ Merge & decide</b>."],
    sh_c_kept: "Kept frames", sh_c_boxed: "With target box", sh_c_need: "Labels still needed (not sent)", sh_c_out: "Labels sent, not back yet",
    sh_c_mine: "Labeled by you (practice pool)", sh_c_conflict: "Conflicts (to decide)", sh_c_done: "Final",
    sh_warn_open: "<b>Settle these conventions before sending packages.</b> Where the rule text is not clear, the rule table is not prefilled; without a convention two people will often answer differently. Edit the values and notes (note / note_zh) in <code>config/action_rules.json</code>, or tell Claude your decision:",
    sh_warn_nopractice: "You have not finished labeling any frame yourself, so the packages will have no practice items. Label 6–10 frames in ② Label first (click Done).",
    sh_warn_nobox: "{n} kept frames have no target box; they are not shared.",
    sh_make_h: "① Make packages", sh_names: "Helper names (comma or new line; real names stay on your drive, the repository only has codes ann01…)",
    sh_names_ph: "e.g. Alice, Bob, Chen", sh_practice: "Practice items each", sh_max: "At most per helper", sh_max_ph: "no limit", sh_make: "Make packages",
    sh_known: "Earlier helpers:", sh_need_names: "Enter at least one helper name.", sh_making: "Working…",
    sh_made_ok: "{n} packages made, in this folder:", sh_open_packages: "Open the packages folder", sh_made_none: "No new packages were made.",
    sh_tmpl_h: "Message for the helpers (copy and paste):", sh_copy: "Copy", sh_copied: "Copied",
    sh_tmpl: "嗨，能帮我标一下道路标线吗？大约 {m} 分钟。\n1. 先把 zip 解压（Windows：右键 → 全部解压缩）。\n2. 双击里面的 index.html，用电脑浏览器打开（不用联网、不用注册）。\n3. 先看“标注说明”，做完练习题再开始。右上角可以切换中文 / English。\n4. 标完点右上角“导出结果”，把下载的 results_….json 文件发给我。\n图片请不要转发，标完删掉文件夹。谢谢！\n\nHi! Could you help me label some road markings? About {m} minutes.\n1. Unzip the file (Windows: right-click → Extract All).\n2. Double-click index.html; it opens in your browser (no internet or account needed).\n3. Read the Guide and do the practice items first. The button at the top right switches between English and Chinese.\n4. When you finish, click \"Export results\" and send me the downloaded results_….json file.\nPlease don't share the images, and delete the folder afterwards. Thank you!",
    sh_sent_h: "② Packages sent", sh_none_sent: "No packages sent yet.",
    th_pkg: "Package", th_helper: "Helper", th_created: "Made", th_items: "Frames", th_status: "Status", th_done: "Done", th_unsure: "Unsure", th_practice: "Practice", th_file: "File",
    ps_sent: "sent", ps_partial: "partly back", ps_complete: "back",
    sh_import_h: "③ Import results", sh_drop: "Drop the returned results_….json files here, or", sh_pick: "Choose files",
    sh_import_folder: "Import every file in the returned folder", sh_open_returned: "Open the returned folder", sh_log: "Detailed log",
    sh_importing: "Importing…", sh_imported: "Imported {f} files. Final labels now: final {d}, conflicts {c}, waiting {w}.",
    sh_imported_file: "{file}: {code} done {done}, draft {draft}, unsure {unsure}", sh_go_adj: "Decide the conflicts", sh_import_none: "No results files found.",
    sh_open_fail: "Could not open the folder automatically. Open it in Finder:", sh_not_json: "Only .json files can be imported.",
    conv_key_arrow: "Arrow · {a}", conv_region: "{r}",
    help_title: "Shortcuts", help_screen: "① Screen video", help_label: "② Label",
    help_keys_screen: [["← / →", "previous / next view"], ["Shift + ← / →", "back / forward 10 s"], [", / .", "back / forward one frame (pick the clearest)"],
      ["Space", "play / pause"], ["K", "keep this frame"], ["L", "label the frame you just kept"], ["A", "show / hide stops"]],
    help_keys_label: [["B / P", "target box / privacy box tool"], ["Delete", "delete the selected privacy box"], ["⌘/Ctrl + Enter", "done and next"],
      ["⌘/Ctrl + S", "save draft"], ["[ / ]", "previous / next frame"], ["Esc", "cancel the box being drawn"]],
    help_one: "One frame per marking", help_one_p: "An arrow stays in view for several seconds as the car approaches. Keep only the clearest frame; keeping another within 3 s shows a warning.",
    vis_tip: "V2 clear: the whole marking is easy to see.\nV1 partly visible: worn, covered or too dark. It decides the behavior only if a line shows its colour and pattern (dashed: one full dash and one gap; solid: unbroken for longer than a dash plus a gap; double: both lines), or an arrow shows its head.\nV0 no usable evidence: almost nothing visible.",
  },
};

const S = {
  lang: L.loadLang(LANG_KEY, "zh"),
  data: null, view: "screen", mode: "label", labels: new Map(), recheck: new Map(), anns: new Map(),
  shown: [], pos: 0, curFrame: 0, playing: false, lastKept: null, maskMode: false, masks: [], maskSel: -1,
  selId: null, tool: "box", box: null, privacy: [], privSel: -1, drawing: null, hover: null, form: {}, sug: null, adjEditing: false,
  share: null, hints: [],
};

function t(key, vars) {
  if (S.data && S.data.kind === "images" && TXT.zh[key + "_img"] !== undefined) key += "_img";
  let s = (TXT[S.lang] && TXT[S.lang][key]) ?? TXT.zh[key] ?? key;
  if (typeof s !== "string") return s;
  for (const [k, v] of Object.entries(vars || {})) s = s.split("{" + k + "}").join(v);
  return s;
}
const O = (group) => L.OPT[S.lang][group];
const SEP = () => (S.lang === "zh" ? "、" : ", ");
const status = (s) => t("st_" + s);

// ------------------------------------------------------------------ helpers
async function api(path, body) {
  const opt = body === undefined ? {} : { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) };
  const r = await fetch(path, opt);
  const j = await r.json().catch(() => ({ error: `HTTP ${r.status}` }));
  if (!r.ok || j.error && j.ok === undefined) throw new Error(j.error || `HTTP ${r.status}`);
  return j;
}
function fmtTime(s) {
  s = Math.max(0, s);
  const m = Math.floor(s / 60), r = s - m * 60;
  return `${String(m).padStart(2, "0")}:${r.toFixed(1).padStart(4, "0")}`;
}
function fps() { return S.data.video.fps; }
function srcW() { return S.data.video.width; }
function srcH() { return S.data.video.height; }
function curRow() { return S.selId ? S.labels.get(S.selId) : null; }
function outW() { const r = curRow(); return (r && Number(r.width)) || S.data.output.width; }
function outH() { const r = curRow(); return (r && Number(r.height)) || S.data.output.height; }
function msg(el, text, cls) { el.textContent = text; el.className = "msg " + (cls || ""); }
function isTyping(e) {
  const x = e.target;
  return x && (x.tagName === "TEXTAREA" || (x.tagName === "INPUT" && (x.type === "text" || x.type === "number")) || x.tagName === "SELECT");
}
function sizeCanvas(c, w, h) {
  const dpr = window.devicePixelRatio || 1;
  c.width = Math.round(w * dpr); c.height = Math.round(h * dpr);
  c.style.width = w + "px"; c.style.height = h + "px";
  c.getContext("2d").setTransform(dpr, 0, 0, dpr, 0, 0);
}

// ------------------------------------------------------------------ language
function applyStatic() {
  document.documentElement.lang = S.lang === "zh" ? "zh-CN" : "en";
  for (const el of document.querySelectorAll("[data-t]")) el.textContent = t(el.dataset.t);
  for (const el of document.querySelectorAll("[data-tt]")) el.title = t(el.dataset.tt);
  for (const el of document.querySelectorAll("[data-tp]")) el.placeholder = t(el.dataset.tp);
  $("lang-btn").textContent = t("lang_other");
  $("guide-lang").textContent = t("lang_other");
  $("play-btn").textContent = S.playing ? t("pause") : t("play");
  $("vis-help").title = t("vis_tip");
  $("rules-expand").textContent = t("expand_all");
  renderHelp();
}
function setLang(lang) {
  S.lang = lang;
  L.saveLang(LANG_KEY, lang);
  applyStatic();
  buildForm();
  if (IMG()) { renderPickFilters(); renderPickDetail(); if (PK.res) renderPickGrid(); }
  if (S.view === "screen") { if (!IMG()) { renderBadges(); drawTimeline(); } }
  else if (S.view === "share") renderShare();
  else switchView(S.view);
  updateCounts();
  if (!$("guide").classList.contains("hidden")) openGuide();
}
function renderHelp() {
  const dl = (rows) => "<dl>" + rows.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("") + "</dl>";
  const first = S.data && S.data.kind === "images" ? [t("help_pick"), t("help_keys_pick")] : [t("help_screen"), t("help_keys_screen")];
  $("help-body").innerHTML = `<h2>${esc(t("help_title"))}</h2><div class="cols"><div><h3>${esc(first[0])}</h3>${dl(first[1])}</div>` +
    `<div><h3>${esc(t("help_label"))}</h3>${dl(t("help_keys_label"))}</div></div><h3>${esc(t("help_one"))}</h3><p>${esc(t("help_one_p"))}</p>`;
}

// ------------------------------------------------------------------ boot
async function boot() {
  applyStatic();
  S.data = await api("/api/state");
  ingestState(S.data);
  const tr = S.data.trip;
  $("tripinfo").textContent = IMG()
    ? `${S.data.set.dataset} · ${tr.region} · ${tr.trip_id}`
    : `${tr.trip_id} · ${tr.region} · ${tr.time_of_day} · ${tr.weather} · split=${tr.split}`;
  $("tripinfo").title = IMG() ? `${tr.trip_id} — ${S.data.workspace}` : $("tripinfo").textContent;
  if (S.data.recheck_mode) $("tab-recheck").classList.remove("hidden");
  buildForm();
  bindEvents();
  applyBrightness();
  if (IMG()) {
    setupPick();
    applyStatic();
    switchView("screen");
    renderPickFilters();
    loadCands();
    renderKeptList();
    updateCounts();
    if (S.data.recheck_mode) switchView("recheck");
    window.addEventListener("resize", () => { layoutLabel(); drawPickOverlay(); });
    return;
  }
  computeShown();
  layoutScreen();
  const first = S.shown.length ? S.data.scan[S.shown[0]].frame_index : 0;
  gotoFrame(first);
  renderKeptList();
  updateCounts();
  if (S.data.recheck_mode) switchView("recheck");
  window.addEventListener("resize", () => { layoutScreen(); layoutLabel(); drawTimeline(); });
  if (!S.data.scan_summary || !S.data.scan_summary.candidates) msg($("screen-msg"), t("no_frames"), "warn");
}
function ingestState(d) {
  S.labels = new Map(d.labels.map((r) => [r.image_id, r]));
  S.recheck = new Map(d.recheck.map((r) => [r.image_id, r]));
  S.anns = new Map(d.annotations.map((a) => [`${a.image_id}|${a.annotator}`, a]));
  S.masks = (d.trip.masks || []).map((m) => m.slice());
}
async function refreshState() {
  const d = await api("/api/state");
  S.data.labels = d.labels; S.data.annotations = d.annotations; S.data.recheck = d.recheck;
  ingestState({ ...d, trip: S.data.trip });
  updateCounts(); if (!IMG()) drawTimeline();
}

// ------------------------------------------------------------------ ① screening
function paintCut() {
  const vals = S.data.scan.filter((r) => r.candidate).map((r) => r.paint).sort((a, b) => a - b);
  return vals.length ? vals[Math.floor(vals.length * 0.4)] : 0;
}
function computeShown() {
  const all = $("show-all").checked, onlyPaint = $("only-paint").checked;
  const cut = onlyPaint ? paintCut() : -1;
  S.shown = [];
  S.data.scan.forEach((r, i) => {
    if (!all && !r.candidate) return;
    if (onlyPaint && r.paint < cut && r.yellow <= 0.01) return;
    S.shown.push(i);
  });
}
function nearestShown(frame) {
  if (!S.shown.length) return 0;
  let lo = 0, hi = S.shown.length - 1;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (S.data.scan[S.shown[mid]].frame_index < frame) lo = mid + 1; else hi = mid;
  }
  if (lo > 0) {
    const a = S.data.scan[S.shown[lo - 1]].frame_index, b = S.data.scan[S.shown[lo]].frame_index;
    if (Math.abs(a - frame) < Math.abs(b - frame)) lo -= 1;
  }
  return lo;
}
function sampleNear(frame) {
  const scan = S.data.scan;
  let best = scan[0], d = Infinity;
  const stepF = scan.length > 1 ? scan[1].frame_index - scan[0].frame_index : 1;
  const guess = Math.max(0, Math.min(scan.length - 1, Math.round((frame - scan[0].frame_index) / stepF)));
  for (let i = Math.max(0, guess - 2); i <= Math.min(scan.length - 1, guess + 2); i++) {
    const dd = Math.abs(scan[i].frame_index - frame);
    if (dd < d) { d = dd; best = scan[i]; }
  }
  return best;
}
function previewWidth() {
  const w = $("screen-stage").clientWidth * (window.devicePixelRatio || 1);
  return Math.min(srcW(), Math.max(320, Math.ceil(w / 160) * 160));
}
function previewUrl(frame) { return `/api/preview?f=${frame}&w=${previewWidth()}&v=${S.data.mask_version}`; }
const preloaders = [];
function preloadAhead() {
  for (let k = 1; k <= 5; k++) {
    const i = S.pos + k;
    if (i >= S.shown.length) break;
    const im = preloaders[k - 1] || (preloaders[k - 1] = new Image());
    im.src = previewUrl(S.data.scan[S.shown[i]].frame_index);
  }
}
let imgLoaded = Promise.resolve();
function gotoFrame(frame, keepPos) {
  const last = S.data.video.frame_count ? S.data.video.frame_count - 1 : Infinity;
  frame = Math.max(0, Math.min(last, Math.round(frame)));
  S.curFrame = frame;
  if (!keepPos) S.pos = nearestShown(frame);
  const img = $("screen-img");
  imgLoaded = new Promise((res) => { img.onload = res; img.onerror = res; });
  img.src = previewUrl(frame);
  renderBadges();
  drawTimeline();
  preloadAhead();
}
function step(delta) {
  if (!S.shown.length) return false;
  const sc = S.data.scan, cur = S.curFrame, n = S.shown.length;
  let p = Math.max(0, Math.min(n - 1, S.pos));
  if (delta > 0) {
    while (p < n - 1 && sc[S.shown[p]].frame_index <= cur) p++;
    if (sc[S.shown[p]].frame_index <= cur) return false;
  } else {
    while (p > 0 && sc[S.shown[p]].frame_index >= cur) p--;
    if (sc[S.shown[p]].frame_index >= cur) return false;
  }
  S.pos = p;
  gotoFrame(sc[S.shown[p]].frame_index, true);
  return true;
}
function jumpSeconds(sec) { gotoFrame(S.curFrame + sec * fps()); }
function keptAt(frame) {
  for (const r of S.labels.values()) if (Number(r.frame_index) === frame) return r;
  return null;
}
function keptNear(frame, sec = 3) {
  return [...S.labels.values()].filter((r) => Math.abs(Number(r.frame_index) - frame) / fps() < sec && Number(r.frame_index) !== frame);
}
function renderBadges() {
  if (!S.data) return;
  const s = sampleNear(S.curFrame);
  const b = [];
  b.push(`<span class="badge">${fmtTime(S.curFrame / fps())}</span>`);
  b.push(`<span class="badge">${esc(t("b_frame", { n: S.curFrame }))}</span>`);
  if (s.frame_index !== S.curFrame) b.push(`<span class="badge">${esc(t("b_fine"))}</span>`);
  if (s.stationary) b.push(`<span class="badge stop">${esc(t("b_stop"))}</span>`);
  else if (s.dup) b.push(`<span class="badge stop">${esc(t("b_crawl"))}</span>`);
  if (s.dark) b.push(`<span class="badge warn">${esc(t("b_dark"))}</span>`);
  if (s.blurry) b.push(`<span class="badge warn">${esc(t("b_blur"))}</span>`);
  if (s.yellow > 0.01) b.push(`<span class="badge">${esc(t("b_yellow"))}</span>`);
  const k = keptAt(S.curFrame);
  if (k) b.push(`<span class="badge kept">${esc(t("b_kept", { s: status(k.label_status) }))}</span>`);
  else if (keptNear(S.curFrame).length) b.push(`<span class="badge warn">${esc(t("b_near"))}</span>`);
  b.push(`<span class="badge">${S.shown.length ? S.pos + 1 : 0} / ${S.shown.length}</span>`);
  $("screen-badges").innerHTML = b.join("");
}
function layoutScreen() {
  if (!S.data || S.view !== "screen") return;
  const view = $("view-screen");
  const others = ["timeline", "mask-bar", "screen-msg"].map((id) => $(id).offsetHeight).reduce((a, b) => a + b, 0)
    + view.querySelector(".controls").offsetHeight;
  const maxH = view.clientHeight - others - 20 - 4 * 8;
  const maxW = view.clientWidth - 28;
  const r = Math.min(maxW / srcW(), maxH / srcH());
  const w = Math.max(200, Math.floor(srcW() * r)), h = Math.max(112, Math.floor(srcH() * r));
  const st = $("screen-stage");
  st.style.width = w + "px"; st.style.height = h + "px";
  sizeCanvas($("screen-overlay"), w, h);
  drawScreenOverlay();
}
function drawTimeline() {
  if (!S.data) return;
  const c = $("timeline");
  const w = c.parentElement.clientWidth - 28, h = 84;
  if (w <= 0) return;
  if (c.width !== Math.round(w * (window.devicePixelRatio || 1)) || c.style.height !== h + "px") sizeCanvas(c, w, h);
  const ctx = c.getContext("2d");
  ctx.clearRect(0, 0, w, h);
  const scan = S.data.scan;
  if (!scan.length) return;
  const t0 = scan[0].time_s, t1 = scan[scan.length - 1].time_s || 1;
  const X = (x) => ((x - t0) / Math.max(1e-6, t1 - t0)) * (w - 2) + 1;
  const maxPaint = Math.max(1e-6, ...scan.map((r) => r.paint));
  const bw = Math.max(1, (w / scan.length) * 1.2);
  for (const r of scan) {
    const x = X(r.time_s);
    if (r.stationary) { ctx.fillStyle = "#5a3434"; ctx.fillRect(x, 2, bw, 12); }
    else if (r.dup) { ctx.fillStyle = "#3a3f47"; ctx.fillRect(x, 2, bw, 12); }
    const ph = (r.paint / maxPaint) * 34;
    ctx.fillStyle = r.candidate ? "#4fb3ff" : "#2c3f52";
    ctx.fillRect(x, 50 - ph, bw, ph);
    if (r.yellow > 0.002) { ctx.fillStyle = `rgba(255, 196, 0, ${Math.min(1, r.yellow * 20)})`; ctx.fillRect(x, 53, bw, 9); }
  }
  for (const r of S.labels.values()) {
    const x = X(Number(r.time_s));
    ctx.fillStyle = { done: "#39c27a", waiting: "#4fb3ff", conflict: "#ff6b6b", excluded: "#777", kept: "#c9d1d9" }[r.label_status] || "#c9d1d9";
    ctx.beginPath(); ctx.moveTo(x, 66); ctx.lineTo(x - 5, 80); ctx.lineTo(x + 5, 80); ctx.closePath(); ctx.fill();
  }
  const cx = X(S.curFrame / fps());
  ctx.fillStyle = "#ff5c5c"; ctx.fillRect(cx - 1, 0, 2, h);
  ctx.fillStyle = "#9aa3ad"; ctx.font = "10px -apple-system, sans-serif"; ctx.textAlign = "right";
  ctx.fillText(t("tl_stop"), w - 4, 12); ctx.fillText(t("tl_paint"), w - 4, 26); ctx.fillText(t("tl_yellow"), w - 4, 61); ctx.fillText(t("tl_kept"), w - 4, 78);
}
function timelineFrame(ev) {
  const c = $("timeline"), rect = c.getBoundingClientRect();
  const scan = S.data.scan, t0 = scan[0].time_s, t1 = scan[scan.length - 1].time_s;
  return Math.round((t0 + ((ev.clientX - rect.left) / rect.width) * (t1 - t0)) * fps());
}
async function playLoop() {
  while (S.playing) {
    const started = performance.now();
    if (!step(1)) { setPlaying(false); break; }
    await imgLoaded;
    const wait = 1000 / Number($("speed").value) - (performance.now() - started);
    if (wait > 0) await new Promise((r) => setTimeout(r, wait));
  }
}
function setPlaying(on) {
  S.playing = on;
  $("play-btn").textContent = on ? t("pause") : t("play");
  if (on) playLoop();
}
async function keepCurrent() {
  if (S.maskMode) return;
  setPlaying(false);
  try {
    const res = await api("/api/keep", { frame_index: S.curFrame });
    S.labels.set(res.row.image_id, res.row);
    S.lastKept = res.row.image_id;
    const near = res.near.map((id) => fmtTime(Number(S.labels.get(id)?.time_s || 0)));
    if (near.length) msg($("screen-msg"), t("kept_near", { t: fmtTime(S.curFrame / fps()), near: near.join(SEP()) }), "warn");
    else msg($("screen-msg"), t("kept_ok", { t: fmtTime(S.curFrame / fps()), id: res.row.image_id }), "ok");
    renderKeptList(); updateCounts(); renderBadges(); drawTimeline();
  } catch (e) { msg($("screen-msg"), t("kept_fail") + e.message, "err"); }
}
function setMaskMode(on) {
  S.maskMode = on;
  setPlaying(false);
  $("mask-bar").classList.toggle("hidden", !on);
  $("screen-overlay").style.cursor = on ? "crosshair" : "default";
  if (!on) { S.masks = (S.data.trip.masks || []).map((m) => m.slice()); S.maskSel = -1; }
  layoutScreen();
}
function drawScreenOverlay() {
  const c = $("screen-overlay"), ctx = c.getContext("2d");
  const w = c.clientWidth, h = c.clientHeight;
  ctx.clearRect(0, 0, w, h);
  if (!S.maskMode) return;
  const sx = w / srcW(), sy = h / srcH();
  const rects = S.masks.slice();
  if (S.drawing && S.drawing.where === "mask") rects.push(S.drawing.rect);
  rects.forEach((m, i) => {
    const [x1, y1, x2, y2] = m;
    ctx.fillStyle = "rgba(255, 209, 102, .25)"; ctx.fillRect(x1 * sx, y1 * sy, (x2 - x1) * sx, (y2 - y1) * sy);
    ctx.strokeStyle = i === S.maskSel ? "#fff" : "#ffd166"; ctx.lineWidth = 2; ctx.strokeRect(x1 * sx, y1 * sy, (x2 - x1) * sx, (y2 - y1) * sy);
  });
}
async function saveMasks() {
  try {
    const res = await api("/api/masks", { masks: S.masks });
    S.data.trip.masks = res.masks;
    S.data.mask_version = res.mask_version;
    setMaskMode(false);
    gotoFrame(S.curFrame, true);
    renderKeptList();
    msg($("screen-msg"), t("masks_ok", { n: res.masks.length, m: res.rerendered }), "ok");
  } catch (e) { msg($("screen-msg"), t("masks_fail") + e.message, "err"); }
}

// ------------------------------------------------------------------ ① pick images (dataset workspaces)
const PK = { pool: "dev", hint: "", tod: "", hide: true, page: 0, seed: "6216", size: 24, res: null, sel: -1, det: null, quota: null, busy: false };
const HINT_GROUP = { white_solid: "solid", white_double_solid: "solid", white_dashed: "dashed", yellow_solid: "yellow", yellow_dashed: "yellow",
  yellow_double_solid: "yellow", yellow_solid_dashed: "yellow", crosswalk: "arrow", no_lane: "degraded", cu_arrow: "arrow", cu_noline: "degraded" };
const HINT_COLOR = { solid: "#4fc3f7", dashed: "#9ccc65", yellow: "#ffd54f", arrow: "#ff8a65", degraded: "#ce93d8", lane: "#36e0c8" };
function IMG() { return !!(S.data && S.data.kind === "images"); }
function isCulane() { return IMG() && S.data.set.dataset === "CULane"; }
const groupName = (g) => t("g_" + (g || "other"));
const poolName = (p) => t("pool_" + (p || ""));
const hintName = (h) => { const k = "h_" + h; const v = t(k); return v === k ? h : v; };
function defaultGroup(hints) {
  if (PK.hint && HINT_GROUP[PK.hint]) return HINT_GROUP[PK.hint];
  for (const h of hints || []) if (HINT_GROUP[h]) return HINT_GROUP[h];
  return "";
}
function setupPick() {
  $("bright").value = "1";
  applyBrightness();
  $("tab-screen").dataset.t = "tab_pick";
  $("tab-screen").textContent = t("tab_pick");
  $("view-screen").classList.add("hidden");
  PK.quota = S.data.quota;
  $("pk-pool").innerHTML = "";
  for (const p of ["dev", "test"]) {
    const b = document.createElement("button");
    b.type = "button"; b.dataset.v = p; b.textContent = poolName(p);
    b.addEventListener("click", () => { PK.pool = p; PK.page = 0; renderPickFilters(); loadCands(); });
    $("pk-pool").appendChild(b);
  }
  $("pk-hint").addEventListener("change", () => { PK.hint = $("pk-hint").value; PK.page = 0; loadCands(); });
  $("pk-tod").addEventListener("change", () => { PK.tod = $("pk-tod").value; PK.page = 0; loadCands(); });
  $("pk-hide").addEventListener("change", () => { PK.hide = $("pk-hide").checked; PK.page = 0; loadCands(); });
  $("pk-shuffle").addEventListener("click", () => { PK.seed = String(Math.floor(Math.random() * 1e9)); PK.page = 0; loadCands(); });
  $("pk-prev").addEventListener("click", () => pickPage(-1));
  $("pk-next").addEventListener("click", () => pickPage(1));
  for (const b of $("pk-keep").querySelectorAll("button[data-g]")) b.addEventListener("click", () => pickKeep(b.dataset.g));
  $("pk-label").addEventListener("click", pickGotoLabel);
  $("pk-img").addEventListener("load", drawPickOverlay);
}
function renderPickFilters() {
  for (const b of $("pk-pool").querySelectorAll("button")) { b.classList.toggle("on", b.dataset.v === PK.pool); b.textContent = poolName(b.dataset.v); }
  const f = (S.data.facets.hints || {})[PK.pool] || {};
  const hints = Object.keys(f).filter((h) => h !== "*").sort((a, b) => (f[b] - f[a]));
  $("pk-hint").innerHTML = `<option value="">${esc(t("pk_all"))} (${f["*"] || 0})</option>` +
    hints.map((h) => `<option value="${esc(h)}"${h === PK.hint ? " selected" : ""}>${esc(hintName(h))} (${f[h]})</option>`).join("");
  const tods = Object.keys(S.data.facets.time_of_day || {});
  $("pk-tod-row").classList.toggle("hidden", isCulane() || !tods.length);
  $("pk-tod").innerHTML = `<option value="">${esc(t("pk_all"))}</option>` +
    tods.map((x) => `<option value="${esc(x)}"${x === PK.tod ? " selected" : ""}>${esc(t("tod_" + x) === "tod_" + x ? x : t("tod_" + x))}</option>`).join("");
  $("pk-hide").checked = PK.hide;
  for (const b of $("pk-keep").querySelectorAll("button[data-g]")) b.querySelector(".gname").textContent = groupName(b.dataset.g);
  renderQuota();
}
function renderQuota() {
  const q = PK.quota;
  if (!q) return;
  const cell = (have, target) => `<td class="${target && have >= target ? "full" : have > target ? "over" : ""}">${have}<span class="muted"> / ${target}</span></td>`;
  $("pk-quota").innerHTML = `<tr><th></th><th>${esc(poolName("dev"))}</th><th>${esc(poolName("test"))}</th></tr>` +
    q.rows.map((r) => `<tr><td>${esc(groupName(r.group))}</td>${cell(r.dev_have, r.dev_target)}${cell(r.test_have, r.test_target)}</tr>`).join("") +
    `<tr class="tot"><td></td>${cell(q.totals.dev.have, q.totals.dev.target)}${cell(q.totals.test.have, q.totals.test.target)}</tr>`;
  $("pk-other").textContent = q.other ? t("pk_other", { n: q.other }) : "";
}
async function loadCands(keepSel) {
  const qs = new URLSearchParams({ pool: PK.pool, hint: PK.hint, tod: PK.tod, hide: PK.hide ? "1" : "0", page: PK.page, size: PK.size, seed: PK.seed });
  try { PK.res = await api("/api/candidates?" + qs.toString()); }
  catch (e) { msg($("pk-msg"), e.message, "err"); return; }
  PK.page = PK.res.page;
  if (!keepSel || PK.sel >= PK.res.items.length) PK.sel = PK.res.items.length ? 0 : -1;
  renderPickGrid();
  if (PK.sel >= 0) selectCand(PK.sel); else clearPickDetail();
}
function renderPickGrid() {
  const r = PK.res;
  $("pk-pageinfo").textContent = t("pk_page", { p: r.page + 1, n: r.pages, t: r.total });
  $("pk-prev").disabled = r.page <= 0; $("pk-next").disabled = r.page >= r.pages - 1;
  const g = $("pk-grid");
  g.innerHTML = "";
  if (!r.items.length) { g.innerHTML = `<div class="muted pad">${esc(t("pk_none"))}</div>`; return; }
  r.items.forEach((it, i) => {
    const d = document.createElement("div");
    d.className = "pk-cell" + (i === PK.sel ? " sel" : "") + (it.kept ? " kept" : "");
    d.dataset.i = i;
    const chips = it.hints.slice(0, 3).map((h) => `<span class="chip" style="border-color:${HINT_COLOR[HINT_GROUP[h]] || "#555"}">${esc(hintName(h))}</span>`).join("");
    d.innerHTML = `<img loading="lazy" alt="" src="/api/cand_image?c=${encodeURIComponent(it.cand_id)}&w=320">` +
      `<div class="cap">${it.kept ? `<b class="ok">✓</b> ` : ""}${chips}</div>`;
    d.addEventListener("click", () => selectCand(i));
    g.appendChild(d);
  });
}
function clearPickDetail() {
  PK.det = null;
  $("pk-img").removeAttribute("src");
  $("pk-info").innerHTML = `<p class="muted">${esc(t("pk_pick_first"))}</p>`;
  drawPickOverlay();
}
async function selectCand(i) {
  PK.sel = i;
  for (const c of $("pk-grid").querySelectorAll(".pk-cell")) c.classList.toggle("sel", Number(c.dataset.i) === i);
  const sel = $("pk-grid").querySelector(".pk-cell.sel");
  if (sel) sel.scrollIntoView({ block: "nearest" });
  const it = PK.res.items[i];
  if (!it) return;
  $("pk-img").src = `/api/cand_image?c=${encodeURIComponent(it.cand_id)}&w=1280`;
  try { PK.det = await api("/api/candidate?c=" + encodeURIComponent(it.cand_id)); } catch (e) { msg($("pk-msg"), e.message, "err"); return; }
  if (PK.res.items[PK.sel] !== it) return;
  renderPickDetail();
}
function renderPickDetail() {
  const d = PK.det;
  if (!d) return;
  const row = (k, v) => v ? `<tr><td>${esc(t(k))}</td><td>${esc(v)}</td></tr>` : "";
  const tod = d.time_of_day ? (t("tod_" + d.time_of_day) === "tod_" + d.time_of_day ? d.time_of_day : t("tod_" + d.time_of_day)) : "";
  const hints = d.hints.map((h) => `<span class="chip" style="border-color:${HINT_COLOR[HINT_GROUP[h]] || "#555"}">${esc(hintName(h))}</span>`).join(" ");
  let warn = "";
  if (d.pool === "test" && isCulane() && d.clip_test_kept >= 2 && !d.kept) warn = `<div class="warnbox">${esc(t("pk_clip_full", { n: d.clip_test_kept }))}</div>`;
  $("pk-info").innerHTML = `<div class="pk-title mono">${esc(d.rel)}</div><table class="pk-meta">` +
    `<tr><td>${esc(t("pk_pool"))}</td><td><b>${esc(poolName(d.pool))}</b></td></tr>` +
    row("pk_info_tod", tod) + row("pk_info_weather", d.weather === "undefined" ? "" : d.weather) + row("pk_info_scene", d.scene === "undefined" ? "" : d.scene) +
    row("pk_info_cat", d.category ? hintName("cu_" + d.category) : "") + (isCulane() ? row("pk_info_clip", d.clip_id) : "") +
    `<tr><td>${esc(t("pk_info_hints"))}</td><td>${hints || "—"}</td></tr></table>` + warn +
    `<p class="muted small">${esc(isCulane() ? t("pk_culane_note") : t("pk_boxes_note"))}</p>`;
  const dg = defaultGroup(d.hints);
  for (const b of $("pk-keep").querySelectorAll("button[data-g]")) {
    b.classList.toggle("suggest", b.dataset.g === dg && !d.kept);
    b.disabled = !!d.kept;
  }
  $("pk-kept").classList.toggle("hidden", !d.kept);
  $("pk-label").classList.toggle("hidden", !d.kept);
  drawPickOverlay();
}
function drawPickOverlay() {
  const img = $("pk-img"), c = $("pk-overlay");
  const w = img.clientWidth, h = img.clientHeight;
  sizeCanvas(c, w, h);
  const ctx = c.getContext("2d");
  ctx.clearRect(0, 0, w, h);
  const d = PK.det;
  if (!d || !img.getAttribute("src") || !w) return;
  const sx = w / d.width, sy = h / d.height;
  for (const [hint, boxes] of Object.entries(d.boxes || {})) {
    const col = hint === "lane" ? HINT_COLOR.lane : (HINT_COLOR[HINT_GROUP[hint]] || "#bbb");
    for (const b of boxes) {
      ctx.strokeStyle = col; ctx.lineWidth = 2; ctx.setLineDash([6, 4]);
      ctx.strokeRect(b[0] * sx, b[1] * sy, (b[2] - b[0]) * sx, (b[3] - b[1]) * sy);
      ctx.setLineDash([]); ctx.fillStyle = col; ctx.font = "11px sans-serif";
      ctx.fillText(hintName(hint), b[0] * sx + 3, Math.max(11, b[1] * sy - 3));
    }
  }
}
function pickPage(delta) {
  if (!PK.res) return;
  const p = PK.res.page + delta;
  if (p < 0 || p >= PK.res.pages) return;
  PK.page = p; loadCands();
}
function pickMove(delta) {
  if (!PK.res || !PK.res.items.length) return;
  const i = PK.sel + delta;
  if (i < 0) { if (PK.res.page > 0) { PK.page = PK.res.page - 1; loadCands().then(() => selectCand(PK.res.items.length - 1)); } return; }
  if (i >= PK.res.items.length) { pickPage(1); return; }
  selectCand(i);
}
async function pickKeep(group) {
  const d = PK.det;
  if (!d || d.kept || PK.busy) return;
  PK.busy = true;
  try {
    const res = await api("/api/pick", { cand_id: d.cand_id, group });
    S.labels.set(res.row.image_id, res.row);
    S.lastKept = res.row.image_id;
    PK.quota = res.quota; renderQuota(); updateCounts();
    d.kept = res.row.image_id;
    const it = PK.res.items[PK.sel]; if (it) it.kept = res.row.image_id;
    const cellEl = $("pk-grid").querySelector(`.pk-cell[data-i="${PK.sel}"]`);
    if (cellEl) { cellEl.classList.add("kept"); cellEl.querySelector(".cap").insertAdjacentHTML("afterbegin", `<b class="ok">✓</b> `); }
    renderPickDetail();
    msg($("pk-msg"), t("pk_picked", { g: groupName(group), p: poolName(res.row.split) }) + ((res.warnings || []).includes("over_quota") ? " " + t("pk_over") : ""),
      (res.warnings || []).length ? "warn" : "ok");
  } catch (e) { msg($("pk-msg"), e.message, "err"); }
  finally { PK.busy = false; }
}
function pickGotoLabel() {
  const id = (PK.det && PK.det.kept) || S.lastKept;
  if (!id) return;
  switchView("label"); openImage(id);
}
function pickKey(e) {
  const k = e.key;
  if (k === "ArrowRight") { e.preventDefault(); pickMove(1); }
  else if (k === "ArrowLeft") { e.preventDefault(); pickMove(-1); }
  else if (k === "]" || k === "PageDown") { e.preventDefault(); pickPage(1); }
  else if (k === "[" || k === "PageUp") { e.preventDefault(); pickPage(-1); }
  else if (/^[1-5]$/.test(k)) { e.preventDefault(); pickKeep(S.data.groups[Number(k) - 1]); }
  else if (k === "l" || k === "L") pickGotoLabel();
}

// ------------------------------------------------------------------ ② labeling form
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
  if (!S.data) return;
  const sc = S.data.schema;
  segment($("f-marking"), only(sc.marking_type, O("marking")), (v) => setField("marking_type", v));
  segment($("f-arrow"), only(sc.arrow_type, O("arrow")), (v) => setField("arrow_type", v));
  segment($("f-dashed"), only(sc.dashed_side, O("dashed")), (v) => setField("dashed_side", v));
  segment($("f-position"), only(sc.position, O("position")), (v) => setField("position", v));
  segment($("f-visibility"), only(sc.visibility, O("vis")), (v) => setField("visibility", v));
  segment($("f-decidable"), O("decide"), (v) => setField("behavior_decidable", v));
  $("f-visibility").title = t("vis_tip");
  const tbl = $("f-actions");
  tbl.innerHTML = "";
  for (const a of sc.actions) {
    const tr = document.createElement("tr"); tr.dataset.action = a;
    const td1 = document.createElement("td"); td1.textContent = O("act")[a] || a; td1.title = a;
    const td2 = document.createElement("td");
    const seg = document.createElement("div"); seg.className = "seg";
    segment(seg, only(sc.action_values, O("actv")), (v) => { S.form.actions[a] = v; renderForm(); }, false);
    td2.appendChild(seg); tr.append(td1, td2); tbl.appendChild(tr);
  }
  L.renderPassages($("f-rules"), S.data.passages, S.lang, (id, on) => {
    const set = new Set(S.form.rule_ids || []);
    if (on) set.add(id); else set.delete(id);
    S.form.rule_ids = [...set];
    L.syncPassages($("f-rules"), S.form.rule_ids, (suggestion(S.form) || {}).rule_ids);
  });
  $("rules-expand").textContent = t("expand_all");
  if (S.form && S.form.actions) renderForm();
}
const evidenceOf = L.evidenceOf;
function suggestion(f) { return L.suggestion(S.data.rules_table, f, S.lang); }
function applySuggestion(withRules) {
  const sug = suggestion(S.form);
  S.sug = sug;
  for (const a of S.data.schema.actions) S.form.actions[a] = sug ? sug.actions[a] || "" : "";
  if (!sug) return;
  if (withRules && S.mode !== "recheck") S.form.rule_ids = sug.rule_ids.filter((id) => S.data.passages.some((p) => p.rule_id === id));
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
  const f = S.form;
  if (!f || !f.actions) return;
  setSeg($("f-marking"), f.marking_type); setSeg($("f-arrow"), f.arrow_type); setSeg($("f-dashed"), f.dashed_side);
  setSeg($("f-position"), f.position); setSeg($("f-visibility"), f.visibility); setSeg($("f-decidable"), f.behavior_decidable);
  $("fs-arrow").classList.toggle("hidden", f.marking_type !== "arrow");
  $("fs-dashed").classList.toggle("hidden", !(S.data.schema.needs_dashed_side || []).includes(f.marking_type));
  $("fs-decidable").classList.toggle("hidden", f.visibility !== "V1");
  const ev = evidenceOf(f.visibility, f.behavior_decidable);
  $("f-evidence").textContent = O("evid")[ev] || "—";
  const sug = suggestion(f);
  S.sug = sug;
  for (const tr of $("f-actions").querySelectorAll("tr")) {
    const a = tr.dataset.action, v = f.actions[a] || "";
    setSeg(tr.querySelector(".seg"), v);
    tr.classList.toggle("unset", !v);
    tr.classList.toggle("suggested-diff", !!(sug && sug.actions[a] && v && sug.actions[a] !== v));
  }
  const empty = sug ? Object.entries(sug.actions).filter(([, v]) => !v).map(([a]) => O("act")[a]) : [];
  const parts = [];
  if (sug && sug.note) parts.push(sug.note);
  if (empty.length) parts.push(t("note_unset", { x: empty.join(SEP()) }));
  $("rule-note").textContent = parts.join(" ");
  $("rule-note").classList.toggle("hidden", !parts.length);
  L.syncPassages($("f-rules"), f.rule_ids, sug ? sug.rule_ids : []);
}

// ------------------------------------------------------------------ lists (② ③ re-check)
function filtersFor(mode) {
  return mode === "adjudicate" ? ["conflict", "waiting", "final", "all"] : ["todo_box", "todo_mine", "all", "final"];
}
function annsFor(id) { return [...S.anns.values()].filter((a) => a.image_id === id).sort((a, b) => (a.saved_utc || "").localeCompare(b.saved_utc || "")); }
function mine(id) { return S.anns.get(`${id}|${S.data.owner}`) || null; }
function hasBox(r) { return ["bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2"].every((k) => r[k] !== "" && r[k] !== undefined && r[k] !== null); }
function matches(r, filter) {
  const st = r.label_status, m = mine(r.image_id);
  switch (filter) {
    case "todo_box": return !hasBox(r) && st !== "excluded";
    case "todo_mine": return st !== "excluded" && st !== "done" && st !== "conflict" && !(m && m.status === "done");
    case "final": return st === "done" || st === "excluded";
    case "conflict": return st === "conflict";
    case "waiting": return st === "waiting";
    default: return true;
  }
}
function setFilterOptions(keepValue) {
  const sel = $("kept-filter");
  const opts = filtersFor(S.mode);
  const prev = sel.value;
  sel.innerHTML = opts.map((v) => `<option value="${v}">${esc(t("f_" + v))}</option>`).join("");
  if (keepValue && opts.includes(prev)) { sel.value = prev; return; }
  const any = (f) => [...S.labels.values()].some((r) => matches(r, f));
  if (S.mode === "adjudicate") sel.value = any("conflict") ? "conflict" : any("waiting") ? "waiting" : "all";
  else if (opts.includes(prev)) sel.value = prev;
  else sel.value = any("todo_box") ? "todo_box" : "todo_mine";
}
function sortedLabels() { return [...S.labels.values()].sort((a, b) => Number(a.frame_index) - Number(b.frame_index)); }
function listRows() {
  if (S.mode === "recheck") return [...S.recheck.values()].map((r) => ({ ...r, _status: r.recheck_status, _base: S.labels.get(r.image_id) || {} }));
  const filter = $("kept-filter").value;
  return sortedLabels().filter((r) => matches(r, filter)).map((r) => ({ ...r, _status: r.label_status, _base: r }));
}
function renderKeptList() {
  if (!S.data) return;
  const ol = $("kept-list");
  const rows = listRows();
  const titles = { recheck: t("title_recheck", { n: rows.length }), adjudicate: t("title_adj", { n: rows.length }), label: t("title_label", { n: S.labels.size }) };
  $("kept-title").textContent = titles[S.mode] || titles.label;
  $("kept-filter").classList.toggle("hidden", S.mode === "recheck");
  ol.innerHTML = "";
  for (const r of rows) {
    const li = document.createElement("li");
    li.dataset.id = r.image_id;
    li.classList.toggle("sel", r.image_id === S.selId);
    let extra = "";
    if (S.mode === "label") {
      const m = mine(r.image_id);
      extra = `<br><span class="sub2">${esc(!hasBox(r) ? t("li_nobox") : m ? (m.status === "done" ? t("li_mine_done") : t("li_mine_draft")) : t("li_mine_none"))}</span>`;
    } else if (S.mode === "adjudicate") {
      extra = `<br><span class="sub2">${esc(t("li_anns", { n: annsFor(r.image_id).filter((a) => a.status === "done").length }))}</span>`;
    }
    const mt = r.marking_type ? O("marking")[r.marking_type] || r.marking_type : "";
    li.innerHTML = `<img loading="lazy" alt="" src="/api/image?id=${encodeURIComponent(r.image_id)}&w=144&v=${S.data.mask_version}">` +
      `<div class="meta">${IMG() ? esc(poolName(r._base.split) + " · " + groupName(r._base.pick_group)) : fmtTime(Number(r._base.time_s || 0))}<br><span class="pill ${r._status}">${esc(status(r._status))}</span> ${S.mode === "recheck" ? "" : esc(mt)}${extra}</div>`;
    li.addEventListener("click", () => openImage(r.image_id));
    ol.appendChild(li);
  }
  if (!rows.length) ol.innerHTML = `<li style="cursor:default;color:var(--muted)">${esc(S.mode === "recheck" ? t("empty_recheck") : t("empty_list"))}</li>`;
}
function updateCounts() {
  if (!S.data) return;
  const st = { kept: 0, waiting: 0, conflict: 0, done: 0, excluded: 0 };
  for (const r of S.labels.values()) st[r.label_status] = (st[r.label_status] || 0) + 1;
  const cand = IMG() ? (S.data.index.images || 0) : S.data.scan.filter((r) => r.candidate).length;
  $("counts").textContent = t(IMG() ? "counts_img" : "counts", { c: cand, k: S.labels.size, nb: st.kept, w: st.waiting, cf: st.conflict, d: st.done }) +
    (S.recheck.size ? t("counts_re", { a: [...S.recheck.values()].filter((r) => r.recheck_status === "done").length, b: S.recheck.size }) : "");
  $("tab-adjudicate").textContent = t("tab_adjudicate") + (st.conflict ? ` (${st.conflict})` : "");
}

function rowToForm(row, recheck) {
  const acts = {};
  for (const a of S.data.schema.actions) acts[a] = (row && row["act_" + a]) || "";
  row = row || {};
  return {
    marking_type: row.marking_type || "", arrow_type: row.arrow_type || "", position: row.position || "",
    dashed_side: row.dashed_side || "", visibility: row.visibility || "", behavior_decidable: row.behavior_decidable || "",
    actions: acts, rule_ids: recheck ? [] : (row.accepted_rule_ids || "").split(";").filter(Boolean),
  };
}
function showFormPanel(which) {
  $("form").classList.toggle("hidden", which !== "form");
  $("adj-panel").classList.toggle("hidden", which !== "adj");
  $("adj-cancel").classList.toggle("hidden", !(S.mode === "adjudicate" && which === "form"));
}
function openImage(id) {
  const base = S.labels.get(id);
  if (!base) return;
  S.selId = id;
  S.adjEditing = false;
  const rec = S.mode === "recheck" ? S.recheck.get(id) : null;
  if (S.mode === "recheck") S.form = rowToForm(rec && rec.recheck_status !== "pending" ? rec : null, true);
  else S.form = rowToForm(mine(id), false);
  const box = ["bbox_x1", "bbox_y1", "bbox_x2", "bbox_y2"].map((k) => base[k]);
  S.box = box.every((v) => v !== "" && v !== undefined) ? box.map(Number) : null;
  const m = mine(id);
  S.privacy = S.mode === "label" ? JSON.parse((m && m.privacy_boxes) || "[]") : JSON.parse(base.privacy_boxes || "[]");
  S.privSel = -1; S.drawing = null;
  $("form-empty").classList.add("hidden");
  $("form-body").classList.remove("hidden");
  $("f-notes").value = base.notes || "";
  $("form-msgs").innerHTML = "";
  const st = rec ? status(rec.recheck_status) : status(base.label_status);
  $("img-title").textContent = IMG() ? `${id} · ${poolName(base.split)} · ${st}` : `${id} · ${fmtTime(Number(base.time_s))} · ${st}`;
  try { S.hints = IMG() ? JSON.parse(base.box_hints || "[]") : []; } catch (e) { S.hints = []; }
  const img = $("label-img");
  img.onload = () => { layoutLabel(); drawLabelOverlay(); };
  img.src = `/api/image?id=${encodeURIComponent(id)}&v=${S.data.mask_version}`;
  if (S.mode === "adjudicate") { showFormPanel("adj"); renderAdj(id); }
  else { showFormPanel("form"); renderForm(); }
  for (const li of $("kept-list").querySelectorAll("li")) li.classList.toggle("sel", li.dataset.id === id);
  const sel = $("kept-list").querySelector("li.sel");
  if (sel) sel.scrollIntoView({ block: "nearest" });
}
function formFields() {
  return {
    marking_type: S.form.marking_type, arrow_type: S.form.arrow_type, position: S.form.position,
    dashed_side: S.form.dashed_side, visibility: S.form.visibility, behavior_decidable: S.form.behavior_decidable,
    actions: S.form.actions, accepted_rule_ids: S.form.rule_ids, notes: $("f-notes").value,
    box: S.box, privacy_boxes: S.privacy,
  };
}
function setAnns(id, list) {
  for (const k of [...S.anns.keys()]) if (k.startsWith(id + "|")) S.anns.delete(k);
  for (const a of list || []) S.anns.set(`${a.image_id}|${a.annotator}`, a);
}
function finalMsg(row) {
  switch (row.label_status) {
    case "waiting": return t("fin_waiting", { n: S.data.required });
    case "conflict": return t("fin_conflict");
    case "done": return row.final_source === "agreed" ? t("fin_agreed") : row.final_source === "single" ? t("fin_single") : t("fin_adj");
    case "kept": return t("fin_kept");
    case "excluded": return t("fin_excluded");
    default: return "";
  }
}
async function save(st) {
  if (!S.selId) return;
  if (S.mode === "adjudicate") { if (S.adjEditing) saveAdjEdit(); return; }
  const id = S.selId;
  const box = $("form-msgs");
  try {
    let res;
    if (S.mode === "recheck") {
      res = await api("/api/recheck", { image_id: id, fields: formFields(), status: st });
      S.recheck.set(id, res.row);
    } else {
      res = await api("/api/label", { image_id: id, fields: formFields(), status: st });
      S.labels.set(id, res.row);
      setAnns(id, res.annotations);
    }
    const parts = [];
    for (const e of res.errors) parts.push(`<div class="e">✗ ${esc(e)}</div>`);
    for (const w of res.warnings) parts.push(`<div class="w">! ${esc(w)}</div>`);
    if (st === "done" && res.errors.length) parts.unshift(`<div class="e">${esc(t("not_done"))}</div>`);
    else if (S.mode === "recheck") parts.unshift(`<div class="ok">${esc(t("saved_st", { s: status(res.row.recheck_status) }))}</div>`);
    else parts.unshift(`<div class="ok">${esc(t("saved") + " " + finalMsg(res.row))}</div>`);
    box.innerHTML = parts.join("");
    renderKeptList(); updateCounts(); drawTimeline();
    const advance = (st === "done" && !res.errors.length && !res.warnings.length) || st === "excluded" || (st === "box" && !res.errors.length);
    if (advance) gotoNextTodo(id, parts.join(""));
    else if (st === "done" && !res.errors.length) box.insertAdjacentHTML("beforeend", `<div class="ok">${esc(t("warn_look"))}</div>`);
  } catch (e) { box.innerHTML = `<div class="e">${esc(t("save_fail") + e.message)}</div>`; }
}
function gotoNextTodo(fromId, keepMsg) {
  let all, isTodo;
  if (S.mode === "recheck") { all = listRows(); isTodo = (r) => r.recheck_status !== "done"; }
  else {
    all = sortedLabels();
    const f = $("kept-filter").value;
    isTodo = (r) => (f === "all" || f === "final") ? matches(r, S.mode === "adjudicate" ? "conflict" : "todo_mine") : matches(r, f);
  }
  const i = all.findIndex((r) => r.image_id === fromId);
  const next = all.slice(i + 1).find(isTodo) || all.slice(0, Math.max(0, i)).find(isTodo);
  const box = $(S.mode === "adjudicate" ? "adj-msgs" : "form-msgs");
  if (next) { openImage(next.image_id); if (keepMsg) $(S.mode === "adjudicate" ? "adj-msgs" : "form-msgs").innerHTML = keepMsg; }
  else box.insertAdjacentHTML("beforeend", `<div class="ok">${esc(t("all_done_cat"))}</div>`);
}
function moveSel(d) {
  const rows = listRows();
  if (!rows.length) return;
  const i = rows.findIndex((r) => r.image_id === S.selId);
  openImage(rows[Math.max(0, Math.min(rows.length - 1, i < 0 ? 0 : i + d))].image_id);
}
async function unkeepSel() {
  if (!S.selId || S.mode !== "label") return;
  if (!confirm(t("confirm_unkeep"))) return;
  const id = S.selId;
  try {
    await api("/api/unkeep", { image_id: id });
    const rows = listRows(); const i = rows.findIndex((r) => r.image_id === id);
    S.labels.delete(id); setAnns(id, []); S.selId = null;
    $("form-body").classList.add("hidden"); $("form-empty").classList.remove("hidden");
    $("label-img").removeAttribute("src"); drawLabelOverlay();
    renderKeptList(); updateCounts(); drawTimeline();
    const rest = listRows();
    if (rest.length) openImage(rest[Math.min(Math.max(0, i), rest.length - 1)].image_id);
  } catch (e) { $("form-msgs").innerHTML = `<div class="e">${esc(t("del_fail") + e.message)}</div>`; }
}

// ------------------------------------------------------------------ ③ merge and adjudication
function who(code) { return code === S.data.owner ? t("you") : code; }
function adjVal(dict, v) { return v ? (dict[v] || v) : "—"; }
function renderAdj(id) {
  const row = S.labels.get(id);
  const anns = annsFor(id).filter((a) => a.status === "done");
  const drafts = annsFor(id).filter((a) => a.status !== "done");
  const panel = $("adj-body");
  const srcName = { agreed: t("src_agreed"), single: t("src_single"), adjudicated: t("src_adj") }[row.final_source] || row.final_source;
  const head = `<div class="adj-status"><span class="pill ${row.label_status}">${esc(status(row.label_status))}</span> ` +
    `${row.final_source ? esc(t("src") + srcName) : ""}${row.adjudication_note ? " · " + esc(row.adjudication_note) : ""}</div>`;
  if (!anns.length) {
    panel.innerHTML = head + `<p class="muted">${esc(t("no_ann"))}${drafts.length ? esc(t("n_drafts", { n: drafts.length })) : ""}</p>`;
  } else {
    const fields = [["marking_type", O("marking")], ["arrow_type", O("arrow")], ["position", O("position")], ["dashed_side", O("dashed")],
      ["visibility", O("vis")], ["behavior_decidable", O("decide")]];
    const cols = anns.map((a) => `<th>${esc(who(a.annotator))}${a.unsure === "1" ? ` <span class="pill unsure">${esc(t("unsure"))}</span>` : ""}</th>`).join("");
    const rows = [];
    const diffRow = (vals) => vals.some((v) => v !== vals[0]);
    for (const [f, dict] of fields) {
      const vals = anns.map((a) => a[f] || "");
      if (vals.every((v) => !v)) continue;
      rows.push(`<tr class="${diffRow(vals) ? "bad" : ""}"><td>${esc(O("field")[f])}</td>${vals.map((v) => `<td>${esc(adjVal(dict, v))}</td>`).join("")}</tr>`);
    }
    for (const a of S.data.schema.actions) {
      const vals = anns.map((x) => x["act_" + a] || "");
      rows.push(`<tr class="${diffRow(vals) ? "bad" : ""}"><td>${esc(O("act")[a])}</td>${vals.map((v) => `<td>${esc(adjVal(O("actv"), v))}</td>`).join("")}</tr>`);
    }
    rows.push(`<tr><td>${esc(t("rules_col"))}</td>${anns.map((a) => `<td class="ids">${(a.accepted_rule_ids || "").split(";").filter(Boolean).map(esc).join("<br>") || "—"}</td>`).join("")}</tr>`);
    const comments = anns.filter((a) => a.comment).map((a) => `<div class="w">${esc(who(a.annotator))}: ${esc(a.comment)}</div>`).join("");
    const choose = anns.map((a) => `<button type="button" class="adj-choose" data-code="${esc(a.annotator)}">${esc(t("adopt", { w: who(a.annotator) }))}</button>`).join("");
    panel.innerHTML = head + `<table class="cmp adj"><tr><th>${esc(t("item"))}</th>${cols}</tr>${rows.join("")}</table>${comments}` +
      (["conflict", "waiting"].includes(row.label_status) ? `<div class="buttons">${choose}</div>` : "");
    for (const b of panel.querySelectorAll(".adj-choose")) b.addEventListener("click", () => adjudicate(b.dataset.code));
  }
  if (drafts.length && anns.length) panel.insertAdjacentHTML("beforeend", `<p class="muted">${esc(t("more_drafts", { n: drafts.length }))}</p>`);
  const decided = row.final_source === "adjudicated" || row.label_status === "excluded";
  $("adj-edit").classList.toggle("hidden", decided);
  $("adj-exclude").classList.toggle("hidden", decided);
  $("adj-reopen").classList.toggle("hidden", !decided);
  $("adj-note").value = "";
  $("adj-msgs").innerHTML = "";
}
async function adjudicate(choice, fields) {
  const id = S.selId;
  try {
    const res = await api("/api/adjudicate", { image_id: id, choice, fields: fields || null, note: $("adj-note").value });
    if (res.errors && res.errors.length) { $("form-msgs").innerHTML = res.errors.map((e) => `<div class="e">✗ ${esc(e)}</div>`).join(""); return false; }
    S.labels.set(id, res.row); setAnns(id, res.annotations);
    renderKeptList(); updateCounts(); drawTimeline();
    const text = { exclude: t("adj_excluded"), reopen: t("adj_reopened"), edit: t("adj_edited") }[choice] || t("adj_adopted", { w: who(choice) });
    S.adjEditing = false;
    if (choice === "reopen") { openImage(id); $("adj-msgs").innerHTML = `<div class="ok">${esc(text)}</div>`; }
    else gotoNextTodo(id, `<div class="ok">✓ ${esc(text)}</div>`);
    return true;
  } catch (e) { $("adj-msgs").innerHTML = `<div class="e">${esc(t("save_fail") + e.message)}</div>`; return false; }
}
function startAdjEdit() {
  const anns = annsFor(S.selId).filter((a) => a.status === "done");
  S.form = rowToForm(anns[0] || S.labels.get(S.selId), false);
  S.adjEditing = true;
  showFormPanel("form");
  $("form-msgs").innerHTML = `<div class="w">${esc(t("adj_edit_hint"))}</div>`;
  renderForm();
}
function saveAdjEdit() { adjudicate("edit", formFields()); }

// ------------------------------------------------------------------ label canvas
function layoutLabel() {
  if (!S.data || S.view === "screen" || S.view === "share") return;
  const work = document.querySelector(".work");
  const maxW = work.clientWidth - 20;
  const maxH = work.clientHeight - document.querySelector(".work .toolbar").offsetHeight - $("stage-hint").offsetHeight - 24;
  const r = Math.min(maxW / outW(), maxH / outH());
  const w = Math.floor(outW() * r), h = Math.floor(outH() * r);
  const st = $("label-stage");
  st.style.width = w + "px"; st.style.height = h + "px";
  sizeCanvas($("label-overlay"), w, h);
  drawLabelOverlay();
}
function toImg(ev, canvas, natW, natH) {
  const rect = canvas.getBoundingClientRect();
  const x = ((ev.clientX - rect.left) / rect.width) * natW, y = ((ev.clientY - rect.top) / rect.height) * natH;
  return [Math.max(0, Math.min(natW, x)), Math.max(0, Math.min(natH, y))];
}
function normRect(a, b) { return [Math.min(a[0], b[0]), Math.min(a[1], b[1]), Math.max(a[0], b[0]), Math.max(a[1], b[1])]; }
function inRect(p, r) { return p[0] >= r[0] && p[0] <= r[2] && p[1] >= r[1] && p[1] <= r[3]; }
function drawLabelOverlay() {
  const c = $("label-overlay"), ctx = c.getContext("2d");
  const w = c.clientWidth, h = c.clientHeight;
  ctx.clearRect(0, 0, w, h);
  if (!S.selId) return;
  const sx = w / outW(), sy = h / outH();
  const R = (r) => [r[0] * sx, r[1] * sy, (r[2] - r[0]) * sx, (r[3] - r[1]) * sy];
  if (S.mode !== "recheck") {
    S.privacy.forEach((r, i) => {
      ctx.fillStyle = "rgba(255, 94, 196, .28)"; ctx.fillRect(...R(r));
      ctx.strokeStyle = i === S.privSel ? "#fff" : "#ff5ec4"; ctx.lineWidth = i === S.privSel ? 3 : 2; ctx.strokeRect(...R(r));
      ctx.fillStyle = "#ff5ec4"; ctx.font = "11px sans-serif"; ctx.fillText(t("lbl_privacy"), r[0] * sx + 3, r[1] * sy - 3);
    });
  }
  if (!S.box && S.mode === "label" && (S.hints || []).length) {
    S.hints.forEach((r, i) => {
      ctx.strokeStyle = "#ffd54f"; ctx.lineWidth = 2; ctx.setLineDash([7, 5]); ctx.strokeRect(...R(r)); ctx.setLineDash([]);
      ctx.fillStyle = "#ffd54f"; ctx.font = "bold 11px sans-serif";
      ctx.fillText(`${t("lbl_hint")} ${i + 1}`, r[0] * sx + 3, Math.max(11, r[1] * sy - 4));
    });
  }
  if (S.box) {
    ctx.strokeStyle = "#36e0c8"; ctx.lineWidth = 2.5; ctx.setLineDash([]); ctx.strokeRect(...R(S.box));
    ctx.fillStyle = "#36e0c8"; ctx.font = "bold 11px sans-serif"; ctx.fillText(t("lbl_target"), S.box[0] * sx + 3, S.box[1] * sy - 4);
  }
  if (S.drawing && S.drawing.where === "label") {
    ctx.setLineDash([6, 4]); ctx.lineWidth = 2;
    ctx.strokeStyle = S.drawing.tool === "box" ? "#36e0c8" : "#ff5ec4";
    ctx.strokeRect(...R(S.drawing.rect)); ctx.setLineDash([]);
  }
}
function drawLoupe(p) {
  const lp = $("loupe");
  if (!$("loupe-on").checked || !p || !S.selId) { lp.classList.add("hidden"); return; }
  lp.classList.remove("hidden");
  const img = $("label-img"), ctx = lp.getContext("2d"), z = 70, k = 220 / z;
  ctx.imageSmoothingEnabled = false;
  ctx.fillStyle = "#000"; ctx.fillRect(0, 0, 220, 220);
  const sx = p[0] - z / 2, sy = p[1] - z / 2;
  try { ctx.drawImage(img, sx, sy, z, z, 0, 0, 220, 220); } catch (e) { /* image not ready */ }
  const drawR = (r, col) => { ctx.strokeStyle = col; ctx.lineWidth = 1.5; ctx.strokeRect((r[0] - sx) * k, (r[1] - sy) * k, (r[2] - r[0]) * k, (r[3] - r[1]) * k); };
  if (S.box) drawR(S.box, "#36e0c8");
  if (S.drawing && S.drawing.where === "label") drawR(S.drawing.rect, S.drawing.tool === "box" ? "#36e0c8" : "#ff5ec4");
  ctx.strokeStyle = "rgba(255,255,255,.7)"; ctx.lineWidth = 1;
  ctx.beginPath(); ctx.moveTo(110, 0); ctx.lineTo(110, 220); ctx.moveTo(0, 110); ctx.lineTo(220, 110); ctx.stroke();
  const stage = $("label-stage").getBoundingClientRect(), mouseX = (p[0] / outW()) * stage.width;
  lp.style.right = mouseX > stage.width - 250 ? "auto" : "8px";
  lp.style.left = mouseX > stage.width - 250 ? "8px" : "auto";
}
function setTool(tool) {
  if (S.mode !== "label") return;
  S.tool = tool;
  $("tool-box").classList.toggle("active", tool === "box");
  $("tool-privacy").classList.toggle("active", tool === "privacy");
}

// ------------------------------------------------------------------ ④ share with helpers
async function loadShare() {
  try { S.share = await api("/api/share"); } catch (e) { S.share = null; $("sh-warn").innerHTML = `<div class="errbox">${esc(e.message)}</div>`; return; }
  renderShare();
}
function convName(c) {
  const [mt, sub] = c.key.split("|");
  let name = O("marking")[mt] || mt;
  if (mt === "arrow" && sub) name = t("conv_key_arrow", { a: O("arrow")[sub] || sub });
  else if (sub) name += " · " + (O("dashed")[sub] || sub);
  return `${O("region")[c.region] || c.region} · ${name}`;
}
function renderShare() {
  $("sh-flow").innerHTML = t("sh_flow").map((x) => `<li>${x}</li>`).join("");
  const d = S.share;
  if (!d) return;
  const sum = (k) => d.trips.reduce((a, r) => a + (r[k] || 0), 0);
  const card = (n, label, cls) => `<div class="card ${cls || ""}"><div class="num">${n}</div><div class="lbl">${esc(label)}</div></div>`;
  $("sh-cards").innerHTML = card(sum("kept"), t("sh_c_kept")) + card(sum("boxed"), t("sh_c_boxed")) +
    card(sum("need"), t("sh_c_need"), sum("need") ? "warn" : "good") + card(sum("outstanding"), t("sh_c_out")) +
    card(sum("mine_done"), t("sh_c_mine"), sum("mine_done") ? "good" : "warn") +
    card(sum("conflict"), t("sh_c_conflict"), sum("conflict") ? "bad" : "") + card(sum("done"), t("sh_c_done"), "good");
  const warns = [];
  if (d.open_cells.length) {
    warns.push(`<div class="warnbox">${t("sh_warn_open")}<ul>` + d.open_cells.map((c) =>
      `<li><b>${esc(convName(c))}</b>: ${esc(c.actions.map((a) => O("act")[a] || a).join(SEP()))}${(S.lang === "zh" ? c.note_zh : c.note) ? ` — ${esc(S.lang === "zh" ? c.note_zh : c.note)}` : ""}</li>`).join("") + "</ul></div>");
  }
  if (!sum("mine_done")) warns.push(`<div class="warnbox">${esc(t("sh_warn_nopractice"))}</div>`);
  if (sum("no_box")) warns.push(`<div class="warnbox">${esc(t("sh_warn_nobox", { n: sum("no_box") }))}</div>`);
  $("sh-warn").innerHTML = warns.join("");
  $("sh-known").innerHTML = d.helpers.length ? `<span class="muted">${esc(t("sh_known"))}</span>` +
    d.helpers.map((h) => `<button type="button" class="chip" data-name="${esc(h.name)}">${esc(h.name)} (${esc(h.code)})</button>`).join("") : "";
  for (const b of $("sh-known").querySelectorAll(".chip")) {
    b.addEventListener("click", () => {
      const cur = $("sh-names").value.split(/[,，\n]/).map((x) => x.trim()).filter(Boolean);
      if (!cur.includes(b.dataset.name)) cur.push(b.dataset.name);
      $("sh-names").value = cur.join(", ");
    });
  }
  $("sh-pkg-path").textContent = d.packages_dir;
  $("sh-ret-path").textContent = d.returned_dir;
  $("sh-table").innerHTML = packageTable(d.packages.slice().reverse(), true);
}
function fmtSize(b) { b = Number(b || 0); return b > 1e6 ? (b / 1e6).toFixed(1) + " MB" : Math.max(1, Math.round(b / 1e3)) + " KB"; }
function packageTable(rows, withStatus) {
  if (!rows.length) return `<p class="muted">${esc(t("sh_none_sent"))}</p>`;
  const head = [t("th_helper"), t("th_items"), t("th_created")].concat(withStatus ? [t("th_status"), t("th_done"), t("th_unsure"), t("th_practice")] : []).concat([t("th_file")]);
  const body = rows.map((p) => {
    const cells = [`${esc(p.name || "")} <span class="muted">(${esc(p.annotator)})</span>`, p.n_items, esc((p.created_utc || "").replace("T", " ").replace("Z", " UTC"))];
    if (withStatus) cells.push(`<span class="pill ${esc(p.status)}">${esc(t("ps_" + p.status))}</span>`, esc(p.done || "0"), esc(p.unsure || "0"), esc(p.practice_score || "—"));
    cells.push(`<span class="mono">${esc(p.file || "")}</span> <span class="muted">${p.size_bytes ? fmtSize(p.size_bytes) : ""}</span>`);
    return `<tr>${cells.map((c) => `<td>${c}</td>`).join("")}</tr>`;
  }).join("");
  return `<table class="list"><tr>${head.map((h) => `<th>${esc(h)}</th>`).join("")}</tr>${body}</table>`;
}
async function makePackages() {
  const names = $("sh-names").value.split(/[,，;\n]/).map((x) => x.trim()).filter(Boolean);
  const out = $("sh-made");
  if (!names.length) { out.innerHTML = `<div class="errbox">${esc(t("sh_need_names"))}</div>`; return; }
  out.innerHTML = `<p class="muted">${esc(t("sh_making"))}</p>`;
  $("sh-make").disabled = true;
  try {
    const res = await api("/api/package", { names, practice: Number($("sh-practice").value || 6), max: $("sh-max").value || null });
    $("sh-log").textContent = (res.log || []).join("\n");
    if (!res.ok) { out.innerHTML = `<div class="errbox">${esc(res.error)}</div>`; return; }
    if (!res.made.length) { out.innerHTML = `<div class="warnbox">${esc(t("sh_made_none"))}</div>`; return; }
    const minutes = Math.max(5, Math.ceil(Math.max(...res.made.map((p) => p.n_items)) * 1.2 + 5));
    out.innerHTML = `<div class="okbox">${esc(t("sh_made_ok", { n: res.made.length }))} <span class="mono">${esc(S.share ? S.share.packages_dir : "")}</span>` +
      ` <button type="button" id="sh-open-made">${esc(t("sh_open_packages"))}</button></div>` + packageTable(res.made, false) +
      `<p><b>${esc(t("sh_tmpl_h"))}</b> <button type="button" id="sh-copy">${esc(t("sh_copy"))}</button></p><div class="tmpl" id="sh-tmpl">${esc(t("sh_tmpl", { m: minutes }))}</div>`;
    $("sh-open-made").addEventListener("click", () => openFolder("packages"));
    $("sh-copy").addEventListener("click", async () => {
      try { await navigator.clipboard.writeText($("sh-tmpl").textContent); $("sh-copy").textContent = t("sh_copied"); } catch (e) { /* select manually */ }
    });
    await loadShare();
  } catch (e) { out.innerHTML = `<div class="errbox">${esc(e.message)}</div>`; }
  finally { $("sh-make").disabled = false; }
}
async function openFolder(which) {
  try {
    const res = await api("/api/open", { which });
    if (!res.ok) alert(t("sh_open_fail") + "\n" + res.path);
  } catch (e) { alert(e.message); }
}
async function importFiles(fileList) {
  const files = [...fileList].filter((f) => f.name.toLowerCase().endsWith(".json"));
  const out = $("sh-import-result");
  if (!files.length) { out.innerHTML = `<div class="errbox">${esc(t("sh_not_json"))}</div>`; return; }
  out.innerHTML = `<p class="muted">${esc(t("sh_importing"))}</p>`;
  const payload = await Promise.all(files.map(async (f) => ({ name: f.name, text: await f.text() })));
  showImport(await api("/api/import", { files: payload }));
}
async function importFolder() {
  $("sh-import-result").innerHTML = `<p class="muted">${esc(t("sh_importing"))}</p>`;
  showImport(await api("/api/import_folder", {}));
}
async function showImport(res) {
  const out = $("sh-import-result");
  $("sh-log").textContent = (res.log || []).join("\n");
  if (!res.ok) { out.innerHTML = `<div class="errbox">${esc(res.error || t("sh_import_none"))}</div>`; return; }
  const c = res.counts || {};
  const lines = (res.files || []).map((f) => `<li>${esc(t("sh_imported_file", { file: f.file, code: f.annotator, done: f.done || 0, draft: f.draft || 0, unsure: f.unsure || 0 }))}</li>`).join("");
  const bad = (res.log || []).filter((l) => l.includes("✗")).map((l) => `<li class="e">${esc(l.trim())}</li>`).join("");
  out.innerHTML = `<div class="okbox">${esc(t("sh_imported", { f: (res.files || []).length, d: c.done || 0, c: c.conflict || 0, w: c.waiting || 0 }))}<ul>${lines}${bad}</ul>` +
    (c.conflict ? `<button type="button" id="sh-go-adj" class="primary">${esc(t("sh_go_adj"))}</button>` : "") + "</div>";
  if (c.conflict) $("sh-go-adj").addEventListener("click", () => switchView("adjudicate"));
  await refreshState();
  await loadShare();
}

// ------------------------------------------------------------------ views
function switchView(v) {
  S.view = v;
  for (const b of document.querySelectorAll(".tab")) b.classList.toggle("active", b.dataset.view === v);
  $("view-screen").classList.toggle("active", v === "screen" && !IMG());
  $("view-pick").classList.toggle("active", v === "screen" && IMG());
  $("view-share").classList.toggle("active", v === "share");
  $("view-label").classList.toggle("active", v === "label" || v === "adjudicate" || v === "recheck");
  if (v === "screen") { if (IMG()) { api("/api/quota").then((q) => { PK.quota = q; renderQuota(); }).catch(() => {}); requestAnimationFrame(drawPickOverlay); return; } layoutScreen(); drawTimeline(); renderBadges(); return; }
  if (!IMG()) setPlaying(false);
  if (v === "share") { renderShare(); loadShare(); return; }
  S.mode = v === "recheck" ? "recheck" : v === "adjudicate" ? "adjudicate" : "label";
  S.adjEditing = false;
  setFilterOptions();
  $("fs-rules").classList.toggle("hidden", v === "recheck");
  for (const id of ["tool-box", "tool-privacy", "del-box", "unkeep", "save-exclude", "save-box"]) $(id).classList.toggle("hidden", S.mode !== "label");
  $("save-draft").classList.toggle("hidden", S.mode === "adjudicate");
  $("save-done").textContent = S.mode === "adjudicate" ? t("save_final") : t("save_done");
  $("stage-hint").textContent = { recheck: t("hint_recheck"), adjudicate: t("hint_adj"), label: IMG() ? t("hint_label_img") : t("hint_label") }[S.mode];
  renderKeptList();
  layoutLabel();
  const rows = listRows();
  if (!S.selId || !rows.some((r) => r.image_id === S.selId)) {
    if (rows[0]) openImage(rows[0].image_id);
    else { S.selId = null; showFormPanel("form"); $("form-body").classList.add("hidden"); $("form-empty").classList.remove("hidden"); $("label-img").removeAttribute("src"); drawLabelOverlay(); }
  } else openImage(S.selId);
}
function applyBrightness() {
  const v = Number($("bright").value);
  $("bright-val").textContent = v.toFixed(1) + "×";
  document.documentElement.style.setProperty("--imgfilter", `brightness(${v}) contrast(${1 + (v - 1) * 0.15})`);
}
function guideCtx() {
  return { region: S.data ? S.data.trip.region : "US", table: S.data ? S.data.rules_table : {}, passages: S.data ? S.data.passages : [], owner: true };
}
function openGuide() {
  $("guide-body").innerHTML = window.LANE_GUIDE ? window.LANE_GUIDE.render(S.lang, guideCtx()) : "";
  $("guide-lang").textContent = t("lang_other");
  $("guide").classList.remove("hidden");
}

// ------------------------------------------------------------------ events
function bindEvents() {
  for (const b of document.querySelectorAll(".tab")) b.addEventListener("click", () => switchView(b.dataset.view));
  $("prev-btn").addEventListener("click", () => step(-1));
  $("next-btn").addEventListener("click", () => step(1));
  $("play-btn").addEventListener("click", () => setPlaying(!S.playing));
  $("frame-back").addEventListener("click", () => gotoFrame(S.curFrame - 1, true));
  $("frame-fwd").addEventListener("click", () => gotoFrame(S.curFrame + 1, true));
  $("keep-btn").addEventListener("click", keepCurrent);
  $("label-now-btn").addEventListener("click", labelLastKept);
  $("show-all").addEventListener("change", () => { computeShown(); gotoFrame(S.curFrame); });
  $("only-paint").addEventListener("change", () => { computeShown(); gotoFrame(S.curFrame); });
  $("mask-btn").addEventListener("click", () => setMaskMode(!S.maskMode));
  $("mask-save").addEventListener("click", saveMasks);
  $("mask-cancel").addEventListener("click", () => setMaskMode(false));
  $("bright").addEventListener("input", applyBrightness);
  $("lang-btn").addEventListener("click", () => setLang(S.lang === "zh" ? "en" : "zh"));
  $("guide-lang").addEventListener("click", () => setLang(S.lang === "zh" ? "en" : "zh"));
  $("help-btn").addEventListener("click", () => $("help").classList.remove("hidden"));
  $("help-close").addEventListener("click", () => $("help").classList.add("hidden"));
  $("guide-btn").addEventListener("click", openGuide);
  $("guide-close").addEventListener("click", () => $("guide").classList.add("hidden"));
  $("guide-print").addEventListener("click", () => window.LANE_GUIDE && window.LANE_GUIDE.openPrintable(S.lang, guideCtx()));
  $("kept-filter").addEventListener("change", renderKeptList);
  $("tool-box").addEventListener("click", () => setTool("box"));
  $("tool-privacy").addEventListener("click", () => setTool("privacy"));
  $("del-box").addEventListener("click", deleteSelectedPrivacy);
  $("prefill-btn").addEventListener("click", () => { applySuggestion(true); renderForm(); });
  $("rules-expand").addEventListener("click", () => {
    const rules = [...$("f-rules").querySelectorAll(".rule")];
    const open = !rules.every((r) => r.classList.contains("open"));
    for (const r of rules) { r.classList.toggle("open", open); r.querySelector(".rmore").textContent = open ? L.RULE_TXT[S.lang].less : L.RULE_TXT[S.lang].more; }
    $("rules-expand").textContent = open ? t("collapse_all") : t("expand_all");
  });
  $("save-done").addEventListener("click", () => save("done"));
  $("save-draft").addEventListener("click", () => save("draft"));
  $("save-exclude").addEventListener("click", () => save("excluded"));
  $("save-box").addEventListener("click", () => save("box"));
  $("adj-edit").addEventListener("click", startAdjEdit);
  $("adj-exclude").addEventListener("click", () => adjudicate("exclude"));
  $("adj-reopen").addEventListener("click", () => adjudicate("reopen"));
  $("adj-cancel").addEventListener("click", () => { S.adjEditing = false; showFormPanel("adj"); renderAdj(S.selId); });
  $("unkeep").addEventListener("click", unkeepSel);
  $("vis-help").addEventListener("click", () => alert(t("vis_tip")));
  // ④
  $("sh-make").addEventListener("click", makePackages);
  $("sh-open-packages").addEventListener("click", () => openFolder("packages"));
  $("sh-open-returned").addEventListener("click", () => openFolder("returned"));
  $("sh-import-folder").addEventListener("click", importFolder);
  $("sh-pick").addEventListener("click", () => $("sh-file").click());
  $("sh-file").addEventListener("change", (e) => { if (e.target.files.length) importFiles(e.target.files); e.target.value = ""; });
  const drop = $("sh-drop");
  drop.addEventListener("dragover", (e) => { e.preventDefault(); drop.classList.add("over"); });
  drop.addEventListener("dragleave", () => drop.classList.remove("over"));
  drop.addEventListener("drop", (e) => { e.preventDefault(); drop.classList.remove("over"); if (e.dataTransfer.files.length) importFiles(e.dataTransfer.files); });

  const tl = $("timeline"), tip = $("tip");
  tl.addEventListener("click", (e) => {
    setPlaying(false);
    const f = timelineFrame(e);
    if ($("show-all").checked) gotoFrame(f); else { S.pos = nearestShown(f); gotoFrame(S.data.scan[S.shown[S.pos]].frame_index, true); }
  });
  tl.addEventListener("mousemove", (e) => {
    const f = timelineFrame(e), s = sampleNear(f);
    tip.textContent = `${fmtTime(f / fps())}${s.stationary ? " · " + t("b_stop") : s.dup ? " · " + t("b_crawl") : ""}${s.dark ? " · " + t("b_dark") : ""}`;
    tip.style.left = e.clientX + 12 + "px"; tip.style.top = e.clientY - 30 + "px";
    tip.classList.remove("hidden");
  });
  tl.addEventListener("mouseleave", () => tip.classList.add("hidden"));

  const so = $("screen-overlay");
  so.addEventListener("mousedown", (e) => {
    if (!S.maskMode) return;
    const p = toImg(e, so, srcW(), srcH());
    const hit = S.masks.findIndex((m) => inRect(p, m));
    if (hit >= 0) { S.maskSel = hit; drawScreenOverlay(); return; }
    S.maskSel = -1;
    S.drawing = { where: "mask", start: p, rect: [p[0], p[1], p[0], p[1]] };
  });
  window.addEventListener("mousemove", (e) => {
    if (S.drawing && S.drawing.where === "mask") { S.drawing.rect = normRect(S.drawing.start, toImg(e, so, srcW(), srcH())); drawScreenOverlay(); }
  });
  window.addEventListener("mouseup", () => {
    if (S.drawing && S.drawing.where === "mask") {
      const r = S.drawing.rect.map(Math.round); S.drawing = null;
      if (r[2] - r[0] >= 4 && r[3] - r[1] >= 4) S.masks.push(r);
      drawScreenOverlay();
    }
  });

  const lo = $("label-overlay");
  lo.addEventListener("mousedown", (e) => {
    if (!S.selId || S.mode !== "label") return;
    const p = toImg(e, lo, outW(), outH());
    if (S.tool === "privacy") {
      const hit = S.privacy.findIndex((r) => inRect(p, r));
      if (hit >= 0) { S.privSel = hit; drawLabelOverlay(); return; }
    }
    S.privSel = -1;
    S.drawing = { where: "label", tool: S.tool, start: p, rect: [p[0], p[1], p[0], p[1]] };
  });
  lo.addEventListener("mousemove", (e) => {
    const p = toImg(e, lo, outW(), outH());
    $("coords").textContent = `x ${Math.round(p[0])}  y ${Math.round(p[1])}`;
    S.hover = p; drawLoupe(p);
  });
  lo.addEventListener("mouseleave", () => { S.hover = null; drawLoupe(null); $("coords").textContent = ""; });
  window.addEventListener("mousemove", (e) => {
    if (S.drawing && S.drawing.where === "label") { const p = toImg(e, lo, outW(), outH()); S.drawing.rect = normRect(S.drawing.start, p); drawLabelOverlay(); drawLoupe(p); }
  });
  window.addEventListener("mouseup", () => {
    if (S.drawing && S.drawing.where === "label") {
      const r = S.drawing.rect.map(Math.round), tool = S.drawing.tool;
      S.drawing = null;
      if (r[2] - r[0] >= 4 && r[3] - r[1] >= 4) { if (tool === "box") S.box = r; else { S.privacy.push(r); S.privSel = S.privacy.length - 1; } }
      else if (tool === "box" && !S.box && (S.hints || []).length) {
        const hit = S.hints.find((h) => inRect([r[0], r[1]], h));
        if (hit) S.box = hit.map(Math.round);
      }
      drawLabelOverlay();
    }
  });
  document.querySelector(".controls").addEventListener("mouseup", (e) => { const b = e.target.closest("button"); if (b) b.blur(); });
  document.addEventListener("keydown", onKey);
}
function deleteSelectedPrivacy() { if (S.privSel >= 0) { S.privacy.splice(S.privSel, 1); S.privSel = -1; drawLabelOverlay(); } }
function labelLastKept() {
  const id = S.lastKept || (keptAt(S.curFrame) || {}).image_id;
  if (!id) { msg($("screen-msg"), t("no_last"), "warn"); return; }
  switchView("label"); openImage(id);
}
function onKey(e) {
  const mod = e.metaKey || e.ctrlKey;
  if (!$("guide").classList.contains("hidden")) { if (e.key === "Escape") $("guide").classList.add("hidden"); return; }
  if (!$("help").classList.contains("hidden")) { if (e.key === "Escape" || e.key === "?") $("help").classList.add("hidden"); return; }
  if (S.view === "share") return;
  if (e.key === "?" && !isTyping(e)) { $("help").classList.remove("hidden"); return; }
  if (S.view !== "screen") {
    if (mod && e.key === "Enter") { e.preventDefault(); save("done"); return; }
    if (mod && (e.key === "s" || e.key === "S")) { e.preventDefault(); save("draft"); return; }
    if (isTyping(e)) return;
    if (e.key === "Escape") {
      if (S.mode === "adjudicate" && S.adjEditing) { S.adjEditing = false; showFormPanel("adj"); renderAdj(S.selId); return; }
      S.drawing = null; S.privSel = -1; drawLabelOverlay(); return;
    }
    if (e.key === "b" || e.key === "B") setTool("box");
    else if (e.key === "p" || e.key === "P") setTool("privacy");
    else if (e.key === "Delete" || e.key === "Backspace") { e.preventDefault(); deleteSelectedPrivacy(); }
    else if (e.key === "[") moveSel(-1);
    else if (e.key === "]") moveSel(1);
    return;
  }
  if (isTyping(e) || mod) return;
  if (IMG()) { pickKey(e); return; }
  if (S.maskMode) {
    if ((e.key === "Delete" || e.key === "Backspace") && S.maskSel >= 0) { e.preventDefault(); S.masks.splice(S.maskSel, 1); S.maskSel = -1; drawScreenOverlay(); }
    if (e.key === "Escape") setMaskMode(false);
    return;
  }
  const k = e.key;
  if (k === " ") { e.preventDefault(); setPlaying(!S.playing); }
  else if (k === "ArrowRight") { e.preventDefault(); setPlaying(false); e.shiftKey ? jumpSeconds(10) : step(1); }
  else if (k === "ArrowLeft") { e.preventDefault(); setPlaying(false); e.shiftKey ? jumpSeconds(-10) : step(-1); }
  else if (k === "," || k === "<") { setPlaying(false); gotoFrame(S.curFrame - 1, true); }
  else if (k === "." || k === ">") { setPlaying(false); gotoFrame(S.curFrame + 1, true); }
  else if (k === "k" || k === "K") keepCurrent();
  else if (k === "l" || k === "L") labelLastKept();
  else if (k === "a" || k === "A") { $("show-all").checked = !$("show-all").checked; computeShown(); gotoFrame(S.curFrame); }
}

boot().catch((e) => {
  document.body.innerHTML = `<div style="padding:30px;color:#ff6b6b;font:15px sans-serif">${t("boot_fail", { e: esc(e.message) })}</div>`;
});
