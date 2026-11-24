# Lane run 20261117_125332_laneA_UK

Test A (image only), region UK, 37 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/37 (0%); without the lines across the lane: 2/37 (5%)
- Lane actions (every action the label decides, contested cells excluded): 8/29 (28%)
- Left boundary: 10/37 (27%); right boundary: 15/37 (41%); both: 5/37 (14%)
- Markings in the lane, exact set: 2/37 (5%) (without the lines across the lane 11/37 (30%)); added (not in the label): 31, of them lines across the lane 12, by the evidence the answer gave {'full': 19, 'partial': 8, 'insufficient': 4}; missed: 15
- Lane count: 6/19 (32%); position of my lane: 10/19 (53%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_right': 1, 'turn_right': 2, 'turn_left': 1, 'go_straight': 1}; over-cautious: 13; contested unsafe: 15
- Prohibited actions also prohibited by the answer: 1/21 (5%)
- Actions decided where the label has no governing marking: 18
- Answers that contradict themselves: 19 {'leftmost lane, but a lane line on the left': 17, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'change_left allowed across a curb': 1, 'change_right prohibited across a broken lane line': 1, 'turn_right allowed': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 62, 'other': 12}
- Readable answers: 31/37 (an unreadable or failed answer counts as wrong); errors: 6; from cache: 0
- Tokens: {'input_tokens': 91512, 'cached_input_tokens': 0, 'output_tokens': 29919}; cost about $0.0; latency: {'mean': 63.16, 'max': 137.76}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 1 |
| change_right | 26 | 15 |
| go_straight | 8 | 6 |
| turn_left | 8 | 1 |
| turn_right | 8 | 1 |
| u_turn | 7 | 0 |
