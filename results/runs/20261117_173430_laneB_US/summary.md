# Lane run 20261117_173430_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 14/38 (37%); without the lines across the lane: 16/38 (42%)
- Lane actions (every action the label decides, contested cells excluded): 24/37 (65%)
- Left boundary: 27/37 (73%); right boundary: 25/37 (68%); both: 19/38 (50%)
- Markings in the lane, exact set: 26/37 (70%) (without the lines across the lane 29/37 (78%)); added (not in the label): 8, of them lines across the lane 0, by the evidence the answer gave {'full': 8}; missed: 7
- Lane count: 15/38 (39%); position of my lane: 28/38 (74%)
- Unsafe errors (label prohibited, answer allowed): 6 {'change_right': 3, 'change_left': 1, 'turn_left': 2}; over-cautious: 7; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 34/42 (81%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 11 {'rightmost lane, but a lane line on the right': 7, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 2, 'change_right decided': 1, 'leftmost lane, but a lane line on the left': 1, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 32, 'unlisted': 2, 'in_pack_not_accepted': 4}; IDs written with brackets (read without them): 91
- Boundary evidence: {'same': 73, 'unsupported_guess': 3}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 369626, 'cached_input_tokens': 0, 'output_tokens': 36191}; cost about $0.0; latency: {'mean': 16.53, 'max': 33.43}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 30 |
| change_right | 21 | 15 |
| go_straight | 8 | 6 |
| turn_left | 8 | 4 |
| turn_right | 8 | 5 |
| u_turn | 7 | 3 |
