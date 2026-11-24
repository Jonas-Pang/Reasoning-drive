# Lane run 20261117_034743_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 44/104 (42%); without the lines across the lane: 46/104 (44%)
- Lane actions (every action the label decides, contested cells excluded): 69/102 (68%)
- Left boundary: 65/103 (63%); right boundary: 67/102 (66%); both: 47/103 (46%)
- Markings in the lane, exact set: 85/101 (84%) (without the lines across the lane 90/101 (89%)); added (not in the label): 5, of them lines across the lane 1, by the evidence the answer gave {'full': 5}; missed: 13
- Lane count: 66/101 (65%); position of my lane: 74/103 (72%)
- Unsafe errors (label prohibited, answer allowed): 9 {'change_left': 6, 'u_turn': 1, 'go_straight': 1, 'turn_left': 1}; over-cautious: 19; contested unsafe: 6
- Prohibited actions also prohibited by the answer: 57/72 (79%)
- Actions decided where the label has no governing marking: 28
- Answers that contradict themselves: 26 {'u_turn decided without an arrow or prohibited-movement marking': 21, 'change_left decided': 1, 'leftmost lane, but a lane line on the left': 1, 'go_straight, turn_right decided without an arrow or prohibited-movement marking': 1, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 104, 'unlisted': 4}; IDs written with brackets (read without them): 127
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 820908, 'cached_input_tokens': 0, 'output_tokens': 73725}; cost about $0.0; latency: {'mean': 16.85, 'max': 30.56}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 80 |
| change_right | 54 | 34 |
| go_straight | 10 | 8 |
| turn_left | 10 | 6 |
| turn_right | 11 | 6 |
| u_turn | 9 | 6 |
