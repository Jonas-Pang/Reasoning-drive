# Reasoning of lane run 20261117_120833_laneB_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        intersections or ramps immediately visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken yellow line separating my lane from the lane to the left. Photo
                        2 shows the same broken yellow line next to my car, with several long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, bordering a shoulder or non-motorized
                        area. Photo 2 shows this solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a center line on the left and an edge line on the right. |
                        roles: the yellow dashed line fits the role of a crossable center line, and the white
                        solid line fits the role of a road edge line. | markings: no markings in my lane to
                        check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel; crossing it is normally prohibited by [CN-4.2.2-a]. [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed by the broken yellow center line and rule [CN-5.1.1].
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and rule [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow in view.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow in view.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection in view.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may change to the left lane if safe, but do not
                        cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 729, 9.58 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road in China, approaching a bridge or overpass.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms a broken white line next to my car with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a shoulder and a metal
                        guardrail. Photo 2 shows the solid white line next to my car and the guardrail further
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (2) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: no markings are
                        present in my lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 854, 14.56 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, moving straight ahead on a clear
                        road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow solid line on the left. Photo 2 shows the same yellow solid
                        line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car and further ahead. Photo 2 shows a
                        white broken line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a center line; the white
                        broken line on the right fits the role of a lane line. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid yellow center line
                        [CN-6.1.4].
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings.
Step 6  u_turn          prohibited: Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not cross the yellow line
                        to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8281, out 820, 25.16 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead on a bridge
                        or elevated section. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my car that is broken. Photo 2 confirms
                        this is a broken yellow line next to my car, with clear yellow dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car, and further ahead it remains
                        solid. Photo 2 shows a solid white line immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a center line on the left and an edge line on the right
                        indicate my lane is the rightmost lane of my direction. | roles: The yellow dashed
                        line on the left fits the role of a crossable center line. The white solid line on the
                        right fits the role of a road edge line. | markings: No markings are present in my
                        lane, which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken yellow center line allows crossing to overtake, turn, or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken yellow center line
                        [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 873, 13.39 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow dashed line separating my lane from the lane to the left. Photo
                        2 confirms this is a yellow broken line next to my car, with visible dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a concrete barrier. Photo 2
                        shows a white solid line immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show white Chinese characters '专用' and '交' (part
                        of '公交专用' meaning Bus Only) painted longitudinally in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2nd
                        from left) agree with the boundaries: a center line on the left and an edge line on
                        the right. | roles: The yellow dashed line fits the role of a crossable center line;
                        the white solid line fits the role of a road edge line. | markings: The '公交专用' text
                        indicates this is a bus lane, which is consistent with the road layout. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable center line allows crossing to overtake, turn, or make a
                        U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the bus lane. [[CN-6.9.1]]
Step 6  change_left     allowed (contested, correct): allowed by the yellow dashed center line [CN-5.1.1].
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight, but
                        the lane is reserved for buses [CN-6.9.1].
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane ('公交专用'). If you are not driving a bus, you should
                        change left into the general traffic lane as soon as it is safe to do so.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 993, 29.53 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an underpass. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues forward. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, continuing forward. Photo 2 confirms
                        a single solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries, as both sides are edge lines (road boundaries). | roles: The
                        white solid lines on both sides fit the role of edge lines for a single-lane road or a
                        separated road section. | markings: No markings are present in the lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): Prohibited by the solid white left boundary (CN-4.2.2-a).
Step 6  change_right    prohibited (correct): Prohibited by the solid white right boundary (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the underpass; lane changes are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 798, 11.25 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus stop on the left and parked scooters on the
                        right. The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, extending forward. Photo 2 confirms
                        a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, extending forward. Photo 2 confirms
                        a single solid white line next to the car, with a raised curb immediately to its
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the boundaries being edge lines on both sides | roles: the white color and solid
                        pattern fit the role of edge lines for a single-lane road | markings: no markings in
                        lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A white edge line on the left side of the direction of travel is
                        permitted on a single-lane two-way road. [[CN-5.4.3]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): the left boundary is a solid white line, and [CN-4.2.2-a]
                        prohibits crossing a solid line
Step 6  change_right    prohibited (correct): the right boundary is a solid white line and a curb, and
                        [CN-4.2.2-a] prohibits crossing a solid line
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 666, 10.35 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right side of the road. Photo 2 shows this
                        solid yellow line next to my car, marking the edge of the motor vehicle lanes.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right.
                        | roles: The white dashed line fits the role of a crossable lane line, and the yellow
                        solid line fits the role of a left-hand edge line for opposing traffic or a right-hand
                        edge line for the current direction if it's a specific road type, but per CN-5.4.3,
                        right edge lines should be white. However, yellow is used for opposite direction
                        separation. Looking at the scene, this is the rightmost lane of the direction of
                        travel. | markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you must not cross the solid yellow line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 8281, out 932, 14.46 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no immediate
                        intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the roadway. Photo 2 confirms
                        this solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to the car with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundaries: a center line on the left and a lane line on the right.
                        | roles: the yellow solid line on the left fits the role of a no-crossing center line;
                        the white broken line on the right fits the role of a crossable lane line. | markings:
                        no markings are present in the lane, which is consistent with the boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 840, 8.65 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        traffic signals ahead. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 4 and ego_lane_index 3
                        are consistent with having lane lines on both the left and right boundaries. | roles:
                        White dashed lines are consistent with the role of crossable lane lines separating
                        traffic in the same direction. | markings: No markings were observed in the lane,
                        which is consistent with the boundaries. | unseen: No attributes were reported that
                        were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that the lane may be crossed.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line indicates that the lane may be crossed.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed: Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed: Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right. Be mindful of the traffic signals at the upcoming intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8281, out 827, 26.89 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, approaching a straight stretch
                        with no immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a white fence. Photo 2 confirms a single
                        solid yellow line immediately to the left of the lane.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a no-crossing center line;
                        the white broken line on the right fits the role of a crossable lane line. | markings:
                        No markings are present in the lane, which is consistent with the boundaries. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, label not_determined): Allowed as no markings restrict carrying on
                        straight along the lane.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['symbol:other']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 845, 12.71 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or bridge, heading straight toward a slight
                        curve in the distance. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the car is in a single lane bounded by edge lines on both sides |
                        roles: the white solid lines on both sides fit the role of edge lines for a single-
                        lane road section | markings: no markings in the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow, but here it is white, which may occur on single-lane two-way roads or specific
                        road configurations; however, the solid pattern generally prohibits crossing.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white; the solid pattern prohibits crossing. [CN-5.4.3] "An edge line on the right
                        side of the direction of travel shall be white, and an edge line on the left side of
                        the direction of travel shall be yellow; a motor/"
Step 6  change_left     prohibited (correct): the left boundary is a solid white line, and according to
                        CN-4.2.2-a, crossing a solid line is normally prohibited.
Step 6  change_right    prohibited (correct): the right boundary is a solid white line, and according to
                        CN-4.2.2-a, crossing a solid line is normally prohibited.
Step 6  go_straight     allowed (contested, correct): no marking governs this action, and there are no
                        restrictions to continuing straight.
Step 6  turn_left       not_applicable: no marking governs this action.
Step 6  turn_right      not_applicable: no marking governs this action.
Step 6  u_turn          not_applicable: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 692, 12.83 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway passing under an overpass. (lanes 2, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the road, next to a guardrail.
                        Photo 2 confirms this solid yellow line is immediately to the left of my car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a single white dash and gap immediately to the right of my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a yellow edge line on the left indicates my lane is the leftmost
                        lane of my direction. | roles: the yellow solid line on the left fits the role of a
                        left edge line; the white broken line on the right fits the role of a lane line. |
                        markings: no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line separates traffic flows in the same
                        direction and may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 887, 13.55 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the roadway. Photo 2 confirms a
                        solid yellow line immediately to the left of my car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a broken white line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundaries; a yellow edge line on the left indicates my lane is the
                        leftmost motor vehicle lane. | roles: the yellow solid line fits the role of a left
                        edge line, and the white broken line fits the role of a crossable lane line. |
                        markings: there are no markings in my lane to contradict. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not cross the solid yellow line on the
                        left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 870, 12.2 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which remains broken further ahead.
                        Photo 2 confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows a white broken line
                        with dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the middle of the
                        lane. Photo 1 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: white broken
                        lines correctly serve as lane lines separating traffic in the same direction. |
                        markings: the straight-ahead arrow is consistent with the lane's position and
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates the vehicle should travel straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a broken
                        white line [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): allowed because the lane marking is a straight-ahead arrow
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area in or next to the
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. You may change lanes to the
                        left or right if needed before the boundaries become solid.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation accepted, contradictions []
Tokens                  in 8281, out 990, 13.19 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a large intersection. (lanes 3, mine
                        1, full)
Step 2  Left            Photo 1 shows a yellow solid line on the left. Photo 2 shows a yellow solid line next
                        to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line. Photo 2 shows a white broken line next to the car
                        with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2 shows a white crosswalk (zebra stripes) across the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left and
                        white lane line on the right agree that my lane is the leftmost lane of my direction.
                        | roles: The yellow solid line fits the role of a no-crossing center line; the white
                        broken line fits the role of a crossable lane line. | markings: The crosswalk is a
                        standard marking across the lane before an intersection. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern the seven
                        vehicle actions. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or change to the right lane, but you
                        must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation unlisted,
                        contradictions []
Tokens                  in 8281, out 898, 13.59 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight toward a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: The white dashed lines on both sides correctly fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        my lane, which is consistent with the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no guide arrows or waiting areas in my
                        lane.
Step 6  turn_right      not_applicable: Not applicable as there are no guide arrows in my lane.
Step 6  u_turn          not_applicable: Not applicable as there are no guide arrows in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 852, 11.76 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car and a raised curb. Photo 2 confirms a
                        white solid line and a concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the right boundary being an edge line and the left boundary being a lane
                        line. | roles: The white dashed line on the left fits the role of a lane line; the
                        white solid line and curb on the right fit the role of an edge line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 825, 15.47 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        overhead signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that remains broken further ahead.
                        Photo 2 confirms a white broken line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that remains broken further ahead.
                        Photo 2 confirms a white broken line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with the role of crossable lane lines | markings: no markings were
                        observed in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white lane line
                        (CN-5.2.1-2)
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 779, 10.16 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line. There is a curb and greenery to the right of this
                        line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right
                        (though the right boundary is an edge line, the lane count includes the rightmost
                        lane; however, looking at the image, there are 3 lanes total, and my car is in the
                        middle one, but the right boundary is the road edge, meaning there are only 2 lanes in
                        this direction. Let me re-evaluate: Photo 1 shows three lanes total: one far left, my
                        lane, and one to my right. My lane is the middle one. The right boundary of my lane is
                        a broken white line, and the rightmost lane is bounded by the solid white edge line.
                        Wait, looking closer at Photo 2, the line to my right is solid white. This means my
                        lane is the rightmost lane. Let me re-count: there is a lane to my left, and my lane.
                        Total 2 lanes. My lane index is 2.) | roles: The white dashed line on the left is a
                        lane line; the white solid line on the right is an edge line. | markings: The straight
                        arrow is consistent with a through lane. | unseen: no | result: corrected lane_count
                        to 2 and ego_lane_index to 2
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (correct): allowed by the straight guide arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited by the straight guide arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight guide arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight guide arrow [CN-5.13.1] which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not cross the solid line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 1151, 17.49 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with a
                        bridge in the distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: white
                        dashed lines are consistent with lane lines separating traffic in the same direction |
                        markings: no markings are present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): the left boundary is a broken white line, which allows crossing per
                        [CN-5.2.1-2]
Step 6  change_right    allowed (WRONG, label not_determined): the right boundary is a broken white line,
                        which allows crossing per [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): no marking restricts going straight in this lane
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 637, 9.79 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a wide intersection or a
                        junction where the road curves slightly to the left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a broken yellow line next to the car with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that becomes solid further ahead.
                        Photo 2 shows a broken white line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a yellow center line on the left and a white lane line on the
                        right place the car in the second lane from the left of its direction (assuming a
                        3-lane setup where the leftmost is a turn lane or similar, but here the yellow line
                        indicates the center of the road). Actually, with a yellow line on the left, my lane
                        is the leftmost motor vehicle lane of my direction. | roles: the yellow dashed line
                        fits the role of a crossable center line, and the white dashed line fits the role of a
                        crossable lane line. | markings: no markings in the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The crossable centre line allows vehicles to cross to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The crossable lane line allows vehicles to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken yellow center line [CN-5.1.1]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          allowed: allowed by the broken yellow center line [CN-5.1.1]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a lane with crossable boundaries on both sides. You may change lanes or
                        proceed straight.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8281, out 741, 11.59 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, approaching a section with
                        overhead lane guidance signs. (lanes 5, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 5 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        correctly serve as lane lines separating traffic in the same direction. | markings: No
                        markings are present in the lane, which is consistent with a standard highway through
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that crossing it to change lanes
                        is permitted. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that crossing it to change lanes
                        is permitted. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
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
Advice                  You are in a through lane on a highway. You may continue straight or change lanes to
                        the left or right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['text:other']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 817, 11.99 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, heading straight on a clear road
                        with an overhead gantry in the distance. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and my position in
                        lane 2 agree with having lane lines on both my left and right | roles: the white
                        dashed patterns fit the role of crossable lane lines | markings: no markings are
                        present in my lane, which is consistent with a highway through-lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through-lane on a highway. You may continue straight or change lanes to
                        the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 838, 12.18 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead guide arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right. | roles: The white
                        dashed lines on both sides correctly fit the role of crossable lane lines separating
                        traffic in the same direction. | markings: The straight-ahead arrow is consistent with
                        the lane boundaries and the general flow of traffic. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): allowed because the right boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): allowed because the guide arrow in my lane indicates straight ahead
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the guide arrow only allows straight movement
                        [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the guide arrow only allows straight movement
                        [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the guide arrow only allows straight movement
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right. Do not attempt to turn left or right from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 995, 13.72 s
```
