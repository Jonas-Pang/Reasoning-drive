# Lane run 20261117_024617_laneA_UK

Test A (image only), region UK, 5 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 3/5 (60%); without the lines across the lane: 3/5 (60%)
- Lane actions (every action the label decides, contested cells excluded): 1/3 (33%)
- Left boundary: 5/5 (100%); right boundary: 2/4 (50%); both: 3/5 (60%)
- Markings in the lane, exact set: 5/5 (100%) (without the lines across the lane 5/5 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 4/5 (80%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 1
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 3 {'change_right decided': 3}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 6, 'unsupported_guess': 4}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 14745, 'cached_input_tokens': 0, 'output_tokens': 3225}; cost about $0.0; latency: {'mean': 16.87, 'max': 19.97}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 1 |
