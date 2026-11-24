# Lane run 20261117_015033_laneA_US

Test A (image only), region US, 2 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 1/2 (50%); without the lines across the lane: 1/2 (50%)
- Lane actions (every action the label decides, contested cells excluded): 2/2 (100%)
- Left boundary: 1/2 (50%); right boundary: 1/2 (50%); both: 1/2 (50%)
- Markings in the lane, exact set: 1/2 (50%) (without the lines across the lane 2/2 (100%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 1
- Lane count: 1/2 (50%); position of my lane: 2/2 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 4/4 (100%)
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 1 {'u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 4}
- Readable answers: 2/2 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 5880, 'cached_input_tokens': 0, 'output_tokens': 1334}; cost about $0.0; latency: {'mean': 68.8, 'max': 131.68}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 1 | 1 |
| go_straight | 1 | 1 |
| turn_left | 1 | 1 |
| turn_right | 1 | 1 |
| u_turn | 1 | 1 |
