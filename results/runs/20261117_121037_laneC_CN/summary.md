# Lane run 20261117_121037_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 11/25 (44%); without the lines across the lane: 11/25 (44%)
- Lane actions (every action the label decides, contested cells excluded): 13/21 (62%)
- Left boundary: 15/25 (60%); right boundary: 15/25 (60%); both: 12/25 (48%)
- Markings in the lane, exact set: 20/25 (80%) (without the lines across the lane 23/25 (92%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 6
- Lane count: 10/22 (45%); position of my lane: 9/22 (41%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 2, 'change_right': 2}; over-cautious: 4; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 23/27 (85%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 1 {'go_straight decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 24, 'unlisted': 1}; IDs written with brackets (read without them): 39
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 232850, 'cached_input_tokens': 0, 'output_tokens': 22519}; cost about $0.0; latency: {'mean': 14.62, 'max': 33.37}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 17 |
| change_right | 21 | 15 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
