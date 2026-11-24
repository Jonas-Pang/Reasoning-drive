# Lane run 20261117_020949_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/38 (0%); without the lines across the lane: 5/38 (13%)
- Lane actions (every action the label decides, contested cells excluded): 20/37 (54%)
- Left boundary: 16/37 (43%); right boundary: 15/37 (41%); both: 7/38 (18%)
- Markings in the lane, exact set: 4/37 (11%) (without the lines across the lane 24/37 (65%)); added (not in the label): 35, of them lines across the lane 23, by the evidence the answer gave {'full': 15, 'insufficient': 8, 'partial': 12}; missed: 10
- Lane count: 14/38 (37%); position of my lane: 19/38 (50%)
- Unsafe errors (label prohibited, answer allowed): 10 {'change_left': 4, 'change_right': 3, 'go_straight': 1, 'turn_left': 1, 'turn_right': 1}; over-cautious: 4; contested unsafe: 6
- Prohibited actions also prohibited by the answer: 18/42 (43%)
- Actions decided where the label has no governing marking: 10
- Answers that contradict themselves: 18 {'leftmost lane, but a lane line on the left': 11, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 5, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'change_left allowed': 1, 'turn_left allowed': 1, 'turn_right allowed': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {'accepted': 30, 'unlisted': 5, 'in_pack_not_accepted': 3}; IDs written with brackets (read without them): 116
- Boundary evidence: {'same': 71, 'other': 1, 'unsupported_guess': 3, 'over_withholding': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 327940, 'cached_input_tokens': 0, 'output_tokens': 42708}; cost about $0.0; latency: {'mean': 29.29, 'max': 46.18}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 26 |
| change_right | 21 | 15 |
| go_straight | 8 | 7 |
| turn_left | 8 | 0 |
| turn_right | 8 | 1 |
| u_turn | 7 | 0 |
