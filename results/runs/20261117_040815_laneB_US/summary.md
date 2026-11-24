# Lane run 20261117_040815_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/38 (0%); without the lines across the lane: 2/38 (5%)
- Lane actions (every action the label decides, contested cells excluded): 17/37 (46%)
- Left boundary: 27/37 (73%); right boundary: 13/37 (35%); both: 7/38 (18%)
- Markings in the lane, exact set: 5/37 (14%) (without the lines across the lane 21/37 (57%)); added (not in the label): 35, of them lines across the lane 16, by the evidence the answer gave {'full': 30, 'insufficient': 5}; missed: 7
- Lane count: 10/38 (26%); position of my lane: 15/38 (39%)
- Unsafe errors (label prohibited, answer allowed): 4 {'turn_left': 3, 'change_right': 1}; over-cautious: 15; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 29/42 (69%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 10 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 3, 'turn_left not_applicable': 2, 'go_straight allowed': 1, 'change_right allowed across a curb': 1, 'rightmost lane, but a lane line on the right': 1, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight prohibited': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 37, 'in_pack_not_accepted': 1}; IDs written with brackets (read without them): 43
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 38
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 30 |
| change_right | 21 | 8 |
| go_straight | 8 | 7 |
| turn_left | 8 | 2 |
| turn_right | 8 | 1 |
| u_turn | 7 | 1 |
