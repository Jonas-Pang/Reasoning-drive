# Lane run 20261117_015337_laneA_CN

Test A (image only), region CN, 25 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/25 (0%); without the lines across the lane: 2/25 (8%)
- Lane actions (every action the label decides, contested cells excluded): 8/21 (38%)
- Left boundary: 13/25 (52%); right boundary: 4/25 (16%); both: 3/25 (12%)
- Markings in the lane, exact set: 1/25 (4%) (without the lines across the lane 10/25 (40%)); added (not in the label): 25, of them lines across the lane 8, by the evidence the answer gave {'insufficient': 11, 'full': 14}; missed: 7
- Lane count: 11/22 (50%); position of my lane: 8/22 (36%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 2, 'change_right': 1, 'turn_left': 1}; over-cautious: 13; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 15/27 (56%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 3 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'turn_left not_applicable': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 73350, 'cached_input_tokens': 0, 'output_tokens': 18904}; cost about $0.0; latency: {'mean': 18.36, 'max': 45.15}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 16 |
| change_right | 21 | 8 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
