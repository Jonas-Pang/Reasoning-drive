# Lane run 20261117_211411_laneB_UK

Test B (image + the region's rule passages), region UK, 48 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 9/48 (19%); without the lines across the lane: 10/48 (21%)
- Lane actions (every action the label decides, contested cells excluded): 21/39 (54%)
- Left boundary: 29/48 (60%); right boundary: 22/47 (47%); both: 16/48 (33%)
- Markings in the lane, exact set: 30/48 (62%) (without the lines across the lane 34/48 (71%)); added (not in the label): 13, of them lines across the lane 0, by the evidence the answer gave {'full': 13}; missed: 11
- Lane count: 21/28 (75%); position of my lane: 22/28 (79%)
- Unsafe errors (label prohibited, answer allowed): 3 {'u_turn': 2, 'change_right': 1}; over-cautious: 17; contested unsafe: 8
- Prohibited actions also prohibited by the answer: 18/21 (86%)
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 13 {'rightmost lane, but a lane line on the right': 7, 'change_right decided': 3, 'leftmost lane, but a lane line on the left': 2, 'go_straight allowed': 1, 'turn_right prohibited': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 28, 'unlisted': 9, 'in_pack_not_accepted': 11}; IDs written with brackets (read without them): 86
- Boundary evidence: {'same': 91, 'unsupported_guess': 4, 'over_withholding': 1}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 3
- Tokens: {'input_tokens': 663930, 'cached_input_tokens': 0, 'output_tokens': 40916}; cost about $0.0; latency: {'mean': 34.01, 'max': 54.75}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 9 |
| change_right | 36 | 23 |
| go_straight | 8 | 7 |
| turn_left | 8 | 7 |
| turn_right | 8 | 8 |
| u_turn | 8 | 5 |
