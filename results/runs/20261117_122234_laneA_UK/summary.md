# Lane run 20261117_122234_laneA_UK

Test A (image only), region UK, 5 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 4/5 (80%); without the lines across the lane: 4/5 (80%)
- Lane actions (every action the label decides, contested cells excluded): 1/3 (33%)
- Left boundary: 4/5 (80%); right boundary: 4/4 (100%); both: 4/5 (80%)
- Markings in the lane, exact set: 5/5 (100%) (without the lines across the lane 5/5 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 4/5 (80%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 3 {'rightmost lane, but a lane line on the right': 2, 'change_right decided': 2}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 4, 'same': 6}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 18210, 'cached_input_tokens': 0, 'output_tokens': 3324}; cost about $0.0; latency: {'mean': 17.8, 'max': 22.04}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 1 |
