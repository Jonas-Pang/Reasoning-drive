# Lane run 20261117_052831_laneA_IN

Test A (image only), region IN, 9 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/9 (11%); without the lines across the lane: 2/9 (22%)
- Lane actions (every action the label decides, contested cells excluded): 1/6 (17%)
- Left boundary: 5/9 (56%); right boundary: 2/8 (25%); both: 3/9 (33%)
- Markings in the lane, exact set: 6/9 (67%) (without the lines across the lane 8/9 (89%)); added (not in the label): 3, of them lines across the lane 2, by the evidence the answer gave {'full': 1, 'partial': 2}; missed: 0
- Lane count: 2/5 (40%); position of my lane: 4/5 (80%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 1/4 (25%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 4 {'rightmost lane, but a lane line on the right': 2, 'change_right decided': 1, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'over_withholding': 5, 'unsupported_guess': 4, 'other': 2, 'same': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 26406, 'cached_input_tokens': 0, 'output_tokens': 7707}; cost about $0.0; latency: {'mean': 5.58, 'max': 6.61}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 1 |
| change_right | 5 | 3 |
