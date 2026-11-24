# Reasoning of lane run 20261117_172755_laneB_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road. The road continues straight ahead
                        with no immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line separating my lane from the lane to the left. Photo
                        2 shows the same yellow broken line next to my car, continuing further ahead. Photo 3
                        shows a yellow line with a gap from approximately 45% to 60% of the height.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right edge of the road. Photo 2 shows this
                        white solid line running from the bottom to the top of the frame. Photo 4 shows the
                        paint running unbroken from the bottom to the top of the photo. There is a metal
                        guardrail and a curb beyond the line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a center line on the left (meaning my lane is the leftmost
                        of its direction if it were a 2-way road, but here it separates opposing traffic) and
                        an edge line on the right. | roles: The yellow dashed line fits the role of a
                        crossable center line. The white solid line fits the role of a road edge line. |
                        markings: No markings in lane, consistent with boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: Crossing the solid white edge line is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken yellow center line [CN-5.1.1].
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action, though the center line
                        allows crossing for it.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change lanes to the left, but do
                        not cross the right edge line into the shoulder.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 936, 17.09 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road in China, heading towards an overpass.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a white broken line next to my car, with a gap from approximately 45% to 60%
                        of the height, and continuing as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 and Photo 4
                        show a continuous white line from the bottom to the top of the photo, with no gaps.
                        There is a metal guardrail (barrier) immediately to the right of this line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (2) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: no markings were
                        observed in my lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which allows
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line, and
                        crossing is prohibited per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 900, 19.21 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from another lane to the left.
                        Photo 2 shows a white dash and gap next to my car, and the line continues as a broken
                        line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line on the right, with a metal guardrail beside it.
                        Photo 2 shows the yellow paint running unbroken from the bottom to the top of the
                        close-up area.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my position (1)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line fits the role of a lane line; the yellow solid line fits
                        the role of a left-hand edge line for the opposite direction or a right-hand edge line
                        for a specific road type, but here it marks the right edge of the carriageway. |
                        markings: no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid yellow edge line
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may stay in your lane or change to the left lane. Do not cross the solid yellow
                        line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['leftmost lane, but
                        a lane line on the left']
Tokens                  in 9053, out 869, 30.92 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead on a bridge or
                        elevated section. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line separating my lane from the lane to the left. Photo
                        2 shows the same yellow broken line next to my car, with a gap from approximately 45%
                        to 60% of the height, and continuing as a broken line further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, next to a physical barrier. Photo 2
                        shows a white solid line running unbroken from the bottom to the top of the photo,
                        with a raised concrete barrier immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a center line on the left (meaning my lane is the leftmost
                        of the direction if it were a 2-way road, but here it separates opposing traffic or a
                        special lane) and an edge line on the right. | roles: The yellow dashed line on the
                        left fits the role of a crossable center line. The white solid line on the right fits
                        the role of a road edge line. | markings: No markings are present in the lane, which
                        is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The crossable center line allows vehicles to cross to overtake, turn,
                        or make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the yellow dashed center line
                        [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a]
                        and the physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          allowed: allowed by the yellow dashed center line [CN-5.1.1].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane if
                        safe; changing to the right is prohibited due to the solid edge line and barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 9053, out 934, 18.38 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with high-rise buildings on both sides. The road
                        ahead appears to be a straight stretch with no immediate intersection or ramp. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows this line is a solid yellow line next to my car, continuing straight ahead.
                        yellow solid, curb no, special_lane_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a solid white line next to my
                        car, and Photo 4 confirms it is solid from the bottom to the top of the image. There
                        is a concrete barrier (curb) immediately to the right of this line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 and Photo 3 show white Chinese characters '专用公交' (Special
                        Bus) painted vertically in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2nd
                        from left) agree with the boundaries: a special lane line on the left and an edge line
                        on the right. | roles: The yellow solid line on the left fits the role of a special
                        lane boundary (bus lane), and the white solid line on the right fits the role of a
                        road edge line. | markings: The '公交' (bus) text in the lane agrees with the yellow
                        boundary on the left, indicating this is a reserved bus lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The bus lane line indicates that vehicles other than buses shall not
                        enter the lane. [CN-6.9.1] "The bus lane line shows that vehicles other than buses
                        shall not enter the lane. It consists of a broken white line and white text. The
                        broken line has 5 m segm"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            text:bus: The text '公交' indicates the lane is reserved for buses, and other vehicles
                        shall not enter. [CN-6.9.1] "The bus lane line shows that vehicles other than buses
                        shall not enter the lane. It consists of a broken white line and white text. The
                        broken line has 5 m segm"
