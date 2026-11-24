# Lane run 20261117_040242_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 11 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 1/11 (9%); without the lines across the lane: 1/11 (9%)
- Lane actions (every action the label decides, contested cells excluded): 3/11 (27%)
- Left boundary: 3/11 (27%); right boundary: 3/10 (30%); both: 1/11 (9%)
- Markings in the lane, exact set: 10/11 (91%) (without the lines across the lane 10/11 (91%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 1
- Lane count: 8/9 (89%); position of my lane: 8/9 (89%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 5; contested unsafe: 1
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 8
- Answers that contradict themselves: 7 {'u_turn decided without an arrow or prohibited-movement marking': 5, 'change_right decided': 3, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'rightmost lane, but a lane line on the right': 1}
- Citations (Test B and C): {'none': 1, 'unlisted': 9, 'in_pack_not_accepted': 1}; IDs written with brackets (read without them): 12
- Boundary evidence: {'same': 18, 'unsupported_guess': 4}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 63756, 'cached_input_tokens': 0, 'output_tokens': 7123}; cost about $0.0; latency: {'mean': 18.34, 'max': 29.02}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 0 |
| change_right | 11 | 4 |
