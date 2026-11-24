# Reasoning of lane run 20261117_035908_laneA_UK

```text
lingoqa__train_1869901e085ad9bfb1081f4efa101c93_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the United Kingdom with shops on both sides; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the roadway from a paved area with shops and pedestrians.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the roadway from a parking area where cars are stopped.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the edge lines on both
                        sides. | roles: The solid white lines on both sides fit the role of edge lines for a
                        single-lane road. | markings: There are no markings in the lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the area to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the area to the right.
Step 6  change_left     prohibited (contested, correct): The left_boundary is a solid white edge line which
                        prohibits leaving the roadway.
Step 6  change_right    prohibited (WRONG, label allowed): The right_boundary is a solid white edge line which
                        prohibits crossing into the parking area.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 590, 14.11 s

lingoqa__train_1c248b91fcec1954ff5503505d99c727_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, looking straight ahead with buildings
                        on the left and trees on the right. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line marks the edge of the roadway next to a sidewalk and trees.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white dashed line fits the role of a lane
                        line, and the white solid line fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: A dashed white line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid white edge line prohibits crossing into the shoulder or
                        sidewalk area.
Step 6  change_left     allowed (contested, label prohibited): The left boundary is a dashed white line, which
                        allows lane changes.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line and a
                        curb, which prohibits leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: No arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: No arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: No arrow governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left lane. Do not
                        cross the solid line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 610, 19.0 s

lingoqa__train_1c5078b108792bcad84aacafb7edf52d_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street in the United Kingdom with buildings on both sides; the road
                        continues straight ahead with traffic moving in the same direction. (lanes 1, mine 1,
                        full)
Step 2  Left            A solid yellow line is visible on the left edge of the roadway, separating the lane
                        from the sidewalk/parking area.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side, as other vehicles are present
                        and the road surface is wet and reflective.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 are consistent with the left
                        boundary being an edge line. | roles: The solid yellow edge line on the left is
                        consistent with UK road markings for parking restrictions at the edge of the
                        carriageway. | markings: There are no markings in the lane, which is consistent with a
                        simple urban street. | unseen: I have not reported any attributes I did not see; the
                        right boundary is marked as insufficient. | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits parking and restricts crossing the
                        boundary to leave the roadway.
Step 5  Rule            right_boundary: No marking is visible to govern movement on the right.
Step 6  change_left     prohibited (contested, label not_determined): The left boundary is a solid yellow edge
                        line, which prohibits leaving the roadway.
Step 6  change_right    not_determined (correct): The right boundary is not visible, leaving this action
                        undecided.
Step 6  go_straight     allowed (contested, label not_determined): No marking governs this action, and the
                        lane does not end, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line on the left.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 644, 16.09 s

lingoqa__train_2fbe08dff3dad5e735cda2ccbca737d3_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street in the United Kingdom with buildings on both sides; the road
                        ahead is clear with a bus in the distance. (lanes 1, mine 1, full)
Step 2  Left            I see a curb and a sidewalk on the left side of the road.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           I see a white dashed line separating my lane from a parking area or another lane on
                        the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A yellow box junction with diagonal lines is painted across the
                        lane.
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the left curb and
                        right lane line. | roles: The white dashed line on the right fits the role of a lane
                        line. | markings: The grid area is a standard junction marking and does not contradict
                        the boundaries. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a dashed white line to change lanes is allowed.
Step 5  Rule            area:grid: Entering the box junction is prohibited unless the exit is clear.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a dashed white line,
                        which allows changing lanes.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the lane does
                        not end.
Step 6  turn_left       not_applicable: No arrow or marking governs this action.
Step 6  turn_right      not_applicable: No arrow or marking governs this action.
Step 6  u_turn          not_applicable: No arrow or marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may proceed straight or change lanes to the right. Do not enter the yellow box
                        junction unless your exit is clear.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['rightmost lane, but a
                        lane line on the right']
Tokens                  in 2949, out 655, 19.61 s

lingoqa__train_3510c0055b143081d71aa4122da19639_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK with traffic keeping to the left; the road continues
                        straight ahead with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a bicycle lane on the left.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           There is no painted line on the right, but a row of parked cars and a curb define the
                        edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left special lane line and
                        right edge curb. | roles: The solid white line on the left fits the role of a special
                        lane line for the cycle lane; the curb on the right fits the edge line role. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A solid white line prohibits crossing into the bicycle lane.
Step 5  Rule            right_boundary: The curb and edge of the roadway prohibit leaving the road to the
                        right.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white special lane line,
                        which prohibits crossing into the cycle lane.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb, which prohibits
                        leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not enter the cycle lane on the left or
                        cross the curb on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 622, 14.23 s

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
                        of center line and edge line in this urban context. | markings: There are no markings
                        in my lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A solid white edge line prohibits crossing into the parking area.
Step 5  Rule            right_boundary: A solid white center line prohibits crossing into the opposite lane of
                        traffic.
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
Advice                  Stay in your lane and proceed straight; lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 587, 13.79 s

lingoqa__train_4fea456d82bfafd9161a364928d30234_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a city road in the United Kingdom with traffic moving on the left; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            A white dashed line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A red solid line marks the edge of the roadway next to the sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white dashed line fits the
                        role of a lane line, and the red solid line fits the role of an edge line (red route).
                        | markings: There are no markings in my lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A white dashed lane line allows changing lanes to the left.
Step 5  Rule            right_boundary: A solid edge line and curb prohibit leaving the roadway to the right.
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
                        cross the red line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 595, 14.75 s

lingoqa__train_70a63438f4f5c50ef21f29cc45d849ab_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road in the UK; the road continues straight ahead with
                        parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            A grey raised curb separates the road from a sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right, but cars are parked along the edge of the
                        roadway.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the left curb and right
                        edge of the roadway. | roles: The left curb acts as an edge_line and the right side is
                        the edge of the roadway. | markings: There are no markings in the lane to contradict
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing a curb onto a sidewalk is prohibited.
Step 5  Rule            right_boundary: Leaving the roadway to the right is prohibited if it involves driving
                        onto a non-road surface or into parked cars.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is the edge of the roadway with
                        parked cars, prohibiting a lane change.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be mindful of the parked cars on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 2949, out 595, 14.34 s

lingoqa__train_74be6bb80c7b66a911cef6cb3c999227_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a city street in the United Kingdom with shops on both sides; the road ahead
                        is straight with no immediate intersection or ramp. (lanes 1, mine 1, full)
Step 2  Left            A grey stone curb separates the roadway from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The curb on the left indicates my lane is the leftmost lane, which agrees
                        with lane_count 1 and ego_lane_index 1. | roles: The curb correctly serves as the left
                        edge of the roadway. | markings: There are no markings in the lane to contradict the
                        boundaries. | unseen: No attributes were reported without visual evidence. | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the curb onto the sidewalk is prohibited.
Step 5  Rule            right_boundary: No marking governs movement to the right.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the roadway.
Step 6  change_right    allowed (correct): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: No arrow governs this action.
Step 6  u_turn          not_applicable: No arrow governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane to go straight. Do not drive onto the sidewalk on the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 2949, out 564, 22.81 s

lingoqa__train_97b78557b9103ec9b3b5dce23c33e5f6_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban street in the UK. The road ahead is straight with parked
                        cars on the right side. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is painted on the left edge of the roadway.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           There is no painted line on the right, but parked cars and a curb define the edge of
                        the road.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The word BUS is painted in yellow across the lane.
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the edge lines on both
                        sides. | roles: The yellow solid line on the left is a typical UK edge line for
                        parking restrictions; the right side is a physical curb. | markings: The BUS marking
                        indicates this is a bus lane. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits crossing into the area beyond it
                        (parking/stopping restrictions).
Step 5  Rule            right_boundary: The curb prohibits leaving the roadway to the right.
Step 5  Rule            text:bus: This lane is reserved for buses; ordinary cars are prohibited from using it
                        during its operational hours.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid yellow edge line which
                        prohibits crossing it.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb which prohibits
                        crossing it.
Step 6  go_straight     prohibited (contested, label allowed): The BUS marking prohibits ordinary cars from
                        using this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a bus lane, which is prohibited for ordinary cars. You should leave this
                        lane if permitted by local signage or avoid entering it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed ['text:other']), actions False, unsafe [], citation None,
                        contradictions ['go_straight decided without an arrow or prohibited-movement marking']
Tokens                  in 2949, out 660, 15.83 s

lingoqa__train_a7fef42c584e5d3b67be7e244e35cd21_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the United Kingdom with buildings on both sides; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is painted along the left edge of the roadway next to a curb.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the left edge line and
                        the absence of a right boundary line. | roles: The solid yellow line on the left is
                        consistent with a UK road edge marking (no parking/waiting). | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A solid yellow edge line prohibits parking or waiting but does not
                        prohibit driving in the lane; crossing it to the left is prohibited by the curb.
Step 5  Rule            right_boundary: The absence of a marking on the right does not prohibit moving to the
                        right, provided it is safe and legal.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb and a solid yellow line,
                        which prohibits leaving the roadway to the left.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or move to the right. Do not cross the left boundary into the
                        curb area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 2949, out 606, 14.27 s
```
