# Lane run 20261117_115409_laneA_CN

Test A (image only), region CN, 25 images, one request each, model llama4:scout

- Lane identified (both boundaries and the markings): 0/25 (0%); without the lines across the lane: 0/25 (0%)
- Lane actions (every action the label decides, contested cells excluded): 3/21 (14%)
- Left boundary: 7/25 (28%); right boundary: 5/25 (20%); both: 0/25 (0%)
- Markings in the lane, exact set: 2/25 (8%) (without the lines across the lane 5/25 (20%)); added (not in the label): 27, of them lines across the lane 6, by the evidence the answer gave {'full': 20, 'partial': 4, 'insufficient': 3}; missed: 8
- Lane count: 10/22 (45%); position of my lane: 7/22 (32%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_right': 3, 'turn_right': 1}; over-cautious: 18; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 14/27 (52%)
- Actions decided where the label has no governing marking: 15
- Answers that contradict themselves: 14 {'turn_right decided without an arrow or prohibited-movement marking': 7, 'go_straight allowed': 3, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 3, 'change_right allowed': 1, 'turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'leftmost lane, but a lane line on the left': 1, 'change_left prohibited across a broken lane line': 1, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 95050, 'cached_input_tokens': 0, 'output_tokens': 16965}; cost about $0.0; latency: {'mean': 21.98, 'max': 68.13}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 11 |
| change_right | 21 | 7 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
