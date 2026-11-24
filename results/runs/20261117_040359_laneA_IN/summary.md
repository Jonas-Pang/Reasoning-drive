# Lane run 20261117_040359_laneA_IN

Test A (image only), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 5/9 (56%); without the lines across the lane: 5/9 (56%)
- Lane actions (every action the label decides, contested cells excluded): 3/6 (50%)
- Left boundary: 6/9 (67%); right boundary: 7/8 (88%); both: 5/9 (56%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 3/5 (60%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 4/4 (100%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 8 {'change_left decided': 5, 'change_right decided': 1, 'leftmost lane, but a lane line on the left': 1, 'rightmost lane, but a lane line on the right': 1, 'u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 26442, 'cached_input_tokens': 0, 'output_tokens': 5551}; cost about $0.0; latency: {'mean': 15.2, 'max': 18.75}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 4 |
| change_right | 5 | 3 |
