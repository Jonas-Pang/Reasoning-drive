# Lane run 20261117_015836_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/25 (0%); without the lines across the lane: 4/25 (16%)
- Lane actions (every action the label decides, contested cells excluded): 5/21 (24%)
- Left boundary: 9/25 (36%); right boundary: 12/25 (48%); both: 7/25 (28%)
- Markings in the lane, exact set: 1/25 (4%) (without the lines across the lane 12/25 (48%)); added (not in the label): 23, of them lines across the lane 9, by the evidence the answer gave {'insufficient': 8, 'full': 7, 'partial': 8}; missed: 8
- Lane count: 12/22 (55%); position of my lane: 8/22 (36%)
- Unsafe errors (label prohibited, answer allowed): 10 {'change_left': 6, 'change_right': 4}; over-cautious: 10; contested unsafe: 3
- Prohibited actions also prohibited by the answer: 8/27 (30%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 3 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'turn_right not_applicable': 1}
- Citations (Test B and C): {'unlisted': 8, 'in_pack_not_accepted': 7, 'accepted': 10}; IDs written with brackets (read without them): 67
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 189775, 'cached_input_tokens': 0, 'output_tokens': 26703}; cost about $0.0; latency: {'mean': 22.82, 'max': 36.23}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 11 |
| change_right | 21 | 9 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
