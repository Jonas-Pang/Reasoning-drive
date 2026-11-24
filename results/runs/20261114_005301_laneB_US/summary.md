# Lane run 20261114_005301_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 17/38 (45%); without the lines across the lane: 21/38 (55%)
- Lane actions (every action the label decides, contested cells excluded): 29/36 (81%)
- Left boundary: 31/37 (84%); right boundary: 32/37 (86%); both: 27/38 (71%)
- Markings in the lane, exact set: 27/37 (73%) (without the lines across the lane 31/37 (84%)); added (not in the label): 18, of them lines across the lane 11, by the evidence the answer gave {'partial': 10, 'full': 7, 'insufficient': 1}; missed: 2
- Lane count: 22/38 (58%); position of my lane: 31/38 (82%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 1, 'change_right': 2}; over-cautious: 4; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 29/36 (81%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'accepted': 36, 'in_pack_not_accepted': 2}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 62, 'over_withholding': 13, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 364724, 'cached_input_tokens': 313242, 'output_tokens': 39181}; cost about $0.5261; latency: {'mean': 16.49, 'max': 28.27}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 32 |
| change_right | 20 | 17 |
| go_straight | 6 | 3 |
| turn_left | 6 | 5 |
| turn_right | 6 | 4 |
| u_turn | 5 | 4 |
