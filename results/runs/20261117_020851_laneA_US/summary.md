# Lane run 20261117_020851_laneA_US

Test A (image only), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 11/38 (29%); without the lines across the lane: 13/38 (34%)
- Lane actions (every action the label decides, contested cells excluded): 26/37 (70%)
- Left boundary: 26/37 (70%); right boundary: 19/37 (51%); both: 15/38 (39%)
- Markings in the lane, exact set: 29/37 (78%) (without the lines across the lane 32/37 (86%)); added (not in the label): 3, of them lines across the lane 0, by the evidence the answer gave {'full': 3}; missed: 7
- Lane count: 16/38 (42%); position of my lane: 25/38 (66%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 1, 'change_right': 2, 'go_straight': 1}; over-cautious: 5; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 35/42 (83%)
- Actions decided where the label has no governing marking: 8
- Answers that contradict themselves: 8 {'u_turn decided without an arrow or prohibited-movement marking': 5, 'rightmost lane, but a lane line on the right': 1, 'leftmost lane, but a lane line on the left': 1, 'change_right allowed across a curb': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 2
- Tokens: {'input_tokens': 105840, 'cached_input_tokens': 0, 'output_tokens': 22540}; cost about $0.0; latency: {'mean': 43.03, 'max': 116.03}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 31 |
| change_right | 21 | 14 |
| go_straight | 8 | 7 |
| turn_left | 8 | 5 |
| turn_right | 8 | 5 |
| u_turn | 7 | 4 |
