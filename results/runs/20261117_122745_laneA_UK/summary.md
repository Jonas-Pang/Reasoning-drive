# Lane run 20261117_122745_laneA_UK

Test A (image only), region UK, 37 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 5/37 (14%); without the lines across the lane: 6/37 (16%)
- Lane actions (every action the label decides, contested cells excluded): 11/29 (38%)
- Left boundary: 15/37 (41%); right boundary: 14/37 (38%); both: 8/37 (22%)
- Markings in the lane, exact set: 25/37 (68%) (without the lines across the lane 29/37 (78%)); added (not in the label): 4, of them lines across the lane 1, by the evidence the answer gave {'full': 4}; missed: 14
- Lane count: 14/19 (74%); position of my lane: 15/19 (79%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 1, 'go_straight': 1}; over-cautious: 17; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 16/21 (76%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 4 {'rightmost lane, but a lane line on the right': 2, 'change_left decided': 1, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 74}
- Readable answers: 37/37 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 109372, 'cached_input_tokens': 0, 'output_tokens': 23223}; cost about $0.0; latency: {'mean': 11.16, 'max': 18.99}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 9 |
| change_right | 26 | 12 |
| go_straight | 8 | 7 |
| turn_left | 8 | 5 |
| turn_right | 8 | 7 |
| u_turn | 7 | 5 |
