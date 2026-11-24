# Lane run 20261118_000010_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 13/121 (11%); without the lines across the lane: 21/121 (17%)
- Lane actions (every action the label decides, contested cells excluded): 37/116 (32%)
- Left boundary: 53/121 (44%); right boundary: 45/118 (38%); both: 28/121 (23%)
- Markings in the lane, exact set: 33/118 (28%) (without the lines across the lane 78/118 (66%)); added (not in the label): 93, of them lines across the lane 50, by the evidence the answer gave {'partial': 23, 'insufficient': 15, 'full': 55}; missed: 40
- Lane count: 53/118 (45%); position of my lane: 59/119 (50%)
- Unsafe errors (label prohibited, answer allowed): 84 {'change_left': 22, 'change_right': 39, 'turn_right': 16, 'go_straight': 4, 'turn_left': 2, 'u_turn': 1}; over-cautious: 31; contested unsafe: 16
- Prohibited actions also prohibited by the answer: 77/174 (44%)
- Actions decided where the label has no governing marking: 40
- Answers that contradict themselves: 34 {'change_left prohibited across a broken lane line': 20, 'leftmost lane, but a lane line on the left': 8, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'turn_left, u_turn decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1, 'change_left decided': 1, 'go_straight prohibited': 1}
- Citations (Test B and C): {'accepted': 90, 'in_pack_not_accepted': 33, 'unlisted': 1}; IDs written with brackets (read without them): 373
- Boundary evidence: {'same': 142, 'unsupported_guess': 106}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1048296, 'cached_input_tokens': 0, 'output_tokens': 121816}; cost about $0.0; latency: {'mean': 7.45, 'max': 11.19}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 72 |
| change_right | 108 | 57 |
| go_straight | 25 | 18 |
| turn_left | 25 | 17 |
| turn_right | 25 | 3 |
| u_turn | 25 | 18 |
