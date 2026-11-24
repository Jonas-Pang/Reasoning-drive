# Lane run 20261117_023728_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 38 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 9/38 (24%); without the lines across the lane: 10/38 (26%)
- Lane actions (every action the label decides, contested cells excluded): 21/37 (57%)
- Left boundary: 23/37 (62%); right boundary: 19/37 (51%); both: 12/38 (32%)
- Markings in the lane, exact set: 29/37 (78%) (without the lines across the lane 31/37 (84%)); added (not in the label): 4, of them lines across the lane 0, by the evidence the answer gave {'full': 4}; missed: 7
- Lane count: 19/38 (50%); position of my lane: 26/38 (68%)
- Unsafe errors (label prohibited, answer allowed): 8 {'change_right': 2, 'change_left': 4, 'go_straight': 1, 'turn_left': 1}; over-cautious: 8; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 31/42 (74%)
- Actions decided where the label has no governing marking: 9
- Answers that contradict themselves: 8 {'u_turn decided without an arrow or prohibited-movement marking': 5, 'rightmost lane, but a lane line on the right': 3, 'change_right decided': 1, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 35, 'unlisted': 3}; IDs written with brackets (read without them): 42
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 288838, 'cached_input_tokens': 0, 'output_tokens': 27214}; cost about $0.0; latency: {'mean': 39.42, 'max': 57.72}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 27 |
| change_right | 21 | 13 |
| go_straight | 8 | 7 |
| turn_left | 8 | 4 |
| turn_right | 8 | 4 |
| u_turn | 7 | 4 |
