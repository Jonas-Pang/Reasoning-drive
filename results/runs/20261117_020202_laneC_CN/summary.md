# Lane run 20261117_020202_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 6/25 (24%); without the lines across the lane: 6/25 (24%)
- Lane actions (every action the label decides, contested cells excluded): 10/21 (48%)
- Left boundary: 12/25 (48%); right boundary: 12/25 (48%); both: 8/25 (32%)
- Markings in the lane, exact set: 18/25 (72%) (without the lines across the lane 21/25 (84%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 9
- Lane count: 12/22 (55%); position of my lane: 10/22 (45%)
- Unsafe errors (label prohibited, answer allowed): 10 {'change_right': 3, 'change_left': 7}; over-cautious: 3; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 14/27 (52%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'in_pack_not_accepted': 25}; IDs written with brackets (read without them): 45
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 215700, 'cached_input_tokens': 0, 'output_tokens': 16932}; cost about $0.0; latency: {'mean': 45.6, 'max': 103.94}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 13 |
| change_right | 21 | 14 |
| go_straight | 3 | 3 |
| turn_left | 3 | 2 |
| turn_right | 3 | 2 |
| u_turn | 3 | 2 |