Step 6  change_left     prohibited (contested, label allowed): allowed by the solid yellow line if it is
                        treated as a lane line, but the bus lane rule CN-6.9.1 prohibits entering the lane;
                        however, since I am already in it, leaving it to the left is governed by the line
                        pattern. CN-4.2.2-a prohibits crossing a solid line.
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        (CN-4.2.2-a) and the physical concrete barrier.
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight in
                        the current lane, although the lane is reserved for buses.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  u_turn          not_applicable: prohibited by the bus lane rule CN-5.3.1-2 (by analogy to tidal lanes)
                        or simply not applicable as no intersection is present.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently driving in a reserved bus lane. You should move out of this lane as
                        soon as it is legally permitted, but currently, the solid lines on both sides prohibit
                        lane changes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 1115, 35.49 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an underpass. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 shows the same
                        solid white line running from the bottom to the top of the frame.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a stone wall. Photo 2 shows the line running
                        unbroken from the bottom to the top. Photo 4 confirms the paint is continuous from the
                        bottom edge upward with no gaps.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the presence of edge lines on both sides. | roles: White solid lines on both
                        sides of a single lane are consistent with edge lines marking the roadway boundaries.
                        | markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The left boundary is a solid white line, which prohibits
                        crossing per [CN-4.2.2-a].
Step 6  change_right    prohibited (correct): The right boundary is a solid white line, which prohibits
                        crossing per [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the boundaries do
                        not restrict it.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the underpass; lane changes are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9053, out 798, 14.09 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus stop on the left and parked scooters on the
                        right. The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows the line next to the car
                        is solid white and continues as a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the line next to the car
                        is solid white and continues as a solid white line further ahead. Photo 4 shows the
                        paint runs unbroken from the bottom to the top of the photo.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries being edge lines on both sides. | roles: White solid lines on both
                        sides are consistent with edge lines for a single-lane road. | markings: No markings
                        are present in the lane, which is consistent with the boundaries. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary between motor
                        vehicle lanes and non-motorized lanes. [CN-5.4.3] "An edge line on the right side of
                        the direction of travel shall be white, and an edge line on the left side of the
                        direction of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The white edge line on the right marks the edge of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary (CN-4.2.2-a).
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary and the physical
                        curb (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white lines on either
                        side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9053, out 851, 16.74 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line to the left of my lane. Photo 2 shows this line is broken
                        next to my car and continues as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line is solid
                        next to my car and remains solid further ahead. Photo 4 shows the paint runs unbroken
                        from the bottom to the top of the photo.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings were observed
                        in my lane, which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on your right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 9053, out 860, 17.24 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road with trees and hedges on the left. The
                        road ahead appears to be a straight stretch with no immediate intersection or ramp.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a hedge. Photo 2 shows the same solid white
                        line running from the bottom to the top of the frame without any gaps.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line. Photo 2 shows a broken white line. Photo 4 shows a
                        piece of paint from the bottom to about 30% of the height, followed by a gap from 30%
                        to 60%, and then another piece of paint.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a white edge line on the left and a white lane line on the
                        right. | roles: The white solid edge line on the left and white dashed lane line on
                        the right fit their respective roles. | markings: No markings were observed in the
                        lane, which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white edge line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, and rule
                        [CN-4.2.2-a] prohibits crossing it.
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, and rule
                        [CN-5.2.1-2] allows crossing it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there are no
                        restrictions to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left boundary into the hedge area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 870, 12.91 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, approaching an intersection with traffic
                        signals ahead. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my car. Photo 2 shows the same white
                        broken line next to my car, and it continues as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my car. Photo 2 shows the same white
                        broken line next to my car, and it continues as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and ego_lane_index 3
                        agree with having lane lines on both left and right | roles: white dashed lines are
                        consistent with lane_line roles | markings: no markings present in my lane | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed: the left boundary is a broken white line, which allows crossing per
                        [CN-5.2.1-2]
Step 6  change_right    allowed: the right boundary is a broken white line, which allows crossing per
                        [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): no marking restricts going straight in this lane
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9053, out 644, 26.84 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no immediate
                        intersections or ramps visible in the foreground. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line next to a white fence. Photo 2 shows a solid yellow line
                        running along the base of the fence next to my car, continuing straight ahead.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from a parking or shoulder area. Photo 2
                        and Photo 4 show a broken white line next to my car, with a gap from approximately 60%
                        to 75% of the height of Photo 4. Further ahead in Photo 1, the line remains broken.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The yellow edge line on the left and
                        white edge line on the right indicate my lane is the only motor vehicle lane in this
                        section of the road. | roles: The yellow left edge line and white right edge line are
                        consistent with GB 5768.3-2025 for a single-lane road or the edge of the carriageway.
                        | markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the left-hand edge of the
                        direction of travel. [[CN-5.4.3]]
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: The white edge line on the right marks the right-hand edge of the
                        direction of travel. [[CN-5.4.3]]
Step 5  Rule            right_boundary: A broken line means it may be crossed. [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [CN-4.2.2-a].
Step 6  change_right    allowed (correct): allowed by the broken white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, label not_determined): allowed as no markings restrict carrying on
                        straight along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may move to the right across the broken
                        line if needed, but do not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['symbol:other']), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 9053, out 1006, 41.71 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or highway, traveling straight ahead on a bridge
                        or elevated section. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left. Photo 2 shows this line is solid and runs
                        continuously from the bottom to the top of the close-up area. Photo 3 confirms the
                        paint is unbroken from the bottom edge to the top of the photo.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is solid and runs
                        continuously from the bottom to the top of the close-up area. Photo 4 confirms the
                        paint is unbroken from the bottom edge to the top of the photo.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries, as both sides are edge lines (marked by solid white lines and
                        physical barriers). | roles: The white color and solid pattern fit the role of edge
                        lines on a road with physical barriers. | markings: No markings are present in the
                        lane, which is consistent with a simple through-lane on a bridge. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): Prohibited by the solid white left boundary line [CN-4.2.2-a].
