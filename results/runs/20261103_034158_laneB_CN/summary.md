# Lane run 20261103_034158_laneB_CN

Test B (image + the region's rule passages), region CN, 68 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 33/68 (49%); without the lines across the lane: 37/68 (54%)
- Lane actions (every action the label decides, contested cells excluded): 58/68 (85%)
- Left boundary: 54/68 (79%); right boundary: 52/68 (76%); both: 41/68 (60%)
- Markings in the lane, exact set: 53/67 (79%) (without the lines across the lane 61/67 (91%)); added (not in the label): 19, of them lines across the lane 14, by the evidence the answer gave {'partial': 11, 'full': 8}; missed: 3
- Lane count: 45/68 (66%); position of my lane: 51/64 (80%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 1, 'go_straight': 1}; over-cautious: 8; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 115/128 (90%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'accepted': 66, 'in_pack_not_accepted': 2}; IDs written with brackets (read without them): 6
- Boundary evidence: {'same': 116, 'over_withholding': 20}
- Readable answers: 68/68 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 585072, 'cached_input_tokens': 495331, 'output_tokens': 70953}; cost about $0.9385; latency: {'mean': 19.4, 'max': 43.63}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 68 | 67 |
| change_right | 68 | 64 |
| go_straight | 18 | 14 |
| turn_left | 18 | 13 |
| turn_right | 18 | 13 |
| u_turn | 18 | 13 |
