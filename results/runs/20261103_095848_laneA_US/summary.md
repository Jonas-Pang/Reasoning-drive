# Lane run 20261103_095848_laneA_US

Test A (image only), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 17/38 (45%); without the lines across the lane: 21/38 (55%)
- Lane actions (every action the label decides, contested cells excluded): 27/36 (75%)
- Left boundary: 32/37 (86%); right boundary: 31/37 (84%); both: 27/38 (71%)
- Markings in the lane, exact set: 27/37 (73%) (without the lines across the lane 31/37 (84%)); added (not in the label): 16, of them lines across the lane 10, by the evidence the answer gave {'partial': 10, 'full': 6}; missed: 2
- Lane count: 21/38 (55%); position of my lane: 31/38 (82%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 4, 'change_right': 1}; over-cautious: 3; contested unsafe: 8
- Prohibited actions also prohibited by the answer: 26/36 (72%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 66, 'over_withholding': 9, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 168188, 'cached_input_tokens': 121878, 'output_tokens': 37711}; cost about $0.4819; latency: {'mean': 19.45, 'max': 32.29}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 28 |
| change_right | 20 | 17 |
| go_straight | 6 | 4 |
| turn_left | 6 | 4 |
| turn_right | 6 | 4 |
| u_turn | 5 | 4 |