Step 6  change_right    prohibited (correct): Prohibited by the solid white right boundary line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings
                        in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes are prohibited on both sides due
                        to solid edge lines and physical barriers.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 877, 17.9 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway passing under an overpass. (lanes 2, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, next to a guardrail. Photo 2 shows the
                        same solid white line running from the bottom edge upward without any gaps.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right. Photo 2 shows a dash and a gap. Photo
                        4 shows a dash from the bottom to about 30% of the height, followed by a gap from 30%
                        to 60%, and another dash above that.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white color and solid/dashed patterns fit the roles of
                        edge_line and lane_line for traffic in the same direction. | markings: No markings are
                        present in the lane, which is consistent with a highway stretch. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): The left boundary is a solid white edge line, and rule
                        [CN-4.2.2-a] prohibits crossing it.
Step 6  change_right    allowed (correct): The right boundary is a broken white lane line, and rule
                        [CN-5.2.1-2] allows crossing it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left edge line into the shoulder/guardrail area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 855, 17.77 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway with overhead signs indicating speed
                        limits for through lanes and an emergency vehicle lane. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line next to my car, with a gap from 45% to 60% of the height,
                        and continuing as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line next to my car, with a gap from 50% to 65% of the height,
                        and continuing as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        a standard highway through lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement in this lane.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings
                        in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a through lane on a highway. You may continue straight or change lanes to
                        the left or right as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 9053, out 895, 16.29 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 and
                        Photo 3 show this line is broken, with a gap from approximately 45% to 60% of the
                        height of Photo 3.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2 and
                        Photo 4 show this line is solid from the bottom to the top of the photo.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible in my lane in Photo 2
                        and Photo 3.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed and
                        solid lines are consistent with lane lines separating traffic in the same direction. |
                        markings: The straight-ahead arrow is consistent with the lane's position and
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed for lane changes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from my side. [CN-6.2.1]
                        "The no-crossing lane line separates vehicles travelling in the same direction and
                        prohibits vehicles on the solid-line side from crossing. It has two forms: sin"
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white line
                        [CN-6.2.1].
Step 6  go_straight     allowed (correct): allowed because the lane marking is a straight-ahead arrow
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area in or next to my lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not cross the solid line to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left'],
                        citation accepted, contradictions []
