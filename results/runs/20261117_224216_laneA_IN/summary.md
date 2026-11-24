# Lane run 20261117_224216_laneA_IN

Test A (image only), region IN, 9 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/9 (0%); without the lines across the lane: 1/9 (11%)
- Lane actions (every action the label decides, contested cells excluded): 3/6 (50%)
- Left boundary: 2/9 (22%); right boundary: 4/8 (50%); both: 1/9 (11%)
- Markings in the lane, exact set: 0/9 (0%) (without the lines across the lane 7/9 (78%)); added (not in the label): 9, of them lines across the lane 7, by the evidence the answer gave {'insufficient': 8, 'full': 1}; missed: 0
- Lane count: 1/5 (20%); position of my lane: 3/5 (60%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 3}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 3/6 (50%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 1 {'change_left decided': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 34254, 'cached_input_tokens': 0, 'output_tokens': 7292}; cost about $0.0; latency: {'mean': 8.5, 'max': 10.6}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 3 |
| change_right | 4 | 3 |
