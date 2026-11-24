# Lane run 20261117_230252_laneB_IN

Test B (image + the region's rule passages), region IN, 9 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/9 (0%); without the lines across the lane: 0/9 (0%)
- Lane actions (every action the label decides, contested cells excluded): 2/6 (33%)
- Left boundary: 2/9 (22%); right boundary: 4/8 (50%); both: 0/9 (0%)
- Markings in the lane, exact set: 1/9 (11%) (without the lines across the lane 7/9 (78%)); added (not in the label): 8, of them lines across the lane 6, by the evidence the answer gave {'full': 4, 'insufficient': 4}; missed: 0
- Lane count: 1/5 (20%); position of my lane: 2/5 (40%)
- Unsafe errors (label prohibited, answer allowed): 4 {'change_left': 4}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 2/6 (33%)
- Actions decided where the label has no governing marking: 5
- Answers that contradict themselves: 3 {'change_left decided': 2, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {'unlisted': 6, 'none_needed': 3}; IDs written with brackets (read without them): 9
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 59877, 'cached_input_tokens': 0, 'output_tokens': 7262}; cost about $0.0; latency: {'mean': 9.52, 'max': 13.01}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 2 |
| change_right | 4 | 3 |
