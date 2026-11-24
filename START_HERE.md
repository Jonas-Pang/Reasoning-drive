# 从这里开始

**Reasoning Driving**：给视觉大模型一张行车照片和当地交规，让它判断“我这条车道能做什么”；部署成一个有验证、监控和用户反馈的网页服务。

> 第一次读：先看这一页。细节看 `docs/GUIDE_zh.md`（中文导览）和 `docs/lane_advisor.md`（部署说明，英文）。

---

## 1. 你最常做的三件事

| 想做什么 | 命令（在 VS Code 终端里，项目目录下） | 或者用任务（终端 → 运行任务…） |
|---|---|---|
| 本机打开网页演示 | `bash scripts/rd.sh web --api nav_gemma4_31b_bf16 --lane-prompt lane_v4c --real`，然后打开 http://localhost:8770/app | 任务 2 |
| 用 Docker 部署全套（应用 + 监控）并演示 | `bash scripts/deploy_demo.sh`：一条命令启动三个容器、发演示流量和反馈、打开网页（只启动不发流量：`bash scripts/docker_build.sh && docker compose up -d --no-build`） | 任务 D0（只启动：D1） |
| 看反馈分析 | `bash scripts/rd.sh --script scripts/feedback_report.py` → `results/app/feedback_report.md` | 任务 5 |

第一次使用前只做一次：`bash scripts/setup_mac.sh`（建 Python 3.11 环境，任务 0）。

---

## 2. 文件夹地图

★ = 你会打开或修改的；○ = 程序自己用，一般不用管。

```
Reasoning_Drive/
├─ START_HERE.md            ★ 本页
├─ README.md                ○ 英文总说明（很长，给复现者看）
├─ main.py                  ★ 唯一入口：python main.py <命令>（--help 看全部）
├─ .env                     ★ 密钥和本机设置（NAVIGATOR_API_KEY、GRAFANA_ADMIN_PASSWORD），不进镜像、不进仓库
├─ Reasoning_Drive.code-workspace  ★ 用 VS Code 打开这个文件（里面有全部任务）
│
├─ Dockerfile               ★ 部署：怎么构建镜像
├─ docker-compose.yml       ★ 部署：应用 + Prometheus + Grafana 三个容器
├─ deploy/                  ○ 部署配置：依赖锁文件、Prometheus 配置、Grafana 面板和告警规则
│
├─ reasoning_drive/         ○ 全部代码
│  ├─ agent/                   调模型（组 prompt、发请求、解析答案）
│  ├─ evaluation/              打分、统计检验、冻结协议
│  ├─ web/                     网页和部署：server.py、guard.py（验证层）、feedback.py（反馈）、metrics.py（监控指标）
│  ├─ labeling/ regulations/ simulation/ tests/   标注工具、法规处理、CARLA 仿真、自检
├─ configs/                 ○ 设置：用哪个模型、哪些数据、答案格式、冻结协议
├─ prompts/lane_v4c/        ○ 最终的 prompt（其他 lane_v* 和 v1–v4 是历史版本，旧运行要用到，不要删）
├─ regulations/<国家>/      ○ 各国条文和规则表
├─ datasets/<国家>/         ○ 标签（图片本身在 T9 的 数据集/ 文件夹）
├─ results/                 ★ 结果：runs/（每次运行）、app/（部署后的审计日志和反馈）
├─ docs/                    ★ 文档：GUIDE_zh.md（中文导览）、lane_advisor.md（部署）、deployment.md（Docker 细节）
├─ scripts/                 ○ 小工具：setup_mac.sh、rd.sh、feedback_report.py、replay_feedback.py、标注和评测脚本
├─ hpg/                     ○ 在 HiPerGator 上跑本地模型
├─ notebooks/               ○ 早期里程碑用的 Jupyter 笔记本
└─ _archive/                ○ 修改前的备份和一次性脚本（运行不需要；在 VS Code 里已隐藏）
```

T9/Project 里项目外面的东西：
- `claude_analysis/`：分析脚本、HiPerGator 的日志和对比结果、部署源文件和截图。
- `hpg_sync_20261118/` 和 `*.zip`：从 HiPerGator 拷回来的原始备份。
- Mac 上的 `~/Projects/Reasning_Drive` 是 11/5 的旧版本，**不要用**。

