# Lane run 20261117_123758_laneA_UK

Test A (image only), region UK, 37 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/37 (0%); without the lines across the lane: 1/37 (3%)
- Lane actions (every action the label decides, contested cells excluded): 5/29 (17%)
- Left boundary: 15/37 (41%); right boundary: 5/37 (14%); both: 3/37 (8%)
- Markings in the lane, exact set: 2/37 (5%) (without the lines across the lane 14/37 (38%)); added (not in the label): 37, of them lines across the lane 14, by the evidence the answer gave {'full': 25, 'insufficient': 12}; missed: 17
- Lane count: 4/19 (21%); position of my lane: 9/19 (47%)
- Unsafe errors (label prohibited, answer allowed): 1 {'turn_left': 1}; over-cautious: 26; contested unsafe: 10
- Prohibited actions also prohibited by the answer: 5/21 (24%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 12 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 4, 'leftmost lane, but a lane line on the left': 3, 'rightmost lane, but a lane line on the right': 1, 'turn_left prohibited': 1, 'turn_right prohibited': 1, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'turn_left not_applicable': 1, 'turn_right not_applicable': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 74}
- Readable answers: 37/37 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 109372, 'cached_input_tokens': 0, 'output_tokens': 28460}; cost about $0.0; latency: {'mean': 8.11, 'max': 24.95}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 5 |
| change_right | 26 | 5 |
| go_straight | 8 | 8 |
| turn_left | 8 | 1 |
| turn_right | 8 | 1 |
| u_turn | 7 | 1 |
