# Run 20261102_150116_testB_US

Test B (image + rule passages), region US, 40 images × 3 repeat(s), model gpt-6-sol

- Output 1 (marking type): 33/40 (82%)
- Output 2 (actions the marking decides, contested cells excluded): 30/37 (81%)
- Contested cells, separately: 1/7 (14%)
- Unsafe errors (label prohibited, answer allowed): 0; over-cautious errors: 5 (contested cells, separately: 0 unsafe, 6 over-cautious)
- Evidence groups: {'correct': 32, 'over_withholding': 5, 'wrong': 3}
- Citations (Test B): {'unlisted': 39, 'none_needed': 1}
- Answers that contradict themselves (hallucination indicator): 1
- Readable answers: 120/120; errors: 0; from cache: 0
- Tokens: {'input_tokens': 511440, 'cached_input_tokens': 460532, 'output_tokens': 28236}; cost ≈ $0.4763; latency: {'mean': 2.83, 'max': 6.85}

| Label | Images | Output 1 correct |
|---|---|---|
| arrow/left | 5 | 3 |
| arrow/straight | 3 | 3 |
| arrow/straight_left | 1 | 0 |
| other | 2 | 1 |
| two_way_left_turn_lane | 2 | 0 |
| white_dashed | 7 | 7 |
| white_solid | 1 | 1 |
| yellow_double_solid | 15 | 15 |
| yellow_solid | 4 | 3 |
