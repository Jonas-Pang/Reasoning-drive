# Lane run 20261117_022329_laneB_IN

Test B (image + the region's rule passages), region IN, 4 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/4 (0%); without the lines across the lane: 0/4 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/2 (50%)
- Left boundary: 0/4 (0%); right boundary: 0/4 (0%); both: 0/4 (0%)
- Markings in the lane, exact set: 0/4 (0%) (without the lines across the lane 3/4 (75%)); added (not in the label): 4, of them lines across the lane 3, by the evidence the answer gave {'partial': 2, 'insufficient': 1, 'full': 1}; missed: 0
- Lane count: 1/2 (50%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 0; contested unsafe: 1
- Prohibited actions also prohibited by the answer: 1/2 (50%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 2 {'change_left allowed across a curb': 2, 'leftmost lane, but a lane line on the left': 1, 'change_left allowed': 1, 'change_right allowed': 1}
- Citations (Test B and C): {'unlisted': 4}; IDs written with brackets (read without them): 10
- Boundary evidence: {'same': 4, 'unsupported_guess': 4}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 23124, 'cached_input_tokens': 0, 'output_tokens': 4281}; cost about $0.0; latency: {'mean': 10.91, 'max': 13.09}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 1 |
