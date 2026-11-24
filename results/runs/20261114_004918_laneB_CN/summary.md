# Lane run 20261114_004918_laneB_CN

Test B (image + the region's rule passages), region CN, 68 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 33/68 (49%); without the lines across the lane: 37/68 (54%)
- Lane actions (every action the label decides, contested cells excluded): 55/68 (81%)
- Left boundary: 52/68 (76%); right boundary: 51/68 (75%); both: 41/68 (60%)
- Markings in the lane, exact set: 53/67 (79%) (without the lines across the lane 61/67 (91%)); added (not in the label): 19, of them lines across the lane 14, by the evidence the answer gave {'partial': 10, 'full': 9}; missed: 3
- Lane count: 43/68 (63%); position of my lane: 48/64 (75%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 2}; over-cautious: 8; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 112/128 (88%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 1 {'change_right allowed across a curb': 1}
- Citations (Test B and C): {'accepted': 66, 'in_pack_not_accepted': 2}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 118, 'over_withholding': 18}
- Readable answers: 68/68 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 603500, 'cached_input_tokens': 513488, 'output_tokens': 68407}; cost about $0.9154; latency: {'mean': 15.56, 'max': 24.25}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 68 | 65 |
| change_right | 68 | 61 |
| go_straight | 18 | 16 |
| turn_left | 18 | 13 |
| turn_right | 18 | 13 |
| u_turn | 18 | 13 |
