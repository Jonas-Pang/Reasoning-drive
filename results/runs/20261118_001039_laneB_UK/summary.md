# Lane run 20261118_001039_laneB_UK

Test B (image + the region's rule passages), region UK, 8 images, one request each, model meta-muse-glimmer-30b

- Lane identified (both boundaries and the markings): 1/8 (12%); without the lines across the lane: 1/8 (12%)
- Lane actions (every action the label decides, contested cells excluded): 1/4 (25%)
- Left boundary: 2/8 (25%); right boundary: 1/7 (14%); both: 1/8 (12%)
- Markings in the lane, exact set: 4/8 (50%) (without the lines across the lane 5/8 (62%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 1
- Lane count: 5/7 (71%); position of my lane: 5/7 (71%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 0/3 (0%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 3 {'leftmost lane, but a lane line on the left': 1, 'change_right decided': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 3, 'accepted': 2, 'no_answer': 3}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 6, 'over_withholding': 2, 'unsupported_guess': 2, 'other': 6}
- Readable answers: 5/8 (an unreadable or failed answer counts as wrong); errors: 3; from cache: 0
- Tokens: {'input_tokens': 86245, 'cached_input_tokens': 0, 'output_tokens': 24636}; cost about $0.0; latency: {'mean': 34.75, 'max': 42.39}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 0 |
| change_right | 4 | 1 |
| go_straight | 1 | 0 |
| turn_left | 1 | 0 |
| turn_right | 1 | 0 |
| u_turn | 1 | 0 |
