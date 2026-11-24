# Lane run 20261117_115716_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model llama4:scout

- Lane identified (both boundaries and the markings): 3/25 (12%); without the lines across the lane: 4/25 (16%)
- Lane actions (every action the label decides, contested cells excluded): 5/21 (24%)
- Left boundary: 12/25 (48%); right boundary: 10/25 (40%); both: 5/25 (20%)
- Markings in the lane, exact set: 16/25 (64%) (without the lines across the lane 19/25 (76%)); added (not in the label): 6, of them lines across the lane 1, by the evidence the answer gave {'full': 6}; missed: 9
- Lane count: 10/22 (45%); position of my lane: 4/22 (18%)
- Unsafe errors (label prohibited, answer allowed): 6 {'change_right': 5, 'change_left': 1}; over-cautious: 15; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 12/27 (44%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 4 {'leftmost lane, but a lane line on the left': 2, 'change_left prohibited across a broken lane line': 2, 'change_right allowed across a curb': 1, 'change_right prohibited across a broken lane line': 1, 'change_right not_determined': 1}
- Citations (Test B and C): {'none_needed': 1, 'in_pack_not_accepted': 8, 'unlisted': 6, 'accepted': 10}; IDs written with brackets (read without them): 57
- Boundary evidence: {'same': 40, 'unsupported_guess': 10}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 209350, 'cached_input_tokens': 0, 'output_tokens': 15057}; cost about $0.0; latency: {'mean': 17.62, 'max': 33.75}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 12 |
| change_right | 21 | 8 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
