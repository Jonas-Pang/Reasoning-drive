# Lane run 20261117_052748_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 11 images, one request each, model gemma4:e4b

- Lane identified (both boundaries and the markings): 0/11 (0%); without the lines across the lane: 0/11 (0%)
- Lane actions (every action the label decides, contested cells excluded): 7/11 (64%)
- Left boundary: 0/11 (0%); right boundary: 7/10 (70%); both: 0/11 (0%)
- Markings in the lane, exact set: 0/11 (0%) (without the lines across the lane 8/11 (73%)); added (not in the label): 11, of them lines across the lane 10, by the evidence the answer gave {'insufficient': 3, 'partial': 6, 'full': 2}; missed: 2
- Lane count: 1/9 (11%); position of my lane: 9/9 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 7
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 11 {'change_left allowed across a curb': 7, 'leftmost lane, but a lane line on the left': 5, 'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'unlisted': 11}; IDs written with brackets (read without them): 29
- Boundary evidence: {'same': 18, 'unsupported_guess': 4}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 63712, 'cached_input_tokens': 0, 'output_tokens': 11860}; cost about $0.0; latency: {'mean': 7.1, 'max': 8.59}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 11 | 7 |
