# 交接说明：CARLA 违规视频 + 回灌诊断（Reasoning Driving 项目）

> 写给接手的 Claude（在 Windows 电脑上工作）。请先通读一遍，再按第 6 节的顺序做。整理于 2026-11-18。
> 和用户交流**一律用中文**。

> **2026-11-18 晚更新（重要）：** 第 3 节“回灌诊断”的网页部分已经在 Mac 端做完了（`reasoning_drive/web/video.py`，网页 Video 页签，Grafana 面板和告警也加了）。**Windows 端只需要做第 2 节：录违规视频 + 输出事件文件**，不要再改 `reasoning_drive/web/` 下的文件，免得两边冲突。
> 事件文件格式以 `START_HERE.md` 第 7 节为准：JSON 列表，每项 `{"t": 秒, "action": "turn_right", "truth": "prohibited", "note": "..."}`，`t` 是动作在**导出片段里**开始的秒数（如果片段是 2× 速度，时间也要按 2× 换算），`truth` 来自 CARLA 地图标线 + 规则表。每个片段配一个同名的 `.events.json`。

---

## 0. 一句话目标

在 CARLA 里录一段 **自车真的做出违规动作** 的行车视频（例如：左转专用道却右转、越双黄线超车、右转专用道却直行），然后做一个 **“回灌诊断”**：
上传视频（+ 行车日志）→ 系统自动找到自车做动作的那一刻 → 取出那一帧 → 用本项目的感知层（车道线识别 + 当地法规）判断这一刻允许做什么 → 判定是否违规，并**自动归因是感知层还是决策层的错**。
这样就把 **感知层（本项目已完成）→ 决策层 → 控制层** 串起来讲清楚，也就是自动驾驶里的“视频回灌”测试。

---

## 1. 项目背景（必须知道的）

- 课程：UF AI Systems 课程项目 “Reasoning Driving”。
- 任务：给一张行车照片 + 当地交通法规，视觉语言模型判断 **本车道左右两条线** 和 **7 个动作** 是否允许：
  `cross_line`（变道越线）、`go_straight`、`turn_left`、`turn_right`、`u_turn`、`enter_center_lane_to_wait`（进中心车道 / 待转区等待）等（完整定义见 `labeling/lanes.py` 和 `lane_schema.json`）。
- 三个测试：A = 只给照片；B = 照片 + 本地区法规；C = 照片 + **另一个地区** 的法规。
- 冻结的最终方案：提示词 **`lane_v4c`**，模型 **Gemma 4 31B**。不要改提示词和协议（要和已有结果可比）。
- 关键结果（31b + v4c，当前标签）：七个动作全对 A 0.611 / B 0.577 / C 0.616；变道错误 94/107 来自车道线认错。
- 校验层 `reasoning_drive/web/guard.py`：用规则表（`labeling/lanes.lane_prefill`）对照模型自己报的车道线，查自相矛盾 → `needs_review`。

### 1.1 位置

- 项目根目录在 T9 移动硬盘：Mac 上是 `/Volumes/T9/Project/Reasoning_Drive`，插到这台 Windows 上一般是 `F:\Project\Reasoning_Drive`（以实际盘符为准）。
- 先读：`START_HERE.md`（中文总览）、`docs/GUIDE_zh.md`、`docs/lane_advisor.md`。
- Windows 环境：`scripts\setup_windows.bat` 建 `.venv`（Python 3.11）；自检 `python main.py selftest`（已知 102 PASS、4 个旧测试 FAIL，属正常）。
- CARLA：**0.9.16** 已装在 `D:\Carla\CARLA_0.9.16`，带 carla 包的 Python 在 `D:\Carla\env916\Scripts\python.exe`（见 `configs/carla.yaml` 的 `server` 段）。显卡 RTX 2060 6 GB（官方最低配置），之前用 `-quality-level=Epic -ResX=1280 -ResY=720` 跑通过。
- 这台 Windows **跑不动本地大模型**（gemma4:12b 每张图 100–234 秒），模型一律用 **UF NaviGator**（见 1.3）。

### 1.2 已有的 CARLA 框架（直接在它上面改，不要重写）

- 命令：`python main.py carla route route1 --record [--mock] [--preview]`（`main.py carla --help` 看全部）。
- 代码：`reasoning_drive/simulation/route.py`（路线 + 站点 + 闭环决策）、`loop.py`（变道闭环，含 **车道入侵传感器** `invasions.jsonl`）、`route_video.py`（讲解视频）、`settings.py`、`scenarios.py`。
- 配置：`configs/carla.yaml`。`route1` 在 **Town03**，一圈 3015 m，7 个站点，每站有导航意图（**意图不告诉模型**）：

