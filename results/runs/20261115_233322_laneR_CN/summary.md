# Lane run 20261115_233322_laneR_CN

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
- Boundary evidence: {'unsupported_guess': 10, 'same': 37, 'over_withholding': 3}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 14
- Tokens: {'input_tokens': 95431, 'cached_input_tokens': 47994, 'output_tokens': 11061}; cost about $0.2103; latency: {'mean': 18.77, 'max': 31.75}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 22 | 21 |
| change_right | 22 | 19 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
