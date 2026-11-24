# Lane run 20261116_132837_laneR_CN

Test R (image + the passages about the elements of the model's own Test A answer), region CN, 25 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 13/25 (52%); without the lines across the lane: 16/25 (64%)
- Lane actions (every action the label decides, contested cells excluded): 18/22 (82%)
- Left boundary: 18/25 (72%); right boundary: 23/25 (92%); both: 17/25 (68%)
- Markings in the lane, exact set: 20/25 (80%) (without the lines across the lane 23/25 (92%)); added (not in the label): 6, of them lines across the lane 4, by the evidence the answer gave {'partial': 1, 'full': 5}; missed: 0
- Lane count: 16/22 (73%); position of my lane: 18/22 (82%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 26/26 (100%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'over_withholding': 3, 'same': 37, 'unsupported_guess': 10}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 25
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 22 | 21 |
| change_right | 22 | 19 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
