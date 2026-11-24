# Lane run 20261117_040817_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 38 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 2/38 (5%); without the lines across the lane: 7/38 (18%)
- Lane actions (every action the label decides, contested cells excluded): 18/37 (49%)
- Left boundary: 27/37 (73%); right boundary: 19/37 (51%); both: 15/38 (39%)
- Markings in the lane, exact set: 2/37 (5%) (without the lines across the lane 15/37 (41%)); added (not in the label): 106, of them lines across the lane 36, by the evidence the answer gave {'insufficient': 62, 'full': 44}; missed: 12
- Lane count: 8/38 (21%); position of my lane: 16/38 (42%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 1, 'go_straight': 1, 'turn_left': 2}; over-cautious: 9; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 25/42 (60%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 12 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 7, 'turn_left not_applicable': 3, 'go_straight decided from an arrow that cannot be read': 3, 'go_straight allowed': 2, 'turn_left allowed': 1, 'change_left allowed across a curb': 1, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 32, 'unlisted': 6}; IDs written with brackets (read without them): 64
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 38
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 30 |
| change_right | 21 | 13 |
| go_straight | 8 | 7 |
| turn_left | 8 | 1 |
| turn_right | 8 | 0 |
| u_turn | 7 | 0 |
