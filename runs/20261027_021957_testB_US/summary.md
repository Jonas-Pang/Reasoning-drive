# Run 20261027_021957_testB_US

Test B (image + rule passages), region US, 40 images × 3 repeat(s), model gpt-6.1-sol

- Output 1 (marking type): 40/40 (100%)
- Output 2 (actions the marking decides, contested cells excluded): 36/37 (97%)
- Contested cells, separately: 1/7 (14%)
- Unsafe errors (label prohibited, answer allowed): 0; over-cautious errors: 0 (contested cells, separately: 0 unsafe, 6 over-cautious)
- Evidence groups: {'correct': 39, 'over_withholding': 1}
- Citations (Test B): {'accepted': 37, 'in_pack_not_accepted': 1, 'none_needed': 2}
- Answers that contradict themselves (hallucination indicator): 0
- Readable answers: 120/120; errors: 0; from cache: 0
- Tokens: {'input_tokens': 475200, 'output_tokens': 26744}; cost ≈ $1.2178; latency: {'mean': 4.13, 'max': 9.67}

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
| yellow_solid | 4 | 4 |
