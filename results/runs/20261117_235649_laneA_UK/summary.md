# Lane run 20261117_235649_laneA_UK

Test A (image only), region UK, 48 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/48 (0%); without the lines across the lane: 4/48 (8%)
- Lane actions (every action the label decides, contested cells excluded): 29/39 (74%)
- Left boundary: 13/48 (27%); right boundary: 33/47 (70%); both: 11/48 (23%)
- Markings in the lane, exact set: 1/48 (2%) (without the lines across the lane 22/48 (46%)); added (not in the label): 51, of them lines across the lane 24, by the evidence the answer gave {'full': 42, 'insufficient': 4, 'partial': 5}; missed: 18
- Lane count: 6/28 (21%); position of my lane: 19/28 (68%)
- Unsafe errors (label prohibited, answer allowed): 8 {'change_right': 1, 'turn_right': 4, 'turn_left': 1, 'u_turn': 1, 'go_straight': 1}; over-cautious: 8; contested unsafe: 31
- Prohibited actions also prohibited by the answer: 13/21 (62%)
- Actions decided where the label has no governing marking: 19
- Answers that contradict themselves: 26 {'leftmost lane, but a lane line on the left': 24, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'turn_right prohibited': 2, 'turn_left prohibited': 1, 'change_left prohibited across a broken lane line': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 92, 'unsupported_guess': 4}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 183120, 'cached_input_tokens': 0, 'output_tokens': 48636}; cost about $0.0; latency: {'mean': 6.99, 'max': 9.15}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 7 |
| change_right | 36 | 35 |
| go_straight | 8 | 7 |
| turn_left | 8 | 4 |
| turn_right | 8 | 4 |
| u_turn | 8 | 6 |
