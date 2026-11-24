# Lane run 20261118_000433_laneA_US

Test A (image only), region US, 38 images, one request each, model meta-muse-glimmer-30b

- Lane identified (both boundaries and the markings): 15/38 (39%); without the lines across the lane: 18/38 (47%)
- Lane actions (every action the label decides, contested cells excluded): 23/36 (64%)
- Left boundary: 26/37 (70%); right boundary: 25/37 (68%); both: 19/38 (50%)
- Markings in the lane, exact set: 29/37 (78%) (without the lines across the lane 33/37 (89%)); added (not in the label): 10, of them lines across the lane 5, by the evidence the answer gave {'partial': 7, 'full': 3}; missed: 6
- Lane count: 21/38 (55%); position of my lane: 25/38 (66%)
- Unsafe errors (label prohibited, answer allowed): 3 {'turn_left': 1, 'change_right': 1, 'change_left': 1}; over-cautious: 14; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 40/47 (85%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 3 {'turn_left decided without an arrow or prohibited-movement marking': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 60, 'over_withholding': 14, 'unsupported_guess': 1, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 35
- Tokens: {'input_tokens': 14022, 'cached_input_tokens': 0, 'output_tokens': 13333}; cost about $0.0; latency: {'mean': 17.94, 'max': 21.06}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 27 |
| change_right | 20 | 12 |
| go_straight | 8 | 7 |
| turn_left | 8 | 6 |
| turn_right | 8 | 6 |
| u_turn | 8 | 6 |
