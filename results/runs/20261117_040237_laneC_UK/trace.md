# Reasoning of lane run 20261117_040237_laneC_UK

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
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the edge lines on both sides. |
                        roles: The white solid line on the left and the curb on the right fit the role of edge
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: No specific rule provided for a curb edge, but it defines the physical
                        limit of the roadway. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        [IN-6(6)] prohibits driving over.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb, which physically
                        prohibits leaving the lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action, but the boundaries prohibit crossing
                        them to perform one.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white line on the left
                        or the curb on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5796, out 609, 14.86 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with
                        buildings on the left and trees on the right. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway, with a sidewalk and trees beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the presence of a
                        lane line on the left and an edge line on the right. | roles: The white dashed line
                        fits the role of a lane line, and the white solid line fits the role of an edge line.
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: I may change lanes to the left after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            right_boundary: I shall not drive on or over the solid longitudinal line on the right.
                        [[IN-6(6)]]
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
                        though crossing the right boundary is prohibited by [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of a two-lane road. You may proceed straight or change
                        to the left lane, but do not cross the solid line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5796, out 671, 21.56 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street with buildings on both sides. The road ahead appears to be a
                        continuous stretch of city road with vehicles in front. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is painted along the left edge of the road next to the curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 are consistent with the left
                        boundary being an edge_line. | roles: The yellow solid line on the left fits the role
                        of an edge_line (curb side). | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs this boundary as no marking is present.
Step 6  change_left     prohibited (contested, label not_determined): The left boundary is a solid yellow
                        line, and [IN-6(6)] prohibits driving on or over a solid longitudinal line.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action.
Step 6  go_straight     allowed (contested, label not_determined): No marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a solid line, and [IN-8(3)(a)(iv)] prohibits U-turns
                        across a continuous solid line.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid yellow line on the left
                        or park along it.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 5796, out 640, 16.14 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street with buildings on both sides. Ahead is a clear road with a red
                        bus in the distance; there is no immediate intersection or ramp. (lanes 1, mine 1,
                        full)
Step 2  Left            I see a curb and a sidewalk on the left side of the road.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           I see a white dashed line separating my lane from a parking area on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A yellow box junction with a criss-cross pattern is painted across
                        the lane.
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the left curb and right
                        lane line. | roles: The white dashed line on the right fits the role of a lane line
                        separating the driving lane from a parking/stopping area. | markings: The yellow box
                        junction is a standard area marking across the lane. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway and prohibits leaving the road
                        to the left.
Step 5  Rule            right_boundary: The dashed line allows lane changes after giving a proper signal.
                        [[IN-6(1)]]
Step 5  Rule            area:grid: A vehicle shall not be stopped on a yellow box marked on road.
                        [[IN-22.(1)viii]]
Step 6  change_left     prohibited (contested, correct): prohibited by the left curb (edge_line).
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the white dashed line and rule
                        [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it and the lane does not
                        end.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  u_turn          allowed: allowed as there are no solid lines or signs prohibiting it in this stretch.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a single driving lane. You may move to the right into the parking area if
                        needed, but do not stop within the yellow box junction ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 5796, out 714, 23.96 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides; a red bus is ahead in the same
                        direction. My car is in the only available driving lane. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line is painted along the left edge of the road, next to a
                        sidewalk.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right, but parked cars and a curb define the edge of
                        the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both sides are
                        edge lines. | roles: The yellow solid line on the left and the curb on the right fit
                        the role of edge lines. | markings: There are no markings in my lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule provided for a non-painted right edge with a curb,
                        but it defines the roadway boundary. [null]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow line, and
                        [IN-6(6)] prohibits driving over a solid longitudinal line.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb, which physically
                        prohibits leaving the lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a solid line, and [IN-8(3)(a)(iv)] prohibits U-turns
                        across a continuous solid line.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the left or
                        attempt a U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 5796, out 673, 16.18 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on both sides; the road continues straight ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway, with a sidewalk and shops beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported that were not visible. | result: consistent
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
Step 6  u_turn          not_applicable: Not applicable as there are no markings governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5796, out 625, 15.71 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom. The road continues straight ahead with no
                        immediate intersection or ramp visible. (lanes 2, mine 1, full)
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
                        leave the road is generally prohibited. [null]
Step 5  Rule            right_boundary: Changing lanes across the dashed line is allowed after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid edge line and a curb,
                        which prohibits leaving the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed lane line, which allows lane changes
                        according to [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the left lane. You may continue straight or change to the right lane if
                        needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 5796, out 629, 16.18 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK, looking straight ahead towards a junction. My car is
                        in the leftmost lane of the road. (lanes 1, mine 1, full)
Step 2  Left            A raised concrete curb separates the road from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from a parking area or another lane on the
                        right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left boundary being a curb
                        (edge) and the right boundary being a lane line. | roles: The white dashed line on the
                        right is consistent with a lane line. | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; crossing it is prohibited as it
                        is a physical barrier.
Step 5  Rule            right_boundary: Lane changes are allowed across a dashed line after giving a proper
                        signal. [[IN-6(1)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the physical curb (left_boundary).
Step 6  change_right    allowed (correct): allowed by the white dashed line (right_boundary) and rule
                        [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable as no marking governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane if
                        needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 5796, out 611, 14.53 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with shops on both sides; the road ahead is straight with no
                        immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            I see a grey concrete curb and a sidewalk with pedestrians and shops beyond it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           I see a dark asphalt surface with parked cars and no painted line.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries, as both
                        sides are edge boundaries (curb on left, parking area on right). | roles: The absence
                        of paint and presence of a curb on the left and parking on the right fit the role of
                        edge lines. | markings: There are no markings in the lane to contradict. | unseen: I
                        have not reported any attributes not visible in the photo. | result: consistent
Step 5  Rule            left_boundary: The curb defines the edge of the roadway; crossing it is prohibited as
                        it leads to a sidewalk.
Step 5  Rule            right_boundary: The right boundary is the edge of the travel lane; crossing it leads
                        to a parking area.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway onto the sidewalk.
Step 6  change_right    allowed (correct): No marking governs this action, but it leads into a parking area.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane to proceed straight. Do not drive onto the sidewalk on the
                        left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation none, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 5796, out 624, 22.58 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road with buildings and parked cars on both sides. The
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line is painted on the left edge of the road, next to the curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right side, only the edge of the roadway where cars
                        are parked.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): The word 'BUS' is painted in yellow in the lane.
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries, as both
                        sides are edge lines. | roles: The yellow solid line on the left is a typical edge
                        line for parking restrictions; the right side is an unmarked edge. | markings: The
                        'BUS' text indicates this is a bus lane. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule provided for an unmarked edge line.
Step 5  Rule            text:bus: Vehicles of other classes than the specified class (bus) shall not be driven
                        in this lane. [[IN-6(3)]]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow line, and
                        [IN-6(6)] prohibits driving over a solid longitudinal line.
Step 6  change_right    allowed (correct): No marking governs this action, but it is the edge of the roadway.
Step 6  go_straight     prohibited (contested, label allowed): The lane is marked as a bus lane, and [IN-6(3)]
                        prohibits other vehicles from driving in it.
Step 6  turn_left       not_applicable: No arrow governs this action, but the lane is a bus lane [IN-6(3)].
Step 6  turn_right      not_applicable: No arrow governs this action, but the lane is a bus lane [IN-6(3)].
Step 6  u_turn          not_applicable: No arrow governs this action, but the lane is a bus lane [IN-6(3)].
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane, which is prohibited for ordinary cars. You should
                        leave this lane immediately if possible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation unlisted,
                        contradictions ['change_right decided with nothing marked on that side', 'go_straight
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 5796, out 750, 17.45 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings on both sides; the road continues straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is painted along the edge of the road next to a curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and the
                        absence of a right lane line. | roles: The yellow solid line on the left fits the role
                        of an edge line (kerb side). | markings: There are no markings in the lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs this boundary as no marking is present.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow line, and
                        [IN-6(6)] prohibits driving over a solid longitudinal line.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          allowed: No marking governs this action, but [IN-8(3)(a)(iv)] prohibits U-turns across
                        solid lines; however, the right side is open.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight or move to the right. Do not cross the yellow line on the
                        left or park along it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 5796, out 628, 14.82 s
```
