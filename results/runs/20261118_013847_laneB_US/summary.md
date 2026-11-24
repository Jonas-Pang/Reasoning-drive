# Lane run 20261118_013847_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 8/38 (21%); without the lines across the lane: 9/38 (24%)
- Lane actions (every action the label decides, contested cells excluded): 23/36 (64%)
- Left boundary: 23/37 (62%); right boundary: 19/37 (51%); both: 12/38 (32%)
- Markings in the lane, exact set: 28/37 (76%) (without the lines across the lane 31/37 (84%)); added (not in the label): 7, of them lines across the lane 1, by the evidence the answer gave {'full': 7}; missed: 5
- Lane count: 19/38 (50%); position of my lane: 25/38 (66%)
- Unsafe errors (label prohibited, answer allowed): 8 {'change_left': 2, 'change_right': 2, 'turn_left': 2, 'u_turn': 2}; over-cautious: 9; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 34/47 (72%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 7 {'leftmost lane, but a lane line on the left': 3, 'rightmost lane, but a lane line on the right': 2, 'enter_waiting_area allowed without a waiting area or two-way left-turn lane': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 34, 'unlisted': 2, 'in_pack_not_accepted': 2}; IDs written with brackets (read without them): 85
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 355148, 'cached_input_tokens': 0, 'output_tokens': 35844}; cost about $0.0; latency: {'mean': 13.61, 'max': 30.88}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 30 |
| change_right | 20 | 14 |
| go_straight | 8 | 7 |
| turn_left | 8 | 3 |
| turn_right | 8 | 5 |
| u_turn | 8 | 3 |
