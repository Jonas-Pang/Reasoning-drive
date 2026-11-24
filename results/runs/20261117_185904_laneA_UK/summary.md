# Lane run 20261117_185904_laneA_UK

Test A (image only), region UK, 48 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 15/48 (31%); without the lines across the lane: 16/48 (33%)
- Lane actions (every action the label decides, contested cells excluded): 21/39 (54%)
- Left boundary: 27/48 (56%); right boundary: 23/47 (49%); both: 17/48 (35%)
- Markings in the lane, exact set: 34/48 (71%) (without the lines across the lane 40/48 (83%)); added (not in the label): 7, of them lines across the lane 0, by the evidence the answer gave {'full': 7}; missed: 10
- Lane count: 21/28 (75%); position of my lane: 21/28 (75%)
- Unsafe errors (label prohibited, answer allowed): 3 {'u_turn': 2, 'change_right': 1}; over-cautious: 16; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 18/21 (86%)
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 15 {'rightmost lane, but a lane line on the right': 10, 'change_right decided': 4, 'leftmost lane, but a lane line on the left': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 91, 'unsupported_guess': 4, 'over_withholding': 1}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 183312, 'cached_input_tokens': 0, 'output_tokens': 32995}; cost about $0.0; latency: {'mean': 13.12, 'max': 23.77}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 7 |
| change_right | 36 | 25 |
| go_straight | 8 | 8 |
| turn_left | 8 | 7 |
| turn_right | 8 | 8 |
| u_turn | 8 | 5 |
