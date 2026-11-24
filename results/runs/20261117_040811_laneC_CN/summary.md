# Lane run 20261117_040811_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 25 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/25 (0%); without the lines across the lane: 2/25 (8%)
- Lane actions (every action the label decides, contested cells excluded): 5/21 (24%)
- Left boundary: 8/25 (32%); right boundary: 5/25 (20%); both: 3/25 (12%)
- Markings in the lane, exact set: 2/25 (8%) (without the lines across the lane 12/25 (48%)); added (not in the label): 43, of them lines across the lane 12, by the evidence the answer gave {'full': 40, 'insufficient': 2, 'partial': 1}; missed: 7
- Lane count: 10/22 (45%); position of my lane: 7/22 (32%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_left': 2}; over-cautious: 19; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 16/27 (59%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 1 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 24, 'unlisted': 1}; IDs written with brackets (read without them): 4
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 25
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 11 |
| change_right | 21 | 8 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
