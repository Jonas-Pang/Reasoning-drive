# Lane run 20261117_022029_laneA_UK

Test A (image only), region UK, 5 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/5 (0%); without the lines across the lane: 0/5 (0%)
- Lane actions (every action the label decides, contested cells excluded): 0/3 (0%)
- Left boundary: 0/5 (0%); right boundary: 1/4 (25%); both: 0/5 (0%)
- Markings in the lane, exact set: 4/5 (80%) (without the lines across the lane 4/5 (80%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'insufficient': 1}; missed: 0
- Lane count: 2/5 (40%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 5 {'leftmost lane, but a lane line on the left': 4, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'over_withholding': 1, 'unsupported_guess': 4, 'same': 5}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 14725, 'cached_input_tokens': 0, 'output_tokens': 4594}; cost about $0.0; latency: {'mean': 24.53, 'max': 32.85}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 0 |
