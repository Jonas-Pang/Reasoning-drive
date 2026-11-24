# Lane run 20261117_044751_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 4 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/4 (25%); without the lines across the lane: 1/4 (25%)
- Lane actions (every action the label decides, contested cells excluded): 0/2 (0%)
- Left boundary: 2/4 (50%); right boundary: 1/4 (25%); both: 1/4 (25%)
- Markings in the lane, exact set: 1/4 (25%) (without the lines across the lane 3/4 (75%)); added (not in the label): 3, of them lines across the lane 2, by the evidence the answer gave {'partial': 2, 'full': 1}; missed: 0
- Lane count: 1/2 (50%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 0; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 0/2 (0%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 2 {'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'change_left allowed across a curb': 1}
- Citations (Test B and C): {'unlisted': 3, 'in_pack_not_accepted': 1}; IDs written with brackets (read without them): 3
- Boundary evidence: {'other': 1, 'same': 3, 'over_withholding': 1, 'unsupported_guess': 3}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 4
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 0 |
