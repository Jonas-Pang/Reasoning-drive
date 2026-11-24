# Lane run 20261117_020201_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 25 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/25 (0%); without the lines across the lane: 3/25 (12%)
- Lane actions (every action the label decides, contested cells excluded): 4/21 (19%)
- Left boundary: 11/25 (44%); right boundary: 10/25 (40%); both: 6/25 (24%)
- Markings in the lane, exact set: 1/25 (4%) (without the lines across the lane 15/25 (60%)); added (not in the label): 23, of them lines across the lane 15, by the evidence the answer gave {'insufficient': 6, 'full': 7, 'partial': 10}; missed: 8
- Lane count: 10/22 (45%); position of my lane: 6/22 (27%)
- Unsafe errors (label prohibited, answer allowed): 8 {'change_left': 4, 'change_right': 4}; over-cautious: 13; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 10/27 (37%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 4 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'change_left allowed across a curb': 1, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 19, 'unlisted': 6}; IDs written with brackets (read without them): 74
- Boundary evidence: {'same': 38, 'unsupported_guess': 11, 'over_withholding': 1}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 215600, 'cached_input_tokens': 0, 'output_tokens': 27865}; cost about $0.0; latency: {'mean': 20.45, 'max': 28.15}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 10 |
| change_right | 21 | 8 |
| go_straight | 3 | 3 |
| turn_left | 3 | 0 |
| turn_right | 3 | 0 |
| u_turn | 3 | 0 |
