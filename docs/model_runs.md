# Model runs: `lane_reasoner`

Reference for the model-run package. The project overview, results and reproduction steps are in the [README](../README.md).

## Model runs: Test A and Test B (`lane_reasoner/`)

Every final label is sent to the model twice. **Test A**: the photo with the target marking in a cyan box and the task. **Test B**: the same plus the rule passages of the photo's region. Everything else (task text, answer schema, model, settings, image) is identical, and every request records hashes of all its parts, so a comparison can check that the two runs differ only in the rule text.

```bash
python -m lane_reasoner selftest          # free: synthetic images, mock answers, a fake API server
python -m lane_reasoner prompt --test B   # the exact prompt
python -m lane_reasoner ping --real       # one tiny request: checks the key, the model name and the settings
python -m lane_reasoner ask <image_id> --real          # one image, Test A and B, reasoning printed step by step
python -m lane_reasoner run --test A --real
python -m lane_reasoner run --test B --real --trace  # --trace prints the reasoning of every answer as it arrives
python -m lane_reasoner trace <run_id> [image_id]    # reasoning steps of a saved run (also in runs/<run_id>/trace.md)
python -m lane_reasoner compare <run_A> <run_B>
python -m lane_reasoner table <run_ids>   # experiment table from saved runs
python -m lane_reasoner rescore <run_ids> # score saved answers again after a scoring or rule-table change
python -m lane_reasoner demo              # demo page in the browser
```

`experiment.ipynb` does the same step by step and asks for the API key in a hidden box (it is written to `.env`). `run --test AB` (or **A + B** on the demo page) runs both tests at the same time on the same images and compares them.

| Where | What |
|---|---|
| `config/experiment.yaml` | `experiment` (region, `use_rules` no/yes = Test A/B, prompt version, split, repeats, mock), `model` (API address, key variable, model, reasoning effort and summary, temperature, image detail, output limit, price), `data` (workspaces whose final labels are used, `send_to_api`), `image` (target box), `regions` (name in the prompt and the rules: passages file, region code, title, language) |
| `prompts/v3/` | `role.txt`, `procedure.txt` (the four steps), `fields.txt` (field definitions), slots `step2_A/B.txt` and `citation_A/B.txt`, `rules_header.txt`, `user.txt`, `examples.json`, `answer_fields.txt` (order of the answer fields: reasoning before the decision); see `prompts/v3/README.md`. Default |
| `prompts/v1/`, `prompts/v2/` | the Milestone 4 versions: one `instructions.txt` with the same slots; v2 explained in `prompts/v2/README.md` |
| `runs/<run_id>/` | `manifest.json` (settings, prompt and label hashes, split version, Git commit, hash of the request and scoring code, image list), `results.jsonl` (one line per request: settings, raw answer, parsed answer, score), `scores.json`, `summary.md`, `trace.md` (reasoning steps of every answer) |
| `runs/cache/` | answers by request hash, so an identical request is not paid twice |

* Request: OpenAI Responses API (`POST /v1/responses`) with the Python standard library: an instructions message (developer role), a user message with one sentence and the boxed image (`input_image`, data URL, `detail` from the settings), and the answer schema as `text.format` (`json_schema`, strict). Rate limits, server errors and timeouts are retried; other errors stop with the API's message and the parameter it names.
* Answer (v3, in this order): `description`, `evidence` (full / partial / insufficient), `marking` (Output 1: marking type, arrow type, position), `rule_reasoning`, `cited_rule_id` (Test B; null in Test A), `action_reasons`, `self_check`, `actions` (Output 2: six actions, each allowed / prohibited / not_determined / not_applicable). v1 and v2 have `description`, `evidence`, `marking`, `actions`, `cited_rule_id`, `reasoning`.
* Reasoning summary: with `model.reasoning_summary: auto` the request asks for the model's summary of its hidden reasoning; it is saved with the answer and printed in the trace. If the API refuses it, the request is sent again without it and the trace says why.
* Hallucination indicators: confidently wrong answers (evidence `full` but wrong), inconsistent answers (`scoring.consistency_issues`: an action set for a marking class that does not govern it, `not_determined` with full evidence, arrow directions missing or on a non-arrow; checked without labels), unsupported citations.
* Scores: Output 1 accuracy and confusion table; Output 2 exact match over the actions the label decides (contested cells reported separately); per-action accuracy; the five evidence groups; citation check (accepted / in the pack but not accepted / not in the pack / none); unsafe and over-cautious errors; with repeats, the majority answer and the flip rate; and the exact McNemar test between Test A and Test B on the same images.
* Adding a region: a passages file in `rules/` (every passage with `rule_id`, `region`, `source`, `section`, `page`, `marking_type`, `text_en`, and `text_zh` or another original text), an entry under `regions` in `config/experiment.yaml`, rows in `config/action_rules.json` with the same region code, and labeled images in a workspace listed under `data.workspaces`. The prompt files do not change. China (`CN`) is set up and only needs labeled images.

### Milestone 4: first model exploration (`model_exploration.ipynb`)

The notebook follows the homework: role of AI and candidates, data audit (what is used, dropped or left unchanged), Test A as the first candidate on the **development images only**, metrics (Output 2 exact match, unsafe errors, Output 1 accuracy / per-class F1 / confusion matrix, evidence groups, readability, repeatability), error cases with crops, latency and cost against the targets in 2.1, Test B as the one targeted change on the same images, and the experiment table (also saved as `runs/milestone4_experiment_table.md`). Finished runs with the same settings, prompt, images and labels are reused, so running it again costs nothing.

A drive that was looked at while developing the prompt can be moved to the development split, with the reason logged:

```bash
python -m video_tool --data "<root>/UF" resplit <trip> dev --reason "used while developing the prompt"
python -m video_tool combine "<root>/UF" "<root>/bdd100k" "<root>/culane"   # writes the next labels/split_v<N>.csv
```
