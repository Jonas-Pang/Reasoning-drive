# Lane run 20261117_193557_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 30/121 (25%); without the lines across the lane: 30/121 (25%)
- Lane actions (every action the label decides, contested cells excluded): 63/116 (54%)
- Left boundary: 56/121 (46%); right boundary: 57/118 (48%); both: 32/121 (26%)
- Markings in the lane, exact set: 98/118 (83%) (without the lines across the lane 106/118 (90%)); added (not in the label): 9, of them lines across the lane 2, by the evidence the answer gave {'full': 9}; missed: 18
- Lane count: 58/118 (49%); position of my lane: 78/119 (66%)
- Unsafe errors (label prohibited, answer allowed): 38 {'change_right': 18, 'change_left': 17, 'go_straight': 3}; over-cautious: 26; contested unsafe: 12
- Prohibited actions also prohibited by the answer: 123/174 (71%)
- Actions decided where the label has no governing marking: 11
- Answers that contradict themselves: 10 {'u_turn decided without an arrow or prohibited-movement marking': 5, 'leftmost lane, but a lane line on the left': 3, 'rightmost lane, but a lane line on the right': 2, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 17, 'accepted': 98, 'unlisted': 9}; IDs written with brackets (read without them): 134
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 18
- Tokens: {'input_tokens': 896548, 'cached_input_tokens': 0, 'output_tokens': 94696}; cost about $0.0; latency: {'mean': 27.58, 'max': 46.97}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 78 |
| change_right | 108 | 78 |
| go_straight | 25 | 22 |
| turn_left | 25 | 20 |
| turn_right | 25 | 19 |
| u_turn | 25 | 20 |
