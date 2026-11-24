# Reasoning Driving 项目导览（中文）

2026-11-18 写给项目作者本人：怎么读懂这个项目、在 Mac 上怎么运行、部署是怎么做的。英文的详细说明在 `README.md` 和 `docs/` 里，这份是入门地图。

---

## 1. 一句话

给通用视觉大模型一张行车照片和当地交规条文，让它判断“我这条车道的左右线是什么、7 个动作能不能做”，用固定格式（JSON）回答。系统再用规则表检查答案，把结果显示给用户，并收集反馈、做监控。

```
照片 + 地区 ─► 输入检查 ─► 组装 prompt（条文 + 看图步骤）─► 视觉大模型 ─► 受约束的 JSON
                                                                     │
      用户反馈 ◄─ 网页 /app ◄─ 审计日志 ◄─ 验证层（规则表套到模型自己看到的线上）
         │
         └─► Prometheus 指标 ─► Grafana 面板和告警 ─► 改标签 / 改规则表 / 改 prompt ─► 重跑冻结测试集
```

## 2. 文件夹地图

| 位置 | 是什么 |
|---|---|
| `main.py` | 唯一的入口。`python main.py <命令>`，`python main.py --help` 列出全部命令 |
| `reasoning_drive/agent/` | 调模型：`lane.py`（车道任务：组 prompt、发请求、解析、打分）、`client.py`（OpenAI / Ollama / NaviGator 三种接口） |
| `reasoning_drive/evaluation/` | 打分和统计：`lane_scoring.py`（逐元素打分、不安全错误）、`protocol.py`（冻结协议）、McNemar 检验 |
| `reasoning_drive/labeling/` | 标注工具，`lanes.py` 里有规则表推动作的逻辑（`lane_prefill`） |
| `reasoning_drive/regulations/` | 法规：从 PDF/HTML 抽条文、存条文 |
| `reasoning_drive/web/` | 网页和部署：`server.py`（所有页面和接口）、`metrics.py`（Prometheus 指标）、**`guard.py`（验证层）**、**`feedback.py`（审计日志和反馈）**、`static/`（前端） |
| `reasoning_drive/simulation/` | CARLA 仿真 |
| `configs/` | 设置：`experiment.yaml`（数据、哪些数据集能发给模型）、`api.yaml`（GPT）、`api_profiles.yaml`（本地 Gemma、NaviGator 等模型配置）、`schemas/lane_schema.json`（答案格式）、`lane_protocol__*.json`（冻结协议） |
| `prompts/lane_v4c/` | 最终 prompt（v3、v4、v5 等是历史版本） |
| `regulations/<国家>/` | `passages_lane.yaml`（给模型的条文）、`lane_action_rules.json`（规则表） |
| `datasets/<国家>/` | 标签 `*.lanes.csv` 和每处修改的记录 `label_corrections.csv`。图片不在这里，在 T9 的 `数据集/` |
| `results/runs/<run_id>/` | 每次运行：`manifest.json`（设置和协议）、`results.jsonl`（每个答案）、`scores.json`（分数） |
| `results/app/` | 部署后的审计日志 `predictions.jsonl`、反馈 `feedback.csv`、反馈报告 |
| `scripts/` | 小工具：`setup_mac.sh`（建环境）、`rd.sh`（用 Mac 环境运行）、`replay_feedback.py`、`feedback_report.py` |
| `deploy/` | Docker 用的依赖锁文件、Prometheus 和 Grafana 配置、告警规则 |
| `Dockerfile`、`docker-compose.yml`、`.dockerignore` | 部署 |
| `hpg/` | HiPerGator 上跑本地模型的脚本 |
| `docs/` | 英文文档；`lane_advisor.md` 是部署系统的说明 |

## 3. 第一次在 Mac 上运行

你的 Mac 上装的是 **Cursor**（VS Code 的改版，用法一样）。项目根目录有 `Reasoning_Drive.code-workspace`，所有常用命令都写在里面，做成了“任务”。