---

## 3. 老师的要求在项目里对应哪里（Module 8 部署 + Module 9 监控与反馈）

| 老师的要求 | 在哪里 | 怎么演示 |
|---|---|---|
| **代码规范**：清楚的命名、模块化 | `reasoning_drive/` 按功能分包 | 讲 PPT 第 4 页的六层结构 |
| **版本管理和可复现**：随机种子、环境文件 | 种子 6216、temperature 0；`requirements.txt`、`deploy/requirements-docker.lock`（版本和哈希锁死）；`configs/lane_protocol__*.json`（冻结模型版本和 prompt 哈希） | 打开一个冻结协议文件给老师看 |
| **日志、模型版本记录** | `results/runs/<run_id>/manifest.json`（每次运行的设置）、`results/app/predictions.jsonl`（部署后每个回答） | 打开一个 manifest |
| **交互界面**（老师用 Gradio） | 网页 `/app`：分析、反馈、监控三个标签页（老师说 Streamlit、Flask 也可以；我们用的是自己写的 Python 网页服务） | 打开 http://localhost:8770/app |
| **输入校验、合规** | 照片格式和大小检查、去掉元数据、按数据集许可决定能不能发给模型、只用 UF 允许的模型（`reasoning_drive/web/server.py`、`configs/experiment.yaml`） | 上传一张不是图片的文件，会被拒绝 |
| **Docker 容器化 + 安全** | `Dockerfile`：小基础镜像、依赖哈希锁、非 root 用户、健康检查；密钥用环境变量；端口只绑本机 | `bash scripts/deploy_demo.sh` |
| **可扩展性** | `docker-compose.yml` 里给应用设了 CPU 和内存上限；扩到多副本的做法见下面 4.4 | 讲 |
| **Prometheus + Grafana 监控** | `reasoning_drive/web/metrics.py`（`app_*` 指标）、`deploy/grafana/dashboards/app.json`（面板 “Lane advisor – monitoring”） | 打开 http://localhost:3000 |
| **告警**（老师的例子是置信度低于 0.9） | `deploy/grafana/provisioning/alerting/rules.yml`：规则一致率低于 0.85、差评超过 30%、延迟 p90 超过 60 秒、模型出错 | Grafana → Alerting → Alert rules |
| **收集用户反馈**（好/坏 + 文字） | `/app` 的反馈页 → `results/app/feedback.csv` + Prometheus 计数 `app_feedback_*` | 见第 5 节 |
| **在 Grafana 里显示反馈表**（老师用 Join by labels） | 面板里的 “Feedback comments” 表 | 提交一条反馈后刷新面板 |
| **分析反馈**（定性 + 定量） | `scripts/feedback_report.py`：各动作错误率（频率分析）、评论主题归类（主题分析）；装了 scikit-learn 还会做 TF-IDF + k-means 聚类 | 运行任务 5，打开报告 |
| **训练指标 vs 监控指标** | 评估用标签算准确率和不安全错误；上线后没有真值，用规则一致率、复核率、差评率、延迟、照片亮度漂移 | PPT 第 16 页 |
| **CI/CD**（讨论） | 设想：每次提交跑自检、schema 和规则表检查，构建镜像并扫描漏洞；发布前在冻结开发集上做回归测试 | PPT 第 17 页 |

---

## 4. Docker 怎么用

### 4.1 准备（只做一次）
1. 安装 **Docker Desktop for Mac（Apple 芯片版）**，打开它，等到状态显示 running。
2. Docker Desktop → Settings → Resources → File sharing：确认 `/Volumes/T9` 在列表里。
3. `.env` 里有这两行：
   ```
   GRAFANA_ADMIN_PASSWORD=自己定一个
   NAVIGATOR_API_KEY=你的 NaviGator 密钥
   ```
   没有密钥也能启动，只是网页只能用 “Saved answer（离线）”。

