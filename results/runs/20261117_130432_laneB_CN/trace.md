# Reasoning of lane run 20261117_130432_laneB_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no immediate
                        intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a metal fence/barrier. Photo 2 confirms a
                        single solid yellow line immediately to the left of the car, running along the edge of
                        the roadway.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left and a white lane line on the
                        right. | roles: The yellow solid line on the left fits the role of a left-hand edge
                        line; the white broken line on the right fits the role of a crossable lane line. |
                        markings: No markings were observed in the lane, which is consistent with the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow edge line and the
                        physical barrier [CN-4.2.2-a]
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot move left due to the road edge and barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 865, 14.46 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with a single lane in its direction, heading
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, which is the edge of the roadway. Photo
                        2 confirms a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 confirms a solid white line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries being edge lines on both sides. | roles: The white color and solid
                        pattern fit the role of edge lines for a single-lane two-way road. | markings: No
                        markings are present in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: On a single-lane two-way road, the edge lines on both sides shall be
                        white. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: On a single-lane two-way road, the edge lines on both sides shall be
                        white. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white edge line;
                        crossing it is normally prohibited per CN-4.2.2-a.
Step 6  change_right    prohibited (contested, correct): The right boundary is a solid white edge line;
                        crossing it is normally prohibited per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to either side are prohibited by
                        the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 821, 13.56 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 777, 11.11 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road with an elevated railway structure on
                        the right. The road continues straight ahead. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a raised curb and fence. Photo 2 confirms a
                        single solid white line immediately to the left of the car, continuing straight ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of a motor/non-motor
                        separation edge line, and the white broken right boundary fits the role of a crossable
                        lane line. | markings: No markings are present in the lane, which is consistent with
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb [CN-4.2.2-a].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left boundary into the non-motorized area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 862, 15.14 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, with an elevated highway
                        structure on the right and a construction fence on the left. The road continues
                        straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, continuing straight ahead. Photo 2
                        confirms a single solid white line next to the car, with a raised curb and fence
                        immediately to its left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a white edge line on the left and a white lane line on the
                        right. | roles: The white solid edge line on the left and white broken lane line on
                        the right fit their respective roles. | markings: No markings were observed in the
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The white edge line marks the boundary between the motor vehicle lane
                        and the non-motorized lane or road edge. [CN-5.4.3] "An edge line on the right side of
                        the direction of travel shall be white, and an edge line on the left side of the
                        direction of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The broken white lane line separates traffic flows in the same
                        direction and may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid line and there is a
                        raised curb, and CN-4.2.2-a prohibits crossing solid lines.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which
                        CN-5.2.1-2 allows crossing.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot move left due to the curb and solid edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 886, 15.43 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, driving straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a landscaped median. Photo 2
                        confirms a single solid white line next to the car, continuing straight ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a broken white line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of an edge_line
                        (motor/non-motor or road edge), and the white broken right boundary fits the role of a
                        crossable lane_line. | markings: No markings were observed in the lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge_line
                        (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white lane_line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the solid line to the left into the median.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 874, 15.06 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards a
                        distant overpass. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a white solid line immediately to the left of the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow broken line next to the car, which continues ahead. Photo 2
                        shows a yellow broken line with long dashes and gaps immediately to the right of the
                        car.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a lane line on the left (separating from another lane of
                        the same direction) and a center line on the right (separating from opposite traffic).
                        Wait, if the right boundary is a center line, my lane is the rightmost lane. If the
                        left boundary is a lane line, there is another lane to my left. This means I am in
                        lane 1 of 2. This is consistent. | roles: The white solid line on the left acts as a
                        lane line; the yellow broken line on the right acts as a center line. This fits the
                        roles. | markings: No markings were found in my lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits the vehicle on the solid side from
                        crossing it. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: A broken yellow center line allows vehicles to cross to overtake,
                        turn, or make a U-turn when safe. [CN-5.1.1] "The crossable centre line separates
                        traffic flows in opposite directions. It means vehicles may cross the line to
                        overtake, turn or make a U-turn when this does"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line (CN-6.2.1).
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken yellow center line
                        (CN-5.1.1).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may proceed straight or change
                        lanes to the right, but you are prohibited from crossing the solid white line to the
                        left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 8281, out 920, 14.93 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road under an elevated highway structure,
                        heading towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right | roles: the white
                        dashed pattern fits the role of a crossable lane line | markings: no markings were
                        observed in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 817, 15.96 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a bridge or overpass with a city
                        skyline in the distance. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line next to the car, which continues ahead. Photo 2
                        confirms a yellow broken line with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego_lane_index
                        (2) agree with the boundaries: a center line on the left and a lane line on the right
                        indicate the car is in the rightmost lane of a two-lane road. | roles: the yellow
                        dashed line on the left fits the role of a crossable center line; the white dashed
                        line on the right fits the role of a crossable lane line. | markings: no markings are
                        present in the lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The crossable centre line allows vehicles to cross to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The crossable lane line allows vehicles to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the yellow broken center line
                        [CN-5.1.1].
Step 6  change_right    allowed (correct): allowed by the white broken lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action.
Step 6  u_turn          allowed: allowed by the yellow broken center line [CN-5.1.1].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight, change lanes to the left, or
                        perform a U-turn across the center line if safe.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 8281, out 860, 13.79 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a single solid yellow
                        line next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 confirms a single solid yellow
                        line next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows large white Chinese characters '公交' painted in the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The presence of yellow center lines on
                        both sides indicates the car is in a special lane (likely a bus lane) separating
                        opposing traffic flows or acting as a dedicated lane. | roles: Yellow solid lines as
                        center lines are consistent with separating opposing traffic or marking special lanes.
                        | markings: The '公交' (bus) text identifies this as a bus lane, which is consistent
                        with the yellow boundaries often used for such dedicated lanes in certain urban
                        configurations. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the bus lane. [[CN-6.9.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow left boundary
                        [CN-6.1.4].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow right boundary
                        [CN-6.1.4].
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits continuing straight,
                        although the lane is reserved for buses [CN-6.9.1].
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane ('公交'). As an ordinary car, you should not be in this
                        lane and are prohibited from crossing the solid yellow boundaries to leave it here;
                        you should have entered the correct lane before this section.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8281, out 958, 62.77 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, approaching an intersection or a road junction.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which marks the edge of the roadway.
                        Photo 2 shows the same solid yellow line next to my car, with a raised curb/planting
                        strip immediately to its right.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a crossable lane line; the yellow solid
                        line fits the role of a left-hand edge line for opposing traffic or a specific road
                        boundary, but here it is on the right, which is unusual for a standard edge line but
                        consistent with the visual evidence of a curb. | markings: No markings are present in
                        the lane to contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid yellow
                        line to the right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8281, out 872, 15.68 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection or overpass
                        area. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a single
                        solid white line immediately to the left of the car, running along the edge of the
                        roadway.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 and Photo 2 show yellow dashed lines running
                        longitudinally in the center of the lane, but these are not across the lane; they
                        appear to be part of a special lane marking (tidal lane) given the sign above.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the left boundary being an edge line and the right boundary being a lane
                        line. | roles: The white solid left edge line and white broken right lane line fit
                        their roles. | markings: The yellow longitudinal dashes in the lane, combined with the
                        overhead sign '17:00-19:00 工作日', indicate this is a tidal lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            symbol:other: Within a tidal lane, vehicles are prohibited from turning left or making
                        a U-turn except in special cases. [CN-5.3.1-2] "The tidal lane line marks a tidal
                        (reversible) lane and is placed on both sides of it. Within a tidal lane on a road
                        section, vehicles are prohibited from turni"
Step 6  change_left     prohibited (contested, correct): prohibited by the solid left boundary (CN-4.2.2-a).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken right boundary (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it.
Step 6  turn_left       prohibited: prohibited because the lane is a tidal lane (CN-5.3.1-2).
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action.
Step 6  u_turn          prohibited: prohibited because the lane is a tidal lane (CN-5.3.1-2).
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a tidal lane; you may go straight or change to the right lane, but you are
                        prohibited from turning left or making a U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe ['change_right'], citation
                        accepted, contradictions ['turn_left, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 8281, out 991, 17.14 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead under a
                        pedestrian overpass. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow broken line separating my lane from opposing traffic. Photo 2
                        confirms this is a broken yellow line next to my car, with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right. Photo 2 shows a white solid line next
                        to my car, and further ahead it remains solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a center line on the left and an edge line on the right indicate
                        my lane is the leftmost (and only) lane of my direction in this section. | roles: the
                        yellow dashed line fits the role of a crossable center line, and the white solid line
                        fits the role of a road edge line. | markings: no markings are present in my lane. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable centre line allows vehicles to cross to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken yellow center line [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          allowed: allowed by the broken yellow center line [CN-5.1.1].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight, make a U-turn, or cross into the
                        opposing lane to overtake if safe, but you must not cross the solid white line to the
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8281, out 863, 14.45 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a channelized
                        right-turn area. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to the car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line that separates the lane from a non-motorized
                        lane/shoulder. Photo 2 shows this solid white line next to the car, continuing
                        straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 shows a channelized area with diagonal white lines
                        (chevrons) to the right of the lane, separating the main road from a right-turn slip
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: The channelizing area is
                        to the right of the lane, consistent with the right boundary being an edge line. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            area:channelizing: Vehicles may not drive on or across the channelizing lines.
                        [[CN-6.6.1-3]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed: the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: the right boundary is a solid
                        white line [CN-4.2.2-a] and is further reinforced by the channelizing area
                        [CN-6.6.1-3].
Step 6  go_straight     allowed (contested, correct): allowed: no marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
                        governs this.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
                        governs this.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane
                        governs this.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line to the right or enter the channelized area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8281, out 1031, 16.37 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road under an overpass, heading straight
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, which continues ahead. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right (though
                        usually, the rightmost lane has the edge line, here I am in the middle lane of 3, but
                        the right boundary is a solid white line which could be a lane line or edge line;
                        looking closer at Photo 1, there is another lane to my right, making me lane 2 of 3.
                        Wait, looking at Photo 1, there are 3 lanes. My car is in the middle one. The line to
                        my right is a broken white line further ahead, but Photo 2 shows it as solid. Let me
                        re-examine. In Photo 1, the line to my right is broken. In Photo 2, it looks solid.
                        According to the rules, Photo 2 decides next to my car. However, looking at the
                        overall scene in Photo 1, there is a lane to my right. The line is a lane line. Let me
                        correct: the right boundary is a broken white line in Photo 1, and Photo 2 shows it as
                        a solid white line. I will follow the rule: Photo 2 decides next to my car, Photo 1
                        decides further ahead. It is a broken-solid white line or a line that changes.
                        Actually, looking at Photo 2 again, it is a solid white line. Looking at Photo 1, it
                        is a broken white line. I will mark it as solid based on Photo 2 for the immediate
                        area and note the change if applicable. But wait, the rightmost lane is separated by a
                        white line. If I am in lane 2, the line to my right is a lane line. If I am in lane 3,
                        it is an edge line. Looking at Photo 1, there is a car in the lane to my right. So I
                        am in lane 2. The line to my right is a lane line. | roles: The left boundary is a
                        white broken lane line, which fits the role of separating lanes in the same direction.
                        The right boundary is a white solid line, which fits the role of a no-crossing lane
                        line or edge line. | markings: No markings in my lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white lane line prohibits me from crossing it. [CN-6.2.1]
                        "The no-crossing lane line separates vehicles travelling in the same direction and
                        prohibits vehicles on the solid-line side from crossing. It has two forms: sin"
Step 6  change_left     allowed (WRONG, label not_determined): allowed because the left boundary is a broken
                        white line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white line
                        [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  You can stay in your lane or change to the left lane, but do not cross the solid line
                        to the right. Follow the overhead speed limit signs for your lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 1230, 23.79 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road. The road continues straight ahead
                        with no immediate intersection or ramp visible. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line marking the right edge of the roadway, followed by a
                        shoulder and a curb. Photo 2 shows the white solid line next to my car and the
                        adjacent curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right.
                        | roles: The white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: No markings are
                        present in my lane, which is consistent with the boundaries. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which allows
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight, and the
                        boundaries do not govern this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 892, 15.17 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a raised curb. Photo 2
                        confirms a solid white line immediately to the right of my car, adjacent to a concrete
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane. Photo 1
                        shows a second straight-ahead arrow further ahead, closer to the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 3 agree with having a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: the straight-ahead arrows
                        agree with the lane's position and boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing to the right is normally
                        prohibited. [[CN-4.2.2-a]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the lane is for traveling
                        straight. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white line
                        [CN-4.2.2-a] and there is a curb.
Step 6  go_straight     allowed (correct): allowed because the lane marking is a straight-ahead arrow
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left, you must change to the
                        left lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 8281, out 1036, 18.87 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test B | no answer
-----------------------------------------------------------------------------------------------------
Error                   Cannot reach Ollama at http://127.0.0.1:11434 (timed out). Is Ollama running?

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane; Photo 1 shows it as well.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        The straight-ahead arrow is consistent with the lane's position and boundaries. |
                        unseen: no | result: consistent
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
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. If you need to
                        turn left or right, you must change to the corresponding outer lanes.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 948, 17.42 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane. Photo 1 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: The straight-ahead arrow is consistent with the lane's position
                        as a through lane. | unseen: no | result: consistent
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
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, change to the
                        corresponding outer lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 8281, out 950, 16.34 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a solid white line extending from the bottom towards the intersection.
                        Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line extending from the bottom towards the intersection.
                        Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows the top part of a white guide arrow pointing
                        straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White solid lines
                        between lanes of the same direction fit the role of no-crossing lane lines on an
                        intersection approach. | markings: The straight arrow is consistent with the lane's
                        position and boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white lane line is prohibited. [CN-6.2.1] "The no-
                        crossing lane line separates vehicles travelling in the same direction and prohibits
                        vehicles on the solid-line side from crossing. It has two forms: sin"
Step 5  Rule            right_boundary: Crossing the solid white lane line is prohibited. [CN-6.2.1] "The no-
                        crossing lane line separates vehicles travelling in the same direction and prohibits
                        vehicles on the solid-line side from crossing. It has two forms: sin"
Step 5  Rule            arrow:straight: The lane is designated for traveling straight ahead. [CN-5.13.1]
                        "Guide arrows indicate the direction of travel for vehicles. (Table 1 meanings:
                        straight ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): prohibited by the solid white line (CN-6.2.1)
Step 6  change_right    prohibited (correct): prohibited by the solid white line (CN-6.2.1)
Step 6  go_straight     allowed (correct): allowed by the straight guide arrow (CN-5.13.1)
Step 6  turn_left       prohibited (correct): prohibited by the straight guide arrow (CN-5.13.1)
Step 6  turn_right      prohibited (correct): prohibited by the straight guide arrow (CN-5.13.1)
Step 6  u_turn          prohibited (correct): prohibited by the straight guide arrow (CN-5.13.1)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight through the intersection; lane changes
                        are prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 891, 14.45 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, which continues ahead. Photo 2
                        confirms a single solid yellow line immediately to the left of the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which becomes a solid white line
                        further ahead. Photo 2 shows a broken white line with several dashes and gaps
                        immediately to the right of the car.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white arrow pointing straight and left.
                        Photo 1 shows the same arrow further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being a center_line and the right boundary being a
                        lane_line. | roles: The yellow solid left boundary fits the role of a no-crossing
                        center_line. The white broken-to-solid right boundary fits the role of a lane_line
                        that becomes a guide lane line. | markings: The straight-left arrow is consistent with
                        the lane's position as the leftmost lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: On a broken-solid white line, vehicles on the broken side may cross,
                        while those on the solid side may not. [[CN-6.2.3]]
Step 5  Rule            arrow:straight_left: The guide arrow indicates that the lane is for going straight or
                        turning left. [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line next to the
                        car [CN-6.2.3]
Step 6  go_straight     allowed (correct): allowed by the guide arrow [CN-5.13.1]
Step 6  turn_left       allowed (correct): allowed by the guide arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the guide arrow which only shows straight and left
                        [CN-5.13.1]
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable as no arrow or prohibition
                        governs it
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or turn left. You may change to the
                        right lane, but do not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8281, out 998, 16.11 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a yellow solid line on the left, which is the edge of the roadway. Photo
                        2 confirms a single yellow solid line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the right lane. Photo 2
                        shows a white broken line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The yellow edge line on the left
                        indicates my lane is the leftmost lane of my direction, which agrees with
                        ego_lane_index 1. | roles: The yellow solid line on the left fits the role of a left
                        edge line; the white broken line on the right fits the role of a crossable lane line.
                        | markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles from crossing it.
                        [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8281, out 819, 14.25 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an underpass beneath the Dashan
                        Bridge. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which becomes a solid white line
                        further ahead. Photo 2 shows a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight and right.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        correctly serve as lane lines separating traffic in the same direction. | markings:
                        The straight-right arrow is consistent with a through lane that also allows a right
                        turn. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            arrow:straight_right: The guide arrow indicates that my car may go straight or turn
                        right. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed: allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed: allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed by the straight-right arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-right arrow (CN-5.13.1), which does
                        not show a left turn.
Step 6  turn_right      allowed (correct): allowed by the straight-right arrow (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited by the straight-right arrow (CN-5.13.1), which does
                        not show a U-turn.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn right. You may also change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:right']), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8281, out 956, 13.89 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid white line next to a white fence. Photo 2 confirms a single
                        solid white line immediately to the left of my lane, with a raised curb and fence
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the one to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        lane 1 agree with the left boundary being an edge line and the right boundary being a
                        lane line. | roles: The white solid left boundary fits the role of an edge line
                        (motor/non-motor separation), and the white broken right boundary fits the role of a
                        crossable lane line. | markings: No markings were observed in my lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The white edge line marks the boundary between motor vehicle lanes and
                        non-motorized lanes. [CN-5.4.3] "An edge line on the right side of the direction of
                        travel shall be white, and an edge line on the left side of the direction of travel
                        shall be yellow; a motor/"
Step 5  Rule            right_boundary: The broken white lane line separates traffic flows in the same
                        direction and may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid line and a physical
                        curb/fence, and crossing is normally prohibited per CN-4.2.2-a.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which may be
                        crossed per CN-5.2.1-2.
Step 6  go_straight     allowed (correct): allowed: no marking restricts carrying on straight along my lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: no arrow or waiting area
                        governs this action.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: no arrow or waiting area
                        governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: no arrow governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot move left due to the curb and fence.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8281, out 884, 14.37 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left, bordering a fence. Photo 2 confirms a
                        single solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the right lane. Photo 2 shows this
                        line is a broken white line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.;
                        line:stop_line (full): Photo 1 and Photo 2 show a solid white stop line across the
                        lane ahead of the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a center line; the white
                        broken line on the right fits the role of a lane line. | markings: The straight arrow
                        and stop line are consistent with a through lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. You are in a through lane and
                        should proceed straight through the intersection, stopping at the stop line if the
                        signal requires it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8281, out 1049, 17.31 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a yellow solid line next to the car, which continues ahead. Photo 2
                        confirms a single yellow solid line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        shows a white broken line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane. Photo 1
                        shows the same arrow.; line:stop_line (full): Photo 1 and Photo 2 show a white solid
                        line across the lane ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being a center_line and the right boundary being a
                        lane_line. | roles: The yellow solid left boundary fits the role of a center_line; the
                        white dashed right boundary fits the role of a lane_line. | markings: The straight
                        arrow and stop line are consistent with a through lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may change to the right lane if needed, but do
                        not cross the yellow line to the left. Stop at the stop line before entering the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions False, unsafe ['change_right'], citation accepted,
                        contradictions []
Tokens                  in 8281, out 1060, 15.27 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, approaching an intersection with a yellow grid
                        marking ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a single solid yellow
                        line next to the car, extending further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 confirms a single solid white
                        line next to the car, extending further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow grid area across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The single lane is bounded by a center
                        line on the left and an edge line on the right, which is consistent with being the
                        only lane of travel in this direction. | roles: Yellow solid on the left as a center
                        line and white solid on the right as an edge line fit the roles. | markings: The grid
                        area is a standard intersection marking and does not contradict the boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop within the yellow grid area ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 912, 15.03 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with multiple lanes. Ahead is a straight stretch of road
                        with no immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a single solid yellow
                        line next to the car, extending further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a white dashed line next to the
                        car, with segments and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 and Photo 2 show a white diamond-shaped symbol painted in
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a no-crossing center line;
                        the white dashed line on the right fits the role of a crossable lane line. | markings:
                        The diamond symbol is informative and does not contradict the boundaries. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            symbol:other: The diamond symbol is not covered by the provided rules but generally
                        indicates a special lane or caution. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8281, out 931, 14.31 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection or a road
                        section with a bus stop/non-motorized lane on the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead. Photo 2 confirms the line next to the car is a white broken line with
                        several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and further ahead, with a raised curb
                        and a red-paved non-motorized lane to its right. Photo 2 confirms the solid white line
                        and the raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white guide arrow pointing straight ahead in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white broken/solid line on the left fits the role of a lane line; the white
                        solid line and curb on the right fit the role of an edge line. | markings: the
                        straight arrow in the rightmost lane is consistent with the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: My car is on the broken side of a broken-solid white line, so it may
                        cross the line to change lanes. [CN-6.2.3] "On a broken-solid white line, vehicles on
                        the solid side may not cross; vehicles on the broken side may cross, and a vehicle
                        crossing the line must give way to "
Step 5  Rule            right_boundary: The white solid edge line marks the right-hand edge of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed: allowed: the left boundary is a broken-solid white line and my car is on the
                        broken side [CN-6.2.3].
Step 6  change_right    prohibited: prohibited: the right boundary is a solid white edge line [CN-4.2.2-a] and
                        there is a raised curb.
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: the guide arrow in my lane indicates
                        straight ahead [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited: the guide arrow in my lane only allows going
                        straight [CN-5.13.1].
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited: the guide arrow in my lane only allows
                        going straight [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited: the guide arrow in my lane only allows going
                        straight [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable: there is no waiting area or two-way left-turn lane
                          in view.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not cross the right boundary into the non-motorized lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation accepted, contradictions []
Tokens                  in 8281, out 1067, 18.37 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a single
                        solid white line immediately to the left of the car, running alongside a concrete
                        barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        shows a broken white line with several long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a white edge line on the left and a white lane line on the
                        right. | roles: The white solid edge line on the left and white broken lane line on
                        the right fit their roles. | markings: No markings were observed in the lane. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     prohibited (WRONG, label not_determined): Prohibited by the solid white edge line and
                        concrete barrier [CN-4.2.2-a].
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot move left due to the barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8281, out 814, 14.3 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with traffic signals
                        ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane. Photo 1
                        shows the same arrow further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right | roles: white dashed
                        lines are consistent with the role of crossable lane lines | markings: the straight-
                        ahead arrow is consistent with the lane boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may proceed straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_left       prohibited: prohibited by the straight-ahead arrow (CN-5.13.1) which restricts
                        movement to straight only
Step 6  turn_right      prohibited: prohibited by the straight-ahead arrow (CN-5.13.1) which restricts
                        movement to straight only
Step 6  u_turn          prohibited: prohibited by the straight-ahead arrow (CN-5.13.1) which restricts
                        movement to straight only
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. If you need to
                        turn, you must change to the corresponding turn lane before the intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 943, 13.79 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: white
                        dashed lines are consistent with the role of crossable lane lines separating traffic
                        in the same direction. | markings: the straight-ahead arrow is consistent with the
                        lane's position and boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may proceed straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. If you need to
                        turn left or right, you must change to the corresponding outer lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation accepted,
                        contradictions []
Tokens                  in 8281, out 949, 15.14 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight toward a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long white dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, marking the edge of the roadway. Photo
                        2 shows this solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right,
                        provided there is another lane to the left. | roles: The white dashed line on the left
                        fits the role of a lane line; the white solid line on the right fits the role of an
                        edge line. | markings: No markings were observed in my lane. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable because there are no guide arrows or waiting areas
                        governing this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no guide arrows governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable because there are no guide arrows governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change to the left lane, but you must not cross
                        the solid white line on your right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 858, 14.01 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, driving straight ahead on a clear
                        stretch of road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 confirms two
                        solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my lane. Photo 2 shows a broken
                        white line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left indicates my lane is the
                        leftmost of my direction | roles: the double solid yellow line fits the role of a
                        center line, and the broken white line fits the role of a lane line | markings: there
                        are no markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the double yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 680, 56.56 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, driving straight ahead towards a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line extending from the foreground into the
                        distance. Photo 2 confirms two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the rightmost lane. Photo 2
                        shows a white broken line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (2)
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: the double solid yellow line fits the role of a no-crossing center line; the
                        broken white line fits the role of a crossable lane line. | markings: no markings are
                        present in the lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (WRONG, label prohibited): allowed as no marking restricts carrying on
                        straight
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable as there is no arrow or waiting
                        area governing this
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the double yellow
                        lines to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left_u_turn', 'arrow:straight']), actions False, unsafe ['go_straight'],
                        citation accepted, contradictions []
Tokens                  in 8281, out 826, 15.2 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards an
                        intersection. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white straight-ahead arrow further ahead in the
                        lane. Photo 2 does not show any markings in the immediate foreground of my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: the white
                        dashed lines fit the role of crossable lane lines separating traffic in the same
                        direction. | markings: the straight-ahead arrow is consistent with the lane boundaries
                        and the general flow of traffic. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle may proceed straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts the movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts the movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts the movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. If you need to
                        turn left or right at the intersection, you must change to the corresponding turn
                        lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 981, 16.17 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues forward. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues forward. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        action.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this action.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 801, 14.31 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows the broken white line
                        next to the car with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: the white dashed
                        lines fit the role of lane lines separating traffic in the same direction | markings:
                        no markings in the lane to contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line next to the car means it may be crossed to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight or change lanes to the left or right.
                        According to the overhead sign, this lane is for going straight.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 824, 16.26 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which remains broken further ahead.
                        Photo 2 confirms a white broken line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows a white broken line
                        with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane. Photo 1 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: white broken lines
                        correctly serve as lane lines separating traffic in the same direction. | markings:
                        the straight-ahead arrow is consistent with the lane's position and boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, change lanes now
                        as the current lane is for straight-through traffic only.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 8281, out 965, 15.91 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a yellow solid line on the left. Photo 2 confirms a yellow solid line
                        next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line. Photo 2 shows a white broken line next to the car
                        with several dashes and gaps, continuing ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a center line; the white
                        broken line on the right fits the role of a lane line. | markings: No markings are
                        present in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): Prohibited by the solid yellow center line
                        [CN-6.1.4].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          prohibited: Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 8281, out 817, 12.24 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a single white solid line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a single white solid line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries; both sides are edge lines, meaning this is a single-lane road. |
                        roles: White solid lines on both sides are consistent with edge lines on a single-lane
                        two-way road or a dedicated lane. | markings: No markings are present in the lane. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow, but on a single-lane two-way road, the edge lines on both sides shall be
                        white. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white line, and
                        crossing a solid line is normally prohibited per [CN-4.2.2-a].
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary is a solid white line,
                        and crossing a solid line is normally prohibited per [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to carrying on straight.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight toward the intersection. Lane changes are
                        prohibited by the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 853, 13.0 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway approaching an exit ramp to the right. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car that becomes a solid white line
                        further ahead as it guides into an exit. Photo 2 shows a broken white line with dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right | roles: the white
                        dashed lines fit the role of lane lines separating traffic in the same direction |
                        markings: no markings are present in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the broken white lane line
                        (CN-5.2.1-2)
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the left or right. If you intend to take
                        the exit indicated by the overhead sign, you should move to the rightmost lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8281, out 814, 13.43 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight. There are no
                        intersections or ramps immediately ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having a lane line on both the left and right. |
                        roles: The white dashed lines on both sides correctly fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        my lane, which is consistent with the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
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
Tokens                  in 8281, out 852, 14.02 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight ahead. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 confirms a single solid yellow
                        line next to my car, extending forward.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows the white characters '公交' (bus) painted vertically in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a crossable lane line; the yellow solid
                        line fits the role of a left-hand edge line for opposing traffic or a right-hand edge
                        line for a special lane. | markings: The '公交' text indicates this is a bus lane, which
                        is consistent with the yellow boundary on the right marking the edge of the motor
                        vehicle roadway or a special lane boundary. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing to the right is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the bus lane. [[CN-6.9.1]]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, label prohibited): allowed as no marking prohibits continuing
                        straight, but I am currently in a reserved lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently driving in a bus lane ('公交'). Since you are an ordinary car, you
                        should change left into the general traffic lane as soon as possible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 979, 17.67 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or urban expressway. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        sides. | roles: The white dashed lines on both sides correctly fit the role of lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        my lane, which is consistent with a standard through-lane on a highway. | unseen: No
                        attributes were reported that were not visible. | result: consistent
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
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 865, 16.64 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or urban expressway. The road ahead is
                        straight with no immediate intersections or ramps visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line next to my car with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to my car with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        sides. | roles: The white dashed lines on both sides correctly fit the role of
                        crossable lane lines separating traffic in the same direction. | markings: There are
                        no markings in my lane, which is consistent with a standard through-lane on a highway.
                        | unseen: No attributes were reported that were not visible. | result: consistent
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
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersections in view.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersections in view.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersections in view.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 859, 16.22 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, moving straight ahead on a clear
                        road. (lanes 3, mine 2, full)
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
                        my lane, which is consistent with a standard highway through-lane. | unseen: No |
                        result: consistent
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
                        my lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        my lane.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings
                        in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 865, 13.63 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway, traveling straight ahead
                        towards a slight curve and overhead signs. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 confirms a solid white line next
                        to the car, extending further ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line on the right. Photo 2 shows a broken white line next
                        to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a white edge line on the left and a white lane line on the
                        right. | roles: The white solid line on the left fits the role of an edge line; the
                        white broken line on the right fits the role of a crossable lane line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The white edge line marks the boundary of the motor vehicle lanes.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid line on your left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8281, out 848, 14.75 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or arterial road with a clear sky and trees
                        on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows this solid white line continuing next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with the boundaries: a lane line on the left and an edge line on the right would
                        typically mean the rightmost lane, but here the right boundary is an edge line and the
                        left is a lane line, meaning I am in the rightmost lane of a 3-lane road (if the
                        leftmost is index 1). Wait, if I am in index 2 of 3, there should be a lane to my
                        right. Looking closer at Photo 1, there are 3 lanes total. My lane is the middle one.
                        The boundary to my right is a broken white line, not a solid edge line. Let me re-
                        examine Photo 2. In Photo 2, the line to the right is indeed a broken white line. I
                        correct the right_boundary to dashed white lane_line. | roles: The left boundary is a
                        broken white lane line and the right boundary is a broken white lane line, which fits
                        the role of separating lanes of the same direction. | markings: No markings in lane,
                        consistent with boundaries. | unseen: no | result: corrected right_boundary from solid
                        edge_line to dashed lane_line
Step 5  Rule            left_boundary: The broken white lane line may be crossed for lane changes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 993, 17.53 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line marking the right edge of the roadway, with a metal
                        guardrail beside it. Photo 2 shows the same white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right.
                        | roles: The white dashed line on the left fits the role of a crossable lane line; the
                        white solid line on the right fits the role of a road edge line. | markings: There are
                        no markings in my lane to contradict the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The solid white line marks the right-hand edge of the direction of
                        travel. [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized ve"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement in the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no turn arrows or waiting areas
                        governing this action.
Step 6  turn_right      not_applicable: not_applicable because there are no turn arrows governing this action.
Step 6  u_turn          not_applicable: not_applicable because there are no U-turn arrows governing this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 928, 15.88 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards a slight curve to the left. There are
                        no intersections or ramps immediately ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car that continues forward. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car that continues forward. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a lane line on the left (separating from another lane of
                        the same direction) and an edge line on the right. | roles: The white color and solid
                        pattern fit the roles of a no-crossing lane line and a road edge line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits the car from crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or non-
                        motorized vehicle lanes, or the boundary between motor vehicle lanes and non-motorized
                        ve"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight; lane changes to the left or right are
                        prohibited by the solid lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 8281, out 835, 13.53 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road in China, heading straight toward a distant
                        intersection or road section. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which continues ahead. Photo 2 shows a
                        white solid line next to my car, and a metal guardrail (barrier) immediately to the
                        right of the line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right.
                        | roles: The white dashed line on the left fits the role of a crossable lane line; the
                        white solid line on the right fits the role of a road edge line. | markings: There are
                        no markings in my lane to contradict the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The white solid line on the right marks the edge of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which allows
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line and there is a physical barrier, prohibiting crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings in my lane restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not attempt to move right as there is a solid edge line and a guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 936, 15.51 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, heading straight ahead on a clear
                        day. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: The white dashed lines on both sides correctly fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        my lane, which is consistent with a standard highway through-lane. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        my lane.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings in
                        my lane.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings
                        in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 861, 14.76 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road or highway, moving straight ahead with
                        a sound barrier on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to the car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line next to the car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings are present in the lane, which is consistent with a
                        standard through-lane on a highway. | unseen: No | result: consistent
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
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 843, 13.24 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway with a sound barrier wall on
                        the right side. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail and a
                        sound barrier wall. Photo 2 shows the solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: no markings in my
                        lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 841, 13.29 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road that curves slightly to the left. There
                        are no intersections or ramps immediately ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which is the edge of the roadway,
                        followed by a concrete barrier. Photo 2 shows the same solid white line and the
                        concrete barrier next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: There are no markings in
                        my lane to contradict. | unseen: No attributes were reported that were not visible. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 891, 14.31 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane road, likely a bridge or overpass, with a blue bus
                        ahead in the same lane. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail. Photo 2
                        shows the white solid line next to my car and the guardrail immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a crossable lane line, and the white
                        solid line fits the role of a right-hand edge line. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken white line,
                        which allows crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane to
                        overtake the bus, but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 8281, out 881, 13.39 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test B | no answer
-----------------------------------------------------------------------------------------------------
Error                   Cannot reach Ollama at http://127.0.0.1:11434 (timed out). Is Ollama running?

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a single lane of travel in its direction, heading
                        towards a distant intersection or overpass. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road, separating the lane
                        from a curb and greenery. Photo 2 confirms a solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, separating the lane from a
                        parking/stopping area where vehicles are parked. Photo 2 shows a solid white line next
                        to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left yellow edge line and right white edge line | roles: the yellow left edge
                        line and white right edge line fit the roles of road boundaries in China | markings:
                        no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The white edge line on the right marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow edge line
                        [CN-4.2.2-a]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid boundary lines on
                        either side.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 804, 15.08 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road in China, traveling straight ahead. There is a
                        physical barrier to the left and a curb to the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a concrete barrier separating the road from another roadway. Photo 2
                        shows the same concrete barrier immediately to the left of the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a raised curb. Photo 2 shows the solid white
                        line and the raised curb immediately to the right of the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the boundaries: a barrier on the left and a curb/edge line on the right. | roles:
                        the white solid line on the right fits the role of an edge line. | markings: no
                        markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The concrete barrier marks the edge of the roadway. [CN-5.4.1] "The
                        carriageway edge line marks the edge of motor vehicle lanes or non-motorized vehicle
                        lanes, or the boundary between motor vehicle lanes and non-motorized ve"
Step 5  Rule            right_boundary: The solid white line marks the right-hand edge of the motor vehicle
                        lane. [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized ve"
Step 6  change_left     prohibited (correct): prohibited by the physical concrete barrier (left_boundary).
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        (CN-4.2.2-a) and the raised curb (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection marking governing
                        this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection marking governing
                        this.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection marking governing
                        this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not attempt to cross the barrier on the
                        left or the curb on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 680, 15.83 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no
                        intersections or ramps immediately visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb with a hedge on top, forming the left edge of the road.
                        Photo 2 confirms the presence of a raised concrete curb immediately to the left of the
                        car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being a curb (edge) and the right boundary being a lane
                        line. | roles: The white dashed line on the right fits the role of a crossable lane
                        line. The curb on the left fits the role of a road edge. | markings: No markings were
                        observed in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The curb marks the edge of the motor vehicle lanes. [CN-5.4.1] "The
                        carriageway edge line marks the edge of motor vehicle lanes or non-motorized vehicle
                        lanes, or the boundary between motor vehicle lanes and non-motorized ve"
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited: the left boundary is a raised
                        curb, which physically prevents leaving the lane to the left.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: the right boundary is a broken white
                        line, which allows crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight, and the
                        boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 862, 14.93 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane urban road heading straight. There are no intersections or
                        ramps immediately ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries, as both sides are edge lines. | roles: The white color and solid
                        pattern fit the role of edge lines separating the motor vehicle lane from non-
                        motorized areas. | markings: There are no markings in the lane to contradict. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The left boundary is a solid white line, which prohibits
                        crossing according to [CN-4.2.2-a].
Step 6  change_right    prohibited (correct): The right boundary is a solid white line, which prohibits
                        crossing according to [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 791, 25.66 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a green-colored pavement, approaching a straight
                        section with a pedestrian overpass on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid grey concrete barrier separating the road from another roadway.
                        Photo 2 confirms a continuous raised concrete barrier immediately to the left of the
                        car.
                        none solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2 shows
                        a white broken line with short segments and gaps.
                        white dotted, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left concrete barrier and right edge line | roles: the white dotted line on
                        the right fits the role of a road edge line (motor/non-motor separation) | markings:
                        no markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The physical concrete barrier prohibits crossing to the left. [null]
Step 5  Rule            right_boundary: The broken edge line indicates that crossing to the right may be
                        allowed (e.g., for roadside openings). [[CN-5.4.2]]
Step 6  change_left     prohibited (correct): prohibited by the physical concrete barrier (left_boundary).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white edge line [CN-5.4.2].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane to go straight. Do not attempt to cross the concrete barrier
                        on the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation unlisted, contradictions
                        []
Tokens                  in 8281, out 789, 14.59 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight toward a
                        distant area with trees and buildings. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating the road from a median strip. Photo 2
                        shows the same solid yellow line next to the car.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the edge of the roadway. Photo 2 shows the
                        same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a center line on the left and an edge line on the right. | roles:
                        The yellow solid line on the left fits the role of a center line; the white solid line
                        on the right fits the role of an edge line. | markings: There are no markings in the
                        lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 814, 15.08 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a city road with a single lane in its direction, heading towards
                        a straight stretch of road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a raised curb and hedge. Photo 2 confirms a
                        solid white line and a raised curb immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a non-motorized path. Photo
                        2 shows a solid white line next to the car, with a raised curb further to the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the presence of edge lines on both sides | roles: the white solid lines on both
                        sides fit the role of edge lines separating the motor vehicle lane from the curb/non-
                        motorized path | markings: no markings present in the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb [CN-4.2.2-a]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Lane changes to either side are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 815, 14.6 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road under an overpass on the left, heading
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 confirms a single solid white
                        line next to the car, continuing straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having a lane line on the left and an edge line on the right, implying
                        there is one more lane to the left. | roles: The white dashed line on the left fits
                        the role of a lane line; the white solid line on the right fits the role of an edge
                        line. | markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 897, 14.3 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a road that appears to be a non-motorized vehicle lane or a shared path,
                        given the presence of cyclists and scooters and the surrounding environment. The road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 confirms a solid white line next
                        to the car and continuing ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 confirms a solid white line
                        next to the car and continuing ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the lane. Photo 1
                        also shows this arrow.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: Crossing the solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The arrow indicates that the vehicle should travel straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary (CN-4.2.2-a)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white right boundary
                        (CN-4.2.2-a)
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead. Do not cross the solid white boundaries
                        on either side.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 879, 15.03 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, driving straight ahead. There is a line of traffic
                        ahead, and the road appears to be a single lane in this direction. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line on the left, separating the road from a median area
                        with bushes. Photo 2 shows the same solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, separating the lane from a
                        parking/sidewalk area. Photo 2 shows the same solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center line on the left and edge line on the right | roles: the yellow solid
                        line on the left fits the role of a no-crossing center line; the white solid line on
                        the right fits the role of a road edge line | markings: no markings in the lane to
                        contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and the
                        presence of a curb [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the left yellow line or the right
                        white edge line.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 8281, out 846, 17.23 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no immediate
                        intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left, separating the road from a non-
                        motorized lane or shoulder. Photo 2 confirms a single solid yellow line immediately to
                        the left of the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left indicates the leftmost motor
                        vehicle lane, and a white lane line on the right indicates another lane of the same
                        direction. | roles: The yellow solid line on the left fits the role of a left-hand
                        edge line. The white broken line on the right fits the role of a crossable lane line.
                        | markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the boundary of the motor
                        vehicle roadway. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow line, and
                        according to [CN-4.2.2-a], crossing a solid line is normally prohibited.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: the right boundary is a broken white line,
                        which [CN-5.2.1-2] and [CN-4.2.2-a] permit crossing.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions False, unsafe ['change_right'], citation accepted,
                        contradictions []
Tokens                  in 8281, out 914, 16.85 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, driving straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a metal fence. Photo 2 confirms a single
                        solid yellow line immediately to the left of the car, running along the fence.
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
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 844, 14.67 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white fence and a solid white line separating the road from the fence.
                        Photo 2 confirms a solid white line next to the car, which continues as a solid white
                        line further ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a broken white line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a white edge line on the left and a white lane line on the
                        right. | roles: The white solid edge line on the left and white dashed lane line on
                        the right fit their respective roles. | markings: No markings are present in the lane,
                        which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid white edge line, and
                        rule [CN-4.2.2-a] prohibits crossing it.
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white lane line, and
                        rule [CN-5.2.1-2] allows crossing it.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8281, out 847, 12.69 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings and trees on both sides, driving
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a single yellow line extending from the bottom towards the horizon.
                        Photo 2 shows this line is a broken yellow line next to the car.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right edge of the road. Photo 2 shows this line is a
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right | roles: the yellow
                        dashed line fits the role of a crossable center line, and the white solid line fits
                        the role of a road edge line | markings: no markings in lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: Crossing the solid white line is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken yellow center line [CN-5.1.1]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a single lane of your direction. You may change left across the center line
                        to overtake if safe, but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 812, 58.57 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with multiple lanes in its direction, approaching a straight
                        stretch with buildings and trees on the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from another lane to the left.
                        Photo 2 shows the same white broken line next to my car, consisting of several long
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which continues ahead. Photo 2 shows a
                        white solid line next to my car, and further ahead it remains a single solid white
                        line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 1 agree with the left boundary being a lane line and the right boundary being an
                        edge line. | roles: The white dashed line on the left fits the role of a crossable
                        lane line, and the white solid line on the right fits the role of a road edge line. |
                        markings: There are no markings in my lane to contradict. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white edge line marks the edge of the motor vehicle lane.
                        [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or non-
                        motorized vehicle lanes, or the boundary between motor vehicle lanes and non-motorized
                        ve"
Step 5  Rule            right_boundary: The solid line means crossing to the right is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 8281, out 911, 16.29 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings and trees on both sides, heading towards a
                        distant intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line on the left that is broken. Photo 2 shows the line next to
                        the car is a broken yellow line with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a solid white line next to the
                        car, and there is a raised curb immediately to the right of this line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right | roles: the yellow
                        dashed line fits the role of a crossable center line, and the white solid line with a
                        curb fits the role of a road edge line | markings: no markings in lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The crossable centre line allows vehicles to cross to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken yellow center line [CN-5.1.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may go straight or change left across the center line if
                        safe, but do not cross the right edge line into the curb/sidewalk.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 834, 15.03 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues straight ahead. Photo
                        2 confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues straight ahead. Photo
                        2 confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no guide arrows or waiting areas in the
                        lane.
Step 6  turn_right      not_applicable: Not applicable as there are no guide arrows or waiting areas in the
                        lane.
Step 6  u_turn          not_applicable: Not applicable as there are no guide arrows in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 819, 15.76 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection with a crosswalk ahead. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car that continues ahead. Photo 2
                        confirms a single solid white line immediately to the left of the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and a raised curb further right.
                        Photo 2 shows a single solid white line immediately to the right of the car, with a
                        yellow-painted curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight and right.
                        Photo 1 shows the same arrow.; line:crosswalk (full): Photo 1 and Photo 2 show a white
                        zebra-stripe crosswalk across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and index 1 agree
                        with the boundaries: a lane line on the left (separating from another lane of the same
                        direction) and an edge line on the right. | roles: The white solid lines fit the roles
                        of lane line and edge line respectively. | markings: The straight-right arrow is
                        consistent with the lane's position as a rightmost lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the solid line is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: Crossing the solid line is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            arrow:straight_right: The lane allows traveling straight ahead or turning right.
                        [[CN-5.13.1]]
Step 5  Rule            line:crosswalk: The crosswalk is an informative marking for pedestrian crossing and
                        does not govern the seven actions. [null]
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white lane line
                        [CN-4.2.2-a]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line
                        [CN-4.2.2-a] and the curb
Step 6  go_straight     allowed (correct): allowed by the straight-right arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight-right arrow [CN-5.13.1] which does
                        not show left
Step 6  turn_right      allowed (correct): allowed by the straight-right arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-right arrow [CN-5.13.1] which does
                        not show U-turn
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn right. Lane changes are
                        prohibited; stay in your lane and yield to pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 8281, out 1077, 17.1 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road. The road continues straight ahead
                        under an overpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line next to my
                        car is a solid yellow line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line next to my
                        car is a broken white line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a center line on the left means my lane is the leftmost of the
                        motor vehicle lanes in my direction, but the lane count is 3, and I am in the middle
                        lane. Wait, looking closer at Photo 1, there is another lane to my left separated by a
                        white line, and the yellow line is further left. Let me re-evaluate. In Photo 2, the
                        line immediately to my left is yellow and solid. This means my lane is the leftmost
                        lane of my direction. The lane count is 3 lanes total for my direction. My lane is
                        index 1. | roles: the yellow solid line on the left fits the role of a center line;
                        the white broken line on the right fits the role of a lane line. | markings: no
                        markings in my lane | unseen: no | result: corrected ego_lane_index to 1
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 923, 15.46 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road, approaching an underpass. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, continuing ahead, with a concrete
                        wall/barrier beyond it. Photo 2 confirms the solid white line and the adjacent
                        concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having a lane line on the left and an edge line on the right. | roles: The
                        white dashed line on the left fits the role of a crossable lane line; the white solid
                        line on the right fits the role of a road edge line. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The solid white line marks the right-hand edge of the direction of
                        travel. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which allows
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid edge line
                        and there is a physical barrier, prohibiting crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not attempt to move right as
                        it is the edge of the roadway bounded by a wall.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 857, 14.23 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight toward a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line and a raised curb further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (2)
                        agree with the boundaries: a lane line on the left and an edge line on the right
                        indicate the car is in the rightmost motor vehicle lane of a three-lane road (though
                        the leftmost lane is partially obscured by other cars, the boundaries of the ego lane
                        are clear). | roles: the white dashed line on the left fits the role of a lane line;
                        the white solid line on the right fits the role of an edge line. | markings: no
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the boundary between the motor vehicle
                        lane and the non-motorized lane/curb. [[CN-5.4.1]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 959, 60.5 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a single-lane road that appears to be a service road or a small
                        access road, with a red wall on the right and bushes on the left. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a curb and a line of bushes on the left. Photo 2 shows a raised concrete
                        curb separating the road from the bushes.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a raised concrete curb and a red wall on the right. Photo 2 confirms a
                        raised concrete curb separating the road from a sidewalk and the wall.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the presence of curbs on both sides | roles: the curbs correctly serve as edge
                        lines for a single-lane road | markings: no markings are present, which is consistent
                        with a simple access road | unseen: no | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the motor vehicle lane. [CN-5.4.1] "The
                        carriageway edge line marks the edge of motor vehicle lanes or non-motorized vehicle
                        lanes, or the boundary between motor vehicle lanes and non-motorized ve"
Step 5  Rule            right_boundary: The curb marks the edge of the motor vehicle lane. [CN-5.4.1] "The
                        carriageway edge line marks the edge of motor vehicle lanes or non-motorized vehicle
                        lanes, or the boundary between motor vehicle lanes and non-motorized ve"
Step 6  change_left     prohibited (correct): prohibited by the physical curb (left_boundary)
Step 6  change_right    prohibited (correct): prohibited by the physical curb (right_boundary)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in the current lane and follow the vehicle ahead; lane changes are impossible due
                        to the curbs on both sides.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 791, 15.18 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and a physical metal fence/barrier.
                        Photo 2 shows a solid white line and a raised curb with a metal fence.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 2 shows a white right-turn arrow in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the right boundary being an edge line and the left boundary being a lane
                        line. | roles: the white color and patterns fit the roles of a lane line on the left
                        and an edge line on the right. | markings: the right-turn arrow is consistent with the
                        lane being the rightmost lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: My car is on the broken side of a broken-solid white line, so it may
                        cross the line to change lanes. [CN-6.2.3] "On a broken-solid white line, vehicles on
                        the solid side may not cross; vehicles on the broken side may cross, and a vehicle
                        crossing the line must give way to "
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:right: The right-turn arrow indicates that the lane is for turning right.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken line
                        next to my car (CN-6.2.3).
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid line and there
                        is a physical barrier (CN-4.2.2-a).
Step 6  go_straight     prohibited (correct): prohibited because the lane has a right-turn arrow which
                        restricts movement to right turns only (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited because the lane has a right-turn arrow (CN-5.13.1).
Step 6  turn_right      allowed (correct): allowed because the lane has a right-turn arrow (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited because the lane has a right-turn arrow (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a right-turn only lane. If you intend to go straight or turn left, you must
                        change to the left lane now while the boundary is still broken.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 8281, out 993, 16.1 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or arterial road under a bridge overpass,
                        with a clear road ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line marking the left edge of the roadway, next to a
                        physical barrier. Photo 2 confirms a solid yellow line immediately to the left of the
                        car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The yellow solid left boundary fits the role of a left edge line;
                        the white dashed right boundary fits the role of a crossable lane line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles from crossing it.
                        [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions from
                        crossing. It is generally used on two-lane two-way roads with limited sight distance
                        or wh"
Step 5  Rule            right_boundary: A broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary is a solid yellow line, which
                        prohibits crossing according to CN-6.1.4.
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        according to CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there are no
                        restrictions to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 840, 12.53 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, heading straight on a clear road.
                        (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the one to the left. Photo 2
                        confirms a broken white line next to the car with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a shoulder and a metal
                        guardrail. Photo 2 shows the solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a yellow number '60' inside a blue circle
                        painted on the pavement in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: the speed limit marking
                        is consistent with a highway lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            text:speed_limit: The yellow number indicates the maximum speed limit for this lane.
                        [CN-5.14.2] "Pavement speed limit markings show the speed limit of a lane and are
                        placed at the start of the lane and at other suitable places where the maximum speed
                        is lim"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white edge line
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting it and it
                        is the default movement.
Step 6  turn_left       not_applicable: not_applicable because there are no turn arrows or intersection
                        markings in view.
Step 6  turn_right      not_applicable: not_applicable because there are no turn arrows or intersection
                        markings in view.
Step 6  u_turn          not_applicable: not_applicable because there are no U-turn arrows or intersection
                        markings in view.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right. Observe the 60 km/h speed limit
                        painted in your lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 987, 16.27 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead on a clear
                        stretch of road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms a broken white line next to my car with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 confirms a broken white line next to my car with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        sides. | roles: the white dashed lines on both sides fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: there are no markings in
                        my lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 834, 13.8 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or arterial road. The road ahead is a
                        straight stretch with no immediate intersections or ramps visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line to the left of my car. Photo 2 confirms this is a
                        broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car. Photo 2 confirms this is a
                        broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having a lane line on both the left and right. | roles: The white dashed
                        lines correctly fit the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in the lane, which is consistent with a
                        standard through-lane on a highway. | unseen: No attributes were reported that were
                        not visible. | result: consistent
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
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 847, 63.77 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or urban arterial road in China, moving
                        straight ahead with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: The white dashed lines on both sides correctly fit the role of lane lines
                        separating traffic in the same direction. | markings: There are no markings in my
                        lane, which is consistent with a standard through-lane on a highway. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 865, 14.96 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway. The road ahead is a
                        straight stretch with no immediate intersections or ramps. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to the car, consisting of long dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a concrete barrier. Photo 2
                        shows the white solid line next to the car and the concrete barrier immediately to its
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line and curb on the right fit the role of an edge line. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which allows
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line and a
                        concrete barrier, which prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move further right due to the solid edge line and barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 878, 15.8 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road passing under an overpass, heading towards an open
                        road section. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow solid line next to a metal guardrail. Photo 2 confirms a single
                        yellow solid line and a raised metal barrier (guardrail) immediately to the left of
                        the lane.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a center line; the white
                        broken line on the right fits the role of a lane line. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): Allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed; do not cross the yellow line
                        to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 838, 14.91 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a physical barrier. Photo 2 confirms a solid
                        yellow line and a metal guardrail barrier immediately to the left of the lane.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the one to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left indicates the leftmost lane
                        of the direction of travel, and a white lane line on the right indicates another lane
                        of the same direction. | roles: The yellow solid line on the left fits the role of a
                        left-hand edge line; the white broken line on the right fits the role of a crossable
                        lane line. | markings: No markings are present in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid yellow left boundary (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white right boundary (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no turn arrows or intersection markings.
Step 6  turn_right      not_applicable: not_applicable as there are no turn arrows or intersection markings.
Step 6  u_turn          not_applicable: not_applicable as there are no U-turn arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right lane if needed. Do not cross the left
                        boundary into the barrier area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 868, 15.58 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, moving straight ahead on a clear
                        road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: The white dashed lines on both sides fit the role of crossable lane lines
                        separating traffic in the same direction. | markings: There are no markings in my
                        lane, which is consistent with a standard highway through-lane. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 847, 15.21 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway. The road ahead is a straight
                        stretch with no immediate intersection or ramp. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a metal guardrail. Photo 2 confirms a single
                        solid white line immediately to the left of the car, running parallel to the
                        guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with several long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of an edge_line
                        (motor/non-motor or road edge), and the white broken right boundary fits the role of a
                        crossable lane_line. | markings: No markings were observed in the lane, which is
                        consistent with a standard highway stretch. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (WRONG, label not_determined): prohibited by the solid white edge_line
                        (CN-4.2.2-a) and the presence of a guardrail.
Step 6  change_right    allowed (correct): allowed by the broken white lane_line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right lane if needed. Do not cross the left
                        boundary as it is a solid line and bordered by a guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 877, 15.79 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, which is the edge of the roadway. Photo
                        2 confirms a single solid white line next to the car, extending further ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to the car with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of an edge_line
                        (though usually yellow for left edges, white is used on single-lane two-way roads or
                        specific highway configurations), and the white broken right boundary fits the role of
                        a lane_line. | markings: No markings are present in the lane, which is consistent with
                        a highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): The left boundary is a solid white line, which prohibits
                        crossing according to [CN-4.2.2-a].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which allows crossing
                        according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there are no
                        restrictions to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right lane if needed. Do not cross the solid
                        white line on the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 861, 9.7 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway in China, moving straight ahead on a clear
                        day. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms this broken white line next to the car, with several visible dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, which continues ahead. Photo 2 shows
                        this solid white line next to the car, and a metal guardrail/barrier running parallel
                        to it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (2)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings are present
                        in my lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 842, 13.5 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms a broken white line next to my car with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to my car with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: The white
                        dashed patterns fit the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No attributes were reported without visual evidence. |
                        result: consistent
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
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 840, 13.37 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, traveling straight ahead on a clear day.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from another lane to the left.
                        Photo 2 shows the same white broken line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail. Photo 2
                        shows the white solid line next to my car and the guardrail immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows large white numbers '100' painted on the road
                        surface in my lane; Photo 1 shows them further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: The speed limit text is a
                        standard informative marking and does not conflict with boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            text:speed_limit: The marking shows the maximum speed limit for the lane.
                        [[CN-5.14.2]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line
                        [CN-4.2.2-a] and there is a physical barrier (guardrail).
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the guardrail. Observe the 100 km/h speed
                        limit painted in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 995, 16.23 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with overhead
                        traffic signals. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line that is solid next to the car and remains solid further
                        ahead. Photo 2 confirms a single solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line that is solid next to the car and remains solid further
                        ahead. Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a center line on the left and an edge line on the right
                        indicate the car is in the rightmost lane of a two-lane road (one direction). | roles:
                        The yellow solid line on the left fits the role of a no-crossing center line. The
                        white solid line on the right fits the role of a road edge line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the boundary between motor vehicle lanes and
                        the road edge. [[CN-5.4.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.1]
                        and the fact that it marks the road edge
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 847, 15.11 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight. The road
                        ahead appears clear with no immediate intersection or ramp. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both my left and right. |
                        roles: the white dashed lines on both sides fit the role of crossable lane lines
                        separating traffic in the same direction. | markings: there are no markings in my
                        lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 855, 11.38 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards a
                        distant intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line next to my
                        car is a broken yellow line with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line next to my
                        car is a solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a yellow center line on the left indicates my lane is
                        the leftmost of my direction, and a white lane line on the right indicates another
                        lane of my direction to the right. | roles: the yellow dashed line fits the role of a
                        crossable center line, and the white solid line fits the role of a no-crossing lane
                        line. | markings: no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: Crossing the solid white lane line is prohibited for vehicles on the
                        solid-line side. [[CN-6.2.1]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken yellow center line
                        [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may change left across the center line if safe, but
                        you are prohibited from changing right into the adjacent lane.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 853, 15.88 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection or a road
                        section with guidance markings. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the lane to the left.
                        Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, bordering a sidewalk/curb area. Photo
                        2 shows a single solid yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2nd
                        from left) agree with the boundaries: a center line on the left and an edge line on
                        the right. | roles: The yellow color and solid patterns fit the roles of a no-crossing
                        center line and a road edge line. | markings: No markings are present in my lane to
                        contradict the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The yellow edge line marks the left-hand edge of the direction of
                        travel or a special boundary; here it marks the right edge of the road, and as a solid
                        line, crossing is normally prohibited per [CN-4.2.2-a]. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings in my lane restrict it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 860, 61.06 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with a bus
                        stop on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which remains broken further ahead.
                        Photo 2 confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which remains broken further ahead.
                        Photo 2 confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with lane lines separating traffic in the same direction | markings: no
                        markings in the lane to contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white lane line
                        (CN-5.2.1-2)
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken white lane line
                        (CN-5.2.1-2)
Step 6  go_straight     allowed (correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right. Be mindful of the traffic signals and the bus stop on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8281, out 804, 15.64 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test B | no answer
-----------------------------------------------------------------------------------------------------
Error                   Cannot reach Ollama at http://127.0.0.1:11434 (timed out). Is Ollama running?

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant intersection or open
                        road section. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 confirms two
                        solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my lane. Photo 2 shows a white line
                        with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (2)
                        agree with the boundaries: a double yellow center line on the left means I am in the
                        leftmost lane of my direction, but the presence of a lane line on the right indicates
                        another lane of my direction exists. Wait, if there is a center line on my left, I am
                        in lane 1. Let me re-evaluate: the double yellow line separates opposing traffic, so
                        my lane is the leftmost. The lane to my right is lane 2. Therefore, my ego_lane_index
                        is 1. | roles: the double solid yellow line fits the role of a no-crossing center
                        line; the broken white line fits the role of a crossable lane line. | markings: no
                        markings in my lane to conflict with boundaries. | unseen: no | result: corrected
                        ego_lane_index to 1
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow center line
                        [CN-6.1.2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the double yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 8281, out 923, 14.0 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right sides | roles: the
                        white dashed lines on both sides fit the role of crossable lane lines separating
                        traffic in the same direction | markings: there are no markings in my lane to
                        contradict the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 823, 25.9 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line next to the car, which continues ahead. Photo 2
                        confirms a yellow broken line with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a yellow center line on the left and a white lane line on the
                        right place the car in the second lane from the left (of the three lanes in this
                        direction). | roles: the yellow dashed line fits the role of a crossable center line,
                        and the white dashed line fits the role of a crossable lane line. | markings: no
                        markings are present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken yellow center line
                        [CN-5.1.1]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          allowed: allowed by the broken yellow center line [CN-5.1.1]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may change lanes to the left or right, or proceed
                        straight. A U-turn is permitted across the center line if safe.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 8281, out 695, 11.43 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with lane_line roles | markings: no markings observed in the lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the broken white lane line
                        (CN-5.2.1-2)
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the broken white lane line
                        (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, label not_determined): allowed as there are no markings
                        restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8281, out 780, 25.09 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead towards a
                        distant intersection with overhead signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line next to my
                        car is a solid yellow line, and further ahead it remains solid yellow.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line next to my
                        car is a broken white line with long dashes and gaps, and further ahead it remains a
                        broken white line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (2)
                        agree with the boundaries: a center line on the left means my lane is the leftmost of
                        the motor vehicle lanes in my direction, but there is a lane to my right, making me
                        the 1st or 2nd. Wait, if the left boundary is a center line, I am the leftmost lane
                        (index 1). Let me re-evaluate: the yellow line is a center line, so there are no lanes
                        of my direction to my left. My lane is index 1. | roles: The yellow solid line fits
                        the role of a no-crossing center line. The white broken line fits the role of a
                        crossable lane line. | markings: No markings in my lane to conflict with boundaries. |
                        unseen: no | result: corrected ego_lane_index to 1
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 926, 17.6 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus stop on the left; the road continues straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a solid yellow line
                        next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 confirms a solid yellow line
                        next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show a yellow grid-like area with
                        diagonal lines on the right side of the lane, but it is not across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The presence of yellow center lines on
                        both sides indicates my lane is a two-way left-turn lane (TWLTL) or a similar special
                        lane separating opposing traffic. | roles: Yellow solid lines on both sides fit the
                        role of center lines for a two-way left-turn lane. | markings: The channelizing area
                        on the right is consistent with the road layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            area:channelizing: Vehicles must follow the set path and may not drive on or across
                        the channelizing lines. [[CN-6.6.1-3]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  go_straight     prohibited (contested, label allowed): prohibited because the car is in a two-way
                        left-turn lane, which is for turning only
Step 6  turn_left       allowed: allowed as this is a two-way left-turn lane
Step 6  turn_right      prohibited: prohibited as this is a two-way left-turn lane
Step 6  u_turn          allowed: allowed as it is a center lane for turning/U-turns [CN-5.1.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a two-way left-turn lane; you may only use this lane to turn left or make a
                        U-turn. Do not drive straight through or change lanes across the solid yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight, turn_left, turn_right, u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8281, out 968, 15.75 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a concrete barrier on the right, heading
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the lane to the left. Photo 2
                        shows this line consists of two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a concrete barrier on the right. Photo 2 confirms a raised concrete
                        barrier immediately to the right of my lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left and a barrier on the right
                        indicate my lane is the rightmost lane of a two-lane road (or a one-way road with a
                        center line). | roles: the double solid yellow line fits the role of a no-crossing
                        center line; the concrete barrier fits the role of a road edge. | markings: no
                        markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The concrete barrier physically prohibits leaving the lane to the
                        right. [null]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the concrete barrier
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 8281, out 811, 13.12 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed and
                        solid lines are consistent with lane lines separating traffic in the same direction. |
                        markings: The straight-ahead arrow is consistent with the lane's position and
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white lane line prohibits vehicles on my side from crossing.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white line [CN-6.2.1].
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1], which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but
                        changing to the right is prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 931, 61.94 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a bridge
                        overhead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white broken/solid
                        lines are consistent with lane_line roles separating traffic in the same direction |
                        markings: the straight-ahead arrow is consistent with the lane's position and
                        boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: My car is on the broken side, so it may cross the line to change left.
                        [CN-6.2.3] "On a broken-solid white line, vehicles on the solid side may not cross;
                        vehicles on the broken side may cross, and a vehicle crossing the line must give way
                        to "
Step 5  Rule            right_boundary: My car is on the broken side, so it may cross the line to change
                        right. [CN-6.2.3] "On a broken-solid white line, vehicles on the solid side may not
                        cross; vehicles on the broken side may cross, and a vehicle crossing the line must
                        give way to "
Step 5  Rule            arrow:straight: The arrow indicates the lane is for traveling straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): allowed by the broken part of the broken-solid white lane line
                        (CN-6.2.3)
Step 6  change_right    allowed (correct): allowed by the broken part of the broken-solid white lane line
                        (CN-6.2.3)
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, change lanes now while the
                        boundary lines are still broken.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 946, 15.09 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        correctly serve as lane lines separating traffic in the same direction. | markings: No
                        markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 8281, out 784, 13.72 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, driving straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms this is a broken white line next to my car, with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right. Photo 2 confirms a solid yellow line
                        next to my car, which continues straight ahead.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a crossable lane line, and the yellow
                        solid line fits the role of a left-hand edge line for opposing traffic or a right-hand
                        edge line for a specific road configuration, but here it marks the right edge of the
                        motor vehicle lanes. | markings: No markings are present in my lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label not_determined): Prohibited by the solid yellow edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  turn_right      not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  u_turn          not_applicable: Not applicable as there are no guide arrows or waiting areas.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight in your current lane or change to the left lane. Do not
                        cross the solid yellow line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 868, 58.64 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a pedestrian
                        crosswalk ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a wide white zebra-striped area across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        dashed lines on both sides fit the role of lane lines separating traffic in the same
                        direction. | markings: the crosswalk is a standard marking across the lane and does
                        not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that crossing it to change lanes
                        is permitted. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line indicates that crossing it to change lanes
                        is permitted. [[CN-5.2.1-2]]
Step 5  Rule            line:crosswalk: The crosswalk is an area for pedestrians and does not govern the seven
                        vehicle actions. [null]
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes. Be mindful of
                        the pedestrian crosswalk and the traffic signal ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8281, out 750, 13.55 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms this is a broken white line next to my car, with several distinct dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to my car, with several distinct dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 2 agree with having lane lines on both the left and right | roles: the white
                        dashed lines correctly fit the role of crossable lane lines | markings: no markings
                        were observed in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 803, 13.62 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        overhead lane-use signs. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that remains broken further ahead.
                        Photo 2 confirms a white broken line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car and further ahead, with a raised curb
                        beside it. Photo 2 confirms a white solid line and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows white Chinese characters '公交专用' (Bus Only) painted
                        vertically in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line and curb on the right fit the role of an edge line. | markings: the '公交专用' text
                        indicates this is a bus lane, which is consistent with the boundaries of a rightmost
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white solid edge line marks the right edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the bus lane. [[CN-6.9.1]]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a] and the
                        physical curb.
Step 6  go_straight     prohibited (contested, label allowed): allowed as no arrow restricts it, but the lane
                        is reserved for buses [CN-6.9.1].
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a reserved bus lane. You should change left into a general-
                        purpose lane immediately.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation accepted,
                        contradictions ['go_straight decided without an arrow or prohibited-movement marking']
Tokens                  in 8281, out 968, 59.27 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows the broken white line
                        next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the lane; Photo 1
                        shows the same arrow and a stop line further ahead.; line:stop_line (full): Photo 1
                        shows a solid white line across the lane at the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        correctly serve as lane lines separating traffic in the same direction. | markings:
                        The straight-ahead arrow is consistent with the lane's position and boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 6  change_left     allowed (WRONG, label prohibited): allowed; the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label prohibited): allowed; the right boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): allowed; the guide arrow allows straight movement [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited; the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited; the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited; the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed
                        before the boundaries become solid near the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation accepted,
                        contradictions []
Tokens                  in 8281, out 1062, 17.15 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. A truck is directly
                        ahead in the same lane. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a solid white line separating my lane from the lane to the left. Photo 2
                        confirms a single solid white line next to the car, extending forward.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb on the right. Photo 2 shows a solid
                        white line immediately next to the car, followed by a concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in the lane.
                        Photo 1 shows the same arrow further ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the right boundary being an edge line and the left boundary being a lane
                        line. | roles: The white solid lines fit the roles of a no-crossing lane line and a
                        road edge line. | markings: The straight-ahead arrow is consistent with the lane's
                        position as a through lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the solid white lane line is prohibited. [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white solid line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 5  Rule            arrow:straight: The arrow indicates that the lane is for traveling straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the raised curb
                        [CN-5.4.1]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 950, 15.33 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings and trees on both sides, heading
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line extending from the bottom towards the distance.
                        Photo 2 confirms a single solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which then ends as the road meets
                        the sidewalk. Photo 2 shows a single white dash and gap next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right | roles: the yellow solid
                        line fits the role of a no-crossing center line; the white dashed line fits the role
                        of a broken edge line | markings: no markings in lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken edge line may be crossed at roadside openings or where
                        parking is allowed. [[CN-5.4.6]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white edge line [CN-5.4.6]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid yellow line to the
                        left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 804, 12.9 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with traffic
                        signals. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and further ahead, with a raised curb
                        and sidewalk to its right. Photo 2 shows a solid white line and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white straight-ahead arrow further ahead in the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with having a lane line on the left and an edge line on the right. | roles: The
                        white broken line on the left fits the role of a crossable lane line; the white solid
                        line on the right fits the role of a road edge line. | markings: The straight-ahead
                        arrow is consistent with the lane's position and boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white solid edge line marks the right-hand edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited because the right boundary is a
                        solid white edge line [CN-4.2.2-a] and there is a raised curb.
Step 6  go_straight     allowed (contested, correct): allowed because the lane marking is a straight-ahead
                        arrow [CN-5.13.1].
Step 6  turn_left       prohibited: prohibited because the lane marking is a straight-ahead arrow, which
                        restricts movement to straight only [CN-5.13.1].
Step 6  turn_right      prohibited: prohibited because the lane marking is a straight-ahead arrow, which
                        restricts movement to straight only [CN-5.13.1].
Step 6  u_turn          prohibited: prohibited because the lane marking is a straight-ahead arrow, which
                        restricts movement to straight only [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left, change to the left lanes
                        before the boundary becomes solid.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions False, unsafe ['change_left'],
                        citation accepted, contradictions []
Tokens                  in 8281, out 1028, 16.14 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a crosswalk and
                        a channelized area to the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car that continues forward. Photo 2
                        confirms a solid white line immediately to the right of my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead guide arrow in my lane.;
                        line:crosswalk (full): Photo 1 and Photo 2 show a white zebra crosswalk across my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: The straight arrow is
                        consistent with the lane's position and the absence of turn-specific markings. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            arrow:straight: The guide arrow indicates that I should travel straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            line:crosswalk: The crosswalk is an informative marking for pedestrian crossing and
                        does not govern the seven actions. [null]
Step 6  change_left     allowed (WRONG, label not_determined): allowed because the left boundary is a broken
                        white line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited because the right boundary is a
                        solid white line [CN-4.2.2-a].
Step 6  go_straight     allowed (correct): allowed because the guide arrow indicates straight ahead
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area in or next to my
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not cross the solid line to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8281, out 1090, 17.28 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings and trees on both sides, driving straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line extending forward. Photo 2 shows a solid yellow line
                        next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line extending forward. Photo 2 shows a solid white line
                        next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and an edge line on the right indicate a single lane for my
                        direction. | roles: the yellow solid line on the left fits the role of a no-crossing
                        center line; the white solid line on the right fits the role of a road edge line. |
                        markings: no markings in the lane to contradict boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the presence of a
                        curb [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 806, 12.5 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a narrow urban road or bridge, flanked by barriers on both
                        sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a concrete barrier and a raised curb on the left. Photo 2 confirms a
                        continuous concrete barrier and raised curb immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a concrete barrier and a raised curb on the right. Photo 2 confirms a
                        continuous concrete barrier and raised curb immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the presence of physical barriers on both sides. | roles: The physical barriers
                        act as the edges of the roadway, fitting the role of edge_line. | markings: No
                        markings are present in the lane, which is consistent with a single-lane road between
                        barriers. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The physical barrier prohibits leaving the lane to the left. [null]
Step 5  Rule            right_boundary: The physical barrier prohibits leaving the lane to the right. [null]
Step 6  change_left     prohibited (correct): prohibited by the physical barrier (left_boundary).
Step 6  change_right    prohibited (correct): prohibited by the physical barrier (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes are impossible due to the
                        physical barriers on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8281, out 781, 12.31 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no
                        intersections or ramps immediately visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms this is a broken white line next to my car, with several visible dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, which separates the motor vehicle lane
                        from a red-colored non-motorized lane. Photo 2 shows this solid white line clearly
                        next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line separating motor and non-motor
                        traffic. | markings: No markings were found in my lane, which is consistent with the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The white solid edge line marks the boundary between motor vehicle
                        lanes and non-motorized lanes. [CN-5.4.3] "An edge line on the right side of the
                        direction of travel shall be white, and an edge line on the left side of the direction
                        of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The solid line means crossing into the non-motorized lane is normally
                        prohibited. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not enter the red non-
                        motorized lane on your right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8281, out 932, 15.47 s
```
