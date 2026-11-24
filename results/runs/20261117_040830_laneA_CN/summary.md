# Lane run 20261117_040830_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 2/121 (2%); without the lines across the lane: 13/121 (11%)
- Lane actions (every action the label decides, contested cells excluded): 31/118 (26%)
- Left boundary: 65/121 (54%); right boundary: 32/118 (27%); both: 20/121 (17%)
- Markings in the lane, exact set: 13/118 (11%) (without the lines across the lane 65/118 (55%)); added (not in the label): 148, of them lines across the lane 55, by the evidence the answer gave {'insufficient': 96, 'full': 52}; missed: 22
- Lane count: 52/118 (44%); position of my lane: 52/119 (44%)
- Unsafe errors (label prohibited, answer allowed): 15 {'go_straight': 3, 'change_left': 7, 'change_right': 3, 'turn_left': 2}; over-cautious: 64; contested unsafe: 3
- Prohibited actions also prohibited by the answer: 75/142 (53%)
- Actions decided where the label has no governing marking: 9
- Answers that contradict themselves: 20 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 9, 'turn_left not_applicable': 4, 'turn_right not_applicable': 3, 'go_straight decided from an arrow that cannot be read': 1, 'change_right allowed across a curb': 1, 'go_straight allowed': 1, 'leftmost lane, but a lane line on the left': 1, 'go_straight prohibited': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 142, 'unsupported_guess': 106}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 23
- Tokens: {'input_tokens': 296334, 'cached_input_tokens': 0, 'output_tokens': 75690}; cost about $0.0; latency: {'mean': 6.83, 'max': 22.4}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 68 |
| change_right | 108 | 45 |
| go_straight | 25 | 22 |
| turn_left | 22 | 2 |
| turn_right | 21 | 1 |
| u_turn | 21 | 1 |