Tokens                  in 9053, out 1010, 20.66 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a large intersection with a
                        crosswalk ahead. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line on the left. Photo 2 shows a yellow line next to the car,
                        and further ahead it remains yellow. Photo 3 shows the paint is unbroken from the
                        bottom to the top of the photo.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white line next to the car,
                        and further ahead it remains white. Photo 4 shows the paint is unbroken from the
                        bottom to the top of the photo.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2 shows a white zebra-striped crosswalk across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left and
                        white lane line on the right agree that my lane is the leftmost lane of my direction.
                        | roles: The yellow solid line fits the role of a no-crossing center line; the white
                        solid line fits the role of a no-crossing lane line. | markings: The crosswalk is a
                        standard transverse marking and does not contradict the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians to cross and does not govern
                        the seven vehicle actions. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not change lanes as both boundaries are
                        solid lines. Be mindful of pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 9053, out 954, 20.86 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road. The road ahead appears to be a
                        straight stretch with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line to the left of my car. Photo 2 shows a white broken
                        line next to my car, and further ahead it remains broken. Photo 3 shows a white line
                        with a gap from approximately 45% to 60% of the height.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my car. Photo 2 shows a white broken
                        line next to my car, and further ahead it remains broken. Photo 4 shows a white line
                        with a gap from approximately 40% to 55% of the height.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right sides. | roles: White
                        dashed lines are consistent with the role of crossable lane lines separating traffic
                        in the same direction. | markings: No markings were observed in the lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 886, 17.81 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road. Ahead is a clear stretch of road with
                        no immediate intersection or ramp visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a long white dash followed by a gap. Photo 3 shows a white dash from the
                        bottom to about 40% of the height, then a gap from 40% to 60%, then another dash.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows a
                        continuous white line. Photo 4 shows the paint running unbroken from the bottom to the
                        top of the photo.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right. | roles: The
                        white dashed line on the left fits the role of a crossable lane line; the white solid
                        line on the right fits the role of a road edge line. | markings: No markings were
                        found in the lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you must not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 911, 17.95 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection or a road
                        section with guidance markings. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line separating my lane from the lane to the left. Photo 2 shows
                        this line is broken next to my car and continues as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the lane to the right. Photo 2
                        shows this line is broken next to my car and continues as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        no_turn:left (full): Photo 2 and Photo 4 show white Chinese characters '公交' (bus)
                        painted in the lane to the right, but not in my lane. Photo 2 and Photo 3 show white
                        Chinese characters '公交' (bus) painted in the lane to the left, but not in my lane. My
                        lane contains no text or arrows.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        index 2 agree with having lane lines on both the left and right. | roles: White dashed
                        lines are consistent with the role of crossable lane lines. | markings: No markings
                        are present in my lane, which is consistent with a general through lane. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow governing this action
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this action
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight or change lanes to the left or
                        right. Note that the lanes to your left and right are marked as bus lanes ('公交'), so
                        you should avoid entering them unless necessary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['no_turn:left'], missed []), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9053, out 948, 14.87 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line next to my car, and it continues as a broken line further
                        ahead. Photo 3 shows a white broken line with a gap from approximately 45% to 60% of
                        the height.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the rightmost lane. Photo 2
                        shows a white solid line next to my car and further ahead. Photo 4 shows the paint
                        runs unbroken from the bottom to the top of the photo.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having a lane line on both the left and right. | roles: White dashed and
                        solid lines are consistent with lane_line roles separating traffic in the same
                        direction. | markings: The straight arrow is consistent with the lane boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing it to change
                        lanes. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The guide arrow indicates that the allowed movement for this lane is
                        straight ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white line [CN-6.2.1].
