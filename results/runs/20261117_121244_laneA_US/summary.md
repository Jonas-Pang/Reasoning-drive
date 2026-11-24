# Lane run 20261117_121244_laneA_US

Test A (image only), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 10/38 (26%); without the lines across the lane: 12/38 (32%)
- Lane actions (every action the label decides, contested cells excluded): 25/37 (68%)
- Left boundary: 25/37 (68%); right boundary: 23/37 (62%); both: 16/38 (42%)
- Markings in the lane, exact set: 27/37 (73%) (without the lines across the lane 30/37 (81%)); added (not in the label): 8, of them lines across the lane 0, by the evidence the answer gave {'full': 7, 'insufficient': 1}; missed: 6
- Lane count: 19/38 (50%); position of my lane: 29/38 (76%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_right': 2, 'turn_left': 2, 'change_left': 1}; over-cautious: 7; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 35/42 (83%)
- Actions decided where the label has no governing marking: 10
- Answers that contradict themselves: 10 {'u_turn decided without an arrow or prohibited-movement marking': 7, 'rightmost lane, but a lane line on the right': 3, 'ONLY': 1, 'change_right decided': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 72, 'unsupported_guess': 3, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 132050, 'cached_input_tokens': 0, 'output_tokens': 25904}; cost about $0.0; latency: {'mean': 12.14, 'max': 36.3}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 31 |
| change_right | 21 | 15 |
| go_straight | 8 | 7 |
| turn_left | 8 | 4 |
| turn_right | 8 | 5 |
| u_turn | 7 | 3 |