### 4.2 启动和访问
```bash
bash scripts/docker_build.sh           # 构建镜像（第一次几分钟）
docker compose up -d --no-build        # 启动三个容器（-d 放到后台）
```
项目在 T9（exFAT 格式）上，macOS 会在每个文件旁边生成隐藏的 `._文件名`，`docker compose up --build` 会因此报错 “failed to xattr … operation not permitted”。`docker_build.sh` 先把构建需要的文件复制到 Mac 本机（`~/.cache/reasoning_drive_build`，不带 `._` 文件），再在那里构建，镜像内容完全一样。代码改动后，重新运行这两条命令即可。
| 地址 | 是什么 |
|---|---|
| http://localhost:8770/app | 用户页面：分析、反馈、监控 |
| http://localhost:8770 | 研究控制台：prompt、批量运行、对比 |
| http://localhost:3000 | Grafana（用户 admin，密码是 `.env` 里设的那个）。首页就是监控面板 |
| http://localhost:9090 | Prometheus（Status → Targets 里 demo 应该是 UP） |

### 4.2b 一键演示（老师那一套完整流程）
```bash
bash scripts/deploy_demo.sh
```
脚本会依次做这些事：
1. 检查 Docker 和 `.env`；
2. 构建并启动三个容器；
3. 等应用起来；
4. 用 `scripts/demo_traffic.py` 通过 HTTP 请求服务 80 次（中美各 40 张测试图），用离线回放的答案，不花钱；
5. 每个答案按标签提交一条评审反馈，来源标为 `simulated_reviewer`，和真实用户的反馈分开统计；
6. 打开应用、Grafana 和 Prometheus。

大约 6 分钟后，Grafana 的告警 “More than 30 % of feedback is bad” 会变成 **Firing**，对应老师截图里的告警示例。服务已经在运行时，只想再发一批流量，就运行任务 D1b。

### 4.3 常用命令
| 命令 | 作用 |
|---|---|
| `docker compose ps` | 看三个容器是否在运行、是否健康 |
| `docker compose logs -f demo` | 看应用日志 |
| `docker compose run --rm demo python main.py selftest` | 在镜像里自检 |
| `docker compose down` | 停止（Prometheus 和 Grafana 的数据保留） |
| `docker compose down -v` | 停止，并清空监控数据 |

### 4.4 扩展到多副本（讲解用）
老师的例子是在 compose 里写 `deploy: replicas: 3`。我们的应用把审计日志和反馈写在文件里，多个副本同时写同一个文件会冲突。要水平扩展需要三步：
1. 把日志和反馈改存到共享数据库（例如 PostgreSQL）。
2. 前面加一个负载均衡（例如 nginx）。
3. 让 Prometheus 分别抓取每个副本的指标。

当前的单副本版本用 CPU 和内存上限，加上健康检查和自动重启（`restart: unless-stopped`），保证稳定运行。

---

## 5. 怎么提交和分析反馈

1. 打开 http://localhost:8770/app ，在 **Analyze** 里选一张照片，点 **Analyze lane**。
2. 点 **Give feedback →**，或切到 **Feedback** 标签页。
3. 填写：
   - 整体 👍 Good 还是 👎 Bad；
   - 左线、右线各自 Right / Wrong / Unsure；
   - 7 个动作各自 Right / Wrong / Unsure；
   - 一段评论，例如 “right line is solid near the junction”。
4. 点 **Submit feedback**。反馈写进 `results/app/feedback.csv`，Prometheus 计数加一，评论会自动归类主题（比如“实线和虚线”“公交车道”）。
5. 去哪里看：
   - **Monitor** 标签页：总数、各动作被说错的比例、评论主题；
   - Grafana 面板：反馈表、差评率；超过 30% 会触发告警；
   - 分析报告：`bash scripts/rd.sh --script scripts/feedback_report.py`，结果在 `results/app/feedback_report.md`。
6. 演示前想有足够多的数据，可以用测试集模拟评审员反馈：`bash scripts/rd.sh --script scripts/replay_feedback.py --test B --clear`（任务 4）。这些行的来源标为 `simulated_reviewer`，和真实用户反馈分开统计。

---

## 6. 本机运行（不用 Docker）

```bash
bash scripts/setup_mac.sh                     # 只第一次：建 Python 3.11 环境（~/.venvs/reasoning_drive）并自检
bash scripts/rd.sh web --api nav_gemma4_31b_bf16 --lane-prompt lane_v4c --real   # 网页
bash scripts/rd.sh selftest                   # 自检
bash scripts/rd.sh --help                     # 全部命令
```
`scripts/rd.sh` 只是用这个环境去运行 `python main.py …`，每次会先把完整命令打印出来。

