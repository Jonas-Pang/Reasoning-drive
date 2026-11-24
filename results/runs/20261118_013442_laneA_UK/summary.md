# Lane run 20261118_013442_laneA_UK

Test A (image only), region UK, 8 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 2/8 (25%); without the lines across the lane: 2/8 (25%)
- Lane actions (every action the label decides, contested cells excluded): 2/4 (50%)
- Left boundary: 6/8 (75%); right boundary: 3/7 (43%); both: 2/8 (25%)
- Markings in the lane, exact set: 6/8 (75%) (without the lines across the lane 6/8 (75%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 2
- Lane count: 4/7 (57%); position of my lane: 6/7 (86%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 2; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 3/3 (100%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 3 {'rightmost lane, but a lane line on the right': 2, 'change_right decided': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 4, 'same': 12}
- Readable answers: 8/8 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 30552, 'cached_input_tokens': 0, 'output_tokens': 5481}; cost about $0.0; latency: {'mean': 15.62, 'max': 24.33}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 2 |
| change_right | 4 | 2 |
| go_straight | 1 | 1 |
| turn_left | 1 | 1 |
| turn_right | 1 | 1 |
| u_turn | 1 | 1 |
