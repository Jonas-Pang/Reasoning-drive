# Lane run 20261117_051415_laneB_US

Test B (image + the region's rule passages), region US, 108 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/104 (1%); without the lines across the lane: 21/104 (20%)
- Lane actions (every action the label decides, contested cells excluded): 56/102 (55%)
- Left boundary: 42/103 (41%); right boundary: 43/102 (42%); both: 24/103 (23%)
- Markings in the lane, exact set: 4/101 (4%) (without the lines across the lane 70/101 (69%)); added (not in the label): 96, of them lines across the lane 68, by the evidence the answer gave {'partial': 44, 'full': 30, 'insufficient': 22}; missed: 15
- Lane count: 47/101 (47%); position of my lane: 53/103 (51%)
- Unsafe errors (label prohibited, answer allowed): 16 {'change_left': 13, 'go_straight': 2, 'change_right': 1}; over-cautious: 19; contested unsafe: 30
- Prohibited actions also prohibited by the answer: 31/72 (43%)
- Actions decided where the label has no governing marking: 32
- Answers that contradict themselves: 53 {'leftmost lane, but a lane line on the left': 19, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 17, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 7, 'change_left allowed across a curb': 5, 'change_right allowed across a curb': 4, 'change_left prohibited across a broken lane line': 2, 'change_left not_determined': 1, 'turn_right decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 77, 'in_pack_not_accepted': 12, 'unlisted': 19}; IDs written with brackets (read without them): 317
- Boundary evidence: {'same': 163, 'unsupported_guess': 50, 'over_withholding': 3}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 932040, 'cached_input_tokens': 0, 'output_tokens': 121607}; cost about $0.0; latency: {'mean': 7.27, 'max': 10.36}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 67 |
| change_right | 54 | 36 |
| go_straight | 10 | 8 |
| turn_left | 10 | 1 |
| turn_right | 11 | 1 |
| u_turn | 9 | 0 |
