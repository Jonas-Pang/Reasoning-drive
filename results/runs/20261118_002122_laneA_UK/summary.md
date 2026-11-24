# Lane run 20261118_002122_laneA_UK

Test A (image only), region UK, 8 images, one request each, model gemma-4-31b-it

- Lane identified (both boundaries and the markings): 2/8 (25%); without the lines across the lane: 2/8 (25%)
- Lane actions (every action the label decides, contested cells excluded): 2/4 (50%)
- Left boundary: 3/8 (38%); right boundary: 2/7 (29%); both: 2/8 (25%)
- Markings in the lane, exact set: 6/8 (75%) (without the lines across the lane 6/8 (75%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 2
- Lane count: 5/7 (71%); position of my lane: 6/7 (86%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 3; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 3/3 (100%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 4 {'change_right decided': 2, 'rightmost lane, but a lane line on the right': 1, 'change_left allowed across a curb': 1, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 12, 'unsupported_guess': 4}
- Readable answers: 8/8 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 30560, 'cached_input_tokens': 0, 'output_tokens': 6417}; cost about $0.0; latency: {'mean': 9.62, 'max': 28.06}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 1 |
| change_right | 4 | 2 |
| go_straight | 1 | 1 |
| turn_left | 1 | 1 |
| turn_right | 1 | 1 |
| u_turn | 1 | 1 |
