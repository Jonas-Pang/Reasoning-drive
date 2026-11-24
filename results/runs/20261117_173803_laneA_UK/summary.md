# Lane run 20261117_173803_laneA_UK

Test A (image only), region UK, 8 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 1/8 (12%); without the lines across the lane: 1/8 (12%)
- Lane actions (every action the label decides, contested cells excluded): 1/5 (20%)
- Left boundary: 3/8 (38%); right boundary: 7/7 (100%); both: 3/8 (38%)
- Markings in the lane, exact set: 4/8 (50%) (without the lines across the lane 5/8 (62%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 4
- Lane count: 5/7 (71%); position of my lane: 6/7 (86%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 0/3 (0%)
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 4 {'change_right decided': 2, 'rightmost lane, but a lane line on the right': 2}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 4, 'same': 12}
- Readable answers: 8/8 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 35168, 'cached_input_tokens': 0, 'output_tokens': 5630}; cost about $0.0; latency: {'mean': 18.75, 'max': 26.19}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 1 |
| change_right | 5 | 3 |
| go_straight | 1 | 1 |
| turn_left | 1 | 0 |
| turn_right | 1 | 0 |
| u_turn | 1 | 0 |
