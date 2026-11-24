# Lane run 20261118_013050_laneA_CN

Test A (image only), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 9/25 (36%); without the lines across the lane: 9/25 (36%)
- Lane actions (every action the label decides, contested cells excluded): 17/21 (81%)
- Left boundary: 16/25 (64%); right boundary: 14/25 (56%); both: 10/25 (40%)
- Markings in the lane, exact set: 21/25 (84%) (without the lines across the lane 24/25 (96%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 5
- Lane count: 8/22 (36%); position of my lane: 10/22 (45%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 3, 'change_right': 2}; over-cautious: 0; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 23/28 (82%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 3 {'leftmost lane, but a lane line on the left': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 94925, 'cached_input_tokens': 0, 'output_tokens': 16474}; cost about $0.0; latency: {'mean': 12.22, 'max': 32.57}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 18 |
| change_right | 21 | 19 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
