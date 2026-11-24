# Lane run 20261117_225842_laneB_US

Test B (image + the region's rule passages), region US, 108 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 5/104 (5%); without the lines across the lane: 16/104 (15%)
- Lane actions (every action the label decides, contested cells excluded): 60/101 (59%)
- Left boundary: 71/103 (69%); right boundary: 43/102 (42%); both: 31/103 (30%)
- Markings in the lane, exact set: 7/101 (7%) (without the lines across the lane 47/101 (47%)); added (not in the label): 175, of them lines across the lane 60, by the evidence the answer gave {'full': 87, 'insufficient': 88}; missed: 13
- Lane count: 43/101 (43%); position of my lane: 43/103 (42%)
- Unsafe errors (label prohibited, answer allowed): 3 {'turn_left': 2, 'change_left': 1}; over-cautious: 43; contested unsafe: 3
- Prohibited actions also prohibited by the answer: 62/68 (91%)
- Actions decided where the label has no governing marking: 38
- Answers that contradict themselves: 28 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 12, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 4, 'turn_left not_applicable': 3, 'leftmost lane, but a lane line on the left': 3, 'go_straight allowed': 2, 'change_left prohibited': 2, 'go_straight, turn_right decided without an arrow or prohibited-movement marking': 1, 'turn_left decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 100, 'in_pack_not_accepted': 5, 'unlisted': 3}; IDs written with brackets (read without them): 83
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 101
- Tokens: {'input_tokens': 65422, 'cached_input_tokens': 0, 'output_tokens': 6386}; cost about $0.0; latency: {'mean': 14.35, 'max': 26.92}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 77 |
| change_right | 51 | 25 |
| go_straight | 9 | 6 |
| turn_left | 9 | 6 |
| turn_right | 9 | 8 |
| u_turn | 9 | 7 |
