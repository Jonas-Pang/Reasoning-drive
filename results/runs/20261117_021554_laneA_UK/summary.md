# Lane run 20261117_021554_laneA_UK

Test A (image only), region UK, 5 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/5 (0%); without the lines across the lane: 0/5 (0%)
- Lane actions (every action the label decides, contested cells excluded): 0/3 (0%)
- Left boundary: 0/5 (0%); right boundary: 0/4 (0%); both: 0/5 (0%)
- Markings in the lane, exact set: 2/5 (40%) (without the lines across the lane 5/5 (100%)); added (not in the label): 3, of them lines across the lane 3, by the evidence the answer gave {'insufficient': 3}; missed: 0
- Lane count: 0/5 (0%); position of my lane: 2/5 (40%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 1; contested unsafe: 1
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 1 {'turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 6, 'unsupported_guess': 4}
- Readable answers: 5/5 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 14745, 'cached_input_tokens': 0, 'output_tokens': 3777}; cost about $0.0; latency: {'mean': 33.29, 'max': 45.57}

| Action | Decided by the label | Correct |
|---|---|---|
| change_right | 3 | 0 |
