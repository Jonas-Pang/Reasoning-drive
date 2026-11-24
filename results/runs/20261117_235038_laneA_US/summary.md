# Lane run 20261117_235038_laneA_US

Test A (image only), region US, 108 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 6/104 (6%); without the lines across the lane: 22/104 (21%)
- Lane actions (every action the label decides, contested cells excluded): 67/101 (66%)
- Left boundary: 45/103 (44%); right boundary: 49/102 (48%); both: 31/103 (30%)
- Markings in the lane, exact set: 19/101 (19%) (without the lines across the lane 65/101 (64%)); added (not in the label): 80, of them lines across the lane 43, by the evidence the answer gave {'full': 42, 'insufficient': 27, 'partial': 11}; missed: 15
- Lane count: 37/101 (37%); position of my lane: 45/103 (44%)
- Unsafe errors (label prohibited, answer allowed): 12 {'change_left': 9, 'change_right': 1, 'turn_left': 1, 'turn_right': 1}; over-cautious: 22; contested unsafe: 21
- Prohibited actions also prohibited by the answer: 49/68 (72%)
- Actions decided where the label has no governing marking: 68
- Answers that contradict themselves: 29 {'leftmost lane, but a lane line on the left': 12, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 10, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 3, 'turn_right allowed': 3, 'change_left prohibited across a broken lane line': 2, 'change_left prohibited': 1, 'change_right prohibited across a broken lane line': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 393984, 'cached_input_tokens': 0, 'output_tokens': 105119}; cost about $0.0; latency: {'mean': 6.77, 'max': 8.36}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 73 |
| change_right | 51 | 38 |
| go_straight | 9 | 9 |
| turn_left | 9 | 6 |
| turn_right | 9 | 6 |
| u_turn | 9 | 5 |
