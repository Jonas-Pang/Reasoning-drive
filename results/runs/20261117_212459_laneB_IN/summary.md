# Lane run 20261117_212459_laneB_IN

Test B (image + the region's rule passages), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 6/9 (67%); without the lines across the lane: 6/9 (67%)
- Lane actions (every action the label decides, contested cells excluded): 6/6 (100%)
- Left boundary: 8/9 (89%); right boundary: 6/8 (75%); both: 6/9 (67%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 3/5 (60%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 6/6 (100%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 4 {'change_left decided': 3, 'u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'unlisted': 8, 'none_needed': 1}; IDs written with brackets (read without them): 13
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 59877, 'cached_input_tokens': 0, 'output_tokens': 7383}; cost about $0.0; latency: {'mean': 17.61, 'max': 25.91}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 6 |
| change_right | 4 | 4 |
