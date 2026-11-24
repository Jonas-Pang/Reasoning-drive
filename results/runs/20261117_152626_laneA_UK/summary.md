# Lane run 20261117_152626_laneA_UK

Test A (image only), region UK, 48 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 12/48 (25%); without the lines across the lane: 13/48 (27%)
- Lane actions (every action the label decides, contested cells excluded): 17/40 (42%)
- Left boundary: 25/48 (52%); right boundary: 23/47 (49%); both: 14/48 (29%)
- Markings in the lane, exact set: 31/48 (65%) (without the lines across the lane 37/48 (77%)); added (not in the label): 10, of them lines across the lane 0, by the evidence the answer gave {'full': 10}; missed: 12
- Lane count: 20/28 (71%); position of my lane: 22/28 (79%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_right': 1}; over-cautious: 16; contested unsafe: 7
- Prohibited actions also prohibited by the answer: 12/21 (57%)
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 19 {'rightmost lane, but a lane line on the right': 13, 'change_right decided': 3, 'go_straight allowed': 2, 'u_turn not_applicable': 1, 'leftmost lane, but a lane line on the left': 1, 'u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'turn_right prohibited': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 92, 'unsupported_guess': 4}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 174816, 'cached_input_tokens': 0, 'output_tokens': 32495}; cost about $0.0; latency: {'mean': 12.46, 'max': 20.59}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 7 |
| change_right | 37 | 22 |
| go_straight | 8 | 8 |
| turn_left | 8 | 6 |
| turn_right | 8 | 6 |
| u_turn | 7 | 2 |
