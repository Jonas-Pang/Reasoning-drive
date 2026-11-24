# Model runs

Reference for the model-run package. The project overview, results and reproduction steps are in the [README](../README.md).

## Model runs: Test A and Test B (`reasoning_drive/`)

Every final label is sent to the model twice. **Test A**: the photo with the target marking in a cyan box and the task. **Test B**: the same plus the rule passages of the photo's region. Everything else (task text, answer schema, model, settings, image) is identical, and every request records hashes of all its parts, so a comparison can check that the two runs differ only in the rule text.

```bash
python main.py selftest          # free: synthetic images, mock answers, a fake API server
python main.py prompt --test B   # the exact prompt
python main.py ping --real       # one tiny request: checks the key, the model name and the settings
python main.py ask <image_id> --real          # one image, Test A and B, reasoning printed step by step
python main.py run --test A --real
python main.py run --test B --real --trace  # --trace prints the reasoning of every answer as it arrives
python main.py trace <run_id> [image_id]    # reasoning steps of a saved run (also in results/runs/<run_id>/trace.md)
python main.py compare <run_A> <run_B>
python main.py table <run_ids>   # experiment table from saved runs
python main.py rescore <run_ids> # score saved answers again after a scoring or rule-table change
python main.py experiment E1_rules   # a named experiment of configs/experiments.yaml from its saved runs; --real runs missing variants
python main.py demo              # demo page in the browser
```

`notebooks/experiment.ipynb` does the same step by step and asks for the API key in a hidden box (it is written to `.env`). `run --test AB` (or **A + B** on the demo page) runs both tests at the same time on the same images and compares them.

| Where | What |
|---|---|
| `configs/experiment.yaml` | `experiment` (region, `use_rules` no/yes = Test A/B, prompt version, split, repeats, mock), `model` (API address, key variable, model, reasoning effort and summary, temperature, image detail, output limit, price), `data` (workspaces whose final labels are used, `send_to_api`), `image` (target box), `regions` (name in the prompt and the rules: passages file, region code, title, language) |
| `prompts/v3/` | `role.txt`, `procedure.txt` (the four steps), `fields.txt` (field definitions), slots `step2_A/B.txt` and `citation_A/B.txt`, `rules_header.txt`, `user.txt`, `examples.json`, `answer_fields.txt` (order of the answer fields: reasoning before the decision); see `prompts/v3/README.md`. Default |
| `prompts/v1/`, `prompts/v2/` | the Milestone 4 versions: one `instructions.txt` with the same slots; v2 explained in `prompts/v2/README.md` |
| `results/runs/<run_id>/` | `manifest.json` (settings, prompt and label hashes, split version, Git commit, hash of the request and scoring code, image list), `results.jsonl` (one line per request: settings, raw answer, parsed answer, score), `scores.json`, `summary.md`, `trace.md` (reasoning steps of every answer) |
| `configs/experiments.yaml` | named experiments (E1 rule text, E2 prompt version, E3 model setting, E4 repeats): question, what changes, what stays fixed, how it is judged, and per variant the settings that differ from `experiment.yaml` and the run that produced the reported result |
| `results/runs/cache/` | answers by request hash, so an identical request is not paid twice |

* Request: OpenAI Responses API (`POST /v1/responses`) with the Python standard library: an instructions message (developer role), a user message with one sentence and the boxed image (`input_image`, data URL, `detail` from the settings), and the answer schema as `text.format` (`json_schema`, strict). Rate limits, server errors and timeouts are retried; other errors stop with the API's message and the parameter it names.
* Answer (v3, in this order): `description`, `evidence` (full / partial / insufficient), `marking` (Output 1: marking type, arrow type, position), `rule_reasoning`, `cited_rule_id` (Test B; null in Test A), `action_reasons`, `self_check`, `actions` (Output 2: six actions, each allowed / prohibited / not_determined / not_applicable). v1 and v2 have `description`, `evidence`, `marking`, `actions`, `cited_rule_id`, `reasoning`.
* Reasoning summary: with `model.reasoning_summary: auto` the request asks for the model's summary of its hidden reasoning; it is saved with the answer and printed in the trace. If the API refuses it, the request is sent again without it and the trace says why.
* Hallucination indicators: confidently wrong answers (evidence `full` but wrong), inconsistent answers (`scoring.consistency_issues`: an action set for a marking class that does not govern it, `not_determined` with full evidence, arrow directions missing or on a non-arrow; checked without labels), unsupported citations.
* Cost: tokens from the API's usage record, priced per model with `model.price_per_million_tokens` in `configs/api.yaml`; input tokens served from the prompt cache are charged at `cached_input`.
* Scores: Output 1 accuracy and confusion table; Output 2 exact match over the actions the label decides (contested cells reported separately); per-action accuracy; the five evidence groups; citation check (accepted / in the pack but not accepted / not in the pack / none); unsafe and over-cautious errors; with repeats, the majority answer and the flip rate; and the exact McNemar test between Test A and Test B on the same images. Output 2 and the citation are taken from the same answer, the majority of the actions.
* Adding a region: a passages file in `regulations/` (every passage with `rule_id`, `region`, `source`, `section`, `page`, `marking_type`, `text_en`, and `text_zh` or another original text), an entry under `regions` in `configs/experiment.yaml`, rows in `regulations/<CODE>/action_rules.json` with the same region code, and labeled images in a workspace listed under `data.workspaces`. The prompt files do not change. China (`CN`) is set up and only needs labeled images.

