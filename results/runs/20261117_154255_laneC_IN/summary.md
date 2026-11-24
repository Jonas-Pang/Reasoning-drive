# Lane run 20261117_154255_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 6/9 (67%); without the lines across the lane: 6/9 (67%)
- Lane actions (every action the label decides, contested cells excluded): 2/6 (33%)
- Left boundary: 7/9 (78%); right boundary: 7/8 (88%); both: 6/9 (67%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 3/5 (60%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_left': 2}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 2/4 (50%)
- Actions decided where the label has no governing marking: 7
- Answers that contradict themselves: 4 {'change_left decided': 4, 'turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'none': 1, 'in_pack_not_accepted': 5, 'unlisted': 3}; IDs written with brackets (read without them): 2
- Boundary evidence: {'unsupported_guess': 7, 'same': 11}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 131076, 'cached_input_tokens': 0, 'output_tokens': 7339}; cost about $0.0; latency: {'mean': 33.48, 'max': 50.78}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 2 |
| change_right | 5 | 4 |
