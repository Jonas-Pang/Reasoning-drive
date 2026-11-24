# CARLA 自车违规短视频（10 段，2 倍速）

用途：交给回灌诊断（replay）系统评估：找出自车动作的时刻 → 取帧 → 感知层（车道线 + 当地法规）判断 → 判定违规并归因。

- 画面：只有车载前视摄像头（无字幕、框、小地图），1280×720，30 fps，**2 倍速**，每段约 13–23 秒。
- 来源：CARLA 0.9.16，Town03，晴天中午；不把关模式（`drive_with: none`）：车不问感知层，照导航意图直接做。录制时没有调用任何模型（无 API 费用）。
- 录制日期：2026-11-18（在 Windows 电脑上用 `python main.py carla noguard violations` 及 violations2–5 录制，代码 `reasoning_drive/simulation/noguard.py`，配置 `configs/carla.yaml`；这些代码目前在 D:\Project\Reasoning_Drive，尚未合并到 F 盘这份项目）。
- 位置：`F:\Project\Reasoning_Drive\carla_violation_clips\`（项目根目录下，方便调用）。
- 文件名格式：`序号_动作_标线或车道[_街道]`；场景、时间和规则结论见下表和 `clips.json`。

| # | 文件 | 场景 | 时长 | 违规动作在片段里的时间（开始–结束） | 规则 US / CN | 结论（地图真值） |
|---|---|---|---|---|---|---|
| 01 | `01_overtake_double_solid_yellow_street1.mp4` | 越双黄实线超车（街道 1） | 19 s | 7.0–11.4 s | prohibited / prohibited | 中美都违规 |
| 02 | `02_overtake_double_solid_yellow_street2.mp4` | 越双黄实线超车（街道 2） | 16 s | 8.1–13.2 s | prohibited / prohibited | 中美都违规 |
| 03 | `03_overtake_double_solid_yellow_street3.mp4` | 越双黄实线超车（街道 3） | 20 s | 3.0–8.8 s | prohibited / prohibited | 中美都违规 |
| 04 | `04_left_turn_from_right_turn_only_lane.mp4` | 右转专用道上直接左转 | 20 s | 11.3–16.4 s | prohibited / prohibited | 中美都违规 |
| 05 | `05_overtake_solid_broken_yellow_solid_on_my_side_street1.mp4` | 越黄色虚实线超车，实线在本车一侧（街道 1） | 21 s | 14.0–18.4 s | prohibited / prohibited | 中美都违规 |
| 06 | `06_right_turn_from_left_turn_only_lane.mp4` | 左转专用道上直接右转 | 23 s | 14.0–20.3 s | prohibited / prohibited | 中美都违规 |
| 07 | `07_overtake_single_solid_yellow.mp4` | 越单黄实线超车 | 20 s | 5.9–10.3 s | prohibited / prohibited | 中美都违规 |
| 08 | `08_lane_change_across_solid_white_before_junction_CN_only.mp4` | 路口前跨白实线变道（仅中国规则违规） | 14 s | 8.0–11.5 s | allowed / prohibited | 仅中国规则违规（美国允许） |
| 09 | `09_wrong_way_driving_across_double_solid_yellow.mp4` | 越双黄实线逆行约 70 米 | 20 s | 5.9–16.2 s | prohibited / prohibited | 中美都违规 |
| 10 | `10_overtake_solid_broken_yellow_solid_on_my_side_street2.mp4` | 越黄色虚实线超车，实线在本车一侧（街道 2） | 13 s | 5.8–10.0 s | prohibited / prohibited | 中美都违规 |

备注
- “违规动作时间”是 2 倍速片段里的秒数。
- 规则结论来自项目规则表（lane_prefill：美国 MUTCD / 中国 GB 5768），标线来自 CARLA 地图真值。
- 超车的几段前方都放了一辆停着、开双闪的货车，作为超车的理由。
- 05、10：CARLA 地图的变道标志说虚线在本车一侧，但实际画的是实线在本车一侧（按画面判定，和 route1 的处理一致），所以记为禁止。
- 08：跨白实线变道，**美国规则允许、中国规则禁止**，适合演示 Test C（美国道路用中国规则）。右侧那条线地图写的是黄实线，实际画的是白实线（`truth_override`）。
- 04、06：Town03 里能“从转向专用道做相反动作”的路口只有这两个（和 route1 演示的是同两个路口）。
- 02、08、10 较短：前后离别的动作或视频开头太近，为了不把别的违规剪进来没有再加长。
- 每段的完整数据在 `clips.json`：源视频时间段（正常速度秒数）、road/lane、实际动作、规则结论、旧文件名。原始整段视频、逐帧行车日志 `drive_log.jsonl`（t = 正常速度秒数，2 倍速片段时间 = (t − 片段起点) / 2）和事件 `events.jsonl` 在 D:\Project\Reasoning_Drive\results\carla\ 下的 `20261118_*_violations*_noguard` 文件夹里。
