# Lane run 20261114_010242_laneR_CN

Test R (image + the passages about the elements of the model's own Test A answer), region CN, 68 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 37/68 (54%); without the lines across the lane: 40/68 (59%)
- Lane actions (every action the label decides, contested cells excluded): 59/68 (87%)
- Left boundary: 54/68 (79%); right boundary: 54/68 (79%); both: 44/68 (65%)
- Markings in the lane, exact set: 54/67 (81%) (without the lines across the lane 61/67 (91%)); added (not in the label): 18, of them lines across the lane 14, by the evidence the answer gave {'partial': 8, 'insufficient': 1, 'full': 9}; missed: 4
- Lane count: 41/68 (60%); position of my lane: 49/64 (77%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_right': 1}; over-cautious: 8; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 112/128 (88%)
- Actions decided where the label has no governing marking: 8
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 120, 'over_withholding': 16}
- Readable answers: 68/68 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 468801, 'cached_input_tokens': 264437, 'output_tokens': 68724}; cost about $1.1224; latency: {'mean': 16.91, 'max': 33.31}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 68 | 65 |
| change_right | 68 | 65 |
| go_straight | 18 | 15 |
| turn_left | 18 | 13 |
| turn_right | 18 | 13 |
| u_turn | 18 | 13 |
