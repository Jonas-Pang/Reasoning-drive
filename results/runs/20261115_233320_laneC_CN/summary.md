# Lane run 20261115_233320_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 25 images, one request each, model gpt-6.1-sol

- Lane identified (both boundaries and the markings): 14/25 (56%); without the lines across the lane: 16/25 (64%)
- Lane actions (every action the label decides, contested cells excluded): 12/22 (55%)
- Left boundary: 18/25 (72%); right boundary: 22/25 (88%); both: 16/25 (64%)
- Markings in the lane, exact set: 21/25 (84%) (without the lines across the lane 24/25 (96%)); added (not in the label): 5, of them lines across the lane 4, by the evidence the answer gave {'full': 5}; missed: 0
- Lane count: 16/22 (73%); position of my lane: 17/22 (77%)
- Unsafe errors (label prohibited, answer allowed): 11 {'change_right': 6, 'change_left': 5}; over-cautious: 0; contested unsafe: 0
- Prohibited actions also prohibited by the answer: 15/26 (58%)
- Actions decided where the label has no governing marking: 3
- Answers that contradict themselves: 1 {'change_left allowed across a curb': 1, 'change_right allowed across a curb': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 24, 'none_needed': 1}; IDs written with brackets (read without them): 0
- Boundary evidence: {'unsupported_guess': 8, 'same': 39, 'over_withholding': 3}
- Readable answers: 25/25 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 25
- Tokens: {'input_tokens': 0, 'cached_input_tokens': 0, 'output_tokens': 0}; cost about $0.0; latency: {}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 22 | 17 |
| change_right | 22 | 14 |
| go_straight | 3 | 3 |
| turn_left | 3 | 3 |
| turn_right | 3 | 3 |
| u_turn | 3 | 3 |
