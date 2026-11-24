# Lane run 20261117_144833_laneB_UK

Test B (image + the region's rule passages), region UK, 37 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 1/37 (3%); without the lines across the lane: 3/37 (8%)
- Lane actions (every action the label decides, contested cells excluded): 12/29 (41%)
- Left boundary: 10/37 (27%); right boundary: 16/37 (43%); both: 6/37 (16%)
- Markings in the lane, exact set: 2/37 (5%) (without the lines across the lane 15/37 (41%)); added (not in the label): 29, of them lines across the lane 14, by the evidence the answer gave {'partial': 10, 'full': 15, 'insufficient': 4}; missed: 14
- Lane count: 7/19 (37%); position of my lane: 12/19 (63%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_right': 1}; over-cautious: 10; contested unsafe: 21
- Prohibited actions also prohibited by the answer: 0/21 (0%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 23 {'leftmost lane, but a lane line on the left': 18, 'change_left allowed across a curb': 4, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 4, 'change_right prohibited across a broken lane line': 2}
- Citations (Test B and C): {'in_pack_not_accepted': 9, 'accepted': 20, 'unlisted': 5, 'no_answer': 3}; IDs written with brackets (read without them): 103
- Boundary evidence: {'same': 68, 'other': 6}
- Readable answers: 34/37 (an unreadable or failed answer counts as wrong); errors: 3; from cache: 33
- Tokens: {'input_tokens': 13887, 'cached_input_tokens': 0, 'output_tokens': 1014}; cost about $0.0; latency: {'mean': 31.27, 'max': 31.27}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 10 | 5 |
| change_right | 26 | 16 |
| go_straight | 8 | 7 |
| turn_left | 8 | 0 |
| turn_right | 8 | 0 |
| u_turn | 7 | 0 |
