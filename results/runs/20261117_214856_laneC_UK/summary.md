# Lane run 20261117_214856_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 48 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 12/48 (25%); without the lines across the lane: 13/48 (27%)
- Lane actions (every action the label decides, contested cells excluded): 23/39 (59%)
- Left boundary: 19/48 (40%); right boundary: 27/47 (57%); both: 13/48 (27%)
- Markings in the lane, exact set: 35/48 (73%) (without the lines across the lane 39/48 (81%)); added (not in the label): 9, of them lines across the lane 3, by the evidence the answer gave {'full': 9}; missed: 11
- Lane count: 21/28 (75%); position of my lane: 21/28 (75%)
- Unsafe errors (label prohibited, answer allowed): 2 {'u_turn': 1, 'change_right': 1}; over-cautious: 16; contested unsafe: 12
- Prohibited actions also prohibited by the answer: 18/21 (86%)
- Actions decided where the label has no governing marking: 9
- Answers that contradict themselves: 24 {'rightmost lane, but a lane line on the right': 11, 'change_right decided': 6, 'u_turn decided without an arrow or prohibited-movement marking': 5, 'change_left allowed across a curb': 2, 'leftmost lane, but a lane line on the left': 2, 'change_right allowed across a curb': 1, 'change_left decided': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'unlisted': 48}; IDs written with brackets (read without them): 79
- Boundary evidence: {'same': 92, 'unsupported_guess': 4}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 319968, 'cached_input_tokens': 0, 'output_tokens': 38514}; cost about $0.0; latency: {'mean': 14.04, 'max': 26.98}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 6 |
| change_right | 36 | 27 |
| go_straight | 8 | 7 |
| turn_left | 8 | 7 |
| turn_right | 8 | 8 |
| u_turn | 8 | 5 |
