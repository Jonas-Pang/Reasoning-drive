/* Reasoning Driving demo page */
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const LANG_KEY = "lane-demo-lang", TASK_KEY = "lane-demo-task";
const ACTS = ["cross_line", "go_straight", "turn_left", "turn_right", "u_turn", "enter_center_lane_to_wait"];
const ACTS_L = ["change_left", "change_right", "go_straight", "turn_left", "turn_right", "u_turn", "enter_waiting_area"];

const TXT = {
  zh: {
    region: "地区", mode_mock: "模拟", mode_real: "真实 API", settings: "模型设置", lang: "English", images: "已标注的图",
    all_types: "全部类型", use_cache: "相同请求用缓存（不重复花钱）", tab_prompt: "提示词", tab_batch: "批量运行", tab_io: "输入 / 输出设计",
    ask: "问模型 · Test {t}", ask_both: "A 和 B 都问", asking: "正在问模型（Test {t}）…", test_A: "Test A · 只有图片", test_B: "Test B · 图片 + 法规",
    key_ok: "API key 已设置 {h}", key_missing: "没有 API key", banner_mock: "模拟模式：答案是程序编的（Test A 故意多错一些），没有调用模型，也不花钱。演示真实结果请切到“真实 API”。",
    banner_nokey: "真实 API 模式需要 API key：在 .env 里设置 OPENAI_API_KEY（见 README）。",
    prompt_help: "这是发给模型的完整文字（图片另外附上）。Test B 只比 Test A 多了下面的法规条文，以及指令里标蓝的两行；其余部分两组完全一样。",
    p_instructions: "① 指令（developer 消息）。两组只有标蓝的两行不同",
    p_rules: "①′ 法规条文：只在 Test B，接在指令后面（同一条 developer 消息）", p_user: "② 用户消息（后面附上画了青色框的图片）", p_schema: "③ 输出格式（JSON schema，严格模式）",
    batch_help: "对当前地区所有已标注的图跑一遍（选 A + B 时两组同时跑，跑完自动比较），结果存在 results/runs/ 里。0 = 全部。勾选了“用缓存”时，问过的相同请求直接用旧答案（不花钱）。",
    limit: "张数", repeats: "重复次数", run: "开始运行", runs: "运行记录（点两条再比较）", compare: "比较选中的两次", compare_help: "McNemar 配对检验",
    cancel: "取消", apply: "应用", save_default: "同时保存为默认设置（写入 configs/api.yaml 或 configs/experiment.yaml）",
    settings_help: "这些设置对 Test A 和 Test B 完全一样。点“应用”只改这次打开的页面；勾选下面一项才会写进 configs/api.yaml（模型设置）或 configs/experiment.yaml（其余设置），文件里的注释保留。API key 不在这里，放在 .env 里。",
    reload: "从文件重新读取", unsaved: "还没写进 configs/ 的修改：{k}", all_saved: "页面上的设置和 configs/ 里的文件一致。",
    field: "项目", label: "标注（标准答案）", answer: "模型回答", o1: "输出 1", o2: "输出 2", cite: "引用",
    marking_type: "标线类型", arrow_type: "箭头类型", position: "位置", evidence: "证据", cited_rule_id: "引用的条文",
    description: "描述", reasoning: "理由", st_look: "1 看", st_rule: "2 规则", st_decide: "3 决定", st_check: "4 检查", st_none: "（这个提示词版本没有单独写）", st_after: "写在决定之后", st_summary: "模型对自己内部推理的总结（API 返回）", cited_passage: "引用条文原文", tokens: "tokens", latency: "耗时", cost: "费用", cached: "缓存", mock: "模拟",
    running: "运行中 {d}/{n}…", finished: "完成：{id}", none: "—", err: "出错：",
    eg_correct: "正确", eg_wrong: "错误", eg_unsupported_guess: "无依据猜测", eg_appropriate_withholding: "恰当保留", eg_over_withholding: "过度保留",
    c_accepted: "引用正确", c_in_pack_not_accepted: "引用了不支持答案的条文", c_unlisted: "编造的编号", c_none: "没有引用", c_none_needed: "无需引用（正确）",
    unsafe: "不安全错误", cautious: "过度保守", contested: "有争议的格子（单独统计）",
    cmp_n: "共同的图", cmp_acc: "{x} 准确率", cmp_only: "只有 {x} 对", cmp_p: "p 值", cmp_same: "两次设置相同、共同的提示词部分相同",
    no_items: "这个地区还没有已完成的标注。", pick_two: "先在列表里点选两次运行。", run_n: "运行", r_errors: "出错", r_readable: "可读的回答",
    task_lane: "车道级", task_marking: "单条标线（M4）", split: "划分", split_dev: "开发集", split_test: "测试集", split_any: "全部",
    f_all: "全部", f_arrow: "有箭头或文字", f_yellow: "有黄线", f_solid: "有实线", f_saved: "正式运行里有回答", f_diff: "A 和 B 的动作结论不同",
    show_lines: "显示标注时画的边界线（只用于对照，不发给模型）", saved_btn: "看正式运行里的回答（不花钱）",
    saved_none: "已保存的运行里没有这张图的回答。", from_run: "来自运行 {id}",
    from_run_note: "这是正式运行时保存的回答（{model} · {prompt}），这次没有调用模型。",
    l_count: "车道数", l_ego: "我的车道（从左数）", l_left: "左边界", l_right: "右边界", l_role_left: "左边界的作用", l_role_right: "右边界的作用",
    l_marks: "车道内标线", l_cite: "引用的条文", near: "靠近我的是", curb: "路缘",
    sc_lane: "车道识别", sc_acts: "动作", sc_contra: "自相矛盾", sc_added: "多报", sc_missed: "漏报",
    L1: "1 场景", L2: "2 两侧边界", L3: "3 车道内标线", L4: "4 交叉检查", L5: "5 规则", L6: "6 每个动作的理由", L7: "7 反思检查",
    Lfinal: "最终决定（在上面 7 步之后才写出）", Ladvice: "建议",
    thinking_note: "下面是模型自己写出的推理，顺序就是它写的顺序：先观察，再检查、套规则、给理由、反思，最后才写决定。",
    raw: "原始输出（JSON，按模型写出的顺序）", side_left: "左", side_right: "右", none_marks: "车道内没有标线", no_rule: "没有引用条文",
    lanes_of: "{n} 条车道，我在第 {k} 条，证据 {e}",
    cc_position: "车道位置", cc_roles: "边界的作用", cc_markings: "标线之间", cc_unseen: "没看到却写了的", cc_result: "结论",
    v_allowed: "允许", v_prohibited: "禁止", v_not_determined: "无法判断", v_not_applicable: "不适用",
    a_change_left: "向左变道", a_change_right: "向右变道", a_go_straight: "直行", a_turn_left: "左转", a_turn_right: "右转", a_u_turn: "掉头",
    a_enter_waiting_area: "进入待转区或双向左转车道",
    k_lane: "车道识别", k_lane_core: "车道识别（不算横向线）", k_output2: "动作", k_both_boundaries: "两侧边界", k_markings: "标线集合", k_no_unsafe: "没有不安全错误",
    cmp_diff: "差值", cmp_diff_note: "差值：后一次减前一次，百分点；下方是 95% 区间。", review_link: "盲审", project_link: "项目：结果、法规、仿真",
    r_lane: "车道", r_acts: "动作", r_unsafe: "不安全",
    prompt_help_lane: "这是发给模型的完整文字（照片另外附上，不画框）。模型必须按 7 个步骤依次写：场景、两侧边界、车道内标线、交叉检查、规则、每个动作的理由、反思，最后才写动作。Test B 只比 Test A 多了下面的法规条文，以及指令里标蓝的两处；其余完全一样。",
    p_user_lane: "② 用户消息（后面附上照片，不画框）",
    batch_help_lane: "对当前地区、所选划分里所有车道标注的图跑一遍（选 A + B 时两组同时跑，跑完自动比较），结果存在 results/runs/ 里，文件夹名带 lane。0 = 全部。勾选了“用缓存”时，问过的相同请求直接用旧答案（不花钱）。",
    no_lane_items: "这个地区、这个划分还没有完成的车道标注。",
    upload_btn: "上传图片", upload_help: "任意路面照片（JPEG/PNG/WebP，≤10 MB），按当前地区提问；没有标注，所以不评分。", uploaded: "已上传：{n}。点“问模型”开始。",
    upload_tag: "上传", no_label: "上传的图片没有标注，只检查答案内部的矛盾。",
    t_copy: "复制文字", t_print: "打印", t_close: "关闭", think_title: "模型的思考过程",
    t_note: "模型按提示词的 7 个步骤依次写出回答：先观察，再检查、套规则、给理由、反思，最后才写决定。新请求一边写一边显示；缓存或保存的回答按原来的顺序回放。",
    ph_start: "已发送请求，模型在思考（隐藏推理，effort {e}）…", ph_writing: "模型正在按步骤写出回答…", ph_replay_cache: "缓存里的回答，按模型写出的顺序回放",
    ph_replay_mock: "模拟答案（没有调用模型），按顺序回放", ph_replay_saved: "保存的回答，按模型写出的顺序回放", ph_done: "完成", ph_error: "出错",
    t_summary: "模型对自己隐藏推理的总结（API 返回）", t_raw: "逐字输出（模型写出的原始 JSON）", t_waiting: "等待", t_writing: "正在写",
    t_view: "查看思考过程", t_checks: "答案内部的矛盾", t_no_checks: "没有发现矛盾", copied: "已复制",
    bl_job: "批量运行过程 · Test {t} · {r}", bl_run: "运行 {id} 的每张图", bl_open: "查看运行过程", bl_each: "查看每张图的思考过程", bl_view: "查看",
  },
  en: {
    region: "Region", mode_mock: "Mock", mode_real: "Real API", settings: "Model settings", lang: "中文", images: "Labeled images",
    all_types: "All types", use_cache: "Reuse cached answers for identical requests", tab_prompt: "Prompt", tab_batch: "Batch run", tab_io: "Input / output design",
    ask: "Ask the model · Test {t}", ask_both: "Ask A and B", asking: "Asking the model (Test {t}) …", test_A: "Test A · image only", test_B: "Test B · image + rules",
    key_ok: "API key set {h}", key_missing: "No API key", banner_mock: "Mock mode: the answers are made up by the program (Test A makes more mistakes on purpose); no model is called and nothing is paid. Switch to Real API for real results.",
    banner_nokey: "Real API mode needs an API key: set OPENAI_API_KEY in .env (see the README).",
    prompt_help: "The full text sent to the model (the image is attached separately). Test B only adds the rule passages below and changes the two highlighted lines; everything else is identical in both tests.",
    p_instructions: "① Instructions (developer message). Only the two highlighted lines differ between the tests",
    p_rules: "①′ Rule passages: Test B only, appended to the instructions (same developer message)", p_user: "② User message (followed by the image with the cyan box)", p_schema: "③ Output format (JSON schema, strict)",
    batch_help: "Run every labeled image of the current region (A + B runs both tests at the same time and compares them); results go to results/runs/. 0 = all. With 'reuse cached answers' ticked, identical requests asked before are not paid again.",
    limit: "Images", repeats: "Repeats", run: "Run", runs: "Runs (click two to compare)", compare: "Compare the two selected", compare_help: "McNemar paired test",
    cancel: "Cancel", apply: "Apply", save_default: "Also save as default (configs/api.yaml or configs/experiment.yaml)",
    settings_help: "These settings are identical for Test A and Test B. Apply changes this page session only; tick the box below to also write them into configs/api.yaml (model settings) or configs/experiment.yaml (the rest); comments are kept. The API key is not here; it lives in .env.",
    reload: "Reload from file", unsaved: "Not yet written to configs/: {k}", all_saved: "The page settings match the files in configs/.",
    field: "Field", label: "Label (ground truth)", answer: "Model answer", o1: "Output 1", o2: "Output 2", cite: "Citation",
    marking_type: "Marking type", arrow_type: "Arrow type", position: "Position", evidence: "Evidence", cited_rule_id: "Cited rule",
    description: "Description", reasoning: "Reasoning", st_look: "1 Look", st_rule: "2 Rule", st_decide: "3 Decide", st_check: "4 Check", st_none: "(not written separately in this prompt version)", st_after: "written after the decision", st_summary: "The model's summary of its hidden reasoning (from the API)", cited_passage: "Cited passage", tokens: "tokens", latency: "time", cost: "cost", cached: "cached", mock: "mock",
    running: "Running {d}/{n} …", finished: "Finished: {id}", none: "—", err: "Error: ",
    eg_correct: "correct", eg_wrong: "wrong", eg_unsupported_guess: "unsupported guess", eg_appropriate_withholding: "appropriate withholding", eg_over_withholding: "over-withholding",
    c_accepted: "citation accepted", c_in_pack_not_accepted: "cited a passage that does not support it", c_unlisted: "made-up ID", c_none: "no citation", c_none_needed: "no passage applies (right)",
    unsafe: "unsafe errors", cautious: "over-cautious", contested: "contested cells (separate)",
    cmp_n: "Shared images", cmp_acc: "{x} accuracy", cmp_only: "only {x} right", cmp_p: "p-value", cmp_same: "same settings and same shared prompt parts",
    no_items: "No finished labels for this region yet.", pick_two: "Click two runs in the list first.", run_n: "run", r_errors: "errors", r_readable: "readable answers",
    task_lane: "Lane", task_marking: "Single marking (M4)", split: "Split", split_dev: "development", split_test: "test", split_any: "all",
    f_all: "All", f_arrow: "Arrow or words", f_yellow: "Yellow line", f_solid: "Solid line", f_saved: "Answered in a run", f_diff: "A and B differ on the actions",
    show_lines: "Show the boundary lines drawn while labeling (for checking only, never sent to the model)", saved_btn: "Show the answers from the runs (free)",
    saved_none: "No finished run has an answer for this image.", from_run: "from run {id}",
    from_run_note: "This is the answer saved by the run ({model} · {prompt}); the model was not called now.",
    l_count: "Lanes", l_ego: "My lane (from the left)", l_left: "Left boundary", l_right: "Right boundary", l_role_left: "Left boundary role", l_role_right: "Right boundary role",
    l_marks: "Markings in my lane", l_cite: "Cited rules", near: "nearer my lane:", curb: "curb",
    sc_lane: "Lane", sc_acts: "Actions", sc_contra: "contradictions", sc_added: "added", sc_missed: "missed",
    L1: "1 Scene", L2: "2 Boundaries", L3: "3 Markings in my lane", L4: "4 Cross-check", L5: "5 Rules", L6: "6 A reason per action", L7: "7 Reflect",
    Lfinal: "Decision (written after the seven steps)", Ladvice: "Advice",
    thinking_note: "Below is the model's own reasoning in the order it wrote it: it observes first, then checks, applies rules, gives reasons and reflects, and only then decides.",
    raw: "Raw output (JSON, in the order the model wrote it)", side_left: "Left", side_right: "Right", none_marks: "nothing painted in my lane", no_rule: "no rule cited",
    lanes_of: "{n} lanes, mine is number {k}, evidence {e}",
    cc_position: "Lane position", cc_roles: "Boundary roles", cc_markings: "Markings", cc_unseen: "Reported without seeing", cc_result: "Result",
    v_allowed: "allowed", v_prohibited: "prohibited", v_not_determined: "not determined", v_not_applicable: "not applicable",
    a_change_left: "change left", a_change_right: "change right", a_go_straight: "go straight", a_turn_left: "turn left", a_turn_right: "turn right", a_u_turn: "U-turn",
    a_enter_waiting_area: "enter waiting area / TWLTL",
    k_lane: "Lane identified", k_lane_core: "Lane identified (lines across the lane not counted)", k_output2: "Actions", k_both_boundaries: "Both boundaries", k_markings: "Marking set", k_no_unsafe: "No unsafe error",
    cmp_diff: "Diff.", cmp_diff_note: "Difference: second run minus first, in points; below it the 95% interval.", review_link: "Blind review", project_link: "Project: results, regulations, simulation",
    r_lane: "lane", r_acts: "actions", r_unsafe: "unsafe",
    prompt_help_lane: "The full text sent to the model (the photo is attached without a box). The model must write seven steps in order: scene, boundaries, markings, cross-check, rules, a reason per action, reflection, and only then the actions. Test B only adds the rule passages below and changes the two highlighted parts; everything else is identical.",
    p_user_lane: "② User message (followed by the photo, no box)",
    batch_help_lane: "Run every image with a final lane label in the current region and split (A + B runs both tests at the same time and compares them); results go to results/runs/, in folders named with 'lane'. 0 = all. With 'reuse cached answers' ticked, identical requests asked before are not paid again.",
    no_lane_items: "No finished lane labels for this region and split yet.",
    upload_btn: "Upload a photo", upload_help: "any road photo (JPEG/PNG/WebP, ≤10 MB), asked for the current region; no label, so no score.", uploaded: "Uploaded: {n}. Click Ask to start.",
    upload_tag: "upload", no_label: "An uploaded photo has no label; only contradictions inside the answer are checked.",
    t_copy: "Copy text", t_print: "Print", t_close: "Close", think_title: "How the model thinks",
    t_note: "The model writes its answer in the seven steps of the prompt: it observes first, then checks, applies rules, gives reasons and reflects, and only then decides. A new request is shown while it is written; a cached or saved answer is replayed in the order it was written.",
    ph_start: "Request sent; the model is thinking (hidden reasoning, effort {e}) …", ph_writing: "The model is writing its answer step by step …", ph_replay_cache: "Answer from the cache, replayed in the order it was written",
    ph_replay_mock: "Mock answer (no model called), replayed in order", ph_replay_saved: "Saved answer, replayed in the order it was written", ph_done: "done", ph_error: "error",
    t_summary: "The model's summary of its hidden reasoning (from the API)", t_raw: "Raw output as written (JSON)", t_waiting: "waiting", t_writing: "writing",
    t_view: "Show the thinking", t_checks: "Contradictions inside the answer", t_no_checks: "none found", copied: "Copied",
    bl_job: "Batch run · Test {t} · {r}", bl_run: "Each image of run {id}", bl_open: "Show the progress", bl_each: "Each image's thinking", bl_view: "view",
  },
};
const IO = {
  zh: `<h4>输入</h4><ul>
<li><b>图片</b>：标注时画的目标框用青色画在图片的副本上，原图不改。和指令一起发给模型（<code>detail: high</code>）。</li>
<li><b>地区</b>：一句话“This photo was taken in the United States / China”，两组都有。</li>
<li><b>指令</b>：<code>prompts/&lt;版本&gt;/</code> 里的文件：角色、处理步骤（看、规则、决定、检查）、每个输出字段的含义。只定义题目，不含任何地区的规则。</li>
<li><b>Test B 额外加上</b>：这个地区的全部法规条文（在 <code>regulations/&lt;代码&gt;/</code> 里），每条带编号、出处、章节和页码。只能引用这些编号。</li></ul>
<h4>输出（严格 JSON schema，按顺序写）</h4><ol>
<li><code>description</code>、<code>evidence</code>、<code>marking</code>：看到了什么（输出 1）</li>
<li><code>rule_reasoning</code>、<code>cited_rule_id</code>：适用哪条规则、它怎么说</li>
<li><code>action_reasons</code>：每个动作一句理由</li>
<li><code>self_check</code>：对照任务定义检查</li>
<li><code>actions</code>：最后的决定（输出 2），6 个动作各自 allowed / prohibited / not_determined / not_applicable</li></ol>
<p class="small">决定写在推理之后，所以答案是从前面的步骤推出来的（提示词 v3）。v1、v2 的 <code>reasoning</code> 写在决定之后。</p>
<h4>怎么调用 API</h4><ul>
<li>OpenAI Responses API：<code>POST https://api.openai.com/v1/responses</code>，用标准库发请求，不依赖 SDK。</li>
<li>设置在 <code>configs/api.yaml</code> 的 <code>model</code> 部分：模型、reasoning_effort、reasoning_summary、temperature、图片清晰度、最大输出长度。两组完全相同。</li>
<li>API key 从 <code>.env</code> 里的 <code>OPENAI_API_KEY</code> 读取。</li>
<li>每次运行在 <code>results/runs/&lt;运行编号&gt;/</code> 保存设置、提示词哈希、原始回答、评分、token 用量，以及每个回答的推理步骤（<code>trace.md</code>）。</li></ul>
<h4>评分</h4><ul>
<li>输出 1：类型（箭头再加箭头类型）和标注相同才算对。</li>
<li>输出 2：标线管的每个动作都对才算对；有争议的格子单独统计。</li>
<li>还会统计：五组证据、引用检查（Test B）、不安全 / 过度保守错误、自相矛盾的回答，以及 A 对 B 的 McNemar 配对检验。</li></ul>
<h4>加一个新国家</h4><ol>
<li>把 <code>regulations/_template/</code> 复制成 <code>regulations/&lt;代码&gt;/</code> 并填好；或者在项目页（/project）上传这个国家标准的 PDF，让模型提取条文，检查后点“采用”。</li>
<li>每条条文带编号、出处、章节、页码、原文和英文；国家的名称、行驶方向和法规名称写在 <code>region.yaml</code> 里。</li>
<li>用标注工具标好这个国家的图，把工作区加进 <code>data.workspaces</code>，再把 <code>experiment.region</code> 改成这个代码。</li></ol>`,
  en: `<h4>Input</h4><ul>
<li><b>Image</b>: a copy with the labeled target box drawn in cyan (the original is not changed), sent with <code>detail: high</code>.</li>
<li><b>Region</b>: one sentence, "This photo was taken in the United States / China", in both tests.</li>
<li><b>Instructions</b>: the files in <code>prompts/&lt;version&gt;/</code>: role, procedure (look, rule, decide, check) and the meaning of every field. They define the task only; no region's rules are in them.</li>
<li><b>Test B adds</b>: every rule passage of the region (from <code>regulations/&lt;CODE&gt;/</code>) with its ID, source, section and page. Only these IDs may be cited.</li></ul>
<h4>Output (strict JSON schema, written in this order)</h4><ol>
<li><code>description</code>, <code>evidence</code>, <code>marking</code>: what is visible (Output 1)</li>
<li><code>rule_reasoning</code>, <code>cited_rule_id</code>: which rule applies and what it says</li>
<li><code>action_reasons</code>: one reason per action</li>
<li><code>self_check</code>: checked against the task definition</li>
<li><code>actions</code>: the decision (Output 2), six actions, each allowed / prohibited / not_determined / not_applicable</li></ol>
<p class="small">The decision is written after the reasoning, so the answer follows from the steps before it (prompt v3). In v1 and v2, <code>reasoning</code> came after the decision.</p>
<h4>How the API is called</h4><ul>
<li>OpenAI Responses API, <code>POST https://api.openai.com/v1/responses</code>, with the Python standard library (no SDK).</li>
<li>Settings under <code>model</code> in <code>configs/api.yaml</code>: model, reasoning_effort, reasoning_summary, temperature, image detail, max output tokens; identical in both tests.</li>
<li>The API key is read from <code>OPENAI_API_KEY</code> in <code>.env</code>.</li>
<li>Every run keeps settings, prompt hashes, raw answers, scores, token use and the reasoning steps of every answer (<code>trace.md</code>) in <code>results/runs/&lt;run_id&gt;/</code>.</li></ul>
<h4>Scoring</h4><ul>
<li>Output 1: the type (and arrow type for arrows) matches the label.</li>
<li>Output 2: every action the marking decides matches; contested cells are counted separately.</li>
<li>Also: the five evidence groups, the citation check (Test B), unsafe vs over-cautious errors, self-contradicting answers, and McNemar between A and B.</li></ul>
<h4>Adding a country</h4><ol>
<li>Copy <code>regulations/_template/</code> to <code>regulations/&lt;CODE&gt;/</code> and fill it in, or upload the country's standard (PDF) on the project page (/project), let the model extract the passages, check them and accept.</li>
<li>Every passage has an ID, source, section, page, original text and English; the country's name, driving side and standard go into <code>region.yaml</code>.</li>
<li>Label its images with the labeling tool, add the workspace to <code>data.workspaces</code> and set <code>experiment.region</code> to the new code.</li></ol>`,
};
const IO_LANE = {
  zh: `<h4>输入</h4><ul>
<li><b>照片</b>：原图重新编码后直接发给模型，不画框（<code>detail: high</code>）。标注时画的边界线只用于对照，不发给模型。</li>
<li><b>地区</b>：一句话“This photo was taken in the United States / China”和行驶方向，两组都有。</li>
<li><b>指令</b>：<code>prompts/lane_v1/</code> 里的文件：角色、7 个步骤、每个输出字段的含义。只定义题目，不含任何地区的规则。</li>
<li><b>Test B 额外加上</b>：这个地区的车道规则条文（<code>regulations/</code> 里的 MUTCD 或 GB 5768.3 条文），按“车道两侧的线、车道里的箭头和文字、特殊车道、横线、区域”分组，每条带编号和出处。只能引用这些编号。</li></ul>
<h4>输出（严格 JSON schema，必须按这个顺序写）</h4><ol>
<li><code>scene</code>、<code>lane_count</code>、<code>ego_lane_index</code>：场景、同方向几条车道、我在第几条</li>
<li><code>left_boundary</code>、<code>right_boundary</code>：先写看到了什么（<code>observation</code>），再填颜色、线型、路缘、作用、证据</li>
<li><code>lane_markings</code>：车道里每个箭头、文字、区域，先写观察</li>
<li><code>cross_check</code>：车道位置、边界作用、标线之间是否一致，有没有没看到却写了的</li>
<li><code>element_rules</code>：每个元素适用哪条规则（Test B 写条文编号）</li>
<li><code>action_reasons</code>：7 个动作各一句理由</li>
<li><code>decision_check</code>：像谨慎的司机一样反思一遍</li>
<li><code>actions</code>：最后才写的决定，7 个动作各自 allowed / prohibited / not_determined / not_applicable；然后是 <code>advice</code></li></ol>
<p class="small">决定写在所有推理之后，所以动作是从前面的观察、检查和规则推出来的；页面上的“推理步骤”就是这些字段，按模型写出的顺序显示。设置里打开 reasoning_summary 时，还会显示 API 返回的模型内部推理总结。</p>
<h4>评分</h4><ul>
<li>车道识别：两侧边界（颜色、线型、路缘）和车道内标线集合都和标注一致才算对。</li>
<li>动作：标注决定的每个动作都对才算对；按项目约定判断的格子单独统计。</li>
<li>还统计：不安全错误（标注禁止、模型允许）、多报和漏报的标线、答案里自相矛盾的地方、引用检查（Test B），以及 A 对 B 的 McNemar 配对检验。</li></ul>`,
  en: `<h4>Input</h4><ul>
<li><b>Photo</b>: the original image, re-encoded, without a box (<code>detail: high</code>). The boundary lines drawn while labeling are for checking only and are never sent.</li>
<li><b>Region</b>: one sentence, "This photo was taken in the United States / China", and the driving side, in both tests.</li>
<li><b>Instructions</b>: the files in <code>prompts/lane_v1/</code>: role, seven steps and the meaning of every field. They define the task only; no region's rules are in them.</li>
<li><b>Test B adds</b>: the region's lane rule passages (MUTCD or GB 5768.3 in <code>regulations/</code>), grouped as lines beside a lane, arrows and words, special lanes, lines across a lane and marked areas, each with its ID and source. Only these IDs may be cited.</li></ul>
<h4>Output (strict JSON schema, written in this order)</h4><ol>
<li><code>scene</code>, <code>lane_count</code>, <code>ego_lane_index</code>: the scene, how many lanes of my direction, which one is mine</li>
<li><code>left_boundary</code>, <code>right_boundary</code>: first what is seen (<code>observation</code>), then colour, pattern, curb, role, evidence</li>
<li><code>lane_markings</code>: every arrow, word and area in my lane, observation first</li>
<li><code>cross_check</code>: do lane position, boundary roles and markings agree; anything reported without being seen?</li>
<li><code>element_rules</code>: the rule for each element (Test B: the passage ID)</li>
<li><code>action_reasons</code>: one reason for each of the seven actions</li>
<li><code>decision_check</code>: a reflection as a cautious driver</li>
<li><code>actions</code>: the decision, written last: seven actions, each allowed / prohibited / not_determined / not_applicable; then <code>advice</code></li></ol>
<p class="small">The decision comes after all the reasoning, so the actions follow from the observations, checks and rules before them; the reasoning steps on the page are these fields in the order the model wrote them. With reasoning_summary turned on in the settings, the API's summary of the model's hidden reasoning is shown too.</p>
<h4>Scoring</h4><ul>
<li>Lane identified: both boundaries (colour, pattern, curb) and the set of markings in my lane match the label.</li>
<li>Actions: every action the label decides matches; cells decided by a project convention are counted separately.</li>
<li>Also: unsafe errors (label prohibits, answer allows), markings added or missed, contradictions inside the answer, the citation check (Test B), and McNemar between A and B.</li></ul>`,
};
const S = { passages: {}, blRows: [], blSince: 0, blMode: null, lang: "zh", task: "lane", split: "dev", runs: [], cfg: null, test: "A", region: "US", items: [], sel: null, results: {}, prompt: null, runsSel: [], poll: null };
try { S.lang = localStorage.getItem(LANG_KEY) || "zh"; S.task = localStorage.getItem(TASK_KEY) || "lane"; } catch (e) { /* storage not available */ }
const t = (k, v) => { let s = (TXT[S.lang] || TXT.zh)[k] ?? TXT.zh[k] ?? k; for (const [a, b] of Object.entries(v || {})) s = s.split("{" + a + "}").join(b); return s; };
const lane = () => S.task === "lane";
const tq = () => "task=" + S.task;
const vt = (v) => (TXT[S.lang] || {})["v_" + v] || v || "—";
const at = (a) => (TXT[S.lang] || {})["a_" + a] || a;
const chip = (v) => `<span class="chip v-${esc(v)}">${esc(vt(v))}</span>`;

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
  $("io-text").innerHTML = (lane() ? IO_LANE : IO)[S.lang];
  $("prompt-help").textContent = t(lane() ? "prompt_help_lane" : "prompt_help");
  $("p-user-h").textContent = t(lane() ? "p_user_lane" : "p_user");
  $("batch-help").textContent = t(lane() ? "batch_help_lane" : "batch_help");
  document.body.classList.toggle("lane", lane());
  for (const b of $("task-seg").querySelectorAll("button")) b.classList.toggle("on", b.dataset.task === S.task);
  $("split").value = S.split;
}
function renderTop() {
  const c = S.cfg.config;
  for (const b of $("test-seg").querySelectorAll("button")) b.classList.toggle("on", b.dataset.test === S.test);
  for (const b of $("mode-seg").querySelectorAll("button")) b.classList.toggle("on", (b.dataset.mock === "1") === !!c.mock);
  const k = $("keyinfo");
  k.textContent = c.api.api_key_set ? t("key_ok", { h: c.api.api_key_hint }) : t("key_missing");
  k.className = "pill " + (c.api.api_key_set ? "ok" : "bad");
  const pdir = lane() ? c.lane.prompt_dir : c.prompt.dir;
  $("modelinfo").textContent = `${c.api.model} · ${pdir.split("/").pop()} · effort ${c.api.reasoning_effort ?? "—"}` + ((S.cfg.unsaved || []).length ? " · *" : "");
  $("modelinfo").title = (S.cfg.unsaved || []).length ? t("unsaved", { k: S.cfg.unsaved.join(", ") }) : t("all_saved");
  const ban = $("banner");
  if (c.mock) { ban.textContent = t("banner_mock"); ban.classList.remove("hidden"); }
  else if (!c.api.api_key_set) { ban.textContent = t("banner_nokey"); ban.classList.remove("hidden"); }
  else ban.classList.add("hidden");
  const count = (code) => lane() ? ((S.cfg.lane_items_per_region || {})[code] || {})[S.split] || 0 : S.cfg.items_per_region[code] || 0;
  $("region").innerHTML = Object.entries(c.regions).map(([code, r]) =>
    `<option value="${esc(code)}"${code === S.region ? " selected" : ""}>${esc(S.lang === "zh" ? (r.name_zh || r.name) : r.name)} (${esc(code)}) · ${count(code)}</option>`).join("");
}
async function setCfg(changes) { S.cfg = await api("/api/config", changes); renderTop(); }

