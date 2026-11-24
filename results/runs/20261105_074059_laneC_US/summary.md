# Lane run 20261105_074059_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 21/38 (55%); without the lines across the lane: 24/38 (63%)
- Lane actions (every action the label decides, contested cells excluded): 29/36 (81%)
- Left boundary: 33/37 (89%); right boundary: 31/37 (84%); both: 28/38 (74%)
- Markings in the lane, exact set: 29/37 (78%) (without the lines across the lane 32/37 (86%)); added (not in the label): 14, of them lines across the lane 8, by the evidence the answer gave {'partial': 9, 'full': 5}; missed: 1
- Lane count: 20/38 (53%); position of my lane: 29/38 (76%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_left': 1, 'change_right': 1}; over-cautious: 4; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 29/36 (81%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'in_pack_not_accepted': 38}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 64, 'over_withholding': 11, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 323950, 'cached_input_tokens': 273541, 'output_tokens': 39332}; cost about $0.5215; latency: {'mean': 20.29, 'max': 37.75}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 32 |
| change_right | 20 | 17 |
| go_straight | 6 | 3 |
| turn_left | 6 | 4 |
| turn_right | 6 | 4 |
| u_turn | 5 | 4 |
