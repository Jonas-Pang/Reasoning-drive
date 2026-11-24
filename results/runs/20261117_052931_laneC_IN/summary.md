# Lane run 20261117_052931_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 9 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/9 (11%); without the lines across the lane: 2/9 (22%)
- Lane actions (every action the label decides, contested cells excluded): 0/6 (0%)
- Left boundary: 6/9 (67%); right boundary: 2/8 (25%); both: 2/9 (22%)
- Markings in the lane, exact set: 4/9 (44%) (without the lines across the lane 8/9 (89%)); added (not in the label): 5, of them lines across the lane 4, by the evidence the answer gave {'partial': 3, 'insufficient': 2}; missed: 0
- Lane count: 1/5 (20%); position of my lane: 4/5 (80%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 1; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 1/4 (25%)
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 2 {'change_right allowed across a curb': 1, 'leftmost lane, but a lane line on the left': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {'unlisted': 6, 'in_pack_not_accepted': 3}; IDs written with brackets (read without them): 12
- Boundary evidence: {'over_withholding': 3, 'same': 9, 'unsupported_guess': 3, 'other': 3}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 122661, 'cached_input_tokens': 0, 'output_tokens': 8470}; cost about $0.0; latency: {'mean': 6.8, 'max': 9.02}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 1 |
| change_right | 5 | 3 |
