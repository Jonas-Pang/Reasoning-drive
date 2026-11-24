# Same map, four countries (Town03, CARLA 0.9.16)

Prompt prompts/lane_v2, model gpt-6.1-sol, tests A, B, the car drives with Test B.

Left-hand countries see the photo flipped left to right (mirror world); the actions below are as in the photo they saw.

| Country | Scene | Intent (in the photo) | Test A: change_left / change_right / turn_left / turn_right | Test B: same | The car (Test B) | A would |
|---|---|---|---|---|---|---|
| US | lane_change | change_right | NO / yes / - / - | NO / yes / - / - | change right (allowed) | change right (allowed) |
| US | arrow_lane | turn_right | NO / yes / yes / NO | NO / yes / yes / NO | turn right not allowed from this lane; changes to the right lane first (allowed), then turns | turn right not allowed from this lane; changes to the right lane first (allowed), then turns |
| CN | lane_change | change_right | NO / NO / - / - | NO / NO / - / - | stays in its lane (change right: prohibited) | stays in its lane (change right: prohibited) |
| CN | arrow_lane | turn_right | NO / NO / yes / NO | NO / NO / yes / NO | turn right: prohibited, change_right: prohibited -> follows the lane (turn left) | turn right: prohibited, change_right: prohibited -> follows the lane (turn left) |
| UK (mirrored) | lane_change | change_left | yes / - / - / - | yes / yes / - / - | change left (allowed) | change left (allowed) |
| UK (mirrored) | arrow_lane | turn_left | NO / NO / NO / yes | yes / NO / NO / yes | turn left not allowed from this lane; changes to the left lane first (allowed), then turns | turn left: prohibited, change_left: prohibited -> follows the lane (turn right) |
| JP (mirrored) | lane_change | change_left | yes / NO / - / - | yes / NO / - / - | change left (allowed) | change left (allowed) |
| JP (mirrored) | arrow_lane | turn_left | yes / NO / NO / yes | yes / NO / NO / yes | turn left not allowed from this lane; changes to the left lane first (allowed), then turns | turn left not allowed from this lane; changes to the left lane first (allowed), then turns |

Cost about $0.1936.
UK: the passages are a draft that has not been reviewed.
JP: the passages are a draft that has not been reviewed.
