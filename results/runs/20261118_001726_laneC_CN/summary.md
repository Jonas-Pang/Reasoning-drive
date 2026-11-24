# Lane run 20261118_001726_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 6/121 (5%); without the lines across the lane: 22/121 (18%)
- Lane actions (every action the label decides, contested cells excluded): 43/116 (37%)
- Left boundary: 47/121 (39%); right boundary: 40/118 (34%); both: 26/121 (21%)
- Markings in the lane, exact set: 33/118 (28%) (without the lines across the lane 89/118 (75%)); added (not in the label): 86, of them lines across the lane 59, by the evidence the answer gave {'partial': 26, 'insufficient': 29, 'full': 31}; missed: 24
- Lane count: 53/118 (45%); position of my lane: 57/119 (48%)
- Unsafe errors (label prohibited, answer allowed): 64 {'change_left': 23, 'change_right': 36, 'go_straight': 4, 'turn_right': 1}; over-cautious: 35; contested unsafe: 12
- Prohibited actions also prohibited by the answer: 89/174 (51%)
- Actions decided where the label has no governing marking: 55
- Answers that contradict themselves: 45 {'change_left prohibited across a broken lane line': 16, 'leftmost lane, but a lane line on the left': 10, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 10, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 9, 'change_right prohibited across a broken lane line': 4, 'change_left allowed across a curb': 4, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'change_right allowed across a curb': 2}
- Citations (Test B and C): {'in_pack_not_accepted': 119, 'unlisted': 5}; IDs written with brackets (read without them): 363
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1176388, 'cached_input_tokens': 0, 'output_tokens': 121283}; cost about $0.0; latency: {'mean': 7.76, 'max': 12.08}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 68 |
| change_right | 108 | 60 |
| go_straight | 25 | 19 |
| turn_left | 25 | 17 |
| turn_right | 25 | 16 |
| u_turn | 25 | 16 |
