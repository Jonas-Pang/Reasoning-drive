# Lane run 20261117_170339_laneB_UK

Test B (image + the region's rule passages), region UK, 48 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 11/48 (23%); without the lines across the lane: 12/48 (25%)
- Lane actions (every action the label decides, contested cells excluded): 22/40 (55%)
- Left boundary: 27/48 (56%); right boundary: 23/47 (49%); both: 16/48 (33%)
- Markings in the lane, exact set: 29/48 (60%) (without the lines across the lane 34/48 (71%)); added (not in the label): 14, of them lines across the lane 1, by the evidence the answer gave {'full': 13, 'insufficient': 1}; missed: 11
- Lane count: 21/28 (75%); position of my lane: 22/28 (79%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 14; contested unsafe: 10
- Prohibited actions also prohibited by the answer: 20/21 (95%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 15 {'rightmost lane, but a lane line on the right': 7, 'change_right decided': 4, 'leftmost lane, but a lane line on the left': 2, 'change_left decided': 1, 'go_straight allowed': 1, 'turn_right prohibited': 1}
- Citations (Test B and C): {'accepted': 30, 'unlisted': 7, 'in_pack_not_accepted': 11}; IDs written with brackets (read without them): 76
- Boundary evidence: {'same': 92, 'unsupported_guess': 4}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 25
- Tokens: {'input_tokens': 335271, 'cached_input_tokens': 0, 'output_tokens': 20476}; cost about $0.0; latency: {'mean': 32.59, 'max': 50.14}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 9 |
| change_right | 37 | 24 |
| go_straight | 8 | 7 |
| turn_left | 8 | 7 |
| turn_right | 8 | 8 |
| u_turn | 7 | 6 |
