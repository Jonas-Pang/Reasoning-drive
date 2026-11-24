# Lane run 20261117_015345_laneA_CN

Test A (image only), region CN, 25 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 2/25 (8%); without the lines across the lane: 4/25 (16%)
- Lane actions (every action the label decides, contested cells excluded): 6/21 (29%)
- Left boundary: 10/25 (40%); right boundary: 11/25 (44%); both: 7/25 (28%)
- Markings in the lane, exact set: 5/25 (20%) (without the lines across the lane 12/25 (48%)); added (not in the label): 18, of them lines across the lane 6, by the evidence the answer gave {'full': 13, 'partial': 4, 'insufficient': 1}; missed: 8
- Lane count: 8/22 (36%); position of my lane: 8/22 (36%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 2, 'change_right': 1}; over-cautious: 12; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 15/27 (56%)
- Actions decided where the label has no governing marking: 11
- Answers that contradict themselves: 6 {'leftmost lane, but a lane line on the left': 5, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 73250, 'cached_input_tokens': 0, 'output_tokens': 23086}; cost about $0.0; latency: {'mean': 34.0, 'max': 158.44}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 14 |
| change_right | 21 | 11 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
