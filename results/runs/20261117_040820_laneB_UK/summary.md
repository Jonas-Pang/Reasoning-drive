# Lane run 20261117_040820_laneB_UK

Test B (image + the region's rule passages), region UK, 5 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/5 (0%); without the lines across the lane: 0/5 (0%)
- Lane actions (every action the label decides, contested cells excluded): 0/3 (0%)
- Left boundary: 0/5 (0%); right boundary: 0/4 (0%); both: 0/5 (0%)
- Markings in the lane, exact set: 1/5 (20%) (without the lines across the lane 3/5 (60%)); added (not in the label): 4, of them lines across the lane 2, by the evidence the answer gave {'full': 4}; missed: 0
- Lane count: 2/5 (40%); position of my lane: 2/5 (40%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 0
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 1 {'change_right decided': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 3, 'accepted': 2}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 6, 'unsupported_guess': 4}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 5
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 0 |
