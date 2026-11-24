# Lane run 20261115_231257_laneC_US

Test C (image + another region's rule passages (control), passages of CN), region US, 38 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 19/38 (50%); without the lines across the lane: 22/38 (58%)
- Lane actions (every action the label decides, contested cells excluded): 30/36 (83%)
- Left boundary: 33/37 (89%); right boundary: 30/37 (81%); both: 27/38 (71%)
- Markings in the lane, exact set: 28/37 (76%) (without the lines across the lane 32/37 (86%)); added (not in the label): 16, of them lines across the lane 10, by the evidence the answer gave {'partial': 12, 'full': 4}; missed: 1
- Lane count: 20/38 (53%); position of my lane: 31/38 (82%)
- Unsafe errors (label prohibited, answer allowed): 1 {'change_left': 1}; over-cautious: 2; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 31/38 (82%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 0 {}
- Citations (Test B and C): {'in_pack_not_accepted': 38}; IDs written with brackets (read without them): 2
- Boundary evidence: {'same': 60, 'over_withholding': 13, 'unsupported_guess': 2, 'other': 1}
- Readable answers: 38/38 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 344432, 'cached_input_tokens': 301416, 'output_tokens': 39025}; cost about $0.5064; latency: {'mean': 21.11, 'max': 32.46}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 32 | 31 |
| change_right | 20 | 17 |
| go_straight | 7 | 6 |
| turn_left | 7 | 6 |
| turn_right | 7 | 5 |
| u_turn | 6 | 5 |
