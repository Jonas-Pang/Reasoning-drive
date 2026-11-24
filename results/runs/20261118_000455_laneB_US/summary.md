# Lane run 20261118_000455_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model meta-muse-glimmer-30b

- Lane identified (both boundaries and the markings): 11/38 (29%); without the lines across the lane: 15/38 (39%)
- Lane actions (every action the label decides, contested cells excluded): 19/36 (53%)
- Left boundary: 24/37 (65%); right boundary: 21/37 (57%); both: 17/38 (45%)
- Markings in the lane, exact set: 23/37 (62%) (without the lines across the lane 28/37 (76%)); added (not in the label): 7, of them lines across the lane 3, by the evidence the answer gave {'partial': 5, 'full': 2}; missed: 7
- Lane count: 17/38 (45%); position of my lane: 27/38 (71%)
- Unsafe errors (label prohibited, answer allowed): 2 {'turn_left': 2}; over-cautious: 14; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 34/47 (72%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 2 {'rightmost lane, but a lane line on the right': 2, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 31, 'no_answer': 5, 'in_pack_not_accepted': 2}; IDs written with brackets (read without them): 5
- Boundary evidence: {'same': 47, 'unsupported_guess': 2, 'other': 11, 'over_withholding': 16}
- Readable answers: 33/38 (an unreadable or failed answer counts as wrong); errors: 5; from cache: 0
- Tokens: {'input_tokens': 324951, 'cached_input_tokens': 0, 'output_tokens': 136978}; cost about $0.0; latency: {'mean': 26.93, 'max': 48.21}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 24 |
| change_right | 20 | 10 |
| go_straight | 8 | 6 |
| turn_left | 8 | 4 |
| turn_right | 8 | 4 |
| u_turn | 8 | 5 |
