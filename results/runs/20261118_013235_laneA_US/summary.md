# Lane run 20261118_013235_laneA_US

Test A (image only), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 10/38 (26%); without the lines across the lane: 11/38 (29%)
- Lane actions (every action the label decides, contested cells excluded): 23/36 (64%)
- Left boundary: 25/37 (68%); right boundary: 22/37 (59%); both: 14/38 (37%)
- Markings in the lane, exact set: 26/37 (70%) (without the lines across the lane 30/37 (81%)); added (not in the label): 8, of them lines across the lane 0, by the evidence the answer gave {'full': 7, 'insufficient': 1}; missed: 9
- Lane count: 19/38 (50%); position of my lane: 27/38 (71%)
- Unsafe errors (label prohibited, answer allowed): 13 {'turn_left': 4, 'u_turn': 4, 'change_right': 3, 'change_left': 2}; over-cautious: 9; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 31/47 (66%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 6 {'rightmost lane, but a lane line on the right': 2, 'change_right decided': 1, 'leftmost lane, but a lane line on the left': 1, 'u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 72, 'unsupported_guess': 3, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 138776, 'cached_input_tokens': 0, 'output_tokens': 25445}; cost about $0.0; latency: {'mean': 9.83, 'max': 13.55}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 30 |
| change_right | 20 | 14 |
| go_straight | 8 | 5 |
| turn_left | 8 | 3 |
| turn_right | 8 | 5 |
| u_turn | 8 | 3 |