## 7. 选模型、上传视频（2026-11-18 新增）

**选模型（Analyze 和 Video 页都有）：**

| 选项 | 说明 | 需要 |
|---|---|---|
| Saved answer | 冻结测试集上 gemma4:31b + lane_v4c 的答案，不调用模型，离线可用 | 只能用测试集示例，Test A/B |
| UF NaviGator · gemma-4-31b-it | 学校的 API（profile `nav_gemma4_31b_bf16`，可用环境变量 `RD_NAVIGATOR_PROFILE` 换） | `.env` 里 `NAVIGATOR_API_KEY` |
| OpenAI · gpt-6.1-sol | `configs/api.yaml` 的设置 | `.env` 里 `OPENAI_API_KEY`（要花钱） |
| Mock | 假答案，只检查流程 | 无 |

**用户自己的 API 密钥（“Your API key” 页）：** 选提供方（OpenAI / UF NaviGator / 其他 OpenAI 兼容服务），填 Base URL 和模型名，粘贴密钥 → “Check key (free)” 只请求免费的 `/models` 列表，不花 token → “Use this key”。之后 Analyze 和 Video 页的模型列表里出现 “Your key · 模型名” 并自动选中。密钥只存在服务内存里、按浏览器标签页区分，不写文件、日志、指标或结果，页面只显示最后 4 位；点 “Forget my key” 或服务停止就没了。测试集照片只能用冻结过协议的模型，用自己的密钥时请上传照片或视频。

**选法规：** 本地区法规（Test B）、不给法规（Test A）、别的地区法规（Test C，例如美国道路配中国 GB 5768）。

**上传视频（Video 页）：** MP4/MOV/AVI，≤ 500 MB、≤ 5 分钟。
1. 每秒取 1 帧（可调），去掉几乎一样的帧，最后一帧一定保留，最多 20 帧（可调到 40）。视频、帧和标注视频留在本机临时文件夹里，服务停止或在页面上点“delete”时删除；同一个视频可以换法规或模型再分析，不用重新上传。
2. 每帧走和照片一样的流程：lane_v4c + 选定法规 + 选定模型 → 验证层 → 预测日志 + 监控指标。
3. 两条线和箭头相同的连续帧合并成一段；每个动作取多数，平票取更严格的值；线型 A-B-A 来回跳 → 标“需人工复核”。
4. **导航意图（可选，不告诉模型）：** 和最后一段比较 → 允许 / 违规。
5. **事件文件（可选，CARLA 日志）：** 每个实际动作取它前 1 秒的“证据帧”判断；如果事件里给了真值（allowed/prohibited），自动归因：决策层的错 / 感知层的错 / 感知过度保守 / 合规。

事件文件格式（JSON 列表、`{"events": [...]}` 或每行一个 JSON）：
```json
[{"t": 19.0, "action": "turn_right", "truth": "prohibited", "note": "左转专用道右转"},
 {"t": 12.0, "action": "change_right", "truth": "allowed"}]
```
`action` 用 7 个动作名（change_left、change_right、go_straight、turn_left、turn_right、u_turn、enter_waiting_area），也认 lane_change_left、straight、right_turn 等写法。

**标注视频（分析完自动生成）：** 原视频逐帧画上系统的判断——顶部是当时读到的两条线和 7 个动作（绿 yes / 红 NO），底部是整段时间线和播放位置；出问题的时段（导航意图被禁止、实际动作违规）加红框和红色横幅 “PROBLEM k: …”，证据帧处标 “EVIDENCE FRAME”。另外每个问题单独切一段 problem_k.mp4（意图：最后 5 秒；事件：前后各 3 秒）。页面上可以直接播放、点时间线跳转、下载。Docker 镜像里装了 ffmpeg（H.264，所有浏览器能播）；本机不用 Docker 运行时请先 `brew install ffmpeg`，否则只能下载后播放。

**缓存：** 同一个视频再上传，每帧都从缓存读，几秒出结果、不调用模型（演示前先跑一次）。

**监控：** Grafana 新增 4 块（已分析视频数、视频分析 p90、动作检查结果、谁的错），告警新增“回灌发现决策层违规”。指标名 `app_video_*`。

**改代码后重新部署：** `bash scripts/docker_build.sh && docker compose up -d --no-build`（Windows：`docker compose up -d --build`）。
