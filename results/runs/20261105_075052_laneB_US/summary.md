# Lane run 20261105_075052_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 15/38 (39%); without the lines across the lane: 19/38 (50%)
- Lane actions (every action the label decides, contested cells excluded): 30/36 (83%)
- Left boundary: 28/37 (76%); right boundary: 30/37 (81%); both: 23/38 (61%)
- Markings in the lane, exact set: 27/37 (73%) (without the lines across the lane 32/37 (86%)); added (not in the label): 18, of them lines across the lane 11, by the evidence the answer gave {'partial': 11, 'full': 6, 'insufficient': 1}; missed: 1
- Lane count: 19/38 (50%); position of my lane: 29/38 (76%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 1, 'change_right': 2}; over-cautious: 3; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 32/36 (89%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'accepted': 36, 'in_pack_not_accepted': 2}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 66, 'over_withholding': 9, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 354616, 'cached_input_tokens': 311600, 'output_tokens': 40734}; cost about $0.5245; latency: {'mean': 21.0, 'max': 35.5}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 32 |
| change_right | 20 | 17 |
| go_straight | 6 | 4 |
| turn_left | 6 | 5 |
| turn_right | 6 | 5 |
| u_turn | 5 | 5 |
