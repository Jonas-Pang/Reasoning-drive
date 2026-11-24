# Lane run 20261117_044509_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 11 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/11 (0%); without the lines across the lane: 0/11 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/11 (9%)
- Left boundary: 3/11 (27%); right boundary: 1/10 (10%); both: 1/11 (9%)
- Markings in the lane, exact set: 1/11 (9%) (without the lines across the lane 5/11 (45%)); added (not in the label): 30, of them lines across the lane 8, by the evidence the answer gave {'full': 6, 'insufficient': 24}; missed: 1
- Lane count: 0/9 (0%); position of my lane: 3/9 (33%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 7; contested unsafe: 0
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 1
- Answers that contradict themselves: 3 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2, 'u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'unlisted': 11}; IDs written with brackets (read without them): 21
- Boundary evidence: {'same': 18, 'unsupported_guess': 4}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 63756, 'cached_input_tokens': 0, 'output_tokens': 7889}; cost about $0.0; latency: {'mean': 8.02, 'max': 11.36}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 11 | 1 |
