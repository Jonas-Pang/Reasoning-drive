# Lane run 20261117_154100_laneA_IN

Test A (image only), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 5/9 (56%); without the lines across the lane: 5/9 (56%)
- Lane actions (every action the label decides, contested cells excluded): 4/6 (67%)
- Left boundary: 7/9 (78%); right boundary: 6/8 (75%); both: 5/9 (56%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 4/5 (80%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 4/4 (100%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 4 {'change_left decided': 2, 'change_right decided': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 32661, 'cached_input_tokens': 0, 'output_tokens': 5612}; cost about $0.0; latency: {'mean': 13.73, 'max': 19.12}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 4 |
| change_right | 5 | 4 |
