# Reasoning of lane run 20261117_024933_laneA_IN

```text
idd__primary_d1_leftCamImgs_0000529 | lane | Test A | gemma4:31b
----------------------------------------------------------------
Step 1  Scene           A narrow residential street in India with buildings and trees on both sides; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the road from a dirt shoulder and parked motorcycles.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the road from a dirt shoulder and greenery.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the presence of edge
                        lines on both sides. | roles: The white solid lines on both sides are consistent with
                        edge lines for a single-lane road. | markings: There are no markings in the lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or leaving
                        the roadway to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or
                        leaving the roadway to the right.
Step 6  change_left     prohibited (correct): The left_boundary is a solid white edge line which prohibits
                        leaving the roadway.
Step 6  change_right    prohibited: The right_boundary is a solid white edge line which prohibits leaving the
                        roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2938, out 596, 14.38 s

idd__primary_d1_leftCamImgs_0000786 | lane | Test A | gemma4:31b
----------------------------------------------------------------
Step 1  Scene           A narrow residential road in India with buildings on both sides; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the road from a dirt shoulder and residential properties.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the road from a paved area and residential properties.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the presence of edge
                        lines on both sides. | roles: The solid white lines on both sides are consistent with
                        edge lines for a single-lane road. | markings: There are no markings in the lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the shoulder or off-
                        road area.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or off-
                        road area.
Step 6  change_left     prohibited (correct): The left_boundary is a solid white edge line which prohibits
                        leaving the roadway.
Step 6  change_right    prohibited: The right_boundary is a solid white edge line which prohibits leaving the
                        roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2938, out 591, 16.95 s

idd__primary_d1_leftCamImgs_0002250 | lane | Test A | gemma4:31b
----------------------------------------------------------------
Step 1  Scene           This is an urban road in India with traffic keeping to the left. The road ahead
                        appears to be a straight stretch with no immediate intersection or ramp visible.
                        (lanes 1, mine 1, full)
Step 2  Left            There is no painted line on the left, but a raised curb and buildings are visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A raised concrete median/curb separates my lane from the opposite direction of
                        traffic.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries, as both
                        sides are edge boundaries (curbs). | roles: The absence of paint and presence of curbs
                        fit the role of edge lines. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: A curb marks the edge of the roadway and prohibits leaving the road to
                        the left.
Step 5  Rule            right_boundary: A raised median prohibits crossing into the opposite direction of
                        traffic to the right.
Step 6  change_left     prohibited: The left_boundary is a curb, which prohibits leaving the roadway.
Step 6  change_right    prohibited (contested, correct): The right_boundary is a raised median, which
                        prohibits crossing into opposite traffic.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes are prohibited on both sides due
                        to the curbs and median.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2938, out 613, 18.75 s

idd__primary_d1_leftCamImgs_0002357 | lane | Test A | gemma4:31b
----------------------------------------------------------------
Step 1  Scene           This is a city street in India with buildings on both sides; the road continues
                        straight ahead with some vehicles and parked motorcycles. (lanes 1, mine 1, full)
Step 2  Left            There is no painted line on the left, but a curb and a sidewalk with parked
                        motorcycles are present.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A raised concrete curb separates the road from the sidewalk on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the presence of curbs on
                        both sides. | roles: The absence of paint and presence of curbs fit the role of edge
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A curb marks the edge of the roadway and prohibits leaving the road to
                        the left.
Step 5  Rule            right_boundary: A curb marks the edge of the roadway and prohibits leaving the road to
                        the right.
Step 6  change_left     prohibited: The left boundary is a curb, which prohibits leaving the roadway.
Step 6  change_right    prohibited (contested, correct): The right boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not attempt to cross the curbs on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 2938, out 615, 17.63 s
```
