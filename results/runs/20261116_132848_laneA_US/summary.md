# Lane run 20261116_132848_laneA_US

Test A (image only), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 19/38 (50%); without the lines across the lane: 21/38 (55%)
- Lane actions (every action the label decides, contested cells excluded): 28/36 (78%)
- Left boundary: 31/37 (84%); right boundary: 30/37 (81%); both: 26/38 (68%)
- Markings in the lane, exact set: 28/37 (76%) (without the lines across the lane 31/37 (84%)); added (not in the label): 14, of them lines across the lane 8, by the evidence the answer gave {'partial': 7, 'full': 7}; missed: 2
- Lane count: 22/38 (58%); position of my lane: 32/38 (84%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 3, 'change_right': 1}; over-cautious: 2; contested unsafe: 7
- Prohibited actions also prohibited by the answer: 30/38 (79%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 64, 'over_withholding': 9, 'unsupported_guess': 2, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 38
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 32 | 29 |
| change_right | 20 | 18 |
| go_straight | 7 | 6 |
| turn_left | 7 | 4 |
| turn_right | 7 | 4 |
| u_turn | 6 | 3 |
