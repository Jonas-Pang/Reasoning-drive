# Lane run 20261117_122641_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 4 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 1/4 (25%); without the lines across the lane: 1/4 (25%)
- Lane actions (every action the label decides, contested cells excluded): 0/2 (0%)
- Left boundary: 3/4 (75%); right boundary: 2/4 (50%); both: 1/4 (25%)
- Markings in the lane, exact set: 4/4 (100%) (without the lines across the lane 4/4 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 2/2 (100%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_left': 2}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 0/2 (0%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 1 {'change_left decided': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 2, 'unlisted': 2}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 4, 'unsupported_guess': 4}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 58256, 'cached_input_tokens': 0, 'output_tokens': 3186}; cost about $0.0; latency: {'mean': 29.1, 'max': 38.46}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 0 |
