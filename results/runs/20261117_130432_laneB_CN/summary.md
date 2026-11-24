# Lane run 20261117_130432_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 31/121 (26%); without the lines across the lane: 31/121 (26%)
- Lane actions (every action the label decides, contested cells excluded): 58/118 (49%)
- Left boundary: 53/121 (44%); right boundary: 57/118 (48%); both: 33/121 (27%)
- Markings in the lane, exact set: 95/118 (81%) (without the lines across the lane 103/118 (87%)); added (not in the label): 10, of them lines across the lane 2, by the evidence the answer gave {'full': 10}; missed: 17
- Lane count: 57/118 (48%); position of my lane: 78/119 (66%)
- Unsafe errors (label prohibited, answer allowed): 30 {'change_right': 17, 'change_left': 11, 'go_straight': 2}; over-cautious: 22; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 107/142 (75%)
- Actions decided where the label has no governing marking: 20
- Answers that contradict themselves: 12 {'u_turn decided without an arrow or prohibited-movement marking': 5, 'leftmost lane, but a lane line on the left': 4, 'rightmost lane, but a lane line on the right': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'turn_left, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 16, 'accepted': 98, 'unlisted': 7, 'no_answer': 3}; IDs written with brackets (read without them): 110
- Boundary evidence: {'unsupported_guess': 104, 'same': 138, 'other': 6}
- Readable answers: 121/124 (an unreadable or failed answer counts as wrong); errors: 3; from cache: 0
- Tokens: {'input_tokens': 1002001, 'cached_input_tokens': 0, 'output_tokens': 107047}; cost about $0.0; latency: {'mean': 18.63, 'max': 63.77}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 69 |
| change_right | 108 | 65 |
| go_straight | 25 | 23 |
| turn_left | 22 | 20 |
| turn_right | 21 | 19 |
| u_turn | 21 | 19 |
