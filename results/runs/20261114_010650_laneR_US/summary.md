# Lane run 20261114_010650_laneR_US

Test R (image + the passages about the elements of the model's own Test A answer), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 12/38 (32%); without the lines across the lane: 16/38 (42%)
- Lane actions (every action the label decides, contested cells excluded): 19/36 (53%)
- Left boundary: 22/37 (59%); right boundary: 23/37 (62%); both: 19/38 (50%)
- Markings in the lane, exact set: 20/37 (54%) (without the lines across the lane 24/37 (65%)); added (not in the label): 13, of them lines across the lane 8, by the evidence the answer gave {'partial': 9, 'full': 4}; missed: 1
- Lane count: 16/38 (42%); position of my lane: 22/38 (58%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 2, 'change_right': 2}; over-cautious: 3; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 23/36 (64%)
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 48, 'over_withholding': 9, 'other': 19}
- Readable answers: 29/38 (an unreadable or failed answer counts as wrong); errors: 9; from cache: 0
- Tokens: {'input_tokens': 183445, 'cached_input_tokens': 45454, 'output_tokens': 30293}; cost about $0.5835; latency: {'mean': 17.64, 'max': 32.5}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 33 | 22 |
| change_right | 20 | 13 |
| go_straight | 6 | 4 |
| turn_left | 6 | 4 |
| turn_right | 6 | 4 |
| u_turn | 5 | 3 |
