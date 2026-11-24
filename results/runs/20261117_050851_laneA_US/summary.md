# Lane run 20261117_050851_laneA_US

Test A (image only), region US, 108 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 3/104 (3%); without the lines across the lane: 16/104 (15%)
- Lane actions (every action the label decides, contested cells excluded): 48/102 (47%)
- Left boundary: 38/103 (37%); right boundary: 42/102 (41%); both: 24/103 (23%)
- Markings in the lane, exact set: 16/101 (16%) (without the lines across the lane 64/101 (63%)); added (not in the label): 82, of them lines across the lane 47, by the evidence the answer gave {'partial': 32, 'full': 41, 'insufficient': 9}; missed: 14
- Lane count: 41/101 (41%); position of my lane: 46/103 (45%)
- Unsafe errors (label prohibited, answer allowed): 15 {'change_left': 12, 'go_straight': 2, 'turn_left': 1}; over-cautious: 28; contested unsafe: 25
- Prohibited actions also prohibited by the answer: 32/72 (44%)
- Actions decided where the label has no governing marking: 70
- Answers that contradict themselves: 41 {'leftmost lane, but a lane line on the left': 23, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 10, 'change_left allowed across a curb': 4, 'change_left decided': 4, 'turn_left not_applicable': 1, 'u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1, 'change_left prohibited across a broken lane line': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 158, 'over_withholding': 8, 'unsupported_guess': 47, 'other': 3}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 317088, 'cached_input_tokens': 0, 'output_tokens': 100479}; cost about $0.0; latency: {'mean': 5.81, 'max': 7.48}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 63 |
| change_right | 54 | 28 |
| go_straight | 10 | 8 |
| turn_left | 10 | 0 |
| turn_right | 11 | 2 |
| u_turn | 9 | 0 |