| 站点 | 标线 | 导航意图 | 美国规则 (B) | 中国规则 (C) |
|---|---|---|---|---|
| 1 | 白虚线 | 越线变道 | 允许 | 允许 |
| 2 | 左侧单黄实线 | 向左越过黄线 | 禁止 | 禁止 |
| 3 | 本车道右转箭头 | 在路口直行 | **禁止** | **禁止** |
| 4 | 环岛内白虚线 | 并到外侧车道出环岛 | 允许 | 允许 |
| 5 | 双黄实线 | 越过中心线超车 | **禁止** | **禁止** |
| 6 | 左转箭头 + 右侧白实线 | 在路口右转 | 右转**禁止**；先跨白实线变道：允许（有争议格） | 右转**禁止**；跨白实线也**禁止** |
| 7 | 双向左转中心车道 | 进中心车道等左转 | 允许 | 中国规则里没有这种车道 |

  （来源：`results/carla/20261113_185858_route1/stops.jsonl` 里的 labels；站点 6 右侧线地图写的是 yellow_solid，实际画的是白实线，有 `truth_override`。）
- **现在的闭环**：`drive_with: B` —— 车在每站先问 Test B，B 说禁止就不做（route1 那次 4 个违规意图全部被拦下）。这本身就是“感知 → 决策 → 控制”的雏形。
- 之前的运行结果都在 `results/carla/`（`20261113_185858_route1` 有 `frames/01–07.png` 到站原图、`nav_plan.json`、`findings.json`）。

### 1.3 已部署的系统（Mac 上已跑通）

- 网页：`main.py web`（`reasoning_drive/web/server.py`，前端 `web/static/app.html|app.js|app.css`）：Analyze / Feedback / Monitor 三个页签；`POST /api/app/predict`、`POST /api/feedback`、`GET /metrics`。
- 反馈与日志：`web/feedback.py`（`results/app/predictions.jsonl`、`feedback.csv`）；指标：`web/metrics.py`。
- Docker：`Dockerfile` + `docker-compose.yml`（demo 8770、Prometheus 9090、Grafana 3000，仪表盘 “Lane advisor – monitoring”，4 条告警规则在 `deploy/grafana/provisioning/alerting/rules.yml`，由 `claude_analysis/deploy_src/make_grafana.py` 生成）。
  - `scripts/deploy_demo.sh`、`docker_build.sh`、`rd.sh` 是 **Mac 的 bash 脚本**（`docker_build.sh` 是为了绕开 macOS 读 exFAT 的 `._` 文件问题）。Windows 上直接 `docker compose up -d --build` 即可；如需要可补一个 `scripts\deploy_demo.bat`。
- 模型：profile `nav_gemma4_31b_bf16`（`configs/api_profiles.yaml`，NaviGator，`https://api.navigator.ai.ufl.edu/v1`），密钥环境变量 `NAVIGATOR_API_KEY`，写在项目根目录 `.env`。**目前 `.env` 里还没有这个密钥**，需要用户自己加。没有密钥时网页显示 MOCK，只能用 “Saved answer” 模式。
- 视频工具：`reasoning_drive/labeling/video.py`（`VideoReader` 用 OpenCV 读帧，已在 2.7K HEVC 视频上用过）；`opencv-python-headless` 已在 `requirements.txt` 和 Docker 锁文件里。

### 1.4 已经做好的演示片段（参考用）

- `datasets/US/carla_demo/`：从旧讲解视频 `carla.mp4` 裁出的 6 段纯摄像头片段（站点 2–7，**4× 快放** + 末尾 3 秒到站原图），有 `README.md` 和 `make_clips.py`。
- **它们不能用来演示违规**：那次车按 B 开，违规全被拦下；站点 6 之后“跨白实线变道再右转”的画面在讲解视频里被剪掉了。所以需要按第 2 节重新录。

---

## 2. 任务 A：在 CARLA 里录“自车违规”的视频（Windows 上做）

1. **加一个“不把关”模式**：`drive_with: none`（或命令行 `--drive-with none`）。车**无视感知层，照导航意图直接执行**：站点 3 直行、站点 5 越双黄线超车、站点 6 从左转车道直接右转（或先跨白实线再右转）、站点 2 越单黄线。
   - 这个模式下**不需要问模型**（感知判断留到回灌阶段做），所以 CARLA 这一步**不花 API 费用**。
   - 如果 CARLA 自带的规划/Traffic Manager 不肯越实线，用 `BasicAgent` 的路径点或直接给横向偏移控制来强制完成动作。
