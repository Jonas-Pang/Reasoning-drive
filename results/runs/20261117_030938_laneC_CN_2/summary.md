# Lane run 20261117_030938_laneC_CN_2

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 37/121 (31%); without the lines across the lane: 37/121 (31%)
- Lane actions (every action the label decides, contested cells excluded): 55/118 (47%)
- Left boundary: 56/121 (46%); right boundary: 68/118 (58%); both: 42/121 (35%)
- Markings in the lane, exact set: 93/118 (79%) (without the lines across the lane 102/118 (86%)); added (not in the label): 4, of them lines across the lane 1, by the evidence the answer gave {'full': 4}; missed: 29
- Lane count: 67/118 (57%); position of my lane: 75/119 (63%)
- Unsafe errors (label prohibited, answer allowed): 51 {'change_left': 24, 'change_right': 24, 'go_straight': 3}; over-cautious: 17; contested unsafe: 17
- Prohibited actions also prohibited by the answer: 73/142 (51%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 4 {'change_left decided': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight allowed': 1, 'u_turn prohibited': 1, 'enter_waiting_area allowed without a waiting area or two-way left-turn lane': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 119, 'unlisted': 5}; IDs written with brackets (read without them): 245
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 1
- Tokens: {'input_tokens': 1061244, 'cached_input_tokens': 0, 'output_tokens': 83579}; cost about $0.0; latency: {'mean': 18.52, 'max': 49.5}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 62 |
| change_right | 108 | 62 |
| go_straight | 25 | 21 |
| turn_left | 22 | 14 |
| turn_right | 21 | 14 |
| u_turn | 21 | 13 |
