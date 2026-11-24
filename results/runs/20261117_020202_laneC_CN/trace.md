# Reasoning of lane run 20261117_020202_laneC_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading straight. The road continues forward with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 648, 102.85 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading straight. There are no intersections or ramps
                        immediately ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the right shoulder, with a metal guardrail
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right indicate my lane is the rightmost of
                        the moving lanes, but there is another lane to my left. Wait, if I am index 2 of 3,
                        there should be a lane to my right. Looking again, the right boundary is an edge line,
                        meaning I am the rightmost lane. Thus, lane_count is 2 and ego_lane_index is 2. |
                        roles: The white broken line fits a lane_line role, and the white solid line fits an
                        edge_line role. | markings: No markings in lane. | unseen: No | result: corrected
                        lane_count to 2 and ego_lane_index to 2
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3A.04-01].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, which prohibits
                        crossing into the shoulder according to [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the right edge line
                        into the shoulder.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 727, 25.25 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, likely a highway or expressway, with a clear path
                        ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line is visible on the left, separating my lane from a shoulder or a
                        special lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as lane 1 are consistent with having an
                        edge line on the left and a lane line on the right. | roles: The solid white edge line
                        and dashed white lane line fit their respective roles. | markings: There are no
                        markings in my lane to contradict. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the edge of the roadway; crossing it is
                        generally discouraged or prohibited depending on the specific application.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition, allowing lane changes.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white edge line, which
                        prohibits or discourages crossing [US-3A.04-01].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white lane line,
                        which permits crossing [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid white line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 653, 98.3 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with high-rise buildings on both sides, heading
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken yellow line separates my lane from the lane to the left.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 are consistent with having
                        boundaries on both sides. | roles: The yellow broken line on the left is unusual for a
                        same-direction lane line, but the white solid line on the right fits a lane line role.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Yellow markings usually delineate opposite traffic or special lanes; a
                        broken line indicates a permissive condition [US-3A.04-01]. [US-3A.03-03-04]
Step 5  Rule            right_boundary: A solid white lane line discourages crossing. [US-3B.06-05-06]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a broken
                        line [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white line which discourages or prohibits crossing [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable because no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable because no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable because no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but avoid changing to the right due to the solid
                        white line. You can proceed straight.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 672, 103.94 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a concrete barrier on the right, heading
                        towards a distant intersection. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line is on the right, next to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 3 agree with the right boundary being
                        an edge line and the left boundary being a lane line. | roles: The white broken line
                        on the left fits the role of a lane line, and the white solid line on the right fits
                        the role of an edge line. | markings: There are no markings in my lane to contradict.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (contested, correct): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, label allowed): The right boundary is a solid white edge line
                        and a concrete barrier, which prohibits leaving the roadway according to
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move right due to the road edge and barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['text:bus']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 684, 99.34 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an overpass. The road appears to
                        be a one-way street or a divided highway. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a concrete barrier and a shoulder area.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a paved shoulder and a stone wall.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the boundaries, as both sides
                        are edge lines. | roles: The white solid lines on both sides fit the role of edge
                        lines for a one-way road or divided highway. | markings: There are no markings in the
                        lane to contradict the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: A white longitudinal line on the left delineates the left-hand edge of
                        a one-way street or divided highway. [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, and [US-3A.04-01]
                        states a solid line discourages or prohibits crossing.
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, and [US-3A.04-01]
                        states a solid line discourages or prohibits crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 668, 18.61 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus stop on the left and parked scooters on the
                        right, heading towards a distant intersection. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a bus stop area on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a parking area for scooters on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries being edge lines.
                        | roles: The white solid lines fit the role of edge lines for the roadway. | markings:
                        There are no markings in the lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid white line delineates the edge of the roadway; crossing it is
                        discouraged or prohibited depending on the application. [US-3B.09-01-02]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway;
                        crossing it is discouraged or prohibited. [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, which prohibits or
                        discourages crossing [US-3B.09-01-02].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, which prohibits
                        or discourages crossing [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict going straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 652, 79.74 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: No markings are present in the lane. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 620, 78.49 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a clear path ahead, surrounded by trees and
                        greenery. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a curb and greenery.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white broken line fits
                        the role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane line allows crossing with
                        care according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line and curb prohibit leaving
                        the roadway according to [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 654, 14.93 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a wide urban road with multiple lanes, heading towards a signalized
                        intersection. (lanes 4, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 4 and ego position 2 are consistent with having lane lines
                        on both sides. | roles: The white dashed lines are consistent with lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed: The left boundary is a broken white line, which is permissive according to
                        [US-3B.06-05-06].
Step 6  change_right    allowed: The right boundary is a broken white line, which is permissive according to
                        [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 639, 96.55 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading straight toward a distant
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is on the left, with a white fence and sidewalk beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        an edge line and the right boundary being a lane line. | roles: The solid yellow left
                        boundary fits the role of an edge line for a one-way street or divided highway; the
                        broken white right boundary fits the role of a lane line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow left edge line delineates the left-hand edge of the
                        roadway and indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow edge line, and rule
                        [US-3B.09-03] prohibits crossing it.
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, and rule
                        [US-3B.06-05-06] allows crossing it.
Step 6  go_straight     allowed (contested, label not_determined): No marking governs this action, and there
                        is no restriction to carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['symbol:other']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 687, 15.36 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane divided highway or expressway, traveling straight ahead on
                        a bridge or overpass. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete barrier beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: White dashed line for lane separation and
                        white solid line for the right edge are consistent with their roles. | markings: No
                        markings are present in the lane, which is consistent with a standard highway through
                        lane. | unseen: No attributes were reported without visual evidence. | result:
                        consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3A.04-01].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [US-3B.09-01-02] and the
                        physical concrete barrier.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings
                        in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting areas are present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the left lane if needed. Do not attempt to move
                        right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 813, 83.82 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway passing under an overpass. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is on the left, with a guardrail and greenery beyond it.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow edge line on the left and the white lane line on the right
                        confirm my lane is the leftmost of two lanes in my direction. | roles: The solid
                        yellow line fits the role of a left edge line, and the broken white line fits the role
                        of a lane line. | markings: There are no markings in my lane to contradict. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The yellow line delineates the left-hand edge of the roadway.
                        [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): The solid yellow edge line prohibits crossing it [US-3A.04-01].
Step 6  change_right    allowed (correct): The broken white lane line permits crossing with care
                        [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change to the right lane, but do not cross the
                        yellow line on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 618, 18.06 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway with clear weather; the road continues straight ahead. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both my left and right. | roles: The white broken lines on both sides
                        are consistent with the role of lane lines separating traffic in the same direction. |
                        markings: There are no markings in my lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive under [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        under [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 637, 16.6 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both the left and right. | roles: The white dashed lines on both sides fit the role of
                        lane lines separating traffic in the same direction. | markings: The straight-ahead
                        arrow is consistent with a through lane. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [[US-FIG-3B-21]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line
                        [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): Allowed by the through lane-use arrow [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): Prohibited by the through lane-use arrow [US-FIG-3B-21] which
                        does not show a left turn.
Step 6  turn_right      prohibited (correct): Prohibited by the through lane-use arrow [US-FIG-3B-21] which
                        does not show a right turn.
Step 6  u_turn          prohibited (correct): Prohibited by the through lane-use arrow [US-FIG-3B-21] which
                        does not show a U-turn.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes, but you cannot
                        turn at the intersection from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 766, 20.02 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a large intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 633, 22.53 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. The road continues forward
                        with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 641, 23.82 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China, looking straight ahead towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white broken lines fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 640, 100.86 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection or a junction
                        with overhead signage. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of lane lines separating traffic
                        in the same direction. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (contested, correct): The right boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 647, 16.44 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: White dashed lines are consistent with lane lines
                        separating traffic in the same direction. | markings: The straight-ahead arrow is
                        consistent with a through lane. | unseen: No attributes were reported without visual
                        evidence. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that going straight is a
                        permissible movement. [US-FIG-3B-21]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (US-3B.06-05-06).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (US-3B.06-05-06).
Step 6  go_straight     allowed (correct): allowed by the through lane-use arrow (US-FIG-3B-21).
Step 6  turn_left       prohibited (correct): prohibited by the through lane-use arrow which does not show a
                        left turn (US-FIG-3B-21).
Step 6  turn_right      prohibited (correct): prohibited by the through lane-use arrow which does not show a
                        right turn (US-FIG-3B-21).
Step 6  u_turn          prohibited (correct): prohibited by the through lane-use arrow which does not show a
                        U-turn (US-FIG-3B-21).
Step 6  enter_waiting_areanot_applicable: no marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may go straight or change lanes. If you need to turn,
                        please move to the corresponding turn lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 929, 23.64 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with a
                        traffic signal. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: No markings are present in the lane to contradict
                        boundaries. | unseen: No attributes were reported without visual evidence. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 640, 16.45 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a wide intersection or open area.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line separates my lane from the lane to its right.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego position (2) agree with the boundaries: a white
                        lane line on the left and a yellow center line on the right indicate my lane is the
                        rightmost lane of my direction, but there is another lane to my left. Wait, if the
                        right boundary is a center line, I am in the rightmost lane. If there are 3 lanes
                        total for my direction, and I am in index 2, there should be a lane to my right.
                        However, the yellow line indicates the opposite direction starts there. Thus, I am in
                        the rightmost lane (index 3 of 3). Correcting lane_count to 2 and ego_lane_index to 2.
                        | roles: The white dashed line fits a lane_line role; the yellow solid line fits a
                        center_line role. | markings: No markings in lane. | unseen: No | result: corrected
                        lane_count to 2 and ego_lane_index to 2
Step 5  Rule            left_boundary: A broken white line indicates that crossing the lane line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid yellow line as a center line prohibits crossing for the
                        traffic adjacent to the solid line. [[US-3B.01-04]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which is
                        permissive [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid yellow center line,
                        which prohibits crossing [US-3B.01-04].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may change lanes to the left, but you must not
                        cross the yellow line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 764, 17.34 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China, looking straight ahead with overhead lane guidance
                        signs. (lanes 5, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 5 and my position at index 2 are consistent with having
                        lane lines on both sides. | roles: The white dashed lines are consistent with lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        my lane to contradict the boundaries. | unseen: No attributes were reported without
                        being visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['text:other']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 628, 16.16 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead on a clear
                        road. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines are consistent with the role of
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which is permissive
                        according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8628, out 647, 17.17 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a clear path ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with lane lines separating traffic
                        in the same direction. | markings: No markings are present in the lane. | unseen: No
                        attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8628, out 625, 13.79 s
```
