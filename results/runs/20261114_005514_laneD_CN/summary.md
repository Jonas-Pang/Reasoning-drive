# Lane run 20261114_005514_laneD_CN

Test D (image only, country not given), region CN, 68 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 32/68 (47%); without the lines across the lane: 36/68 (53%)
- Lane actions (every action the label decides, contested cells excluded): 52/68 (76%)
- Left boundary: 54/68 (79%); right boundary: 50/68 (74%); both: 41/68 (60%)
- Markings in the lane, exact set: 53/67 (79%) (without the lines across the lane 61/67 (91%)); added (not in the label): 19, of them lines across the lane 14, by the evidence the answer gave {'partial': 9, 'full': 9, 'insufficient': 1}; missed: 3
- Lane count: 43/68 (63%); position of my lane: 49/64 (77%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 1, 'change_right': 3}; over-cautious: 11; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 108/128 (84%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 117, 'over_withholding': 19}
- Readable answers: 68/68 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 308244, 'cached_input_tokens': 220698, 'output_tokens': 70154}; cost about $0.8987; latency: {'mean': 19.15, 'max': 31.99}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 68 | 64 |
| change_right | 68 | 59 |
| go_straight | 18 | 15 |
| turn_left | 18 | 13 |
| turn_right | 18 | 13 |
| u_turn | 18 | 13 |
