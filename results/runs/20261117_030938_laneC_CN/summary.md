# Lane run 20261117_030938_laneC_CN

Test C (image + another region's rule passages (control), passages of US), region CN, 124 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 39/121 (32%); without the lines across the lane: 39/121 (32%)
- Lane actions (every action the label decides, contested cells excluded): 59/118 (50%)
- Left boundary: 58/121 (48%); right boundary: 69/118 (58%); both: 44/121 (36%)
- Markings in the lane, exact set: 92/118 (78%) (without the lines across the lane 101/118 (86%)); added (not in the label): 4, of them lines across the lane 1, by the evidence the answer gave {'full': 4}; missed: 29
- Lane count: 68/118 (58%); position of my lane: 75/119 (63%)
- Unsafe errors (label prohibited, answer allowed): 46 {'change_left': 21, 'change_right': 22, 'go_straight': 3}; over-cautious: 16; contested unsafe: 17
- Prohibited actions also prohibited by the answer: 75/142 (53%)
- Actions decided where the label has no governing marking: 4
- Answers that contradict themselves: 2 {'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1, 'go_straight allowed': 1, 'u_turn prohibited': 1}
- Citations (Test B and C): {'in_pack_not_accepted': 119, 'unlisted': 4, 'none': 1}; IDs written with brackets (read without them): 242
- Boundary evidence: {'unsupported_guess': 106, 'same': 142}
- Readable answers: 124/124 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 1069872, 'cached_input_tokens': 0, 'output_tokens': 84214}; cost about $0.0; latency: {'mean': 18.3, 'max': 47.3}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 107 | 67 |
| change_right | 108 | 64 |
| go_straight | 25 | 20 |
| turn_left | 22 | 13 |
| turn_right | 21 | 13 |
| u_turn | 21 | 12 |
