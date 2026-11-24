# Lane run 20261118_001835_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gemma-4-31b-it

- Lane identified (both boundaries and the markings): 11/38 (29%); without the lines across the lane: 13/38 (34%)
- Lane actions (every action the label decides, contested cells excluded): 25/36 (69%)
- Left boundary: 27/37 (73%); right boundary: 20/37 (54%); both: 16/38 (42%)
- Markings in the lane, exact set: 29/37 (78%) (without the lines across the lane 33/37 (89%)); added (not in the label): 5, of them lines across the lane 0, by the evidence the answer gave {'full': 5}; missed: 6
- Lane count: 20/38 (53%); position of my lane: 30/38 (79%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 1, 'change_right': 2, 'turn_left': 1, 'u_turn': 1}; over-cautious: 8; contested unsafe: 3
- Prohibited actions also prohibited by the answer: 39/47 (83%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 5 {'rightmost lane, but a lane line on the right': 3, 'change_right decided': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 36, 'unlisted': 2}; IDs written with brackets (read without them): 86
- Boundary evidence: {'same': 72, 'unsupported_guess': 3, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 361228, 'cached_input_tokens': 0, 'output_tokens': 33226}; cost about $0.0; latency: {'mean': 17.25, 'max': 35.62}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 31 |
| change_right | 20 | 14 |
| go_straight | 8 | 7 |
| turn_left | 8 | 6 |
| turn_right | 8 | 5 |
| u_turn | 8 | 6 |
