# Lane run 20261115_154534_laneA_US

Test A (image only), region US, 2 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 1/2 (50%); without the lines across the lane: 2/2 (100%)
- Lane actions (every action the label decides, contested cells excluded): 2/2 (100%)
- Left boundary: 2/2 (100%); right boundary: 2/2 (100%); both: 2/2 (100%)
- Markings in the lane, exact set: 1/2 (50%) (without the lines across the lane 2/2 (100%)); added (not in the label): 2, of them lines across the lane 2, by the evidence the answer gave {'full': 2}; missed: 0
- Lane count: 1/2 (50%); position of my lane: 1/2 (50%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 4/4 (100%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 4}
- Readable answers: 2/2 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 2
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 1 | 1 |
| go_straight | 1 | 1 |
| turn_left | 1 | 1 |
| turn_right | 1 | 1 |
| u_turn | 1 | 1 |
