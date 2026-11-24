# Lane run 20261116_011440_laneA_US

Test A (image only), region US, 108 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 0/104 (0%); without the lines across the lane: 0/104 (0%)
- Lane actions (every action the label decides, contested cells excluded): 0/102 (0%)
- Left boundary: 0/103 (0%); right boundary: 0/102 (0%); both: 0/103 (0%)
- Markings in the lane, exact set: 0/101 (0%) (without the lines across the lane 0/101 (0%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 0/101 (0%); position of my lane: 0/103 (0%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 0/72 (0%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'other': 216}
- Readable answers: 0/108 (an unreadable or failed answer counts as wrong); errors: 108; from cache: 0
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 0 |
| change_right | 54 | 0 |
| go_straight | 10 | 0 |
| turn_left | 10 | 0 |
| turn_right | 11 | 0 |
| u_turn | 9 | 0 |
