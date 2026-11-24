# Lane run 20261116_004611_laneB_CN

Test B (image + the region's rule passages), region CN, 124 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 33/121 (27%); without the lines across the lane: 38/121 (31%)
- Lane actions (every action the label decides, contested cells excluded): 73/122 (60%)
- Left boundary: 68/121 (56%); right boundary: 77/118 (65%); both: 46/121 (38%)
- Markings in the lane, exact set: 87/118 (74%) (without the lines across the lane 98/118 (83%)); added (not in the label): 46, of them lines across the lane 26, by the evidence the answer gave {'full': 23, 'partial': 23}; missed: 2
- Lane count: 62/118 (53%); position of my lane: 72/119 (61%)
- Unsafe errors (label prohibited, answer allowed): 12 {'change_left': 8, 'change_right': 4}; over-cautious: 21; contested unsafe: 4
- Prohibited actions also prohibited by the answer: 118/136 (87%)
- Actions decided where the label has no governing marking: 45
- Answers that contradict themselves: 4 {'turn_left, u_turn decided without an arrow or prohibited-movement marking': 3, 'change_right not_determined': 1, 'change_left not_determined': 1}
- Citations (Test B and C): {'accepted': 113, 'none_needed': 1, 'in_pack_not_accepted': 10}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 148, 'unsupported_guess': 90, 'other': 5, 'over_withholding': 5}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1334984, 'cached_input_tokens': 975636, 'output_tokens': 127290}; cost about $2.0892; latency: {'mean': 18.4, 'max': 35.46}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 116 | 84 |
| change_right | 112 | 78 |
| go_straight | 24 | 23 |
| turn_left | 21 | 19 |
| turn_right | 20 | 18 |
| u_turn | 20 | 17 |
