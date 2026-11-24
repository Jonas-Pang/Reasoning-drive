# Lane run 20261117_044418_laneB_UK

Test B (image + the region's rule passages), region UK, 11 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/11 (0%); without the lines across the lane: 0/11 (0%)
- Lane actions (every action the label decides, contested cells excluded): 0/11 (0%)
- Left boundary: 2/11 (18%); right boundary: 0/10 (0%); both: 0/11 (0%)
- Markings in the lane, exact set: 1/11 (9%) (without the lines across the lane 5/11 (45%)); added (not in the label): 10, of them lines across the lane 4, by the evidence the answer gave {'insufficient': 3, 'full': 7}; missed: 1
- Lane count: 0/9 (0%); position of my lane: 2/9 (22%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 8; contested unsafe: 1
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 2 {'leftmost lane, but a lane line on the left': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {'unlisted': 1, 'in_pack_not_accepted': 7, 'accepted': 3}; IDs written with brackets (read without them): 1
- Boundary evidence: {'same': 18, 'unsupported_guess': 4}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 150084, 'cached_input_tokens': 0, 'output_tokens': 7687}; cost about $0.0; latency: {'mean': 9.3, 'max': 15.31}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 11 | 0 |
