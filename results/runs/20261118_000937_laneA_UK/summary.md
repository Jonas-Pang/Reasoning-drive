# Lane run 20261118_000937_laneA_UK

Test A (image only), region UK, 8 images, one request each, model meta-muse-glimmer-30b

- Lane identified (both boundaries and the markings): 1/8 (12%); without the lines across the lane: 1/8 (12%)
- Lane actions (every action the label decides, contested cells excluded): 0/4 (0%)
- Left boundary: 2/8 (25%); right boundary: 2/7 (29%); both: 1/8 (12%)
- Markings in the lane, exact set: 4/8 (50%) (without the lines across the lane 4/8 (50%)); added (not in the label): 2, of them lines across the lane 0, by the evidence the answer gave {'full': 2}; missed: 2
- Lane count: 4/7 (57%); position of my lane: 4/7 (57%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 3; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 0/3 (0%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 9, 'other': 5, 'over_withholding': 1, 'unsupported_guess': 1}
- Readable answers: 6/8 (an unreadable or failed answer counts as wrong); errors: 2; from cache: 0
- Tokens: {'input_tokens': 45006, 'cached_input_tokens': 0, 'output_tokens': 24147}; cost about $0.0; latency: {'mean': 26.37, 'max': 39.29}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 0 |
| change_right | 4 | 0 |
| go_straight | 1 | 0 |
| turn_left | 1 | 0 |
| turn_right | 1 | 0 |
| u_turn | 1 | 0 |
