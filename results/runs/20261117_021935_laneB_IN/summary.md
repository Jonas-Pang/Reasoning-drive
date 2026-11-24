# Lane run 20261117_021935_laneB_IN

Test B (image + the region's rule passages), region IN, 4 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/4 (0%); without the lines across the lane: 0/4 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/2 (50%)
- Left boundary: 0/4 (0%); right boundary: 0/4 (0%); both: 0/4 (0%)
- Markings in the lane, exact set: 0/4 (0%) (without the lines across the lane 3/4 (75%)); added (not in the label): 12, of them lines across the lane 6, by the evidence the answer gave {'full': 1, 'insufficient': 11}; missed: 0
- Lane count: 1/2 (50%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 1/2 (50%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 3 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'leftmost lane, but a lane line on the left': 1, 'change_left allowed across a curb': 1, 'change_right allowed across a curb': 1, 'go_straight decided from an arrow that cannot be read': 1}
- Citations (Test B and C): {'unlisted': 4}; IDs written with brackets (read without them): 5
- Boundary evidence: {'same': 4, 'unsupported_guess': 4}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 23140, 'cached_input_tokens': 0, 'output_tokens': 2971}; cost about $0.0; latency: {'mean': 17.62, 'max': 21.23}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 1 |
