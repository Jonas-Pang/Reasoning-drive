# Lane run 20261118_000118_laneA_US

Test A (image only), region US, 38 images, one request each, model meta-muse-glimmer-30b

- Lane identified (both boundaries and the markings): 14/38 (37%); without the lines across the lane: 17/38 (45%)
- Lane actions (every action the label decides, contested cells excluded): 21/36 (58%)
- Left boundary: 25/37 (68%); right boundary: 23/37 (62%); both: 18/38 (47%)
- Markings in the lane, exact set: 26/37 (70%) (without the lines across the lane 30/37 (81%)); added (not in the label): 10, of them lines across the lane 5, by the evidence the answer gave {'partial': 7, 'full': 3}; missed: 6
- Lane count: 20/38 (53%); position of my lane: 23/38 (61%)
- Unsafe errors (label prohibited, answer allowed): 3 {'turn_left': 1, 'change_right': 1, 'change_left': 1}; over-cautious: 13; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 38/47 (81%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 3 {'turn_left decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 55, 'other': 7, 'unsupported_guess': 1, 'over_withholding': 13}
- Readable answers: 35/38 (an unreadable or failed answer counts as wrong); errors: 3; from cache: 0
- Tokens: {'input_tokens': 163590, 'cached_input_tokens': 0, 'output_tokens': 142835}; cost about $0.0; latency: {'mean': 19.1, 'max': 28.59}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 24 |
| change_right | 20 | 12 |
| go_straight | 8 | 7 |
| turn_left | 8 | 6 |
| turn_right | 8 | 6 |
| u_turn | 8 | 6 |
