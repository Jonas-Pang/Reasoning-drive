# Lane run 20261117_124320_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 23/121 (19%); without the lines across the lane: 24/121 (20%)
- Lane actions (every action the label decides, contested cells excluded): 60/118 (51%)
- Left boundary: 52/121 (43%); right boundary: 62/118 (53%); both: 29/121 (24%)
- Markings in the lane, exact set: 92/118 (78%) (without the lines across the lane 101/118 (86%)); added (not in the label): 13, of them lines across the lane 3, by the evidence the answer gave {'full': 13}; missed: 23
- Lane count: 62/118 (53%); position of my lane: 75/119 (63%)
- Unsafe errors (label prohibited, answer allowed): 28 {'change_left': 14, 'change_right': 13, 'go_straight': 1}; over-cautious: 24; contested unsafe: 11
- Prohibited actions also prohibited by the answer: 105/142 (74%)
- Actions decided where the label has no governing marking: 23
- Answers that contradict themselves: 21 {'u_turn decided without an arrow or prohibited-movement marking': 7, 'leftmost lane, but a lane line on the left': 4, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 4, 'go_straight decided without an arrow or prohibited-movement marking': 3, 'rightmost lane, but a lane line on the right': 2, 'go_straight allowed': 1, 'u_turn not_applicable': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 448880, 'cached_input_tokens': 0, 'output_tokens': 82060}; cost about $0.0; latency: {'mean': 27.38, 'max': 70.2}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 66 |
| change_right | 108 | 71 |
| go_straight | 25 | 23 |
| turn_left | 22 | 18 |
| turn_right | 21 | 18 |
| u_turn | 21 | 17 |
