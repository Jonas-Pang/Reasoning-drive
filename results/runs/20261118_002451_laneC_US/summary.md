# Lane run 20261118_002451_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 108 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 14/104 (13%); without the lines across the lane: 35/104 (34%)
- Lane actions (every action the label decides, contested cells excluded): 55/101 (54%)
- Left boundary: 54/103 (52%); right boundary: 60/102 (59%); both: 37/103 (36%)
- Markings in the lane, exact set: 27/101 (27%) (without the lines across the lane 79/101 (78%)); added (not in the label): 72, of them lines across the lane 50, by the evidence the answer gave {'partial': 15, 'full': 43, 'insufficient': 14}; missed: 20
- Lane count: 40/101 (40%); position of my lane: 48/103 (47%)
- Unsafe errors (label prohibited, answer allowed): 27 {'change_right': 3, 'change_left': 20, 'go_straight': 1, 'turn_left': 1, 'turn_right': 2}; over-cautious: 24; contested unsafe: 25
- Prohibited actions also prohibited by the answer: 35/68 (51%)
- Actions decided where the label has no governing marking: 41
- Answers that contradict themselves: 26 {'change_left prohibited across a broken lane line': 9, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 6, 'leftmost lane, but a lane line on the left': 6, 'change_right prohibited across a broken lane line': 2, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'turn_right prohibited': 1, 'ONLY': 1, 'go_straight prohibited': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 103, 'unlisted': 5}; IDs written with brackets (read without them): 305
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 897372, 'cached_input_tokens': 0, 'output_tokens': 110297}; cost about $0.0; latency: {'mean': 7.15, 'max': 10.53}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 60 |
| change_right | 51 | 37 |
| go_straight | 9 | 8 |
| turn_left | 9 | 6 |
| turn_right | 9 | 5 |
| u_turn | 9 | 6 |
