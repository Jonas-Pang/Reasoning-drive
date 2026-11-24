# Lane run 20261117_234328_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 3/121 (2%); without the lines across the lane: 20/121 (17%)
- Lane actions (every action the label decides, contested cells excluded): 37/116 (32%)
- Left boundary: 47/121 (39%); right boundary: 45/118 (38%); both: 29/121 (24%)
- Markings in the lane, exact set: 14/118 (12%) (without the lines across the lane 77/118 (65%)); added (not in the label): 99, of them lines across the lane 59, by the evidence the answer gave {'full': 54, 'partial': 22, 'insufficient': 23}; missed: 24
- Lane count: 53/118 (45%); position of my lane: 58/119 (49%)
- Unsafe errors (label prohibited, answer allowed): 62 {'change_left': 21, 'change_right': 32, 'turn_left': 2, 'u_turn': 2, 'go_straight': 4, 'turn_right': 1}; over-cautious: 51; contested unsafe: 7
- Prohibited actions also prohibited by the answer: 103/174 (59%)
- Actions decided where the label has no governing marking: 94
- Answers that contradict themselves: 34 {'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 15, 'leftmost lane, but a lane line on the left': 12, 'turn_right allowed': 2, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'change_right decided': 1, 'change_left prohibited across a broken lane line': 1, 'change_right prohibited across a broken lane line': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 470332, 'cached_input_tokens': 0, 'output_tokens': 123507}; cost about $0.0; latency: {'mean': 7.06, 'max': 23.37}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 61 |
| change_right | 108 | 56 |
| go_straight | 25 | 20 |
| turn_left | 25 | 18 |
| turn_right | 25 | 21 |
| u_turn | 25 | 18 |
