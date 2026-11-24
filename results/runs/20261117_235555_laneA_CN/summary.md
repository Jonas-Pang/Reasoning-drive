# Lane run 20261117_235555_laneA_CN

Test A (image only), region CN, 25 images, one request each, model meta-muse-glimmer-30b

- Lane identified (both boundaries and the markings): 5/25 (20%); without the lines across the lane: 5/25 (20%)
- Lane actions (every action the label decides, contested cells excluded): 9/21 (43%)
- Left boundary: 9/25 (36%); right boundary: 7/25 (28%); both: 5/25 (20%)
- Markings in the lane, exact set: 15/25 (60%) (without the lines across the lane 17/25 (68%)); added (not in the label): 6, of them lines across the lane 0, by the evidence the answer gave {'full': 2, 'partial': 4}; missed: 6
- Lane count: 12/22 (55%); position of my lane: 14/22 (64%)
- Unsafe errors (label prohibited, answer allowed): 6 {'change_left': 3, 'change_right': 2, 'turn_right': 1}; over-cautious: 10; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 19/28 (68%)
- Actions decided where the label has no governing marking: 11
- Answers that contradict themselves: 1 {'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 34, 'unsupported_guess': 6, 'over_withholding': 4, 'other': 6}
- Readable answers: 22/25 (an unreadable or failed answer counts as wrong); errors: 3; from cache: 0
- Tokens: {'input_tokens': 153120, 'cached_input_tokens': 0, 'output_tokens': 80025}; cost about $0.0; latency: {'mean': 17.72, 'max': 28.33}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 12 |
| change_right | 21 | 10 |
| go_straight | 3 | 2 |
| turn_left | 3 | 3 |
| turn_right | 3 | 2 |
| u_turn | 3 | 3 |