1. 在 Cursor 里用 **文件 → 从文件打开工作区…** 打开 `/Volumes/T9/Project/Reasoning_Drive/Reasoning_Drive.code-workspace`。只打开文件夹的话，任务菜单里没有这些任务。
2. 打开终端：菜单 **终端 → 新建终端**（或 ⌃\`）。终端已经在项目目录里。
3. 第一次先建 Python 环境（装在 Mac 上的 `~/.venvs/reasoning_drive`，不在 T9 上）：
   ```bash
   bash scripts/setup_mac.sh
   ```
   也可以用菜单 **终端 → 运行任务… → 0 · Setup**。装完会自动跑一遍自检。
4. 设置 `.env`（项目根目录，已经有了）。要加的两行：
   ```
   NAVIGATOR_API_KEY=你的 NaviGator 密钥（不加引号）
   GRAFANA_ADMIN_PASSWORD=自己定一个
   ```
   在 Cursor 左侧文件列表里直接点开 `.env` 编辑即可。密钥只放这里，不要写进别的文件。

## 4. 常用命令

每条命令都可以在终端里直接敲，也可以用 **终端 → 运行任务…** 选对应编号。

| 任务 | 命令 | 做什么 |
|---|---|---|
| 1 | `bash scripts/rd.sh selftest` | 自检，不调模型 |
| 2 | `bash scripts/rd.sh web --api nav_gemma4_31b_bf16 --lane-prompt lane_v4c --real` | 启动网页，打开 http://localhost:8770/app 。“Live model” 调 NaviGator 上的 Gemma 31B，“Saved answer” 离线回放 |
| 3 | `bash scripts/rd.sh web --api nav_gemma4_31b_bf16 --lane-prompt lane_v4c --mock` | 同上，但用假答案，完全不联网 |
| 4 | `bash scripts/rd.sh --script scripts/replay_feedback.py --test B --clear` | 把测试集当成用户回放一遍，生成模拟评审反馈 |
| 5 | `bash scripts/rd.sh --script scripts/feedback_report.py` | 反馈分析报告 → `results/app/feedback_report.md` |
| 6 | `bash scripts/rd.sh results --kind lane` | 所有运行结果一张表 |
| — | `bash scripts/rd.sh lane ask <image_id> --test B --real` | 问一张图，打印推理过程 |
| — | `bash scripts/rd.sh lane run --test AB --split dev --real` | 批量跑开发集（会调模型，可能花钱） |

网页停止：在运行它的终端里按 ⌃C。

## 5. 部署是怎么做的（Docker）

### 5.1 为什么用 Docker

把“Python 3.11 + 固定版本的依赖 + 代码 + 配置 + prompt + 条文”打包成一个镜像，任何装了 Docker 的电脑一条命令就能得到完全一样的环境（老师 Module 8 讲的 containerization）。再用 docker compose 同时启动三个容器：

```
浏览器 ──8770──► demo（应用：python main.py web）──HTTPS──► UF NaviGator（Gemma 4 31B）或 OpenAI
                  │ /metrics（每 15 秒被读一次）
                  ▼
               prometheus（存指标）──9090──► 浏览器
                  │
                  ▼
               grafana（面板 + 告警）──3000──► 浏览器
