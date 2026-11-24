# Lane run 20261117_022231_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 5 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/5 (0%); without the lines across the lane: 0/5 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/3 (33%)
- Left boundary: 0/5 (0%); right boundary: 2/4 (50%); both: 0/5 (0%)
- Markings in the lane, exact set: 2/5 (40%) (without the lines across the lane 2/5 (40%)); added (not in the label): 3, of them lines across the lane 0, by the evidence the answer gave {'insufficient': 2, 'full': 1}; missed: 0
- Lane count: 2/5 (40%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 4
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 4 {'leftmost lane, but a lane line on the left': 2, 'change_left allowed across a curb': 2, 'turn_right allowed': 1}
- Citations (Test B and C): {'unlisted': 5}; IDs written with brackets (read without them): 12
- Boundary evidence: {'same': 6, 'unsupported_guess': 4}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 28960, 'cached_input_tokens': 0, 'output_tokens': 5300}; cost about $0.0; latency: {'mean': 21.53, 'max': 27.76}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 1 |
