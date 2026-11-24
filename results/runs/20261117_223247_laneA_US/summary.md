# Lane run 20261117_223247_laneA_US

Test A (image only), region US, 108 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 4/104 (4%); without the lines across the lane: 26/104 (25%)
- Lane actions (every action the label decides, contested cells excluded): 76/101 (75%)
- Left boundary: 76/103 (74%); right boundary: 53/102 (52%); both: 38/103 (37%)
- Markings in the lane, exact set: 4/101 (4%) (without the lines across the lane 57/101 (56%)); added (not in the label): 107, of them lines across the lane 52, by the evidence the answer gave {'insufficient': 60, 'full': 46, 'partial': 1}; missed: 15
- Lane count: 48/101 (48%); position of my lane: 48/103 (47%)
- Unsafe errors (label prohibited, answer allowed): 4 {'turn_left': 2, 'change_left': 2}; over-cautious: 24; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 62/68 (91%)
- Actions decided where the label has no governing marking: 44
- Answers that contradict themselves: 21 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 8, 'rightmost lane, but a lane line on the right': 4, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'go_straight allowed': 2, 'turn_left not_applicable': 2, 'leftmost lane, but a lane line on the left': 2, 'turn_left prohibited': 1, 'turn_right prohibited': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 394416, 'cached_input_tokens': 0, 'output_tokens': 90440}; cost about $0.0; latency: {'mean': 7.36, 'max': 8.85}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 89 |
| change_right | 51 | 31 |
| go_straight | 9 | 8 |
| turn_left | 9 | 6 |
| turn_right | 9 | 7 |
| u_turn | 9 | 8 |
