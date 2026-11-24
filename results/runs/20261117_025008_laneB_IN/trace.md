# Reasoning of lane run 20261117_025008_laneB_IN

```text
idd__primary_d1_leftCamImgs_0000529 | lane | Test B | gemma4:31b
----------------------------------------------------------------
Step 1  Scene           This is a narrow urban road in India with buildings and trees on both sides. The road
                        continues straight ahead with some parked vehicles and a motorcyclist in the distance.
                        (lanes 1, mine 1, full)
Step 2  Left            A white solid line is visible on the left edge of the road, separating the lane from a
                        dirt shoulder and parked motorcycles.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A white solid line is visible on the right edge of the road, separating the lane from
                        a dirt shoulder and vegetation.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries, as both
                        are edge lines. | roles: The white solid lines on both sides fit the role of edge
                        lines for a single-lane road. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid line. [[IN-6(6)]]
Step 6  change_left     prohibited (correct): The left boundary is a solid line, which [IN-6(6)] prohibits
                        driving over.
Step 6  change_right    prohibited: The right boundary is a solid line, which [IN-6(6)] prohibits driving
                        over.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The boundaries are solid lines, and [IN-8(3)(a)(iv)] prohibits U-turns
                        across them.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid edge lines on either
                        side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 5785, out 645, 65.54 s

idd__primary_d1_leftCamImgs_0000786 | lane | Test B | gemma4:31b
----------------------------------------------------------------
Step 1  Scene           A residential road in India with buildings on both sides; the road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line marks the left edge of the roadway next to a driveway and fence.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway next to a driveway and fence.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the presence of edge
                        lines on both sides. | roles: The white solid lines on both sides are consistent with
                        edge lines for a single-lane residential road. | markings: There are no markings in
                        the lane, which is consistent with a simple residential road. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid white line. [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver shall not drive on or over the solid white line.
                        [[IN-6(6)]]
Step 6  change_left     prohibited (correct): The left boundary is a solid white line, and [IN-6(6)] prohibits
                        driving over it.
Step 6  change_right    prohibited: The right boundary is a solid white line, and [IN-6(6)] prohibits driving
                        over it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The boundaries are solid lines, and [IN-8(3)(a)(iv)] prohibits U-turns
                        across continuous solid lines.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 5785, out 634, 59.96 s

idd__primary_d1_leftCamImgs_0002250 | lane | Test B | gemma4:31b
----------------------------------------------------------------
Step 1  Scene           This is an urban road in India with buildings and shops on both sides. The road ahead
                        is straight with no immediate intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            There is no painted line on the left, but the lane is bounded by a curb and parked
                        vehicles.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A raised concrete curb separates my lane from the opposite direction of traffic.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both sides are
                        bounded by curbs/edges rather than lane lines. | roles: The absence of paint and
                        presence of curbs fit the role of edge boundaries. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The curb defines the edge of the roadway; crossing it is prohibited as
                        it is a physical barrier.
Step 5  Rule            right_boundary: The curb defines the edge of the roadway; crossing it is prohibited as
                        it is a physical barrier.
Step 6  change_left     prohibited: prohibited by the physical curb and edge boundary.
Step 6  change_right    prohibited (contested, correct): prohibited by the physical curb and edge boundary.
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or intersection is in view.
Step 6  turn_right      not_applicable: not_applicable as no arrow or intersection is in view.
Step 6  u_turn          prohibited: prohibited by the physical curb on both sides.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not attempt to cross the curbs on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation none_needed, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 5785, out 750, 54.9 s

idd__primary_d1_leftCamImgs_0002357 | lane | Test B | gemma4:31b
----------------------------------------------------------------
Step 1  Scene           This is a two-way urban road with buildings on both sides. My car is in the left lane
                        of its direction, and there is a curb to the right separating the road from the
                        opposite direction's traffic. (lanes 1, mine 1, full)
Step 2  Left            There is no painted line on the left, only the edge of the roadway next to parked
                        motorcycles and a sidewalk.
                        none none, curb no, edge_line, evidence full
Step 2  Right           A raised concrete curb separates my lane from the opposite direction of traffic.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries: no
                        lane line on the left and a curb on the right. | roles: The absence of paint and
                        presence of a curb fit the role of edge boundaries. | markings: There are no markings
                        in my lane to contradict. | unseen: No attributes were reported that were not visible.
                        | result: consistent
Step 5  Rule            left_boundary: No specific rule prohibits leaving the lane to the left, provided it is
                        safe and not over a solid line (none present).
Step 5  Rule            right_boundary: The driver shall not drive on or over the physical curb. [[IN-6(6)]]
Step 6  change_left     allowed: no marking governs this action
Step 6  change_right    prohibited (contested, correct): the right boundary is a curb, and [IN-6(6)] prohibits
                        driving over it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       allowed: no marking governs this action
Step 6  turn_right      prohibited: the right boundary is a curb, and [IN-6(6)] prohibits driving over it
Step 6  u_turn          allowed: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may proceed straight or turn left, but do not cross the
                        curb on your right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['change_left decided
                        with nothing marked on that side', 'turn_left, turn_right, u_turn decided without an
                        arrow or prohibited-movement marking']
Tokens                  in 5785, out 629, 21.87 s
```
