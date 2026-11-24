# Lane run 20261118_002152_laneB_UK

Test B (image + the region's rule passages), region UK, 8 images, one request each, model gemma-4-31b-it

- Lane identified (both boundaries and the markings): 2/8 (25%); without the lines across the lane: 3/8 (38%)
- Lane actions (every action the label decides, contested cells excluded): 3/4 (75%)
- Left boundary: 5/8 (62%); right boundary: 4/7 (57%); both: 4/8 (50%)
- Markings in the lane, exact set: 5/8 (62%) (without the lines across the lane 6/8 (75%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 3
- Lane count: 6/7 (86%); position of my lane: 6/7 (86%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 3/3 (100%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 5 {'change_right decided': 4, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 2, 'unlisted': 4, 'accepted': 2}; IDs written with brackets (read without them): 3
- Boundary evidence: {'unsupported_guess': 4, 'same': 12}
- Readable answers: 8/8 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 118040, 'cached_input_tokens': 0, 'output_tokens': 6554}; cost about $0.0; latency: {'mean': 6.85, 'max': 11.14}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 1 |
| change_right | 4 | 4 |
| go_straight | 1 | 1 |
| turn_left | 1 | 1 |
| turn_right | 1 | 1 |
| u_turn | 1 | 1 |