2. **录原始摄像头视频**：只录车载相机画面，**不要任何字幕、小地图、框**。1280×720，正常速度（建议 20 fps），H.264 mp4。相机位置沿用 `route.py` 里的 `CAM_X / CAM_Z`。
3. **同时写行车日志** `drive_log.jsonl`（每个仿真 tick 或每 0.1 s 一行），至少包括：
   - `t`（视频里的秒数，要和录像帧严格对齐）、`frame`、`x, y, yaw`、`speed`
   - `road_id, lane_id, is_junction`
   - 当前车道左右标线：`left_marking / right_marking`（CARLA `waypoint.left_lane_marking.type/color`，用 `route.py` 里已有的 `project_marking(...)` 转成项目的标线词汇），`lane_change` 许可
   - 以及事件文件 `events.jsonl`：
     - 压线事件（车道入侵传感器 `sensor.other.lane_invasion`，`loop.py` 里已有写法）：时间、压到的标线类型
     - 路口转向（进路口前后的航向变化 > 60° 判为左/右转，< 30° 判为直行）
     - 每个站点：站点号、标线、导航意图、实际执行的动作
4. 跑 `route1`（可以只跑有违规的站点，或者用 `--max-stops`），输出到 `results/carla/<时间戳>_route1_noguard/`：`camera.mp4`、`drive_log.jsonl`、`events.jsonl`、`meta.json`。
5. **导出演示片段**：每个违规动作截一段 **20–30 秒**（动作前约 20 秒到动作完成后几秒），按 **2× 速度** 导出（用户要求 2×）；同时保留正常速度版本。放到 `datasets/US/carla_demo/noguard/`，并更新那里的 `README.md`（片段 ↔ 站点 ↔ 意图 ↔ 违规时刻）。

> 先用 `--preview` 或短距离试跑，确认相机画面、日志时间对齐，再跑整圈。

---

## 3. 任务 B：回灌诊断（核心功能）

### 3.1 流程

```
输入：视频（必须）+ 行车日志 events/drive_log（CARLA 有；真实行车视频没有时见 3.4）
 1. 找出自车动作：变道（压线事件）、路口左转/右转/直行、越中心线
 2. 对每个动作取“证据帧”：动作开始前约 1 秒、标线清楚的那一帧（可取 2–3 帧择优）
 3. 感知层判断：证据帧 → 现有流程（lane_v4c + 选定地区法规 + 校验层 guard.verify）
    → 左右车道线、7 个动作允许/禁止、引用条文、推理
 4. 对比：实际动作 vs 感知层结论 → 合规 / 违规
 5. 自动归因（用 CARLA 地图真值，日志里的 left/right_marking → 规则表 lane_prefill 算出标准答案）
```

| 地图真值 | 感知层判断 | 车的动作 | 结论 |
|---|---|---|---|
| 禁止 | 禁止 | 做了 | **决策层的错**：感知给了正确信息，决策没采纳 |
| 禁止 | 允许 | 做了 | **感知层的错**：看错线/判错规则，误导了决策 |
| 允许 | 禁止 | 没做 / 做了 | 感知层过度保守（false alarm） |
| 允许 | 允许 | 做了 | 合规 |

- 法规可选：美国 MUTCD（Test B）、中国 GB 5768（相当于 Test C：美国道路用中国规则）、不给法规（Test A）。站点 6、7 中美结论不同，适合演示。
- 只有事件帧才调用模型：一段视频约 5–10 次调用，便宜、几十秒出结果。

### 3.2 实现建议

- 新模块：`reasoning_drive/replay/`（`events.py` 读日志/检测动作、`evidence.py` 取证据帧、`diagnose.py` 跑感知层 + 对比 + 归因、`report.py` 出报告）。复用 `labeling/video.py`、`web/guard.py`、`labeling/lanes.py`、现有的模型调用和 **缓存**（按图片哈希缓存，**同一个视频再上传要秒出**，演示时不用联网）。
- 命令行：`python main.py replay <video.mp4> --log <events.jsonl|drive_log.jsonl> --rules US|CN|none --api nav_gemma4_31b_bf16 [--mock]`
  输出到 `results/replay/<时间戳>/`：`report.json`、`report.md`、`evidence/*.jpg`（证据帧，标出时间）。
- 网页：在 Analyze 旁边加一个 **“Replay（回灌诊断）”** 页签：
  - 输入：上传视频 + 日志（可选）；法规下拉（US MUTCD / CN GB 5768 / none）。
  - 输出：视频时间线，事件处打标记（绿=合规，红=违规，黄=需人工复核）；点事件显示证据帧、自车动作、感知层结论（两条线、7 个动作、条文、推理）、地图真值、归因结论。
  - 每个事件可以提交反馈（复用 `/api/feedback`，加 `source=replay` 和事件 id）。
  - 后台任务 + 进度条（视频处理不要阻塞请求）；限制大小（≤ 300 MB、≤ 2 分钟）；原视频处理完即删，只保留证据帧。
- 监控：新增指标 `replay_events_total{verdict,attribution}`、`replay_job_seconds`；Grafana 加一块“回灌事件与归因”面板；可加告警“决策层违规 > 0”。改 Grafana 时改 `make_grafana.py` 再生成，不要手改 json。
- 文档：更新 `START_HERE.md`、`docs/GUIDE_zh.md`（回灌怎么用）、`docs/lane_advisor.md`（英文）。

