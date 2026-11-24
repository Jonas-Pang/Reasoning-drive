# Lane run 20261117_034804_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 41/104 (39%); without the lines across the lane: 43/104 (41%)
- Lane actions (every action the label decides, contested cells excluded): 66/102 (65%)
- Left boundary: 62/103 (60%); right boundary: 67/102 (66%); both: 43/103 (42%)
- Markings in the lane, exact set: 84/101 (83%) (without the lines across the lane 89/101 (88%)); added (not in the label): 5, of them lines across the lane 1, by the evidence the answer gave {'full': 5}; missed: 16
- Lane count: 67/101 (66%); position of my lane: 73/103 (71%)
- Unsafe errors (label prohibited, answer allowed): 11 {'change_left': 6, 'go_straight': 2, 'u_turn': 1, 'turn_left': 1, 'change_right': 1}; over-cautious: 20; contested unsafe: 7
- Prohibited actions also prohibited by the answer: 55/72 (76%)
- Actions decided where the label has no governing marking: 27
- Answers that contradict themselves: 27 {'u_turn decided without an arrow or prohibited-movement marking': 23, 'change_left decided': 1, 'go_straight, turn_right decided without an arrow or prohibited-movement marking': 1, 'change_right decided': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 104, 'unlisted': 4}; IDs written with brackets (read without them): 127
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 820908, 'cached_input_tokens': 0, 'output_tokens': 73175}; cost about $0.0; latency: {'mean': 16.71, 'max': 25.91}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 79 |
| change_right | 54 | 33 |
| go_straight | 10 | 7 |
| turn_left | 10 | 6 |
| turn_right | 11 | 6 |
| u_turn | 9 | 6 |
