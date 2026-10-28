# Run 20261027_221432_testB_US

Test B (image + rule passages), region US, 40 images × 3 repeat(s), model gpt-6.1-sol

- Output 1 (marking type): 39/40 (98%)
- Output 2 (actions the marking decides, contested cells excluded): 34/37 (92%)
- Contested cells, separately: 1/7 (14%)
- Unsafe errors (label prohibited, answer allowed): 2; over-cautious errors: 0 (contested cells, separately: 0 unsafe, 6 over-cautious)
- Evidence groups: {'correct': 37, 'over_withholding': 1, 'wrong': 2}
- Citations (Test B): {'accepted': 37, 'none': 1, 'none_needed': 2}
- Answers that contradict themselves (hallucination indicator): 0
- Readable answers: 120/120; errors: 0; from cache: 0
- Tokens: {'input_tokens': 502440, 'output_tokens': 37983}; cost ≈ $1.3847; latency: {'mean': 5.02, 'max': 10.59}

| Label | Images | Output 1 correct |
|---|---|---|
| arrow/left | 5 | 5 |
| arrow/straight | 3 | 3 |
| arrow/straight_left | 1 | 1 |
| other | 2 | 2 |
| two_way_left_turn_lane | 2 | 2 |
| white_dashed | 7 | 7 |
| white_solid | 1 | 1 |
| yellow_double_solid | 15 | 15 |
| yellow_solid | 4 | 3 |
