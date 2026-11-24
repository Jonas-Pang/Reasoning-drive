# Lane run 20261117_235806_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model meta-muse-glimmer-30b

- Lane identified (both boundaries and the markings): 5/25 (20%); without the lines across the lane: 6/25 (24%)
- Lane actions (every action the label decides, contested cells excluded): 11/21 (52%)
- Left boundary: 13/25 (52%); right boundary: 10/25 (40%); both: 8/25 (32%)
- Markings in the lane, exact set: 16/25 (64%) (without the lines across the lane 19/25 (76%)); added (not in the label): 6, of them lines across the lane 1, by the evidence the answer gave {'partial': 3, 'full': 3}; missed: 8
- Lane count: 14/22 (64%); position of my lane: 16/22 (73%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 2, 'turn_right': 1}; over-cautious: 12; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 25/28 (89%)
- Actions decided where the label has no governing marking: 11
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'no_answer': 1, 'in_pack_not_accepted': 6, 'accepted': 18}; IDs written with brackets (read without them): 8
- Boundary evidence: {'other': 2, 'unsupported_guess': 9, 'same': 27, 'over_withholding': 12}
- Readable answers: 24/25 (an unreadable or failed answer counts as wrong); errors: 1; from cache: 0
- Tokens: {'input_tokens': 271680, 'cached_input_tokens': 0, 'output_tokens': 104376}; cost about $0.0; latency: {'mean': 28.93, 'max': 40.95}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 17 |
| change_right | 21 | 12 |
| go_straight | 3 | 2 |
| turn_left | 3 | 3 |
| turn_right | 3 | 2 |
| u_turn | 3 | 3 |
