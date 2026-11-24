# Lane run 20261117_222453_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 5/121 (4%); without the lines across the lane: 10/121 (8%)
- Lane actions (every action the label decides, contested cells excluded): 58/116 (50%)
- Left boundary: 73/121 (60%); right boundary: 39/118 (33%); both: 27/121 (22%)
- Markings in the lane, exact set: 14/118 (12%) (without the lines across the lane 44/118 (37%)); added (not in the label): 115, of them lines across the lane 24, by the evidence the answer gave {'insufficient': 29, 'partial': 4, 'full': 82}; missed: 16
- Lane count: 64/118 (54%); position of my lane: 59/119 (50%)
- Unsafe errors (label prohibited, answer allowed): 23 {'change_left': 12, 'change_right': 6, 'go_straight': 2, 'turn_left': 3}; over-cautious: 53; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 148/174 (85%)
- Actions decided where the label has no governing marking: 129
- Answers that contradict themselves: 19 {'turn_left prohibited': 9, 'turn_right prohibited': 5, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 3, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'leftmost lane, but a lane line on the left': 2, 'rightmost lane, but a lane line on the right': 1, 'go_straight allowed': 1, 'turn_left not_applicable': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 142, 'unsupported_guess': 106}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 470828, 'cached_input_tokens': 0, 'output_tokens': 106508}; cost about $0.0; latency: {'mean': 7.95, 'max': 23.51}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 89 |
| change_right | 108 | 63 |
| go_straight | 25 | 22 |
| turn_left | 25 | 20 |
| turn_right | 25 | 21 |
| u_turn | 25 | 22 |
