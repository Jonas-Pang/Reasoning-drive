# Lane run 20261117_033505_laneB_US

Test B (image + the region's rule passages), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 37/104 (36%); without the lines across the lane: 38/104 (37%)
- Lane actions (every action the label decides, contested cells excluded): 65/102 (64%)
- Left boundary: 63/103 (61%); right boundary: 65/102 (64%); both: 38/103 (37%)
- Markings in the lane, exact set: 88/101 (87%) (without the lines across the lane 90/101 (89%)); added (not in the label): 6, of them lines across the lane 1, by the evidence the answer gave {'full': 6}; missed: 12
- Lane count: 58/101 (57%); position of my lane: 75/103 (73%)
- Unsafe errors (label prohibited, answer allowed): 8 {'change_left': 6, 'turn_left': 1, 'change_right': 1}; over-cautious: 19; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 54/72 (75%)
- Actions decided where the label has no governing marking: 7
- Answers that contradict themselves: 7 {'rightmost lane, but a lane line on the right': 4, 'leftmost lane, but a lane line on the left': 2, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 98, 'unlisted': 4, 'in_pack_not_accepted': 6}; IDs written with brackets (read without them): 178
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 932472, 'cached_input_tokens': 0, 'output_tokens': 90664}; cost about $0.0; latency: {'mean': 18.9, 'max': 27.33}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 80 |
| change_right | 54 | 34 |
| go_straight | 10 | 8 |
| turn_left | 10 | 5 |
| turn_right | 11 | 5 |
| u_turn | 9 | 5 |
