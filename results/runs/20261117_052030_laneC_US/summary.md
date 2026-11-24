# Lane run 20261117_052030_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 108 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 2/104 (2%); without the lines across the lane: 15/104 (14%)
- Lane actions (every action the label decides, contested cells excluded): 43/102 (42%)
- Left boundary: 49/103 (48%); right boundary: 46/102 (45%); both: 24/103 (23%)
- Markings in the lane, exact set: 11/101 (11%) (without the lines across the lane 61/101 (60%)); added (not in the label): 86, of them lines across the lane 48, by the evidence the answer gave {'partial': 36, 'insufficient': 23, 'full': 27}; missed: 15
- Lane count: 39/101 (39%); position of my lane: 43/103 (42%)
- Unsafe errors (label prohibited, answer allowed): 21 {'change_left': 17, 'turn_right': 1, 'go_straight': 2, 'change_right': 1}; over-cautious: 30; contested unsafe: 29
- Prohibited actions also prohibited by the answer: 32/72 (44%)
- Actions decided where the label has no governing marking: 34
- Answers that contradict themselves: 34 {'leftmost lane, but a lane line on the left': 11, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 8, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 6, 'change_right allowed across a curb': 3, 'change_left prohibited across a broken lane line': 2, 'change_left allowed across a curb': 2, 'u_turn decided without an arrow or prohibited-movement marking': 1, 'turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 73, 'unlisted': 35}; IDs written with brackets (read without them): 306
- Boundary evidence: {'same': 161, 'unsupported_guess': 50, 'over_withholding': 5}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 820476, 'cached_input_tokens': 0, 'output_tokens': 113541}; cost about $0.0; latency: {'mean': 6.86, 'max': 9.57}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 56 |
| change_right | 54 | 30 |
| go_straight | 10 | 8 |
| turn_left | 10 | 3 |
| turn_right | 11 | 3 |
| u_turn | 9 | 3 |
