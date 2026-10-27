# Run 20261027_021835_testA_US

Test A (image only), region US, 40 images × 3 repeat(s), model gpt-6.1-sol

- Output 1 (marking type): 39/40 (98%)
- Output 2 (actions the marking decides, contested cells excluded): 35/37 (95%)
- Contested cells, separately: 7/7 (100%)
- Unsafe errors (label prohibited, answer allowed): 1; over-cautious errors: 0 (contested cells, separately: 0 unsafe, 0 over-cautious)
- Evidence groups: {'correct': 38, 'over_withholding': 1, 'wrong': 1}
- Citations (Test B): {}
- Answers that contradict themselves (hallucination indicator): 0
- Readable answers: 120/120; errors: 0; from cache: 0
- Tokens: {'input_tokens': 282960, 'output_tokens': 25686}; cost ≈ $0.8228; latency: {'mean': 4.78, 'max': 12.86}

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
