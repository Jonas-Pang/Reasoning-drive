# Lane run 20261118_003346_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 9 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 2/9 (22%); without the lines across the lane: 2/9 (22%)
- Lane actions (every action the label decides, contested cells excluded): 2/6 (33%)
- Left boundary: 5/9 (56%); right boundary: 2/8 (25%); both: 2/9 (22%)
- Markings in the lane, exact set: 6/9 (67%) (without the lines across the lane 8/9 (89%)); added (not in the label): 3, of them lines across the lane 2, by the evidence the answer gave {'insufficient': 1, 'full': 1, 'partial': 1}; missed: 0
- Lane count: 1/5 (20%); position of my lane: 4/5 (80%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_left': 2}; over-cautious: 2; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 4/6 (67%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 7 {'leftmost lane, but a lane line on the left': 4, 'change_right allowed across a curb': 2, 'rightmost lane, but a lane line on the right': 1, 'change_left allowed across a curb': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 7, 'unlisted': 2}; IDs written with brackets (read without them): 20
- Boundary evidence: {'same': 12, 'over_withholding': 2, 'unsupported_guess': 4}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 132633, 'cached_input_tokens': 0, 'output_tokens': 7917}; cost about $0.0; latency: {'mean': 9.19, 'max': 13.52}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 4 |
| change_right | 4 | 2 |
