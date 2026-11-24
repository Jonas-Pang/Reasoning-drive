# Lane run 20261117_023321_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 10/38 (26%); without the lines across the lane: 11/38 (29%)
- Lane actions (every action the label decides, contested cells excluded): 19/37 (51%)
- Left boundary: 22/37 (59%); right boundary: 19/37 (51%); both: 13/38 (34%)
- Markings in the lane, exact set: 29/37 (78%) (without the lines across the lane 31/37 (84%)); added (not in the label): 4, of them lines across the lane 0, by the evidence the answer gave {'full': 4}; missed: 6
- Lane count: 17/38 (45%); position of my lane: 24/38 (63%)
- Unsafe errors (label prohibited, answer allowed): 9 {'change_left': 5, 'change_right': 3, 'turn_left': 1}; over-cautious: 10; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 30/42 (71%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 7 {'rightmost lane, but a lane line on the right': 2, 'change_right decided': 2, 'leftmost lane, but a lane line on the left': 2, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 35, 'unlisted': 2, 'in_pack_not_accepted': 1}; IDs written with brackets (read without them): 68
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 24
- Tokens: {'input_tokens': 120876, 'cached_input_tokens': 0, 'output_tokens': 12369}; cost about $0.0; latency: {'mean': 38.67, 'max': 68.24}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 26 |
| change_right | 21 | 11 |
| go_straight | 8 | 8 |
| turn_left | 8 | 3 |
| turn_right | 8 | 4 |
| u_turn | 7 | 4 |
