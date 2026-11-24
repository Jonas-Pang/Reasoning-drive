# Lane run 20261117_044746_laneA_US

Test A (image only), region US, 38 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/38 (3%); without the lines across the lane: 4/38 (11%)
- Lane actions (every action the label decides, contested cells excluded): 15/37 (41%)
- Left boundary: 16/37 (43%); right boundary: 16/37 (43%); both: 7/38 (18%)
- Markings in the lane, exact set: 4/37 (11%) (without the lines across the lane 21/37 (57%)); added (not in the label): 36, of them lines across the lane 19, by the evidence the answer gave {'full': 18, 'partial': 13, 'insufficient': 5}; missed: 10
- Lane count: 14/38 (37%); position of my lane: 17/38 (45%)
- Unsafe errors (label prohibited, answer allowed): 13 {'change_left': 6, 'change_right': 4, 'go_straight': 1, 'turn_left': 1, 'turn_right': 1}; over-cautious: 6; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 16/42 (38%)
- Actions decided where the label has no governing marking: 27
- Answers that contradict themselves: 24 {'leftmost lane, but a lane line on the left': 14, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 6, 'change_left allowed across a curb': 3, 'go_straight, turn_left decided without an arrow or prohibited-movement marking': 1, 'change_left decided': 1, 'change_right prohibited across a broken lane line': 1, 'change_left prohibited across a broken lane line': 1, 'turn_right allowed': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 71, 'unsupported_guess': 4, 'over_withholding': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 38
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 26 |
| change_right | 21 | 11 |
| go_straight | 8 | 7 |
| turn_left | 8 | 1 |
| turn_right | 8 | 1 |
| u_turn | 7 | 0 |
