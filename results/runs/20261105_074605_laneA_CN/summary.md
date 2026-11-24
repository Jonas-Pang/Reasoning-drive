# Lane run 20261105_074605_laneA_CN

Test A (image only), region CN, 68 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 37/68 (54%); without the lines across the lane: 41/68 (60%)
- Lane actions (every action the label decides, contested cells excluded): 57/68 (84%)
- Left boundary: 56/68 (82%); right boundary: 54/68 (79%); both: 45/68 (66%)
- Markings in the lane, exact set: 53/67 (79%) (without the lines across the lane 61/67 (91%)); added (not in the label): 20, of them lines across the lane 15, by the evidence the answer gave {'partial': 11, 'full': 9}; missed: 3
- Lane count: 45/68 (66%); position of my lane: 50/64 (78%)
- Unsafe errors (label prohibited, answer allowed): 2 {'go_straight': 1, 'change_right': 1}; over-cautious: 8; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 115/128 (90%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 120, 'over_withholding': 16}
- Readable answers: 68/68 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 306340, 'cached_input_tokens': 220698, 'output_tokens': 66665}; cost about $0.86; latency: {'mean': 18.61, 'max': 36.87}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 68 | 65 |
| change_right | 68 | 62 |
| go_straight | 18 | 15 |
| turn_left | 18 | 15 |
| turn_right | 18 | 15 |
| u_turn | 18 | 15 |
