# Lane run 20261117_020252_laneA_US

Test A (image only), region US, 38 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 2/38 (5%); without the lines across the lane: 5/38 (13%)
- Lane actions (every action the label decides, contested cells excluded): 21/37 (57%)
- Left boundary: 26/37 (70%); right boundary: 17/37 (46%); both: 13/38 (34%)
- Markings in the lane, exact set: 3/37 (8%) (without the lines across the lane 17/37 (46%)); added (not in the label): 42, of them lines across the lane 13, by the evidence the answer gave {'insufficient': 22, 'full': 20}; missed: 13
- Lane count: 11/38 (29%); position of my lane: 14/38 (37%)
- Unsafe errors (label prohibited, answer allowed): 4 {'go_straight': 2, 'turn_left': 2}; over-cautious: 9; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 25/42 (60%)
- Actions decided where the label has no governing marking: 10
- Answers that contradict themselves: 10 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 5, 'change_right allowed across a curb': 1, 'leftmost lane, but a lane line on the left': 1, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight, turn_right decided without an arrow or prohibited-movement marking': 1, 'turn_left not_applicable': 1, 'turn_right not_applicable': 1, 'turn_left decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 111720, 'cached_input_tokens': 0, 'output_tokens': 29037}; cost about $0.0; latency: {'mean': 18.73, 'max': 66.63}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 31 |
| change_right | 21 | 15 |
| go_straight | 8 | 4 |
| turn_left | 8 | 0 |
| turn_right | 8 | 0 |
| u_turn | 7 | 0 |
