# Lane run 20261118_002208_laneA_IN

Test A (image only), region IN, 4 images, one request each, model gemma-4-31b-it

- Lane identified (both boundaries and the markings): 1/4 (25%); without the lines across the lane: 1/4 (25%)
- Lane actions (every action the label decides, contested cells excluded): 1/2 (50%)
- Left boundary: 3/4 (75%); right boundary: 2/4 (50%); both: 1/4 (25%)
- Markings in the lane, exact set: 4/4 (100%) (without the lines across the lane 4/4 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 2/2 (100%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 1/2 (50%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 1 {'change_left decided': 1, 'turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 4, 'unsupported_guess': 4}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 15228, 'cached_input_tokens': 0, 'output_tokens': 2896}; cost about $0.0; latency: {'mean': 9.41, 'max': 16.36}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 1 |
