# Lane run 20261117_025517_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 33/121 (27%); without the lines across the lane: 33/121 (27%)
- Lane actions (every action the label decides, contested cells excluded): 58/118 (49%)
- Left boundary: 53/121 (44%); right boundary: 74/118 (63%); both: 38/121 (31%)
- Markings in the lane, exact set: 97/118 (82%) (without the lines across the lane 104/118 (88%)); added (not in the label): 3, of them lines across the lane 1, by the evidence the answer gave {'full': 3}; missed: 22
- Lane count: 64/118 (54%); position of my lane: 78/119 (66%)
- Unsafe errors (label prohibited, answer allowed): 44 {'change_left': 21, 'change_right': 20, 'go_straight': 3}; over-cautious: 14; contested unsafe: 17
- Prohibited actions also prohibited by the answer: 85/142 (60%)
- Actions decided where the label has no governing marking: 17
- Answers that contradict themselves: 11 {'u_turn decided without an arrow or prohibited-movement marking': 9, 'change_left decided': 1, 'turn_left, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 24, 'accepted': 98, 'unlisted': 2}; IDs written with brackets (read without them): 168
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 941780, 'cached_input_tokens': 0, 'output_tokens': 90943}; cost about $0.0; latency: {'mean': 18.19, 'max': 52.34}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 66 |
| change_right | 108 | 69 |
| go_straight | 25 | 22 |
| turn_left | 22 | 16 |
| turn_right | 21 | 14 |
| u_turn | 21 | 15 |
