# Lane run 20261117_184713_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 29/121 (24%); without the lines across the lane: 29/121 (24%)
- Lane actions (every action the label decides, contested cells excluded): 68/116 (59%)
- Left boundary: 57/121 (47%); right boundary: 60/118 (51%); both: 33/121 (27%)
- Markings in the lane, exact set: 95/118 (81%) (without the lines across the lane 104/118 (88%)); added (not in the label): 11, of them lines across the lane 3, by the evidence the answer gave {'full': 11}; missed: 21
- Lane count: 63/118 (53%); position of my lane: 72/119 (61%)
- Unsafe errors (label prohibited, answer allowed): 35 {'change_right': 17, 'change_left': 16, 'go_straight': 2}; over-cautious: 23; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 123/174 (71%)
- Actions decided where the label has no governing marking: 11
- Answers that contradict themselves: 16 {'u_turn decided without an arrow or prohibited-movement marking': 6, 'rightmost lane, but a lane line on the right': 3, 'go_straight decided without an arrow or prohibited-movement marking': 3, 'leftmost lane, but a lane line on the left': 2, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 88
- Tokens: {'input_tokens': 136692, 'cached_input_tokens': 0, 'output_tokens': 23781}; cost about $0.0; latency: {'mean': 12.92, 'max': 30.49}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 79 |
| change_right | 108 | 82 |
| go_straight | 25 | 23 |
| turn_left | 25 | 19 |
| turn_right | 25 | 18 |
| u_turn | 25 | 19 |
