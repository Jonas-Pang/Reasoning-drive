# Lane run 20261117_021852_laneA_IN

Test A (image only), region IN, 4 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/4 (0%); without the lines across the lane: 0/4 (0%)
- Lane actions (every action the label decides, contested cells excluded): 2/2 (100%)
- Left boundary: 2/4 (50%); right boundary: 0/4 (0%); both: 0/4 (0%)
- Markings in the lane, exact set: 0/4 (0%) (without the lines across the lane 3/4 (75%)); added (not in the label): 5, of them lines across the lane 3, by the evidence the answer gave {'insufficient': 5}; missed: 0
- Lane count: 0/2 (0%); position of my lane: 0/2 (0%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 2/2 (100%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 4, 'same': 4}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 11752, 'cached_input_tokens': 0, 'output_tokens': 2837}; cost about $0.0; latency: {'mean': 23.73, 'max': 29.56}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 2 |
