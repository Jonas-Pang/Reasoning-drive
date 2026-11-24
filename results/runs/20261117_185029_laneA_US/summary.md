# Lane run 20261117_185029_laneA_US

Test A (image only), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 40/104 (38%); without the lines across the lane: 41/104 (39%)
- Lane actions (every action the label decides, contested cells excluded): 80/101 (79%)
- Left boundary: 69/103 (67%); right boundary: 63/102 (62%); both: 42/103 (41%)
- Markings in the lane, exact set: 87/101 (86%) (without the lines across the lane 91/101 (90%)); added (not in the label): 6, of them lines across the lane 0, by the evidence the answer gave {'full': 6}; missed: 12
- Lane count: 63/101 (62%); position of my lane: 76/103 (74%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 3, 'turn_left': 1, 'u_turn': 1}; over-cautious: 16; contested unsafe: 3
- Prohibited actions also prohibited by the answer: 58/68 (85%)
- Actions decided where the label has no governing marking: 10
- Answers that contradict themselves: 11 {'rightmost lane, but a lane line on the right': 3, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'u_turn decided without an arrow or prohibited-movement marking': 2, 'change_right allowed across a curb': 1, 'leftmost lane, but a lane line on the left': 1, 'enter_waiting_area allowed without a waiting area or two-way left-turn lane': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 394416, 'cached_input_tokens': 0, 'output_tokens': 69853}; cost about $0.0; latency: {'mean': 11.19, 'max': 16.06}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 82 |
| change_right | 51 | 44 |
| go_straight | 9 | 9 |
| turn_left | 9 | 6 |
| turn_right | 9 | 6 |
| u_turn | 9 | 6 |
