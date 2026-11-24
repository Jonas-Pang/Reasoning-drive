# Lane run 20261117_025255_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 38/121 (31%); without the lines across the lane: 38/121 (31%)
- Lane actions (every action the label decides, contested cells excluded): 63/118 (53%)
- Left boundary: 60/121 (50%); right boundary: 69/118 (58%); both: 44/121 (36%)
- Markings in the lane, exact set: 94/118 (80%) (without the lines across the lane 103/118 (87%)); added (not in the label): 3, of them lines across the lane 1, by the evidence the answer gave {'full': 3}; missed: 27
- Lane count: 64/118 (54%); position of my lane: 74/119 (62%)
- Unsafe errors (label prohibited, answer allowed): 41 {'change_left': 19, 'change_right': 19, 'go_straight': 3}; over-cautious: 9; contested unsafe: 15
- Prohibited actions also prohibited by the answer: 83/142 (58%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 5 {'go_straight decided without an arrow or prohibited-movement marking': 2, 'change_left decided': 1, 'u_turn decided without an arrow or prohibited-movement marking': 1, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 99
- Tokens: {'input_tokens': 73350, 'cached_input_tokens': 0, 'output_tokens': 15223}; cost about $0.0; latency: {'mean': 14.22, 'max': 16.91}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 70 |
| change_right | 108 | 70 |
| go_straight | 25 | 22 |
| turn_left | 22 | 14 |
| turn_right | 21 | 13 |
| u_turn | 21 | 13 |
