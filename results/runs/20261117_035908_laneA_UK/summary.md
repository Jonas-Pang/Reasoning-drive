# Lane run 20261117_035908_laneA_UK

Test A (image only), region UK, 11 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 2/11 (18%); without the lines across the lane: 2/11 (18%)
- Lane actions (every action the label decides, contested cells excluded): 2/11 (18%)
- Left boundary: 5/11 (45%); right boundary: 1/10 (10%); both: 2/11 (18%)
- Markings in the lane, exact set: 10/11 (91%) (without the lines across the lane 10/11 (91%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 1
- Lane count: 7/9 (78%); position of my lane: 8/9 (89%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 7; contested unsafe: 1
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 5 {'change_right decided': 3, 'rightmost lane, but a lane line on the right': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 19, 'unsupported_guess': 3}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 32439, 'cached_input_tokens': 0, 'output_tokens': 6728}; cost about $0.0; latency: {'mean': 16.26, 'max': 22.81}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 11 | 2 |
