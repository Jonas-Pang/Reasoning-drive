# Lane run 20261118_003058_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 48 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/48 (2%); without the lines across the lane: 4/48 (8%)
- Lane actions (every action the label decides, contested cells excluded): 28/39 (72%)
- Left boundary: 13/48 (27%); right boundary: 29/47 (62%); both: 8/48 (17%)
- Markings in the lane, exact set: 13/48 (27%) (without the lines across the lane 26/48 (54%)); added (not in the label): 39, of them lines across the lane 15, by the evidence the answer gave {'partial': 8, 'full': 25, 'insufficient': 6}; missed: 14
- Lane count: 7/28 (25%); position of my lane: 19/28 (68%)
- Unsafe errors (label prohibited, answer allowed): 8 {'change_right': 1, 'turn_right': 4, 'turn_left': 1, 'u_turn': 1, 'go_straight': 1}; over-cautious: 9; contested unsafe: 37
- Prohibited actions also prohibited by the answer: 11/21 (52%)
- Actions decided where the label has no governing marking: 25
- Answers that contradict themselves: 32 {'leftmost lane, but a lane line on the left': 28, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 7, 'change_left prohibited across a broken lane line': 7, 'turn_right allowed': 1, 'change_left allowed': 1}
- Citations (Test B and C): {'unlisted': 48}; IDs written with brackets (read without them): 135
- Boundary evidence: {'same': 92, 'unsupported_guess': 4}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 319776, 'cached_input_tokens': 0, 'output_tokens': 45088}; cost about $0.0; latency: {'mean': 7.2, 'max': 10.35}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 8 |
| change_right | 36 | 32 |
| go_straight | 8 | 7 |
| turn_left | 8 | 4 |
| turn_right | 8 | 4 |
| u_turn | 8 | 4 |
