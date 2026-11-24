# Lane run 20261117_224254_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 5/121 (4%); without the lines across the lane: 11/121 (9%)
- Lane actions (every action the label decides, contested cells excluded): 52/116 (45%)
- Left boundary: 63/121 (52%); right boundary: 47/118 (40%); both: 32/121 (26%)
- Markings in the lane, exact set: 8/118 (7%) (without the lines across the lane 37/118 (31%)); added (not in the label): 125, of them lines across the lane 28, by the evidence the answer gave {'full': 84, 'insufficient': 38, 'partial': 3}; missed: 32
- Lane count: 61/118 (52%); position of my lane: 67/119 (56%)
- Unsafe errors (label prohibited, answer allowed): 29 {'u_turn': 10, 'turn_right': 2, 'go_straight': 3, 'change_left': 8, 'change_right': 4, 'turn_left': 2}; over-cautious: 56; contested unsafe: 4
- Prohibited actions also prohibited by the answer: 140/174 (80%)
- Actions decided where the label has no governing marking: 99
- Answers that contradict themselves: 20 {'turn_left prohibited': 5, 'turn_left allowed': 4, 'change_left allowed across a curb': 4, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'leftmost lane, but a lane line on the left': 2, 'rightmost lane, but a lane line on the right': 1, 'go_straight allowed': 1, 'turn_right prohibited': 1}
- Citations (Test B and C): {'unlisted': 31, 'accepted': 67, 'in_pack_not_accepted': 26}; IDs written with brackets (read without them): 275
- Boundary evidence: {'same': 142, 'unsupported_guess': 106}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1048792, 'cached_input_tokens': 0, 'output_tokens': 111997}; cost about $0.0; latency: {'mean': 9.52, 'max': 30.41}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 82 |
| change_right | 108 | 67 |
| go_straight | 25 | 22 |
| turn_left | 25 | 22 |
| turn_right | 25 | 21 |
| u_turn | 25 | 12 |
