# Prompt version v3

The prompt is split into files by what they do. A request is built from them in this order:

| File | Part of the request | What it contains |
|---|---|---|
| `role.txt` | instructions (developer message) | who the model is and which marking it judges |
| `procedure.txt` | instructions | how to process the photo: the four steps (look, rule, decide, check) and the order in which they are written |
| `step2_A.txt` / `step2_B.txt` | slot `{STEP2}` in `procedure.txt` | step 2 without rules (Test A: recall the region's rule) or with rules (Test B: use the passages below) |
| `fields.txt` | instructions | how to fill in each answer field, with the definitions of the marking types and the six actions |
| `citation_A.txt` / `citation_B.txt` | slot `{CITATION}` in `fields.txt` | how to fill in `cited_rule_id` |
| `rules_header.txt` + passages | instructions, Test B only | the heading of the rule block, then every passage of the region (file and code set in `config/experiment.yaml`) |
| `examples.json` | instructions | fixed text examples (empty: zero-shot) |
| `user.txt` | user message, followed by the photo | the input sentence, with the region's name |
| `answer_fields.txt` | answer schema | the order of the answer fields |

Test A and Test B differ only in the two slots and the rule block.

## Reasoning before the decision

The answer is strict JSON, and the model writes its fields in the order of `answer_fields.txt`:

1. `description`, `evidence`, `marking`: what is visible (Output 1)
2. `rule_reasoning`, `cited_rule_id`: which rule applies and what it says
3. `action_reasons`: one reason per action, from steps 1 and 2
4. `self_check`: the answer checked against the task definition
5. `actions`: the final decision (Output 2)

In v1 and v2, `actions` came before `reasoning`, so the reasoning was written after the decision. In v3 every decision is written after the steps it depends on. `python -m lane_reasoner ask <image_id>` and `python -m lane_reasoner trace <run_id>` print these steps for each answer.

The model also reasons internally before it writes the answer (`reasoning_effort`). Those tokens are not returned; with `model.reasoning_summary: auto` in `config/experiment.yaml` the API adds the model's own summary of them, which the trace shows as well.
