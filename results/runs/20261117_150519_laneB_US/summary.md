# Lane run 20261117_150519_laneB_US

Test B (image + the region's rule passages), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 39/104 (38%); without the lines across the lane: 41/104 (39%)
- Lane actions (every action the label decides, contested cells excluded): 69/101 (68%)
- Left boundary: 68/103 (66%); right boundary: 64/102 (63%); both: 41/103 (40%)
- Markings in the lane, exact set: 87/101 (86%) (without the lines across the lane 92/101 (91%)); added (not in the label): 8, of them lines across the lane 1, by the evidence the answer gave {'full': 8}; missed: 12
- Lane count: 64/101 (63%); position of my lane: 76/103 (74%)
- Unsafe errors (label prohibited, answer allowed): 6 {'change_left': 4, 'turn_left': 2}; over-cautious: 18; contested unsafe: 7
- Prohibited actions also prohibited by the answer: 55/67 (82%)
- Actions decided where the label has no governing marking: 9
- Answers that contradict themselves: 10 {'change_right decided': 2, 'change_left decided': 2, 'leftmost lane, but a lane line on the left': 2, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'turn_right decided without an arrow or prohibited-movement marking': 1, 'enter_waiting_area allowed without a waiting area or two-way left-turn lane': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {'accepted': 96, 'unlisted': 7, 'in_pack_not_accepted': 5}; IDs written with brackets (read without them): 224
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 990252, 'cached_input_tokens': 0, 'output_tokens': 96632}; cost about $0.0; latency: {'mean': 15.17, 'max': 46.38}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 84 |
| change_right | 51 | 30 |
| go_straight | 9 | 8 |
| turn_left | 9 | 5 |
| turn_right | 10 | 5 |
| u_turn | 9 | 6 |
