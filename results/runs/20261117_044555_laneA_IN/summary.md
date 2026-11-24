# Lane run 20261117_044555_laneA_IN

Test A (image only), region IN, 9 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/9 (0%); without the lines across the lane: 0/9 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/6 (17%)
- Left boundary: 2/9 (22%); right boundary: 2/8 (25%); both: 0/9 (0%)
- Markings in the lane, exact set: 0/9 (0%) (without the lines across the lane 6/9 (67%)); added (not in the label): 10, of them lines across the lane 6, by the evidence the answer gave {'full': 2, 'insufficient': 8}; missed: 0
- Lane count: 1/5 (20%); position of my lane: 2/5 (40%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_left': 2}; over-cautious: 3; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 2/4 (50%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 5 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 3, 'leftmost lane, but a lane line on the left': 1, 'change_left decided': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 26442, 'cached_input_tokens': 0, 'output_tokens': 6626}; cost about $0.0; latency: {'mean': 7.15, 'max': 9.09}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 2 |
| change_right | 5 | 0 |
