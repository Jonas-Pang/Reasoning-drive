# Lane run 20261117_052859_laneB_IN

Test B (image + the region's rule passages), region IN, 9 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/9 (0%); without the lines across the lane: 1/9 (11%)
- Lane actions (every action the label decides, contested cells excluded): 1/6 (17%)
- Left boundary: 4/9 (44%); right boundary: 3/8 (38%); both: 2/9 (22%)
- Markings in the lane, exact set: 3/9 (33%) (without the lines across the lane 8/9 (89%)); added (not in the label): 6, of them lines across the lane 5, by the evidence the answer gave {'insufficient': 2, 'partial': 4}; missed: 0
- Lane count: 2/5 (40%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 3}; over-cautious: 0; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 1/4 (25%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 5 {'leftmost lane, but a lane line on the left': 3, 'change_left allowed across a curb': 1, 'rightmost lane, but a lane line on the right': 1, 'change_right prohibited across a broken lane line': 1}
- Citations (Test B and C): {'unlisted': 9}; IDs written with brackets (read without them): 17
- Boundary evidence: {'over_withholding': 2, 'same': 10, 'unsupported_guess': 3, 'other': 3}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 52029, 'cached_input_tokens': 0, 'output_tokens': 8893}; cost about $0.0; latency: {'mean': 6.46, 'max': 7.37}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 1 |
| change_right | 5 | 4 |
