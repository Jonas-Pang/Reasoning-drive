# Lane run 20261118_001346_laneB_UK

Test B (image + the region's rule passages), region UK, 48 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/48 (0%); without the lines across the lane: 2/48 (4%)
- Lane actions (every action the label decides, contested cells excluded): 23/39 (59%)
- Left boundary: 15/48 (31%); right boundary: 26/47 (55%); both: 9/48 (19%)
- Markings in the lane, exact set: 6/48 (12%) (without the lines across the lane 25/48 (52%)); added (not in the label): 46, of them lines across the lane 20, by the evidence the answer gave {'full': 35, 'partial': 8, 'insufficient': 3}; missed: 17
- Lane count: 8/28 (29%); position of my lane: 21/28 (75%)
- Unsafe errors (label prohibited, answer allowed): 9 {'change_right': 1, 'turn_left': 2, 'turn_right': 4, 'u_turn': 1, 'go_straight': 1}; over-cautious: 15; contested unsafe: 26
- Prohibited actions also prohibited by the answer: 11/21 (52%)
- Actions decided where the label has no governing marking: 16
- Answers that contradict themselves: 32 {'leftmost lane, but a lane line on the left': 24, 'change_left prohibited across a broken lane line': 11, 'change_right prohibited across a broken lane line': 3, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'turn_left allowed': 1, 'turn_right allowed': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 19, 'accepted': 26, 'unlisted': 3}; IDs written with brackets (read without them): 147
- Boundary evidence: {'same': 91, 'unsupported_guess': 4, 'over_withholding': 1}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 708000, 'cached_input_tokens': 0, 'output_tokens': 48487}; cost about $0.0; latency: {'mean': 8.46, 'max': 13.16}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 5 |
| change_right | 36 | 30 |
| go_straight | 8 | 6 |
| turn_left | 8 | 4 |
| turn_right | 8 | 4 |
| u_turn | 8 | 5 |
