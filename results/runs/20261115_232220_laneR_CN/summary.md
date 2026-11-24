# Lane run 20261115_232220_laneR_CN

Test R (image + the passages about the elements of the model's own Test A answer), region CN, 25 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 6/25 (24%); without the lines across the lane: 8/25 (32%)
- Lane actions (every action the label decides, contested cells excluded): 9/22 (41%)
- Left boundary: 10/25 (40%); right boundary: 12/25 (48%); both: 9/25 (36%)
- Markings in the lane, exact set: 11/25 (44%) (without the lines across the lane 13/25 (52%)); added (not in the label): 4, of them lines across the lane 3, by the evidence the answer gave {'partial': 1, 'full': 3}; missed: 0
- Lane count: 9/22 (41%); position of my lane: 9/22 (41%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 17/26 (65%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 21, 'unsupported_guess': 5, 'over_withholding': 2, 'other': 22}
- Readable answers: 14/25 (an unreadable or failed answer counts as wrong); errors: 11; from cache: 0
- Tokens: {'input_tokens': 121979, 'cached_input_tokens': 30354, 'output_tokens': 14389}; cost about $0.3302; latency: {'mean': 20.43, 'max': 29.46}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 22 | 11 |
| change_right | 22 | 10 |
| go_straight | 3 | 2 |
| turn_left | 3 | 2 |
| turn_right | 3 | 2 |
| u_turn | 3 | 2 |
