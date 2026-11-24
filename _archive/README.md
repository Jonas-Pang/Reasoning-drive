# _archive：不再使用、但留作记录的文件

2026-11-18 整理项目时从各处挪到这里，保留了原来的相对路径（例如 `datasets/US/bdd100k/xxx.before_round3` 原来就在 `datasets/US/bdd100k/` 下）。项目运行不需要这里的任何文件；挪走它们没有改变任何功能。需要找回某个旧版本时，把它复制回原位置即可。

## 1. 修改前的备份（58 个）

文件名后缀说明是在哪一步修改之前备份的：

- `.before_claude_review` / `.before_round2` / `.before_round3` / `.before_round4b..d`：标签复核各轮之前
- `.before_conv4`：按 11/17 标注口径批量转换之前
- `.before_expand`：英国、印度扩充图片之前
- `.before_v4` / `.before_v5`、`lane.py.v5`：prompt v4、v5 改代码之前；v5 那一版（已放弃）
- `.before_hpgsync`：11/18 从 HiPerGator 同步回 T9 之前
- `.before_app`：11/18 加部署页面 /app 之前
- `.broken_by_seed`：标注工具出错时被重置的文件（已恢复）
- `.before_py311`：Mac 安装脚本改成 Python 3.11 之前

每一处标签修改的内容和原因记在各数据集目录里的 `label_corrections.csv`（那些文件没有挪）。

- `docker-compose.yml.before_app`
- `.env.example.before_app`
- `configs/api_profiles.yaml.before_hpgsync`
- `configs/schemas/lane_schema.json.before_v4`
- `datasets/CN/mapdr/mapdr.lanes.csv.before_claude_review`
- `datasets/CN/mapdr/label_corrections.csv.before_hpgsync`
- `datasets/CN/mapdr/mapdr.lanes.csv.before_hpgsync`
- `datasets/CN/mapdr/mapdr.lanes.csv.before_conv4`
- `datasets/CN/mapdr/mapdr.lanes.csv.before_round3`
- `datasets/CN/mapdr/mapdr.lanes.csv.before_round4b`
- `datasets/CN/mapdr/mapdr.lanes.csv.before_round4c`
- `datasets/CN/mapdr/mapdr.lanes.csv.before_round4d`
- `datasets/IN/idd/idd.lanes.csv.before_claude_review`
- `datasets/IN/idd/idd.lanes.csv.before_expand`
- `datasets/IN/idd/idd.lanes.csv.broken_by_seed`
- `datasets/IN/idd/idd.lanes.csv.before_conv4`
- `datasets/IN/idd/idd.lanes.csv.before_hpgsync`
- `datasets/IN/idd/label_corrections.csv.before_hpgsync`
- `datasets/UK/lingoqa/lingoqa.lanes.csv.before_claude_review`
- `datasets/UK/lingoqa/lingoqa.lanes.csv.before_expand`
- `datasets/UK/lingoqa/lingoqa.lanes.csv.broken_by_seed`
- `datasets/UK/lingoqa/label_corrections.csv.before_hpgsync`
- `datasets/UK/lingoqa/lingoqa.lanes.csv.before_hpgsync`
- `datasets/UK/lingoqa/lingoqa.lanes.csv.before_conv4`
- `datasets/US/bdd100k/bdd100k_val.lanes.csv.before_claude_review`
- `datasets/US/bdd100k/bdd100k_val.lanes.csv.before_hpgsync`
- `datasets/US/bdd100k/label_corrections.csv.before_hpgsync`
- `datasets/US/bdd100k/bdd100k_val.lanes.csv.before_conv4`
- `datasets/US/bdd100k/bdd100k_val.lanes.csv.before_round2`
- `datasets/US/bdd100k/bdd100k_val.lanes.csv.before_round4b`
- `datasets/US/bdd100k/bdd100k_val.lanes.csv.before_round4d`
- `datasets/US/bdd100k/bdd100k_val.lanes.csv.before_round3`
- `prompts/lane_v4/fields.txt.before_v4`
- `prompts/lane_v4/role.txt.before_v4`
- `reasoning_drive/cli.py.before_app`
- `reasoning_drive/agent/lane.py.before_v4`
- `reasoning_drive/agent/client.py.before_v4`
- `reasoning_drive/agent/lane.py.v5`
- `reasoning_drive/agent/lane.py.before_v5`
- `reasoning_drive/labeling/lanes.py.before_hpgsync`
- `reasoning_drive/labeling/lanes.py.before_conv4`
- `reasoning_drive/web/metrics.py.before_app`
- `reasoning_drive/web/server.py.before_app`
- `regulations/CN/lane_action_rules.json.before_hpgsync`
- `regulations/CN/lane_action_rules.json.before_conv4`
- `regulations/IN/lane_action_rules.json.before_hpgsync`
- `regulations/IN/lane_action_rules.json.before_conv4`
- `regulations/UK/passages_lane.yaml.before_v4`
- `regulations/UK/lane_action_rules.json.before_v4`
- `regulations/UK/lane_action_rules.json.before_hpgsync`
- `regulations/UK/lane_action_rules.json.before_conv4`
- `regulations/US/lane_action_rules.json.before_hpgsync`
- `regulations/US/lane_action_rules.json.before_conv4`
- `results/lane_report_dev.csv.before_hpgsync`
- `results/lane_report_dev.md.before_hpgsync`
- `results/lane_report_test.csv.before_hpgsync`
- `results/lane_report_test.md.before_hpgsync`
- `scripts/setup_mac.sh.before_py311`

## 2. 一次性的辅助脚本（28 个）

数据迁移、标签补填、英印试点、Windows 上本地模型试跑等一次性的脚本，只彼此引用、项目代码不调用。它们是从 `scripts/` 挪过来的，如果要再跑，需要先把它放回 `scripts/`。

- `scripts/claude_check_newcountry.bat`
- `scripts/claude_fill_special.bat`
- `scripts/claude_fill_special.py`
- `scripts/claude_finalize.bat`
- `scripts/claude_finalize.py`
- `scripts/claude_fix_bike_role.bat`
- `scripts/claude_fix_bike_role.py`
- `scripts/claude_label_cn.bat`
- `scripts/claude_label_us.bat`
- `scripts/claude_lane_dev.bat`
- `scripts/claude_lane_dev.py`
- `scripts/claude_lane_eval_fill.bat`
- `scripts/claude_lane_eval_test.bat`
- `scripts/claude_lane_eval_test_resume.bat`
- `scripts/claude_local_check.bat`
- `scripts/claude_local_dev.bat`
- `scripts/claude_migrate_straight.bat`
- `scripts/claude_migrate_straight.py`
- `scripts/claude_move_check.bat`
- `scripts/claude_move_check.py`
- `scripts/claude_move_to_f.bat`
- `scripts/claude_pilot_drafts.json`
- `scripts/claude_pilot_ukin.bat`
- `scripts/claude_pilot_ukin.py`
- `scripts/claude_pilot_ukin_redo.bat`
- `scripts/claude_ports.bat`
- `scripts/claude_single_annotator.bat`
- `scripts/claude_single_annotator.py`
