# Lane run 20261117_043732_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 108 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 2/104 (2%); without the lines across the lane: 14/104 (13%)
- Lane actions (every action the label decides, contested cells excluded): 47/102 (46%)
- Left boundary: 63/103 (61%); right boundary: 44/102 (43%); both: 28/103 (27%)
- Markings in the lane, exact set: 4/101 (4%) (without the lines across the lane 33/101 (33%)); added (not in the label): 334, of them lines across the lane 116, by the evidence the answer gave {'full': 51, 'insufficient': 283}; missed: 16
- Lane count: 41/101 (41%); position of my lane: 45/103 (44%)
- Unsafe errors (label prohibited, answer allowed): 8 {'change_left': 3, 'turn_left': 3, 'go_straight': 2}; over-cautious: 43; contested unsafe: 3
- Prohibited actions also prohibited by the answer: 43/72 (60%)
- Actions decided where the label has no governing marking: 21
- Answers that contradict themselves: 46 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 32, 'go_straight decided from an arrow that cannot be read': 21, 'turn_left not_applicable': 3, 'leftmost lane, but a lane line on the left': 3, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'turn_left allowed': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 85, 'unlisted': 23}; IDs written with brackets (read without them): 190
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 820908, 'cached_input_tokens': 0, 'output_tokens': 85724}; cost about $0.0; latency: {'mean': 7.33, 'max': 12.12}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 75 |
| change_right | 54 | 18 |
| go_straight | 10 | 6 |
| turn_left | 10 | 1 |
| turn_right | 11 | 1 |
| u_turn | 9 | 0 |
