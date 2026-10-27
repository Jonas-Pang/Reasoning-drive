# Run 20261027_021643_testA_US

Test A (image only), region US, 40 images × 3 repeat(s), model gpt-6.1-sol

- Output 1 (marking type): 40/40 (100%)
- Output 2 (actions the marking decides, contested cells excluded): 36/37 (97%)
- Contested cells, separately: 3/7 (43%)
- Unsafe errors (label prohibited, answer allowed): 1; over-cautious errors: 0 (contested cells, separately: 0 unsafe, 4 over-cautious)
- Evidence groups: {'correct': 39, 'wrong': 1}
- Citations (Test B): {}
- Answers that contradict themselves (hallucination indicator): 6
- Readable answers: 120/120; errors: 0; from cache: 40
- Tokens: {'input_tokens': 168400, 'output_tokens': 17360}; cost ≈ $0.5104; latency: {'mean': 4.83, 'max': 12.17}

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
