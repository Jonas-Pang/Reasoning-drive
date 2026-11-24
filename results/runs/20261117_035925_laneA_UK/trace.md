# Reasoning of lane run 20261117_035925_laneA_UK

```text
lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a city street in the United Kingdom with shops on both sides; the road ahead
                        is straight with no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the roadway from a paved area with shops and pedestrians.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the roadway from a parking area where a car is stopped.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the edge lines on both sides.
                        | roles: The solid white lines on both sides fit the role of edge lines for a single-
                        lane road. | markings: There are no markings in the lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the area to the right.
Step 6  change_left     prohibited (contested, correct): The left_boundary is a solid white edge line which
                        prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): The right_boundary is a solid white edge line which
                        prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 596, 24.88 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom with buildings on the left and trees on
                        the right; the road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from another lane of my direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway next to a sidewalk and trees.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the white solid line fits the role of an edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk on the right.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line,
                        which prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left lane. Do not
                        cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 612, 14.54 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street in the United Kingdom with buildings on both sides; the road
                        ahead continues straight with other vehicles present. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left edge of the roadway, separating the lane
                        from the sidewalk/parking area.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           The right side of the lane is not marked by a painted line, but is occupied by
                        oncoming traffic and parked cars.
                        none none, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the left edge line and the
                        right center line role. | roles: The yellow solid line on the left fits the role of an
                        edge line (parking restriction) in the UK. | markings: There are no markings in the
                        lane, which is consistent with a simple urban street. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits parking and crossing into the
                        sidewalk area.
Step 5  Rule            right_boundary: The center of the road separates traffic moving in opposite
                        directions; crossing it is prohibited unless overtaking is safe and legal.
Step 6  change_left     prohibited (contested, label not_determined): The left boundary is a solid yellow edge
                        line with a curb, which prohibits leaving the roadway.
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary is a center line
                        separating opposite traffic, which prohibits changing into the oncoming lane.
Step 6  go_straight     allowed (contested, label not_determined): No marking governs this action, and the
                        lane does not end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the left or
                        enter the oncoming traffic lane on the right.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 2949, out 637, 15.5 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street in the United Kingdom with buildings on both sides; the road
                        ahead appears to be a straight stretch with parked cars on the right. (lanes 1, mine
                        1, full)
Step 2  Left            I see a white dashed line separating my lane from a cycle lane on the left.
                        white dashed, curb no, special_lane_line, evidence full
Step 2  Right           I see a grey curb with parked cars beyond it on the right.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        area:grid (full): A yellow box junction with a criss-cross pattern is painted across
                        the lane.
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the left boundary
                        being a special lane line and the right boundary being a curb. | roles: The white
                        dashed line fits the role of a special lane line for a cycle lane, and the curb fits
                        the role of an edge line. | markings: The grid area is a standard box junction and
                        does not contradict the boundaries. | unseen: No, all reported attributes are visible.
                        | result: consistent
Step 5  Rule            left_boundary: A dashed line allows crossing into the cycle lane if it is safe to do
                        so.
Step 5  Rule            right_boundary: The curb prohibits leaving the roadway to the right.
Step 5  Rule            area:grid: Vehicles must not enter the box junction unless their exit is clear.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary is a curb, which
                        prohibits leaving the road.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the lane does
                        not end.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight or move left into the cycle lane if necessary. Do not enter
                        the yellow box junction unless your exit is clear.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 693, 12.49 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with a red bus ahead; the road continues straight
                        forward. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a bicycle lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           There is no painted line on the right, but parked cars and a curb define the edge of
                        the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left special lane line and
                        right edge curb. | roles: The solid white line on the left fits the role of a special
                        lane boundary for the cycle lane. | markings: There are no markings in my lane to
                        contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white line prohibits crossing into the bicycle lane.
Step 5  Rule            right_boundary: The curb and edge of the roadway prohibit leaving the road to the
                        right.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line which
                        prohibits crossing into the cycle lane.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb which prohibits
                        leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle lane on the left or
                        cross the curb on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 592, 29.68 s

lingoqa__train_39b0fb645812ec9da3cbf9a64e3e2b12_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with shops on both sides; the road continues straight ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates my lane from a parking area with cars on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the opposite direction of traffic.
                        white solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a center line on
                        the right and an edge line on the left. | roles: The solid white lines fit the roles
                        of center line and edge line for a single-lane road in this context. | markings: There
                        are no markings in my lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the parking area.
Step 5  Rule            right_boundary: A solid white center line prohibits crossing into the opposite traffic
                        lane.
Step 6  change_left     prohibited (contested, correct): The left_boundary is a solid white edge line which
                        prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): The right_boundary is a solid white center line
                        which prohibits crossing it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 591, 13.86 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city road in the United Kingdom with traffic moving on the left; the road continues
                        straight ahead with a bus and other vehicles in the distance. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid red line marks the edge of the roadway next to a sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with a lane line on the
                        left and an edge line on the right. | roles: The white dashed line fits a lane line
                        role, and the red solid line fits an edge line role. | markings: There are no markings
                        in my lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid red edge line prohibits leaving the roadway to the right.
Step 6  change_left     allowed (correct): The white dashed lane line allows changing to the left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid red edge line and curb prohibit changing
                        to the right.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight.
Step 6  turn_left       not_applicable: No arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: No arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: No arrow governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left lane. Do not
                        cross the red line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 592, 13.89 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK, looking straight ahead towards a junction; my car
                        is in the leftmost lane. (lanes 1, mine 1, full)
Step 2  Left            A raised concrete curb separates the road from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from a parking area or another lane on the
                        right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the left curb (edge) and right
                        dashed line (lane line). | roles: The white dashed line on the right fits the role of
                        a lane line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a broken white line to change lanes is allowed.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (correct): The right boundary is a dashed white line, which allows lane
                        changes.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or change lanes to the right. Do not drive onto the sidewalk
                        on the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 2949, out 596, 13.92 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with shops on both sides; the road ahead is clear
                        and continues straight. (lanes 1, mine 1, full)
Step 2  Left            A grey stone curb separates the roadway from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The curb on the left indicates my lane is the leftmost lane, which agrees
                        with lane_count 1 and ego_lane_index 1. | roles: The curb correctly serves as an
                        edge_line. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: No marking prohibits moving to the right if the path is clear.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (correct): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane to go straight. Do not drive onto the sidewalk on the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 2949, out 572, 10.56 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A residential urban street in the UK with parked cars on both sides; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line is painted along the left edge of the roadway, next to the
                        sidewalk.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right side, only a row of parked cars and the curb.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The word 'BUS' is painted in yellow across the lane.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the edge lines on both sides. |
                        roles: The yellow solid line on the left is a typical UK edge line for parking
                        restrictions; the right side is a curb. | markings: The 'BUS' marking indicates a bus
                        lane. | unseen: No attributes were reported without visual evidence. | result:
                        consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits parking but does not prohibit
                        driving in the lane.
Step 5  Rule            right_boundary: The curb marks the edge of the roadway and prohibits leaving the road.
Step 5  Rule            text:bus: This lane is reserved for buses; ordinary cars are prohibited from driving
                        in it during its hours of operation.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow edge line and a
                        curb, which prohibits leaving the roadway to the left.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb and parked cars, which
                        prohibits leaving the roadway to the right.
Step 6  go_straight     prohibited (contested, label allowed): The 'BUS' marking prohibits ordinary cars from
                        using this lane.
Step 6  turn_left       not_applicable: No marking governs this action, but the 'BUS' marking prohibits being
                        in the lane to perform it.
Step 6  turn_right      not_applicable: No marking governs this action, but the 'BUS' marking prohibits being
                        in the lane to perform it.
Step 6  u_turn          not_applicable: No marking governs this action, but the 'BUS' marking prohibits being
                        in the lane to perform it.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane, which is prohibited for ordinary cars. You should
                        leave this lane as soon as it is safe and legal to do so.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation None,
                        contradictions ['go_straight decided without an arrow or prohibited-movement marking']
Tokens                  in 2949, out 727, 16.55 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom with buildings on both sides; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line marks the left edge of the roadway next to a curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line is visible on the right side of the lane, and there is no curb.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 are consistent with the left edge
                        line and the absence of a lane line on the right. | roles: The solid yellow line on
                        the left is consistent with a UK edge line (often indicating parking restrictions). |
                        markings: There are no markings in the lane to contradict the boundaries. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits crossing into the curb area or
                        parking, but does not prohibit driving in the lane.
Step 5  Rule            right_boundary: The absence of a marking on the right does not prohibit movement, but
                        there is no designated lane to change into.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow edge line with a
                        curb, which prohibits leaving the roadway.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action as there is no
                        painted line or curb on the right.
Step 6  go_straight     allowed (contested, correct): No marking governs this action; going straight is
                        allowed by default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the scene.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Be mindful of the cyclist and parked
                        cars on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 2949, out 619, 15.08 s
```
