# Lane run 20261117_145317_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 32/121 (26%); without the lines across the lane: 32/121 (26%)
- Lane actions (every action the label decides, contested cells excluded): 56/118 (47%)
- Left boundary: 59/121 (49%); right boundary: 56/118 (47%); both: 35/121 (29%)
- Markings in the lane, exact set: 92/118 (78%) (without the lines across the lane 101/118 (86%)); added (not in the label): 15, of them lines across the lane 3, by the evidence the answer gave {'full': 15}; missed: 21
- Lane count: 60/118 (51%); position of my lane: 77/119 (65%)
- Unsafe errors (label prohibited, answer allowed): 36 {'change_right': 21, 'change_left': 13, 'go_straight': 2}; over-cautious: 20; contested unsafe: 11
- Prohibited actions also prohibited by the answer: 91/142 (64%)
- Actions decided where the label has no governing marking: 13
- Answers that contradict themselves: 13 {'leftmost lane, but a lane line on the left': 4, 'rightmost lane, but a lane line on the right': 3, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'go_straight decided without an arrow or prohibited-movement marking': 2, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 109, 'unlisted': 15}; IDs written with brackets (read without them): 229
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 111
- Tokens: {'input_tokens': 121082, 'cached_input_tokens': 0, 'output_tokens': 12121}; cost about $0.0; latency: {'mean': 21.77, 'max': 46.72}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 70 |
| change_right | 108 | 64 |
| go_straight | 25 | 22 |
| turn_left | 22 | 16 |
| turn_right | 21 | 16 |
| u_turn | 21 | 15 |
