# Lane run 20261117_172755_laneB_CN

Test B (image + the region's rule passages), region CN, 25 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 4/25 (16%); without the lines across the lane: 4/25 (16%)
- Lane actions (every action the label decides, contested cells excluded): 12/21 (57%)
- Left boundary: 12/25 (48%); right boundary: 10/25 (40%); both: 4/25 (16%)
- Markings in the lane, exact set: 20/25 (80%) (without the lines across the lane 23/25 (92%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 5
- Lane count: 8/22 (36%); position of my lane: 10/22 (45%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 4}; over-cautious: 5; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 23/27 (85%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 3 {'leftmost lane, but a lane line on the left': 2, 'u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 4, 'accepted': 20, 'unlisted': 1}; IDs written with brackets (read without them): 18
- Boundary evidence: {'same': 39, 'unsupported_guess': 11}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 226325, 'cached_input_tokens': 0, 'output_tokens': 23107}; cost about $0.0; latency: {'mean': 22.46, 'max': 52.8}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 21 | 16 |
| change_right | 21 | 15 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
