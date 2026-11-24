# Lane run 20261117_215321_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 9 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 6/9 (67%); without the lines across the lane: 6/9 (67%)
- Lane actions (every action the label decides, contested cells excluded): 5/6 (83%)
- Left boundary: 7/9 (78%); right boundary: 7/8 (88%); both: 6/9 (67%)
- Markings in the lane, exact set: 9/9 (100%) (without the lines across the lane 9/9 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 3/5 (60%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 5/6 (83%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 4 {'change_left decided': 4}
- Citations (Test B and C): {'in_pack_not_accepted': 5, 'none': 1, 'unlisted': 3}; IDs written with brackets (read without them): 4
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 132669, 'cached_input_tokens': 0, 'output_tokens': 7433}; cost about $0.0; latency: {'mean': 33.5, 'max': 50.8}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 5 |
| change_right | 4 | 4 |
