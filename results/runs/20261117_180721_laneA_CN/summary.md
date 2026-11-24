# Lane run 20261117_180721_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 30/121 (25%); without the lines across the lane: 30/121 (25%)
- Lane actions (every action the label decides, contested cells excluded): 59/118 (50%)
- Left boundary: 53/121 (44%); right boundary: 60/118 (51%); both: 34/121 (28%)
- Markings in the lane, exact set: 92/118 (78%) (without the lines across the lane 101/118 (86%)); added (not in the label): 13, of them lines across the lane 3, by the evidence the answer gave {'full': 13}; missed: 23
- Lane count: 65/118 (55%); position of my lane: 75/119 (63%)
- Unsafe errors (label prohibited, answer allowed): 32 {'change_right': 19, 'change_left': 11, 'go_straight': 2}; over-cautious: 24; contested unsafe: 8
- Prohibited actions also prohibited by the answer: 101/142 (71%)
- Actions decided where the label has no governing marking: 17
- Answers that contradict themselves: 14 {'u_turn decided without an arrow or prohibited-movement marking': 5, 'leftmost lane, but a lane line on the left': 2, 'go_straight decided without an arrow or prohibited-movement marking': 2, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'rightmost lane, but a lane line on the right': 2, 'go_straight allowed': 1, 'turn_right prohibited': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 460908, 'cached_input_tokens': 0, 'output_tokens': 82000}; cost about $0.0; latency: {'mean': 11.84, 'max': 18.87}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 69 |
| change_right | 108 | 68 |
| go_straight | 25 | 22 |
| turn_left | 22 | 18 |
| turn_right | 21 | 17 |
| u_turn | 21 | 17 |