async function loadItems() {
  S.items = await api(`/api/items?${tq()}&region=${encodeURIComponent(S.region)}&split=${S.split}`);
  $("type-filter").value = "";
  renderFilter();
  renderItems();
  if (S.items.length) select(S.items[0].image_id);
  else { S.sel = null; $("img").removeAttribute("src"); $("imgmeta").textContent = t(lane() ? "no_lane_items" : "no_items"); $("results").innerHTML = ""; }
}
const LANE_FILTERS = {
  arrow: (i) => i.arrow, yellow: (i) => i.yellow, solid: (i) => i.solid, saved: (i) => i.saved && (i.saved.A || i.saved.B),
  diff: (i) => i.saved && i.saved.A && i.saved.B && i.saved.A.output2 !== i.saved.B.output2,
};
function renderFilter() {
  const cur = $("type-filter").value;
  if (lane()) {
    $("type-filter").innerHTML = `<option value="">${esc(t("f_all"))} (${S.items.length})</option>` +
      Object.entries(LANE_FILTERS).map(([k, f]) => `<option value="${k}"${k === cur ? " selected" : ""}>${esc(t("f_" + k))} (${S.items.filter(f).length})</option>`).join("");
    return;
  }
  const types = [...new Set(S.items.map((i) => i.marking))].sort();
  $("type-filter").innerHTML = `<option value="">${esc(t("all_types"))} (${S.items.length})</option>` +
    types.map((x) => `<option${x === cur ? " selected" : ""}>${esc(x)}</option>`).join("");
}
const okmark = (v) => v === true ? `<span class="ok">✓</span>` : v === false ? `<span class="bad">✗</span>` : "·";
function renderItems() {
  const f = $("type-filter").value;
  const rows = lane() ? S.items.filter((i) => !f || LANE_FILTERS[f](i)) : S.items.filter((i) => !f || i.marking === f);
  $("count").textContent = rows.length;
  $("items").innerHTML = rows.map((i) => {
    const thumb = `<img loading="lazy" src="/api/image?${tq()}&id=${encodeURIComponent(i.image_id)}&w=200" alt="">`;
    if (!lane()) return `<li data-id="${esc(i.image_id)}" class="${i.image_id === S.sel ? "sel" : ""}">${thumb}<div class="m"><b>${esc(i.marking)}</b><br>${esc(i.visibility)} · ${esc(i.collection)} · ${esc(i.split)}<br><span class="muted">${esc(i.image_id.slice(-12))}</span></div></li>`;
    if (i.upload) return `<li data-id="${esc(i.image_id)}" class="${i.image_id === S.sel ? "sel" : ""}">${thumb}<div class="m"><b class="up">${esc(t("upload_tag"))}</b> ${esc(i.name || "")}<br><span class="muted">${i.width}×${i.height} · …${esc(i.image_id.slice(-8))}</span></div></li>`;
    const sv = i.saved || {};
    const badge = sv.A || sv.B ? `<span class="badge" title="${esc(t("sc_lane") + " / " + t("sc_acts"))}">A ${sv.A ? okmark(sv.A.lane) + okmark(sv.A.output2) : "··"} · B ${sv.B ? okmark(sv.B.lane) + okmark(sv.B.output2) : "··"}</span>` : "";
    return `<li data-id="${esc(i.image_id)}" class="${i.image_id === S.sel ? "sel" : ""}">${thumb}<div class="m"><b>L ${esc(i.left || "—")} · R ${esc(i.right || "—")}</b><br>${esc(i.markings.join(" ") || "—")}<br><span class="muted">${esc(i.dataset)} · ${esc(i.split)} · …${esc(i.image_id.slice(-10))}</span> ${badge}</div></li>`;
  }).join("");
  for (const li of $("items").querySelectorAll("li")) li.addEventListener("click", () => select(li.dataset.id));
}
function imgUrl(id) { return `/api/image?${tq()}&id=${encodeURIComponent(id)}` + (lane() && $("show-lines").checked ? "&lines=1" : ""); }
function select(id) {
  S.sel = id; S.results = {};
  for (const li of $("items").querySelectorAll("li")) li.classList.toggle("sel", li.dataset.id === id);
  const it = S.items.find((i) => i.image_id === id);
  $("img").src = imgUrl(id);
  $("imgmeta").textContent = `${id} · ${it.dataset} · ${it.width}×${it.height}` + (lane() ? ` · ${it.split}` : "");
  $("results").innerHTML = ""; $("ask-msg").textContent = "";
  $("saved-btn").disabled = lane() && !(it.saved && (it.saved.A || it.saved.B));
  if (it.upload) $("imgmeta").textContent = `${it.name || id} · ${it.width}×${it.height} · ${t("upload_tag")}`;
}
async function loadPrompt() {
  S.prompt = await api(`/api/prompt?${tq()}&test=${S.test}&region=${encodeURIComponent(S.region)}`);
  const rb = S.prompt.rules_block || "";
  let ins = S.prompt.instructions;
  if (rb) ins = ins.replace(rb, "").replace(/\n+$/, "");
  ins = esc(ins);
  for (const slot of Object.values(S.prompt.slots || {})) ins = ins.replace(esc(slot), `<mark>${esc(slot)}</mark>`);
  $("p-instructions").innerHTML = ins;
  $("p-rules").textContent = rb;
  $("p-rules-wrap").classList.toggle("hidden", !rb);
  $("p-user").textContent = S.prompt.user_text + (lane() ? "\n[image: the photo, no box]" : "\n[image: the photo with the cyan box]");
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
function stepsHtml(r) {  // the answer fields in the order the model wrote them
  const a = r.answer, rs = a.action_reasons || null, resp = r.response || {}, m = a.marking || {};
  let h = `<ol class="steps"><li><b>${t("st_look")}</b> ${esc(a.description)} <span class="muted">(${esc(a.evidence)}; ${esc(m.marking_type)}${m.arrow_type ? " / " + esc(m.arrow_type) : ""})</span></li>`;
  h += `<li><b>${t("st_rule")}</b> ${a.rule_reasoning !== undefined ? esc(a.rule_reasoning) : `<span class="muted">${t("st_none")}</span>`}${a.cited_rule_id ? ` <span class="muted">[${esc(a.cited_rule_id)}]</span>` : ""}</li>`;
  h += `<li><b>${t("st_decide")}</b><table class="reasons">` + ACTS.filter((k) => (a.actions || {})[k] !== undefined)
    .map((k) => `<tr><td>${esc(k)}</td><td>${esc(a.actions[k])}</td><td>${rs ? esc(rs[k] || "") : ""}</td></tr>`).join("") + `</table></li>`;
  if (a.self_check !== undefined) h += `<li><b>${t("st_check")}</b> ${esc(a.self_check)}</li>`;
  h += `</ol>`;
  if (a.reasoning) h += `<p class="small"><b>${t("reasoning")}:</b> ${esc(a.reasoning)}${a.self_check === undefined ? ` <span class="muted">(${t("st_after")})</span>` : ""}</p>`;
  if (resp.reasoning_summary) h += `<div class="quote"><b>${t("st_summary")}</b><br>${esc(resp.reasoning_summary)}</div>`;
  else if (resp.reasoning_summary_note) h += `<p class="small muted">${esc(resp.reasoning_summary_note)}</p>`;
  return h;
}
function renderMarkingResults() {
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
      h += stepsHtml(r);
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

// ---- lane task: comparison with the label and the model's reasoning, step by step
function sideText(b) {
  if (!b || !b.color) return "—";
  let p = b.pattern || "";
  if (p === "solid_dashed" && b.near_line && b.near_line !== "not_applicable") p += ` (${t("near")} ${b.near_line})`;
  return `${b.color} ${p}` + (b.curb === "yes" ? ` + ${t("curb")}` : "");
}
const labSide = (L, s) => ({ color: L[s + "_color"], pattern: L[s + "_pattern"], near_line: L[s + "_near_line"], curb: L[s + "_curb"], role: L[s + "_role"], evidence: L[s + "_evidence"] });
const toks = (x) => (Array.isArray(x) ? x : String(x || "").split(";")).filter(Boolean);
function laneTags(r) {
  const sc = r.score;
  let h = (r.mock ? `<span class="tag warn">${t("mock")}</span>` : "") + (r.cached ? `<span class="tag">${t("cached")}</span>` : "") +
    (r.from_run ? `<span class="tag">${esc(t("from_run", { id: r.from_run.run_id }))}</span>` : "");
  if (!sc) return h;
  return h + `<div class="score"><span class="tag ${cls(sc.lane)}">${t("sc_lane")}${mark(sc.lane)}</span>` +
    `<span class="tag ${cls(sc.output2)}">${t("sc_acts")}${sc.output2 === null ? " —" : mark(sc.output2)}</span>` +
    (sc.unsafe.length ? `<span class="tag bad">${t("unsafe")}: ${esc(sc.unsafe.map(at).join(", "))}</span>` : "") +
    (sc.consistency.length ? `<span class="tag warn">${t("sc_contra")} ${sc.consistency.length}</span>` : "") +
    (sc.citation ? `<span class="tag ${["accepted", "none_needed"].includes(sc.citation) ? "ok" : "bad"}">${esc(t("c_" + sc.citation))}</span>` : "") + `</div>`;
}
function renderLaneResults() {
  const tests = ["A", "B"].filter((x) => S.results[x]);
  if (!tests.length) { $("results").innerHTML = ""; return; }
  const recs = tests.map((x) => S.results[x]);
  const L = recs[0].label || {};
  const row = (name, lab, cells) => `<tr><td>${esc(name)}</td><td>${lab}</td>${cells.map(([v, ok]) => `<td class="${cls(ok)}">${v}${mark(ok)}</td>`).join("")}</tr>`;
  const per = (f) => recs.map((r) => (r.answer ? f(r.answer, r.score || {}) : ["—", null]));
  const nz = (v) => (v === undefined ? null : v);
  const w = tests.length === 2 ? `<col style="width:20%"><col style="width:22%"><col><col>` : `<col style="width:28%"><col style="width:30%"><col>`;
  let h = `<div class="card"><table class="cmp"><colgroup>${w}</colgroup><tr><th>${t("field")}</th><th>${t("label")}</th>` +
    tests.map((x) => `<th class="test">${esc(t("test_" + x))}</th>`).join("") + `</tr>` +
    `<tr class="scores"><td></td><td></td>${recs.map((r) => `<td>${laneTags(r)}${r.error || (!r.answer && r.parse_error) ? `<div class="msg err">${esc(t("err") + (r.error || r.parse_error))}</div>` : ""}</td>`).join("")}</tr>`;
  h += row(t("l_count"), esc(L.lane_count || "—"), per((a, sc) => [esc(a.lane_count ?? "null"), nz((sc.scene || {}).lane_count)]));
  h += row(t("l_ego"), esc(L.ego_index || "—"), per((a, sc) => [esc(a.ego_lane_index ?? "null"), nz((sc.scene || {}).ego_index)]));
  for (const s of ["left", "right"]) {
    h += row(t("l_" + s), esc(sideText(labSide(L, s))), per((a, sc) => [esc(sideText(a[s + "_boundary"])), (sc.sides || {})[s] ? sc.sides[s].all : null]));
    h += row(t("l_role_" + s), esc(L[s + "_role"] || "—"), per((a, sc) => [esc((a[s + "_boundary"] || {}).role || "—"), nz((sc.role || {})[s])]));
  }
  h += row(t("l_marks"), esc(toks(L.markings).join(" ") || "—"), per((a, sc) => {
    const m = sc.markings;
    const extra = m && (m.added.length || m.missed.length) ? `<br><span class="small muted">${m.added.length ? t("sc_added") + " " + esc(m.added.join(" ")) : ""} ${m.missed.length ? t("sc_missed") + " " + esc(m.missed.join(" ")) : ""}</span>` : "";
    return [esc((a.lane_markings || []).map((x) => x.marking).join(" ") || "—") + extra, m ? m.exact : null];
  }));
  const contested = new Set(recs.flatMap((r) => (r.score ? Object.keys(r.score.contested) : [])));
  for (const k of ACTS_L) {
    h += row(at(k) + (contested.has(k) ? " ◆" : ""), L["act_" + k] ? chip(L["act_" + k]) : "—", per((a, sc) => [chip((a.actions || {})[k]),
      !sc.actions ? null : k in sc.actions ? sc.actions[k] : k in (sc.contested || {}) ? sc.contested[k] : null]));
  }
  if (tests.includes("B")) {
    h += row(t("l_cite"), esc(toks(L.accepted_rule_ids).join(", ") || "—"), recs.map((r) => !r.answer || r.test !== "B" ? ["—", null] :
      [esc(((r.score || {}).cited || []).join(", ") || "—"), r.score ? ["accepted", "none_needed"].includes(r.score.citation) : null]));
  }
  h += `</table>${contested.size ? `<p class="small muted">◆ ${t("contested")}</p>` : ""}</div><div class="details">`;
  for (const r of recs) {
    h += `<div class="card"><h3>${esc(t("test_" + r.test))} <span class="grow"></span>${r.answer ? `<button class="view-think" data-test="${r.test}">${t("t_view")}</button>` : ""}</h3>`;
    if (r.checks) h += `<p class="small">${t("no_label")} ${t("t_checks")}: ${esc(r.checks.join("; ") || t("t_no_checks"))}</p>`;
    if (r.answer) h += laneSteps(r);
    else if (r.text) h += `<pre class="prompt">${esc(r.text)}</pre>`;
    const u = (r.response || {}).usage || {};
    if (r.response) h += `<div class="small muted">${esc(r.response.model || "")} · ${t("tokens")} ${u.input_tokens ?? "?"} / ${u.output_tokens ?? "?"} · ${t("latency")} ${r.response.latency_s ?? "?"} s · ${t("cost")} $${r.cost_usd ?? 0}</div>`;
    if (r.from_run) h += `<div class="small muted">${esc(t("from_run_note", { model: r.from_run.model, prompt: r.from_run.prompt }))}</div>`;
    h += `</div>`;
  }
  $("results").innerHTML = h + `</div>`;
  for (const b of $("results").querySelectorAll(".view-think")) b.addEventListener("click", () => {
    const r = S.results[b.dataset.test];
    openThink({ image_id: r.image_id, region: r.region, tests: [r.test], replay: { [r.test]: r } });
  });
}
function laneSteps(r) {  // the answer fields in the order the model wrote them
  const a = r.answer, resp = r.response || {};
  let h = `<p class="note">${t("thinking_note")}</p><div class="lsteps">${stepBlocks(a, true, r.passages || {})}</div>`;
  if (resp.reasoning_summary) h += `<div class="quote"><b>${t("st_summary")}</b><br>${esc(resp.reasoning_summary)}</div>`;
  else if (resp.reasoning_summary_note) h += `<p class="small muted">${esc(resp.reasoning_summary_note)}</p>`;
  let raw = r.text || "";
  try { raw = JSON.stringify(JSON.parse(raw), null, 2); } catch (e) { /* keep the text as it came */ }
  h += `<details class="raw"><summary>${t("raw")}</summary><pre class="prompt">${esc(raw)}</pre></details>`;
  return h;
}
function renderResults() { return lane() ? renderLaneResults() : renderMarkingResults(); }
async function askModels(tests) {  // several tests are asked at the same time
  if (!S.sel) return;
  if (lane()) { const it = S.items.find((i) => i.image_id === S.sel) || {}; openThink({ image_id: S.sel, region: S.region, tests, upload: !!it.upload }); return; }
  const id = S.sel;
  $("ask-msg").textContent = t("asking", { t: tests.join(S.lang === "zh" ? "、" : " + ") }); $("ask-msg").className = "msg";
  const errs = [];
  await Promise.all(tests.map(async (test) => {
    try {
      const rec = await api("/api/ask", { image_id: id, test, cache: $("use-cache").checked, task: S.task });
      if (S.sel !== id) return;
      S.results[test] = rec; renderResults();
    } catch (e) { errs.push(`Test ${test}: ${e.message}`); }
  }));
  if (S.sel !== id) return;
  $("ask-msg").textContent = errs.length ? t("err") + errs.join(" · ") : "";
  $("ask-msg").className = errs.length ? "msg err" : "msg";
}
async function showSaved() {  // the answers of the finished runs, no new request
  if (!S.sel) return;
  const id = S.sel;
  try {
    const recs = await api("/api/saved?id=" + encodeURIComponent(id));
    if (S.sel !== id) return;
    S.results = recs; renderResults();
    $("ask-msg").textContent = Object.keys(recs).length ? "" : t("saved_none"); $("ask-msg").className = "msg";
  } catch (e) { $("ask-msg").textContent = t("err") + e.message; $("ask-msg").className = "msg err"; }
}


// ---- the thinking window: the model's answer shown while it is written (or replayed), step by step
const STEPS = [
  { k: "L1", keys: ["scene", "lane_count", "ego_lane_index", "scene_evidence"] }, { k: "L2", keys: ["left_boundary", "right_boundary"] },
  { k: "L3", keys: ["lane_markings"] }, { k: "L4", keys: ["cross_check"] }, { k: "L5", keys: ["element_rules"] }, { k: "L6", keys: ["action_reasons"] },
  { k: "L7", keys: ["decision_check"] }, { k: "Lfinal", keys: ["actions"], final: true }, { k: "Ladvice", keys: ["advice"] },
];
function closeJSON(t) {  // close the open strings, objects and arrays of a JSON text that is still being written
  const stack = []; let inStr = false, escp = false;
  for (const ch of t) {
    if (inStr) { if (escp) escp = false; else if (ch === "\\") escp = true; else if (ch === '"') inStr = false; continue; }
    if (ch === '"') inStr = true; else if (ch === "{" || ch === "[") stack.push(ch); else if (ch === "}" || ch === "]") stack.pop();
  }
  let u = t;
  if (inStr) u = (escp ? u.slice(0, -1) : u) + '"';
  u = u.replace(/[\s,:]+$/, "");
  return u + stack.reverse().map((c) => (c === "{" ? "}" : "]")).join("");
}
function partialJSON(text) {
  let t = text;
  for (let k = 0; k < 8 && t; k++) {
    try { return JSON.parse(closeJSON(t)); } catch (e) { /* cut back to the last complete item */ }
    const cut = Math.max(t.lastIndexOf(","), t.lastIndexOf("{"), t.lastIndexOf("["));
    if (cut <= 0) return null;
    t = t.slice(0, t[cut] === "," ? cut : cut + 1);
  }
  return null;
}
function stepBody(k, a, pas) {
  const side = (s) => { const b = a[s + "_boundary"]; if (!b) return "";
    return `<div class="bside"><b>${t("side_" + s)}</b>: ${esc(b.observation || "")}${b.color ? `<div class="attrs">→ ${esc(sideText(b))} · ${esc(b.role || "")} · ${esc(b.evidence || "")}</div>` : ""}</div>`; };
  const tbl = (keys, f) => `<table>${keys.map((x) => `<tr><td>${f(x)[0]}</td><td>${f(x)[1]}</td></tr>`).join("")}</table>`;
  switch (k) {
    case "L1": return esc(a.scene || "") + (a.lane_count !== undefined ? ` <span class="muted">(${esc(t("lanes_of", { n: a.lane_count ?? "?", k: a.ego_lane_index ?? "?", e: a.scene_evidence || "" }))})</span>` : "");
    case "L2": return side("left") + side("right");
    case "L3": { const m = a.lane_markings || []; return m.length ? `<ul>${m.map((x) => `<li><b>${esc(x.marking || "")}</b> <span class="muted">(${esc(x.evidence || "")})</span>: ${esc(x.observation || "")}</li>`).join("")}</ul>` : `<span class="muted">${t("none_marks")}</span>`; }
    case "L4": { const cc = a.cross_check || {}; return tbl(["position", "roles", "markings", "unseen", "result"].filter((x) => cc[x] !== undefined), (x) => [t("cc_" + x), esc(cc[x])]); }
    case "L5": { const r = a.element_rules || []; return r.length ? `<ul>${r.map((e) => { const p = e.rule_id ? (pas || {})[e.rule_id] : null;
      const txt = p ? (S.lang === "zh" && p.text_zh ? p.text_zh : p.text_en) : "";
      return `<li><b>${esc(e.element || "")}</b>: ${esc(e.meaning || "")} ${e.rule_id ? `<span class="muted">[${esc(e.rule_id)}]</span>` : `<span class="muted">(${t("no_rule")})</span>`}` +
        (p ? `<details><summary class="small muted">${esc(p.source || "")} ${esc(p.section || "")}</summary><div class="quote">${esc(txt)}</div></details>` : "") + `</li>`; }).join("")}</ul>` : `<span class="muted">${t("no_rule")}</span>`; }
    case "L6": { const r = a.action_reasons || {}; return tbl(ACTS_L.filter((x) => r[x] !== undefined), (x) => [esc(at(x)), esc(r[x])]); }
    case "L7": return esc(a.decision_check || "");
    case "Lfinal": { const r = a.actions || {}; return tbl(ACTS_L.filter((x) => r[x] !== undefined), (x) => [esc(at(x)), chip(r[x])]); }
    case "Ladvice": return esc(a.advice || "");
  }
  return "";
}
function stepBlocks(a, done, pas) {
  a = a || {};
  let last = -1;
  STEPS.forEach((st, i) => { if (st.keys.some((x) => a[x] !== undefined)) last = i; });
  return STEPS.map((st, i) => {
    const state = i < last || (i === last && done) || (done && last >= 0) ? "done" : i === last ? "active" : "pending";
    const tag = state === "active" ? ` <span class="small">· ${t("t_writing")}…</span>` : state === "pending" ? ` <span class="small">· ${t("t_waiting")}</span>` : "";
    return `<div class="tstep ${state}${st.final ? " final" : ""}"><div class="sh">${t(st.k)}${tag}</div><div class="sb">${state === "pending" ? "" : stepBody(st.k, a, pas)}</div></div>`;
  }).join("");
}
const TK = { cols: {}, es: [], timers: [] };
async function passagesOf(region) {
  if (!S.passages[region]) { try { S.passages[region] = await api("/api/passages?region=" + encodeURIComponent(region)); } catch (e) { S.passages[region] = {}; } }
  return S.passages[region];
}
function closeThink() {
  for (const es of TK.es) es.close();
  for (const tm of TK.timers) clearInterval(tm);
  TK.es = []; TK.timers = []; TK.cols = {};
  $("think").classList.add("hidden");
}
async function openThink(o) {
  closeThink();
  const c = S.cfg.config;
  const rn = (c.regions[o.region] || {});
  $("think-img").src = `/api/image?task=lane&id=${encodeURIComponent(o.image_id)}&w=360`;
  $("think-title").textContent = t("think_title");
  $("think-sub").textContent = `${o.image_id} · ${S.lang === "zh" ? (rn.name_zh || rn.name || o.region) : (rn.name || o.region)} · ${o.tests.map((x) => t("test_" + x)).join("  |  ")}` +
    (o.replay ? "" : ` · ${c.mock ? t("mock") : c.api.model + " · effort " + (c.api.reasoning_effort ?? "—")}`);
  $("think-cols").innerHTML = o.tests.map((x) => `<div class="tcol" id="tcol-${x}"><div class="thead"><b>${esc(t("test_" + x))}</b><span class="tstatus"></span><span class="ttimer"></span></div>
    <div class="tsum hidden"><b>${t("t_summary")}</b><div class="tsum-text"></div></div><div class="tsteps">${stepBlocks({}, false, {})}</div>
    <details class="traw" open><summary>${t("t_raw")}</summary><pre class="traw-text tcursor"></pre></details><div class="tfoot small muted"></div></div>`).join("");
  $("think").classList.remove("hidden");
  const pas = await passagesOf(o.region);
  for (const test of o.tests) {
    const st = TK.cols[test] = { text: "", summary: "", done: false, rec: null, t0: Date.now(), pas, dirty: false, phase: "" };
    const el = $("tcol-" + test);
    const setPhase = (txt, cls) => { const s2 = el.querySelector(".tstatus"); s2.textContent = txt; s2.className = "tstatus " + (cls || ""); };
    TK.timers.push(setInterval(() => { if (!st.done) el.querySelector(".ttimer").textContent = ((Date.now() - st.t0) / 1000).toFixed(1) + " s"; }, 200));
    const render = () => {
      st.dirty = false;
      const a = st.done && st.rec && st.rec.answer ? st.rec.answer : partialJSON(st.text);
      el.querySelector(".tsteps").innerHTML = stepBlocks(a, st.done, st.pas);
      const pre = el.querySelector(".traw-text"); pre.textContent = st.text; pre.classList.toggle("tcursor", !st.done); pre.scrollTop = pre.scrollHeight;
      if (st.summary) { el.querySelector(".tsum").classList.remove("hidden"); el.querySelector(".tsum-text").textContent = st.summary; }
    };
    const kick = () => { if (!st.dirty) { st.dirty = true; setTimeout(render, 90); } };
    const finish = (rec) => {
      st.done = true; st.rec = rec;
      if (rec.text && rec.text.length >= st.text.length) st.text = rec.text;
      render();
      const r = rec.response || {}, u = r.usage || {};
      setPhase(t("ph_done"), "done");
      el.querySelector(".ttimer").textContent = r.latency_s ? `${r.latency_s} s` : el.querySelector(".ttimer").textContent;
      el.querySelector(".tfoot").innerHTML = (rec.score ? laneTags(rec) : "") + (rec.checks ? `<div>${t("t_checks")}: ${esc(rec.checks.join("; ") || t("t_no_checks"))}</div>` : "") +
        (r.model ? `<div>${esc(r.model)} · ${t("tokens")} ${u.input_tokens ?? "?"} / ${u.output_tokens ?? "?"} · ${t("cost")} $${rec.cost_usd ?? 0}</div>` : "");
    };
    if (o.replay) {  // an answer already on the page: replayed in the order it was written
      const rec = o.replay[test];
      setPhase(rec.from_run ? t("ph_replay_saved") : rec.mock ? t("ph_replay_mock") : t("ph_replay_cache"));
      const parts = [["summary", (rec.response || {}).reasoning_summary || ""], ["text", rec.text || ""]];
      let pi = 0, pos = 0;
      const step = Math.max(16, Math.ceil((rec.text || "").length / 110));
      const tm = setInterval(() => {
        while (pi < parts.length && pos >= parts[pi][1].length) { pi++; pos = 0; }
        if (pi >= parts.length) { clearInterval(tm); finish(rec); return; }
        const [kind, body] = parts[pi], d = body.slice(pos, pos + step); pos += step;
        if (kind === "summary") st.summary += d; else st.text += d;
        kick();
      }, 14);
      TK.timers.push(tm);
      continue;
    }
    setPhase("…");
    const es = new EventSource(`/api/ask_stream?id=${encodeURIComponent(o.image_id)}&test=${test}&cache=${$("use-cache").checked ? 1 : 0}`);
    TK.es.push(es);
    es.addEventListener("status", (e) => { const d = JSON.parse(e.data);
      if (d.phase === "start") setPhase(d.mock ? t("ph_replay_mock") : t("ph_start", { e: d.effort ?? "—" }));
      else if (d.phase === "writing") setPhase(t("ph_writing"));
      else if (d.phase === "replay") setPhase(d.source === "mock" ? t("ph_replay_mock") : t("ph_replay_cache"));
      else if (d.note) setPhase(d.note); });
    es.addEventListener("reasoning", (e) => { st.summary += JSON.parse(e.data).d; kick(); });
    es.addEventListener("text", (e) => { st.text += JSON.parse(e.data).d; kick(); });
    es.addEventListener("done", (e) => { es.close(); const rec = JSON.parse(e.data); finish(rec);
      if (S.sel === o.image_id) { S.results[test] = rec; renderResults(); } });
    es.addEventListener("fail", (e) => { es.close(); st.done = true; setPhase(t("ph_error") + ": " + JSON.parse(e.data).message, "err"); render(); });
    es.onerror = () => { if (!st.done) { es.close(); st.done = true; setPhase(t("ph_error"), "err"); } };
  }
}
function traceText() {  // the thinking of the open window as plain text
  const lines = [$("think-title").textContent, $("think-sub").textContent, ""];
  for (const [test, st] of Object.entries(TK.cols)) {
    const a = (st.rec && st.rec.answer) || partialJSON(st.text) || {};
    lines.push(`=== ${t("test_" + test)} ===`);
    if (st.summary) lines.push(`${t("t_summary")}: ${st.summary}`);
    const div = document.createElement("div");
    for (const s2 of STEPS) { div.innerHTML = stepBody(s2.k, a, st.pas); lines.push(`${t(s2.k)}: ${div.innerText.replace(/\n+/g, " | ")}`); }
    lines.push("");
  }
  return lines.join("\n");
}

// ---- batch window: one line per answer, each opens its thinking
function blRow(r, runId) {
  const ok = (v) => (v === true ? `<span class="ok">✓</span>` : v === false ? `<span class="bad">✗</span>` : "—");
  return `<div class="bl-row"><span>${r.total ? `${r.done}/${r.total}` : r.done}</span><span>Test ${esc(r.test || "")}</span><span>…${esc((r.image_id || "").slice(-22))}</span>` +
    `<span>${t("r_lane")} ${ok(r.o1)} · ${t("r_acts")} ${ok(r.o2)}${r.unsafe ? ` · <span class="bad">${t("r_unsafe")} ${r.unsafe}</span>` : ""}</span>` +
    `<span class="muted">${r.cached ? t("cached") : r.mock ? t("mock") : r.latency_s ? r.latency_s + " s" : ""}</span><span class="bad small">${r.error ? esc(r.error.slice(0, 30)) : ""}</span>` +
    `<span>${lane() && !r.error ? `<button data-test="${esc(r.test)}" data-id="${esc(r.image_id)}" data-run="${esc(runId || "")}" data-region="${esc(r.region || "")}">${t("bl_view")}</button>` : ""}</span></div>`;
}
function bindRows() {
  for (const b of $("bl-list").querySelectorAll("button[data-id]")) b.addEventListener("click", async () => {
    try {
      const rec = await api(`/api/record?test=${b.dataset.test}&id=${encodeURIComponent(b.dataset.id)}` + (b.dataset.run ? "&run=" + encodeURIComponent(b.dataset.run) : ""));
      openThink({ image_id: rec.image_id, region: rec.region, tests: [rec.test], replay: { [rec.test]: rec } });
    } catch (e) { alert(e.message); }
  });
}
function renderBatchLog(p) {
  if (p) {
    $("bl-bar").style.width = p.total ? (100 * p.done / p.total) + "%" : "0";
    const ids = Object.values(p.run_ids || {});
    $("bl-status").textContent = p.running ? t("running", { d: p.done, n: p.total || "?" }) : (ids.length ? t("finished", { id: ids.join(" · ") }) : "") + (p.error ? "  " + t("err") + p.error : "");
  }
  $("bl-list").innerHTML = S.blRows.slice().reverse().map((r) => blRow(r, "")).join("");
  bindRows();
}
async function openBatchLog(o) {
  S.blMode = o;
  $("batchlog").classList.remove("hidden");
  if (o.run) {
    $("bl-title").textContent = t("bl_run", { id: o.run }); $("bl-bar").style.width = "100%"; $("bl-status").textContent = "";
    const rows = await api("/api/run_records?id=" + encodeURIComponent(o.run));
    $("bl-list").innerHTML = rows.map((r) => blRow(r, o.run)).join(""); bindRows();
    return;
  }
  $("bl-title").textContent = t("bl_job", { t: o.test || "", r: o.region || "" });
  renderBatchLog(await api("/api/progress?since=" + S.blSince).then((p) => { if (p.log) { S.blRows.push(...p.log); S.blSince = p.log_total; } return p; }));
}

// ---- a photo uploaded on the page
function uploadPhoto(file) {
  if (!file) return;
  if (file.size > 10 * 1024 * 1024) { $("ask-msg").textContent = t("err") + "> 10 MB"; $("ask-msg").className = "msg err"; return; }
  const rd = new FileReader();
  rd.onload = async () => {
    try {
      const r = await api("/api/upload", { name: file.name, region: S.region, data: rd.result });
      await loadItems(); select(r.image_id);
      $("ask-msg").textContent = t("uploaded", { n: file.name }); $("ask-msg").className = "msg ok";
    } catch (e) { $("ask-msg").textContent = t("err") + e.message; $("ask-msg").className = "msg err"; }
  };
  rd.readAsDataURL(file);
}

// ---- batch
async function startRun() {
  try {
    await api("/api/run", { task: S.task, test: $("b-test").value, region: S.region, split: lane() ? S.split : "any", limit: Number($("b-limit").value || 0),
      repeats: Number($("b-repeats").value || 1), cache: $("use-cache").checked });
    S.blRows = []; S.blSince = 0;
    openBatchLog({ job: true, test: $("b-test").value, region: S.region });
    pollRun();
  } catch (e) { $("b-status").textContent = t("err") + e.message; }
}
function pollRun() {
  clearInterval(S.poll);
  S.poll = setInterval(async () => {
    const p = await api("/api/progress?since=" + S.blSince);
    if (p.log) { S.blRows.push(...p.log); S.blSince = p.log_total; if (S.blMode && S.blMode.job) renderBatchLog(p); }
    $("b-bar").style.width = p.total ? (100 * p.done / p.total) + "%" : "0";
    const ids = Object.values(p.run_ids || {});
    $("b-status").textContent = p.running ? t("running", { d: p.done, n: p.total || "?" }) : (ids.length ? t("finished", { id: ids.join(" · ") }) : "") + (p.error ? "  " + t("err") + p.error : "");
    if (!p.running) {
      clearInterval(S.poll);
      if ((p.task || "marking") !== S.task) return;
      if (p.run_ids && p.run_ids.A && p.run_ids.B) {  // both tests ran together: compare them right away
        S.runsSel = [p.run_ids.A, p.run_ids.B];
        await loadRuns(); compareRuns(); showRun(p.run_ids.B);
      } else { await loadRuns(); if (p.run_id) showRun(p.run_id); }
      if (lane()) loadItems();
    }
  }, 800);
}
const pct = (x) => x === null || x === undefined ? "—" : Math.round(x * 100) + "%";
async function loadRuns() {
  const runs = S.runs = await api("/api/runs?" + tq());
  if (lane()) {
    $("runs").innerHTML = `<table class="runs"><tr><th>run</th><th>Test</th><th>n</th><th>${t("r_lane")}</th><th>${t("r_acts")}</th><th>${t("r_unsafe")}</th><th>$</th></tr>` +
      runs.map((r) => `<tr data-id="${esc(r.run_id)}" class="${S.runsSel.includes(r.run_id) ? "sel" : ""}"><td>${esc(r.run_id.slice(0, 15))} ${esc(r.region)}${r.mock ? " (mock)" : ""}</td><td>${r.test}</td><td>${r.n_items}</td><td>${pct(r.lane)}</td><td>${pct(r.output2)}</td><td>${r.unsafe ?? "—"}</td><td>${r.cost_usd ?? "—"}</td></tr>`).join("") + "</table>";
  } else {
    $("runs").innerHTML = `<table class="runs"><tr><th>run</th><th>Test</th><th>n</th><th>${t("o1")}</th><th>${t("o2")}</th><th>$</th></tr>` +
      runs.map((r) => `<tr data-id="${esc(r.run_id)}" class="${S.runsSel.includes(r.run_id) ? "sel" : ""}"><td>${esc(r.run_id.slice(0, 15))}${r.mock ? " (mock)" : ""}</td><td>${r.test}</td><td>${r.n_items}×${r.repeats}</td><td>${pct(r.output1)}</td><td>${pct(r.output2)}</td><td>${r.cost_usd ?? "—"}</td></tr>`).join("") + "</table>";
  }
  for (const tr of $("runs").querySelectorAll("tr[data-id]")) tr.addEventListener("click", () => {
    const id = tr.dataset.id;
    S.runsSel = S.runsSel.includes(id) ? S.runsSel.filter((x) => x !== id) : [...S.runsSel, id].slice(-2);
    loadRuns(); showRun(id);
  });
}
async function showRun(id) {
  const r = await api(`/api/run?${tq()}&id=` + encodeURIComponent(id));
  const s = r.summary || {};
  const f = (d) => d && d.n ? `${d.correct}/${d.n} (${Math.round(100 * d.correct / d.n)}%)` : "—";
  const cites = Object.entries(s.citations || {}).map(([k, v]) => `${t("c_" + k)} ${v}`).join(" · ");
  const common = `<tr><td>${t("tokens")} / ${t("cost")}</td><td>${(s.usage || {}).input_tokens ?? 0} / ${(s.usage || {}).output_tokens ?? 0} · $${s.cost_usd ?? 0}</td></tr>
    <tr><td>${t("r_errors")}</td><td>${s.errors ?? 0} · ${t("r_readable")} ${(s.readable || {}).n ?? 0}/${(s.readable || {}).of ?? 0} · ${t("cached")} ${s.cached ?? 0}</td></tr>`;
  if (lane()) {
    $("run-detail").innerHTML = `<div class="card"><h3>${esc(id)}</h3><table>
      <tr><td>${t("k_lane")}</td><td>${f(s.lane)}</td></tr><tr><td>${t("k_output2")}</td><td>${f(s.output2)}</td></tr>
      <tr><td>${t("l_left")} / ${t("l_right")}</td><td>${f(s.left_boundary)} / ${f(s.right_boundary)}</td></tr>
      <tr><td>${t("k_both_boundaries")}</td><td>${f(s.both_boundaries)}</td></tr>
      <tr><td>${t("l_marks")}</td><td>${f(s.markings_exact)} · ${t("sc_added")} ${s.markings_added ?? 0} · ${t("sc_missed")} ${s.markings_missed ?? 0}</td></tr>
      <tr><td>${t("l_count")} / ${t("l_ego")}</td><td>${f(s.lane_count)} / ${f(s.ego_index)}</td></tr>
      <tr><td>${t("unsafe")} / ${t("cautious")}</td><td>${s.unsafe_errors ?? 0} / ${s.over_cautious_errors ?? 0} <span class="muted">(◆ ${s.contested_unsafe_errors ?? 0})</span></td></tr>
      <tr><td>${t("sc_contra")}</td><td>${s.inconsistent_answers ?? 0}</td></tr>${cites ? `<tr><td>${t("cite")}</td><td>${esc(cites)}</td></tr>` : ""}${common}</table>
      <div class="row"><button id="run-each">${t("bl_each")}</button></div></div>`;
    $("run-each").addEventListener("click", () => openBatchLog({ run: id }));
    return;
  }
  const groups = Object.entries(s.evidence_groups || {}).map(([k, v]) => `${t("eg_" + k)} ${v}`).join(" · ");
  $("run-detail").innerHTML = `<div class="card"><h3>${esc(id)}</h3><table>
    <tr><td>${t("o1")}</td><td>${f(s.output1)}</td></tr><tr><td>${t("o2")}</td><td>${f(s.output2)}</td></tr>
    <tr><td>${t("contested")}</td><td>${f(s.contested)}</td></tr>
    <tr><td>${t("unsafe")} / ${t("cautious")}</td><td>${s.unsafe_errors ?? 0} / ${s.over_cautious_errors ?? 0} <span class="muted">(◆ ${s.contested_unsafe_errors ?? 0} / ${s.contested_over_cautious_errors ?? 0})</span></td></tr>
    <tr><td>${t("evidence")}</td><td>${esc(groups)}</td></tr>${cites ? `<tr><td>${t("cite")}</td><td>${esc(cites)}</td></tr>` : ""}${common}</table></div>`;
}
async function compareRuns() {
  if (S.runsSel.length !== 2) { $("compare-out").textContent = t("pick_two"); return; }
  try {
    const testOf = (id) => (S.runs.find((r) => r.run_id === id) || {}).test || "";
    const [ra, rb] = [...S.runsSel].sort((x, y) => testOf(x).localeCompare(testOf(y)) || x.localeCompare(y));  // Test A first
    const c = await api(`/api/compare?${tq()}&a=${encodeURIComponent(ra)}&b=${encodeURIComponent(rb)}`);
    const same = c.tests[0] === c.tests[1];
    const n1 = "Test " + c.tests[0] + (same ? " (" + t("run_n") + " 1)" : ""), n2 = "Test " + c.tests[1] + (same ? " (" + t("run_n") + " 2)" : "");
    const keys = lane() ? ["lane", "lane_core", "output2", "both_boundaries", "markings", "no_unsafe"].filter((k) => c[k]) : ["output1", "output2"];
    const pp = (v) => (v > 0 ? "+" : "") + Math.round(v * 1000) / 10;
    const diff = (d) => d.diff === undefined || d.diff === null ? "—" : `${pp(d.diff)}<br><span class="muted small">${pp(d.ci95[0])}…${pp(d.ci95[1])}</span>`;
    const name = (k) => lane() ? t("k_" + k) : t(k === "output1" ? "o1" : "o2");
    const row = (k) => { const d = c[k]; return `<tr><td>${esc(name(k))}</td><td>${d.n}</td><td>${pct(d.acc_A)}</td><td>${pct(d.acc_B)}</td><td>${d.only_B_right}</td><td>${d.only_A_right}</td><td>${d.p_value === null ? "—" : d.p_value < 0.001 ? "<0.001" : d.p_value.toFixed(3)}</td>${lane() ? `<td>${diff(d)}</td>` : ""}</tr>`; };
    const unsafe = lane() && c.unsafe_errors ? `<p class="small">${t("unsafe")}: ${esc(n1)} ${c.unsafe_errors.A} · ${esc(n2)} ${c.unsafe_errors.B}</p>` : "";
    $("compare-out").innerHTML = `<div class="card"><table><tr><th></th><th>${t("cmp_n")}</th><th>${esc(t("cmp_acc", { x: n1 }))}</th><th>${esc(t("cmp_acc", { x: n2 }))}</th><th>${esc(t("cmp_only", { x: n2 }))}</th><th>${esc(t("cmp_only", { x: n1 }))}</th><th>${t("cmp_p")}</th>${lane() ? `<th>${t("cmp_diff")}</th>` : ""}</tr>${keys.map(row).join("")}</table>${unsafe}
      ${lane() ? `<p class="small muted">${t("cmp_diff_note")}</p>` : ""}<p class="small ${c.same_settings && c.same_shared_prompt ? "" : "msg err"}">${t("cmp_same")}: ${c.same_settings && c.same_shared_prompt ? "✓" : "✗"}</p></div>`;
  } catch (e) { $("compare-out").textContent = t("err") + e.message; }
}

// ---- settings
function openSettings() {
  const c = S.cfg.config, a = c.api;
  $("s-model").value = a.model; $("s-effort").value = a.reasoning_effort ?? ""; $("s-temp").value = a.temperature ?? "";
  $("s-detail").value = a.image_detail; $("s-max").value = a.max_output_tokens; $("s-par").value = a.parallel; $("s-save").checked = false;
  $("s-lmax").value = c.lane.max_output_tokens ?? "";
  const cur = c.prompt.dir.split("/").pop(), lcur = c.lane.prompt_dir.split("/").pop();
  $("s-prompt").innerHTML = (S.cfg.prompt_versions || [cur]).map((v) => `<option${v === cur ? " selected" : ""}>${esc(v)}</option>`).join("");
  $("s-lprompt").innerHTML = (S.cfg.lane_prompt_versions || [lcur]).map((v) => `<option${v === lcur ? " selected" : ""}>${esc(v)}</option>`).join("");
  $("s-summary").value = a.reasoning_summary || "off";
  renderUnsaved();
  $("settings").classList.remove("hidden");
}
function renderUnsaved() {
  const u = S.cfg.unsaved || [];
  $("s-unsaved").textContent = u.length ? t("unsaved", { k: u.join(", ") }) : t("all_saved");
}
async function applySettings() {
  try {
    await setCfg({ "api.model": $("s-model").value.trim(), "api.reasoning_effort": $("s-effort").value.trim(), "api.temperature": $("s-temp").value.trim(),
      "api.image_detail": $("s-detail").value, "api.max_output_tokens": Number($("s-max").value), "api.parallel": Number($("s-par").value),
      "prompt.dir": "prompts/" + $("s-prompt").value, "lane.prompt_dir": "prompts/" + $("s-lprompt").value, "lane.max_output_tokens": $("s-lmax").value.trim(),
      "api.reasoning_summary": $("s-summary").value, save: $("s-save").checked });
    $("settings").classList.add("hidden"); loadPrompt();
  } catch (e) { alert(e.message); }
}

async function setTask(task) {
  S.task = task; S.results = {}; S.runsSel = [];
  try { localStorage.setItem(TASK_KEY, task); } catch (e) { /* ignore */ }
  applyStatic(); renderTop();
  await loadItems(); await loadPrompt();
  if (!$("pane-batch").classList.contains("hidden")) loadRuns();
  $("run-detail").innerHTML = ""; $("compare-out").innerHTML = "";
}
async function boot() {
  applyStatic();
  S.cfg = await api("/api/config");
  S.test = S.cfg.config.run.test; S.region = S.cfg.config.run.region;
  renderTop();
  for (const b of $("task-seg").querySelectorAll("button")) b.addEventListener("click", () => setTask(b.dataset.task));
  for (const b of $("test-seg").querySelectorAll("button")) b.addEventListener("click", async () => { S.test = b.dataset.test; await setCfg({ "run.test": S.test }); loadPrompt(); });
  for (const b of $("mode-seg").querySelectorAll("button")) b.addEventListener("click", () => setCfg({ mock: b.dataset.mock === "1" }));
  $("region").addEventListener("change", async () => { S.region = $("region").value; await setCfg({ "run.region": S.region }); loadItems(); loadPrompt(); });
  $("split").addEventListener("change", () => { S.split = $("split").value; renderTop(); loadItems(); });
  $("type-filter").addEventListener("change", renderItems);
  $("show-lines").addEventListener("change", () => { if (S.sel) $("img").src = imgUrl(S.sel); });
  $("ask-a").addEventListener("click", () => askModels(["A"]));
  $("ask-b").addEventListener("click", () => askModels(["B"]));
  $("ask-both").addEventListener("click", () => askModels(["A", "B"]));
  $("saved-btn").addEventListener("click", showSaved);
  $("upload-btn").addEventListener("click", () => $("upload-file").click());
  $("upload-file").addEventListener("change", () => { uploadPhoto($("upload-file").files[0]); $("upload-file").value = ""; });
  $("think-close").addEventListener("click", closeThink);
  $("think-print").addEventListener("click", () => window.print());
  $("think-copy").addEventListener("click", async () => { try { await navigator.clipboard.writeText(traceText()); $("think-copy").textContent = t("copied"); setTimeout(() => { $("think-copy").textContent = t("t_copy"); }, 1500); } catch (e) { alert(e.message); } });
  $("b-open").addEventListener("click", () => openBatchLog({ job: true, test: $("b-test").value, region: S.region }));
  $("bl-close").addEventListener("click", () => { $("batchlog").classList.add("hidden"); S.blMode = null; });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") { if (!$("think").classList.contains("hidden")) closeThink(); else $("batchlog").classList.add("hidden"); } });
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
  $("s-reload").addEventListener("click", async () => {
    S.cfg = await api("/api/config", { reload: true }); S.test = S.cfg.config.run.test; S.region = S.cfg.config.run.region;
    renderTop(); openSettings(); loadItems(); loadPrompt();
  });
  $("lang-btn").addEventListener("click", () => { S.lang = S.lang === "zh" ? "en" : "zh"; try { localStorage.setItem(LANG_KEY, S.lang); } catch (e) { /* ignore */ } applyStatic(); renderTop(); renderResults(); renderFilter(); renderItems(); if (S.prompt) loadPrompt(); });
  await loadItems();
  await loadPrompt();
  const p = await api("/api/progress"); if (p.running) pollRun();
}
boot().catch((e) => { document.body.innerHTML = `<div style="padding:30px;color:#ff6b6b">${esc(e.message)}</div>`; });
