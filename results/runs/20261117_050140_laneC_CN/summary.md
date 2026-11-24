# Lane run 20261117_050140_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/121 (0%); without the lines across the lane: 12/121 (10%)
- Lane actions (every action the label decides, contested cells excluded): 34/118 (29%)
- Left boundary: 43/121 (36%); right boundary: 37/118 (31%); both: 22/121 (18%)
- Markings in the lane, exact set: 8/118 (7%) (without the lines across the lane 63/118 (53%)); added (not in the label): 108, of them lines across the lane 60, by the evidence the answer gave {'insufficient': 36, 'full': 39, 'partial': 33}; missed: 29
- Lane count: 59/118 (50%); position of my lane: 57/119 (48%)
- Unsafe errors (label prohibited, answer allowed): 52 {'change_left': 25, 'change_right': 23, 'go_straight': 3, 'turn_right': 1}; over-cautious: 44; contested unsafe: 13
- Prohibited actions also prohibited by the answer: 34/142 (24%)
- Actions decided where the label has no governing marking: 20
- Answers that contradict themselves: 41 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 14, 'leftmost lane, but a lane line on the left': 12, 'change_left allowed across a curb': 6, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'change_left prohibited across a broken lane line': 2, 'change_right allowed across a curb': 2, 'go_straight, turn_right decided without an arrow or prohibited-movement marking': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 90, 'unlisted': 34}; IDs written with brackets (read without them): 340
- Boundary evidence: {'unsupported_guess': 103, 'same': 141, 'over_withholding': 4}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1069376, 'cached_input_tokens': 0, 'output_tokens': 134402}; cost about $0.0; latency: {'mean': 7.19, 'max': 10.66}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 45 |
| change_right | 108 | 49 |
| go_straight | 25 | 21 |
| turn_left | 22 | 1 |
| turn_right | 21 | 1 |
| u_turn | 21 | 1 |
