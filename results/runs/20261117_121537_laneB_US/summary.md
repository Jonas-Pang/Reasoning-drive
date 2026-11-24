# Lane run 20261117_121537_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 9/38 (24%); without the lines across the lane: 10/38 (26%)
- Lane actions (every action the label decides, contested cells excluded): 23/37 (62%)
- Left boundary: 24/37 (65%); right boundary: 19/37 (51%); both: 13/38 (34%)
- Markings in the lane, exact set: 26/37 (70%) (without the lines across the lane 29/37 (78%)); added (not in the label): 9, of them lines across the lane 1, by the evidence the answer gave {'full': 9}; missed: 6
- Lane count: 17/38 (45%); position of my lane: 24/38 (63%)
- Unsafe errors (label prohibited, answer allowed): 7 {'change_left': 4, 'turn_left': 3}; over-cautious: 11; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 34/42 (81%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 7 {'leftmost lane, but a lane line on the left': 3, 'rightmost lane, but a lane line on the right': 2, 'change_left allowed': 1, 'enter_waiting_area allowed without a waiting area or two-way left-turn lane': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 35, 'in_pack_not_accepted': 2, 'unlisted': 1}; IDs written with brackets (read without them): 88
- Boundary evidence: {'same': 72, 'unsupported_guess': 3, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 348422, 'cached_input_tokens': 0, 'output_tokens': 35932}; cost about $0.0; latency: {'mean': 17.95, 'max': 62.67}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 28 |
| change_right | 21 | 16 |
| go_straight | 8 | 5 |
| turn_left | 8 | 3 |
| turn_right | 8 | 5 |
| u_turn | 7 | 4 |
