# Lane run 20261117_223915_laneA_UK

Test A (image only), region UK, 48 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/48 (0%); without the lines across the lane: 1/48 (2%)
- Lane actions (every action the label decides, contested cells excluded): 19/39 (49%)
- Left boundary: 20/48 (42%); right boundary: 22/47 (47%); both: 10/48 (21%)
- Markings in the lane, exact set: 3/48 (6%) (without the lines across the lane 13/48 (27%)); added (not in the label): 59, of them lines across the lane 11, by the evidence the answer gave {'full': 50, 'insufficient': 7, 'partial': 2}; missed: 15
- Lane count: 3/28 (11%); position of my lane: 18/28 (64%)
- Unsafe errors (label prohibited, answer allowed): 3 {'change_right': 1, 'turn_left': 2}; over-cautious: 23; contested unsafe: 12
- Prohibited actions also prohibited by the answer: 18/21 (86%)
- Actions decided where the label has no governing marking: 16
- Answers that contradict themselves: 13 {'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 5, 'turn_right prohibited': 5, 'turn_left prohibited': 3, 'change_left prohibited': 1, 'change_right allowed across a curb': 1, 'change_left allowed across a curb': 1}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 92, 'unsupported_guess': 4}
- Readable answers: 48/48 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 183312, 'cached_input_tokens': 0, 'output_tokens': 40871}; cost about $0.0; latency: {'mean': 7.8, 'max': 11.84}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 11 | 9 |
| change_right | 36 | 19 |
| go_straight | 8 | 7 |
| turn_left | 8 | 4 |
| turn_right | 8 | 7 |
| u_turn | 8 | 7 |
