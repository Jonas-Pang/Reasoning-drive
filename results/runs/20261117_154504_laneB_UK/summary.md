# Lane run 20261117_154504_laneB_UK

Test B (image + the region's rule passages), region UK, 37 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/37 (3%); without the lines across the lane: 3/37 (8%)
- Lane actions (every action the label decides, contested cells excluded): 13/29 (45%)
- Left boundary: 12/37 (32%); right boundary: 18/37 (49%); both: 7/37 (19%)
- Markings in the lane, exact set: 2/37 (5%) (without the lines across the lane 15/37 (41%)); added (not in the label): 32, of them lines across the lane 14, by the evidence the answer gave {'insufficient': 4, 'full': 18, 'partial': 10}; missed: 14
- Lane count: 7/19 (37%); position of my lane: 12/19 (63%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 1, 'go_straight': 1}; over-cautious: 12; contested unsafe: 22
- Prohibited actions also prohibited by the answer: 0/21 (0%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 26 {'leftmost lane, but a lane line on the left': 21, 'change_left allowed across a curb': 4, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 4, 'change_right prohibited across a broken lane line': 2, 'change_left prohibited across a broken lane line': 1, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {'unlisted': 5, 'accepted': 22, 'in_pack_not_accepted': 10}; IDs written with brackets (read without them): 114
- Boundary evidence: {'same': 74}
- Readable answers: 37/37 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 34
- Tokens: {'input_tokens': 41661, 'cached_input_tokens': 0, 'output_tokens': 3389}; cost about $0.0; latency: {'mean': 26.56, 'max': 26.85}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 5 |
| change_right | 26 | 18 |
| go_straight | 8 | 7 |
| turn_left | 8 | 0 |
| turn_right | 8 | 1 |
| u_turn | 7 | 0 |
