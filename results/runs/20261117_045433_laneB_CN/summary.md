# Lane run 20261117_045433_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/121 (1%); without the lines across the lane: 8/121 (7%)
- Lane actions (every action the label decides, contested cells excluded): 28/118 (24%)
- Left boundary: 40/121 (33%); right boundary: 36/118 (31%); both: 13/121 (11%)
- Markings in the lane, exact set: 6/118 (5%) (without the lines across the lane 49/118 (42%)); added (not in the label): 110, of them lines across the lane 47, by the evidence the answer gave {'full': 43, 'insufficient': 45, 'partial': 22}; missed: 32
- Lane count: 54/118 (46%); position of my lane: 58/119 (49%)
- Unsafe errors (label prohibited, answer allowed): 59 {'change_right': 28, 'change_left': 25, 'go_straight': 3, 'turn_right': 3}; over-cautious: 35; contested unsafe: 14
- Prohibited actions also prohibited by the answer: 35/142 (25%)
- Actions decided where the label has no governing marking: 19
- Answers that contradict themselves: 24 {'leftmost lane, but a lane line on the left': 8, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 5, 'change_left prohibited across a broken lane line': 5, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'change_left allowed across a curb': 2, 'change_left allowed': 1, 'change_left decided': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 27, 'accepted': 58, 'unlisted': 39}; IDs written with brackets (read without them): 331
- Boundary evidence: {'unsupported_guess': 105, 'same': 133, 'over_withholding': 10}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 941284, 'cached_input_tokens': 0, 'output_tokens': 134283}; cost about $0.0; latency: {'mean': 7.06, 'max': 8.71}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 54 |
| change_right | 108 | 44 |
| go_straight | 25 | 22 |
| turn_left | 22 | 4 |
| turn_right | 21 | 2 |
| u_turn | 21 | 4 |
