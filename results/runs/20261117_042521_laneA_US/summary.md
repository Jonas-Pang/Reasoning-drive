# Lane run 20261117_042521_laneA_US

Test A (image only), region US, 108 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 2/104 (2%); without the lines across the lane: 17/104 (16%)
- Lane actions (every action the label decides, contested cells excluded): 51/102 (50%)
- Left boundary: 66/103 (64%); right boundary: 38/102 (37%); both: 24/103 (23%)
- Markings in the lane, exact set: 6/101 (6%) (without the lines across the lane 69/101 (68%)); added (not in the label): 101, of them lines across the lane 60, by the evidence the answer gave {'insufficient': 62, 'full': 38, 'partial': 1}; missed: 16
- Lane count: 44/101 (44%); position of my lane: 47/103 (46%)
- Unsafe errors (label prohibited, answer allowed): 4 {'turn_left': 1, 'go_straight': 1, 'change_left': 2}; over-cautious: 33; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 46/72 (64%)
- Actions decided where the label has no governing marking: 22
- Answers that contradict themselves: 31 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 19, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 4, 'rightmost lane, but a lane line on the right': 3, 'leftmost lane, but a lane line on the left': 2, 'change_right allowed across a curb': 1, 'turn_right not_applicable': 1, 'turn_left prohibited': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 317520, 'cached_input_tokens': 0, 'output_tokens': 81482}; cost about $0.0; latency: {'mean': 6.44, 'max': 8.67}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 83 |
| change_right | 54 | 20 |
| go_straight | 10 | 8 |
| turn_left | 10 | 2 |
| turn_right | 11 | 1 |
| u_turn | 9 | 0 |
