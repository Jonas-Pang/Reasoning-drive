# Lane run 20261117_041814_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 4/121 (3%); without the lines across the lane: 11/121 (9%)
- Lane actions (every action the label decides, contested cells excluded): 20/118 (17%)
- Left boundary: 50/121 (41%); right boundary: 30/118 (25%); both: 19/121 (16%)
- Markings in the lane, exact set: 14/118 (12%) (without the lines across the lane 52/118 (44%)); added (not in the label): 183, of them lines across the lane 53, by the evidence the answer gave {'full': 162, 'insufficient': 21}; missed: 20
- Lane count: 54/118 (46%); position of my lane: 56/119 (47%)
- Unsafe errors (label prohibited, answer allowed): 5 {'go_straight': 2, 'change_left': 1, 'change_right': 1, 'turn_left': 1}; over-cautious: 93; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 83/142 (58%)
- Actions decided where the label has no governing marking: 9
- Answers that contradict themselves: 16 {'turn_left not_applicable': 8, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 5, 'turn_right not_applicable': 3, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'leftmost lane, but a lane line on the left': 1, 'go_straight decided from an arrow that cannot be read': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 118, 'unlisted': 6}; IDs written with brackets (read without them): 22
- Boundary evidence: {'same': 142, 'unsupported_guess': 106}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1069872, 'cached_input_tokens': 0, 'output_tokens': 98194}; cost about $0.0; latency: {'mean': 7.45, 'max': 15.42}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 50 |
| change_right | 108 | 42 |
| go_straight | 25 | 23 |
| turn_left | 22 | 2 |
| turn_right | 21 | 1 |
| u_turn | 21 | 1 |
