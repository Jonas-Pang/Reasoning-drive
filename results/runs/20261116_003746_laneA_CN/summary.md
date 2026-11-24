# Lane run 20261116_003746_laneA_CN

Test A (image only), region CN, 124 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 36/121 (30%); without the lines across the lane: 41/121 (34%)
- Lane actions (every action the label decides, contested cells excluded): 72/122 (59%)
- Left boundary: 70/121 (58%); right boundary: 78/118 (66%); both: 47/121 (39%)
- Markings in the lane, exact set: 86/118 (73%) (without the lines across the lane 98/118 (83%)); added (not in the label): 47, of them lines across the lane 27, by the evidence the answer gave {'full': 22, 'partial': 24, 'insufficient': 1}; missed: 2
- Lane count: 65/118 (55%); position of my lane: 75/119 (63%)
- Unsafe errors (label prohibited, answer allowed): 10 {'change_left': 6, 'change_right': 4}; over-cautious: 22; contested unsafe: 4
- Prohibited actions also prohibited by the answer: 122/136 (90%)
- Actions decided where the label has no governing marking: 36
- Answers that contradict themselves: 1 {'change_right not_determined': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'over_withholding': 2, 'same': 152, 'unsupported_guess': 90, 'other': 4}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 793104, 'cached_input_tokens': 438126, 'output_tokens': 121870}; cost about $1.9725; latency: {'mean': 18.34, 'max': 33.35}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 116 | 85 |
| change_right | 112 | 77 |
| go_straight | 24 | 23 |
| turn_left | 21 | 20 |
| turn_right | 20 | 19 |
| u_turn | 20 | 18 |
