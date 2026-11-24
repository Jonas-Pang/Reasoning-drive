# Lane run 20261117_023312_laneA_CN

Test A (image only), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 8/25 (32%); without the lines across the lane: 8/25 (32%)
- Lane actions (every action the label decides, contested cells excluded): 8/21 (38%)
- Left boundary: 14/25 (56%); right boundary: 12/25 (48%); both: 10/25 (40%)
- Markings in the lane, exact set: 19/25 (76%) (without the lines across the lane 22/25 (88%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 8
- Lane count: 10/22 (45%); position of my lane: 9/22 (41%)
- Unsafe errors (label prohibited, answer allowed): 11 {'change_right': 3, 'change_left': 8}; over-cautious: 3; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 13/27 (48%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 2 {'go_straight decided without an arrow or prohibited-movement marking': 1, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 25
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 13 |
| change_right | 21 | 13 |
| go_straight | 3 | 3 |
| turn_left | 3 | 2 |
| turn_right | 3 | 2 |
| u_turn | 3 | 2 |
