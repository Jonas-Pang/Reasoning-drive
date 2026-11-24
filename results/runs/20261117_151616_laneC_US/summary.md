# Lane run 20261117_151616_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 42/104 (40%); without the lines across the lane: 44/104 (42%)
- Lane actions (every action the label decides, contested cells excluded): 75/101 (74%)
- Left boundary: 70/103 (68%); right boundary: 67/102 (66%); both: 46/103 (45%)
- Markings in the lane, exact set: 86/101 (85%) (without the lines across the lane 90/101 (89%)); added (not in the label): 9, of them lines across the lane 2, by the evidence the answer gave {'full': 9}; missed: 9
- Lane count: 70/101 (69%); position of my lane: 72/103 (70%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 3, 'turn_left': 1, 'change_right': 1}; over-cautious: 14; contested unsafe: 7
- Prohibited actions also prohibited by the answer: 56/67 (84%)
- Actions decided where the label has no governing marking: 15
- Answers that contradict themselves: 13 {'u_turn decided without an arrow or prohibited-movement marking': 8, 'rightmost lane, but a lane line on the right': 2, 'leftmost lane, but a lane line on the left': 2, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {'unlisted': 9, 'in_pack_not_accepted': 99}; IDs written with brackets (read without them): 89
- Boundary evidence: {'same': 165, 'unsupported_guess': 50, 'over_withholding': 1}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 878688, 'cached_input_tokens': 0, 'output_tokens': 92255}; cost about $0.0; latency: {'mean': 14.5, 'max': 42.12}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 83 |
| change_right | 51 | 34 |
| go_straight | 9 | 8 |
| turn_left | 9 | 6 |
| turn_right | 10 | 6 |
| u_turn | 9 | 6 |
