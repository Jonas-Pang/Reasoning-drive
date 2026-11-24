# Lane run 20261115_231546_laneD_US

Test D (image only, country not given), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 18/38 (47%); without the lines across the lane: 20/38 (53%)
- Lane actions (every action the label decides, contested cells excluded): 30/36 (83%)
- Left boundary: 33/37 (89%); right boundary: 29/37 (78%); both: 26/38 (68%)
- Markings in the lane, exact set: 27/37 (73%) (without the lines across the lane 31/37 (84%)); added (not in the label): 17, of them lines across the lane 11, by the evidence the answer gave {'full': 7, 'partial': 10}; missed: 2
- Lane count: 23/38 (61%); position of my lane: 32/38 (84%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_left': 2}; over-cautious: 2; contested unsafe: 4
- Prohibited actions also prohibited by the answer: 31/38 (82%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 62, 'over_withholding': 10, 'other': 2, 'unsupported_guess': 2}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 179360, 'cached_input_tokens': 135356, 'output_tokens': 39105}; cost about $0.4926; latency: {'mean': 21.31, 'max': 34.82}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 32 | 30 |
| change_right | 20 | 18 |
| go_straight | 7 | 6 |
| turn_left | 7 | 5 |
| turn_right | 7 | 5 |
| u_turn | 6 | 4 |
