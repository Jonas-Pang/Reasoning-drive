# Lane run 20261116_010353_laneD_CN

Test D (image only, country not given), region CN, 124 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 36/121 (30%); without the lines across the lane: 40/121 (33%)
- Lane actions (every action the label decides, contested cells excluded): 67/122 (55%)
- Left boundary: 68/121 (56%); right boundary: 78/118 (66%); both: 45/121 (37%)
- Markings in the lane, exact set: 88/118 (75%) (without the lines across the lane 99/118 (84%)); added (not in the label): 44, of them lines across the lane 25, by the evidence the answer gave {'partial': 24, 'full': 20}; missed: 2
- Lane count: 71/118 (60%); position of my lane: 74/119 (62%)
- Unsafe errors (label prohibited, answer allowed): 12 {'change_right': 5, 'change_left': 7}; over-cautious: 23; contested unsafe: 3
- Prohibited actions also prohibited by the answer: 116/136 (85%)
- Actions decided where the label has no governing marking: 33
- Answers that contradict themselves: 2 {'change_left not_determined': 2, 'change_right not_determined': 2}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 149, 'unsupported_guess': 90, 'over_withholding': 5, 'other': 4}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 796576, 'cached_input_tokens': 441688, 'output_tokens': 126613}; cost about $2.0201; latency: {'mean': 17.7, 'max': 43.83}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 116 | 83 |
| change_right | 112 | 74 |
| go_straight | 24 | 23 |
| turn_left | 21 | 19 |
| turn_right | 20 | 18 |
| u_turn | 20 | 17 |
