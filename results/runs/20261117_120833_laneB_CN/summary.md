# Lane run 20261117_120833_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 5/25 (20%); without the lines across the lane: 5/25 (20%)
- Lane actions (every action the label decides, contested cells excluded): 13/21 (62%)
- Left boundary: 14/25 (56%); right boundary: 12/25 (48%); both: 7/25 (28%)
- Markings in the lane, exact set: 20/25 (80%) (without the lines across the lane 23/25 (92%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 6
- Lane count: 10/22 (45%); position of my lane: 11/22 (50%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 3, 'change_right': 2}; over-cautious: 4; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 22/27 (81%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 2 {'u_turn decided without an arrow or prohibited-movement marking': 2}
- Citations (Test B and C): {'accepted': 20, 'in_pack_not_accepted': 4, 'unlisted': 1}; IDs written with brackets (read without them): 24
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 207025, 'cached_input_tokens': 0, 'output_tokens': 21149}; cost about $0.0; latency: {'mean': 14.24, 'max': 29.53}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 17 |
| change_right | 21 | 14 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
