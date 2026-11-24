# Lane run 20261105_074605_laneB_CN

Test B (image + the region's rule passages), region CN, 68 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 32/68 (47%); without the lines across the lane: 36/68 (53%)
- Lane actions (every action the label decides, contested cells excluded): 58/68 (85%)
- Left boundary: 54/68 (79%); right boundary: 50/68 (74%); both: 40/68 (59%)
- Markings in the lane, exact set: 52/67 (78%) (without the lines across the lane 60/67 (90%)); added (not in the label): 19, of them lines across the lane 13, by the evidence the answer gave {'full': 9, 'partial': 10}; missed: 3
- Lane count: 44/68 (65%); position of my lane: 49/64 (77%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 1, 'go_straight': 1}; over-cautious: 8; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 114/128 (89%)
- Actions decided where the label has no governing marking: 9
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'accepted': 65, 'in_pack_not_accepted': 2, 'none': 1}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 118, 'over_withholding': 18}
- Readable answers: 68/68 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 585072, 'cached_input_tokens': 502724, 'output_tokens': 68369}; cost about $0.8987; latency: {'mean': 19.69, 'max': 33.81}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 68 | 67 |
| change_right | 68 | 63 |
| go_straight | 18 | 15 |
| turn_left | 18 | 14 |
| turn_right | 18 | 13 |
| u_turn | 18 | 14 |
