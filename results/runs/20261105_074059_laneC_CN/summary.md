# Lane run 20261105_074059_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 68 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 33/68 (49%); without the lines across the lane: 37/68 (54%)
- Lane actions (every action the label decides, contested cells excluded): 31/68 (46%)
- Left boundary: 52/68 (76%); right boundary: 55/68 (81%); both: 42/68 (62%)
- Markings in the lane, exact set: 53/67 (79%) (without the lines across the lane 61/67 (91%)); added (not in the label): 18, of them lines across the lane 14, by the evidence the answer gave {'partial': 9, 'full': 9}; missed: 3
- Lane count: 41/68 (60%); position of my lane: 50/64 (78%)
- Unsafe errors (label prohibited, answer allowed): 40 {'change_right': 28, 'change_left': 12}; over-cautious: 6; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 69/128 (54%)
- Actions decided where the label has no governing marking: 8
- Answers that contradict themselves: 1 {'change_right allowed across a double solid line': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 68}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 111, 'over_withholding': 25}
- Readable answers: 68/68 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 639948, 'cached_input_tokens': 549400, 'output_tokens': 73915}; cost about $0.9752; latency: {'mean': 21.76, 'max': 36.84}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 68 | 53 |
| change_right | 68 | 37 |
| go_straight | 18 | 14 |
| turn_left | 18 | 13 |
| turn_right | 18 | 13 |
| u_turn | 18 | 13 |
