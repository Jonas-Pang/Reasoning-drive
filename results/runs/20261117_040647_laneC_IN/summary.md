# Lane run 20261117_040647_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 4/9 (44%); without the lines across the lane: 4/9 (44%)
- Lane actions (every action the label decides, contested cells excluded): 0/6 (0%)
- Left boundary: 6/9 (67%); right boundary: 6/8 (75%); both: 4/9 (44%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 4/5 (80%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 3}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 1/4 (25%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 6 {'change_left decided': 5, 'change_right decided': 3}
- Citations (Test B and C): {'none': 2, 'in_pack_not_accepted': 4, 'none_needed': 3}; IDs written with brackets (read without them): 1
- Boundary evidence: {'unsupported_guess': 7, 'same': 11}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 122697, 'cached_input_tokens': 0, 'output_tokens': 5532}; cost about $0.0; latency: {'mean': 21.15, 'max': 31.36}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 1 |
| change_right | 5 | 3 |
