# Lane run 20261116_005447_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 37/121 (31%); without the lines across the lane: 43/121 (36%)
- Lane actions (every action the label decides, contested cells excluded): 60/122 (49%)
- Left boundary: 69/121 (57%); right boundary: 81/118 (69%); both: 49/121 (40%)
- Markings in the lane, exact set: 89/118 (75%) (without the lines across the lane 101/118 (86%)); added (not in the label): 41, of them lines across the lane 24, by the evidence the answer gave {'partial': 23, 'full': 18}; missed: 2
- Lane count: 63/118 (53%); position of my lane: 78/119 (66%)
- Unsafe errors (label prohibited, answer allowed): 42 {'change_left': 18, 'change_right': 24}; over-cautious: 12; contested unsafe: 8
- Prohibited actions also prohibited by the answer: 85/136 (62%)
- Actions decided where the label has no governing marking: 27
- Answers that contradict themselves: 2 {'change_left not_determined': 1, 'change_left allowed across a curb': 1, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 123, 'none': 1}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 82, 'same': 157, 'other': 7, 'over_withholding': 2}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1434432, 'cached_input_tokens': 1074282, 'output_tokens': 130810}; cost about $2.1358; latency: {'mean': 19.95, 'max': 40.58}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 116 | 75 |
| change_right | 112 | 64 |
| go_straight | 24 | 23 |
| turn_left | 21 | 19 |
| turn_right | 20 | 18 |
| u_turn | 20 | 17 |
