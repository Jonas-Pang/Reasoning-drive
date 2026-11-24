# Lane run 20261117_232159_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 9 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/9 (0%); without the lines across the lane: 0/9 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/6 (17%)
- Left boundary: 1/9 (11%); right boundary: 3/8 (38%); both: 0/9 (0%)
- Markings in the lane, exact set: 3/9 (33%) (without the lines across the lane 8/9 (89%)); added (not in the label): 6, of them lines across the lane 5, by the evidence the answer gave {'full': 2, 'insufficient': 4}; missed: 0
- Lane count: 1/5 (20%); position of my lane: 1/5 (20%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 5}; over-cautious: 2; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 1/6 (17%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 4 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 3, 'change_left decided': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 7, 'none_needed': 2}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 132669, 'cached_input_tokens': 0, 'output_tokens': 6630}; cost about $0.0; latency: {'mean': 10.55, 'max': 16.64}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 1 |
| change_right | 4 | 2 |
