# Lane run 20261117_225928_laneB_UK

Test B (image + the region's rule passages), region UK, 48 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/48 (0%); without the lines across the lane: 3/48 (6%)
- Lane actions (every action the label decides, contested cells excluded): 18/39 (46%)
- Left boundary: 17/48 (35%); right boundary: 18/47 (38%); both: 8/48 (17%)
- Markings in the lane, exact set: 1/48 (2%) (without the lines across the lane 11/48 (23%)); added (not in the label): 58, of them lines across the lane 11, by the evidence the answer gave {'full': 49, 'partial': 3, 'insufficient': 6}; missed: 12
- Lane count: 5/28 (18%); position of my lane: 12/28 (43%)
- Unsafe errors (label prohibited, answer allowed): 1 {'go_straight': 1}; over-cautious: 27; contested unsafe: 13
- Prohibited actions also prohibited by the answer: 18/21 (86%)
- Actions decided where the label has no governing marking: 22
- Answers that contradict themselves: 14 {'turn_left prohibited': 4, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 4, 'change_left allowed': 3, 'change_left prohibited across a broken lane line': 2, 'turn_right prohibited': 2, 'change_left prohibited': 1, 'change_right prohibited': 1, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 15, 'unlisted': 3, 'accepted': 30}; IDs written with brackets (read without them): 7
- Boundary evidence: {'same': 92, 'unsupported_guess': 4}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 708192, 'cached_input_tokens': 0, 'output_tokens': 42881}; cost about $0.0; latency: {'mean': 9.71, 'max': 17.86}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 7 |
| change_right | 36 | 18 |
| go_straight | 8 | 6 |
| turn_left | 8 | 6 |
| turn_right | 8 | 6 |
| u_turn | 8 | 6 |
