# Reasoning of lane run 20261118_001835_laneB_US

```text
bdd100k_val__b2afce7f-0cb9967a | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane highway with traffic moving in the same direction, heading straight.
                        (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a single white dash and gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the edge of the roadway, with a metal guardrail
                        running alongside it. Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the left and an edge line on the right
                        indicate I am in the rightmost lane. | roles: the white broken line for a lane
                        separator and white solid line for the roadway edge fit their roles. | markings: no
                        markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02] and the presence of a guardrail.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you cannot move to the right due to the edge line and guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 876, 3.83 s

bdd100k_val__b459e707-2d208c56 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane road in a suburban area, with the car traveling straight ahead. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from another lane to the left.
                        Photo 2 shows the same broken white line next to my car, consisting of several white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right edge of the roadway. Photo 2 shows a
                        solid yellow line next to my car.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the lane line with
                        care is not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line is used for the right edge, but here a solid yellow
                        line is used, which according to [US-3A.03-03-04] delineates the left-hand edge of a
                        divided highway or one-way street; however, since it is on the right, it serves as a
                        boundary to the roadway edge. [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the broken white lane line [US-3B.06-05-06] permits
                        crossing with care.
Step 6  change_right    prohibited (correct): prohibited: the solid yellow line [US-3A.04-01] discourages or
                        prohibits crossing the roadway edge.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left. Do not cross the right boundary
                        line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 864, 23.38 s

bdd100k_val__b5046f1e-b1ef44b9 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides, approaching an intersection.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues forward. Photo 2
                        shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues forward. Photo 2
                        shows a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the end of a word, 'NLY', and Photo 1 shows the full
                        word 'ONLY' painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        white edge line on the left and a white lane line on the right indicate the leftmost
                        lane of a multi-lane road in the same direction. | roles: the white solid line on the
                        left fits the role of an edge line, and the white broken line on the right fits the
                        role of a lane line. | markings: the 'ONLY' text is in the lane, but there is no
                        accompanying arrow visible in the lane to specify the movement. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            text:only: The ONLY word marking is used to supplement lane-use arrow markings in
                        lanes designated for the exclusive use of a single movement. [[US-3B.21-04]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a solid edge line
                        [US-3B.09-01-02].
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a broken lane
                        line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no arrow restricts this movement, and the lane
                        does not end.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you cannot cross the left edge line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 986, 3.64 s

bdd100k_val__b6decb24-82234e11 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           City street with multiple lanes of traffic moving in the same direction, approaching
                        an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, which continues as a broken white
                        line further ahead. Photo 2 shows a broken white line with several long dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, which continues as a broken white
                        line further ahead. Photo 2 shows a broken white line with several long dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the word 'ONLY' painted in white in my lane. Photo 1
                        shows a left-turn arrow ahead of the word 'ONLY'.; arrow:left (full): Photo 1 shows a
                        left-turn arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            text:only: The ONLY word marking is used to supplement lane-use arrows in lanes
                        designated for the exclusive use of a single movement. [[US-3B.21-04]]
Step 5  Rule            arrow:left: The left-turn arrow indicates that the mandatory or permissible movement
                        for this lane is a left turn. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     prohibited (WRONG, label allowed): prohibited by the left-turn arrow and ONLY marking
                        [US-3B.23-01], [US-3B.21-04]
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the left-turn arrow [US-3B.23-01]
Step 6  turn_right      prohibited (correct): prohibited by the left-turn arrow and ONLY marking
                        [US-3B.23-01], [US-3B.21-04]
Step 6  u_turn          allowed (WRONG, label prohibited): allowed by the left-turn arrow [US-3B.23-01] as it
                        is a turn toward opposite traffic
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  My lane is a mandatory left-turn lane. I must turn left or perform a U-turn at the
                        intersection, or change lanes if I intend to go straight.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:left', 'text:only'], missed ['arrow:straight']), actions False, unsafe
                        ['turn_left', 'u_turn'], citation accepted, contradictions []
Tokens                  in 9506, out 1093, 30.96 s

bdd100k_val__b7719f1d-e6e580dd | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway heading straight. There are no intersections or
                        ramps immediately ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the roadway, with a concrete
                        barrier beyond it. Photo 2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; a lane line on the left and an edge line on the right indicate
                        the rightmost lane. | roles: the white broken line for a lane separator and white
                        solid line for the roadway edge fit their roles. | markings: no markings in my lane to
                        check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02] and the physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you cannot move to the right due to the edge line and barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 867, 35.42 s

bdd100k_val__b775af1c-bb5afbe3 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The road is a multi-lane city street approaching an intersection. My car is in the
                        rightmost lane. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with one dash and one gap next to my
                        car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car and a raised curb further ahead. Photo
                        2 shows a solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 2 shows a white arrow pointing right in my lane.;
                        line:stop_line (full): Photo 1 and Photo 2 show a solid white line extending across my
                        lane at the intersection.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a white lane line on the left and an edge line/curb on
                        the right indicate the rightmost lane of a two-lane road. | roles: the white color and
                        solid/broken patterns fit the roles of lane line and edge line. | markings: the right-
                        turn arrow and stop line are consistent with the lane's position as a mandatory turn
                        lane at an intersection. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line discourages crossing into the adjacent lane.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:right: The arrow indicates that a right turn is the mandatory movement for this
                        lane. [[US-3B.23-01]]
Step 5  Rule            line:stop_line: The stop line indicates the point where vehicles are required to stop.
                        [[US-3B.19-01-02]]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, label allowed): prohibited by the edge line and curb
                        [US-3B.09-01-02].
Step 6  go_straight     prohibited (correct): prohibited by the right-turn arrow [US-3B.23-01].
Step 6  turn_left       prohibited (correct): prohibited by the right-turn arrow [US-3B.23-01].
Step 6  turn_right      stop_first (WRONG, label allowed): stop_first because the right-turn arrow allows the
                        movement [US-3B.23-01] but the stop line requires a stop [US-3B.19-01-02].
Step 6  u_turn          prohibited (correct): prohibited by the right-turn arrow [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a mandatory right-turn lane. Stop at the stop line and then turn right;
                        lane changes are prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 1139, 35.07 s

bdd100k_val__b9db357e-cd30a8ae | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           Urban road with multiple lanes approaching a signalized intersection. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line with one long dash and one gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with one long dash and one gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 780, 27.06 s

bdd100k_val__bc05c126-d00aeb9c | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A two-way urban road with parked cars on the left and a red-colored shoulder or bike
                        lane on the right. My car is in the rightmost lane of its direction. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 shows two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a red-colored area. Photo 2
                        shows a single solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited
                        for traffic traveling in either direction. [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 808, 6.22 s

bdd100k_val__bca36352-5de70a3f | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The road is a multi-lane urban street with a construction zone ahead, where the
                        roadway narrows or is redirected by cones and barriers. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line that becomes a solid yellow line further ahead as it
                        enters a construction area. Photo 2 shows a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You may continue straight in your lane or change to the left lane. Do not cross the
                        solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 787, 2.96 s

bdd100k_val__bcbbfd82-add80c05 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, approaching an intersection. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from another lane to the left.
                        Photo 2 shows the same white broken line next to my car, consisting of long dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the right edge of the roadway. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change lanes to the left, but
                        you cannot cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 9506, out 776, 34.78 s

bdd100k_val__bd026bc5-9418706c | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in an urban area, approaching an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a white broken line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a white broken line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates the lane is for going straight.
                        [[US-FIG-3B-21]]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the through lane-use arrow [US-FIG-3B-21]
Step 6  turn_left       prohibited (correct): prohibited by the through lane-use arrow [US-FIG-3B-21]
Step 6  turn_right      prohibited (correct): prohibited by the through lane-use arrow [US-FIG-3B-21]
Step 6  u_turn          prohibited (correct): prohibited by the through lane-use arrow [US-FIG-3B-21]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. Lane changes to the left or
                        right are permitted.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 9506, out 912, 34.51 s

bdd100k_val__be278041-2173a980 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road or ramp approaching a split or intersection, with a
                        concrete barrier on the left. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 shows the same
                        solid yellow line and concrete barrier immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that is broken near the car and becomes a double solid
                        white line further ahead. Photo 2 shows a broken white line (one dash and one gap
                        visible) next to the car.
                        white solid_dashed (near line dashed), curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        yellow edge line on the left indicates the leftmost lane of the direction of travel. |
                        roles: the yellow solid edge line and white lane line fit their roles. | markings: no
                        markings in lane, consistent with boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway and
                        indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: The broken white line indicates that crossing the lane line with care
                        is not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and concrete barrier
                        [US-3B.09-03].
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not cross the left boundary due to the
                        solid yellow line and concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 840, 8.51 s

bdd100k_val__be4cbd00-97fec78b | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street at night, approaching an intersection with
                        traffic signals. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing forward. Photo 2 shows a
                        single white dash next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing forward. Photo 2 shows a
                        single white dash next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as no arrow or prohibited-
                        movement marking governs this action
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable as no arrow or prohibited-
                        movement marking governs this action
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as no arrow or prohibited-
                        movement marking governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 782, 4.19 s

bdd100k_val__beccfad4-d24a29c5 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, likely a ramp or a divided highway, heading towards
                        an intersection or a merge point. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues forward. Photo 2
                        shows a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues forward. Photo 2
                        shows a broken white line with several short dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [US-3A.04-01] "The general functions of longitudinal lines shall be as follows: A. A
                        double line indicates maximum or special restrictions. B. A solid line discourages or
                        proh"
Step 6  change_left     prohibited (correct): prohibited: the left boundary is an edge line with a physical
                        barrier (curb), and the solid line discourages/prohibits crossing [US-3A.04-01].
Step 6  change_right    allowed (WRONG, label prohibited): allowed: the right boundary is a broken white lane
                        line, which indicates a permissive condition [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You may continue straight in your lane or change lanes to the right. Do not cross the
                        left boundary as it is the edge of the roadway with a barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 9506, out 823, 31.27 s

bdd100k_val__bf6315ee-a77e1bb2 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street at night, approaching a signalized
                        intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right edge of the roadway. Photo 2 shows a
                        white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change lanes to the left, but
                        you cannot cross the right edge line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 777, 35.62 s

bdd100k_val__bf6711ef-76e408aa | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching an intersection or a point
                        where lanes are designated for specific movements. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the roadway. Photo 2 shows the
                        same solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a broken white line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the word 'ONLY' painted in the lane. Photo 1 also
                        shows it.; arrow:straight (full): Photo 1 and Photo 2 show a white arrow pointing
                        straight ahead in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        yellow edge line on the left indicates the leftmost lane of the direction of travel. |
                        roles: the yellow solid edge line and white broken lane line fit their roles. |
                        markings: the 'ONLY' text and straight arrow are consistent with a mandatory through
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway and
                        indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: The broken white line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            text:only: The ONLY word marking supplements the lane-use arrow to designate the lane
                        for the exclusive use of a single movement. [[US-3B.21-04]]
Step 5  Rule            arrow:straight: The through lane-use arrow indicates that the mandatory movement for
                        this lane is to go straight. [[US-FIG-3B-21]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03].
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): allowed by the straight lane-use arrow [US-FIG-3B-21].
Step 6  turn_left       prohibited (correct): prohibited by the straight lane-use arrow [US-FIG-3B-21] and the
                        ONLY text [US-3B.21-04].
Step 6  turn_right      prohibited (correct): prohibited by the straight lane-use arrow [US-FIG-3B-21] and the
                        ONLY text [US-3B.21-04].
Step 6  u_turn          prohibited (correct): prohibited by the straight lane-use arrow [US-FIG-3B-21] and the
                        ONLY text [US-3B.21-04].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a mandatory through lane; you must go straight. You may change lanes to the
                        right if needed, but you cannot cross the yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 1146, 35.61 s

bdd100k_val__bfd64d5f-ec05de8b | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The road is a multi-lane highway with an exit ramp to the right. My car is in the
                        rightmost through lane approaching the exit. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from another lane to the left.
                        Photo 2 shows the same broken white line next to my car, consisting of long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line that separates my lane from the exit ramp. Photo 2
                        shows this solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a broken white line on the left indicates another lane
                        of my direction, and a solid white line on the right separates my lane from the exit
                        ramp area. | roles: the white color and patterns (dashed left, solid right) fit the
                        roles of a lane line and a boundary separating through traffic from an auxiliary/exit
                        area. | markings: no markings are present in my lane, which is consistent with the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line discourages crossing. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which permits
                        crossing per [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a solid white
                        line, which discourages but does not prohibit crossing per [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed: no marking governs this action, and the
                        boundaries do not restrict continuing straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost through lane. You may continue straight or change lanes to
                        the left. Crossing the solid white line to the right will lead you onto the exit ramp.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 9506, out 928, 3.36 s

bdd100k_val__c01c4d85-36b417ee | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane road at night, appearing to be a highway or a wide urban road, with my
                        car traveling straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from another lane to the left.
                        Photo 2 shows a single white dash and gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the roadway. Photo 2 shows a
                        continuous solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you must not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 820, 3.99 s

bdd100k_val__c0a71f47-14439a44 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, approaching an intersection with
                        traffic signals visible ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating the road from opposite traffic.
                        Photo 2 shows the same double solid yellow lines next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows the right edge of the roadway with no painted line. Photo 2 shows the
                        road surface ending at the right edge with no painted line.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing double solid yellow center lines for passing is prohibited for
                        traffic traveling in either direction. [[US-3B.01-04]]
Step 5  Rule            right_boundary: No painted line is present, but the edge of the roadway defines the
                        boundary. [null]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (correct): prohibited as it would leave the roadway (edge of road)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight toward the intersection; do not cross the
                        double yellow lines to the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 9506, out 748, 19.04 s

bdd100k_val__c0f5b0d0-17e0110c | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road at night, traveling straight ahead on what appears to
                        be a highway or ramp. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows the same solid yellow
                        line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left edge of a divided highway or one-way
                        street delineates the left-hand edge of the roadway. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and continue straight; lane changes to the left or right are
                        prohibited by the edge lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 769, 4.2 s

bdd100k_val__c16d3fdb-a3a8c912 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is traveling on a divided highway with a concrete barrier on the left and a
                        guardrail on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car and continuing ahead, with a
                        concrete barrier to its left. Photo 2 shows the same solid yellow line next to the
                        car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and continuing ahead, with a
                        guardrail further right. Photo 2 shows the same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway.
                        [[US-3B.09-03]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03] and the
                        concrete barrier.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes to the left or right are
                        prohibited by the edge lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 798, 31.93 s

bdd100k_val__c1e6340e-084ce27d | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road at night, moving straight ahead. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows a solid yellow line next
                        to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line on the right. Photo 2 shows a broken white line next
                        to the car with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        yellow edge line on the left indicates the leftmost lane of the roadway. | roles: the
                        yellow solid line fits the role of a left edge line, and the white broken line fits
                        the role of a lane line. | markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left edge of a roadway indicates the left-
                        hand edge and restricts driving to the left of this marking. [US-3B.09-03] "If used on
                        the roadways of divided highways or one-way streets, or on any ramp in the direction
                        of travel, left edge line pavement markings shall consist of a n"
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [US-3A.04-01] "The general functions of longitudinal lines shall be as follows: A. A
                        double line indicates maximum or special restrictions. B. A solid line discourages or
                        proh"
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not cross the yellow line on the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 813, 2.88 s

bdd100k_val__c39dc2ff-6976d19d | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city street at night, approaching an intersection. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line on the left edge of the road. Photo 2 shows the same
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the lane to the right. Photo
                        2 shows the same solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): Photo 2 shows a white left-turn arrow in my lane.; text:only
                        (full): Photo 2 shows the white word 'ONLY' in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The solid white lane line discourages crossing into the adjacent lane.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:left: The left-turn arrow indicates that a left turn is a mandatory or
                        permissible movement. [[US-3B.23-01]]
Step 5  Rule            text:only: The ONLY word marking indicates that the lane is designated for the
                        exclusive use of a single movement. [[US-3B.21-04]]
Step 6  change_left     prohibited (correct): prohibited by the left edge line [US-3B.09-01-02]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white lane line
                        [US-3B.06-05-06]
Step 6  go_straight     prohibited (correct): prohibited by the left-turn arrow and ONLY marking
                        [US-3B.23-01], [US-3B.21-04]
Step 6  turn_left       allowed (correct): allowed by the left-turn arrow [US-3B.23-01]
Step 6  turn_right      prohibited (correct): prohibited by the left-turn arrow and ONLY marking
                        [US-3B.23-01], [US-3B.21-04]
Step 6  u_turn          allowed (correct): allowed by the left-turn arrow [US-3B.23-01]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a mandatory left-turn lane. You must turn left or perform a U-turn at the
                        intersection; lane changes and going straight are prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 9506, out 1038, 13.22 s

bdd100k_val__c3ecb3cb-5fb43d29 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane urban road with a construction zone on the left; my car is in a lane that
                        is designated for a specific movement. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left, bordered by a row of orange and white
                        traffic cones. Photo 2 shows the same solid yellow line and cones immediately next to
                        my car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that is broken near my car and becomes solid further ahead.
                        Photo 2 shows a broken white line (one dash and one gap visible) next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the word 'ONLY' painted in white in my lane.;
                        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway and
                        indicates driving restrictions to the left. [[US-3B.09-03]]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted with care. [[US-3B.06-05-06]]
Step 5  Rule            text:only: The ONLY marking supplements the lane-use arrow to designate the lane for
                        the exclusive use of a single movement. [[US-3B.21-04]]
Step 5  Rule            arrow:straight: The through lane-use arrow indicates that the mandatory movement for
                        this lane is to go straight. [[US-FIG-3B-21]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03]
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the through lane-use arrow [US-FIG-3B-21]
Step 6  turn_left       prohibited (correct): prohibited by the through lane-use arrow [US-FIG-3B-21]
Step 6  turn_right      prohibited (correct): prohibited by the through lane-use arrow [US-FIG-3B-21]
Step 6  u_turn          prohibited (correct): prohibited by the through lane-use arrow [US-FIG-3B-21]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the right if needed, but do
                        not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 1048, 3.67 s

bdd100k_val__c400a0e1-c137168b | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban roadway, likely a highway or ramp, with an exit or
                        intersection ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms a solid
                        yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the word 'ONLY' painted in white in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway and
                        indicates driving restrictions to the left. [[US-3B.09-03]]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        is permitted with care. [[US-3B.06-05-06]]
Step 5  Rule            text:only: The ONLY marking indicates that the lane is designated for the exclusive
                        use of a single movement. [[US-3B.21-04]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and concrete barrier
                        [US-3B.09-03]
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     prohibited (contested, label allowed): prohibited because the lane is marked ONLY for
                        a specific movement (turn right) [US-3B.21-04]
Step 6  turn_left       prohibited: prohibited by the left boundary and the ONLY marking [US-3B.21-04]
Step 6  turn_right      allowed: allowed as the ONLY marking corresponds to the exit/turn movement indicated
                        by the road geometry and signs [US-3B.21-04]
Step 6  u_turn          prohibited: prohibited by the ONLY marking and the left boundary [US-3B.21-04]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a mandatory turn-only lane. You must turn right or change lanes to the
                        right if you intend to go straight.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:only'], missed []), actions True, unsafe [], citation accepted, contradictions
                        ['go_straight, turn_left, turn_right, u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 9506, out 941, 18.5 s

bdd100k_val__c464c963-0279dcc0 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a two-way residential road with parked cars on both sides, heading
                        straight. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating the road from the opposite
                        direction. Photo 2 shows the same double solid yellow line next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, but a curb with parked cars. Photo 2 shows
                        the road edge meeting a raised curb with a parked car next to it.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The right edge of the roadway is delineated by the curb.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (correct): prohibited by the raised curb [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area exists
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes are prohibited on both sides.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 756, 34.34 s

bdd100k_val__c4b77809-63fd577c | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city street approaching an intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line. Photo 2 shows two solid yellow lines side by
                        side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows the edge of the roadway with a white truck parked next to it. Photo 2
                        shows no painted line, but the road edge meets the sidewalk/curb area.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:stop (full): Photo 2 shows the word 'STOP' painted in white across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The right edge of the roadway is delineated. [[US-3B.09-01-02]]
Step 5  Rule            text:stop: Vehicles are required to stop at this marking. [[US-3B.19-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (correct): prohibited by the curb/edge of the roadway [US-3B.09-01-02]
Step 6  go_straight     stop_first (contested, correct): stop_first due to the STOP word marking
                        [US-3B.19-01-02]
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stop your vehicle at the STOP line before proceeding straight through the
                        intersection. Lane changes are prohibited.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 861, 3.63 s

bdd100k_val__c4d25f00-3b1d8669 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, approaching a signalized intersection
                        with a crosswalk. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line to the left of my car. Photo 2 shows a single white
                        dash and a gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car. Photo 2 shows a single white
                        dash and a gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white crosswalk extending across my lane at the
                        intersection.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06] "Where crossing the lane line markings
                        with care is not discouraged or prohibited, the lane line markings shall consist of a
                        normal width broken white line. Wher"
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06] "Where crossing the lane line markings
                        with care is not discouraged or prohibited, the lane line markings shall consist of a
                        normal width broken white line. Wher"
Step 5  Rule            line:crosswalk: A crosswalk is an informative marking and does not govern the seven
                        actions. [null]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (US-3B.06-05-06)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (US-3B.06-05-06)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking is in my
                        lane
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking is in my
                        lane
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking is in my
                        lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes. Be mindful of
                        the crosswalk and traffic signals at the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 9506, out 898, 8.47 s

bdd100k_val__c4e92086-e1b8324f | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane city road with traffic moving in the same direction. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a parking or shoulder area on
                        the right. Photo 2 shows a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the left. Do not cross the solid white
                        line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 770, 28.55 s

bdd100k_val__c55da7df-facccafc | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane road in the United States, approaching an intersection or ramp area with
                        overhead signage for San Francisco and San Jose. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to my car that becomes a dotted white line
                        further ahead. Photo 2 shows a broken white line with long dashes and gaps next to my
                        car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line delineating the right edge of the roadway. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows the word 'ONLY' and a right-turn arrow painted in my
                        lane.; arrow:right (full): Photo 2 shows a right-turn arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white line indicates that crossing the lane line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            text:only: The ONLY word marking is used to supplement lane-use arrows in lanes
                        designated for the exclusive use of a single movement. [[US-3B.21-04]]
Step 5  Rule            arrow:right: The right-turn arrow indicates that the mandatory movement for this lane
                        is to turn right. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the right-turn arrow
                        [US-3B.23-01] and ONLY text [US-3B.21-04]
Step 6  turn_left       prohibited: prohibited by the right-turn arrow [US-3B.23-01] and ONLY text
                        [US-3B.21-04]
Step 6  turn_right      allowed: allowed by the right-turn arrow [US-3B.23-01]
Step 6  u_turn          prohibited: prohibited by the right-turn arrow [US-3B.23-01] and ONLY text
                        [US-3B.21-04]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  My lane is a mandatory right-turn lane. I must turn right or change to the left lane
                        if I intend to go straight or turn left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 9506, out 1089, 4.45 s

bdd100k_val__c588eb5e-dfd59d8e | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street with traffic in both directions. The road
                        continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from traffic in the opposite
                        direction. Photo 2 shows the same solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line next to my car, consisting of one visible dash and a gap.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left indicates my lane is the leftmost of my direction | roles: the
                        yellow solid line fits the role of a center line on a two-way road, and the white
                        broken line fits the role of a lane line | markings: no markings in my lane | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            left_boundary: A solid line prohibits crossing. [[US-3A.04-01]]
Step 5  Rule            right_boundary: The white lane line separates traffic flows in the same direction.
                        [[US-3B.06-01]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [US-3A.04-01]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the yellow center
                        line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 910, 5.95 s

bdd100k_val__c59500f0-130d7415 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A two-way urban road with my car traveling in the rightmost lane of its direction.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction of traffic. Photo 2 shows the same double solid yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the roadway. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited
                        for traffic traveling in either direction. [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along my lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking is in my
                        lane
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking is in my
                        lane
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking is in my
                        lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 792, 3.47 s

bdd100k_val__c5b2506d-07e406a6 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane city road with buildings on both sides, heading towards a distant
                        intersection. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the roadway. Photo 2 shows the
                        same solid yellow line next to my car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dash and gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left edge of a one-way street delineates the
                        left-hand edge of the roadway. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the lane line with
                        care is not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
                        [US-3B.09-03]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you cannot cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 778, 16.05 s

bdd100k_val__c74ee988-8f4b380d | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings and parked cars on both sides. The road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line. Photo 2 shows two solid yellow lines side by
                        side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line that is broken near the car and continues ahead. Photo 2
                        shows a broken white line with a dash and a gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line is prohibited for traffic
                        traveling in either direction. [[US-3B.01-06]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-06]
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken white lane line
                        [US-3A.04-01]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the right. Do not cross the double yellow
                        line to the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 9506, out 755, 28.25 s

bdd100k_val__c7c042ec-4986a853 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with several dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with several dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: A through lane-use arrow indicates that the lane is for going
                        straight. [[US-FIG-3B-21]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the through lane-use arrow [US-FIG-3B-21]
Step 6  turn_left       prohibited (correct): prohibited by the through lane-use arrow which does not show a
                        left turn [US-FIG-3B-21]
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the through lane-use arrow which does
                        not show a right turn [US-FIG-3B-21]
Step 6  u_turn          prohibited (correct): prohibited by the through lane-use arrow which does not show a
                        U-turn [US-FIG-3B-21]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:straight_right']), actions False, unsafe [],
                        citation accepted, contradictions []
Tokens                  in 9506, out 927, 14.72 s

bdd100k_val__c96ffe59-1cf2df11 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street heading towards an intersection. (lanes 2, mine
                        2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from another lane to the left.
                        Photo 2 shows a broken white line next to my car, consisting of one visible dash and
                        one gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the right edge of the roadway. Photo 2 shows a
                        solid white line next to my car, which is the edge of the pavement next to a curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and curb
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the right lane. You may continue straight or change lanes to the left, but
                        you cannot cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 788, 27.51 s

bdd100k_val__ca15f699-e51c14c0 | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           A multi-lane road at night with traffic moving in the same direction; the road
                        continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a white dashed line next to my car, with one clear dash and one gap visible.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to my car, with one clear dash and one gap visible.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego lane index agree
                        with the boundaries; there are lane lines on both sides, placing my lane in the middle
                        of three lanes. | roles: the white dashed patterns for both boundaries fit the role of
                        lane lines separating traffic in the same direction. | markings: no markings are
                        present in my lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9506, out 873, 23.12 s

bdd100k_val__fe194677-e2d2ac8c | lane | Test B | gemma-4-31b-it
---------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road, likely near a transit hub or airport, with
                        traffic moving forward. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a white line on the left, but it is mostly obscured by a large pile of
                        snow. Photo 2 shows the road edge is defined by a large pile of snow, with no visible
                        paint next to the car.
                        none none, curb no, edge_line, evidence partial
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a dark road surface with no visible line immediately next to the car, but the
                        broken white line is visible further ahead in Photo 1.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; the
                        left boundary is the road edge (snow pile) and the right is a lane line. | roles: the
                        white dashed line on the right correctly functions as a lane line separating traffic
                        in the same direction. | markings: no markings are present in the lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The left edge of the roadway is delineated, and crossing it is
                        generally prohibited by the physical presence of the snow pile. [US-3B.09-01-02] "If
                        used, edge line pavement markings shall delineate the right or left edges of a
                        roadway. ... Right edge line pavement markings, if used, shall consist of a no"
Step 5  Rule            right_boundary: A broken white line indicates that crossing the lane line with care is
                        permitted. [US-3B.06-05-06] "Where crossing the lane line markings with care is not
                        discouraged or prohibited, the lane line markings shall consist of a normal width
                        broken white line. Wher"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is the edge of the
                        roadway blocked by snow.
Step 6  change_right    allowed (WRONG, label prohibited): allowed: the right boundary is a broken white lane
                        line which permits crossing.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right if needed. Do not move left due to the snow
                        pile at the road edge.
Score                   lane False, boundaries {'left': None, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 9506, out 870, 3.29 s
```
