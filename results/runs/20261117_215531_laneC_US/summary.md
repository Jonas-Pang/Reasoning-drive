# Lane run 20261117_215531_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 40/104 (38%); without the lines across the lane: 42/104 (40%)
- Lane actions (every action the label decides, contested cells excluded): 84/101 (83%)
- Left boundary: 67/103 (65%); right boundary: 68/102 (67%); both: 46/103 (45%)
- Markings in the lane, exact set: 86/101 (85%) (without the lines across the lane 90/101 (89%)); added (not in the label): 9, of them lines across the lane 2, by the evidence the answer gave {'full': 9}; missed: 9
- Lane count: 73/101 (72%); position of my lane: 70/103 (68%)
- Unsafe errors (label prohibited, answer allowed): 6 {'change_left': 4, 'turn_left': 1, 'u_turn': 1}; over-cautious: 14; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 57/68 (84%)
- Actions decided where the label has no governing marking: 20
- Answers that contradict themselves: 13 {'u_turn decided without an arrow or prohibited-movement marking': 6, 'leftmost lane, but a lane line on the left': 2, 'turn_left, u_turn decided without an arrow or prohibited-movement marking': 2, 'rightmost lane, but a lane line on the right': 2, 'change_right decided': 1, 'change_right allowed across a curb': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 98, 'unlisted': 10}; IDs written with brackets (read without them): 148
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 108
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 93 | 87 |
| change_right | 51 | 40 |
| go_straight | 9 | 9 |
| turn_left | 9 | 6 |
| turn_right | 9 | 6 |
| u_turn | 9 | 6 |
