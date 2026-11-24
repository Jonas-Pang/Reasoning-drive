# Lane run 20261117_043107_laneB_US

Test B (image + the region's rule passages), region US, 108 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 2/104 (2%); without the lines across the lane: 12/104 (12%)
- Lane actions (every action the label decides, contested cells excluded): 43/102 (42%)
- Left boundary: 63/103 (61%); right boundary: 31/102 (30%); both: 18/103 (17%)
- Markings in the lane, exact set: 6/101 (6%) (without the lines across the lane 63/101 (62%)); added (not in the label): 169, of them lines across the lane 71, by the evidence the answer gave {'full': 85, 'insufficient': 84}; missed: 13
- Lane count: 41/101 (41%); position of my lane: 43/103 (42%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 1, 'turn_left': 2, 'go_straight': 1}; over-cautious: 48; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 47/72 (65%)
- Actions decided where the label has no governing marking: 18
- Answers that contradict themselves: 24 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 10, 'turn_left not_applicable': 4, 'go_straight allowed': 3, 'turn_right not_applicable': 3, 'change_right allowed across a curb': 2, 'leftmost lane, but a lane line on the left': 2, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight decided from an arrow that cannot be read': 1}
- Citations (Test B and C): {'accepted': 96, 'in_pack_not_accepted': 8, 'unlisted': 4}; IDs written with brackets (read without them): 107
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 932472, 'cached_input_tokens': 0, 'output_tokens': 91689}; cost about $0.0; latency: {'mean': 7.77, 'max': 12.64}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 74 |
| change_right | 54 | 15 |
| go_straight | 10 | 7 |
| turn_left | 10 | 1 |
| turn_right | 11 | 2 |
| u_turn | 9 | 1 |
