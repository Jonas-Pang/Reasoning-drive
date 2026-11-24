# Lane run 20261117_145105_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 37 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/37 (3%); without the lines across the lane: 3/37 (8%)
- Lane actions (every action the label decides, contested cells excluded): 17/29 (59%)
- Left boundary: 12/37 (32%); right boundary: 19/37 (51%); both: 10/37 (27%)
- Markings in the lane, exact set: 3/37 (8%) (without the lines across the lane 16/37 (43%)); added (not in the label): 33, of them lines across the lane 16, by the evidence the answer gave {'full': 18, 'partial': 14, 'insufficient': 1}; missed: 15
- Lane count: 6/19 (32%); position of my lane: 12/19 (63%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 1, 'go_straight': 1}; over-cautious: 8; contested unsafe: 28
- Prohibited actions also prohibited by the answer: 0/21 (0%)
- Actions decided where the label has no governing marking: 9
- Answers that contradict themselves: 32 {'leftmost lane, but a lane line on the left': 21, 'change_left allowed across a curb': 15, 'change_right prohibited across a broken lane line': 5, 'turn_right allowed': 3, 'change_right allowed across a curb': 1, 'change_left decided': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1, 'turn_right not_applicable': 1}
- Citations (Test B and C): {'unlisted': 37}; IDs written with brackets (read without them): 107
- Boundary evidence: {'same': 72, 'over_withholding': 2}
- Readable answers: 37/37 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 214563, 'cached_input_tokens': 0, 'output_tokens': 39934}; cost about $0.0; latency: {'mean': 7.29, 'max': 9.8}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 7 |
| change_right | 26 | 20 |
| go_straight | 8 | 7 |
| turn_left | 8 | 0 |
| turn_right | 8 | 0 |
| u_turn | 7 | 0 |
