# Reasoning of lane run 20261117_023728_laneC_US

```text
bdd100k_val__b2afce7f-0cb9967a | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway with a guardrail on the right and a concrete
                        barrier on the left, heading straight. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the road, with a metal guardrail
                        immediately beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 3 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line; the white solid line on the right fits the role of an
                        edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line [CN-4.2.2-a]
                        and the presence of a guardrail.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no intersection or arrow governing this.
Step 6  turn_right      not_applicable: Not applicable as there is no intersection or arrow governing this.
Step 6  u_turn          not_applicable: Not applicable as there is no intersection or arrow governing this.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 661, 39.47 s

bdd100k_val__b459e707-2d208c56 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-lane two-way road, traveling straight ahead on a clear stretch of
                        road. (lanes 1, mine 1, full)
Step 2  Left            A broken yellow line separates my lane from the opposite direction of traffic.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A solid yellow line marks the right edge of the roadway, with a dirt shoulder beyond
                        it.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the center line on the
                        left and edge line on the right. | roles: The yellow color for both boundaries fits
                        their roles as center and edge lines on a two-way road. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: Crossing the solid line is normally prohibited and may be crossed only
                        in an emergency when safe. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): Allowed by the broken yellow center line [CN-5.1.1].
Step 6  change_right    prohibited (correct): Prohibited by the solid yellow edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          allowed: Allowed by the broken yellow center line [CN-5.1.1].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may drive straight or move left to overtake if safe; do not cross the solid yellow
                        line on the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 7601, out 652, 38.28 s

bdd100k_val__b5046f1e-b1ef44b9 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with tall buildings on both sides, heading towards an
                        intersection. (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates the lane from a parking or non-motorized area on the
                        left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a parking or non-motorized area on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries being edge lines
                        on both sides. | roles: The white solid lines on both sides fit the role of edge lines
                        for a single-lane road. | markings: There are no markings in the lane to contradict. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow, but on a single-lane two-way road, the edge lines on both sides shall be
                        white. [CN-5.4.3]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [CN-5.4.3]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white edge line, and
                        crossing solid lines is normally prohibited per CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line, and crossing
                        solid lines is normally prohibited per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['text:only']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7601, out 648, 40.2 s

bdd100k_val__b6decb24-82234e11 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban city road in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): The word ONLY is painted in white across the lane.
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of lane lines separating traffic
                        in the same direction. | markings: The word ONLY is present but there is no
                        accompanying arrow to specify the restriction. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            text:other: The word ONLY indicates a restriction, but without an arrow or further
                        text, the specific restriction is not defined by the provided rules.
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed as no marking prohibits it and the lane does not end.
Step 6  turn_left       not_applicable (WRONG, label prohibited): Not applicable as there is no arrow or
                        waiting area governing this movement.
Step 6  turn_right      not_applicable (WRONG, label prohibited): Not applicable as there is no arrow or
                        prohibited-movement marking governing this movement.
Step 6  u_turn          not_applicable (WRONG, label prohibited): Not applicable as there is no arrow or
                        prohibited-movement marking governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may change lanes to the left or right, or proceed
                        straight. The 'ONLY' marking is ambiguous without an arrow; proceed with caution and
                        check overhead signs or signals.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed ['arrow:straight']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 722, 39.67 s

bdd100k_val__b7719f1d-e6e580dd | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway heading straight. The road continues forward with
                        no immediate intersection or ramp visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a concrete barrier beyond
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and my position as index 3 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line; the white solid line on the right fits the role of an
                        edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane;
                        crossing it is normally prohibited per [CN-4.2.2-a]. [[CN-5.4.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 666, 37.61 s

bdd100k_val__b775af1c-bb5afbe3 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the lane from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_left (full): A white arrow pointing straight and left is painted in the
                        lane.; line:stop_line (full): A solid white line is painted across the lane at the
                        intersection entrance.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the center line on the left and
                        edge line on the right. | roles: The yellow solid line fits the role of a no-crossing
                        center line, and the white solid line fits the role of a road edge line. | markings:
                        The straight-left arrow and stop line are consistent with a single-lane approach to an
                        intersection. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            arrow:straight_left: The guide arrow indicates that the vehicle may go straight or
                        turn left. [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid yellow center line
                        [CN-6.1.4].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line [CN-5.4.3]
                        and the presence of a curb.
Step 6  go_straight     allowed (WRONG, label prohibited): Allowed by the guide arrow [CN-5.13.1].
Step 6  turn_left       allowed (WRONG, label prohibited): Allowed by the guide arrow [CN-5.13.1].
Step 6  turn_right      prohibited (WRONG, label allowed): Prohibited by the guide arrow [CN-5.13.1], which
                        only shows straight and left.
Step 6  u_turn          prohibited (correct): Not determined as no specific U-turn arrow is present, but
                        generally prohibited by the solid center line [CN-6.1.4].
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the lane.
Step 7  Reflect         consistent
Advice                  You are in a single lane that allows you to go straight or turn left. Do not change
                        lanes or turn right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_left'], missed ['arrow:right']), actions False, unsafe
                        ['go_straight', 'turn_left'], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 829, 39.22 s

bdd100k_val__b9db357e-cd30a8ae | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: White dashed lines are consistent with lane lines
                        separating traffic in the same direction. | markings: No markings are present in the
                        lane, which is consistent with the boundaries. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means vehicles may cross it to change
                        lanes. [CN-5.2.1-2]
Step 6  change_left     allowed (contested, correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (contested, label not_determined): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        action.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 752, 38.7 s

bdd100k_val__bc05c126-d00aeb9c | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with a two-way left-turn lane. The road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A pair of yellow lines, one solid and one broken, separates my lane from a two-way
                        left-turn lane.
                        yellow solid_dashed (near line dashed), curb no, center_line, evidence full
Step 2  Right           A solid white line separates my lane from a reddish-brown shoulder or bike lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (full): A two-way left-turn lane is directly to the left
                        of my lane, marked by yellow lines.
Step 4  Cross-check     position: The lane count (1) and position (1) agree with the boundaries: a center line
                        on the left and an edge line on the right. | roles: The yellow solid-dashed line fits
                        the role of a center line for a two-way left-turn lane; the white solid line fits the
                        role of a right edge line. | markings: The two-way left-turn lane area is consistent
                        with the yellow solid-dashed boundary on its right. | unseen: No attributes were
                        reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles on the broken side may cross the line. [CN-6.1.3]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3]
Step 5  Rule            area:two_way_left_turn_lane: A two-way left-turn lane is used for vehicles to wait or
                        prepare for a left turn. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken-solid yellow
                        line and my car is on the broken side (CN-6.1.3).
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed: no marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow in my lane governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow in my lane governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow in my lane governs this movement.
Step 6  enter_waiting_areaallowed: allowed: the two-way left-turn lane to the left is a designated waiting
                          area.
Step 7  Reflect         consistent
Advice                  You may continue straight or move into the two-way left-turn lane to the left if you
                        intend to turn left. Do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions False, unsafe ['change_left'],
                        citation unlisted, contradictions []
Tokens                  in 7601, out 975, 45.31 s

bdd100k_val__bca36352-5de70a3f | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection or a road
                        transition area with construction barrels on the right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from a channelized area with orange barrels.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having a lane line on both
                        the left and right. | roles: The white color and dashed/solid patterns fit the roles
                        of lane lines separating traffic in the same direction. | markings: There are no
                        markings in the lane to contradict the boundaries. | unseen: No attributes were
                        reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on the solid-line side
                        from crossing. [CN-6.2.1]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white lane line (CN-6.2.1).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not change to the right as it
                        is marked by a solid line and contains construction barrels.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 781, 41.75 s

bdd100k_val__bcbbfd82-add80c05 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, heading towards an intersection with
                        traffic signals ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane of the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line marks the left edge of the roadway for the opposite direction, or
                        the right edge of my direction if it's a two-way road, but here it appears to be the
                        right edge of the motor vehicle lanes.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego_lane_index (2) agree with the boundaries: a lane
                        line on the left and an edge line on the right. | roles: The white dashed line fits
                        the role of a lane line; the yellow solid line fits the role of an edge line (though
                        yellow is typically for the left edge, in some US contexts or specific road types it
                        varies, but based on the provided China rules, yellow is for the left edge/opposite
                        traffic). | markings: No markings are present in the lane. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid yellow edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may change to the left lane, but you cannot cross
                        the right boundary. Proceed straight toward the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7601, out 707, 40.4 s

bdd100k_val__bd026bc5-9418706c | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           Urban city road with multiple lanes, approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: The straight arrow is consistent with a through lane. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken white lane line to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: Vehicles may cross the broken white lane line to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [CN-5.13.1]
Step 6  change_left     allowed (contested, correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (contested, correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): Allowed by the straight guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): Prohibited by the straight guide arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight guide arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight guide arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. Do not attempt to
                        turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7601, out 713, 35.92 s

bdd100k_val__be278041-2173a980 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching a fork or a channelized area where the
                        road splits. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid yellow line marks the left edge of the road from the perspective of opposing
                        traffic, but here it is the right boundary of my lane leading into a channelized area.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with the white lane line on
                        the left and the edge line on the right. | roles: The white dashed line fits the role
                        of a lane line; the yellow solid line fits the role of an edge line in this specific
                        road geometry. | markings: There are no markings in my lane to contradict. | unseen:
                        No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, label allowed): Prohibited by the solid yellow edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict continuing straight.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may stay in your lane or change to the left lane. Do not cross the solid yellow
                        line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7601, out 651, 39.45 s

bdd100k_val__be4cbd00-97fec78b | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, heading towards an intersection with
                        traffic signals visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means vehicles may cross it to change
                        lanes. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per CN-5.2.1-2.
Step 6  go_straight     allowed (correct): No marking restricts going straight, and the boundaries do not
                        govern this action.
Step 6  turn_left       not_applicable (WRONG, label not_determined): No arrow or prohibited-movement marking
                        governs this action.
Step 6  turn_right      not_applicable (WRONG, label not_determined): No arrow or prohibited-movement marking
                        governs this action.
Step 6  u_turn          not_applicable (WRONG, label not_determined): No arrow or prohibited-movement marking
                        governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 632, 38.33 s

bdd100k_val__beccfad4-d24a29c5 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching an intersection or a merge area, with a
                        concrete barrier on the right. (lanes 1, mine 1, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the edge of the road, next to a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 is consistent with a lane line on the left
                        and an edge line on the right. | roles: The white broken line on the left fits the
                        role of a lane line; the white solid line on the right fits the role of an edge line.
                        | markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the boundary of the motor vehicle
                        lane. [[CN-5.4.1]]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line and concrete barrier
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  turn_right      not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  u_turn          not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left. Do not cross the right boundary
                        due to the solid line and concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 7601, out 646, 39.66 s

bdd100k_val__bf6315ee-a77e1bb2 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road at night, facing an intersection with traffic signals ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid white line separates my lane from a line of parked cars on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a line of parked cars on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the boundaries, as both sides are
                        edge lines. | roles: The white solid lines on both sides fit the role of edge lines
                        separating the motor vehicle lane from parking/shoulders. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
Step 5  Rule            right_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  change_right    prohibited (contested, label allowed): The right boundary is a solid white line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight toward the intersection. Do not cross the solid
                        white lines into the parking areas.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 756, 38.62 s

bdd100k_val__bf6711ef-76e408aa | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, traveling under an overpass toward an
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the road from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is visible on the right, separating my lane from the adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): The word 'ONLY' is painted in white across the lane.; arrow:straight
                        (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 are consistent with a center line
                        on the left and a lane line on the right. | roles: The yellow solid line on the left
                        fits the role of a center line; the white solid line on the right fits the role of a
                        lane line. | markings: The 'ONLY' text and straight arrow are consistent with a
                        dedicated through lane. | unseen: No attributes were reported without visual evidence.
                        | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A solid white lane line prohibits vehicles on the solid-line side from
                        crossing. [[CN-6.2.1]]
Step 5  Rule            text:only: The word 'ONLY' indicates that the lane is restricted to the movement shown
                        by the accompanying arrow.
Step 5  Rule            arrow:straight: The straight arrow indicates that the direction of travel for this
                        lane is straight ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    prohibited (contested, label allowed): Prohibited by the solid white lane line
                        [CN-6.2.1].
Step 6  go_straight     allowed (correct): Allowed by the straight arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight arrow and 'ONLY' text, which restrict
                        the lane to straight movement only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight arrow and 'ONLY' text, which restrict
                        the lane to straight movement only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight arrow and 'ONLY' text, which restrict
                        the lane to straight movement only.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight; lane changes are prohibited by the solid lines on
                        both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 815, 42.3 s

bdd100k_val__bfd64d5f-ec05de8b | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway approaching an exit ramp to the right. (lanes 2,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the exit ramp area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line; the white solid line on the right fits the role of an
                        edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid white
                        line to the right; use the designated exit ramp if you intend to exit.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 783, 57.72 s

bdd100k_val__c01c4d85-36b417ee | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The road is a multi-lane urban road at night, with an intersection or a junction
                        ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with having a lane line
                        on the left and an edge line on the right. | roles: The white broken line on the left
                        fits the role of a lane line, and the white solid line on the right fits the role of
                        an edge line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the edge of the motor vehicle lane;
                        crossing it is normally prohibited per [CN-4.2.2-a]. [[CN-5.4.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may change to the left lane, but do not cross the
                        right edge line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 656, 40.32 s

bdd100k_val__c0a71f47-14439a44 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road at night, looking straight ahead towards a distant
                        intersection. (lanes 1, mine 1, full)
Step 2  Left            A double solid yellow line separates the road from the opposite direction of travel.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           The right edge of the road is marked by a dark area with no visible painted line or
                        raised curb.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The double yellow line on the left indicates my lane is the leftmost of my
                        direction, which agrees with a lane count of 1. | roles: The yellow color and double
                        solid pattern fit the role of a no-crossing center line. | markings: There are no
                        markings in the lane to contradict the boundaries. | unseen: No attributes were
                        reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: No marking governs the right boundary; it is the edge of the roadway.
                        [null]
Step 6  change_left     prohibited (correct): The left boundary is a double solid yellow line, which prohibits
                        crossing according to [CN-6.1.2].
Step 6  change_right    allowed (WRONG, label prohibited): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow line to the
                        left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation unlisted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 7601, out 615, 37.53 s

bdd100k_val__c0f5b0d0-17e0110c | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road at night, heading towards a distant intersection or
                        overpass area with traffic congestion ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line separates my lane from traffic in the opposite direction.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a dark shoulder beyond
                        it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the center line on the left
                        and edge line on the right. | roles: The yellow color for the left boundary (center
                        line) and white for the right boundary (edge line) fit their roles. | markings: There
                        are no markings in the lane to contradict. | unseen: No attributes were reported that
                        were not visible. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 777, 38.9 s

bdd100k_val__c16d3fdb-a3a8c912 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway, traveling straight ahead on a road that appears to
                        be a main carriageway. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line separates the lane from a shoulder or opposite traffic area on the
                        left.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from a shoulder or non-motorized area on the
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the boundaries: a yellow line
                        on the left and a white line on the right indicate a single-lane road or the
                        leftmost/rightmost lane of a direction. | roles: The yellow color for the left
                        boundary and white for the right boundary fit the roles of left and right edge lines
                        respectively. | markings: There are no markings in the lane to contradict. | unseen:
                        No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left side of the direction of travel marks
                        the edge of the roadway; crossing it is normally prohibited per CN-4.2.2-a. [CN-5.4.3]
Step 5  Rule            right_boundary: The white edge line on the right side of the direction of travel marks
                        the edge of the roadway; crossing it is normally prohibited per CN-4.2.2-a. [CN-5.4.3]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, which prohibits
                        crossing per CN-4.2.2-a.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no merge or
                        turn restriction, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not cross the solid boundary lines
                        on either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 697, 33.58 s

bdd100k_val__c1e6340e-084ce27d | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road at night, traveling straight ahead on a stretch of
                        road with no immediate intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line is visible on the left, separating the lane from opposing traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line is visible on the right, marking the edge of the roadway.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the center line on the left
                        and edge line on the right. | roles: The yellow solid line fits the role of a no-
                        crossing center line, and the white solid line fits the role of a road edge line. |
                        markings: There are no markings in the lane to contradict the boundaries. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white; it marks the edge of the roadway. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, which prohibits
                        crossing according to [CN-6.1.4].
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a solid white edge line;
                        while [CN-5.4.3] defines it, crossing a solid line is normally prohibited per
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid lines on either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 669, 40.17 s

bdd100k_val__c39dc2ff-6976d19d | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street at night, approaching an intersection. (lanes 1, mine 1,
                        full)
Step 2  Left            A solid white line separates the lane from a sidewalk or bike lane on the left.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A solid white line separates the lane from another lane of the same direction.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white arrow pointing left is painted in the lane.; text:only
                        (full): The word ONLY is painted in white in the lane.; line:stop_line (full): A solid
                        white line across the lane marks the stop line.
Step 4  Cross-check     position: The lane count is 1, but the right boundary is a lane line, implying another
                        lane exists to the right. My lane is the leftmost of the motor vehicle lanes. | roles:
                        The white solid lines fit the roles of edge line (left) and lane line (right). |
                        markings: The left-turn arrow and 'ONLY' text are consistent with a dedicated left-
                        turn lane. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing from the solid side.
                        [CN-6.2.1]
Step 5  Rule            arrow:left: The arrow indicates that the lane is for left turns. [CN-5.13.1]
Step 5  Rule            text:only: The text 'ONLY' indicates that only the movement shown by the arrow is
                        permitted. [CN-5.14.1]
Step 5  Rule            line:stop_line: The stop line marks where vehicles must stop when waiting to proceed.
                        [CN-6.4.1-2]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line (CN-6.2.1/CN-5.4.3)
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white lane line
                        (CN-6.2.1)
Step 6  go_straight     prohibited (correct): prohibited by the left-turn arrow and 'ONLY' text (CN-5.13.1,
                        CN-5.14.1)
Step 6  turn_left       allowed (correct): allowed by the left-turn arrow (CN-5.13.1)
Step 6  turn_right      prohibited (correct): prohibited by the left-turn arrow and 'ONLY' text (CN-5.13.1,
                        CN-5.14.1)
Step 6  u_turn          prohibited (contested, label allowed): prohibited by the left-turn arrow and 'ONLY'
                        text (CN-5.13.1, CN-5.14.1)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a dedicated left-turn lane. You must turn left at the intersection and are
                        prohibited from going straight or changing lanes.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 7601, out 917, 40.39 s

bdd100k_val__c3ecb3cb-5fb43d29 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, approaching an intersection or a turn-off.
                        There is a lane to the right and a separated area to the left. (lanes 2, mine 1, full)
Step 2  Left            A yellow solid line is visible, with orange traffic cones placed along it, separating
                        my lane from a left-turn area.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white broken line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): The word ONLY is painted in white across the lane.; arrow:straight
                        (full): A white arrow pointing straight ahead is painted in the lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the yellow center line
                        on the left and white lane line on the right. | roles: The yellow solid line fits the
                        role of a center line; the white broken line fits the role of a lane line. | markings:
                        The ONLY text and straight arrow are consistent with a dedicated through lane. |
                        unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            text:only: The word ONLY indicates that only the movement shown by the accompanying
                        arrow is permitted.
Step 5  Rule            arrow:straight: The straight arrow indicates that the vehicle may proceed straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    allowed (contested, correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): Allowed by the straight arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): Prohibited by the straight arrow and ONLY text, which restrict
                        movement to straight only.
Step 6  turn_right      prohibited (correct): Prohibited by the straight arrow and ONLY text, which restrict
                        movement to straight only.
Step 6  u_turn          prohibited (correct): Prohibited by the straight arrow and ONLY text, which restrict
                        movement to straight only.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in my lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the right lane if needed, but do
                        not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 809, 40.23 s

bdd100k_val__c400a0e1-c137168b | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an exit ramp ahead to the right. (lanes 3,
                        mine 1, full)
Step 2  Left            A solid yellow line is painted on the pavement next to a concrete barrier.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (3) and ego position (1) agree with the left boundary being a
                        center line (yellow) and the right being a lane line (white). | roles: The yellow
                        solid line on the left fits the role of a center line/edge line for opposing traffic;
                        the white dashed line on the right fits the role of a lane line. | markings: There are
                        no markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): The left boundary is a solid yellow line, which prohibits
                        crossing per [CN-6.1.4].
Step 6  change_right    allowed (contested, correct): The right boundary is a broken white line, which allows
                        crossing per [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the solid yellow
                        line to the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 632, 34.78 s

bdd100k_val__c464c963-0279dcc0 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           A residential two-way road with parked cars on both sides; the road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            A double solid yellow line separates my lane from the opposite direction of travel.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           There is no painted line on the right, but parked cars and a curb define the edge of
                        the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 agree with the center line on
                        the left and the edge on the right. | roles: The yellow double solid line fits the
                        role of a center line separating opposite traffic. | markings: There are no markings
                        in my lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: No painted line exists, but the physical curb prohibits leaving the
                        roadway. [null]
Step 6  change_left     prohibited (correct): Prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  change_right    prohibited (correct): Prohibited by the physical curb and edge of the roadway.
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          prohibited: Prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines to the
                        left or drive off the road to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 7601, out 767, 40.34 s

bdd100k_val__c4b77809-63fd577c | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street in the United States, approaching an intersection. (lanes
                        1, mine 1, full)
Step 2  Left            A double solid yellow line separates my lane from the opposite direction of traffic.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A white solid line marks the right edge of the roadway, with a parked white truck and
                        a curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:stop (full): The word STOP is painted in white across the lane.; line:stop_line
                        (full): A solid white line is painted across the lane at the intersection entrance.
Step 4  Cross-check     position: The double yellow line on the left and the white edge line on the right
                        confirm my lane is the only lane for my direction. | roles: The yellow color for the
                        center line and white for the edge line are consistent with standard road markings. |
                        markings: The STOP text and stop line are consistent with an intersection approach. |
                        unseen: No attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.2]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [CN-5.4.1]
Step 5  Rule            text:stop: The STOP marking indicates where vehicles must stop when waiting to
                        proceed. [CN-6.4.1-2]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [CN-6.4.1-2]
Step 6  change_left     prohibited (correct): Prohibited by the double solid yellow center line (CN-6.1.2).
Step 6  change_right    prohibited (correct): Prohibited by the solid white edge line and the presence of a
                        curb (CN-5.4.1).
Step 6  go_straight     stop_first (contested, correct): Allowed as there are no arrows restricting it, but
                        must stop first due to the STOP text and stop line.
Step 6  turn_left       not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the scene.
Step 7  Reflect         consistent
Advice                  Stay in your lane and come to a complete stop at the stop line before proceeding
                        straight through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 793, 35.67 s

bdd100k_val__c4d25f00-3b1d8669 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching a crosswalk and an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        sides. | roles: The white dashed lines fit the role of crossable lane lines. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in or next to the lane.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk', 'line:stop_line']), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 594, 38.32 s

bdd100k_val__c4e92086-e1b8324f | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with buildings on the right; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 2 agree with having lane lines on
                        both the left and right. | roles: The white broken lines fit the role of crossable
                        lane lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        allows crossing per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7601, out 595, 37.54 s

bdd100k_val__c55da7df-facccafc | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching an intersection or highway ramp split.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken white line separates my lane from the lane to its left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, beyond which is a shoulder
                        with a parked vehicle.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): The word 'ONLY' followed by a right-turn arrow is painted in the
                        lane.; text:only (full): The word 'ONLY' is painted before the arrow.
Step 4  Cross-check     position: The lane count of 3 and ego position 3 agree with the right boundary being
                        an edge line and the left boundary being a lane line. | roles: White dashed line for
                        lane_line and white solid line for edge_line are consistent with the roles. |
                        markings: The 'ONLY' text and right-turn arrow are consistent with a dedicated turn
                        lane. | unseen: No attributes were reported without visual evidence. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white edge line marks the edge of the motor vehicle lane.
                        [CN-5.4.1]
Step 5  Rule            arrow:right: The right-turn arrow indicates that the direction of travel for this lane
                        is to turn right. [CN-5.13.1]
Step 5  Rule            text:only: The text 'ONLY' indicates that the movement shown by the accompanying arrow
                        is mandatory. [CN-5.14.1]
Step 6  change_left     allowed (correct): allowed; the left boundary is a broken white line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited; the right boundary is a solid white edge
                        line (CN-4.2.2-a).
Step 6  go_straight     prohibited (contested, label allowed): prohibited; the lane is marked with a right-
                        turn arrow and 'ONLY' (CN-5.13.1).
Step 6  turn_left       prohibited: prohibited; the lane is marked with a right-turn arrow and 'ONLY'
                        (CN-5.13.1).
Step 6  turn_right      allowed: allowed; the lane is marked with a right-turn arrow (CN-5.13.1).
Step 6  u_turn          prohibited: prohibited; the lane is marked with a right-turn arrow and 'ONLY'
                        (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a mandatory right-turn lane. If you intend to go straight or turn left, you
                        must change to the left lane immediately.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 7601, out 1062, 45.34 s

bdd100k_val__c588eb5e-dfd59d8e | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at dusk, looking straight ahead towards a
                        distant intersection. (lanes 2, mine 2, full)
Step 2  Left            A double solid yellow line separates my lane from the opposing traffic flow.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count (2) and ego position (2) agree with the boundaries: a center
                        line on the left and a lane line on the right. | roles: The yellow double solid line
                        fits the role of a center line; the broken white line fits the role of a lane line. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): The left boundary is a double solid yellow line, which prohibits
                        crossing per [CN-6.1.2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a double solid yellow line, which prohibits crossing
                        per [CN-6.1.2].
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the double yellow
                        line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['rightmost lane, but a lane line on the right', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 7601, out 638, 30.77 s

bdd100k_val__c59500f0-130d7415 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The road is a multi-lane urban street with traffic moving in both directions. Ahead is
                        a clear stretch of road with no immediate intersection or ramp visible. (lanes 2, mine
                        2, full)
Step 2  Left            A double solid yellow line separates my lane from the opposite direction of traffic.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to its right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and my position as index 2 agree with the boundaries: a
                        center line on the left and a lane line on the right. | roles: The yellow double solid
                        line fits the role of a center line, and the broken white line fits the role of a lane
                        line. | markings: There are no markings in my lane to contradict. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): The left boundary is a double solid yellow line, which prohibits
                        crossing according to [CN-6.1.2].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a double solid yellow line, which prohibits crossing
                        and thus prohibits a U-turn according to [CN-6.1.2].
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the double yellow
                        line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['rightmost lane, but a lane line on the right', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 7601, out 668, 42.76 s

bdd100k_val__c5b2506d-07e406a6 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban city road with tall buildings on both sides;
                        the road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 608, 37.46 s

bdd100k_val__c74ee988-8f4b380d | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides; the road ahead appears to be
                        a straight stretch with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            A double solid yellow line separates my lane from the opposite direction of traffic.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           There is no painted line on the right, but a row of parked cars and a curb define the
                        edge of the roadway.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The double yellow line on the left and the curb on the right indicate my
                        lane is the only lane for my direction. | roles: The yellow color and double solid
                        pattern of the left boundary fit the role of a no-crossing center line. | markings:
                        There are no markings in my lane to contradict the boundaries. | unseen: No attributes
                        were reported without being visible. | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The right boundary marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): The left boundary is a double solid yellow line, which prohibits
                        crossing according to [CN-6.1.2].
Step 6  change_right    prohibited (contested, correct): The right boundary is a curb, which physically
                        prohibits leaving the lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a double solid yellow line, which prohibits crossing
                        and thus prohibits a U-turn according to [CN-6.1.2].
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow line to the
                        left or attempt to drive onto the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 7601, out 655, 38.63 s

bdd100k_val__c7c042ec-4986a853 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching an intersection. (lanes 2,
                        mine 2, full)
Step 2  Left            A broken white line separates my lane from another lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, with a curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 2 agree with a lane line on the left
                        and an edge line on the right. | roles: The white broken line fits the role of a lane
                        line, and the white solid line fits the role of an edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported without
                        being seen. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the boundary of the motor vehicle
                        lane. [[CN-5.4.1]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (correct): Allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable (WRONG, label not_determined): Not applicable as there are no arrows or
                        waiting areas governing this.
Step 6  turn_right      not_applicable (WRONG, label allowed): Not applicable as there are no arrows or
                        waiting areas governing this.
Step 6  u_turn          not_applicable (WRONG, label not_determined): Not applicable as there are no arrows or
                        waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but you
                        cannot cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:straight_right']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 639, 37.61 s

bdd100k_val__c96ffe59-1cf2df11 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings and parked cars on both sides, looking
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A solid yellow line separates my lane from the opposite direction of traffic.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A solid white line marks the right edge of the roadway, next to a parking area.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the center line on the left
                        and edge line on the right. | roles: The yellow solid line fits the role of a center
                        line, and the white solid line fits the role of an edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white; it marks the edge of the roadway. [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow center line,
                        which prohibits crossing according to [CN-6.1.4].
Step 6  change_right    prohibited (correct): The right boundary is a solid white edge line; while [CN-5.4.3]
                        defines it, [CN-4.2.2-a] states a solid line means crossing is normally prohibited.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to carrying on straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 650, 47.89 s

bdd100k_val__ca15f699-e51c14c0 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, heading towards a distant intersection
                        with traffic signals. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane to the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego position 2 agree with having lane lines on both
                        the left and right. | roles: The white dashed lines fit the role of crossable lane
                        lines. | markings: There are no markings in the lane to contradict. | unseen: No
                        attributes were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line allows crossing for lane changes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line allows crossing for lane changes.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing per
                        CN-5.2.1-2.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may proceed straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 596, 24.35 s

bdd100k_val__fe194677-e2d2ac8c | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, likely at an airport terminal pickup/drop-off
                        area, with other vehicles ahead. (lanes 3, mine 1, full)
Step 2  Left            There is no painted line on the left, but a large pile of snow and a curb separate the
                        lane from the sidewalk area.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 3 and ego_lane_index 1 agree with the left boundary being
                        an edge/curb and the right boundary being a lane line. | roles: The white dashed line
                        on the right fits the role of a lane line separating traffic in the same direction. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: The boundary marks the edge of the motor vehicle lane. [CN-5.4.1]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (contested, label not_determined): Prohibited by the physical curb and snow
                        pile (left_boundary).
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right if needed. Do not attempt to move left due to
                        the curb and snow.
Score                   lane False, boundaries {'left': None, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 7601, out 788, 42.94 s
```
