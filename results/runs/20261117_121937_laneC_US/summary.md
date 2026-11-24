# Lane run 20261117_121937_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 8/38 (21%); without the lines across the lane: 9/38 (24%)
- Lane actions (every action the label decides, contested cells excluded): 24/37 (65%)
- Left boundary: 20/37 (54%); right boundary: 20/37 (54%); both: 11/38 (29%)
- Markings in the lane, exact set: 26/37 (70%) (without the lines across the lane 28/37 (76%)); added (not in the label): 10, of them lines across the lane 0, by the evidence the answer gave {'full': 9, 'partial': 1}; missed: 6
- Lane count: 18/38 (47%); position of my lane: 25/38 (66%)
- Unsafe errors (label prohibited, answer allowed): 6 {'change_right': 3, 'turn_left': 2, 'change_left': 1}; over-cautious: 8; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 34/42 (81%)
- Actions decided where the label has no governing marking: 7
- Answers that contradict themselves: 6 {'rightmost lane, but a lane line on the right': 3, 'u_turn decided without an arrow or prohibited-movement marking': 2, 'leftmost lane, but a lane line on the left': 1, 'turn_left, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 34, 'unlisted': 4}; IDs written with brackets (read without them): 39
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 309168, 'cached_input_tokens': 0, 'output_tokens': 33925}; cost about $0.0; latency: {'mean': 13.69, 'max': 31.84}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 31 |
| change_right | 21 | 14 |
| go_straight | 8 | 6 |
| turn_left | 8 | 4 |
| turn_right | 8 | 5 |
| u_turn | 7 | 3 |
