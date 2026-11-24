# Run 20261102_150301_testA_US

Test A (image only), region US, 40 images × 3 repeat(s), model gpt-6-sol

- Output 1 (marking type): 35/40 (88%)
- Output 2 (actions the marking decides, contested cells excluded): 31/37 (84%)
- Contested cells, separately: 2/7 (29%)
- Unsafe errors (label prohibited, answer allowed): 2; over-cautious errors: 4 (contested cells, separately: 0 unsafe, 5 over-cautious)
- Evidence groups: {'correct': 33, 'over_withholding': 5, 'wrong': 2}
- Citations (Test B): {}
- Answers that contradict themselves (hallucination indicator): 0
- Readable answers: 120/120; errors: 0; from cache: 0
- Tokens: {'input_tokens': 319080, 'cached_input_tokens': 272033, 'output_tokens': 40490}; cost ≈ $0.5534; latency: {'mean': 4.51, 'max': 12.05}

| Label | Images | Output 1 correct |
|---|---|---|
| arrow/left | 5 | 3 |
| arrow/straight | 3 | 3 |
| arrow/straight_left | 1 | 0 |
| other | 2 | 1 |
| two_way_left_turn_lane | 2 | 2 |
| white_dashed | 7 | 7 |
| white_solid | 1 | 1 |
| yellow_double_solid | 15 | 15 |
| yellow_solid | 4 | 3 |
