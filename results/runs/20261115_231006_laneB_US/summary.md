# Lane run 20261115_231006_laneB_US

Test B (image + the region's rule passages), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 18/38 (47%); without the lines across the lane: 21/38 (55%)
- Lane actions (every action the label decides, contested cells excluded): 33/36 (92%)
- Left boundary: 31/37 (84%); right boundary: 31/37 (84%); both: 26/38 (68%)
- Markings in the lane, exact set: 28/37 (76%) (without the lines across the lane 32/37 (86%)); added (not in the label): 15, of them lines across the lane 9, by the evidence the answer gave {'full': 6, 'partial': 9}; missed: 1
- Lane count: 20/38 (53%); position of my lane: 30/38 (79%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_right': 1}; over-cautious: 2; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 36/38 (95%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 1 {'change_right not_determined': 1}
- Citations (Test B and C): {'accepted': 37, 'in_pack_not_accepted': 1}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 64, 'other': 2, 'over_withholding': 8, 'unsupported_guess': 2}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 374908, 'cached_input_tokens': 331892, 'output_tokens': 38817}; cost about $0.5074; latency: {'mean': 21.34, 'max': 35.67}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 32 | 32 |
| change_right | 20 | 18 |
| go_straight | 7 | 6 |
| turn_left | 7 | 7 |
| turn_right | 7 | 6 |
| u_turn | 6 | 6 |
