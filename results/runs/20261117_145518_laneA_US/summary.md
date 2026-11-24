# Lane run 20261117_145518_laneA_US

Test A (image only), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 40/104 (38%); without the lines across the lane: 41/104 (39%)
- Lane actions (every action the label decides, contested cells excluded): 76/101 (75%)
- Left boundary: 70/103 (68%); right boundary: 64/102 (63%); both: 42/103 (41%)
- Markings in the lane, exact set: 87/101 (86%) (without the lines across the lane 91/101 (90%)); added (not in the label): 6, of them lines across the lane 0, by the evidence the answer gave {'full': 6}; missed: 12
- Lane count: 61/101 (60%); position of my lane: 74/103 (72%)
- Unsafe errors (label prohibited, answer allowed): 2 {'turn_left': 1, 'change_right': 1}; over-cautious: 11; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 58/67 (87%)
- Actions decided where the label has no governing marking: 24
- Answers that contradict themselves: 25 {'u_turn decided without an arrow or prohibited-movement marking': 16, 'rightmost lane, but a lane line on the right': 4, 'leftmost lane, but a lane line on the left': 3, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'go_straight, turn_right decided without an arrow or prohibited-movement marking': 1, 'change_right decided': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 375300, 'cached_input_tokens': 0, 'output_tokens': 70486}; cost about $0.0; latency: {'mean': 13.26, 'max': 48.65}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 87 |
| change_right | 51 | 35 |
| go_straight | 9 | 8 |
| turn_left | 9 | 6 |
| turn_right | 10 | 6 |
| u_turn | 9 | 5 |
