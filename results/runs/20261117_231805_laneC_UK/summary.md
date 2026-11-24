# Lane run 20261117_231805_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 48 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/48 (0%); without the lines across the lane: 1/48 (2%)
- Lane actions (every action the label decides, contested cells excluded): 17/39 (44%)
- Left boundary: 15/48 (31%); right boundary: 21/47 (45%); both: 8/48 (17%)
- Markings in the lane, exact set: 3/48 (6%) (without the lines across the lane 8/48 (17%)); added (not in the label): 54, of them lines across the lane 6, by the evidence the answer gave {'full': 50, 'partial': 1, 'insufficient': 3}; missed: 10
- Lane count: 6/28 (21%); position of my lane: 13/28 (46%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 23; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 17/21 (81%)
- Actions decided where the label has no governing marking: 19
- Answers that contradict themselves: 17 {'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 4, 'change_left allowed': 3, 'turn_left prohibited': 3, 'turn_right prohibited': 3, 'leftmost lane, but a lane line on the left': 2, 'rightmost lane, but a lane line on the right': 2, 'turn_left not_applicable': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'unlisted': 46, 'no_answer': 1, 'none': 1}; IDs written with brackets (read without them): 99
- Boundary evidence: {'same': 90, 'unsupported_guess': 4, 'other': 2}
- Readable answers: 47/48 (an unreadable or failed answer counts as wrong); errors: 1; from cache: 0
- Tokens: {'input_tokens': 313302, 'cached_input_tokens': 0, 'output_tokens': 41460}; cost about $0.0; latency: {'mean': 8.66, 'max': 13.55}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 6 |
| change_right | 36 | 19 |
| go_straight | 8 | 8 |
| turn_left | 8 | 7 |
| turn_right | 8 | 7 |
| u_turn | 8 | 4 |