```

### 5.2 Dockerfile 逐步解释

| 步骤 | 作用 |
|---|---|
| `FROM python:3.11-slim` | 最小的 Debian + Python 基础镜像（安全：越小漏洞越少） |
| `COPY deploy/requirements-docker.lock` + `pip install --require-hashes` | 先装依赖，每个包的版本和文件哈希都锁死，保证可复现；代码改了也不用重装依赖 |
| `COPY main.py reasoning_drive configs prompts regulations` | 只复制运行需要的东西。`.dockerignore` 挡住了 `.env`、图片、数据集、结果、PDF |
| `useradd appuser` + `USER appuser` | 不用 root 运行（安全） |
| `EXPOSE 8770` + `HEALTHCHECK …/healthz` | 端口和健康检查；容器坏了 Docker 会知道 |
| `CMD python main.py web …` | 启动网页 |

### 5.3 docker-compose.yml 的三个服务

- **demo**：上面的镜像。
  - 启动命令是 `main.py web --api ${LANE_API_PROFILE:-nav_gemma4_31b_bf16} --lane-prompt lane_v4c`。
  - 密钥从 `.env` 作为环境变量传进容器，不进镜像。
  - 图片目录（`DATASETS_ROOT`）和标签只读挂载；`results/` 可写，审计日志和反馈会落到你的硬盘上。
  - 限制 2 核 2 GB。
  - 端口只绑 127.0.0.1，只有本机能访问。
- **prometheus**：读 `deploy/prometheus.yml`，每 15 秒抓 `demo:8770/metrics`，数据保存 30 天。
- **grafana**：
  - 自动加载数据源、两个面板和告警规则：`deploy/grafana/dashboards/app.json` 是 “Lane advisor – monitoring”，`deploy/grafana/provisioning/alerting/rules.yml` 是 4 条告警。
  - 必须设管理员密码，不允许匿名访问。

### 5.4 在 Mac 上第一次部署

1. 安装 **Docker Desktop for Mac（Apple 芯片版）**：docker.com → Download Docker Desktop。你的 Mac 上目前还没有装 Docker。
2. Docker Desktop → Settings → Resources → File sharing，确认 `/Volumes/T9` 在列表里（项目和图片都在 T9 上）。
3. `.env` 里有 `GRAFANA_ADMIN_PASSWORD` 和 `NAVIGATOR_API_KEY`。
4. 在 Cursor 终端里：
   ```bash
   docker compose up --build        # 第一次要构建镜像，几分钟；以后只重建改过的部分
   ```
   或者运行任务 **D1**。
5. 打开：
   - http://localhost:8770/app ：用户页面，有分析、反馈、监控三个标签页。
   - http://localhost:8770 ：研究控制台，包括 prompt、批量运行、对比。
   - http://localhost:3000 ：Grafana，用户 `admin`，密码是 `.env` 里设的那个。首页就是监控面板，告警在 Alerting → Alert rules。
   - http://localhost:9090 ：Prometheus。Status → Targets 应该显示 demo 为 UP。
6. 常用：
   - `docker compose ps`：看状态。
   - `docker compose logs -f demo`：看日志。
   - `docker compose down`：停止，数据保留。
   - `docker compose run --rm demo python main.py selftest`：在镜像里自检。

### 5.5 怎么在答辩里讲部署

按老师的要求逐条对上：

| 老师的要求 | 项目里对应的部分 |
|---|---|
| 交互界面（Gradio 示例） | `/app` 三个标签页（老师说 Streamlit、Flask 也可以，我们用的是自己的 Python 网页服务） |
| 输入校验 / 合规 | 文件类型和大小检查、去掉照片元数据、按数据集许可决定能不能发给模型、只用 UF 允许的模型 |
| Docker、安全的 Dockerfile | 小基础镜像、依赖哈希锁、非 root、密钥走环境变量、只绑本机端口、健康检查 |
| Prometheus + Grafana | `app_*` 指标、“Lane advisor – monitoring” 面板 |
| 告警（老师的例子是置信度 < 0.9） | 规则一致率 < 0.85、差评 > 30%、延迟 p90 > 60 秒、模型出错 |
| 收集反馈（好/坏 + 文字） | 反馈页：整体好坏、每条线和每个动作对错、评论；写进 CSV，Prometheus 计数 |
| 分析反馈（定性 + 定量） | `feedback_report.py`：各动作错误率（频率），评论主题归类（主题分析），装了 scikit-learn 还会做聚类 |
| 训练指标 vs 监控指标 | 评估用标签算准确率和不安全错误；上线后没有真值，用规则一致率、复核率、差评率、延迟、亮度漂移 |
| CI/CD（讨论） | 提交时：自检、schema 和规则表检查、构建镜像并扫描漏洞；发布前在冻结开发集上做回归测试 |

## 6. 怎么把它讲成一个 AI 系统

六层，每层都能单独检查（PPT 第 4 页）：

1. **输入检查**：照片格式、大小、去元数据、数据许可开关。
2. **知识层**：各国条文（带编号）、规则表、模糊情况的口径（公交车道、箭头）。
3. **感知 + 推理**：视觉大模型。这是唯一“学来的”部分，可以换成 GPT、本地 Gemma 或 NaviGator。
4. **验证层**：把规则表套到模型自己看到的线上，矛盾就要人工复核。
5. **界面 + 审计日志**：每个回答都记下模型、prompt、请求编号。
6. **监控 + 学习闭环**：指标、告警、反馈 → 改标签、规则表、prompt → 重跑冻结测试集再发布。

知识层和验证层不依赖模型，所以能分清是“看错了线”还是“用错了规则”。实验结论是：错主要错在看线，推理本身基本自洽。

## 7. 常见问题

- **网页打开没有英国、印度的例子**：`configs/experiment.yaml` 的 `send_to_api` 里还没开 lingoqa、idd，这是在等你确认这两个数据集的使用条款。
- **“Live model” 报错没有密钥**：`.env` 里加 `NAVIGATOR_API_KEY`，然后重启网页或容器。
- **8770 端口被占用**：之前开的网页还在跑。按 ⌃C 停掉它，或者执行 `docker compose down`。
- **T9 上出现很多 `._` 开头的文件**：这是 macOS 在 exFAT 硬盘上自动生成的，镜像和 Grafana 都已经设成忽略它们。
- **想改用 GPT**：`.env` 里设 `LANE_API_PROFILE` 为 OpenAI 的配置，并填 `OPENAI_API_KEY`。注意每次调用要花钱。
