# Lane run 20261118_013556_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 7/25 (28%); without the lines across the lane: 7/25 (28%)
- Lane actions (every action the label decides, contested cells excluded): 15/21 (71%)
- Left boundary: 13/25 (52%); right boundary: 15/25 (60%); both: 9/25 (36%)
- Markings in the lane, exact set: 20/25 (80%) (without the lines across the lane 23/25 (92%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 6
- Lane count: 10/22 (45%); position of my lane: 11/22 (50%)
- Unsafe errors (label prohibited, answer allowed): 7 {'change_right': 3, 'change_left': 4}; over-cautious: 1; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 21/28 (75%)
- Actions decided where the label has no governing marking: 2
- Answers that contradict themselves: 1 {'change_right allowed across a curb': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 3, 'accepted': 20, 'unlisted': 2}; IDs written with brackets (read without them): 20
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 211450, 'cached_input_tokens': 0, 'output_tokens': 21687}; cost about $0.0; latency: {'mean': 18.76, 'max': 45.04}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 16 |
| change_right | 21 | 18 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
