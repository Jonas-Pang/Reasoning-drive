# Lane run 20261117_025521_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 33/121 (27%); without the lines across the lane: 33/121 (27%)
- Lane actions (every action the label decides, contested cells excluded): 58/118 (49%)
- Left boundary: 53/121 (44%); right boundary: 72/118 (61%); both: 38/121 (31%)
- Markings in the lane, exact set: 96/118 (81%) (without the lines across the lane 104/118 (88%)); added (not in the label): 3, of them lines across the lane 1, by the evidence the answer gave {'full': 3}; missed: 25
- Lane count: 63/118 (53%); position of my lane: 80/119 (67%)
- Unsafe errors (label prohibited, answer allowed): 43 {'change_left': 20, 'change_right': 20, 'go_straight': 3}; over-cautious: 16; contested unsafe: 17
- Prohibited actions also prohibited by the answer: 86/142 (61%)
- Actions decided where the label has no governing marking: 11
- Answers that contradict themselves: 6 {'u_turn decided without an arrow or prohibited-movement marking': 3, 'change_left decided': 1, 'turn_left, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 22, 'accepted': 100, 'unlisted': 2}; IDs written with brackets (read without them): 164
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 941780, 'cached_input_tokens': 0, 'output_tokens': 90505}; cost about $0.0; latency: {'mean': 18.22, 'max': 49.34}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 66 |
| change_right | 108 | 69 |
| go_straight | 25 | 22 |
| turn_left | 22 | 16 |
| turn_right | 21 | 14 |
| u_turn | 21 | 15 |