Step 6  go_straight     allowed (correct): allowed because the lane marking is a straight arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the lane marking is a straight arrow, which
                        restricts movement to straight only [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the lane marking is a straight arrow, which
                        restricts movement to straight only [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the lane marking is a straight arrow, which
                        restricts movement to straight only [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but
                        changing to the right lane is prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 1017, 18.72 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead toward a
                        distant overpass. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, continuing forward. Photo 3 shows a
                        white line with a gap from approximately 65% to 80% of the height.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, next to a physical barrier. Photo 2
                        shows the solid yellow line and the barrier. Photo 4 shows the paint is unbroken from
                        the bottom to the top of the photo.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right. | roles: The
                        white dashed line fits the role of a crossable lane line; the yellow solid line with a
                        curb fits the role of a right-hand edge line for the direction of travel (though
                        usually right edges are white, yellow is used for specific separations or tidal lanes,
                        but here it marks the boundary to a physical barrier/bus lane area). | markings: No
                        markings in lane, consistent with boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: the right boundary is a solid
                        yellow line [CN-4.2.2-a] and there is a physical curb.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not attempt to move right as
                        it is blocked by a solid line and a physical barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 924, 18.35 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road that curves slightly to the right. There are no
                        immediate intersections or ramps ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my car. Photo 2 shows the same white
                        broken line next to my car, and it continues as a broken line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line to the right of my car. Photo 2 shows a yellow solid
                        line next to my car, and it remains solid further ahead. Photo 4 shows the paint is
                        unbroken from the bottom to the top of the photo.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a lane line on the left (though here it is the leftmost
                        lane of the direction, the line on the left is actually a lane line for a lane that
                        may be for a different purpose or the road is wider than 2 lanes; however, looking at
                        the right boundary being a yellow center line, my lane is the leftmost of the motor
                        vehicle lanes in my direction). Wait, if the right boundary is a center line, I am in
                        the rightmost lane of my direction. Let me re-evaluate: the yellow line is on the
                        right, meaning traffic in the opposite direction is to my right. This implies I am in
                        the rightmost lane of a one-way street or the rightmost lane of a two-way road. But
                        the prompt says traffic keeps to the right. If the yellow line is on my right, I am
                        driving on the left side of the road, which is incorrect for China. Let me re-examine
                        the photos. The yellow line is indeed on the right. This suggests the road is a one-
                        way street where the yellow line marks the edge, or I am in the opposite direction.
                        No, looking at the cars ahead, they are facing me. The yellow line separates my
                        direction from the opposite direction. Since the yellow line is on my right, I am in
                        the leftmost lane of my direction, and the opposite traffic is to my right. This is
                        highly unusual for China. Let me look again. The yellow line is on the right, the
                        white broken line is on the left. This means there is another lane of my direction to
                        my left. So I am in lane 2 of 2. Let me correct: lane_count 2, ego_lane_index 2. |
                        roles: The white broken line on the left is a lane line. The yellow solid line on the
                        right is a center line. | markings: No markings in lane. | unseen: no | result:
                        corrected lane_count to 2 and ego_lane_index to 2
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid yellow center line prohibits crossing into the opposite
                        traffic lane. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both
                        directions from crossing. It is generally used on two-lane two-way roads with limited
                        sight distance or wh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area exists
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of your direction. You may go straight or change to the
                        left lane, but you must not cross the solid yellow line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 9053, out 1193, 52.8 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 5, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 shows the same
                        solid white line running from the bottom to the top of the frame.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line. Photo 2 shows a broken white line. Photo 4 shows a
                        gap from approximately 45% to 60% of the height, indicating a dashed pattern.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): Photo 2 and Photo 3 show large white characters painted across
                        the lane, which appear to be part of a warning or guidance text (though the specific
                        characters are partially obscured by the car's hood).
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 5 and ego_lane_index 1
                        agree with the left boundary being an edge line and the right boundary being a lane
                        line. | roles: The white solid left edge line and white dashed right lane line fit
                        their respective roles. | markings: The text markings are informative and do not
                        contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            text:other: Informative text on the pavement does not restrict movement.
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        concrete barrier [CN-4.2.2-a].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not cross the left boundary as it is a
                        solid edge line with a barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 946, 18.47 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway with a clear road ahead. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line next to my car, with clear gaps between dashes. Photo 3
                        shows a white dash from the bottom to about 30% of the height, followed by a gap from
                        30% to 50%, and another dash above that.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line next to my car. Photo 4 shows a white dash from the bottom
                        to about 35% of the height, followed by a gap from 35% to 55%, and another dash above
                        that.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: White dashed
                        lines are consistent with the role of crossable lane lines separating traffic in the
                        same direction. | markings: No markings were observed in the lane, which is consistent
                        with a standard highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings
                        in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 912, 17.1 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with three lanes of travel in its direction,
                        heading towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line next to my car, with a gap from 40% to 55% of the height
                        of Photo 3.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line next to my car, with a gap from 40% to 55% of the height
                        of Photo 4.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines. | markings: The straight-ahead
                        arrow is consistent with the lane's position and boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the middle lane, which is designated for going straight. You may change
                        lanes to the left or right if needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9053, out 996, 41.36 s
```
