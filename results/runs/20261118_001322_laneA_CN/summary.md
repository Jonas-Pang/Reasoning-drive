# Lane run 20261118_001322_laneA_CN

Test A (image only), region CN, 25 images, one request each, model gemma-4-31b-it

- Lane identified (both boundaries and the markings): 4/25 (16%); without the lines across the lane: 4/25 (16%)
- Lane actions (every action the label decides, contested cells excluded): 12/21 (57%)
- Left boundary: 13/25 (52%); right boundary: 11/25 (44%); both: 4/25 (16%)
- Markings in the lane, exact set: 20/25 (80%) (without the lines across the lane 23/25 (92%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 6
- Lane count: 8/22 (36%); position of my lane: 8/22 (36%)
- Unsafe errors (label prohibited, answer allowed): 6 {'change_left': 4, 'change_right': 2}; over-cautious: 5; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 22/28 (79%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 1 {'leftmost lane, but a lane line on the left': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 94950, 'cached_input_tokens': 0, 'output_tokens': 19833}; cost about $0.0; latency: {'mean': 6.84, 'max': 16.07}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 14 |
| change_right | 21 | 17 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
