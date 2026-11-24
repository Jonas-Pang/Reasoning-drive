# Reasoning of lane run 20261117_040242_laneC_UK

```text
lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom with shops on both sides; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a parking or shoulder area on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           There is no painted line on the right, but a curb and parked cars are visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries being edge lines
                        on both sides. | roles: The white solid line on the left and the curb on the right fit
                        the role of edge lines. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: No specific rule provided for a curb edge line, but it defines the
                        physical limit of the roadway. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        [IN-6(6)] prohibits driving over.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb, which physically
                        prohibits leaving the lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a solid line, which [IN-8(3)(a)(iv)] prohibits
                        crossing for a U-turn.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line on the left
                        or the curb on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 5796, out 625, 13.26 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road ahead is straight with no
                        immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            I see a grey curb and a sidewalk to the left of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           I see a white dashed line separating my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge/curb and the right boundary being a lane line. | roles: The white dashed
                        line is consistent with a lane line separating traffic in the same direction. |
                        markings: There are no markings in my lane to contradict. | unseen: I have not
                        reported any attributes I did not see. | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; driving over it is prohibited
                        by definition of the roadway edge.
Step 5  Rule            right_boundary: I shall drive within the lane and may change lanes after giving a
                        proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, and rule [IN-6(1)]
                        allows lane changes after signaling.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right
                        after signaling.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 5796, out 610, 27.35 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street in the United Kingdom with buildings on both sides; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line is painted along the left edge of the road next to the
                        curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left boundary being an edge
                        line and the right boundary being unmarked. | roles: The yellow solid line on the left
                        fits the role of an edge line (parking restriction). | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs this unmarked boundary.
Step 6  change_left     prohibited (contested, label not_determined): The left boundary is a solid yellow
                        line, and [IN-6(6)] prohibits driving over a solid longitudinal line.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action.
Step 6  go_straight     allowed (contested, label not_determined): No marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          allowed: No marking governs this action, but [IN-8(3)(a)(iv)] prohibits U-turns across
                        solid lines; however, the right side is unmarked.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the left or
                        park there.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 5796, out 627, 15.0 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street with buildings on both sides. A red bus is ahead in the
                        distance, and there is a yellow box junction ahead of my car. (lanes 1, mine 1, full)
Step 2  Left            A grey curb separates the road from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right, but parked cars are present along the edge of
                        the road.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): A yellow box junction with criss-cross lines is painted across the
                        lane.
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the boundaries
                        being edge lines on both sides. | roles: The absence of paint and presence of a curb
                        on the left and parked cars on the right fit the role of edge lines. | markings: The
                        yellow box junction is a standard area marking across the lane. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; crossing it is prohibited as it
                        leads to the sidewalk.
Step 5  Rule            right_boundary: The right edge of the road is not marked by paint, but is bounded by
                        parked vehicles.
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    not_applicable (WRONG, label not_determined): No marking governs this action, but the
                        presence of parked cars and the road edge makes it not applicable for a lane change.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight; it is allowed.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action, but it is generally allowed if safe
                        and not prohibited by signs.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop inside the yellow box junction
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 5796, out 707, 29.02 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides. A red bus is ahead in the
                        distance, and several cars are parked on the right side of the road. (lanes 1, mine 1,
                        full)
Step 2  Left            A single solid yellow line is painted along the left edge of the road, next to a
                        sidewalk.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right, but parked cars and a curb define the edge of
                        the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries, as both
                        sides are edge lines. | roles: The yellow solid line on the left is a typical edge
                        line for parking restrictions; the right side is a physical edge. | markings: There
                        are no markings in the lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule provided for a non-painted curb boundary, but it
                        defines the road edge. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow line, and
                        [IN-6(6)] prohibits driving over a solid longitudinal line.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb, which physically
                        prohibits leaving the lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there are no
                        restrictions to proceeding straight.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a solid line, and [IN-8(3)(a)(iv)] prohibits U-turns
                        across a continuous solid line.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the left or
                        the curb on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 5796, out 680, 14.01 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on both sides; the road continues straight ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line separates my lane from the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
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
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along my lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement, though
                        crossing the right boundary is prohibited by [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your lane or change to the left lane after signaling. Do
                        not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5796, out 647, 14.89 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with a
                        bus stopped on the left side. (lanes 2, mine 1, full)
Step 2  Left            A red solid line is painted along the edge of the road next to the sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left boundary
                        being an edge line and the right boundary being a lane line. | roles: The red solid
                        line on the left fits the role of an edge line (red route), and the white dashed line
                        on the right fits the role of a lane line. | markings: There are no markings in my
                        lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: The red solid line marks the edge of the carriageway; crossing it to
                        leave the road is prohibited. [null]
Step 5  Rule            right_boundary: Changing lanes across the dashed line is allowed after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid edge line and a curb,
                        which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed lane line, which allows lane changes
                        according to [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may continue straight or change to the right lane if
                        needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5796, out 627, 15.05 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road ahead appears to be a straight
                        stretch with parked cars on the right and a sidewalk on the left. (lanes 1, mine 1,
                        full)
Step 2  Left            I see a raised concrete curb and a sidewalk to the left of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           I see a white dashed line separating my lane from a parking area where cars are
                        stopped.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the left boundary being
                        an edge (curb) and the right boundary being a lane line (separating the driving lane
                        from parking). | roles: The white dashed line on the right is consistent with a lane
                        line separating traffic from a parking/stopping area. | markings: There are no
                        markings in the lane, which is consistent with a standard urban road stretch. |
                        unseen: I have not reported any attributes not visible in the image. | result:
                        consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; driving over it is prohibited
                        by definition of the roadway edge.
Step 5  Rule            right_boundary: The driver shall drive within the lane and may change lanes after
                        giving a proper signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the left boundary (curb) which defines
                        the edge of the road.
Step 6  change_right    allowed (correct): allowed by the white dashed line and rule [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this action.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this action.
Step 6  u_turn          allowed: allowed as there are no solid lines or signs prohibiting it in this stretch.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane to proceed straight. You may move to the right if needed, but do not
                        cross the curb on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 5796, out 678, 15.32 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on both sides; the road continues straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A grey concrete curb separates the road from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left curb acting as an edge
                        line. | roles: The left boundary is a curb, which fits the role of an edge line. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; crossing it is prohibited as it
                        leads to the sidewalk.
Step 5  Rule            right_boundary: No marking governs this side.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, and crossing it onto the
                        sidewalk is prohibited.
Step 6  change_right    allowed (correct): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may proceed straight or move to the right, but do not
                        cross the curb on the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation none, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 5796, out 575, 25.57 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road with buildings and parked cars on both sides. The
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line is painted on the left side of the lane, next to the curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right side, only a curb with parked cars.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The word 'BUS' is painted in yellow in the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries being edge lines
                        on both sides. | roles: The yellow solid line on the left is a typical edge line for
                        parking restrictions; the right side is a physical curb. | markings: The 'BUS' text
                        indicates this is a special lane for buses. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over the solid yellow line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: No specific rule for a non-painted boundary, but the curb physically
                        limits movement.
Step 5  Rule            text:bus: No vehicle of any other class than buses shall be driven in this lane.
                        [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid yellow line [IN-6(6)].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the physical curb and the absence of
                        a lane to change into.
Step 6  go_straight     prohibited (contested, label allowed): Prohibited because the lane is reserved for
                        buses [IN-6(3)].
Step 6  turn_left       prohibited: Prohibited because the lane is reserved for buses [IN-6(3)].
Step 6  turn_right      prohibited: Prohibited because the lane is reserved for buses [IN-6(3)].
Step 6  u_turn          prohibited: Prohibited because the lane is reserved for buses [IN-6(3)].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane. You should leave this lane immediately if you are not
                        driving a bus, as it is reserved for specified vehicles.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation unlisted,
                        contradictions ['go_straight, turn_left, turn_right, u_turn decided without an arrow
                        or prohibited-movement marking']
Tokens                  in 5796, out 714, 17.55 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides; the road continues straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is painted along the edge of the road next to a curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 are consistent with the left
                        boundary being an edge line and the right boundary being unmarked. | roles: The yellow
                        solid line on the left fits the role of an edge line (kerb side). | markings: There
                        are no markings in the lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs this unmarked boundary.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow line, and
                        [IN-6(6)] prohibits driving on or over a solid longitudinal line.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          allowed: No marking governs this action, but [IN-8(3)(a)(iv)] prohibits U-turns across
                        solid lines; however, the right side is unmarked.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or move to the right. Do not cross the solid yellow line on
                        the left or park along it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 5796, out 633, 14.71 s
```
