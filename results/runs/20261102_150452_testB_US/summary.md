# Run 20261102_150452_testB_US

Test B (image + rule passages), region US, 40 images × 3 repeat(s), model gpt-6-sol

- Output 1 (marking type): 37/40 (92%)
- Output 2 (actions the marking decides, contested cells excluded): 34/37 (92%)
- Contested cells, separately: 1/7 (14%)
- Unsafe errors (label prohibited, answer allowed): 0; over-cautious errors: 2 (contested cells, separately: 0 unsafe, 6 over-cautious)
- Evidence groups: {'correct': 37, 'over_withholding': 2, 'wrong': 1}
- Citations (Test B): {'unlisted': 31, 'accepted': 7, 'none_needed': 2}
- Answers that contradict themselves (hallucination indicator): 1
- Readable answers: 120/120; errors: 0; from cache: 0
- Tokens: {'input_tokens': 511440, 'cached_input_tokens': 459403, 'output_tokens': 40410}; cost ≈ $0.6001; latency: {'mean': 3.81, 'max': 9.66}

| Label | Images | Output 1 correct |
|---|---|---|
| arrow/left | 5 | 5 |
| arrow/straight | 3 | 3 |
| arrow/straight_left | 1 | 0 |
| other | 2 | 2 |
| two_way_left_turn_lane | 2 | 1 |
| white_dashed | 7 | 7 |
| white_solid | 1 | 1 |
| yellow_double_solid | 15 | 15 |
| yellow_solid | 4 | 3 |
