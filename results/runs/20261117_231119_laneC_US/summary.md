# Lane run 20261117_231119_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 108 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 6/104 (6%); without the lines across the lane: 15/104 (14%)
- Lane actions (every action the label decides, contested cells excluded): 62/101 (61%)
- Left boundary: 72/103 (70%); right boundary: 49/102 (48%); both: 33/103 (32%)
- Markings in the lane, exact set: 10/101 (10%) (without the lines across the lane 35/101 (35%)); added (not in the label): 154, of them lines across the lane 48, by the evidence the answer gave {'full': 82, 'insufficient': 67, 'partial': 5}; missed: 17
- Lane count: 50/101 (50%); position of my lane: 47/103 (46%)
- Unsafe errors (label prohibited, answer allowed): 5 {'turn_left': 2, 'change_left': 1, 'turn_right': 2}; over-cautious: 40; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 59/68 (87%)
- Actions decided where the label has no governing marking: 38
- Answers that contradict themselves: 24 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 5, 'go_straight allowed': 4, 'turn_left not_applicable': 4, 'go_straight decided from an arrow that cannot be read': 4, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'turn_right prohibited': 3, 'turn_left prohibited': 2, 'leftmost lane, but a lane line on the left': 2}
- Citations (Test B and C): {'unlisted': 28, 'in_pack_not_accepted': 80}; IDs written with brackets (read without them): 241
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 897804, 'cached_input_tokens': 0, 'output_tokens': 91799}; cost about $0.0; latency: {'mean': 8.15, 'max': 14.12}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 82 |
| change_right | 51 | 25 |
| go_straight | 9 | 6 |
| turn_left | 9 | 6 |
| turn_right | 9 | 4 |
| u_turn | 9 | 7 |
