# Lane run 20261117_044628_laneB_IN

Test B (image + the region's rule passages), region IN, 9 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/9 (0%); without the lines across the lane: 1/9 (11%)
- Lane actions (every action the label decides, contested cells excluded): 0/6 (0%)
- Left boundary: 4/9 (44%); right boundary: 1/8 (12%); both: 1/9 (11%)
- Markings in the lane, exact set: 2/9 (22%) (without the lines across the lane 7/9 (78%)); added (not in the label): 31, of them lines across the lane 10, by the evidence the answer gave {'full': 2, 'insufficient': 29}; missed: 0
- Lane count: 1/5 (20%); position of my lane: 1/5 (20%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 3; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 2/4 (50%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 6 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 4, 'u_turn decided without an arrow or prohibited-movement marking': 2, 'change_right allowed across a curb': 1, 'go_straight decided from an arrow that cannot be read': 1, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {'unlisted': 9}; IDs written with brackets (read without them): 16
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 52065, 'cached_input_tokens': 0, 'output_tokens': 6371}; cost about $0.0; latency: {'mean': 7.7, 'max': 10.34}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 2 |
| change_right | 5 | 1 |
