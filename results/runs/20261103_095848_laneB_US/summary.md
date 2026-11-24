# Lane run 20261103_095848_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 17/38 (45%); without the lines across the lane: 21/38 (55%)
- Lane actions (every action the label decides, contested cells excluded): 28/36 (78%)
- Left boundary: 31/37 (84%); right boundary: 29/37 (78%); both: 25/38 (66%)
- Markings in the lane, exact set: 28/37 (76%) (without the lines across the lane 32/37 (86%)); added (not in the label): 17, of them lines across the lane 10, by the evidence the answer gave {'full': 8, 'partial': 9}; missed: 1
- Lane count: 22/38 (58%); position of my lane: 30/38 (79%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 1, 'change_right': 2}; over-cautious: 2; contested unsafe: 8
- Prohibited actions also prohibited by the answer: 27/36 (75%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'accepted': 36, 'in_pack_not_accepted': 2}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 66, 'over_withholding': 9, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 354616, 'cached_input_tokens': 303400, 'output_tokens': 39745}; cost about $0.5302; latency: {'mean': 22.91, 'max': 39.57}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 31 |
| change_right | 20 | 16 |
| go_straight | 6 | 5 |
| turn_left | 6 | 4 |
| turn_right | 6 | 4 |
| u_turn | 5 | 3 |
