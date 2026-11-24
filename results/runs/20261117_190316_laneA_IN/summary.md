# Lane run 20261117_190316_laneA_IN

Test A (image only), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 4/9 (44%); without the lines across the lane: 4/9 (44%)
- Lane actions (every action the label decides, contested cells excluded): 5/6 (83%)
- Left boundary: 6/9 (67%); right boundary: 6/8 (75%); both: 4/9 (44%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 2/5 (40%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 5/6 (83%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 2 {'change_left decided': 2}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 34254, 'cached_input_tokens': 0, 'output_tokens': 5640}; cost about $0.0; latency: {'mean': 14.49, 'max': 20.42}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 5 |
| change_right | 4 | 4 |
