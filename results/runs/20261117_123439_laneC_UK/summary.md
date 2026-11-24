# Lane run 20261117_123439_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 37 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 5/37 (14%); without the lines across the lane: 6/37 (16%)
- Lane actions (every action the label decides, contested cells excluded): 9/29 (31%)
- Left boundary: 14/37 (38%); right boundary: 13/37 (35%); both: 7/37 (19%)
- Markings in the lane, exact set: 22/37 (59%) (without the lines across the lane 28/37 (76%)); added (not in the label): 8, of them lines across the lane 4, by the evidence the answer gave {'full': 8}; missed: 15
- Lane count: 12/19 (63%); position of my lane: 16/19 (84%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 1, 'go_straight': 1}; over-cautious: 18; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 7/21 (33%)
- Actions decided where the label has no governing marking: 11
- Answers that contradict themselves: 15 {'u_turn decided without an arrow or prohibited-movement marking': 9, 'rightmost lane, but a lane line on the right': 4, 'leftmost lane, but a lane line on the left': 1, 'change_right decided': 1, 'turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'unlisted': 37}; IDs written with brackets (read without them): 66
- Boundary evidence: {'same': 74}
- Readable answers: 37/37 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 214711, 'cached_input_tokens': 0, 'output_tokens': 25183}; cost about $0.0; latency: {'mean': 12.29, 'max': 23.25}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 8 |
| change_right | 26 | 12 |
| go_straight | 8 | 7 |
| turn_left | 8 | 3 |
| turn_right | 8 | 2 |
| u_turn | 7 | 2 |
