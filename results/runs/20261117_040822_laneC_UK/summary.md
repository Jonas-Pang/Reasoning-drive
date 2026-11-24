# Lane run 20261117_040822_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 5 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/5 (0%); without the lines across the lane: 0/5 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/3 (33%)
- Left boundary: 0/5 (0%); right boundary: 0/4 (0%); both: 0/5 (0%)
- Markings in the lane, exact set: 1/5 (20%) (without the lines across the lane 4/5 (80%)); added (not in the label): 5, of them lines across the lane 4, by the evidence the answer gave {'full': 2, 'insufficient': 2, 'partial': 1}; missed: 1
- Lane count: 1/5 (20%); position of my lane: 3/5 (60%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 3 {'change_right allowed across a curb': 1, 'go_straight decided from an arrow that cannot be read': 1, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {'unlisted': 4, 'none_needed': 1}; IDs written with brackets (read without them): 8
- Boundary evidence: {'unsupported_guess': 4, 'same': 6}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 5
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 1 |
