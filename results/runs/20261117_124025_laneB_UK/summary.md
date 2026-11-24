# Lane run 20261117_124025_laneB_UK

Test B (image + the region's rule passages), region UK, 37 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/37 (0%); without the lines across the lane: 1/37 (3%)
- Lane actions (every action the label decides, contested cells excluded): 6/29 (21%)
- Left boundary: 19/37 (51%); right boundary: 9/37 (24%); both: 5/37 (14%)
- Markings in the lane, exact set: 2/37 (5%) (without the lines across the lane 14/37 (38%)); added (not in the label): 76, of them lines across the lane 21, by the evidence the answer gave {'full': 48, 'insufficient': 28}; missed: 16
- Lane count: 4/19 (21%); position of my lane: 9/19 (47%)
- Unsafe errors (label prohibited, answer allowed): 1 {'go_straight': 1}; over-cautious: 24; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 7/21 (33%)
- Actions decided where the label has no governing marking: 15
- Answers that contradict themselves: 12 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 7, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'rightmost lane, but a lane line on the right': 1, 'leftmost lane, but a lane line on the left': 1, 'turn_left prohibited': 1, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {'accepted': 24, 'in_pack_not_accepted': 13}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 74}
- Readable answers: 37/37 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 513967, 'cached_input_tokens': 0, 'output_tokens': 28609}; cost about $0.0; latency: {'mean': 8.37, 'max': 14.94}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 5 |
| change_right | 26 | 9 |
| go_straight | 8 | 7 |
| turn_left | 8 | 2 |
| turn_right | 8 | 2 |
| u_turn | 7 | 2 |
