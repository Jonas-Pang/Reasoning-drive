# Lane run 20261118_000715_laneB_US

Test B (image + the region's rule passages), region US, 108 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 12/104 (12%); without the lines across the lane: 32/104 (31%)
- Lane actions (every action the label decides, contested cells excluded): 71/101 (70%)
- Left boundary: 52/103 (50%); right boundary: 53/102 (52%); both: 35/103 (34%)
- Markings in the lane, exact set: 23/101 (23%) (without the lines across the lane 83/101 (82%)); added (not in the label): 79, of them lines across the lane 61, by the evidence the answer gave {'full': 34, 'insufficient': 23, 'partial': 22}; missed: 17
- Lane count: 41/101 (41%); position of my lane: 46/103 (45%)
- Unsafe errors (label prohibited, answer allowed): 12 {'change_left': 12}; over-cautious: 18; contested unsafe: 32
- Prohibited actions also prohibited by the answer: 51/68 (75%)
- Actions decided where the label has no governing marking: 71
- Answers that contradict themselves: 40 {'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 18, 'change_left prohibited across a broken lane line': 9, 'leftmost lane, but a lane line on the left': 8, 'change_right prohibited across a broken lane line': 3, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'change_right decided': 2, 'change_right allowed across a curb': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 94, 'in_pack_not_accepted': 10, 'unlisted': 4}; IDs written with brackets (read without them): 328
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1008936, 'cached_input_tokens': 0, 'output_tokens': 114132}; cost about $0.0; latency: {'mean': 7.9, 'max': 13.06}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 74 |
| change_right | 51 | 40 |
| go_straight | 9 | 9 |
| turn_left | 9 | 7 |
| turn_right | 9 | 7 |
| u_turn | 9 | 7 |
