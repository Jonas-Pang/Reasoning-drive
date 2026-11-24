# Lane run 20261118_001517_laneA_US

Test A (image only), region US, 38 images, one request each, model gemma-4-31b-it

- Lane identified (both boundaries and the markings): 12/38 (32%); without the lines across the lane: 15/38 (39%)
- Lane actions (every action the label decides, contested cells excluded): 27/36 (75%)
- Left boundary: 26/37 (70%); right boundary: 24/37 (65%); both: 19/38 (50%)
- Markings in the lane, exact set: 27/37 (73%) (without the lines across the lane 31/37 (84%)); added (not in the label): 6, of them lines across the lane 0, by the evidence the answer gave {'full': 6}; missed: 6
- Lane count: 21/38 (55%); position of my lane: 26/38 (68%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_right': 3, 'change_left': 1}; over-cautious: 6; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 40/47 (85%)
- Actions decided where the label has no governing marking: 9
- Answers that contradict themselves: 8 {'u_turn decided without an arrow or prohibited-movement marking': 4, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'rightmost lane, but a lane line on the right': 2, 'change_right decided': 1, 'turn_left, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 144856, 'cached_input_tokens': 0, 'output_tokens': 30568}; cost about $0.0; latency: {'mean': 18.93, 'max': 36.93}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 29 |
| change_right | 20 | 15 |
| go_straight | 8 | 8 |
| turn_left | 8 | 7 |
| turn_right | 8 | 6 |
| u_turn | 8 | 7 |
