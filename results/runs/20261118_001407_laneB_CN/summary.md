# Lane run 20261118_001407_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model gemma-4-31b-it

- Lane identified (both boundaries and the markings): 7/25 (28%); without the lines across the lane: 7/25 (28%)
- Lane actions (every action the label decides, contested cells excluded): 16/21 (76%)
- Left boundary: 13/25 (52%); right boundary: 14/25 (56%); both: 8/25 (32%)
- Markings in the lane, exact set: 19/25 (76%) (without the lines across the lane 23/25 (92%)); added (not in the label): 1, of them lines across the lane 1, by the evidence the answer gave {'full': 1}; missed: 6
- Lane count: 10/22 (45%); position of my lane: 11/22 (50%)
- Unsafe errors (label prohibited, answer allowed): 5 {'change_left': 3, 'change_right': 2}; over-cautious: 2; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 23/28 (82%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 1 {'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 4, 'accepted': 19, 'unlisted': 2}; IDs written with brackets (read without them): 34
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 211475, 'cached_input_tokens': 0, 'output_tokens': 20613}; cost about $0.0; latency: {'mean': 10.34, 'max': 22.21}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 16 |
| change_right | 21 | 19 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
