# Lane run 20261117_122406_laneC_UK

Test C (image + another region's rule passages (control), passages of IN), region UK, 5 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 2/5 (40%); without the lines across the lane: 3/5 (60%)
- Lane actions (every action the label decides, contested cells excluded): 1/3 (33%)
- Left boundary: 3/5 (60%); right boundary: 3/4 (75%); both: 3/5 (60%)
- Markings in the lane, exact set: 4/5 (80%) (without the lines across the lane 5/5 (100%)); added (not in the label): 1, of them lines across the lane 1, by the evidence the answer gave {'full': 1}; missed: 0
- Lane count: 5/5 (100%); position of my lane: 5/5 (100%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 0; contested unsafe: 1
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 4 {'change_right decided': 3, 'u_turn decided without an arrow or prohibited-movement marking': 3}
- Citations (Test B and C): {'unlisted': 5}; IDs written with brackets (read without them): 5
- Boundary evidence: {'same': 6, 'unsupported_guess': 4}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 32445, 'cached_input_tokens': 0, 'output_tokens': 4128}; cost about $0.0; latency: {'mean': 44.85, 'max': 64.57}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 1 |
