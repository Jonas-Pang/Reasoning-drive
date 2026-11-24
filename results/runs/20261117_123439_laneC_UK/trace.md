# Reasoning of lane run 20261117_123439_laneC_UK

```text
lingoqa__evaluation_images_val_01dbcf4b079b49b6ca34c0475492380c_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching an intersection where a red double-
                        decker bus is stopped ahead. (lanes 1, mine 1, full)
Step 2  Left            A red line is painted along the edge of the road next to the sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the area where the bus is positioned.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and right lane
                        line. | roles: The red solid line on the left is an edge line; the white dashed line
                        on the right is a lane line. | markings: There are no markings in my lane. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The red edge line marks the boundary of the roadway; crossing it into
                        the sidewalk is prohibited by general road usage rules. [null]
Step 5  Rule            right_boundary: The dashed white line allows changing lanes after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is an edge line with a curb, and
                        crossing it is prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a dashed white line, which
                        allows lane changes per [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action, so it is not_applicable.
Step 6  turn_right      not_applicable: No marking governs this action, so it is not_applicable.
Step 6  u_turn          not_applicable: No marking governs this action, so it is not_applicable.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  You can proceed straight or change lanes to the right. Do not cross the red line on
                        the left into the sidewalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe ['change_right'],
                        citation unlisted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 5803, out 632, 10.78 s

lingoqa__evaluation_images_val_04c64714f8a1bf28da156721ed7eff32_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road with a slight bend to the right. My car is in a
                        single lane moving forward. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a cycle lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A solid white line separates the lane from the right curb and sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a special lane
                        line on the left and an edge line on the right. | roles: The white solid lines fit the
                        roles of special lane line and edge line respectively. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        [IN-6(6)] prohibits driving over.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white line and a curb,
                        which [IN-6(6)] prohibits driving over.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The boundaries are solid lines, which [IN-8(3)(a)(iv)] prohibits crossing
                        for a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation unlisted, contradictions
                        ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 630, 9.04 s

lingoqa__evaluation_images_val_192ddf6ced03be1ea37e716d960eb1d4_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead towards
                        a junction with buildings and pedestrians visible. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from a cycle lane and the curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the white dashed
                        line on the left and the solid edge line on the right. | roles: The white dashed line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: The straight arrow is consistent with the lane's direction and boundaries.
                        | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line to the right.
                        [[IN-6(6)]]
Step 5  Rule            arrow:straight: The arrow allows me to proceed straight ahead.
Step 6  change_left     allowed (correct): Allowed by the white dashed line and rule [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the white solid line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (correct): Allowed by the straight arrow in my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action; the arrow
                        only shows straight.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action; the arrow
                        only shows straight.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may proceed straight or change to
                        the left lane, but do not cross the solid line to the right into the cycle lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 5803, out 694, 10.41 s

lingoqa__evaluation_images_val_2a3e08c04123f3cb76368ec6f2800ae6_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road with buildings on the left and right. The road
                        continues straight ahead with no immediate intersection or ramp visible. (lanes 1,
                        mine 1, full)
Step 2  Left            A double solid yellow line separates the road from the curb and sidewalk on the left.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           A single dashed white line is visible on the right, separating my lane from another
                        lane of traffic.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left boundary being an edge
                        line and the right boundary being a lane line, as there is at least one more lane to
                        the right. | roles: The double solid yellow line on the left fits the role of an edge
                        line (parking restriction), and the dashed white line on the right fits the role of a
                        lane line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a double solid yellow line;
                        [IN-6(6)] prohibits driving on or over a solid longitudinal line.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line; [IN-6(1)] allows
                        changing lanes after signaling.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a double solid yellow line; [IN-8(3)(a)(iv)]
                        prohibits U-turns across a continuous single or double solid line.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the double yellow
                        lines on the left or attempt a U-turn across them.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 5803, out 701, 10.15 s

lingoqa__evaluation_images_val_45b587bf54ee9db25085eb483cac242e_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK, leading towards a T-junction or intersection. My car
                        is positioned in the single lane approaching the junction. (lanes 1, mine 1, full)
Step 2  Left            A white solid line separates the lane from the sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white solid line separates the lane from the sidewalk/curb area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:yield_line (full): A white dashed transverse line across the lane before the
                        intersection.; line:crosswalk (full): A white zebra-style pedestrian crossing across
                        the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the presence of edge lines on
                        both sides. | roles: The white solid lines on both sides correctly fit the role of
                        edge lines for a single-lane road. | markings: The yield line and crosswalk are
                        consistent with an approach to an intersection. | unseen: No attributes were reported
                        without being visible. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid line. [IN-6(6)]
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid line. [IN-6(6)]
Step 5  Rule            line:yield_line: The driver shall slow down, give way to traffic on the road he is
                        approaching, and proceed cautiously. [IN-7(3)]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing. [IN-8(2)(e)]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings prohibiting it, though
                        the road layout suggests a junction.
Step 6  turn_left       not_applicable: Not applicable as there is no lane-use arrow governing this movement.
Step 6  turn_right      not_applicable: Not applicable as there is no lane-use arrow governing this movement.
Step 6  u_turn          prohibited: Prohibited by the solid edge lines and rule [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and slow down at the yield line. Give way to any pedestrians on the
                        crosswalk before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:yield_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 789, 16.34 s

lingoqa__evaluation_images_val_590371e02b04e7d99853064a97ed3fe1_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           A residential urban road with houses on the left and trees on the right; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Two solid red lines are painted along the left edge of the roadway next to the curb.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the area where cars are stopped on the
                        right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and the right
                        lane line (which separates the driving lane from a parking/stopping area). | roles:
                        The red double solid lines on the left act as an edge line; the white dashed line on
                        the right acts as a lane line. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: No provided rule covers red double solid lines; by definition, it is an
                        edge line prohibiting parking/stopping. [null]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a double solid edge line and a
                        curb, which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows lane
                        changes according to [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if necessary; do not cross the red lines on the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 5803, out 773, 12.52 s

lingoqa__evaluation_images_val_6522f0c917af4a0d8deb045e07cba594_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with buildings on the right and a park area on
                        the left. The road continues straight ahead. (lanes 3, mine 1, full)
Step 2  Left            A solid white line separates the roadway from a blue-painted bicycle lane and a curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A dashed white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 agree with the left boundary being
                        an edge_line and the right boundary being a lane_line. | roles: The white solid edge
                        line and white dashed lane line fit their respective roles. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        [IN-6(6)] prohibits crossing.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which [IN-6(1)] allows
                        crossing after signaling.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a solid line, which [IN-8(3)(a)(iv)] prohibits
                        crossing for a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right. Do not cross the solid white line on
                        the left into the cycle lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 643, 9.54 s

lingoqa__evaluation_images_val_6fcc62c8231450608cddba5a8e4193cd_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on the right and a sidewalk on the left. The road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A white dashed line separates my lane from a bicycle lane on the left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from a parking area where cars are stopped on
                        the right.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a special lane
                        line on the left and an edge line on the right. | roles: The white dashed patterns fit
                        the roles of a special lane boundary and a roadway edge. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed line allows crossing for lane changes or overtaking, provided
                        it is safe. [null]
Step 5  Rule            right_boundary: A dashed line allows crossing to enter or leave the roadway
                        edge/parking area. [null]
Step 6  change_left     allowed (correct): The left boundary is a dashed line, which allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a dashed line, which allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight in your lane. You may change lanes to the left or right
                        across the dashed lines if safe to do so.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 589, 11.09 s

lingoqa__evaluation_images_val_8127f3b506fa0146a795f0085bb60cd3_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching a pedestrian crossing.
                        (lanes 2, mine 1, full)
Step 2  Left            A raised curb and sidewalk are on the left side of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A white transverse line across the lane before the pedestrian
                        crossing.; line:crosswalk (full): White stripes forming a pedestrian crossing across
                        the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left boundary being
                        a curb and the right boundary being a lane line. | roles: The white dashed line is
                        consistent with a lane line separating traffic in the same direction. | markings: The
                        stop line and crosswalk are standard for an urban intersection/crossing. | unseen: No
                        attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; driving over it is prohibited
                        by definition.
Step 5  Rule            right_boundary: Lane changes across the dashed line are allowed after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            line:stop_line: The car must stop before this line if the traffic signal is red.
                        [[IN-12(1)(a)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians on the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a dashed lane line, which
                        allows lane changes per [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight; it is allowed.
Step 6  turn_left       not_applicable: No arrow or marking governs this action; it is not applicable at this
                        specific crossing point.
Step 6  turn_right      not_applicable: No arrow or marking governs this action; it is not applicable.
Step 6  u_turn          not_applicable: No marking governs this action, but it is not indicated as allowed.
Step 6  enter_waiting_areanot_applicable: No waiting area is present; not applicable.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right if needed. Give way to the pedestrian
                        currently crossing the road.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 768, 13.09 s

lingoqa__evaluation_images_val_88005f114b4afb9e1c9e30c022a1ff6d_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with a
                        pedestrian crossing and a cycle lane to the left. (lanes 1, mine 1, full)
Step 2  Left            A white dashed line separates my lane from a cycle lane on the left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           There is no painted line or curb on the right side of my lane; it is the edge of the
                        carriageway.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left boundary being a special
                        lane line and the right boundary being the edge of the road. | roles: The white dashed
                        line on the left fits the role of a special lane line for the cycle lane. | markings:
                        There are no markings in my lane to contradict. | unseen: No attributes were reported
                        that were not visible. | result: consistent
Step 5  Rule            left_boundary: A dashed line generally allows crossing for lane changes, provided it
                        is safe and signaled. [null]
Step 5  Rule            right_boundary: No specific rule prohibits moving to the right where no line exists,
                        though the edge of the road should be respected. [null]
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a white dashed line; no
                        rule in the provided list prohibits crossing it, and general traffic rules allow lane
                        changes across dashed lines.
Step 6  change_right    allowed (correct): No marking governs this action as there is no line or curb on the
                        right.
Step 6  go_straight     allowed (contested, correct): No marking governs this action; going straight is
                        allowed by default.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action; however, no solid line prohibits it
                        here.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may proceed straight or change lanes if safe. Be mindful
                        of the cycle lane to your left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions True, unsafe [], citation unlisted,
                        contradictions ['change_right decided with nothing marked on that side']
Tokens                  in 5803, out 665, 12.93 s

lingoqa__evaluation_images_val_8acfd91fc5488115f4a96cfb9901b35c_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with shops on the left; the road continues straight
                        ahead towards a distant intersection. (lanes 1, mine 1, full)
Step 2  Left            A solid red line is painted along the edge of the road next to the sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A dashed white line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and right
                        center line. | roles: The red solid edge line and white dashed center line fit their
                        roles for a single-lane road in the UK. | markings: The straight arrow is consistent
                        with the lane's path. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: The red solid line marks the edge of the carriageway; crossing it to
                        leave the road is prohibited. [null]
Step 5  Rule            right_boundary: Lane changes are permitted across a broken line after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow allows the vehicle to proceed straight ahead. [null]
Step 6  change_left     prohibited (contested, label allowed): The left boundary is a solid red edge line and
                        curb, which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed white center line, which allows
                        crossing for overtaking or changing lanes per [IN-6(1)].
Step 6  go_straight     allowed (correct): The straight arrow in the lane allows this movement.
Step 6  turn_left       not_applicable (WRONG, label allowed): No marking governs this action, but the left
                        boundary is a curb.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action, but the
                        right boundary is a center line.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action, but the
                        right boundary is a dashed line.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the photo.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may cross the right boundary to overtake
                        if safe to do so.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 5803, out 700, 23.25 s

lingoqa__evaluation_images_val_97a2a11eb970cb429cf1cf8457123fab_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is a city road with buildings on the left and a sidewalk on the right. The road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A white dashed line separates my lane from a parking area where cars are stopped.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a red-paved cycle lane and a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries; the left is a
                        parking edge and the right is a cycle lane edge. | roles: The white dashed line on the
                        left and solid white line on the right fit the role of edge lines. | markings: There
                        are no markings in my lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: No specific rule prohibits crossing a dashed edge line to enter a
                        parking area, but general lane discipline applies. [null]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a dashed line, and no rule prohibits
                        crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        line, which [IN-6(6)] prohibits driving over.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line into the
                        cycle lane on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 656, 10.27 s

lingoqa__evaluation_images_val_a395b347e02d4f0bf9d69da3ebd52ea4_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road continues straight ahead towards a junction
                        with traffic signals. (lanes 2, mine 1, full)
Step 2  Left            A solid red line is painted along the edge of the road next to the sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The red solid
                        edge line and white dashed lane line fit their respective roles. | markings: The
                        straight-ahead arrow is consistent with the lane's direction and boundaries. | unseen:
                        No attributes were reported without being visible. | result: consistent
Step 5  Rule            left_boundary: The red solid line marks the edge of the carriageway; crossing it to
                        leave the road is prohibited. [null]
Step 5  Rule            right_boundary: Lane changes across the broken white line are allowed after giving a
                        proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow allows the vehicle to proceed straight ahead. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid red edge line and a
                        curb, which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, which allows lane
                        changes per [IN-6(1)].
Step 6  go_straight     allowed (correct): The straight-ahead arrow in the lane allows this movement.
Step 6  turn_left       prohibited (WRONG, label allowed): No marking in my lane allows a left turn; the arrow
                        only shows straight.
Step 6  turn_right      prohibited (correct): No marking in my lane allows a right turn; the arrow only shows
                        straight.
Step 6  u_turn          prohibited (correct): No marking in my lane allows a U-turn; the arrow only shows
                        straight.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 5803, out 706, 11.36 s

lingoqa__evaluation_images_val_a55026aa4029fd3db4f6738006a50675_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road ahead appears
                        to be a single-lane stretch leading toward a junction or narrowing. (lanes 1, mine 1,
                        full)
Step 2  Left            A solid white line separates the lane from a sidewalk/parking area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a sidewalk/parking area on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the presence of edge lines on
                        both sides. | roles: The white solid lines on both sides fit the role of edge lines
                        for a single-lane road. | markings: There are no markings in the lane to contradict
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or waiting areas in the
                        lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or waiting areas in the
                        lane.
Step 6  u_turn          prohibited: Prohibited by the solid white lines and rule [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation unlisted, contradictions
                        ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 641, 11.27 s

lingoqa__evaluation_images_val_b458631e4e946fe134f09a9e979d6347_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead towards
                        a distant intersection. (lanes 2, mine 1, full)
Step 2  Left            A raised curb with a red line painted along the edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The white dashed
                        line fits the role of a lane line. | markings: The straight arrow is consistent with
                        the lane boundaries. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: The curb and red line mark the edge of the roadway; crossing it is
                        prohibited as it is a physical barrier. [null]
Step 5  Rule            right_boundary: Lane changes are allowed across a dashed line after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow allows the vehicle to proceed straight ahead. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the physical curb (left_boundary).
Step 6  change_right    allowed (correct): allowed by the dashed white line (right_boundary) and rule
                        [IN-6(1)].
Step 6  go_straight     allowed (correct): allowed by the straight arrow in the lane.
Step 6  turn_left       prohibited (WRONG, label allowed): prohibited by the straight arrow in the lane.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as no arrow governs this
                        movement and it is not a right-turn lane.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as no marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area in view.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_left']), actions False, unsafe [],
                        citation unlisted, contradictions []
Tokens                  in 5803, out 670, 11.13 s

lingoqa__evaluation_images_val_ce3084593e16b501a27dbbef7b2aa653_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK, leading towards a junction with a pedestrian crossing
                        ahead. My car is positioned in the single lane of its direction. (lanes 1, mine 1,
                        full)
Step 2  Left            A solid white line marks the left edge of the roadway, beyond which is a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, beyond which is a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): A white zebra crossing is painted across the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the presence of edge lines on
                        both sides. | roles: The white solid lines on both sides fit the role of edge lines
                        for a single-lane urban road. | markings: The crosswalk is a standard transverse
                        marking across the lane. | unseen: No attributes were reported without being visible.
                        | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at uncontrolled pedestrian
                        crossings. [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict continuing straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or prohibited-movement marking
                        governing this.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or prohibited-movement marking
                        governing this.
Step 6  u_turn          prohibited: Prohibited by the solid white edge lines and rule [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Give way to any pedestrians crossing the zebra
                        crossing ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 713, 11.81 s

lingoqa__evaluation_images_val_d082bdc55d81a79652063c87996514aa_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road ahead is straight with no
                        immediate intersection or ramp visible. My car is in the rightmost lane of the road.
                        (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane to the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A solid red line marks the edge of the roadway next to a curb.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and an edge line on the right. | roles: The solid white
                        line fits the role of a special lane boundary, and the red line fits the role of an
                        edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        [IN-6(6)] prohibits crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid red line and a curb,
                        which [IN-6(6)] prohibits crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The boundaries are solid lines, which [IN-8(3)(a)(iv)] prohibits crossing
                        for a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Do not cross the solid lines to the
                        left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 654, 10.62 s

lingoqa__evaluation_images_val_e99f7824f2219b27f6bddc184eb505c1_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with a
                        bus stopped in a lane to the left. (lanes 2, mine 2, full)
Step 2  Left            A white solid line separates my lane from the bus lane to the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A grey metal railing and a curb form the right edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and an edge line on the right. | roles: The white solid
                        line fits the role of a special lane line (bus lane boundary), and the curb fits the
                        role of an edge line. | markings: There are no markings in my lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The curb marks the edge of the roadway and prohibits leaving the road.
                        [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid line, which [IN-6(6)]
                        prohibits crossing.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb, which prohibits
                        leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line into the bus
                        lane or cross the curb on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:speed_limit']), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5803, out 615, 7.06 s

lingoqa__evaluation_images_val_f376bb31c1f1f01cb9aa5c2887800ab1_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with traffic moving on the left. The road ahead
                        continues straight with vehicles in front. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A red solid line is painted along the edge of the road next to the curb.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the red solid line at the curb fits the role of an edge line.
                        | markings: The straight arrow is consistent with the lane's path. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I shall drive within the lane and may change lanes after giving a
                        proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over a solid longitudinal line. [[IN-6(6)]]
Step 5  Rule            arrow:straight: The arrow allows me to proceed straight ahead.
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line and rule [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid red edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (correct): Allowed by the straight arrow in my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable as there is no left-turn
                        arrow in my lane.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable as there is no right-turn
                        arrow in my lane.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no U-turn arrow
                        in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may change to the left lane if needed, but do
                        not cross the red line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 704, 12.01 s

lingoqa__evaluation_images_val_fee75bebc1fae19b92ee5fd77e6eecb7_2 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead towards
                        a junction with traffic lights. (lanes 3, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both my left and right. | roles: The white dashed patterns are
                        consistent with lane lines separating traffic in the same direction. | markings: The
                        straight-ahead arrow is consistent with a central lane in a multi-lane road. | unseen:
                        No attributes were reported without being visible. | result: consistent
Step 5  Rule            left_boundary: I shall drive within the lane and may change lanes after giving a
                        proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall drive within the lane and may change lanes after giving a
                        proper signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow allows me to proceed straight ahead.
Step 6  change_left     allowed (correct): The left boundary is a white dashed lane line, which allows lane
                        changes per [IN-6(1)].
Step 6  change_right    allowed (correct): The right boundary is a white dashed lane line, which allows lane
                        changes per [IN-6(1)].
Step 6  go_straight     allowed (correct): The arrow in my lane specifically allows going straight.
Step 6  turn_left       prohibited (correct): No marking in my lane allows a left turn; the arrow only shows
                        straight.
Step 6  turn_right      prohibited (correct): No marking in my lane allows a right turn; the arrow only shows
                        straight.
Step 6  u_turn          prohibited (correct): No marking in my lane allows a U-turn; the arrow only shows
                        straight.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, you must change
                        lanes first.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 706, 12.21 s

lingoqa__train_158fe8e268d93d340d564184b41ac65e_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom with buildings and trees lining the sides;
                        the road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I may change lanes across this dashed line after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over this solid line. [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the white dashed lane line and rule
                        [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the white solid edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no markings governing this movement,
                        though crossing the right boundary is prohibited by [IN-6(6)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane
                        after signaling; do not cross the solid line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 651, 11.48 s

lingoqa__train_1d19421a315491db945049675540d325_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The road continues straight ahead, passing a bus stop
                        area on the left. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the right edge of the roadway, with a sidewalk beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the presence of a
                        lane line on the left and an edge line on the right. | roles: The white dashed line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line to the right.
                        [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the white dashed lane line and rule
                        [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the white solid edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement, though
                        the right boundary prohibits crossing it.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane if
                        needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 645, 10.52 s

lingoqa__train_3973acbe0b3b5883aad991111ac25658_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. Ahead is a junction with a traffic signal and a
                        pedestrian crossing. My car is in the lane approaching the junction. (lanes 1, mine 1,
                        full)
Step 2  Left            A solid white line separates the lane from a cycle lane or shoulder on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a parking area or opposite traffic lane on
                        the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A white transverse line across the lane before the pedestrian
                        crossing.; line:crosswalk (full): White stripes across the road for pedestrians.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries being edge lines.
                        | roles: The white solid lines fit the role of edge lines in this urban context. |
                        markings: The stop line and crosswalk are consistent with an intersection approach. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single longitudinal solid line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 5  Rule            line:stop_line: The driver shall stop before the stop line when facing a red light.
                        [[IN-12(1)(a)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white left boundary and rule
                        [IN-6(6)].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white right boundary and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking prohibits it and it is the natural
                        path of the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow in my lane.
Step 6  u_turn          prohibited: Prohibited by the solid boundaries and rule [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Stop before the stop line if the traffic
                        signal is red and yield to pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions None, unsafe [], citation
                        unlisted, contradictions ['u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 5803, out 789, 12.0 s

lingoqa__train_3c118fd985ea813c22cb8f98dc969354_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on the left. The road continues straight ahead
                        towards a distant intersection. (lanes 2, mine 1, full)
Step 2  Left            A raised stone curb separates the road from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The white dashed
                        line is consistent with a lane line separating traffic in the same direction. |
                        markings: The straight arrow is consistent with the lane's path. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; crossing it is prohibited as it
                        is a physical barrier. [null]
Step 5  Rule            right_boundary: I may change lanes across the dashed line after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            arrow:straight: The arrow allows me to proceed straight ahead. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (contested, correct): The right boundary is a dashed lane line, which allows
                        lane changes per [IN-6(1)].
Step 6  go_straight     allowed (correct): The straight arrow in my lane allows this movement.
Step 6  turn_left       prohibited (correct): No marking governs this action, but the curb prohibits turning
                        left here.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line', 'symbol:bike']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 5803, out 661, 11.75 s

lingoqa__train_5b8bca960f1f1db0ab958d3f0468491e_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 1, full)
Step 2  Left            A red line is painted along the edge of the road on the left, next to the sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The red solid
                        line on the left fits the role of an edge line (parking restriction), and the white
                        dashed line on the right fits the role of a lane line. | markings: There are no
                        markings in my lane to contradict. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: The red line is a parking restriction and does not govern driving
                        movements. [null]
Step 5  Rule            right_boundary: I shall drive within the lane and may change lanes after giving a
                        proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is an edge line with a curb;
                        crossing it is prohibited.
Step 6  change_right    allowed (correct): The right boundary is a dashed lane line, which allows lane changes
                        according to [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action, but it is not prohibited by any
                        visible line in the current stretch.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may continue straight or change to the right lane if
                        needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 632, 12.17 s

lingoqa__train_6e75a948a141d9d4c61555dcd4a5647c_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with no
                        immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the roadway, with a sidewalk and railing beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the presence of a
                        lane line on the left and an edge line on the right. | roles: The white dashed line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line. [[IN-6(6)]]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line and rule [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or waiting areas in my
                        lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or waiting areas in my
                        lane.
Step 6  u_turn          not_applicable: Not applicable as there are no markings governing U-turns in this
                        stretch.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane if
                        needed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 636, 10.3 s

lingoqa__train_762eb6ccbf33e80e3c600aefbd51d0a9_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides. The road ahead is straight with no
                        immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from a red-painted area on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the white dashed
                        line on the left and the edge line on the right. | roles: The white dashed line fits
                        the role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line. [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): The white dashed lane line allows changing
                        lanes according to [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): The white solid edge line prohibits crossing it
                        according to [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 618, 22.03 s

lingoqa__train_8afed745d85e70b5320d331336bfa686_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a bus lane to its left; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A solid white line separates my lane from a bus lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A dashed white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left (bus lane) and a lane line on the right. | roles: The
                        solid white line for a special lane and dashed white line for a lane line are
                        consistent with their roles. | markings: There are no markings in my lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid white line [IN-6(6)]
                        separating my lane from the bus lane.
Step 6  change_right    allowed (correct): Allowed by the dashed white line [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no marking governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not enter the bus lane to your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 5803, out 780, 11.64 s

lingoqa__train_8b4478ffa676fe11532a753aaa84bad9_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road with shops on the right. The road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            A white solid line separates the lane from a parking area on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A raised concrete curb forms the right edge of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a white solid
                        edge line on the left and a curb on the right. | roles: The white solid line on the
                        left and the curb on the right both fit the role of edge lines. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid white line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The curb defines the edge of the roadway and prohibits leaving the
                        road. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        [IN-6(6)] prohibits driving over.
Step 6  change_right    prohibited (contested, correct): The right boundary is a curb, which physically
                        prohibits leaving the lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a solid line, which [IN-8(3)(a)(iv)] prohibits
                        crossing for a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line on the left
                        or the curb on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 616, 21.76 s

lingoqa__train_94ed4692ec2e63b4d6c6c74e18bebf9a_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead towards
                        an intersection with traffic signals. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A grey raised curb and a metal railing form the right edge of the road.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in my lane.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the curb fits the role of an edge line. | markings: The
                        straight arrow is consistent with the lane's path and boundaries. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I must drive within the lane and may change lanes after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The curb prohibits leaving the roadway to the right. [null]
Step 5  Rule            arrow:straight: The arrow allows me to proceed straight ahead. [null]
Step 6  change_left     allowed (correct): Allowed by the white dashed lane line and rule [IN-6(1)].
Step 6  change_right    prohibited (contested, correct): Prohibited by the physical curb and railing.
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed by the straight arrow in my lane.
Step 6  turn_left       prohibited (correct): No marking governs this action, but the straight arrow restricts
                        movement to straight ahead.
Step 6  turn_right      prohibited (WRONG, label allowed): No marking governs this action, but the straight
                        arrow restricts movement to straight ahead.
Step 6  u_turn          prohibited: No marking governs this action, but the straight arrow restricts movement
                        to straight ahead.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation unlisted, contradictions []
Tokens                  in 5803, out 671, 11.47 s

lingoqa__train_95c9eedfeefe6164b2047d3818abf472_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with
                        parked cars on the right side. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from a parking area on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        lane line on the left and an edge line on the right. | roles: The white dashed line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid white line to the right.
                        [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the dashed white lane line and rule
                        [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or waiting areas in my
                        lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or waiting areas in my
                        lane.
Step 6  u_turn          not_applicable: Not applicable as there are no markings governing U-turns in this
                        stretch.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost driving lane. You may continue straight or change to the left
                        lane, but do not cross the solid line to the right into the parking area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 653, 10.52 s

lingoqa__train_9a9318bc560cdeb5fa6fe82739d6e31a_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with shops on both sides, proceeding straight
                        ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway, with a parking area and sidewalk
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the white dashed lane line and rule
                        [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the white solid edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no markings governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 774, 12.39 s

lingoqa__train_a6d4392c47e82bcb0f97dd4430f37484_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings and trees on both sides; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from a bus lane to the left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           A white dashed line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        special lane line on the left and a center line on the right. | roles: The white
                        dashed patterns fit the roles of a special lane boundary and a center line in this
                        context. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: My car, not being a bus, is prohibited from driving in the special bus
                        lane. [[IN-6(3)]]
Step 5  Rule            right_boundary: I may change lanes across the dashed line after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: The rule against crossing solid lines does not apply here as the line
                        is dashed. [[IN-6(4)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a special lane line for buses,
                        and rule [IN-6(3)] prohibits other vehicles from entering it.
Step 6  change_right    allowed (correct): The right boundary is a dashed center line, and rule [IN-6(1)]
                        allows lane changes across dashed lines.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and nothing restricts
                        carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move to the right if necessary; do not enter the bus lane to your
                        left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 668, 12.39 s

lingoqa__train_b1c4ab69f9c1c6bbf7dbfdf1fd160bf7_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings and shops on both sides. The road continues
                        straight ahead with a dividing island to the right. (lanes 1, mine 1, full)
Step 2  Left            A white dashed line separates my lane from a parking or service area on the left.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           A white solid line separates my lane from a concrete traffic island on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries; there is an edge
                        line on the left and a solid line/curb on the right. | roles: The white dashed line on
                        the left and white solid line on the right are consistent with edge markings in this
                        urban context. | markings: There are no markings in the lane to contradict. | unseen:
                        No attributes were reported without being visible. | result: consistent
Step 5  Rule            left_boundary: No specific rule prohibits crossing a white dashed edge line, but the
                        driver should stay within the lane unless changing lanes according to general rules.
                        [null]
Step 5  Rule            right_boundary: The driver shall not drive on or over a single longitudinal solid
                        line. [[IN-6(6)]]
Step 6  change_left     allowed (contested, label prohibited): The white dashed line is not a solid line
                        prohibiting movement, and [IN-6(1)] allows lane changes with proper signaling.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid line and a curb,
                        which [IN-6(6)] prohibits driving over.
Step 6  go_straight     allowed (contested, correct): No markings restrict going straight in this lane.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      prohibited: The right boundary is a solid line and curb, and no arrow allows a right
                        turn.
Step 6  u_turn          prohibited: The right boundary is a solid line, which [IN-8(3)(a)(iv)] prohibits
                        crossing for a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in view.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid line or curb to the
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['turn_right,
                        u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 5803, out 670, 11.12 s

lingoqa__train_b72ec4fa519e91678efc0ed0f506772f_3 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway next to a sidewalk.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A white circle containing the number 20 is painted on the
                        road surface.
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: The speed limit marking is consistent with the road type and boundaries. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I shall drive within the lane and may change lanes after giving a
                        proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid longitudinal line. [[IN-6(6)]]
Step 5  Rule            text:speed_limit: This is an informative marking indicating the speed limit and does
                        not govern the seven actions.
Step 6  change_left     allowed (contested, correct): Allowed by the white dashed lane line and rule
                        [IN-6(1)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the white solid edge line and rule
                        [IN-6(6)].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings prohibiting it and it
                        is the natural path of the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement, though
                        crossing the right boundary is prohibited by [IN-6(6)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the solid line on the right. Observe the 20 mph speed limit.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 743, 12.3 s

lingoqa__train_be3bc3f2632c3e8246ed7e87f9174829_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with buildings on both sides; the road continues
                        straight ahead. (lanes 2, mine 1, full)
Step 2  Left            A white solid line separates the roadway from the sidewalk/parking area on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The white solid
                        edge line and white dashed lane line fit their respective roles. | markings: There are
                        no markings in my lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall drive within the lane and change lanes only after
                        giving a proper signal. [[IN-6(1)]]
Step 5  Rule            right_boundary: Overtaking from the left is permitted if driving on a multi-lane road
                        in a marked lane. [[IN-14(2)(a)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid line, which prohibits
                        driving over it per [IN-6(6)].
Step 6  change_right    allowed (contested, label prohibited): The right boundary is a dashed lane line, which
                        allows lane changes per [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and nothing restricts
                        carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may continue straight or change to the right lane, but
                        do not cross the solid line on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 5803, out 665, 11.7 s

lingoqa__train_dd7bd3bab81865ff4917d1b3a2162372_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road ahead is straight with parked
                        vehicles on the right side. (lanes 1, mine 1, full)
Step 2  Left            I see a white dashed line on the left, with another lane of traffic moving in the same
                        direction beyond it.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           I see a single yellow solid line on the right, next to a curb and parked vehicles.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 are consistent with the left
                        boundary being a lane line (indicating another lane to the left) and the right
                        boundary being an edge line. | roles: The white dashed line fits the role of a lane
                        line, and the yellow solid line on the curb side fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I am prohibited from parking where there is a continuous yellow line
                        on the curb side. [[IN-22.(2)(j)]]
Step 6  change_left     allowed (correct): The left boundary is a white dashed lane line, which allows lane
                        changes according to [IN-6(1)].
Step 6  change_right    prohibited (contested, correct): The right boundary is a yellow solid edge line and a
                        curb; [IN-6(6)] prohibits driving over a solid line.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the yellow line on
                        the right or park along the curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 5803, out 662, 12.25 s
```
