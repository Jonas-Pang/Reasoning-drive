# Lane run 20261117_044755_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 3/121 (2%); without the lines across the lane: 4/121 (3%)
- Lane actions (every action the label decides, contested cells excluded): 25/118 (21%)
- Left boundary: 37/121 (31%); right boundary: 37/118 (31%); both: 19/121 (16%)
- Markings in the lane, exact set: 14/118 (12%) (without the lines across the lane 34/118 (29%)); added (not in the label): 100, of them lines across the lane 24, by the evidence the answer gave {'full': 62, 'insufficient': 22, 'partial': 16}; missed: 32
- Lane count: 60/118 (51%); position of my lane: 74/119 (62%)
- Unsafe errors (label prohibited, answer allowed): 41 {'change_left': 16, 'change_right': 18, 'go_straight': 3, 'turn_right': 2, 'turn_left': 1, 'u_turn': 1}; over-cautious: 61; contested unsafe: 6
- Prohibited actions also prohibited by the answer: 47/142 (33%)
- Actions decided where the label has no governing marking: 57
- Answers that contradict themselves: 29 {'leftmost lane, but a lane line on the left': 21, 'change_left decided': 4, 'change_right prohibited across a broken lane line': 3, 'turn_right allowed': 2, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 106, 'same': 137, 'over_withholding': 5}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 363320, 'cached_input_tokens': 0, 'output_tokens': 116885}; cost about $0.0; latency: {'mean': 6.23, 'max': 20.51}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 47 |
| change_right | 108 | 40 |
| go_straight | 25 | 22 |
| turn_left | 22 | 0 |
| turn_right | 21 | 2 |
| u_turn | 21 | 0 |
