# Lane run 20261117_153635_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 48 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 11/48 (23%); without the lines across the lane: 13/48 (27%)
- Lane actions (every action the label decides, contested cells excluded): 17/40 (42%)
- Left boundary: 23/48 (48%); right boundary: 23/47 (49%); both: 14/48 (29%)
- Markings in the lane, exact set: 35/48 (73%) (without the lines across the lane 40/48 (83%)); added (not in the label): 7, of them lines across the lane 1, by the evidence the answer gave {'full': 7}; missed: 12
- Lane count: 19/28 (68%); position of my lane: 22/28 (79%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_right': 1}; over-cautious: 17; contested unsafe: 11
- Prohibited actions also prohibited by the answer: 7/21 (33%)
- Actions decided where the label has no governing marking: 15
- Answers that contradict themselves: 25 {'u_turn decided without an arrow or prohibited-movement marking': 14, 'rightmost lane, but a lane line on the right': 8, 'leftmost lane, but a lane line on the left': 3, 'change_right decided': 3, 'change_left decided': 1, 'go_straight, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight allowed': 1, 'turn_right prohibited': 1}
- Citations (Test B and C): {'unlisted': 47, 'none': 1}; IDs written with brackets (read without them): 81
- Boundary evidence: {'same': 92, 'unsupported_guess': 4}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 311472, 'cached_input_tokens': 0, 'output_tokens': 37021}; cost about $0.0; latency: {'mean': 13.89, 'max': 26.18}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 9 |
| change_right | 37 | 20 |
| go_straight | 8 | 7 |
| turn_left | 8 | 4 |
| turn_right | 8 | 4 |
| u_turn | 7 | 1 |
