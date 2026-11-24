# Lane run 20261117_172509_laneA_CN

Test A (image only), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 2/25 (8%); without the lines across the lane: 2/25 (8%)
- Lane actions (every action the label decides, contested cells excluded): 10/21 (48%)
- Left boundary: 11/25 (44%); right boundary: 8/25 (32%); both: 2/25 (8%)
- Markings in the lane, exact set: 17/25 (68%) (without the lines across the lane 21/25 (84%)); added (not in the label): 3, of them lines across the lane 1, by the evidence the answer gave {'full': 3}; missed: 7
- Lane count: 9/22 (41%); position of my lane: 9/22 (41%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 3, 'change_right': 2}; over-cautious: 7; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 22/27 (81%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 2 {'rightmost lane, but a lane line on the right': 1, 'change_left allowed across a curb': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 109800, 'cached_input_tokens': 0, 'output_tokens': 17791}; cost about $0.0; latency: {'mean': 17.88, 'max': 39.44}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 16 |
| change_right | 21 | 12 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
