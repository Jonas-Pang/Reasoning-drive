# Lane run 20261117_123051_laneB_UK

Test B (image + the region's rule passages), region UK, 37 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 7/37 (19%); without the lines across the lane: 8/37 (22%)
- Lane actions (every action the label decides, contested cells excluded): 13/29 (45%)
- Left boundary: 18/37 (49%); right boundary: 16/37 (43%); both: 10/37 (27%)
- Markings in the lane, exact set: 22/37 (59%) (without the lines across the lane 26/37 (70%)); added (not in the label): 8, of them lines across the lane 1, by the evidence the answer gave {'full': 8}; missed: 15
- Lane count: 14/19 (74%); position of my lane: 15/19 (79%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 1, 'go_straight': 1}; over-cautious: 16; contested unsafe: 7
- Prohibited actions also prohibited by the answer: 19/21 (90%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 2 {'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {'accepted': 24, 'in_pack_not_accepted': 7, 'unlisted': 6}; IDs written with brackets (read without them): 72
- Boundary evidence: {'same': 74}
- Readable answers: 37/37 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 513967, 'cached_input_tokens': 0, 'output_tokens': 31641}; cost about $0.0; latency: {'mean': 14.9, 'max': 34.82}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 7 |
| change_right | 26 | 16 |
| go_straight | 8 | 7 |
| turn_left | 8 | 5 |
| turn_right | 8 | 7 |
| u_turn | 7 | 7 |
