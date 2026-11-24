# Lane run 20261103_034158_laneA_CN

Test A (image only), region CN, 68 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 34/68 (50%); without the lines across the lane: 38/68 (56%)
- Lane actions (every action the label decides, contested cells excluded): 57/68 (84%)
- Left boundary: 55/68 (81%); right boundary: 50/68 (74%); both: 42/68 (62%)
- Markings in the lane, exact set: 53/67 (79%) (without the lines across the lane 61/67 (91%)); added (not in the label): 19, of them lines across the lane 14, by the evidence the answer gave {'partial': 10, 'full': 9}; missed: 3
- Lane count: 45/68 (66%); position of my lane: 52/64 (81%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 1, 'go_straight': 1}; over-cautious: 9; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 115/128 (90%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 120, 'over_withholding': 16}
- Readable answers: 68/68 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 306340, 'cached_input_tokens': 220698, 'output_tokens': 66279}; cost about $0.8561; latency: {'mean': 18.09, 'max': 32.34}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 68 | 65 |
| change_right | 68 | 62 |
| go_straight | 18 | 15 |
| turn_left | 18 | 14 |
| turn_right | 18 | 13 |
| u_turn | 18 | 14 |
