# Lane run 20261117_044703_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 9 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/9 (0%); without the lines across the lane: 0/9 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/6 (17%)
- Left boundary: 2/9 (22%); right boundary: 2/8 (25%); both: 0/9 (0%)
- Markings in the lane, exact set: 2/9 (22%) (without the lines across the lane 9/9 (100%)); added (not in the label): 8, of them lines across the lane 8, by the evidence the answer gave {'full': 4, 'insufficient': 4}; missed: 0
- Lane count: 1/5 (20%); position of my lane: 1/5 (20%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_left': 3}; over-cautious: 4; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 1/4 (25%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 4 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'leftmost lane, but a lane line on the left': 2}
- Citations (Test B and C): {'in_pack_not_accepted': 9}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 11, 'unsupported_guess': 7}
- Readable answers: 9/9 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 122697, 'cached_input_tokens': 0, 'output_tokens': 6111}; cost about $0.0; latency: {'mean': 9.74, 'max': 15.97}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 6 | 1 |
| change_right | 5 | 0 |
