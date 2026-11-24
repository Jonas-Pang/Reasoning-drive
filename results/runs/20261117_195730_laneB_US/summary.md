# Lane run 20261117_195730_laneB_US

Test B (image + the region's rule passages), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 39/104 (38%); without the lines across the lane: 41/104 (39%)
- Lane actions (every action the label decides, contested cells excluded): 76/101 (75%)
- Left boundary: 68/103 (66%); right boundary: 64/102 (63%); both: 42/103 (41%)
- Markings in the lane, exact set: 86/101 (85%) (without the lines across the lane 91/101 (90%)); added (not in the label): 9, of them lines across the lane 1, by the evidence the answer gave {'full': 9}; missed: 12
- Lane count: 64/101 (63%); position of my lane: 73/103 (71%)
- Unsafe errors (label prohibited, answer allowed): 9 {'change_left': 5, 'turn_left': 2, 'u_turn': 2}; over-cautious: 20; contested unsafe: 6
- Prohibited actions also prohibited by the answer: 54/68 (79%)
- Actions decided where the label has no governing marking: 12
- Answers that contradict themselves: 11 {'leftmost lane, but a lane line on the left': 4, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'enter_waiting_area allowed without a waiting area or two-way left-turn lane': 2, 'rightmost lane, but a lane line on the right': 2, 'change_left allowed': 1, 'change_right decided': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 95, 'unlisted': 8, 'in_pack_not_accepted': 5}; IDs written with brackets (read without them): 230
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1009368, 'cached_input_tokens': 0, 'output_tokens': 97279}; cost about $0.0; latency: {'mean': 14.83, 'max': 28.54}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 84 |
| change_right | 51 | 37 |
| go_straight | 9 | 8 |
| turn_left | 9 | 5 |
| turn_right | 9 | 5 |
| u_turn | 9 | 5 |
