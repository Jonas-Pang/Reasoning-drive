# Lane run 20261117_201113_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 0/121 (0%); without the lines across the lane: 0/121 (0%)
- Lane actions (every action the label decides, contested cells excluded): 0/116 (0%)
- Left boundary: 0/121 (0%); right boundary: 0/118 (0%); both: 0/121 (0%)
- Markings in the lane, exact set: 0/118 (0%) (without the lines across the lane 0/118 (0%)); added (not in the label): 0, of them lines across the lane 0, by the evidence the answer gave {}; missed: 0
- Lane count: 0/118 (0%); position of my lane: 0/119 (0%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 0/174 (0%)
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'no_answer': 124}; IDs written with brackets (read without them): 0
- Boundary evidence: {'other': 248}
- Readable answers: 0/124 (an unreadable or failed answer counts as wrong); errors: 124; from cache: 0
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 108 | 0 |
| change_right | 108 | 0 |
| go_straight | 25 | 0 |
| turn_left | 25 | 0 |
| turn_right | 25 | 0 |
| u_turn | 25 | 0 |
