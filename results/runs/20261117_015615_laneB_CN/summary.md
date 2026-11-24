# Lane run 20261117_015615_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 1/25 (4%); without the lines across the lane: 2/25 (8%)
- Lane actions (every action the label decides, contested cells excluded): 7/21 (33%)
- Left boundary: 12/25 (48%); right boundary: 7/25 (28%); both: 6/25 (24%)
- Markings in the lane, exact set: 1/25 (4%) (without the lines across the lane 4/25 (16%)); added (not in the label): 88, of them lines across the lane 28, by the evidence the answer gave {'insufficient': 62, 'full': 26}; missed: 8
- Lane count: 12/22 (55%); position of my lane: 8/22 (36%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 3, 'turn_left': 1}; over-cautious: 11; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 15/27 (56%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 8 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 8, 'go_straight decided from an arrow that cannot be read': 7, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 9, 'unlisted': 6, 'accepted': 10}; IDs written with brackets (read without them): 64
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 189875, 'cached_input_tokens': 0, 'output_tokens': 19385}; cost about $0.0; latency: {'mean': 21.59, 'max': 59.78}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 16 |
| change_right | 21 | 10 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
