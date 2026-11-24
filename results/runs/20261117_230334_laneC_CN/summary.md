# Lane run 20261117_230334_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 8/121 (7%); without the lines across the lane: 14/121 (12%)
- Lane actions (every action the label decides, contested cells excluded): 52/116 (45%)
- Left boundary: 58/121 (48%); right boundary: 35/118 (30%); both: 26/121 (21%)
- Markings in the lane, exact set: 17/118 (14%) (without the lines across the lane 43/118 (36%)); added (not in the label): 201, of them lines across the lane 42, by the evidence the answer gave {'full': 181, 'insufficient': 17, 'partial': 3}; missed: 18
- Lane count: 60/118 (51%); position of my lane: 62/119 (52%)
- Unsafe errors (label prohibited, answer allowed): 9 {'go_straight': 2, 'turn_left': 3, 'change_left': 2, 'change_right': 2}; over-cautious: 78; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 155/174 (89%)
- Actions decided where the label has no governing marking: 72
- Answers that contradict themselves: 32 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 12, 'go_straight allowed': 10, 'turn_right not_applicable': 8, 'turn_left not_applicable': 7, 'turn_left prohibited': 3, 'turn_right prohibited': 3, 'rightmost lane, but a lane line on the right': 2, 'leftmost lane, but a lane line on the left': 2}
- Citations (Test B and C): {'unlisted': 7, 'in_pack_not_accepted': 117}; IDs written with brackets (read without them): 65
- Boundary evidence: {'same': 142, 'unsupported_guess': 106}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1176884, 'cached_input_tokens': 0, 'output_tokens': 103867}; cost about $0.0; latency: {'mean': 8.46, 'max': 14.64}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 78 |
| change_right | 108 | 61 |
| go_straight | 25 | 23 |
| turn_left | 25 | 18 |
| turn_right | 25 | 18 |
| u_turn | 25 | 20 |
