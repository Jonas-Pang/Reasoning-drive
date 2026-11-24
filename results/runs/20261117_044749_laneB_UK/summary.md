# Lane run 20261117_044749_laneB_UK

Test B (image + the region's rule passages), region UK, 5 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/5 (0%); without the lines across the lane: 0/5 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/3 (33%)
- Left boundary: 0/5 (0%); right boundary: 2/4 (50%); both: 0/5 (0%)
- Markings in the lane, exact set: 1/5 (20%) (without the lines across the lane 3/5 (60%)); added (not in the label): 3, of them lines across the lane 1, by the evidence the answer gave {'insufficient': 2, 'full': 1}; missed: 1
- Lane count: 2/5 (40%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 4
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 4 {'leftmost lane, but a lane line on the left': 4}
- Citations (Test B and C): {'in_pack_not_accepted': 1, 'unlisted': 3, 'accepted': 1}; IDs written with brackets (read without them): 12
- Boundary evidence: {'unsupported_guess': 4, 'same': 6}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 5
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 1 |
