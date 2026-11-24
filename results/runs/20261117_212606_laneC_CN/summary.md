# Lane run 20261117_212606_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 33/121 (27%); without the lines across the lane: 34/121 (28%)
- Lane actions (every action the label decides, contested cells excluded): 66/116 (57%)
- Left boundary: 59/121 (49%); right boundary: 62/118 (53%); both: 38/121 (31%)
- Markings in the lane, exact set: 93/118 (79%) (without the lines across the lane 102/118 (86%)); added (not in the label): 15, of them lines across the lane 3, by the evidence the answer gave {'full': 15}; missed: 21
- Lane count: 61/118 (52%); position of my lane: 78/119 (66%)
- Unsafe errors (label prohibited, answer allowed): 40 {'change_right': 19, 'change_left': 18, 'go_straight': 1, 'turn_left': 1, 'u_turn': 1}; over-cautious: 25; contested unsafe: 10
- Prohibited actions also prohibited by the answer: 124/174 (71%)
- Actions decided where the label has no governing marking: 11
- Answers that contradict themselves: 16 {'leftmost lane, but a lane line on the left': 5, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 5, 'rightmost lane, but a lane line on the right': 3, 'go_straight allowed': 1, 'enter_waiting_area allowed without a waiting area or two-way left-turn lane': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 112, 'unlisted': 11, 'none': 1}; IDs written with brackets (read without them): 244
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1176884, 'cached_input_tokens': 0, 'output_tokens': 114073}; cost about $0.0; latency: {'mean': 15.14, 'max': 28.13}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 78 |
| change_right | 108 | 77 |
| go_straight | 25 | 23 |
| turn_left | 25 | 20 |
| turn_right | 25 | 21 |
| u_turn | 25 | 20 |
