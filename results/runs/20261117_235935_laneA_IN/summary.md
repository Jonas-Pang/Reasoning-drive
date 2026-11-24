# Lane run 20261117_235935_laneA_IN

Test A (image only), region IN, 9 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/9 (0%); without the lines across the lane: 0/9 (0%)
- Lane actions (every action the label decides, contested cells excluded): 2/6 (33%)
- Left boundary: 4/9 (44%); right boundary: 3/8 (38%); both: 1/9 (11%)
- Markings in the lane, exact set: 0/9 (0%) (without the lines across the lane 2/9 (22%)); added (not in the label): 9, of them lines across the lane 2, by the evidence the answer gave {'insufficient': 6, 'full': 2, 'partial': 1}; missed: 0
- Lane count: 0/5 (0%); position of my lane: 3/5 (60%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 3}; over-cautious: 1; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 3/6 (50%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 5 {'leftmost lane, but a lane line on the left': 2, 'change_left allowed across a curb': 2, 'change_left decided': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 5, 'same': 12, 'over_withholding': 1}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 34218, 'cached_input_tokens': 0, 'output_tokens': 8538}; cost about $0.0; latency: {'mean': 7.78, 'max': 10.02}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 3 |
| change_right | 4 | 3 |
