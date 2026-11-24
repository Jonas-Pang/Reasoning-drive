# Reasoning of lane run 20261117_015555_laneB_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. The road continues forward
                        with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white color and dashed/solid patterns fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in the
                        lane to contradict the boundaries. | unseen: No attributes were reported without being
                        visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): Prohibited by the solid white lane line (CN-6.2.1).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left, but you are prohibited from
                        changing lanes to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 763, 20.21 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading straight. The road continues forward with no
                        immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a shoulder or non-motorized lane on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 are consistent with having a lane
                        line on the left and an edge line on the right, implying my lane is the rightmost
                        motor vehicle lane. | roles: The white broken line on the left fits the role of a lane
                        line, and the white solid line on the right fits the role of an edge line. | markings:
                        There are no markings in my lane to contradict. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the edge of the motor vehicle lane;
                        crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost motor vehicle lane. You may change lanes to the left, but do
                        not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 684, 14.43 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway with a clear road ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a guardrail and shoulder
                        beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line fits the
                        role of a crossable lane line, and the white solid line fits the role of a right-hand
                        edge line. | markings: There are no markings in the lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid white edge line
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the carriageway. You may continue straight or change
                        to the left lane, but do not cross the right edge line into the shoulder.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 793, 116.61 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight toward a distant intersection
                        or road section. (lanes 2, mine 2, full)
