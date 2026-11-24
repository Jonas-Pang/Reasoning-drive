# Lane run 20261114_005949_laneD_US

Test D (image only, country not given), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 17/38 (45%); without the lines across the lane: 22/38 (58%)
- Lane actions (every action the label decides, contested cells excluded): 27/36 (75%)
- Left boundary: 32/37 (86%); right boundary: 31/37 (84%); both: 27/38 (71%)
- Markings in the lane, exact set: 27/37 (73%) (without the lines across the lane 32/37 (86%)); added (not in the label): 17, of them lines across the lane 11, by the evidence the answer gave {'full': 5, 'partial': 11, 'insufficient': 1}; missed: 1
- Lane count: 23/38 (61%); position of my lane: 31/38 (82%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 2, 'change_right': 1}; over-cautious: 3; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 27/36 (75%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 62, 'over_withholding': 12, 'other': 2}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 169176, 'cached_input_tokens': 125172, 'output_tokens': 41691}; cost about $0.5174; latency: {'mean': 21.13, 'max': 34.04}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 31 |
| change_right | 20 | 16 |
| go_straight | 6 | 4 |
| turn_left | 6 | 5 |
| turn_right | 6 | 4 |
| u_turn | 5 | 4 |
