# Lane run 20261117_052625_laneA_UK

Test A (image only), region UK, 11 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/11 (0%); without the lines across the lane: 0/11 (0%)
- Lane actions (every action the label decides, contested cells excluded): 4/11 (36%)
- Left boundary: 2/11 (18%); right boundary: 7/10 (70%); both: 1/11 (9%)
- Markings in the lane, exact set: 2/11 (18%) (without the lines across the lane 4/11 (36%)); added (not in the label): 9, of them lines across the lane 3, by the evidence the answer gave {'partial': 2, 'full': 4, 'insufficient': 3}; missed: 2
- Lane count: 2/9 (22%); position of my lane: 8/9 (89%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 3; contested unsafe: 5
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 10
- Answers that contradict themselves: 7 {'leftmost lane, but a lane line on the left': 4, 'change_left allowed across a curb': 3, 'change_right prohibited across a broken lane line': 2}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 18, 'unsupported_guess': 4}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 32395, 'cached_input_tokens': 0, 'output_tokens': 10036}; cost about $0.0; latency: {'mean': 5.75, 'max': 6.81}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 0 |
| change_right | 11 | 5 |
