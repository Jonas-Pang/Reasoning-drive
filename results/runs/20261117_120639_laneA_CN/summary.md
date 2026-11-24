# Lane run 20261117_120639_laneA_CN

Test A (image only), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 7/25 (28%); without the lines across the lane: 7/25 (28%)
- Lane actions (every action the label decides, contested cells excluded): 11/21 (52%)
- Left boundary: 18/25 (72%); right boundary: 9/25 (36%); both: 7/25 (28%)
- Markings in the lane, exact set: 19/25 (76%) (without the lines across the lane 22/25 (88%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 7
- Lane count: 9/22 (41%); position of my lane: 11/22 (50%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 2, 'change_right': 2, 'turn_right': 1}; over-cautious: 6; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 22/27 (81%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 2 {'go_straight decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 90500, 'cached_input_tokens': 0, 'output_tokens': 16227}; cost about $0.0; latency: {'mean': 13.1, 'max': 37.58}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 18 |
| change_right | 21 | 12 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 2 |
| u_turn | 3 | 3 |
