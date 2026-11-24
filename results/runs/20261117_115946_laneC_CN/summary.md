# Lane run 20261117_115946_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 25 images, one request each, model llama4:scout

- Lane identified (both boundaries and the markings): 3/25 (12%); without the lines across the lane: 4/25 (16%)
- Lane actions (every action the label decides, contested cells excluded): 6/21 (29%)
- Left boundary: 10/25 (40%); right boundary: 6/25 (24%); both: 5/25 (20%)
- Markings in the lane, exact set: 19/25 (76%) (without the lines across the lane 21/25 (84%)); added (not in the label): 3, of them lines across the lane 0, by the evidence the answer gave {'full': 3}; missed: 8
- Lane count: 7/22 (32%); position of my lane: 4/22 (18%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 19; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 18/27 (67%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'in_pack_not_accepted': 25}; IDs written with brackets (read without them): 55
- Boundary evidence: {'same': 37, 'unsupported_guess': 11, 'over_withholding': 2}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 232550, 'cached_input_tokens': 0, 'output_tokens': 15175}; cost about $0.0; latency: {'mean': 15.43, 'max': 28.99}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 13 |
| change_right | 21 | 8 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
