# Lane run 20261117_041359_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 7/121 (6%); without the lines across the lane: 15/121 (12%)
- Lane actions (every action the label decides, contested cells excluded): 28/118 (24%)
- Left boundary: 59/121 (49%); right boundary: 39/118 (33%); both: 25/121 (21%)
- Markings in the lane, exact set: 14/118 (12%) (without the lines across the lane 45/118 (38%)); added (not in the label): 228, of them lines across the lane 82, by the evidence the answer gave {'insufficient': 128, 'full': 100}; missed: 19
- Lane count: 55/118 (47%); position of my lane: 59/119 (50%)
- Unsafe errors (label prohibited, answer allowed): 10 {'change_left': 5, 'go_straight': 3, 'turn_left': 1, 'change_right': 1}; over-cautious: 76; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 77/142 (54%)
- Actions decided where the label has no governing marking: 17
- Answers that contradict themselves: 30 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 21, 'go_straight decided from an arrow that cannot be read': 11, 'turn_left not_applicable': 3, 'turn_right not_applicable': 3, 'leftmost lane, but a lane line on the left': 2, 'change_left allowed across a curb': 2, 'u_turn not_applicable': 1}
- Citations (Test B and C): {'unlisted': 43, 'in_pack_not_accepted': 30, 'accepted': 50, 'none': 1}; IDs written with brackets (read without them): 288
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 47
- Tokens: {'input_tokens': 584815, 'cached_input_tokens': 0, 'output_tokens': 57895}; cost about $0.0; latency: {'mean': 7.11, 'max': 10.89}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 58 |
| change_right | 108 | 46 |
| go_straight | 25 | 21 |
| turn_left | 22 | 2 |
| turn_right | 21 | 1 |
| u_turn | 21 | 1 |
