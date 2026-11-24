# Lane try: the United Kingdom (UK), drives on the left

3 photos flipped left to right, tests A, B, prompt prompts/lane_v2, 22 passages from the DRAFT (not reviewed; not a result)

Requests 6, errors 0, from cache 0, cost about $0.0881. Not scored: these photos have no label.

Actions: yes = allowed, NO = prohibited, ? = not determined, - = not applicable.

## 02_mirrored.png

| Test | Left boundary | Right boundary | Markings in the lane | change_left | change_right | go_straight | turn_left | turn_right | u_turn | enter_waiting_area | Passages cited |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | white dashed lane_line | yellow solid edge_line | none | yes | NO | - | - | - | - | - | - |
| B | white dashed lane_line | yellow solid edge_line | none | yes | NO | - | - | - | - | - | UK-Rule131 |

Changed from A to B: nothing

## 05_mirrored.png

| Test | Left boundary | Right boundary | Markings in the lane | change_left | change_right | go_straight | turn_left | turn_right | u_turn | enter_waiting_area | Passages cited |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | white solid lane_line | yellow double_solid center_line | none | NO | ? | ? | ? | ? | ? | - | - |
| B | white solid lane_line | yellow double_solid center_line | none | ? | ? | - | - | - | - | - | - |

Changed from A to B: change_left NO -> ?; go_straight ? -> -; turn_left ? -> -; turn_right ? -> -; u_turn ? -> -

## 06_mirrored.png

| Test | Left boundary | Right boundary | Markings in the lane | change_left | change_right | go_straight | turn_left | turn_right | u_turn | enter_waiting_area | Passages cited |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | white solid lane_line | white solid edge_line | arrow:right | NO | NO | NO | NO | yes | NO | - | - |
| B | white solid lane_line | white solid edge_line | arrow:right | ? | NO | NO | NO | yes | NO | - | UK-Rule134 |

Changed from A to B: change_left NO -> ?
