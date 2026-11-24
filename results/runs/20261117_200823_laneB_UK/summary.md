# Lane run 20261117_200823_laneB_UK

Test B (image + the region's rule passages), region UK, 48 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 0/48 (0%); without the lines across the lane: 0/48 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/39 (3%)
- Left boundary: 1/48 (2%); right boundary: 3/47 (6%); both: 1/48 (2%)
- Markings in the lane, exact set: 2/48 (4%) (without the lines across the lane 2/48 (4%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 1
- Lane count: 2/28 (7%); position of my lane: 2/28 (7%)
- Unsafe errors (label prohibited, answer allowed): 1 {'u_turn': 1}; over-cautious: 1; contested unsafe: 2
- Prohibited actions also prohibited by the answer: 1/21 (5%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 2 {'rightmost lane, but a lane line on the right': 2, 'leftmost lane, but a lane line on the left': 1}
- Citations (Test B and C): {'accepted': 2, 'unlisted': 1, 'no_answer': 45}; IDs written with brackets (read without them): 5
- Boundary evidence: {'same': 5, 'unsupported_guess': 1, 'other': 90}
- Readable answers: 3/48 (an unreadable or failed answer counts as wrong); errors: 45; from cache: 0
- Tokens: {'input_tokens': 44262, 'cached_input_tokens': 0, 'output_tokens': 2711}; cost about $0.0; latency: {'mean': 40.21, 'max': 45.16}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 0 |
| change_right | 36 | 2 |
| go_straight | 8 | 0 |
| turn_left | 8 | 1 |
| turn_right | 8 | 1 |
| u_turn | 8 | 0 |
