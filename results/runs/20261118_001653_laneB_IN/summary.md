# Lane run 20261118_001653_laneB_IN

Test B (image + the region's rule passages), region IN, 9 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/9 (11%); without the lines across the lane: 1/9 (11%)
- Lane actions (every action the label decides, contested cells excluded): 1/6 (17%)
- Left boundary: 4/9 (44%); right boundary: 3/8 (38%); both: 1/9 (11%)
- Markings in the lane, exact set: 7/9 (78%) (without the lines across the lane 9/9 (100%)); added (not in the label): 2, of them lines across the lane 2, by the evidence the answer gave {'insufficient': 2}; missed: 0
- Lane count: 0/5 (0%); position of my lane: 4/5 (80%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 4}; over-cautious: 0; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 1/6 (17%)
- Actions decided where the label has no governing marking: 8
- Answers that contradict themselves: 5 {'leftmost lane, but a lane line on the left': 3, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'change_left allowed across a curb': 1}
- Citations (Test B and C): {'unlisted': 9}; IDs written with brackets (read without them): 18
- Boundary evidence: {'over_withholding': 1, 'same': 12, 'unsupported_guess': 5}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 59841, 'cached_input_tokens': 0, 'output_tokens': 7267}; cost about $0.0; latency: {'mean': 6.92, 'max': 8.72}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 1 |
| change_right | 4 | 4 |
