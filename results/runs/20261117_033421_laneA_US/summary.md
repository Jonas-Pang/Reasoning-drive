# Lane run 20261117_033421_laneA_US

Test A (image only), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 42/104 (40%); without the lines across the lane: 44/104 (42%)
- Lane actions (every action the label decides, contested cells excluded): 76/102 (75%)
- Left boundary: 68/103 (66%); right boundary: 66/102 (65%); both: 44/103 (43%)
- Markings in the lane, exact set: 86/101 (85%) (without the lines across the lane 91/101 (90%)); added (not in the label): 4, of them lines across the lane 0, by the evidence the answer gave {'full': 4}; missed: 14
- Lane count: 64/101 (63%); position of my lane: 73/103 (71%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 1, 'turn_left': 1, 'change_right': 1}; over-cautious: 13; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 63/72 (88%)
- Actions decided where the label has no governing marking: 17
- Answers that contradict themselves: 22 {'u_turn decided without an arrow or prohibited-movement marking': 13, 'leftmost lane, but a lane line on the left': 3, 'rightmost lane, but a lane line on the right': 2, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'change_right decided': 1, 'change_left decided': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 99
- Tokens: {'input_tokens': 26460, 'cached_input_tokens': 0, 'output_tokens': 5534}; cost about $0.0; latency: {'mean': 14.13, 'max': 24.21}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 85 |
| change_right | 54 | 38 |
| go_straight | 10 | 10 |
| turn_left | 10 | 7 |
| turn_right | 11 | 7 |
| u_turn | 9 | 6 |
