# Lane run 20261117_182216_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 23/121 (19%); without the lines across the lane: 23/121 (19%)
- Lane actions (every action the label decides, contested cells excluded): 52/117 (44%)
- Left boundary: 41/121 (34%); right boundary: 45/118 (38%); both: 26/121 (21%)
- Markings in the lane, exact set: 65/118 (55%) (without the lines across the lane 73/118 (62%)); added (not in the label): 9, of them lines across the lane 3, by the evidence the answer gave {'full': 9}; missed: 18
- Lane count: 46/118 (39%); position of my lane: 54/119 (45%)
- Unsafe errors (label prohibited, answer allowed): 28 {'change_right': 15, 'change_left': 11, 'go_straight': 2}; over-cautious: 15; contested unsafe: 6
- Prohibited actions also prohibited by the answer: 91/161 (57%)
- Actions decided where the label has no governing marking: 15
- Answers that contradict themselves: 11 {'u_turn decided without an arrow or prohibited-movement marking': 5, 'rightmost lane, but a lane line on the right': 2, 'leftmost lane, but a lane line on the left': 2, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 73, 'same': 103, 'other': 72}
- Readable answers: 88/124 (an unreadable or failed answer counts as wrong); errors: 36; from cache: 0
- Tokens: {'input_tokens': 334136, 'cached_input_tokens': 0, 'output_tokens': 57957}; cost about $0.0; latency: {'mean': 11.84, 'max': 20.74}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 106 | 56 |
| change_right | 107 | 58 |
| go_straight | 25 | 18 |
| turn_left | 22 | 14 |
| turn_right | 21 | 13 |
| u_turn | 22 | 14 |
