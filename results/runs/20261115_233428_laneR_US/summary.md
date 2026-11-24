# Lane run 20261115_233428_laneR_US

Test R (image + the passages about the elements of the model's own Test A answer), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 19/38 (50%); without the lines across the lane: 21/38 (55%)
- Lane actions (every action the label decides, contested cells excluded): 31/36 (86%)
- Left boundary: 32/37 (86%); right boundary: 29/37 (78%); both: 26/38 (68%)
- Markings in the lane, exact set: 28/37 (76%) (without the lines across the lane 31/37 (84%)); added (not in the label): 15, of them lines across the lane 9, by the evidence the answer gave {'partial': 9, 'full': 6}; missed: 2
- Lane count: 22/38 (58%); position of my lane: 30/38 (79%)
- Unsafe errors (label prohibited, answer allowed): 2 {'change_right': 2}; over-cautious: 3; contested unsafe: 9
- Prohibited actions also prohibited by the answer: 33/38 (87%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {}; IDs written with brackets (read without them): 0
- Boundary evidence: {'same': 64, 'over_withholding': 9, 'unsupported_guess': 2, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 253829, 'cached_input_tokens': 98802, 'output_tokens': 38194}; cost about $0.7019; latency: {'mean': 18.39, 'max': 36.7}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 32 | 32 |
| change_right | 20 | 18 |
| go_straight | 7 | 5 |
| turn_left | 7 | 5 |
| turn_right | 7 | 5 |
| u_turn | 6 | 4 |
