# Lane run 20261117_023314_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 7/25 (28%); without the lines across the lane: 7/25 (28%)
- Lane actions (every action the label decides, contested cells excluded): 7/21 (33%)
- Left boundary: 12/25 (48%); right boundary: 12/25 (48%); both: 9/25 (36%)
- Markings in the lane, exact set: 19/25 (76%) (without the lines across the lane 22/25 (88%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 8
- Lane count: 11/22 (50%); position of my lane: 6/22 (27%)
- Unsafe errors (label prohibited, answer allowed): 11 {'change_left': 9, 'change_right': 2}; over-cautious: 4; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 13/27 (48%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 2 {'go_straight decided without an arrow or prohibited-movement marking': 1, 'u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 20, 'in_pack_not_accepted': 5}; IDs written with brackets (read without them): 34
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 25
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 12 |
| change_right | 21 | 13 |
| go_straight | 3 | 3 |
| turn_left | 3 | 2 |
| turn_right | 3 | 2 |
| u_turn | 3 | 2 |
