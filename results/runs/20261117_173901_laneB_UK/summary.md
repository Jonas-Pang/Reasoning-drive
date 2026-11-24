# Lane run 20261117_173901_laneB_UK

Test B (image + the region's rule passages), region UK, 8 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 3/8 (38%); without the lines across the lane: 3/8 (38%)
- Lane actions (every action the label decides, contested cells excluded): 2/5 (40%)
- Left boundary: 4/8 (50%); right boundary: 7/7 (100%); both: 4/8 (50%)
- Markings in the lane, exact set: 5/8 (62%) (without the lines across the lane 6/8 (75%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 3
- Lane count: 6/7 (86%); position of my lane: 6/7 (86%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 3/3 (100%)
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 5 {'rightmost lane, but a lane line on the right': 3, 'change_right decided': 2, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 3, 'unlisted': 2, 'accepted': 3}; IDs written with brackets (read without them): 13
- Boundary evidence: {'same': 12, 'unsupported_guess': 4}
- Readable answers: 8/8 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 122648, 'cached_input_tokens': 0, 'output_tokens': 7111}; cost about $0.0; latency: {'mean': 24.76, 'max': 42.37}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 1 |
| change_right | 5 | 3 |
| go_straight | 1 | 1 |
| turn_left | 1 | 1 |
| turn_right | 1 | 1 |
| u_turn | 1 | 1 |
