# Lane run 20261117_040150_laneB_UK

Test B (image + the region's rule passages), region UK, 11 images, one request each, model gemma4:31b

- Lane identified (both boundaries and the markings): 1/11 (9%); without the lines across the lane: 1/11 (9%)
- Lane actions (every action the label decides, contested cells excluded): 3/11 (27%)
- Left boundary: 2/11 (18%); right boundary: 1/10 (10%); both: 1/11 (9%)
- Markings in the lane, exact set: 10/11 (91%) (without the lines across the lane 10/11 (91%)); added (not in the label): 1, of them lines across the lane 0, by the evidence the answer gave {'full': 1}; missed: 1
- Lane count: 8/9 (89%); position of my lane: 7/9 (78%)
- Unsafe errors (label prohibited, answer allowed): 0 {}; over-cautious: 5; contested unsafe: 4
- Prohibited actions also prohibited by the answer: -
- Actions decided where the label has no governing marking: 0
- Answers that contradict themselves: 5 {'change_right decided': 5}
- Citations (Test B and C): {'in_pack_not_accepted': 7, 'unlisted': 2, 'accepted': 2}; IDs written with brackets (read without them): 10
- Boundary evidence: {'same': 18, 'unsupported_guess': 4}
- Readable answers: 11/11 (an unreadable or failed answer counts as wrong); errors: 0; from cache: 5
- Tokens: {'input_tokens': 81864, 'cached_input_tokens': 0, 'output_tokens': 4799}; cost about $0.0; latency: {'mean': 18.25, 'max': 19.92}

| Action | Decided by the label | Correct |
|---|---|---|
| change_left | 1 | 1 |
| change_right | 11 | 3 |
