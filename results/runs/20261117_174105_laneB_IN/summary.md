# Lane run 20261117_174105_laneB_IN

Test B (image + the region's rule passages), region IN, 4 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 0/4 (0%); without the lines across the lane: 0/4 (0%)
- Lane actions (every action the label decides, contested cells excluded): 2/2 (100%)
- Left boundary: 2/4 (50%); right boundary: 2/4 (50%); both: 0/4 (0%)
- Markings in the lane, exact set: 4/4 (100%) (without the lines across the lane 4/4 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 2/2 (100%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 2/2 (100%)
- Actions decided where the label has no governing marking: 6
- Answers that contradict themselves: 2 {'u_turn decided without an arrow or prohibited-movement marking': 2}
- Citations (Test B and C): {'unlisted': 3, 'none_needed': 1}; IDs written with brackets (read without them): 2
- Boundary evidence: {'same': 4, 'unsupported_guess': 4}
- Readable answers: 4/4 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 28904, 'cached_input_tokens': 0, 'output_tokens': 3311}; cost about $0.0; latency: {'mean': 23.02, 'max': 29.19}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 2 | 2 |
