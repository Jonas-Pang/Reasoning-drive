# Lane run 20261117_040456_laneB_IN

Test B (image + the region's rule passages), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 3/9 (33%); without the lines across the lane: 3/9 (33%)
- Lane actions (every action the label decides, contested cells excluded): 3/6 (50%)
- Left boundary: 5/9 (56%); right boundary: 6/8 (75%); both: 3/9 (33%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 3/5 (60%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 3/4 (75%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 6 {'change_left decided': 3, 'change_right decided': 3, 'change_left allowed across a curb': 1, 'u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'unlisted': 6, 'none': 1, 'none_needed': 2}; IDs written with brackets (read without them): 8
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 52065, 'cached_input_tokens': 0, 'output_tokens': 6181}; cost about $0.0; latency: {'mean': 28.01, 'max': 55.72}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 3 |
| change_right | 5 | 4 |
