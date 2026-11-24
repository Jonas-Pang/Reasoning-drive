# Lane run 20261117_173113_laneA_US

Test A (image only), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 9/38 (24%); without the lines across the lane: 11/38 (29%)
- Lane actions (every action the label decides, contested cells excluded): 22/37 (59%)
- Left boundary: 23/37 (62%); right boundary: 23/37 (62%); both: 14/38 (37%)
- Markings in the lane, exact set: 26/37 (70%) (without the lines across the lane 29/37 (78%)); added (not in the label): 10, of them lines across the lane 1, by the evidence the answer gave {'full': 10}; missed: 5
- Lane count: 19/38 (50%); position of my lane: 29/38 (76%)
- Unsafe errors (label prohibited, answer allowed): 6 {'change_right': 4, 'change_left': 1, 'turn_left': 1}; over-cautious: 8; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 35/42 (83%)
- Actions decided where the label has no governing marking: 10
- Answers that contradict themselves: 14 {'u_turn decided without an arrow or prohibited-movement marking': 5, 'rightmost lane, but a lane line on the right': 4, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'change_right decided': 2, 'change_left decided': 1, 'go_straight, turn_left, turn_right decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 153254, 'cached_input_tokens': 0, 'output_tokens': 27952}; cost about $0.0; latency: {'mean': 14.97, 'max': 50.04}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 29 |
| change_right | 21 | 13 |
| go_straight | 8 | 6 |
| turn_left | 8 | 5 |
| turn_right | 8 | 7 |
| u_turn | 7 | 4 |
