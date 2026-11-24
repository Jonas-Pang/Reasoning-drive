# Lane run 20261117_044337_laneA_UK

Test A (image only), region UK, 11 images, one request each, model gemma4:12b

- Lane identified (both boundaries and the markings): 0/11 (0%); without the lines across the lane: 0/11 (0%)
- Lane actions (every action the label decides, contested cells excluded): 1/11 (9%)
- Left boundary: 2/11 (18%); right boundary: 1/10 (10%); both: 0/11 (0%)
- Markings in the lane, exact set: 1/11 (9%) (without the lines across the lane 5/11 (45%)); added (not in the label): 10, of them lines across the lane 4, by the evidence the answer gave {'full': 6, 'insufficient': 4}; missed: 1
- Lane count: 0/9 (0%); position of my lane: 4/9 (44%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 7; contested unsafe: 1
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 5 {'leftmost lane, but a lane line on the left': 3, 'go_straight allowed without the stop that the STOP or 停 marking in my lane requires': 2}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 18, 'unsupported_guess': 4}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 32439, 'cached_input_tokens': 0, 'output_tokens': 8009}; cost about $0.0; latency: {'mean': 6.75, 'max': 8.28}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 11 | 1 |
