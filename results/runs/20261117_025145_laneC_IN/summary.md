# Lane run 20261117_025145_laneC_IN

Test C (image + another region's rule passages (control), passages of UK), region IN, 4 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 0/4 (0%); without the lines across the lane: 0/4 (0%)
- Lane actions (every action the label decides, contested cells excluded): 0/2 (0%)
- Left boundary: 2/4 (50%); right boundary: 2/4 (50%); both: 0/4 (0%)
- Markings in the lane, exact set: 4/4 (100%) (without the lines across the lane 4/4 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 2/2 (100%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_left': 2}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 0/2 (0%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'none_needed': 2, 'in_pack_not_accepted': 2}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 4, 'same': 4}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 54532, 'cached_input_tokens': 0, 'output_tokens': 2843}; cost about $0.0; latency: {'mean': 36.75, 'max': 42.48}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 0 |
