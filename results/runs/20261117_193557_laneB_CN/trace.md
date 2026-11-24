# Reasoning of lane run 20261117_193557_laneB_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. The road
                        appears to be a wide city street with buildings and a fence on the sides. (lanes 3,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a metal fence. Photo 2 confirms a single
                        solid yellow line immediately to the left of the car, running along the fence.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the one to the right. Photo
                        2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the left boundary being an edge_line (yellow solid) and the right boundary
                        being a lane_line (white dashed). | roles: The yellow solid line on the left fits the
                        role of a left-hand edge line. The white dashed line on the right fits the role of a
                        crossable lane line. | markings: There are no markings in my lane to contradict. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: A broken white lane line separates traffic flows in the same direction
                        and may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in
                        the same direction and is placed between lanes of the same direction. It is a broken
                        white line."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid yellow
                        edge line and there is a physical fence, and CN-4.2.2-a prohibits crossing solid
                        lines.
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a broken white
                        lane line which CN-5.2.1-2 allows crossing.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot move left due to the solid edge line and fence.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 911, 13.39 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with a single lane in its direction, heading
                        towards a straight stretch of road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows the same solid yellow
                        line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and position (1)
                        agree with the boundaries: a center line on the left and an edge line on the right. |
                        roles: the yellow solid line on the left fits the role of a no-crossing center line;
                        the white solid line on the right fits the role of a road edge line. | markings: no
                        markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          prohibited: prohibited by the solid yellow center line [CN-6.1.4].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes and U-turns are prohibited due to
                        the solid boundary lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 8458, out 829, 11.21 s

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
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 816, 12.82 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road with an elevated railway structure on
                        the right. The road ahead appears to be a straight stretch with no immediate
                        intersection or ramp. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a raised curb and fence. Photo 2 confirms a
                        single solid white line immediately to the left of the car, bordering a concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of a road edge line
                        (motor/non-motor separation), and the white broken right boundary fits the role of a
                        crossable lane line. | markings: No markings are present in the lane, which is
                        consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white edge line marks the boundary between motor vehicle lanes and
                        non-motorized lanes or the road edge. [CN-5.4.3] "An edge line on the right side of
                        the direction of travel shall be white, and an edge line on the left side of the
                        direction of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The broken white lane line separates traffic flows in the same
                        direction and may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid line and a raised curb,
                        and crossing into a non-motorized area is prohibited by the nature of the edge line.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line, which
                        allows crossing according to CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right;
                        do not cross the left boundary into the non-motorized area.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 909, 41.19 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road with an elevated highway structure on
                        the right. The road ahead is straight with no immediate intersection or ramp. (lanes
                        2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues straight ahead.
                        Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a white edge line on the left and a white lane line on the
                        right. | roles: The white solid line on the left fits the role of an edge line; the
                        white broken line on the right fits the role of a lane line. | markings: No markings
                        are present in the lane, which is consistent with the boundaries. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: The white edge line marks the boundary between motor vehicle lanes and
                        non-motorized lanes or the road edge. [CN-5.4.3] "An edge line on the right side of
                        the direction of travel shall be white, and an edge line on the left side of the
                        direction of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The broken white lane line separates traffic flows in the same
                        direction and may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid white edge line, and
                        crossing it is normally prohibited per CN-4.2.2-a.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line, which may
                        be crossed per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the solid white line on your left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 881, 14.68 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with commercial buildings on the right. The road
                        continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a landscaped median. Photo 2
                        shows the same solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of an edge_line
                        (motor/non-motor or road edge), and the white broken right boundary fits the role of a
                        crossable lane_line. | markings: No markings are present in the lane, which is
                        consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge_line
                        (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white lane_line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 858, 12.46 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection or a
                        road section with changing lane configurations. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white solid line next to the car that continues forward. Photo 2
                        confirms a white solid line immediately to the left of the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a yellow solid line next to the car. Photo 2 shows a yellow solid line
                        immediately to the right of the car.
                        yellow solid, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a white lane line on the left (though here it is the
                        leftmost motor lane) and a yellow center line on the right indicate the car is in the
                        leftmost lane of its direction, but the presence of a white line on the left suggests
                        another lane exists or it is a separation from a non-motorized lane. Looking closer at
                        Photo 1, there is a fence and a non-motorized lane to the left; thus the white line is
                        an edge line. | roles: The yellow line on the right fits the role of a center line.
                        The white line on the left fits the role of an edge line separating motor and non-
                        motorized traffic. | markings: No markings are present in the lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The white edge line on the left separates motor vehicle lanes from non-
                        motorized lanes. [CN-5.4.3] "An edge line on the right side of the direction of travel
                        shall be white, and an edge line on the left side of the direction of travel shall be
                        yellow; a motor/"
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid white edge
                        line, and crossing into a non-motorized lane is generally prohibited by the role of
                        the edge line.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid yellow
                        center line, which prohibits crossing according to [CN-6.1.4].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in the lane restrict going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Lane changes to the left or right are
                        prohibited due to the solid edge and center lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 8458, out 936, 42.02 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road under an elevated highway structure,
                        heading towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: The white dashed
                        lines correctly fit the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 829, 39.66 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test B | gemma4:31b | from cache
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a bridge or overpass with a city
                        skyline in the distance. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line next to the car, which continues ahead. Photo 2
                        confirms a yellow broken line with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (2)
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow dashed line on the left fits the role of a crossable center line;
                        the white dashed line on the right fits the role of a crossable lane line. | markings:
                        No markings are present in the lane to contradict the boundaries. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: The crossable centre line allows vehicles to cross to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The crossable lane line allows vehicles to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the yellow broken center line
                        [CN-5.1.1]
Step 6  change_right    allowed (correct): allowed by the white broken lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          allowed: allowed by the yellow broken center line [CN-5.1.1]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight, change lanes to the left, or
                        perform a U-turn across the center line if safe.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right', 'u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 8458, out 836, 41.08 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a single solid yellow
                        line next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 confirms a single solid white
                        line next to the car and continuing ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows large white Chinese characters '公交' painted in the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a no-crossing center line;
                        the white solid line on the right fits the role of a no-crossing lane line. |
                        markings: The '公交' (bus) text indicates this is a bus lane, which is consistent with
                        the solid boundaries prohibiting entry/exit from other lanes. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A single solid white line prohibits vehicles on the solid-line side
                        from crossing. [[CN-6.2.1]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the bus lane. [[CN-6.9.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): allowed as no marking in the lane restricts going
                        straight, and the car is already in the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane; as an ordinary car, you should not be in this lane.
                        Lane changes are prohibited by the solid lines on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8458, out 958, 40.79 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, approaching an intersection or a road section
                        with a change in lane configuration. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line marking the right edge of the roadway, with a raised
                        curb and greenery beyond it. Photo 2 shows the same solid yellow line and the curb
                        next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line, and the yellow solid line
                        fits the role of an edge line | markings: there are no markings in my lane to
                        contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The yellow solid line marks the edge of the roadway; crossing it is
                        normally prohibited by [CN-4.2.2-a]. [[CN-5.4.3]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but you
                        cannot cross the right boundary into the curb area.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8458, out 716, 11.47 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection or overpass
                        area. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a solid
                        white line immediately to the left of the car, bordering a raised concrete
                        median/barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several visible dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left edge line and white broken right lane line
                        fit their respective roles. | markings: No markings are present in the lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The white solid edge line marks the left edge of the motor vehicle
                        lanes. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid line and
                        there is a physical concrete barrier [CN-4.2.2-a].
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a broken white
                        lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot move left due to the concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 862, 40.03 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead under a
                        pedestrian overpass. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms a broken white line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, next to a metal fence. Photo 2 shows
                        the solid white line continuing straight ahead next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings are present
                        in the lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line on the right marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 847, 40.16 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a channelized
                        island to the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, which continues ahead. Photo 2
                        confirms a single solid yellow line on the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line on the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The single lane is bounded by a yellow
                        center line on the left and a white edge line on the right, which is consistent with
                        being the only lane of travel in this direction at this point. | roles: The yellow
                        solid line on the left acts as a center line separating opposing traffic, and the
                        white solid line on the right acts as the road edge line. | markings: No markings are
                        present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-5.4.3] and the fact
                        that it marks the road edge.
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 832, 39.98 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road under an overpass, heading straight
                        ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which is the edge of the roadway. Photo
                        2 shows a white solid line next to my car, and there is a metal guardrail/barrier
                        immediately to the right of this line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings in my lane to
                        check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
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
                        it.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you must not cross the right edge line into the barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 878, 40.11 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road in China, approaching an area with
                        overhead gantries and a roadside fence on the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway, followed by a
                        green strip and a fence. Photo 2 shows a solid white line immediately to the right of
                        my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right.
                        | roles: The white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The solid white line marks the right-hand edge of the direction of
                        travel. [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or
                        non-motorized vehicle lanes, or the boundary between motor vehicle lanes and non-
                        motorized ve"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which may be
                        crossed according to CN-5.2.1-2.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line, and
                        crossing it is normally prohibited according to CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings in my lane restrict going straight.
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
                        but do not cross the solid white line on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 898, 41.51 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a traffic
                        signal ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead. Photo 2 confirms the line next to the car is a white broken line with
                        several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and further ahead, with a raised curb
                        and a fence beside it. Photo 2 confirms the solid white line and the raised curb
                        immediately to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the lane. Photo 1
                        shows another straight-ahead arrow further ahead near the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the right boundary being an edge_line and the left boundary being a
                        lane_line. | roles: The white broken/solid line on the left fits the role of a
                        lane_line; the white solid line and curb on the right fit the role of an edge_line. |
                        markings: The straight-ahead arrows agree with the lane's position and boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: My car is on the broken side of a broken-solid white line, so it may
                        cross the line to change lanes. [CN-6.2.3] "On a broken-solid white line, vehicles on
                        the solid side may not cross; vehicles on the broken side may cross, and a vehicle
                        crossing the line must give way to "
Step 5  Rule            right_boundary: The white solid edge line marks the right edge of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the vehicle should proceed
                        straight. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken-solid white
                        line and my car is on the broken side [CN-6.2.3].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line
                        [CN-4.2.2-a] and there is a raised curb.
Step 6  go_straight     allowed (correct): allowed: the lane marking is a straight-ahead arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited: the straight-ahead arrow prohibits movements other
                        than straight [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited: the straight-ahead arrow prohibits movements other
                        than straight [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited: the straight-ahead arrow prohibits movements other
                        than straight [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not attempt to move right as there is a curb.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 8458, out 1061, 22.94 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white broken/solid
                        lines are consistent with lane_line roles separating traffic in the same direction |
                        markings: no markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: My car is on the broken side, so it may cross the line to change lanes,
                        giving way to other vehicles. [CN-6.2.3] "On a broken-solid white line, vehicles on
                        the solid side may not cross; vehicles on the broken side may cross, and a vehicle
                        crossing the line must give way to "
Step 5  Rule            right_boundary: My car is on the broken side, so it may cross the line to change
                        lanes, giving way to other vehicles. [CN-6.2.3] "On a broken-solid white line,
                        vehicles on the solid side may not cross; vehicles on the broken side may cross, and a
                        vehicle crossing the line must give way to "
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken part of the solid-dashed
                        white lane line (CN-6.2.3)
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken part of the solid-dashed
                        white lane line (CN-6.2.3)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight or change lanes now, but be aware that
                        the lane lines become solid further ahead, which will prohibit lane changes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 839, 39.41 s

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
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        dashed lines correctly fit the role of lane lines separating traffic in the same
                        direction. | markings: the straight-ahead arrow is consistent with the lane's position
                        and boundaries. | unseen: no | result: consistent
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
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed because the right boundary is a broken white line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed because the lane marking is a straight-ahead arrow
                        (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited because the straight-ahead arrow prohibits other
                        movements (CN-5.13.1).
Step 6  turn_right      prohibited (correct): prohibited because the straight-ahead arrow prohibits other
                        movements (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited because the straight-ahead arrow prohibits other
                        movements (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 955, 41.35 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car that remains broken further ahead.
                        Photo 2 confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that remains broken further ahead.
                        Photo 2 confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane; Photo 1 shows it as well.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        The straight-ahead arrow is consistent with the lane's position as a through lane. |
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
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a broken
                        white line [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): allowed because the lane arrow indicates straight ahead
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the lane arrow only allows straight ahead
                        [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the lane arrow only allows straight ahead
                        [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the lane arrow only allows straight ahead
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, you must change
                        lanes as the current lane is for straight-through traffic only.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 8458, out 957, 15.14 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a broken white line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line extending from the car toward the intersection. Photo
                        2 shows a solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (2)
                        agree with the boundaries: a lane line on the left and a lane line on the right. |
                        roles: the white color and patterns (dashed left, solid right) fit the role of lane
                        lines separating traffic in the same direction. | markings: no markings in the lane to
                        contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white lane line prohibits the car from crossing it.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white line
                        [CN-6.2.1].
Step 6  go_straight     allowed (correct): allowed as there are no markings in the lane restricting it.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable because there is no arrow or
                        waiting area governing this movement.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable because there is no arrow
                        governing this movement.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable because there is no arrow
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane, but you are prohibited from
                        changing to the right lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 8458, out 814, 13.05 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, which continues ahead. Photo 2
                        confirms a single solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which becomes a solid white line
                        further ahead. Photo 2 shows a broken white line next to the car with several dashes
                        and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white arrow pointing straight and left.
                        Photo 1 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego lane position
                        (1) agree with the boundaries: a center line on the left and a lane line on the right.
                        | roles: The yellow solid line on the left fits the role of a no-crossing center line.
                        The white broken-to-solid line on the right fits the role of a lane line that becomes
                        a guide lane line. | markings: The straight-left arrow is consistent with the lane's
                        position as the leftmost lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The broken part may be crossed, but the solid part is normally
                        prohibited from crossing. [[CN-4.2.2-a]]
Step 5  Rule            arrow:straight_left: The arrow allows the vehicle to go straight or turn left.
                        [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label prohibited): allowed next to the car due to the broken white
                        line [CN-4.2.2-a], but prohibited further ahead where it becomes solid [CN-6.10.1-2]
Step 6  go_straight     allowed (correct): allowed by the guide arrow [CN-5.13.1]
Step 6  turn_left       allowed (correct): allowed by the guide arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the guide arrow which only shows straight and left
                        [CN-5.13.1]
Step 6  u_turn          allowed (correct): allowed as the left-turn arrow also permits U-turns unless a no-U-
                        turn marking is present [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight, turn left, or make a U-turn. You
                        may change lanes to the right now, but this will be prohibited as you approach the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8458, out 1026, 15.08 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a white solid line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        shows a white broken line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and position agree; a
                        white edge line on the left indicates the leftmost lane of the direction of travel,
                        and a white lane line on the right indicates another lane to the right. | roles: The
                        white solid line on the left fits the role of an edge line, and the white broken line
                        on the right fits the role of a lane line. | markings: No markings are present in the
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: Crossing a solid line is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): The left boundary is a solid white line, which prohibits
                        crossing according to [CN-4.2.2-a].
Step 6  change_right    allowed (WRONG, label prohibited): The right boundary is a broken white line, which
                        allows crossing according to [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane,
                        but do not cross the solid line to the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8458, out 836, 40.66 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an underpass/bridge area. There is
                        an intersection or road junction ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead. Photo 2 confirms the line next to the car is a white broken line with
                        several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead. Photo 2 confirms the line next to the car is a white broken line with
                        several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight and right
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        correctly serve as lane lines separating traffic in the same direction. | markings:
                        The straight-right arrow is consistent with the lane's position and boundaries. |
                        unseen: no | result: consistent
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
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label prohibited): allowed because the right boundary is a broken
                        white line [CN-5.2.1-2].
Step 6  go_straight     allowed (WRONG, label prohibited): allowed because the guide arrow shows straight
                        ahead [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the guide arrow does not show a left turn
                        [CN-5.13.1].
Step 6  turn_right      allowed (correct): allowed because the guide arrow shows a right turn [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the guide arrow does not show a U-turn
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area in view.
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn right. You may also change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_right'], missed ['arrow:right']), actions False, unsafe
                        ['change_left', 'change_right', 'go_straight'], citation accepted, contradictions []
Tokens                  in 8458, out 993, 42.34 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid white line next to a white fence. Photo 2 confirms a single
                        solid white line immediately to the left of the car, with a raised curb and fence
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of an edge_line
                        (motor/non-motor separation), and the white broken right boundary fits the role of a
                        crossable lane_line. | markings: No markings were observed in the lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid white edge_line (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white lane_line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed as no marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as there is no arrow or
                        waiting area governing this movement.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as there is no arrow or
                        waiting area governing this movement.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as there is no arrow or
                        waiting area governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you cannot cross the left boundary due to the solid line and fence.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 850, 54.26 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, which continues ahead. Photo 2
                        confirms a single solid yellow line on the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows the broken white line
                        next to the car.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane. Photo 1
                        shows the same arrow.; line:stop_line (full): Photo 1 and Photo 2 show a solid white
                        line across the lane ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being a center_line and the right boundary being a
                        lane_line. | roles: The yellow solid line on the left fits the role of a center_line;
                        the white broken/solid line on the right fits the role of a lane_line. | markings: The
                        straight arrow and stop line are consistent with a through lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: On a broken-solid white line, vehicles on the broken side may cross,
                        while the solid side is prohibited from crossing. [[CN-6.2.3]]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line next to the
                        car [CN-6.2.3].
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may change to the right lane if needed, but do
                        not cross the yellow line to the left. Stop at the stop line before entering the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8458, out 1095, 23.23 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a yellow solid line next to the car, which continues ahead. Photo 2
                        confirms a single yellow solid line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which becomes a white solid line
                        further ahead. Photo 2 shows a white broken line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.;
                        line:stop_line (full): Photo 1 and Photo 2 show a white solid stop line across the
                        lane before the crosswalk.; line:crosswalk (full): Photo 1 and Photo 2 show a white
                        zebra crosswalk across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left and
                        white lane line on the right agree that my lane is the leftmost of two lanes in my
                        direction. | roles: The yellow solid line fits the role of a no-crossing center line;
                        the white broken line fits the role of a crossable lane line. | markings: The straight
                        arrow is consistent with the lane's position and the stop line/crosswalk at the
                        intersection. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 5  Rule            line:crosswalk: The crosswalk is an area for pedestrians to cross and does not govern
                        vehicle movements other than yielding. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. You may only proceed straight
                        through the intersection; stop at the stop line for the traffic signal.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation unlisted, contradictions
                        []
Tokens                  in 8458, out 1151, 24.2 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. There is a yellow grid area
                        ahead in the lane. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows the same solid yellow
                        line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:grid (full): Photo 1 and Photo 2 show a yellow grid area across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left and
                        white edge line on the right agree with my lane being the only lane of my direction. |
                        roles: The yellow solid line fits the role of a no-crossing center line; the white
                        solid line fits the role of a road edge line. | markings: The grid area is a standard
                        intersection marking. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 5  Rule            area:grid: The grid marking shows an area where stopping for any reason is prohibited.
                        [[CN-6.8.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line [CN-5.4.3]
                        and the general rule for solid lines [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop within the yellow grid area.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 911, 41.24 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings and trees on both sides, heading towards a
                        distant intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a single solid yellow
                        line next to the car and continuing ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a broken white line next to the
                        car, consisting of several dashes and gaps, continuing ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Photo 1 and Photo 2 show a white diamond-shaped symbol painted in
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line fits the role of a no-crossing center line; the white
                        broken line fits the role of a crossable lane line. | markings: The diamond symbol is
                        informative and does not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            symbol:other: The diamond symbol is a general road marking and does not govern the
                        seven specific actions.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or change to the right lane, but you
                        must not cross the solid yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 922, 40.61 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection or a road
                        section with a bus stop/non-motorized lane on the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and further ahead, with a raised curb
                        and a red-paved non-motorized lane to its right. Photo 2 shows a solid white line next
                        to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white broken/solid line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: the straight arrow
                        in the lane is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: My car is on the broken side of a broken-solid white line, so it may
                        cross the line to change lanes. [CN-6.2.3] "On a broken-solid white line, vehicles on
                        the solid side may not cross; vehicles on the broken side may cross, and a vehicle
                        crossing the line must give way to "
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle should travel straight
                        ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken-solid white
                        line and my car is on the broken side (CN-6.2.3).
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (WRONG, label prohibited): allowed: the lane marking is a straight arrow
                        (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited: the lane marking is a straight arrow, which
                        prohibits turns (CN-5.13.1).
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited: the lane marking is a straight arrow,
                        which prohibits turns (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited: the lane marking is a straight arrow, which
                        prohibits U-turns (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may change to the left lane if needed, but
                        do not enter the non-motorized lane on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['change_left',
                        'go_straight'], citation accepted, contradictions []
Tokens                  in 8458, out 1044, 41.26 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a single
                        solid white line immediately to the left of the car, bordering a concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        shows a broken white line with several long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge line and the right boundary being a lane
                        line. | roles: The white solid edge line on the left and white broken lane line on the
                        right fit their roles. | markings: No markings were found in the lane. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid line and a concrete
                        barrier [CN-4.2.2-a].
Step 6  change_right    allowed (WRONG, label prohibited): allowed: the right boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane;
                        changing left is prohibited by the concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8458, out 826, 39.72 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        traffic signals ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead guide arrow in my lane.
                        Photo 1 shows the same arrow further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: White dashed lines are consistent with the role of crossable lane lines
                        separating traffic in the same direction. | markings: The straight-ahead arrow is
                        consistent with a through lane bounded by lane lines. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle should travel straight
                        ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    allowed (correct): allowed because the right boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (correct): allowed because the guide arrow in my lane indicates straight ahead
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. Do not attempt to
                        turn left or right from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 985, 13.88 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car that remains broken further ahead.
                        Photo 2 confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows a white broken line
                        with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane.
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
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, you must change
                        lanes as the current lane is for straight-through traffic only.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation accepted,
                        contradictions []
Tokens                  in 8458, out 937, 41.21 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long white dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, which continues ahead. Photo 2 shows a
                        solid white line immediately to the right of my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right
                        indicate my lane is the rightmost of the motor vehicle lanes (though the count is 3,
                        the rightmost lane is index 3; however, looking at the image, there are 3 lanes total,
                        and I am in the middle one. Wait, looking closer at Photo 1, there is a lane to my
                        left and a lane to my right. I am in the middle lane. Let me re-evaluate: there is a
                        white dashed line to my left and a white dashed line to my right. No, the rightmost
                        line is solid. So there are 2 lanes in my direction, and I am in the rightmost one.
                        Let me re-count: there is one lane to my left, and I am in the second. The line to my
                        right is a solid white edge line. Thus, lane_count is 2, ego_lane_index is 2.
                        Correcting step 1.) | roles: The white dashed line on the left fits the role of a
                        lane_line. The white solid line on the right fits the role of an edge_line. |
                        markings: No markings in my lane, consistent with boundaries. | unseen: no | result:
                        corrected lane_count to 2 and ego_lane_index to 2
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 1057, 42.96 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 confirms two
                        solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my lane. Photo 2 shows a broken
                        white line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundaries: a center line on the left and a lane line on the right.
                        | roles: the double solid yellow line fits the role of a no-crossing center line; the
                        broken white line fits the role of a crossable lane line. | markings: no markings in
                        my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change to
                        the right lane, but you must not cross the double yellow lines to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 845, 12.64 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards a distant intersection
                        or overpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from a two-way left-turn
                        lane. Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (2)
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: the double solid yellow line fits the role of a no-crossing center line; the
                        broken white line fits the role of a crossable lane line. | markings: no markings are
                        present in my lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow line [CN-6.1.2].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (WRONG, label prohibited): allowed as no marking restricts carrying on
                        straight along the lane.
Step 6  turn_left       not_applicable (WRONG, label allowed): not_applicable as there is no arrow or waiting
                        area governing this movement.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as there is no arrow
                        governing this movement.
Step 6  u_turn          not_applicable (WRONG, label allowed): not_applicable as there is no arrow governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Changing to the left is
                        prohibited by the double solid yellow lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left_u_turn', 'arrow:straight']), actions False, unsafe ['go_straight'],
                        citation accepted, contradictions []
Tokens                  in 8458, out 839, 13.34 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead toward an
                        intersection. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white guide arrow pointing straight
                        ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed lines correctly fit the role of crossable lane lines separating traffic in the
                        same direction | markings: the straight-ahead arrow is consistent with the lane
                        boundaries and the general flow of traffic | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle should travel straight
                        ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed because the right boundary is a broken white line
                        [CN-5.2.1-2]
Step 6  go_straight     allowed (correct): allowed because the guide arrow in the lane indicates straight
                        ahead [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited because the guide arrow only shows straight ahead
                        [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. Lane changes to the left or right are permitted.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 946, 42.39 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There is an
                        overpass to the left and an intersection further ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which remains broken further ahead.
                        Photo 2 confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which remains broken further ahead.
                        Photo 2 confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with the role of crossable lane lines | markings: no markings in the
                        lane to contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 814, 13.26 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right | roles: the white
                        dashed lines correctly fit the role of crossable lane lines | markings: there are no
                        markings in my lane to contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight or change lanes to the left or right.
                        Use the overhead sign to determine which lane is needed for your intended turn at the
                        intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 833, 13.66 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which remains broken further ahead.
                        Photo 2 confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows a white broken line
                        with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane. Photo 1 shows the same arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        correctly serve as lane lines separating traffic in the same direction. | markings:
                        The straight-ahead arrow is consistent with the lane's position and boundaries. |
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
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1).
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead guide arrow (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn left or right, change lanes now
                        as the current lane is restricted to straight-ahead movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 8458, out 944, 12.76 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a yellow solid line on the left edge of the road. Photo 2 shows the same
                        yellow solid line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the next lane. Photo 2 shows
                        a white broken line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the left boundary being a center_line and the right boundary being a
                        lane_line. | roles: The yellow solid line on the left fits the role of a center_line;
                        the white broken line on the right fits the role of a lane_line. | markings: No
                        markings were found in the lane, which is consistent with the boundaries. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight or change to the right lane, but you
                        must not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 824, 53.7 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which is the edge of the roadway. Photo
                        2 shows a solid white line next to my car, and further ahead it remains solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my position (2)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings in my lane to
                        check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but you
                        must not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 839, 39.44 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway approaching an exit ramp to the right. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car that becomes a solid white line
                        further ahead as it guides traffic toward the exit. Photo 2 shows the broken white
                        line next to my car with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right sides | roles: the
                        white dashed lines fit the role of crossable lane lines separating traffic in the same
                        direction | markings: no markings are present in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the left or right. If you intend to take
                        the exit indicated by the overhead sign, you should move to the rightmost lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8458, out 825, 36.76 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road in China, heading straight toward a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms this is a broken white line next to my car, with several clear dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed lines fit the role of crossable lane lines separating traffic in the same
                        direction | markings: no markings are present in the lane, which is consistent with
                        the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 823, 12.28 s

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
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a crossable lane line; the yellow solid
                        line fits the role of a left-hand edge line for opposite traffic or a right-hand edge
                        line for a special lane. Given the '公交' text, this is a bus lane. | markings: The '公交'
                        text identifies this as a bus lane, which is consistent with the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing to the right is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the bus lane. [[CN-6.9.1]]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid line
                        [CN-4.2.2-a].
Step 6  go_straight     prohibited (contested, correct): prohibited: my car is an ordinary car in a bus lane,
                        and [CN-6.9.1] prohibits non-buses from entering/using this lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus lane, which is prohibited for ordinary cars. You should
                        change left into the general traffic lane immediately.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions ['go_straight
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8458, out 989, 14.03 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or urban expressway. The road ahead is a
                        straight stretch with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: The white dashed
                        lines correctly fit the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 856, 40.97 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or urban expressway. The road ahead is a
                        straight stretch with no immediate intersections or ramps visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right sides. | roles: The white
                        dashed lines correctly fit the role of crossable lane lines separating traffic in the
                        same direction. | markings: There are no markings in the lane, which is consistent
                        with a standard highway through-lane. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): allowed; the left boundary is a broken white line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed; the right boundary is a broken white line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed; no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 871, 40.3 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway with a clear road ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: The white dashed
                        lines correctly fit the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 834, 9.51 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban expressway, traveling straight ahead
                        toward a potential exit or intersection indicated by overhead signs. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line on the left, which is the edge of the roadway next to
                        a concrete barrier. Photo 2 confirms this solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to the car, with several dashes and gaps
                        visible.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of an edge_line
                        (though usually yellow for left edges, white is used for motor/non-motor or specific
                        road types), and the white broken right boundary fits the role of a lane_line. |
                        markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary (CN-4.2.2-a).
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white right boundary
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8458, out 876, 14.77 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or arterial road with a clear sky and
                        trees on both sides. The road continues straight ahead with no immediate intersection
                        or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to my car, and further ahead it remains
                        solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with the boundaries: a lane line on the left and an edge line on the right would
                        typically mean the rightmost lane, but here the right boundary is an edge line and the
                        left is a lane line, meaning I am in the rightmost lane of a 3-lane road if there are
                        two lanes to my left. Wait, looking at Photo 1, there are three lanes total for my
                        direction. My lane is the rightmost one (index 3). Let me re-evaluate: there is one
                        lane to my left, and one further left. So I am in lane 3. Correcting ego_lane_index to
                        3. | roles: The white dashed line on the left fits the role of a lane line. The white
                        solid line on the right fits the role of an edge line. | markings: No markings are
                        present in my lane, which is consistent with the boundaries. | unseen: No | result:
                        corrected ego_lane_index to 3
Step 5  Rule            left_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The solid white edge line marks the right-hand edge of the direction
                        of travel; crossing it is normally prohibited per CN-4.2.2-a. [CN-5.4.3] "An edge line
                        on the right side of the direction of travel shall be white, and an edge line on the
                        left side of the direction of travel shall be yellow; a motor/"
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 1021, 22.85 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail. Photo 2
                        shows the solid white line next to my car and the guardrail further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line | markings: no markings are
                        present in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line (CN-4.2.2-a)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 845, 41.28 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a slight curve. There are no
                        intersections or ramps immediately ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues as a solid white
                        line further ahead. Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues as a solid white
                        line further ahead. Photo 2 confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white color and solid pattern fit the roles of a no-crossing lane line and
                        a road edge line. | markings: No markings are present in the lane, which is consistent
                        with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits vehicles on the solid-line side from
                        crossing. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The white edge line marks the boundary between the motor vehicle lane
                        and the road edge. [CN-5.4.1] "The carriageway edge line marks the edge of motor
                        vehicle lanes or non-motorized vehicle lanes, or the boundary between motor vehicle
                        lanes and non-motorized ve"
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white lane line (CN-6.2.1).
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['leftmost lane, but a lane line on the left']
Tokens                  in 8458, out 848, 38.83 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road in China, approaching a section where the
                        road layout may change or merge ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which continues ahead. Photo 2 shows a
                        white solid line next to my car, and a metal guardrail (barrier) running parallel to
                        it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings are present
                        in my lane, which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The white solid line on the right marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        line [CN-4.2.2-a] and there is a physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not attempt to cross the right edge line as it is prohibited and blocked by a
                        guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 936, 41.5 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms a broken white line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 confirms a broken white line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings are present in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
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
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 826, 40.27 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road or highway, moving straight ahead with
                        a sound barrier on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings are present in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
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
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 806, 12.75 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway with a sound barrier wall
                        on the right side. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail and a
                        sound barrier wall. Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: no markings in my
                        lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 836, 40.57 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a slight curve. There are no
                        intersections or ramps immediately ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a concrete barrier. Photo 2
                        shows the solid white line next to my car and the concrete barrier immediately to its
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right. | roles: The
                        white dashed line on the left fits the role of a crossable lane line; the white solid
                        line on the right fits the role of a road edge line. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line and a
                        concrete barrier, which [CN-4.2.2-a] prohibits crossing.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move to the right due to the edge line and barrier.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 885, 41.59 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, possibly a bridge or overpass, with a blue bus ahead
                        in the same lane. The road continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail. Photo 2
                        shows the white solid line next to my car and the guardrail immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right. | roles: The
                        white dashed line on the left fits the role of a crossable lane line; the white solid
                        line on the right fits the role of a road edge line. | markings: No markings were
                        observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The white solid line on the right marks the edge of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken white line,
                        which may be crossed according to CN-5.2.1-2.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line and is
                        further restricted by a physical guardrail, and crossing solid lines is normally
                        prohibited per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not attempt to move right as
                        there is a solid edge line and a guardrail.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 8458, out 906, 15.13 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway. The road ahead is a
                        straight stretch with no immediate intersections or ramps. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 4 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings are present in the lane, which is consistent with a
                        standard highway through lane. | unseen: No | result: consistent
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
Advice                  You are in a through lane on a highway. You may continue straight or change lanes to
                        the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 835, 39.61 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a single lane of travel in its direction, heading
                        towards an intersection or a road end. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the road from a raised curb and greenery.
                        Photo 2 confirms a solid white line next to the car, followed by a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a parking/stopping area on
                        the right. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left and right boundaries both being edge lines | roles: the white color and
                        solid pattern for both boundaries fit the role of edge lines | markings: no markings
                        in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white solid line on the left marks the edge of the motor vehicle
                        lane. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 5  Rule            right_boundary: The white solid line on the right marks the edge of the motor vehicle
                        lane. [CN-5.4.3] "An edge line on the right side of the direction of travel shall be
                        white, and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and curb [CN-4.2.2-a]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to either side are prohibited by
                        solid edge lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 810, 39.08 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road in China, traveling straight ahead. There is a
                        physical barrier to the left and a curb to the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a concrete barrier separating the road from another roadway. Photo 2
                        confirms a raised concrete barrier immediately to the left of the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line next to the car that continues ahead. Photo 2 shows this
                        line is a solid white line next to a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the boundaries: a barrier on the left and a curb/edge line on the right. | roles:
                        the white solid line on the right fits the role of a road edge line. | markings: no
                        markings are present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The physical barrier prohibits leaving the lane to the left. [null]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited by the physical barrier (left_boundary).
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to either side are prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8458, out 795, 12.22 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no
                        intersections or ramps immediately visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a raised curb and a yellow line along the left edge of the road. Photo 2
                        confirms a raised curb and a solid yellow line immediately to the left of my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 1 agree with the left boundary being an edge line and the right boundary being a
                        lane line. | roles: The yellow solid line on the left fits the role of a left edge
                        line; the white broken line on the right fits the role of a lane line. | markings:
                        There are no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: A broken white lane line separates traffic in the same direction and
                        may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and the raised curb
                        [CN-4.2.2-a].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left boundary due to the curb and solid line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 911, 39.82 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane road heading straight. There are no intersections or ramps
                        immediately ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues straight ahead.
                        Photo 2 confirms a single solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues straight ahead.
                        Photo 2 confirms a single solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries, as both sides are edge lines. | roles: The white solid lines on
                        both sides fit the role of edge lines for a single-lane road. | markings: There are no
                        markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white edge line on the left marks the boundary between the motor
                        vehicle lane and a non-motorized lane or sidewalk. [CN-5.4.3] "An edge line on the
                        right side of the direction of travel shall be white, and an edge line on the left
                        side of the direction of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The white edge line on the right marks the edge of the roadway.
                        [CN-5.4.3] "An edge line on the right side of the direction of travel shall be white,
                        and an edge line on the left side of the direction of travel shall be yellow; a
                        motor/"
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid white line, and
                        CN-4.2.2-a prohibits crossing solid lines.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line, and
                        CN-4.2.2-a prohibits crossing solid lines.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to either side are prohibited by
                        the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 832, 43.41 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a green-colored pavement, approaching an intersection
                        with a traffic signal ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid grey concrete barrier separating the road from another roadway.
                        Photo 2 confirms a raised concrete barrier immediately to the left of the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is a dense broken
                        white line (short dashes and short gaps) next to the car, continuing ahead.
                        white dotted, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the left concrete barrier and right edge line | roles: the white dotted line on
                        the right fits the role of a road edge line | markings: no markings in lane | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The concrete barrier prohibits crossing to the left. [null]
Step 5  Rule            right_boundary: The broken edge line marks the edge of the roadway and may be crossed.
                        [[CN-5.4.2]]
Step 6  change_left     prohibited (correct): prohibited by the concrete barrier
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white edge line [CN-5.4.2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a single lane bounded by a barrier on the left and a broken edge line on
                        the right. You may proceed straight or move to the right, but you cannot cross the
                        barrier to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation unlisted, contradictions
                        []
Tokens                  in 8458, out 781, 39.07 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading straight toward a
                        distant area with trees and buildings. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating the road from a median strip. Photo 2
                        shows the same solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the road. Photo 2 shows the
                        same solid white line immediately to the right of the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center_line on the left and edge_line on the right | roles: the yellow solid
                        line on the left fits the role of a center_line; the white solid line on the right
                        fits the role of an edge_line | markings: no markings in the lane to contradict |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center_line [CN-6.1.4]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge_line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 822, 13.95 s

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
                        with the left and right boundaries both being edge lines | roles: the white solid
                        lines on both sides fit the role of edge lines separating the motor vehicle lane from
                        the curb/non-motorized path | markings: no markings present in the lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The left edge line is white (on a single-lane two-way road) or yellow;
                        here it is white, marking the edge of the roadway. [CN-5.4.3] "An edge line on the
                        right side of the direction of travel shall be white, and an edge line on the left
                        side of the direction of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The right edge line shall be white, marking the edge of the motor
                        vehicle lane. [CN-5.4.3] "An edge line on the right side of the direction of travel
                        shall be white, and an edge line on the left side of the direction of travel shall be
                        yellow; a motor/"
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary line [CN-4.2.2-a]
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to either side are prohibited by
                        the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 843, 13.79 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road under an overpass on the left, with a
                        sidewalk and trees on the right. The road continues straight ahead. (lanes 3, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the roadway. Photo 2 shows the
                        same solid yellow line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the left boundary being an edge_line (leftmost lane) and the right boundary
                        being a lane_line. | roles: The yellow solid line on the left fits the role of a left
                        edge_line; the white broken line on the right fits the role of a lane_line. |
                        markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid yellow
                        line, and [CN-4.2.2-a] prohibits crossing solid lines.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, and
                        [CN-5.2.1-2] allows crossing it.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 885, 40.05 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a road that appears to be a non-motorized vehicle lane or a shared path,
                        as indicated by the presence of bicycles and scooters and the surrounding environment.
                        The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a green area/shoulder. Photo
                        2 shows the same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a sidewalk/curb area. Photo
                        2 shows the same solid white line next to the car, with a raised curb and greenery
                        immediately to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 both show a white straight-ahead arrow
                        painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries being edge lines on both sides. | roles: The white color and solid
                        pattern for both boundaries fit the role of edge lines separating the lane from non-
                        motorized areas or shoulders. | markings: The straight-ahead arrow is consistent with
                        the lane's boundaries and the general direction of travel. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary (CN-4.2.2-a).
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white right boundary
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1), which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight ahead. Lane changes and turns are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 985, 13.38 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in China, driving straight ahead. There are no intersections
                        or ramps immediately visible in the foreground. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, which continues straight ahead.
                        Photo 2 confirms a single solid yellow line immediately to the left of the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line immediately to the right of the car, bordering a
                        sidewalk area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a center line on the left and an edge line on the right. | roles:
                        The yellow solid line on the left fits the role of a no-crossing center line; the
                        white solid line on the right fits the role of a road edge line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
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
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 8458, out 851, 40.0 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no immediate
                        intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a single solid yellow
                        line next to the car and extending forward.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a no-crossing center line;
                        the white broken line on the right fits the role of a crossable lane line. | markings:
                        No markings were found in the lane, which is consistent with the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8458, out 839, 13.99 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a metal fence. Photo 2 confirms a single
                        solid yellow line immediately to the left of the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line separating the road from a sidewalk/curb area. Photo
                        2 shows a single solid yellow line to the right of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        are slightly contradicted by the boundaries; the left boundary is a yellow center line
                        and the right is a yellow edge line, meaning this is a single-lane road in my
                        direction, not two lanes. I correct lane_count to 1 and ego_lane_index to 1. | roles:
                        The yellow solid left boundary fits the role of a center line on a two-way road. The
                        yellow solid right boundary fits the role of an edge line (though usually white,
                        yellow is used for specific separations or in certain urban contexts). | markings: No
                        markings in lane, consistent with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to either side are prohibited by
                        the solid yellow lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 890, 15.26 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead toward a
                        distant intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a white fence and a solid white line separating the road from a non-
                        motorized lane. Photo 2 confirms a solid white line next to the car, extending further
                        ahead.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a broken white line next to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of a motor/non-motor
                        separation edge line, and the white broken right boundary fits the role of a crossable
                        lane line. | markings: No markings are present in the lane, which is consistent with
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white solid line on the left marks the boundary between motor
                        vehicle lanes and non-motorized vehicle lanes. [CN-5.4.3] "An edge line on the right
                        side of the direction of travel shall be white, and an edge line on the left side of
                        the direction of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The broken white lane line separates traffic flows in the same
                        direction and may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid line, and
                        crossing is normally prohibited per CN-4.2.2-a.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: the right boundary is a broken white line,
                        which may be crossed per CN-5.2.1-2.
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
Advice                  You are in the leftmost motor vehicle lane. You may continue straight or change lanes
                        to the right, but do not cross the solid white line on your left into the non-
                        motorized lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        []
Tokens                  in 8458, out 909, 12.64 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings and trees on both sides, driving straight
                        ahead. (lanes 1, mine 1, full)
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
Step 5  Rule            right_boundary: Crossing the solid white edge line is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken yellow center line [CN-5.1.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          allowed: allowed by the broken yellow center line [CN-5.1.1]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may go straight, make a U-turn, or change left across
                        the center line if safe, but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 8458, out 823, 13.26 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with multiple lanes in its direction, approaching an
                        intersection with a blue overhead guide sign. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, separating the road from a non-
                        motorized lane. Photo 2 shows a white solid line next to my car, and it remains solid
                        further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a crossable lane line, and the white
                        solid line fits the role of a right-hand edge line | markings: no markings in my lane
                        to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the rightmost motor vehicle lane. You may go straight or change to the left
                        lane, but do not cross the solid white line on the right into the non-motorized lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 854, 12.46 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings and trees on both sides, heading towards a
                        straight stretch of road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line on the left. Photo 2 shows this line is a single solid
                        yellow line next to the car and remains solid further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows this line is a solid white line
                        next to the car and remains solid further ahead, bordering a sidewalk with a raised
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right | roles: the yellow solid
                        line on the left fits the role of a no-crossing center line; the white solid line on
                        the right fits the role of a road edge line | markings: no markings in lane | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the presence of a
                        curb [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 834, 36.6 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection in the
                        distance. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, continuing ahead. Photo 2 confirms
                        a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, continuing ahead. Photo 2 confirms
                        a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 790, 11.29 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection with a crosswalk ahead. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car that continues ahead. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and a raised curb further ahead.
                        Photo 2 shows a single solid white line next to the car and a yellow-painted raised
                        curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): Photo 2 shows a white arrow pointing straight and right.
                        Photo 1 shows the same arrow.; line:crosswalk (full): Photo 1 and Photo 2 show a white
                        zebra-stripe crosswalk across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and index 1 agree
                        with the boundaries: a lane line on the left (separating from another lane) and an
                        edge line/curb on the right. | roles: The white solid lines fit the roles of lane line
                        and edge line. | markings: The straight-right arrow is consistent with the lane's
                        position. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            arrow:straight_right: The arrow allows the car to go straight or turn right.
                        [[CN-5.13.1]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern the seven
                        vehicle actions. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line [CN-4.2.2-a]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a] and the
                        raised curb
Step 6  go_straight     allowed (correct): allowed by the straight-right arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight-right arrow [CN-5.13.1]
Step 6  turn_right      allowed (correct): allowed by the straight-right arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-right arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn right. Lane changes are
                        prohibited; stay in your lane and yield to pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions True, unsafe [], citation
                        unlisted, contradictions ['leftmost lane, but a lane line on the left']
Tokens                  in 8458, out 1052, 41.16 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road. Ahead is a clear stretch of road
                        passing under an overpass. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line is a solid
                        yellow line next to my car, continuing as a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line is a
                        broken white line next to my car, with several dashes and gaps visible, continuing as
                        a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with the boundaries: a center line on the left (meaning I am in the leftmost
                        lane of my direction) and a lane line on the right (meaning there is another lane to
                        my right). Wait, if I am in index 2 of 3, I should have a lane line on my left. Let me
                        re-examine. Looking at Photo 1, there are three lanes for my direction. My car is in
                        the middle lane. The boundary to my left is a broken white line, and the boundary to
                        my right is a broken white line. Let me re-evaluate the left boundary. | roles: The
                        left boundary is a broken white lane line, and the right boundary is a broken white
                        lane line. Both fit the role of lane_line. | markings: No markings in my lane. |
                        unseen: no | result: corrected lane_index and left_boundary
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 930, 13.83 s

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
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the right-hand edge of the roadway.
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line and there is a physical barrier, which [CN-4.2.2-a] prohibits crossing.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not attempt to move right as
                        it is the edge of the road bounded by a wall.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 860, 9.87 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road in China, heading towards a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, continuing ahead. Photo 2 confirms a
                        single solid white line and a raised curb further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with the boundaries: a lane line on the left and an edge line on the right
                        indicate the car is in the rightmost motor vehicle lane of a three-lane road (though
                        the leftmost lane is partially obscured by other cars, the boundaries of the ego lane
                        are clear). | roles: The white broken line on the left fits the role of a lane line;
                        the white solid line on the right fits the role of an edge line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the right-hand edge of the direction
                        of travel. [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line and a
                        curb, and [CN-4.2.2-a] prohibits crossing solid lines.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
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
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 915, 14.46 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a narrow road, possibly a service road or access road, with a
                        red wall on the right and bushes on the left. A bridge overpass is visible ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a curb and a line of bushes. Photo 2 shows a raised concrete curb
                        separating the road from the bushes.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a sidewalk and a red wall. Photo 2 shows a raised concrete curb
                        separating the road from a paved sidewalk.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the presence of curbs on both sides | roles: the curbs act as physical edge lines
                        | markings: no markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The physical curb prohibits crossing to the left. [null]
Step 5  Rule            right_boundary: The physical curb prohibits crossing to the right. [null]
Step 6  change_left     prohibited (correct): prohibited by the physical curb on the left
Step 6  change_right    prohibited (correct): prohibited by the physical curb on the right
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not attempt to cross the curbs on either
                        side.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8458, out 748, 12.5 s

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
Step 3  Markings        arrow:right (full): Photo 2 shows a white arrow pointing right.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate
                        the rightmost lane. | roles: the white color and patterns fit the roles of a lane line
                        and an edge line for traffic in the same direction. | markings: the right-turn arrow
                        is consistent with the rightmost lane position. | unseen: no | result: consistent
Step 5  Rule            left_boundary: My car is on the broken side of a broken-solid white line, so it may
                        cross the line to change lanes. [CN-6.2.3] "On a broken-solid white line, vehicles on
                        the solid side may not cross; vehicles on the broken side may cross, and a vehicle
                        crossing the line must give way to "
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:right: The guide arrow indicates that the lane is for right turns. [CN-5.13.1]
                        "Guide arrows indicate the direction of travel for vehicles. (Table 1 meanings:
                        straight ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken line next to
                        my car, and CN-6.2.3 allows crossing from the broken side.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid line and a curb, and
                        CN-4.2.2-a prohibits crossing solid lines.
Step 6  go_straight     prohibited (correct): prohibited: the lane has a right-turn arrow, which prohibits
                        movements not shown (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited: the lane has a right-turn arrow, which prohibits
                        movements not shown (CN-5.13.1).
Step 6  turn_right      allowed (correct): allowed: the right-turn arrow allows this movement (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited: the lane has a right-turn arrow, which prohibits
                        movements not shown (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a right-turn-only lane. If you intend to go straight or turn left, you must
                        change to the left lane before the boundary becomes solid.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 8458, out 1017, 14.52 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or arterial road. The road ahead is
                        straight with no immediate intersections or ramps visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left, separating the road from a
                        shoulder/barrier area. Photo 2 confirms a solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left and a white lane line on the
                        right. | roles: The yellow solid line on the left fits the role of a left edge line;
                        the white broken line on the right fits the role of a crossable lane line. | markings:
                        No markings are present in the lane, which is consistent with the boundaries. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid yellow
                        edge line and there is a physical barrier/curb, and crossing solid lines is normally
                        prohibited [CN-4.2.2-a].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line, which may
                        be crossed [CN-4.2.2-a, CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 887, 11.38 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the one to the left. Photo 2
                        confirms a broken white line next to the car with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail. Photo 2
                        shows a solid white line next to the car and a metal barrier (guardrail) immediately
                        to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows a yellow number '60' inside a blue circle
                        painted on the road surface in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right.
                        | roles: The white broken line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: The speed limit
                        marking is consistent with a highway lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            text:speed_limit: The yellow number shows the maximum speed limit for this lane.
                        [[CN-5.14.2]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line
                        [CN-4.2.2-a] and there is a physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the barrier. Observe the 60 km/h speed limit
                        painted in your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 992, 41.34 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. The road
                        continues forward with no immediate intersection or ramp visible. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms a broken white line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 confirms a broken white line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of crossable lane lines | markings: no markings are
                        present in the lane, which is consistent with the boundaries | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 835, 39.91 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or arterial road. The road ahead is clear
                        and continues straight. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line to the left of my car. Photo 2 confirms a broken
                        white line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car. Photo 2 confirms a broken
                        white line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings are present in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No | result: consistent
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
Tokens                  in 8458, out 827, 38.94 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or arterial road in China, moving
                        straight ahead with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line to the left of my car. Photo 2 confirms a broken
                        white line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car. Photo 2 confirms a broken
                        white line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings are present in the lane, which is consistent with a
                        standard through-lane on a highway. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
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
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 834, 12.81 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway. The road ahead is a
                        straight stretch with no immediate intersections or ramps visible. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a concrete barrier. Photo 2
                        shows a white solid line next to my car and a concrete barrier immediately to its
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
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line
                        [CN-4.2.2-a] and there is a physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you cannot move to the right due to the solid edge line and concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 881, 13.71 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road passing under an overpass, heading towards an open
                        road section. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow solid line next to a metal guardrail. Photo 2 confirms a single
                        yellow solid line and a raised metal barrier (guardrail) on the left.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line. Photo 2 shows a white broken line with long dashes
                        and gaps next to my car, continuing further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left and
                        white lane line on the right agree that my lane is the leftmost of two lanes in my
                        direction. | roles: The yellow solid line fits the role of a no-crossing center line;
                        the white broken line fits the role of a crossable lane line. | markings: No markings
                        are present in the lane, which is consistent with the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane; do not cross the yellow line to the
                        left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 819, 12.69 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a physical barrier. Photo 2 confirms a solid
                        yellow line and a raised metal guardrail barrier immediately to the left of the lane.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the one to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (1)
                        agree with the boundaries: a center line on the left indicates the leftmost lane, and
                        a lane line on the right indicates another lane of the same direction exists. | roles:
                        The yellow solid line on the left fits the role of a no-crossing center line/edge
                        line; the white broken line on the right fits the role of a crossable lane line. |
                        markings: No markings are present in the lane, which is consistent with a highway
                        stretch. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow left boundary [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white right boundary [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or intersection is in view
Step 6  turn_right      not_applicable: not_applicable as no arrow or intersection is in view
Step 6  u_turn          not_applicable: not_applicable as no arrow or intersection is in view
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not cross the solid yellow
                        line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 852, 53.82 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line to the left of my car. Photo 2 confirms a broken
                        white line next to my car with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car. Photo 2 confirms a broken
                        white line next to my car with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: The white dashed lines on both sides correctly fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        my lane, which is consistent with a standard highway through-lane. | unseen: No
                        attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 845, 12.75 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or expressway. The road ahead is straight
                        with no immediate intersection or ramp visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a metal guardrail. Photo 2 confirms a single
                        solid white line immediately to the left of the car, with a raised metal barrier
                        (guardrail) beside it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of an edge_line (road
                        edge), and the white broken right boundary fits the role of a lane_line (separating
                        same-direction traffic). | markings: No markings were observed in the lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid white edge_line (CN-4.2.2-a) and the
                        physical guardrail.
Step 6  change_right    allowed (correct): allowed by the broken white lane_line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right lane if needed. Do not cross the left
                        boundary due to the solid line and guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 875, 13.27 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues straight ahead.
                        Photo 2 confirms a single solid white line immediately to the left of the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with clear dashes and gaps immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a white edge line on the left indicates the leftmost lane,
                        and a white lane line on the right indicates another lane of the same direction. |
                        roles: The white solid line on the left fits the role of an edge line; the white
                        broken line on the right fits the role of a crossable lane line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The white solid line on the left marks the edge of the roadway.
                        [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white line is a crossable lane line separating traffic in
                        the same direction. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid edge line, and crossing
                        it is normally prohibited per [CN-4.2.2-a].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken lane line, which may be
                        crossed per [CN-4.2.2-a] and [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane;
                        changing to the left is prohibited as it is the edge of the road.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 903, 14.56 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a road
                        with an overpass to the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, which continues ahead. Photo 2 shows a
                        solid white line next to my car, and a metal guardrail/barrier running parallel to it
                        further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right
                        indicate my lane is the rightmost of the motor vehicle lanes (excluding the emergency
                        lane). | roles: The white broken line on the left fits the role of a crossable lane
                        line; the white solid line on the right fits the role of a road edge line. | markings:
                        No markings are present in my lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the edge of the motor vehicle lanes.
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which
                        [CN-5.2.1-2] allows crossing.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line and
                        there is a physical barrier, and [CN-4.2.2-a] prohibits crossing solid lines.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not attempt to move to the
                        right as it is the road edge protected by a barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 912, 41.94 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test B | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms this is a broken white line next to my car, with several visible dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to my car, with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed patterns fit the role of crossable lane lines | markings: no markings were
                        observed in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 835, 13.63 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in China, traveling straight ahead on a clear road.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 confirms this is a broken white line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a metal guardrail. Photo 2
                        shows the solid white line next to my car and the guardrail immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows large white numbers '60' and '100' painted on
                        the road surface in my lane; Photo 1 shows these are speed limit markings.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white broken line on the left fits the role of a crossable lane line, and
                        the white solid line on the right fits the role of a road edge line. | markings: The
                        speed limit text is consistent with a highway environment. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line indicates that crossing to the right is normally
                        prohibited. [[CN-4.2.2-a]]
Step 5  Rule            text:speed_limit: These markings show the maximum and minimum speed limits for the
                        lane. [[CN-5.14.2]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line
                        [CN-4.2.2-a] and there is a physical barrier (guardrail).
Step 6  go_straight     allowed (contested, correct): allowed: no markings in my lane restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrows or waiting areas govern this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrows or waiting areas govern this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrows or waiting areas govern this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you must not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 1006, 15.44 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with overhead
                        traffic signals. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line is a
                        broken yellow line next to my car, continuing as a broken yellow line further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line is a solid
                        white line next to my car, continuing as a solid white line further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left
                        indicates my lane is the leftmost of the motor vehicle lanes in my direction, but the
                        lane count of 3 and index 2 suggests there is a lane to my left. However, the yellow
                        line is a center line, meaning the lane to the left is for opposite traffic. Thus, my
                        lane is the leftmost lane of my direction (index 1). Correcting ego_lane_index to 1. |
                        roles: The yellow dashed line fits the role of a crossable center line. The white
                        solid line fits the role of a no-crossing lane line. | markings: No markings in my
                        lane to conflict with boundaries. | unseen: no | result: corrected ego_lane_index to 1
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: Crossing the solid white lane line is prohibited for vehicles on the
                        solid-line side. [[CN-6.2.1]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken yellow center line
                        [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white lane line [CN-6.2.1].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area in my lane.
Step 6  u_turn          allowed: allowed by the crossable center line [CN-5.1.1].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may go straight, make a U-turn, or change left
                        across the center line if safe, but you must not change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 8458, out 928, 15.25 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no
                        intersections or ramps immediately visible in the foreground. (lanes 3, mine 2, full)
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
                        roles: The white dashed lines on both sides correctly fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: There are no markings in
                        my lane to contradict the boundaries. | unseen: No attributes were reported that were
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white lane line,
                        which permits crossing per CN-5.2.1-2.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line, which
                        permits crossing per CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 885, 39.58 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. A bus is
                        stopped or moving slowly in the lane to the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed pattern fits the role of a crossable lane line | markings: no markings were
                        observed in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white lane line
                        (CN-5.2.1-2)
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken white lane line
                        (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 821, 39.96 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with a
                        blue overhead sign indicating a left-turn lane ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the lane to the left.
                        Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, bordering a sidewalk/curb area. Photo
                        2 shows a single solid yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and position (2)
                        agree; the left boundary is a center line (double yellow) and the right is an edge
                        line (solid yellow), meaning my lane is the rightmost lane of my direction. | roles:
                        Yes, yellow lines are used for center lines and left-hand edges, but here the right
                        boundary is also yellow, which is unusual for a right edge (usually white per
                        CN-5.4.3), but it is clearly a solid yellow line bordering a curb. | markings: No
                        markings are present in my lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line [CN-6.1.4]
                        and the presence of a curb.
Step 6  go_straight     allowed (contested, correct): allowed as no markings in my lane restrict it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited by the solid yellow lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 878, 13.59 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with a bus
                        stop on the right. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        correctly serve as lane lines between lanes of the same direction | markings: no
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
Step 6  go_straight     allowed (correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as there is no arrow or
                        waiting area governing this movement
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as there is no arrow or
                        waiting area governing this movement
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as there is no arrow
                        governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane; you may go straight or change lanes to the left or right.
                        Be mindful of the traffic signals and the bus stop on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8458, out 806, 39.04 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken yellow line to the left of my lane. Photo 2 confirms this is a
                        broken yellow line next to my car, with several long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken yellow line to the right of my lane. Photo 2 confirms this is a
                        broken yellow line next to my car, with several long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        area:two_way_left_turn_lane (full): Photo 1 and Photo 2 show a two-way left-turn lane
                        directly to the left of my lane, bounded by yellow broken lines.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count and ego position (2nd of
                        3) are consistent with having boundaries on both sides. However, both boundaries are
                        yellow broken lines, which typically indicates a two-way left-turn lane (TWLTL)
                        configuration where my lane is one of the through lanes. | roles: Yellow broken lines
                        as center lines are consistent with the presence of a TWLTL. | markings: The two-way
                        left-turn lane to the left is consistent with the yellow broken boundary on the left.
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable centre line allows crossing to overtake, turn or make a
                        U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The crossable centre line allows crossing to overtake, turn or make a
                        U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            area:two_way_left_turn_lane: A two-way left-turn lane is a designated area for
                        vehicles to wait or prepare for a left turn. [null]
Step 6  change_left     allowed (contested, correct): allowed; the left boundary is a broken yellow line
                        [CN-5.1.1].
Step 6  change_right    allowed (contested, label prohibited): allowed; the right boundary is a broken yellow
                        line [CN-5.1.1].
Step 6  go_straight     allowed (contested, correct): allowed; no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable; no arrow in my lane governs this movement.
Step 6  turn_right      not_applicable: not_applicable; no arrow in my lane governs this movement.
Step 6  u_turn          not_applicable: not_applicable; no arrow in my lane governs this movement.
Step 6  enter_waiting_areaallowed: allowed; there is a two-way left-turn lane to the left.
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight, change lanes, or enter the two-
                        way left-turn lane to the left if you intend to turn left ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:two_way_left_turn_lane'], missed []), actions None, unsafe [], citation
                        unlisted, contradictions []
Tokens                  in 8458, out 1029, 14.39 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a distant intersection or open
                        road section. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of my lane. Photo 2 confirms two
                        solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my lane. Photo 2 shows a white
                        broken line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left
                        indicates my lane is the leftmost of my direction (or the first lane next to the
                        center), but the lane count shows 3 lanes. Wait, looking closer at Photo 1, there is a
                        lane to my left separated by the double yellow line? No, the double yellow line
                        separates opposing traffic. Therefore, my lane is the leftmost lane of my direction.
                        The lane count of 3 includes the lane to my right and the one further right. My
                        position is 1. | roles: Yellow double solid is a center line; white dashed is a lane
                        line. This fits. | markings: No markings in lane. | unseen: no | result: corrected
                        ego_lane_index to 1
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow center line
                        [CN-6.1.2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane,
                        but you must not cross the double yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 8458, out 886, 41.27 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead towards an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed pattern fits the role of a crossable lane line | markings: no markings are
                        present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as there are no arrows or
                        waiting areas governing this
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as there are no arrows or
                        waiting areas governing this
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as there are no arrows or
                        waiting areas governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 814, 42.63 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line next to my
                        car is a broken yellow line with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line next to my
                        car is a broken white line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries: a center line on the left and a lane line on the right indicate
                        my lane is the second from the left among three lanes of my direction, but the center
                        line indicates it is the leftmost motor lane of my direction if the leftmost lane is a
                        special lane or if the road is two-way. However, looking at the scene, there are three
                        lanes for my direction; the leftmost is separated by a yellow line, meaning it is a
                        two-way left-turn lane or similar. My lane is the first through-lane. | roles: the
                        yellow dashed line on the left fits the role of a crossable center line; the white
                        dashed line on the right fits the role of a crossable lane line. | markings: no
                        markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken yellow center line
                        [CN-5.1.1]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts it
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through-lane. You may change lanes to the left or right if safe.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 755, 13.06 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to the car that continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car that continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed: Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed: Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 781, 42.54 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead toward a
                        distant intersection with overhead signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my lane. Photo 2 shows this line is a solid
                        yellow line next to my car, continuing as a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line to the right of my lane. Photo 2 shows this line is a
                        broken white line next to my car, continuing as a broken white line further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with the boundaries: a center line on the left (meaning I am in the leftmost
                        motor lane of my direction, but there is a two-way left-turn lane or similar to the
                        left) and a lane line on the right (meaning there is another lane to my right). Wait,
                        if I am index 2, there is one lane to my left. But the left boundary is a yellow
                        center line. This means my lane is the leftmost lane of my direction. I must correct
                        ego_lane_index to 1. | roles: The yellow solid line on the left fits the role of a no-
                        crossing center line. The white broken line on the right fits the role of a crossable
                        lane line. | markings: No markings in my lane to check. | unseen: no | result:
                        corrected ego_lane_index to 1
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes. [CN-5.2.1-2]
                        "The crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 943, 46.97 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line on the left. Photo 2 shows this line is a solid yellow
                        line next to the car, continuing as a solid yellow line further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a yellow line on the right. Photo 2 shows this line is a broken yellow
                        line next to the car, consisting of several short dashes and gaps, continuing as a
                        broken yellow line further ahead.
                        yellow dashed, curb no, center_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show a yellow grid-like area with
                        diagonal lines to the right of the lane, but it is not inside my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The yellow boundaries on both sides
                        indicate that my lane is a special lane separating opposing traffic flows, likely a
                        two-way left-turn lane or a tidal lane. | roles: The yellow color for both boundaries
                        fits the role of separating opposing traffic flows. | markings: The channelizing area
                        is to the right, not in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken yellow center line means vehicles may cross the line to
                        overtake, turn or make a U-turn when safe. [[CN-5.1.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid yellow center line
                        [CN-6.1.4].
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken yellow center line
                        [CN-5.1.1].
Step 6  go_straight     allowed (contested, correct): allowed as no marking in the lane restricts it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a lane bounded by yellow lines. You may proceed straight or change lanes to
                        the right, but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8458, out 921, 15.29 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a green-colored pavement, heading towards a
                        distant intersection or road section. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow solid line separating my lane from the lane to the left.
                        Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid grey concrete barrier on the right. Photo 2 shows the concrete
                        barrier immediately to the right of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a center line on the left and a barrier on the right
                        indicate the rightmost lane of a two-lane road. | roles: The double solid yellow line
                        fits the role of a no-crossing center line; the concrete barrier fits the role of a
                        road edge. | markings: No markings are present in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The concrete barrier marks the edge of the roadway and prohibits
                        leaving the roadway. [[CN-5.4.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by the double solid yellow line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the concrete barrier [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 835, 39.43 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which remains broken further ahead.
                        Photo 2 confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues as a solid line
                        ahead. Photo 2 confirms a single solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having a lane line on both the left and right. | roles: White dashed and
                        solid lines are consistent with lane lines separating traffic in the same direction. |
                        markings: The straight-ahead arrow is consistent with the lane's position and
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing from my side.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The guide arrow indicates the allowed direction of travel is straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a broken
                        white line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white line [CN-6.2.1].
Step 6  go_straight     allowed (correct): allowed because the lane arrow shows straight ahead [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the lane arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited because the lane arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the lane arrow only shows straight ahead
                        [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but
                        changing to the right lane is prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 933, 14.72 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a bridge
                        overhead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which remains broken further ahead.
                        Photo 2 confirms a broken white line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which remains broken further ahead.
                        Photo 2 confirms a broken white line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white guide arrow pointing straight ahead in
                        the center of the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        correctly serve as lane lines separating traffic in the same direction. | markings:
                        The straight-ahead arrow is consistent with the lane's position as a through lane. |
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
Step 6  change_left     allowed (correct): allowed; the left boundary is a broken white line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed; the right boundary is a broken white line (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed; the guide arrow indicates straight ahead (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited; the guide arrow only shows straight ahead,
                        prohibiting other movements (CN-5.13.1).
Step 6  turn_right      prohibited (correct): prohibited; the guide arrow only shows straight ahead,
                        prohibiting other movements (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited; the guide arrow only shows straight ahead,
                        prohibiting other movements (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. Do not attempt to
                        turn left or right from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 964, 40.58 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows the broken white line
                        next to the car with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: the white dashed
                        lines fit the role of lane lines separating traffic in the same direction | markings:
                        no markings were observed in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may go straight or change lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation accepted, contradictions []
Tokens                  in 8458, out 792, 11.78 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, driving straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line on the left, which is solid near the car and remains solid
                        further ahead. Photo 2 confirms a single solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line on the right. Photo 2 shows a white broken line next
                        to the car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow solid line on the left fits the role of a no-crossing center line;
                        the white broken line on the right fits the role of a crossable lane line. | markings:
                        No markings are present in the lane, which is consistent with the boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 853, 39.8 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a pedestrian
                        crosswalk. (lanes 3, mine 2, full)
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
                        dashed lines correctly fit the role of lane lines separating traffic in the same
                        direction. | markings: the crosswalk is a standard marking across the lane and does
                        not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern the seven
                        vehicle actions. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    allowed (WRONG, label prohibited): allowed: the right boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no arrow restricts this movement.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right. Be mindful of the pedestrian crosswalk ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation unlisted,
                        contradictions []
Tokens                  in 8458, out 928, 37.66 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: the white
                        dashed pattern fits the role of a crossable lane line | markings: no markings were
                        observed in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
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
Tokens                  in 8458, out 807, 40.23 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        overhead lane-use signs. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows a solid
                        white line next to the car and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows white Chinese characters '公交专用' painted vertically in
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the right boundary being an edge line and the left boundary being a lane
                        line. | roles: the white color and broken/solid patterns fit the roles of lane line
                        and edge line for traffic in the same direction. | markings: the '公交专用' (bus only)
                        text is consistent with the lane being a reserved bus lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: My car is on the broken side of a broken-solid white line, so it may
                        cross into the left lane, giving way to other vehicles. [CN-6.2.3] "On a broken-solid
                        white line, vehicles on the solid side may not cross; vehicles on the broken side may
                        cross, and a vehicle crossing the line must give way to "
Step 5  Rule            right_boundary: The solid white edge line means crossing to the right is normally
                        prohibited. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 5  Rule            text:bus: Vehicles other than buses shall not enter this lane. [CN-6.9.1] "The bus
                        lane line shows that vehicles other than buses shall not enter the lane. It consists
                        of a broken white line and white text. The broken line has 5 m segm"
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken-solid white line
                        and my car is on the broken side [CN-6.2.3].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed: no marking in the lane prohibits going
                        straight, and the car is already in the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a reserved bus lane ('公交专用'). If you are not driving a bus, you
                        should change left into the adjacent lane as soon as possible, as the current lane is
                        reserved for buses.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:bus'], missed ['text:other']), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8458, out 985, 40.9 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test B | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, which remains broken further ahead.
                        Photo 2 confirms a broken white line with several dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows a broken white line
                        with dashes and gaps next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane; Photo 1
                        shows the same arrow further ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right | roles: white broken
                        and solid lines are consistent with lane lines separating traffic in the same
                        direction | markings: the straight-ahead arrow is consistent with the lane boundaries
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line further ahead prohibits me from crossing it.
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: The guide arrow indicates that I should travel straight ahead.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited because the right boundary becomes a solid white line
                        [CN-6.2.1]
Step 6  go_straight     allowed (correct): allowed because the lane arrow shows straight ahead [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited because the lane arrow only shows straight ahead
                        [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited because the lane arrow only shows straight ahead
                        [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited because the lane arrow only shows straight ahead
                        [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the intersection. You may change to the
                        left lane if needed, but changing to the right is prohibited as you approach the
                        intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left'], citation accepted,
                        contradictions []
Tokens                  in 8458, out 962, 20.65 s

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
                        Photo 1 also shows this arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the right boundary being an edge line and the left boundary being a lane
                        line. | roles: The white solid line on the left fits the role of a no-crossing lane
                        line on an intersection approach. The white solid line and curb on the right fit the
                        role of a road edge line. | markings: The straight-ahead arrow is consistent with the
                        lane's position as a through lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line prohibits crossing from the solid side.
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the vehicle should proceed
                        straight. [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by the solid white lane line [CN-6.2.1]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and raised curb
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
Tokens                  in 8458, out 968, 14.25 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings and trees on both sides, heading
                        straight. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a single solid yellow
                        line next to the car and extending forward.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a broken white line next to the
                        car, consisting of short dashes and gaps.
                        white dotted, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The single lane count and index 1 agree
                        with a center line on the left and an edge line on the right. | roles: The yellow
                        solid line fits the role of a no-crossing center line; the white dotted line fits the
                        role of a broken edge line. | markings: No markings in the lane to contradict. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken edge line may be crossed at roadside openings or where
                        parking is allowed. [[CN-5.4.6]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white edge line [CN-5.4.6]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid yellow line to the
                        left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 796, 13.07 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with traffic
                        signals. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a broken white line with long dashes and gaps next to the car.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a raised curb. Photo 2 shows a solid white line
                        and a raised curb next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the right boundary being an edge line and the left boundary being a lane
                        line. | roles: the white color and patterns fit the roles of a lane line on the left
                        and an edge line on the right. | markings: the straight arrow is consistent with the
                        lane's position and boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: My car is on the broken side of a broken-solid white line, so it may
                        cross the line to change lanes. [CN-6.2.3] "On a broken-solid white line, vehicles on
                        the solid side may not cross; vehicles on the broken side may cross, and a vehicle
                        crossing the line must give way to "
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The guide arrow indicates that the vehicle should travel straight
                        ahead. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table
                        1 meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken-solid
                        white line and my car is on the broken side [CN-6.2.3].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white line
                        [CN-4.2.2-a] and there is a raised curb.
Step 6  go_straight     allowed (contested, correct): allowed because the lane marking is a straight arrow
                        [CN-5.13.1].
Step 6  turn_left       prohibited: prohibited because the lane marking is a straight arrow, which restricts
                        movement to straight only [CN-5.13.1].
Step 6  turn_right      prohibited: prohibited because the lane marking is a straight arrow, which restricts
                        movement to straight only [CN-5.13.1].
Step 6  u_turn          prohibited: prohibited because the lane marking is a straight arrow, which restricts
                        movement to straight only [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. If you need to turn, you must change to the left
                        lanes before the intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:stop_line']), actions False, unsafe ['change_left'],
                        citation accepted, contradictions []
Tokens                  in 8458, out 1007, 13.93 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a crosswalk and
                        a right-turn channel ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line that curves to the right, forming a channel. Photo 2
                        shows a solid white line immediately to the right of my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead guide arrow in my lane.;
                        line:crosswalk (full): Photo 1 and Photo 2 show a white zebra crosswalk across the
                        lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with having a lane line on the left and a boundary on the right. | roles: The
                        white dashed line on the left fits the role of a crossable lane line; the white solid
                        line on the right fits the role of a guide lane line for the intersection approach. |
                        markings: The straight-ahead arrow is consistent with the lane's path and the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white guide lane line prohibits crossing. [[CN-6.10.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [[CN-5.13.1]]
Step 5  Rule            line:crosswalk: The crosswalk is an informative marking for pedestrian crossing and
                        does not govern the seven actions. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white guide lane line
                        [CN-6.10.1-2].
Step 6  go_straight     allowed (correct): allowed: the guide arrow in my lane shows straight ahead
                        [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited: the guide arrow only shows straight ahead,
                        prohibiting other movements [CN-5.13.1].
Step 6  turn_right      prohibited (correct): prohibited: the guide arrow only shows straight ahead,
                        prohibiting other movements [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited: the guide arrow only shows straight ahead,
                        prohibiting other movements [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight ahead. You may change to the left lane if
                        needed, but do not cross the solid line to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk'], missed ['line:stop_line']), actions False, unsafe ['change_left'],
                        citation unlisted, contradictions ['rightmost lane, but a lane line on the right']
Tokens                  in 8458, out 1115, 46.32 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings and trees on both sides, driving straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line extending from the bottom to the distance. Photo 2
                        shows the same solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        yellow center line on the left and a white edge line on the right indicate a single
                        lane for my direction. | roles: the yellow solid line fits the role of a no-crossing
                        center line, and the white solid line fits the role of a road edge line. | markings:
                        no markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and the presence of a
                        curb [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 817, 38.73 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test B | gemma4:31b | from cache
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a single-lane road, likely a bridge or overpass, with buildings
                        on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a concrete barrier and a raised curb on the left. Photo 2 confirms a
                        raised concrete curb forming the left edge of the lane.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a concrete barrier and a raised curb on the right. Photo 2 confirms a
                        raised concrete curb forming the right edge of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the presence of curbs on both sides. | roles: The curbs act as physical
                        boundaries for the single lane. | markings: No markings are present in the lane. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: The physical curb prohibits leaving the lane to the left. [null]
Step 5  Rule            right_boundary: The physical curb prohibits leaving the lane to the right. [null]
Step 6  change_left     prohibited (correct): prohibited by the physical curb on the left.
Step 6  change_right    prohibited (correct): prohibited by the physical curb on the right.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes are prohibited by the
                        physical barriers on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8458, out 761, 12.08 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test B | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no
                        intersections or ramps immediately visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which separates the road from a red-
                        painted bicycle lane. Photo 2 shows this solid white line next to my car, and it
                        continues straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a crossable lane line; the
                        white solid line on the right fits the role of a road edge line. | markings: There are
                        no markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that I may cross it to change
                        lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white edge line marks the boundary between the motor vehicle
                        lane and the non-motorized lane. [[CN-5.4.1]]
Step 5  Rule            right_boundary: The solid line means crossing into the bicycle lane is normally
                        prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line [CN-5.2.1-2].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not enter the red bicycle
                        lane on your right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8458, out 920, 40.52 s
```
