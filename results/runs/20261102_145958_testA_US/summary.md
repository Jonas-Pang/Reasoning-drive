# Run 20261102_145958_testA_US

Test A (image only), region US, 40 images × 3 repeat(s), model gpt-6-sol

- Output 1 (marking type): 34/40 (85%)
- Output 2 (actions the marking decides, contested cells excluded): 30/37 (81%)
- Contested cells, separately: 1/7 (14%)
- Unsafe errors (label prohibited, answer allowed): 3; over-cautious errors: 2 (contested cells, separately: 0 unsafe, 5 over-cautious)
- Evidence groups: {'correct': 32, 'wrong': 4, 'over_withholding': 4}
- Citations (Test B): {}
- Answers that contradict themselves (hallucination indicator): 0
- Readable answers: 120/120; errors: 0; from cache: 0
- Tokens: {'input_tokens': 319080, 'cached_input_tokens': 270904, 'output_tokens': 27945}; cost ≈ $0.43; latency: {'mean': 3.19, 'max': 9.47}

| Label | Images | Output 1 correct |
|---|---|---|
| arrow/left | 5 | 4 |
| arrow/straight | 3 | 3 |
| arrow/straight_left | 1 | 0 |
| other | 2 | 1 |
| two_way_left_turn_lane | 2 | 0 |
| white_dashed | 7 | 7 |
| white_solid | 1 | 1 |
| yellow_double_solid | 15 | 15 |
| yellow_solid | 4 | 3 |