### Milestone 4: first model exploration (`notebooks/model_exploration.ipynb`)

The notebook follows the homework: role of AI and candidates, data audit (what is used, dropped or left unchanged), Test A as the first candidate on the **development images only**, metrics (Output 2 exact match, unsafe errors, Output 1 accuracy / per-class F1 / confusion matrix, evidence groups, readability, repeatability), error cases with crops, latency and cost against the targets in 2.1, Test B as the one targeted change on the same images, and the experiment table (also saved as `results/runs/milestone4_experiment_table.md`). Finished runs with the same settings, prompt, images and labels are reused, so running it again costs nothing.

A drive that was looked at while developing the prompt can be moved to the development split, with the reason logged:

```bash
python main.py label --data "<root>/UF" resplit <trip> dev --reason "used while developing the prompt"
python main.py label combine "<root>/UF" "<root>/bdd100k" "<root>/culane"   # writes the next datasets/splits/split_v<N>.csv
```

## Lane-level task (`reasoning_drive/agent/lane.py`, Milestone 5)

```bash
python main.py lane prompt --test B --region CN     # the exact prompt (add --schema for the answer schema)
python main.py lane items                          # images with a final lane label
python main.py lane ask <image_id> --test AB --real # one image, every step of the answer printed
python main.py lane run --test AB --split dev --real
python main.py lane run --test C --split dev --real                # control: another region's passages
python main.py lane run --test AB --split dev --real --no-cache    # a repeat (new requests, not the cache)
python main.py lane compare <run_A> <run_B>                        # paired: McNemar and difference with 95% CI
python main.py lane compare <A_CN> <B_CN> <A_US> <B_US>            # each pair, then pooled over both regions
python main.py lane trace <run_id>
python main.py lane review                                         # blind review: items and decisions per region
python main.py lane rescore <run_id>... --reviewed                 # scores after the review, next to the originals
python main.py lane compare <run_A> <run_B> --reviewed
python main.py lane freeze --note "before the test run"            # freeze the protocol of the test run
python main.py lane protocol                                       # does everything still match it?
python main.py experiment E5_lane_rules --real     # --mock checks the pipeline for free
python main.py experiment E6_lane_controls         # Test C and the repeats, from the saved runs
```

* Settings: the `lane` section of `configs/experiment.yaml` (prompt folder, output limit); everything else (model, effort, image detail, split, region, Test A or B, mock) as for the single-marking task. Regions name their `driving_side` and the passage files of the lane task (`lane_rules`).
* Request: the photo re-encoded as JPEG without any drawing, one request per image (no repeats). Test B adds every passage of the region's lane files, grouped by element (general; lines and curbs beside a lane; arrows, words and symbols in a lane; special lanes; lines across a lane; marked areas). Test C (control) is Test B with the passages of another region (`lane.control_region`, otherwise the other configured region) under their own title; B and C differ only in the passages.
* Answer (in this order): `scene`, `lane_count`, `ego_lane_index`, `scene_evidence`, `left_boundary` and `right_boundary` (observation, colour, pattern, near line, curb, role, evidence), `lane_markings` (observation, marking token, evidence), `cross_check` (position, roles, markings, unseen, result), `element_rules` (element, rule ID, meaning), `action_reasons`, `decision_check`, `actions` (seven), `advice`.
* Runs: `results/runs/<time>_lane<A|B|C>_<region>/` with the same files as the single-marking runs; the manifest records `task: lane`, the lane code hash, the hash of the passage files, whose passages were listed (`rules_region`) and the protocol state. Lane runs are listed with `lane runs`, not with `runs`.
* Scores (`lane_scoring.py`): lane identified, lane actions (contested cells separately), each boundary attribute and role, markings exact set, markings added (not in the label) and missed, lane count and position, unsafe and over-cautious errors, prohibited actions kept, actions decided where the label has no governing marking, citations, boundary evidence, and contradictions inside the answer found without the label (a crossing allowed over a curb, a double solid line or the solid side of a solid-and-broken pair; a broken lane line that may not be crossed; a side that cannot be seen but is decided; a movement that disagrees with the reported arrows or is decided from an arrow that cannot be read; ONLY with a two-movement arrow; a waiting area entered without one; a lane position that disagrees with the boundary roles). Also: lane identified and markings without the lines across the lane (stop and yield lines, crosswalks), the evidence level of each added marking, and cited IDs written in brackets (counted, then read without them). An image without a readable answer counts as wrong wherever the label decides. `lane rescore` scores saved answers again without the API.
* Comparisons: exact McNemar on paired images and the difference in accuracy (second run minus first) with Newcombe's 95% interval for paired proportions; several pairs of runs can be pooled.
* Blind review (`reasoning_drive/evaluation/review.py`, page `/review` of the demo): every field where a saved answer differs from the label, with the values shown as options without their source; decisions in `results/runs/review/lane_review.csv`; the labels are not changed, and the scores after the review are written next to the originals (`scores_reviewed.json`).
* Frozen protocol (`reasoning_drive/evaluation/protocol.py`, `configs/lane_protocol.json`): prompt files, schema, rule table, passage files, prompt-building and scoring code, model settings and prompt hashes. Test images are answered only while they match, and each test runs once per region on them (`--again` is recorded).
* Smoke test (4 unlabeled frames, not scored, not saved as a run): the schema is accepted; Test A about 4,400 input tokens, Test B 8,600 (CN) to 9,300 (US); 1,000 to 1,700 output tokens; 17 to 40 s; $0.013 to $0.034 per request.