### 3.3 次要功能（有时间再做）：普通视频模式

没有日志的普通视频：每秒抽 1 帧（去掉停车、重复、模糊帧，最多 20 帧）→ 每帧跑感知层 → 按左右车道线把连续帧合并成段 → 输出“每段允许做什么”的时间线；可选“导航意图”（不发给模型），在最后一段对比意图给出警告。相邻帧车道线来回跳变（闪烁）标为需人工复核。

### 3.4 真实行车视频（没有日志）

只做说明或简单原型：变道可以从视频里检测（最近的车道线横向扫过画面中线），转向可以用光流/航向变化估计。CARLA 演示用日志即可。

---

## 4. 讲法（答辩 / PPT）

- 架构：**感知层**（本项目：读车道线 + 按当地法规解释成 7 个动作的许可，带条文依据）→ **决策层**（规划时把“禁止”当约束；CARLA 闭环里已有简单规则版：意图 vs 许可 → 执行 / 拒绝 / 换替代方案）→ **控制层**（CARLA 自带）。
- 回灌诊断 = 把录好的数据重新喂给系统，自动找出问题帧并归因到感知或决策。
- 价值：工业界车道许可通常来自高精地图（OpenDRIVE 车道线自带能否变道，CARLA 真值就是这么来的）；本系统适合 **没有高精地图 / 地图过期（重新划线）/ 跨国法规不同** 的情况，也能反过来校验地图。
- 必须主动说明的限制：每帧 10–60 秒，只能离线回灌或当低频“慢系统”，不能实时控车；准确率约 0.6、有不安全错误，决策层不能盲信（看 needs_review，拿不准就保守）；仿真画面与真实照片有差距，CARLA 结果是受控场景测试，不替代 BDD100K / CULane 主结果；CARLA 城镇是美式标线，中国特有标线（待转区等）测不到。
- 决策层本身放在 future work，不要真去做完整规划器。
- PPT 已有 18 页（English 正文 + 中文讲稿），在用户的 claude.ai 账户里；新内容可以给出要加的页面文字和截图，由用户放进去。

---

## 5. 规矩（必须遵守）

1. **API 密钥只放在 `.env`，由用户自己写**。不要替用户输入或写入密钥，不要在任何输出、日志、截图说明里显示 `.env` 的内容或密钥值。
2. **花钱的模型调用先问用户**（说清楚大约多少次调用）。能用 `--mock` 和缓存先跑通就先跑通。CARLA 录制本身不调用模型。
3. **不要 git commit / push**，除非用户明确同意。
4. **不删除文件**：需要清理的移到 `_archive/`（里面有 README 说明）。
5. 不改冻结的协议：`prompts/lane_v4c`、`configs/lane_protocol__*`、标签文件。新功能都是在外面加。
6. UF 政策：**UF 的资源上不用来自受关注国家的大模型**；本项目主模型是 Gemma（Google）。
7. 硬盘是 exFAT：macOS 会生成 `._*` 文件，Windows 上不要误当成数据文件处理；写文件后确认能读回。
8. 数据许可：BDD100K / CULane 仅限研究和教学用途；用户自己的行车视频不公开，发布的图要打码车牌和人脸。GPT 在 UK/IN 数据上的调用需用户先确认数据条款。
9. 每完成一步，用中文简短告诉用户做了什么、文件在哪、怎么验证。

---

## 6. 建议顺序与验收

1. 读 `START_HERE.md`、本文件；在 Windows 上确认 `.venv` 自检能过、CARLA 0.9.16 能启动、`python main.py carla routes` 能列出 route1。
2. 加 `drive_with: none` + 原始相机录像 + `drive_log.jsonl` / `events.jsonl`；先短距离试跑，检查视频帧和日志时间对齐。
   - 验收：视频里能清楚看到站点 3/5/6 的违规动作；`events.jsonl` 里有对应事件和时间。
3. 导出 2× 演示片段到 `datasets/US/carla_demo/noguard/` 并写 README。
4. 做 `main.py replay`（先 `--mock` 跑通，再问用户后用 NaviGator 跑一次，结果进缓存）。
   - 验收：每个违规动作都被找到；报告里有证据帧、感知结论、真值、归因；同一视频第二次运行秒出、不调用模型。
5. 网页 “Replay” 页签 + 反馈 + 指标 + Grafana 面板；Docker 里也能用。
   - 验收：浏览器上传片段 → 时间线 + 红色违规事件 + 归因；Grafana 能看到回灌事件计数。
6. 更新文档；给出 PPT 要加的 1–2 页（回灌诊断流程图 + 一个违规例子截图）。
