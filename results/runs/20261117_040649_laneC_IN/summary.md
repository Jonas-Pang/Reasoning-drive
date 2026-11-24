# Lane run 20261117_040649_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 3/9 (33%); without the lines across the lane: 3/9 (33%)
- Lane actions (every action the label decides, contested cells excluded): 0/6 (0%)
- Left boundary: 5/9 (56%); right boundary: 6/8 (75%); both: 3/9 (33%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 4/5 (80%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 4}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 0/4 (0%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 8 {'change_left decided': 7, 'change_right decided': 3}
- Citations (Test B and C): {'none': 2, 'in_pack_not_accepted': 4, 'none_needed': 3}; IDs written with brackets (read without them): 2
- Boundary evidence: {'unsupported_guess': 7, 'same': 11}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 122697, 'cached_input_tokens': 0, 'output_tokens': 5494}; cost about $0.0; latency: {'mean': 23.86, 'max': 40.37}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 0 |
| change_right | 5 | 4 |
