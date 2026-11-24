# Lane run 20261115_230052_laneA_CN

Test A (image only), region CN, 25 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 12/25 (48%); without the lines across the lane: 14/25 (56%)
- Lane actions (every action the label decides, contested cells excluded): 18/22 (82%)
- Left boundary: 18/25 (72%); right boundary: 20/25 (80%); both: 15/25 (60%)
- Markings in the lane, exact set: 19/25 (76%) (without the lines across the lane 22/25 (88%)); added (not in the label): 7, of them lines across the lane 4, by the evidence the answer gave {'partial': 2, 'full': 5}; missed: 0
- Lane count: 15/22 (68%); position of my lane: 18/22 (82%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 26/26 (100%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 11, 'same': 39}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 159900, 'cached_input_tokens': 81926, 'output_tokens': 24195}; cost about $0.4061; latency: {'mean': 20.32, 'max': 30.85}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 22 | 21 |
| change_right | 22 | 19 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