Step 2  Left            A broken yellow line separates my lane from the lane to the left.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a physical barrier beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (2) agree with the boundaries: a center
                        line on the left and an edge line on the right indicate my lane is the rightmost of
                        the direction of travel, but the yellow line suggests it separates opposing traffic,
                        meaning there is only one lane for my direction here. | roles: The yellow dashed line
                        fits the role of a crossable center line; the white solid line fits the role of a road
                        edge line. | markings: No markings are present in the lane to contradict boundaries. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken yellow center line
                        [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line and physical
                        barrier [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: Not applicable as no arrow governs this movement.
Step 6  u_turn          allowed: Allowed by the broken yellow center line [CN-5.1.1].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or cross the center line to the
                        left to overtake or turn if safe; do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 7595, out 833, 22.86 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. There are no immediate
                        intersections or ramps visible ahead. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): The Chinese characters '公交' (bus) are painted in white in the lane.
Step 4  Cross-check     position: The lane count of 3 and my position as index 3 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line; the white solid line on the right fits the role of an
                        edge line. | markings: The '公交' text indicates this is a bus lane, which is consistent
                        with the boundaries. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the lane. [CN-6.9.1] "The bus lane
                        line shows that vehicles other than buses shall not enter the lane. It consists of a
                        broken white line and white text. The broken line has 5 m segm"
Step 6  change_left     allowed (contested, correct): allowed; the left boundary is a broken white line
                        (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, label allowed): prohibited; the right boundary is a solid white
                        edge line (CN-4.2.2-a) and there is a physical barrier.
Step 6  go_straight     prohibited (contested, label allowed): prohibited; the lane is marked as a bus lane
                        (CN-6.9.1) and my car is an ordinary car.
Step 6  turn_left       not_applicable: not_applicable; no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable; no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable; no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane. You should change left into a general traffic lane
                        immediately.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions ['go_straight
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 7595, out 919, 119.66 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an overpass/bridge. (lanes 2,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a curb and a wall.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (2) agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white broken line fits
                        the role of a lane line, and the white solid line fits the role of a right edge line.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line marks the right edge of the direction of travel.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line and the presence of a
                        curb (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7595, out 794, 18.73 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with a bus stop on the left and parked scooters on the right.
                        The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the lane from a bus stop area.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is visible on the right, separating the lane from a parking area
                        for scooters.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries: a yellow center
                        line on the left and a white edge line on the right indicate a single-lane road for my
                        direction. | roles: The yellow solid line on the left fits the role of a center line
                        (separating opposite directions), and the white solid line on the right fits the role
                        of an edge line. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white; it marks the edge of the motor vehicle lane. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, which prohibits
                        crossing according to [CN-6.1.4].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line; while [CN-5.4.3]
                        defines it, [CN-4.2.2-a] states a solid line means crossing is normally prohibited.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid lines on either side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 686, 20.97 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in or ahead of my lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 7595, out 598, 18.61 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a clear path ahead, flanked by trees and
                        greenery. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a curb and greenery.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line, and the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken white line,
                        which may be crossed according to CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line, and crossing solid lines is normally prohibited according to CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 829, 18.48 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road in China. The road continues straight ahead towards a
                        traffic signalized intersection. (lanes 4, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 4 and my position at index 2 are consistent with having
                        lane lines on both my left and right. | roles: The white broken lines on both sides
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in my lane to contradict the boundaries.
                        | unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed: The left boundary is a broken white line, which [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed: The right boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it, so it is allowed.
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
Tokens                  in 7595, out 624, 112.15 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards a distant
                        intersection. (lanes 2, mine 2, full)
Step 2  Left            A solid yellow line separates my lane from the lane to the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a non-motorized lane or shoulder on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (2) are consistent with the
                        boundaries: a center line on the left and an edge line on the right indicate my lane
                        is the rightmost of my direction, and there is one other lane to the left (which,
                        given the yellow line, is for opposing traffic). Wait, if the left boundary is a
                        center line, my lane is the leftmost of my direction. Let me re-evaluate: the yellow
                        line separates opposing traffic. Thus, there is only 1 lane in my direction.
                        Correcting lane_count to 1 and ego_lane_index to 1. | roles: The yellow solid line on
                        the left fits the role of a no-crossing center line. The white solid line on the right
                        fits the role of a road edge line. | markings: No markings are present in the lane,
                        which is consistent with the boundaries. | unseen: No attributes were reported without
                        being seen. | result: corrected lane_count to 1 and ego_lane_index to 1
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, label not_determined): Allowed as no marking restricts carrying on
                        straight along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['symbol:other']), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 7595, out 953, 29.18 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or highway, traveling straight ahead on a bridge
                        or elevated section. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete barrier beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white dashed line fits
                        the role of a crossable lane line, and the white solid line fits the role of a right-
                        hand edge line. | markings: There are no markings in the lane to contradict. | unseen:
                        No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line and physical barrier
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings in the
                        lane.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings in the
                        lane.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings in the
                        lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move to the right due to the road edge and barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 807, 22.15 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway under an overpass, with a clear road
                        ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a shoulder beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line, and the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in the lane to contradict. | unseen:
                        No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 7595, out 788, 19.15 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, traveling straight ahead on a clear road.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 agree with having lane lines
                        on both the left and right. | roles: The white dashed lines are consistent with the
                        role of crossable lane lines separating traffic in the same direction. | markings:
                        There are no markings in my lane to contradict the boundaries. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane on a highway; you may continue straight or change lanes to
                        the left or right as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 7595, out 767, 23.15 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road in China. The car is approaching an intersection with
                        several other vehicles ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in the middle of the
                        lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: The straight-ahead arrow is consistent with a
                        through lane bounded by lane lines. | unseen: No attributes were reported without
                        being visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may travel straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): Allowed by the straight-ahead guide arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight-ahead guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight-ahead guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight-ahead guide arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action; no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. Do not attempt to
                        turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation accepted, contradictions []
Tokens                  in 7595, out 740, 100.6 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 597, 13.01 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road with a clear path ahead. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 586, 98.64 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white broken lines fit the role of crossable lane lines. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right, or continue
                        straight. Use the overhead signs to determine which lane is needed for your intended
                        turn at the intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 609, 18.0 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with overhead
                        signs. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: White dashed lines are consistent with the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (contested, correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7595, out 734, 18.54 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane to the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white color and dashed/solid patterns fit the role of lane lines
                        separating traffic in the same direction. | markings: The straight arrow is consistent
                        with a through lane. | unseen: No attributes were reported without being visible. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from my side. [CN-6.2.1]
                        "The no-crossing lane line separates vehicles travelling in the same direction and
                        prohibits vehicles on the solid-line side from crossing. It has two forms: sin"
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white line [CN-6.2.1].
Step 6  go_straight     allowed (correct): allowed because the guide arrow indicates straight ahead
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the guide arrow only allows straight ahead
                        [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the guide arrow only allows straight ahead
                        [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the guide arrow only allows straight ahead
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not cross the solid line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 891, 104.51 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane urban road in China. The road continues straight ahead towards a
                        distant intersection or bridge area. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 2 are consistent with having
                        lane lines on both my left and right. | roles: The white broken lines on both sides
                        fit the role of crossable lane lines separating traffic in the same direction. |
                        markings: There are no markings in my lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (WRONG, label not_determined): The right boundary is a broken white line,
                        which [CN-5.2.1-2] allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present to govern this
                          action.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 663, 23.39 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a wide intersection or junction.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines on both sides fit the role of
                        crossable lane lines. | markings: There are no markings in the lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): The left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in or next to the lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 7595, out 610, 20.21 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway, traveling straight ahead on a
                        clear road. (lanes 5, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 5 and ego position 3 are consistent with having lane lines
                        on both the left and right. | roles: The white dashed lines on both sides are
                        consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in the lane to contradict the boundaries.
                        | unseen: No attributes were reported without being visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a five-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['text:other']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 620, 21.7 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multi-lane highway or expressway. The road continues straight ahead with
                        overhead signs in the distance; my car is traveling in one of the lanes. (lanes 4,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 4 and my position at index 2 agree with having lane lines
                        on both sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in my lane to contradict. | unseen: No attributes were
                        reported without being visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane on a highway. You may continue straight or change lanes to
                        the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 614, 18.26 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards a clear stretch
                        of road. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which [CN-5.2.1-2] allows
                        crossing.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which [CN-5.2.1-2]
                        allows crossing.
Step 6  go_straight     allowed (correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 7595, out 593, 19.67 s
```
