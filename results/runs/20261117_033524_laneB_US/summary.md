# Lane run 20261117_033524_laneB_US

Test B (image + the region's rule passages), region US, 108 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 33/104 (32%); without the lines across the lane: 33/104 (32%)
- Lane actions (every action the label decides, contested cells excluded): 63/102 (62%)
- Left boundary: 61/103 (59%); right boundary: 57/102 (56%); both: 33/103 (32%)
- Markings in the lane, exact set: 89/101 (88%) (without the lines across the lane 91/101 (90%)); added (not in the label): 4, of them lines across the lane 0, by the evidence the answer gave {'full': 4}; missed: 11
- Lane count: 58/101 (57%); position of my lane: 74/103 (72%)
- Unsafe errors (label prohibited, answer allowed): 8 {'change_left': 7, 'turn_left': 1}; over-cautious: 23; contested unsafe: 5
- Prohibited actions also prohibited by the answer: 51/72 (71%)
- Actions decided where the label has no governing marking: 7
- Answers that contradict themselves: 5 {'rightmost lane, but a lane line on the right': 2, 'go_straight decided without an arrow or prohibited-movement marking': 1, 'leftmost lane, but a lane line on the left': 1, 'go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-movement marking': 1}
- Citations (Test B and C): {'accepted': 97, 'unlisted': 5, 'in_pack_not_accepted': 6}; IDs written with brackets (read without them): 194
- Boundary evidence: {'same': 166, 'unsupported_guess': 50}
- Readable answers: 108/108 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 0
- Tokens: {'input_tokens': 932472, 'cached_input_tokens': 0, 'output_tokens': 90250}; cost about $0.0; latency: {'mean': 18.9, 'max': 28.91}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 94 | 78 |
| change_right | 54 | 32 |
| go_straight | 10 | 8 |
| turn_left | 10 | 4 |
| turn_right | 11 | 4 |
| u_turn | 9 | 4 |
