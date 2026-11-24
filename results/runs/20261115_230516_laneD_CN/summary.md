# Lane run 20261115_230516_laneD_CN

Test D (image only, country not given), region CN, 25 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 13/25 (52%); without the lines across the lane: 16/25 (64%)
- Lane actions (every action the label decides, contested cells excluded): 18/22 (82%)
- Left boundary: 18/25 (72%); right boundary: 22/25 (88%); both: 17/25 (68%)
- Markings in the lane, exact set: 18/25 (72%) (without the lines across the lane 21/25 (84%)); added (not in the label): 9, of them lines across the lane 4, by the evidence the answer gave {'partial': 3, 'full': 6}; missed: 0
- Lane count: 14/22 (64%); position of my lane: 16/22 (73%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 26/26 (100%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 1 {'change_right prohibited': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 40, 'unsupported_guess': 9, 'over_withholding': 1}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 160600, 'cached_input_tokens': 89050, 'output_tokens': 25524}; cost about $0.4072; latency: {'mean': 21.73, 'max': 37.05}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 22 | 21 |
| change_right | 22 | 19 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
