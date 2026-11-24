# Lane run 20261117_120158_laneA_US

Test A (image only), region US, 38 images, one request each, model llama4:scout

- Lane identified (both boundaries and the markings): 1/38 (3%); without the lines across the lane: 1/38 (3%)
- Lane actions (every action the label decides, contested cells excluded): 17/37 (46%)
- Left boundary: 9/37 (24%); right boundary: 19/37 (51%); both: 5/38 (13%)
- Markings in the lane, exact set: 6/37 (16%) (without the lines across the lane 11/37 (30%)); added (not in the label): 31, of them lines across the lane 7, by the evidence the answer gave {'partial': 2, 'insufficient': 5, 'full': 24}; missed: 11
- Lane count: 9/38 (24%); position of my lane: 12/38 (32%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 1, 'go_straight': 1, 'turn_left': 1, 'turn_right': 1}; over-cautious: 20; contested unsafe: 4
- Prohibited actions also prohibited by the answer: 25/42 (60%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 11 {'leftmost lane, but a lane line on the left': 7, 'turn_right decided without an arrow or prohibited-movement marking': 2, 'change_left prohibited across a broken lane line': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 144552, 'cached_input_tokens': 0, 'output_tokens': 25525}; cost about $0.0; latency: {'mean': 16.55, 'max': 25.76}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 21 |
| change_right | 21 | 12 |
| go_straight | 8 | 7 |
| turn_left | 8 | 3 |
| turn_right | 8 | 2 |
| u_turn | 7 | 2 |
