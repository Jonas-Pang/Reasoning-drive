# Lane run 20261117_052701_laneB_UK

Test B (image + the region's rule passages), region UK, 11 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/11 (0%); without the lines across the lane: 1/11 (9%)
- Lane actions (every action the label decides, contested cells excluded): 6/11 (55%)
- Left boundary: 1/11 (9%); right boundary: 8/10 (80%); both: 1/11 (9%)
- Markings in the lane, exact set: 1/11 (9%) (without the lines across the lane 7/11 (64%)); added (not in the label): 11, of them lines across the lane 6, by the evidence the answer gave {'partial': 5, 'insufficient': 3, 'full': 3}; missed: 1
- Lane count: 1/9 (11%); position of my lane: 7/9 (78%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 2; contested unsafe: 6
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 7 {'leftmost lane, but a lane line on the left': 6, 'change_left allowed across a curb': 1, 'change_right prohibited across a broken lane line': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {'unlisted': 5, 'in_pack_not_accepted': 4, 'accepted': 2}; IDs written with brackets (read without them): 31
- Boundary evidence: {'same': 18, 'unsupported_guess': 4}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 150040, 'cached_input_tokens': 0, 'output_tokens': 11621}; cost about $0.0; latency: {'mean': 8.17, 'max': 11.41}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 11 | 6 |
