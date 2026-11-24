# Lane run 20261105_075052_laneA_US

Test A (image only), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 19/38 (50%); without the lines across the lane: 22/38 (58%)
- Lane actions (every action the label decides, contested cells excluded): 27/36 (75%)
- Left boundary: 32/37 (86%); right boundary: 32/37 (86%); both: 28/38 (74%)
- Markings in the lane, exact set: 28/37 (76%) (without the lines across the lane 31/37 (84%)); added (not in the label): 15, of them lines across the lane 9, by the evidence the answer gave {'partial': 8, 'full': 7}; missed: 2
- Lane count: 23/38 (61%); position of my lane: 32/38 (84%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 3, 'change_right': 2}; over-cautious: 3; contested unsafe: 8
- Prohibited actions also prohibited by the answer: 27/36 (75%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 65, 'over_withholding': 10, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 168188, 'cached_input_tokens': 125172, 'output_tokens': 37863}; cost about $0.4772; latency: {'mean': 19.19, 'max': 27.01}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 30 |
| change_right | 20 | 17 |
| go_straight | 6 | 3 |
| turn_left | 6 | 4 |
| turn_right | 6 | 4 |
| u_turn | 5 | 3 |
