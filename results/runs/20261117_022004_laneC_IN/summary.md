# Lane run 20261117_022004_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 4 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/4 (0%); without the lines across the lane: 0/4 (0%)
- Lane actions (every action the label decides, contested cells excluded): 2/2 (100%)
- Left boundary: 2/4 (50%); right boundary: 0/4 (0%); both: 0/4 (0%)
- Markings in the lane, exact set: 0/4 (0%) (without the lines across the lane 4/4 (100%)); added (not in the label): 4, of them lines across the lane 4, by the evidence the answer gave {'full': 3, 'insufficient': 1}; missed: 0
- Lane count: 0/2 (0%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 2/2 (100%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 3 {'leftmost lane, but a lane line on the left': 2, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 4}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 4, 'unsupported_guess': 4}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 54532, 'cached_input_tokens': 0, 'output_tokens': 2612}; cost about $0.0; latency: {'mean': 22.41, 'max': 27.98}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 2 |
