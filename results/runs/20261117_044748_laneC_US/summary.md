# Lane run 20261117_044748_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 38 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/38 (0%); without the lines across the lane: 7/38 (18%)
- Lane actions (every action the label decides, contested cells excluded): 17/37 (46%)
- Left boundary: 15/37 (41%); right boundary: 16/37 (43%); both: 8/38 (21%)
- Markings in the lane, exact set: 4/37 (11%) (without the lines across the lane 22/37 (59%)); added (not in the label): 33, of them lines across the lane 20, by the evidence the answer gave {'full': 17, 'partial': 13, 'insufficient': 3}; missed: 14
- Lane count: 10/38 (26%); position of my lane: 17/38 (45%)
- Unsafe errors (label prohibited, answer allowed): 12 {'turn_right': 2, 'change_right': 6, 'change_left': 3, 'go_straight': 1}; over-cautious: 7; contested unsafe: 8
- Prohibited actions also prohibited by the answer: 19/42 (45%)
- Actions decided where the label has no governing marking: 18
- Answers that contradict themselves: 17 {'leftmost lane, but a lane line on the left': 7, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 4, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'change_left allowed across a curb': 2, 'change_left prohibited across a broken lane line': 1, 'change_right decided': 1, 'change_right allowed across a curb': 1, 'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 29, 'unlisted': 9}; IDs written with brackets (read without them): 108
- Boundary evidence: {'same': 72, 'unsupported_guess': 4}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 38
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 26 |
| change_right | 21 | 10 |
| go_straight | 8 | 7 |
| turn_left | 8 | 2 |
| turn_right | 8 | 2 |
| u_turn | 7 | 1 |
