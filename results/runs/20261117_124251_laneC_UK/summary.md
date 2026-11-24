# Lane run 20261117_124251_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 37 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/37 (0%); without the lines across the lane: 2/37 (5%)
- Lane actions (every action the label decides, contested cells excluded): 4/29 (14%)
- Left boundary: 14/37 (38%); right boundary: 7/37 (19%); both: 3/37 (8%)
- Markings in the lane, exact set: 2/37 (5%) (without the lines across the lane 13/37 (35%)); added (not in the label): 46, of them lines across the lane 17, by the evidence the answer gave {'insufficient': 12, 'full': 33, 'partial': 1}; missed: 16
- Lane count: 6/19 (32%); position of my lane: 9/19 (47%)
- Unsafe errors (label prohibited, answer allowed): 1 {'turn_left': 1}; over-cautious: 28; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 5/21 (24%)
- Actions decided where the label has no governing marking: 10
- Answers that contradict themselves: 12 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 5, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'turn_left not_applicable': 2, 'u_turn decided without an arrow or prohibited-movement marking': 2, 'rightmost lane, but a lane line on the right': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'turn_left prohibited': 1, 'turn_right prohibited': 1}
- Citations (Test B and C): {'unlisted': 37}; IDs written with brackets (read without them): 88
- Boundary evidence: {'same': 74}
- Readable answers: 37/37 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 214711, 'cached_input_tokens': 0, 'output_tokens': 30302}; cost about $0.0; latency: {'mean': 45.28, 'max': 72.36}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 3 |
| change_right | 26 | 6 |
| go_straight | 8 | 8 |
| turn_left | 8 | 0 |
| turn_right | 8 | 1 |
| u_turn | 7 | 2 |
