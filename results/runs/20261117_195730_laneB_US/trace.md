# Reasoning of lane run 20261117_195730_laneB_US

```text
bdd100k_val__b1c66a42-6f7d68ca | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on the right and a sidewalk/median on the
                        left, heading toward a distant intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car and further ahead. Photo 2 confirms
                        a single solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only parked cars and the road edge. Photo
                        2 shows no painted line next to the car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show the word 'SCHOOL' painted in white across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the single lane is bounded by a yellow
                        edge line on the left and no line on the right, consistent with a one-way street or a
                        road where the left edge is delineated. | roles: the yellow solid line on the left
                        fits the role of a left edge line for a one-way street or divided highway. | markings:
                        the word 'SCHOOL' is a guidance marking and does not contradict the boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left delineates the left-hand edge of the
                        roadway. [[US-3B.09-03]]
Step 5  Rule            right_boundary: The right edge of the roadway is typically delineated by a solid white
                        line, but its absence here does not prohibit driving. [[US-3B.09-01-02]]
Step 5  Rule            text:other: Word markings on the pavement are used for regulating, warning, or guiding
                        traffic. [[US-3B.20-01]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow line, and
                        [US-3A.04-01] states a solid line discourages or prohibits crossing.
Step 6  change_right    allowed: allowed: there is no painted line or curb on the right to prohibit leaving
                        the lane.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in the lane and proceed straight. Be alert for children as you are entering a
                        school zone, indicated by the 'SCHOOL' marking on the pavement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 9346, out 997, 14.9 s

bdd100k_val__b1f0efd9-e900c6e5 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. There is a
                        pedestrian crossing and a 'NO U TURN' sign visible ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line that delineates the right edge of the roadway, ending
                        at the intersection. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane_line on the left and an edge_line on the right | roles: white dashed
                        line for lane_line and white solid line for edge_line are consistent with MUTCD |
                        markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed: the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in my lane restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but do
                        not cross the solid white line to the right. Note the 'NO U TURN' sign ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 9346, out 894, 15.01 s

bdd100k_val__b1f4491b-dd8dfed5 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban roadway or highway. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having a lane line on both the left and right
                        sides. | roles: the white dashed lines on both sides fit the role of lane lines
                        separating traffic in the same direction. | markings: there are no markings in my lane
                        to contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or prohibited-movement markings
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 878, 14.55 s

bdd100k_val__b20b69d2-e31380a7 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a roadway that curves to the right, approaching a large sign for Resorts
                        World New York City. The road appears to be a ramp or a dedicated access road. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues forward and follows
                        the curve of the road. Photo 2 confirms a single solid white line immediately to the
                        left of the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right that follows the curve of the road, with
                        a raised curb and grass beyond it. Photo 2 shows the solid white line and the adjacent
                        raised curb next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries; both the left and right boundaries are edge lines, meaning this
                        is a single-lane road. | roles: The white color and solid pattern for both boundaries
                        fit the role of edge lines for a single-lane access road/ramp. | markings: There are
                        no markings in the lane, which is consistent with a simple access road. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: A white longitudinal line delineates the edge of the roadway.
                        [US-3A.03-03-04] "When used, yellow markings for longitudinal lines shall delineate:
                        A. The separation of traffic traveling in opposite directions, B. The left-hand edge
                        of the r"
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02] "If used, edge line pavement markings shall delineate the right or
                        left edges of a roadway. ... Right edge line pavement markings, if used, shall consist
                        of a no"
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid white line, and
                        [US-3A.04-01] states a solid line discourages or prohibits crossing.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white line
                        and a raised curb; [US-3A.04-01] prohibits crossing solid lines and the curb is a
                        physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict continuing straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or marking governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and follow the road as it curves to the right. Lane changes are
                        prohibited on both sides.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 913, 18.17 s

bdd100k_val__b263f57d-1ccf6e51 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road in the United States, approaching an
                        intersection. The road surface is wet from rain. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that continues ahead. Photo 2 shows a
                        white broken line with one visible dash and one gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car that continues to the intersection.
                        Photo 2 shows a solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 3 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line | markings: no markings in my
                        lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited: prohibited: the right boundary is a solid white edge line, and crossing it
                        would mean leaving the roadway [US-3B.09-01-02].
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
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line on your right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 893, 14.39 s

bdd100k_val__b2fbf86d-d5de82a4 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in an urban area, driving straight ahead toward
                        a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line to the left of my car. Photo 2 shows a broken white
                        line with one clear dash and one gap immediately in front of my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line to the right of my car. Photo 2 shows a broken white
                        line with one clear dash and one gap immediately in front of my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right. |
                        roles: White dashed lines are correct for separating lanes of traffic moving in the
                        same direction. | markings: There are no markings in my lane to contradict the
                        boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which permits crossing
                        per [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which permits crossing
                        per [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No markings in my lane restrict going straight, and the
                        boundaries do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking in my lane governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present to govern this
                          action.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 892, 14.32 s

bdd100k_val__b3060c96-d2391b61 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road with trees on both sides, heading toward a
                        distant intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the road. Photo 2 confirms a
                        solid yellow line immediately to the left of the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dash and gap immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is an edge line and
                        the right is a lane line, which agrees with my lane being the leftmost of two lanes in
                        my direction. | roles: The yellow solid line on the left fits the role of a left edge
                        line; the white broken line on the right fits the role of a lane line. | markings: No
                        markings are present in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left edge delineates the left-hand edge of
                        the roadway and indicates driving or passing restrictions left of this marking.
                        [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left edge line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 852, 9.74 s

bdd100k_val__b306fb3f-f02e46cc | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road with a grassy area to the left. The road
                        continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the roadway, bordering a
                        grassy area. Photo 2 confirms a single solid yellow line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a gap and a dash of a white broken line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The yellow solid line on the left fits the role of a left edge
                        line for a divided highway or one-way street. The white broken line on the right fits
                        the role of a lane line separating traffic in the same direction. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: A solid yellow left edge line delineates the left-hand edge of the
                        roadway and indicates driving or passing restrictions left of the marking.
                        [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow edge line
                        [US-3B.09-03] and solid lines discourage or prohibit crossing [US-3A.04-01].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which indicates
                        a permissive condition [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 924, 12.74 s

bdd100k_val__b321c6b6-ab603d42 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with construction barriers on the left. The road continues
                        straight ahead toward a distant intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues forward. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues forward. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 are
                        consistent with having an edge line on the left and a lane line on the right, as there
                        is another lane of the same direction to the right. | roles: The white color and solid
                        pattern fit the roles of edge line and lane line. | markings: No markings in the lane
                        to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway (due
                        to construction/temporary layout), and crossing it is discouraged or prohibited.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A solid white lane line discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white lane line
                        [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
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
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 9346, out 860, 12.16 s

bdd100k_val__b4542860-0b880bb4 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with a traffic
                        signal. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, which continues ahead. Photo 2 shows a
                        solid white line immediately to the right of my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line, and crossing it would mean leaving the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may proceed straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 901, 13.99 s

bdd100k_val__b48c7b5f-800d31b4 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus and other vehicles ahead. The road continues
                        straight toward an intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line that is solid next to my car and remains solid further
                        ahead. Photo 2 shows a single solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line that is solid next to my car and continues as a solid line.
                        Photo 2 shows a single solid white line next to my car. There is a raised curb to the
                        right of this line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right | roles: the yellow solid
                        line fits the role of a center line on a two-way road, and the white solid line with a
                        curb fits the role of a right edge line | markings: no markings in lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            left_boundary: A solid line prohibits crossing. [[US-3A.04-01]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A solid line prohibits crossing. [[US-3A.04-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [US-3A.04-01]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [US-3A.04-01] and the physical curb
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
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 943, 10.15 s

bdd100k_val__b49d6c0d-457e13b3 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, approaching an
                        intersection with a green overhead sign for 'EAST BROOKLYN Business District'. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction of
                        traffic. Photo 2 confirms two yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car, which continues ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 and Photo 2 show a white bicycle symbol painted in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left and
                        solid white line on the right indicate my lane is the rightmost lane of my direction
                        on a two-way road. | roles: The double yellow center line and white edge line are
                        consistent with their roles. | markings: The bicycle symbol indicates a shared lane;
                        it does not restrict movements. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            symbol:bike: The bicycle symbol indicates the lane is shared with bicycles but does
                        not prohibit vehicle movements. [null]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as no marking in my lane restricts it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be mindful of cyclists as indicated by the
                        bicycle symbol in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 9346, out 944, 15.0 s

bdd100k_val__b4d18d1a-193e24a1 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading toward an intersection with a traffic
                        signal. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right. | roles: The
                        white dashed line on the left fits the role of a lane_line; the white solid line on
                        the right fits the role of an edge_line. | markings: No markings are present in the
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line, and crossing it would leave the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in the lane restrict going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 893, 15.08 s

bdd100k_val__b5042634-1034573c | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road passing under a large bridge structure,
                        approaching an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car that continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having white lane lines on both the left and right boundaries. | roles:
                        White dashed lines are consistent with lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No attributes were reported that were not visible. | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in the lane to restrict
                        it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow or prohibited-movement marking
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 852, 13.47 s

bdd100k_val__b54c065e-8b13cfe7 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road, traveling straight ahead toward an intersection.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction of
                        traffic. Photo 2 shows the same double yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line delineating the right edge of the roadway. Photo 2
                        shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left and
                        the white edge line on the right confirm my lane is the only lane for my direction. |
                        roles: The yellow double solid line fits the role of a center line for a no-passing
                        zone, and the solid white line fits the role of a right edge line. | markings: No
                        markings are present in my lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: Crossing the double yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double yellow center line [US-3B.01-04].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 835, 14.44 s

bdd100k_val__b5661732-3684230b | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in the United States, traveling straight ahead
                        toward an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one visible dash and one gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with one visible dash and one gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        sides | roles: the white dashed lines on both sides fit the role of lane lines
                        separating traffic in the same direction | markings: there are no markings in my lane
                        to contradict the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking
                        governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 868, 13.42 s

bdd100k_val__b577827c-28fc9b0d | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching a signalized intersection with a
                        commercial building on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of one visible dash and
                        one gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line that delineates the right edge of the roadway, ending
                        at a curb. Photo 2 shows the same solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line | markings: no markings in my
                        lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line and there is a curb, which prohibits leaving the roadway according to
                        [US-3B.09-01-02].
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
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane;
                        do not cross the right edge line into the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 909, 15.12 s

bdd100k_val__b59e50fa-ca034dd0 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in the United States, traveling straight ahead
                        toward a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one clear dash and one gap immediately in front of
                        the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with one clear dash and one gap immediately in front of
                        the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were observed in the lane, which is consistent with the boundaries. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which permits crossing
                        per [US-3B.06-05-06].
Step 6  change_right    allowed (correct): The right boundary is a broken white line, which permits crossing
                        per [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): No markings restrict going straight, and the boundaries
                        do not govern this action.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right as needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 873, 14.31 s

bdd100k_val__b5cd5f72-32232751 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching an intersection with a traffic signal
                        ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right edge of the road. Photo 2 shows a white
                        solid line next to my car, continuing straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:left (full): Photo 1 and Photo 2 both show a white left-turn arrow painted in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line fits the role of a lane line and the white solid line
                        fits the role of an edge line | markings: the left-turn arrow is consistent with the
                        lane's position as a turn lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition, allowing crossing for
                        lane changes. [[US-3A.04-01]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:left: The left-turn arrow indicates that a left turn is a permissible or
                        mandatory movement from this lane. [[US-3B.23-01]]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a broken white line
                        [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white edge line [US-3B.09-01-02].
Step 6  go_straight     prohibited (correct): prohibited because the lane-use arrow only shows a left turn
                        [US-3B.23-01].
Step 6  turn_left       allowed (WRONG, label prohibited): allowed because the lane-use arrow shows a left
                        turn [US-3B.23-01].
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited because the lane-use arrow does not show
                        a right turn [US-3B.23-01].
Step 6  u_turn          allowed (WRONG, label prohibited): allowed because a left-turn arrow also allows a
                        U-turn unless prohibited by other markings [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a left-turn lane. You may turn left or make a U-turn at the intersection,
                        or change lanes to the left if needed. Do not go straight or turn right from this
                        lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:right']), actions False, unsafe ['turn_left',
                        'u_turn'], citation accepted, contradictions []
Tokens                  in 9346, out 1043, 15.7 s

bdd100k_val__b5f84825-c97df380 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street approaching an intersection. There are multiple lanes of
                        traffic moving in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car that continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white arrow in my lane that points both
                        straight and to the left.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 2 agree with having a lane line on both my left and right | roles: white dashed
                        lines are consistent with lane lines separating traffic in the same direction |
                        markings: the straight-and-left arrow is consistent with a through lane that also
                        allows a left turn | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight_left: The lane-use arrow indicates that both going straight and turning
                        left are permissible movements. [[US-3B.23-01]]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the lane-use arrow [US-3B.23-01]
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the lane-use arrow [US-3B.23-01]
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the lane-use arrow which does not
                        show a right turn [US-3B.23-01]
Step 6  u_turn          allowed (WRONG, label prohibited): allowed as the left-turn arrow also permits U-turns
                        unless a no-U-turn marking is present [US-3B.23-01]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn left. You may also change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_left'], missed ['arrow:straight_right', 'line:stop_line']), actions
                        False, unsafe ['turn_left', 'u_turn'], citation accepted, contradictions []
Tokens                  in 9346, out 990, 15.44 s

bdd100k_val__b65fd3df-87ed965a | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on the right. Ahead is a straight road with
                        parked cars on the right side. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, separating the lane from a parking
                        area. Photo 2 shows the same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a lane line on the left suggests another lane of the same
                        direction, and an edge line on the right marks the roadway boundary. | roles: The
                        white color and solid pattern fit the roles of a lane line and an edge line. |
                        markings: No markings in the lane to check. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid white lane line discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 9346, out 864, 11.74 s

bdd100k_val__b7041acc-6de39959 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway heading towards an overpass. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to the car and further ahead. Photo 2 shows a
                        broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and further ahead. Photo 2 shows a
                        solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and position 2 agree
                        with the boundaries: a lane line on the left and an edge line on the right indicate
                        the car is in the rightmost lane of a 3-lane road (though the count is 3, the
                        boundaries suggest it is the rightmost lane; looking closer at Photo 1, there are 3
                        lanes in the ego direction, and the car is in the rightmost one, making it index 3.
                        Correcting ego_lane_index to 3). | roles: The white broken line on the left fits the
                        role of a lane line, and the white solid line on the right fits the role of an edge
                        line. | markings: No markings in the lane to contradict. | unseen: No | result:
                        corrected ego_lane_index to 3
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which permits
                        crossing per [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, and crossing it would leave the roadway, which is generally prohibited by the
                        role of an edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in the lane restrict going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 962, 14.22 s

bdd100k_val__b7935597-13c4b9dd | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban residential road, heading towards an intersection.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a dark area with a line of parked cars and a curb. Photo 2 shows a
                        raised concrete curb and a dark asphalt edge next to my car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a parking area. Photo 2 shows
                        a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a curb on the left and an edge line on the right. | roles: The
                        white solid line on the right fits the role of a right edge line. | markings: No
                        markings in the lane to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The physical curb prohibits leaving the lane to the left. [null]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a raised curb.
Step 6  change_right    prohibited (contested, label allowed): prohibited: the right boundary is a solid white
                        edge line which discourages or prohibits crossing [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the right edge line into the
                        parking area or the left curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 9346, out 820, 13.54 s

bdd100k_val__b7aa329e-25d68dec | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-lane, two-way residential road, traveling straight ahead. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating the lanes. Photo 2 confirms two
                        solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows a solid
                        white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and position (1)
                        agree with the center line on the left and edge line on the right. | roles: the double
                        solid yellow line fits the role of a center line on a two-way road, and the solid
                        white line fits the role of a right edge line. | markings: no markings in lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 829, 12.33 s

bdd100k_val__b80018ef-3a620af0 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road at night, traveling straight ahead. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a double yellow line separating the road from parked cars and opposite
                        traffic. Photo 2 shows two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the roadway. Photo 2 shows a
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the center line on the left and edge line on the right. | roles: The yellow
                        double solid line fits the role of a center line on a two-way road, and the solid
                        white line fits the role of a right edge line. | markings: No markings in the lane to
                        contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A double yellow line indicates a no-passing zone where crossing the
                        center line is prohibited for traffic in either direction. [[US-3B.01-04]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 840, 13.15 s

bdd100k_val__b84146a1-a5f588ef | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, which continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, which continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right | roles: white dashed
                        lines are consistent with lane lines separating traffic in the same direction |
                        markings: no markings present in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9346, out 811, 13.75 s

bdd100k_val__b8fe9f2b-d63131a3 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with one visible dash and one gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with one visible dash and one gap.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with lane lines separating traffic in the same direction | markings: no
                        markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 827, 14.13 s

bdd100k_val__b91cdc5d-bce994ce | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with buildings on the right. The road continues
                        straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from the right edge of the
                        roadway. Photo 2 shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white broken line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to check. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line, and crossing it would mean leaving the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in my lane restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 895, 10.46 s

bdd100k_val__b928271b-fe5cc5d1 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead toward a signalized
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with a clear dash and gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the rightmost lane. Photo 2
                        shows a white solid line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed and
                        solid lines are consistent with lane_line roles for traffic in the same direction |
                        markings: no markings in lane to contradict | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line indicates that crossing is discouraged.
                        [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a solid
                        white line, which only discourages crossing but does not prohibit it [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane
                        restricting it.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes; note that
                        changing right is discouraged by the solid line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 849, 14.66 s

bdd100k_val__b9429f07-33ae3ff1 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way road with one lane in each direction, approaching an
                        intersection with traffic signals. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating the ego lane from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows a solid
                        white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center line on the left and edge line on the right | roles: the double yellow
                        center line and solid white edge line fit their roles | markings: no markings in lane
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02] and the presence of a curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 813, 13.25 s

bdd100k_val__ba2db972-f29458c8 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a single white dash and a gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line at the right edge of the roadway, followed by a
                        dirt/concrete shoulder. Photo 2 shows the solid white line and the edge of the
                        pavement next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: There are no markings in
                        my lane to check. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive [US-3A.04-01].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line, and
                        crossing it would leave the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 892, 14.65 s

bdd100k_val__ba9f6c98-2a75a096 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-lane, two-way rural road, traveling straight ahead. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a double yellow line separating the road from the opposite direction.
                        Photo 2 shows the same double yellow line next to the car, consisting of two solid
                        yellow lines side by side.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center line on the left and edge line on the right | roles: the double yellow
                        center line and solid white edge line fit their roles | markings: no markings in lane
                        | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 816, 13.2 s

bdd100k_val__bab692c9-4d1f2bdd | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with streetcar tracks embedded in the road. The road
                        continues straight ahead toward a slight incline. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two yellow lines side by side, one solid and one broken. Photo 2
                        confirms a solid yellow line and a broken yellow line side by side, with the broken
                        line closer to my lane.
                        yellow solid_dashed (near line dashed), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and an edge line on the right indicate a single lane of travel
                        in my direction. | roles: the yellow solid-dashed line fits the role of a center line
                        for a two-way left-turn lane, and the solid white line fits the role of a right edge
                        line. | markings: no markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line and broken yellow line delineate a two-way left-
                        turn lane; crossing the broken line is permitted for left-turn maneuvers.
                        [[US-3B.05-01]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed; the left boundary is a broken yellow line
                        (part of a two-way left-turn lane) which is a permissive condition [US-3A.04-01].
Step 6  change_right    prohibited (contested, label allowed): prohibited; the right boundary is a solid white
                        edge line which prohibits crossing [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed; no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable; no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        movement.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        movement.
Step 6  enter_waiting_areaallowed: allowed; the two-way left-turn lane to the left is a marked place to wait
                          for a left turn [US-3B.05-01].
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may go straight or move left into the two-way left-turn
                        lane to prepare for a left turn. Do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['enter_waiting_area allowed without a waiting area or two-way left-
                        turn lane']
Tokens                  in 9346, out 936, 17.29 s

bdd100k_val__bb289fdb-4bc01501 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching a signalized intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having white lane lines on both the left and right. | roles: White dashed
                        lines are consistent with lane lines separating traffic in the same direction. |
                        markings: No markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 807, 14.1 s

bdd100k_val__bb8dba97-3537805c | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane divided highway or one-way street, traveling straight ahead
                        toward a distant intersection or ramp area. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the roadway, next to a metal
                        guardrail. Photo 2 confirms a single solid yellow line immediately to the left of the
                        car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dash and a gap immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the left boundary being an edge_line and the right boundary being a
                        lane_line | roles: the yellow solid left boundary fits the role of a left edge line on
                        a divided highway; the white broken right boundary fits the role of a lane line
                        separating traffic in the same direction | markings: no markings in my lane to check |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow left edge line delineates the left-hand edge of the
                        roadway and indicates driving restrictions left of this marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03] and the
                        physical guardrail.
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not cross the left
                        boundary due to the solid yellow line and guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 882, 14.39 s

bdd100k_val__bbf0f5d7-ea2f1cc3 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, possibly a ramp or an underpass, heading
                        towards an intersection or a merge point. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms a
                        single solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a white broken line with a dash and a gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries: a yellow edge line on the left indicates the leftmost lane of the
                        roadway. | roles: the yellow solid line fits the role of a left edge line, and the
                        white broken line fits the role of a lane line. | markings: no markings present in the
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow left edge line delineates the left-hand edge of the
                        roadway and indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and concrete barrier
                        [US-3B.09-03].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left boundary due to the solid yellow line and barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 862, 13.94 s

bdd100k_val__bbf48d08-b6a11dd8 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road, approaching a T-intersection where the road ahead
                        ends or turns. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 shows the same double yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line that delineates the right edge of the roadway. Photo
                        2 shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and position (1)
                        agree with the center line on the left and edge line on the right | roles: the yellow
                        double solid line fits the role of a center line on a two-way road, and the white
                        solid line fits the role of a right edge line | markings: no markings in lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane. You may proceed straight, but do not cross the center line or the
                        right edge line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 832, 14.34 s

bdd100k_val__bbfe3b4f-5137ff9f | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a crosswalk and
                        traffic signals ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car that continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car that continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 both show a white straight-ahead arrow
                        painted in the lane.; line:crosswalk (full): Photo 1 and Photo 2 show a white zebra-
                        style crosswalk extending across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having broken white lane lines on both the left and right sides. | roles:
                        white dashed lines correctly serve as lane lines separating traffic in the same
                        direction. | markings: the straight-ahead arrow is consistent with the lane's position
                        and the crosswalk is a standard intersection feature. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the permissible movement for
                        this lane is to go straight. [[US-3B.23-01]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern the
                        vehicle's movement options, though the driver must yield to pedestrians. [null]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    allowed (contested, correct): allowed because the right boundary is a broken white
                        line [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): allowed because the lane-use arrow shows a straight-ahead movement
                        [US-3B.23-01].
Step 6  turn_left       prohibited (correct): prohibited because the lane-use arrow only shows straight ahead,
                        prohibiting other movements [US-3B.23-01].
Step 6  turn_right      prohibited (correct): prohibited because the lane-use arrow only shows straight ahead,
                        prohibiting other movements [US-3B.23-01].
Step 6  u_turn          prohibited (correct): prohibited because the lane-use arrow only shows straight ahead,
                        prohibiting other movements [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no marked waiting area or two-way
                          left-turn lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. You may change lanes to the
                        left or right if needed, and be prepared to stop for the traffic signal and yield to
                        pedestrians in the crosswalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 9346, out 1157, 16.3 s

bdd100k_val__bc19c993-c0a0f85f | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading toward an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white broken line next to my car, which becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with one visible dash and gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to my car and continuing ahead. Photo 2 shows a
                        white solid line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 1 and Photo 2 show the word 'ONLY' painted in white in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (2)
                        agree with having lane lines on both sides | roles: white lines on both sides fit the
                        role of lane lines separating traffic in the same direction | markings: the 'ONLY'
                        text indicates a mandatory movement, which is consistent with the solid white boundary
                        on the right separating it from a through lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white line indicates that crossing the lane line with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            text:only: The ONLY word marking designates the lane for the exclusive use of a single
                        movement. [[US-3B.21-04]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white line [US-3B.06-05-06].
Step 6  go_straight     prohibited (contested, label allowed): prohibited because the 'ONLY' marking
                        [US-3B.21-04] indicates a mandatory turn, and no straight arrow is present.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow in my lane to govern this
                        movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow in my lane to govern this
                        movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow in my lane to govern this
                        movement.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a mandatory turn lane. Since no arrow is visible but 'ONLY' is present, you
                        must check for the corresponding arrow or sign to determine the required turn
                        direction; you may change left to a through lane if needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:only'], missed ['text:other']), actions False, unsafe ['change_left'], citation
                        accepted, contradictions ['go_straight decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 9346, out 997, 16.06 s

bdd100k_val__bc9b5bfb-51ebcf39 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching an intersection. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from a two-way left-turn lane.
                        Photo 2 shows the same double yellow line next to my car, consisting of one solid and
                        one broken line.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right. Photo 2 shows a solid white line next
                        to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a center line on the left and an edge line on the right indicate
                        my lane is the rightmost of two lanes in my direction (excluding the TWLTL). | roles:
                        the yellow solid-dashed line fits the role of a center line for a two-way left-turn
                        lane, and the solid white line fits the role of a right edge line. | markings: no
                        markings in my lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line adjacent to my lane prohibits crossing into the
                        two-way left-turn lane except for left-turn maneuvers. [[US-3B.05-01]]
Step 5  Rule            right_boundary: The solid white edge line delineates the right edge of the roadway and
                        prohibits crossing it. [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed; the left boundary is a center line for a
                        TWLTL, and while the solid line discourages crossing, it allows it for left-turn
                        maneuvers per [US-3B.05-01].
Step 6  change_right    prohibited (contested, label allowed): prohibited; the right boundary is a solid white
                        edge line which prohibits crossing per [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed; no marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: not_applicable; no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable; no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable; no arrow governs this movement.
Step 6  enter_waiting_areaallowed: allowed; the two-way left-turn lane to the left is a waiting area for left
                          turns per [US-3B.05-01].
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or move into the two-way
                        left-turn lane to the left if you intend to turn left at the intersection. Do not
                        cross the right edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions ['change_left allowed with the solid line of a solid-and-broken pair
                        nearer my lane', 'enter_waiting_area allowed without a waiting area or two-way left-
                        turn lane']
Tokens                  in 9346, out 948, 15.3 s

bdd100k_val__bcbf328d-953430de | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching a signalized intersection. (lanes 2, mine
                        2, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 shows the same double yellow line next to my car, consisting of two solid
                        yellow lines.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:merge_right (full): Photo 2 shows a white arrow pointing right in my lane.;
                        text:only (full): Photo 2 shows the word 'ONLY' painted in white in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left and
                        solid white line on the right indicate my lane is the rightmost lane of my direction.
                        | roles: The yellow double solid line fits the role of a center line for a no-passing
                        zone; the white solid line fits the role of a right edge line. | markings: The 'ONLY'
                        text and right-turn arrow are consistent with a mandatory turn lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: Crossing the double yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:merge_right: The arrow indicates that a right turn is a permissible or mandatory
                        movement. [[US-3B.23-01]]
Step 5  Rule            text:only: The ONLY marking indicates the lane is designated for the exclusive use of
                        a single movement. [[US-3B.21-04]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04].
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the mandatory right-turn arrow
                        and ONLY text [US-3B.21-04].
Step 6  turn_left       prohibited: prohibited by the mandatory right-turn arrow and ONLY text [US-3B.21-04].
Step 6  turn_right      allowed: allowed by the right-turn arrow [US-3B.23-01] and ONLY text [US-3B.21-04].
Step 6  u_turn          prohibited: prohibited by the mandatory right-turn arrow and ONLY text [US-3B.21-04].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a mandatory right-turn lane. You must turn right at the intersection; lane
                        changes and going straight are prohibited.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:merge_right', 'text:only'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions ['go_straight, turn_left, turn_right, u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 9346, out 1104, 20.07 s

bdd100k_val__bd338426-4b27de63 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead toward a distant
                        intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from another lane to the left.
                        Photo 2 shows the same white broken line next to my car, consisting of several long
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, which continues ahead. Photo 2 shows a
                        white solid line next to my car, bordering a curb and a driveway area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: There are no markings in
                        my lane to conflict with boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and a curb, and [US-3A.04-01] states solid lines discourage or prohibit crossing.
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
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line into the curb area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 908, 15.21 s

bdd100k_val__bd354e59-e5a9e8c6 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the roadway. Photo 2 confirms a
                        solid yellow line immediately to the left of the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from a lane of parked cars. Photo 2
                        shows this line is solid white next to the car and remains solid further ahead.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is an edge line
                        (yellow solid), and the right boundary is a lane line (white solid), which is
                        consistent with being in the leftmost lane of a two-lane road where the right lane is
                        used for parking/stopping. | roles: The yellow solid line on the left fits the role of
                        a left edge line for a divided highway or one-way street. The white solid line on the
                        right fits the role of a lane line separating traffic flows. | markings: No markings
                        are present in the lane, which is consistent with the boundaries. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A solid yellow left edge line delineates the left-hand edge of the
                        roadway and indicates driving or passing restrictions left of this marking.
                        [[US-3B.09-03]]
Step 5  Rule            right_boundary: A solid white lane line discourages crossing. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid yellow
                        edge line [US-3B.09-03].
Step 6  change_right    allowed (contested, correct): allowed: the right boundary is a solid white line which
                        discourages but does not prohibit crossing [US-3B.06-05-06].
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
Advice                  Stay in your lane and proceed straight. Avoid crossing the left yellow edge line; you
                        may change to the right if necessary, though the solid white line discourages it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 934, 13.8 s

bdd100k_val__bd3bd3ab-8e38f822 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, likely near an airport terminal given the
                        overhead signage and architecture, heading toward an area where the road continues
                        straight. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from another lane to the left.
                        Photo 2 shows a white broken line with a visible dash and gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which appears to be the edge of the
                        roadway. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane_line on the left and an edge_line on the right | roles: white dashed
                        line for lane_line and white solid line for edge_line are consistent with MUTCD |
                        markings: no markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a broken
                        white line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed because there are no markings in the lane to
                        restrict it.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 878, 17.77 s

bdd100k_val__bd656105-ed6f8161 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a signalized intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 and Photo 2 show a wide white line extending across the
                        lane at the intersection entrance.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: white dashed
                        lines are consistent with lane lines separating traffic in the same direction. |
                        markings: the stop line is consistent with an approach to a signalized intersection. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            line:stop_line: Vehicles are required to stop behind the stop line in compliance with
                        a traffic control signal. [[US-3B.19-01-02]]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line, which
                        is permissive [US-3A.04-01].
Step 6  change_right    allowed (contested, label prohibited): allowed: the right boundary is a broken white
                        line, which is permissive [US-3A.04-01].
Step 6  go_straight     stop_first (contested, label allowed): stop_first: no arrow restricts movement, but
                        the stop line requires stopping first [US-3B.19-01-02].
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may change lanes to the left or right. Stop behind the
                        stop line and obey the traffic signal before proceeding straight.
Score                   lane False, boundaries {'left': None, 'right': None}, markings False (added
                        ['line:stop_line'], missed ['line:crosswalk']), actions None, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 9346, out 980, 14.52 s

bdd100k_val__bd65dd37-4c3cdf2d | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards an overpass. The road appears to be a
                        highway or a major arterial road. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, which continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car, and a concrete barrier running
                        parallel to it. Photo 2 confirms the solid white line and the adjacent concrete
                        barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white broken line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: No markings were
                        found in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and a concrete barrier, which prohibits leaving the roadway according to
                        [US-3B.09-01-02].
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
                        but you cannot move to the right due to the road edge and barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 917, 13.37 s

bdd100k_val__bd8d420d-ec34c634 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings and a bus stop on the right. The road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which continues ahead. Photo 2 shows a
                        solid white line next to my car, separating the lane from the curb/shoulder area.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and there is a curb, which prohibits leaving the roadway according to
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (correct): allowed: no marking in my lane restricts going straight.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: no arrow or prohibited-
                        movement marking governs this action.
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable: no arrow or prohibited-movement
                        marking governs this action.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: no arrow or prohibited-
                        movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line into the curb area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:straight_right']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 9346, out 916, 15.0 s

bdd100k_val__bdc0dc52-b4d05890 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading toward a signalized intersection. A
                        large bridge structure is visible on the left. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        shows a broken white line with one visible dash and gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        shows a broken white line with one visible dash and gap.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with lane lines separating traffic in the same direction | markings: no
                        markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right. Be mindful of the traffic signal ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 826, 13.32 s

bdd100k_val__bdf6ab8b-3ebe8356 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road, possibly a bridge or highway, with a clear
                        path ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the road, next to a guardrail.
                        Photo 2 confirms this solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road, next to a guardrail.
                        Photo 2 confirms this solid white line immediately to the right of the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries, as both the left and right boundaries are edge lines. | roles:
                        The yellow solid left edge line and white solid right edge line fit the roles of edge
                        lines for a one-way road or divided highway. | markings: There are no markings in the
                        lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid yellow left edge line delineates the left-hand edge of the
                        roadway and indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A solid white right edge line delineates the right-hand edge of the
                        roadway. [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to the left or right are
                        prohibited by the edge lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 863, 28.46 s

bdd100k_val__be0a188d-c47bac51 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a bridge with a steel structure overhead, traveling on a multi-lane
                        road. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows a solid
                        white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane_line on the left and an edge_line on the right | roles: white dashed
                        line for lane_line and white solid line for edge_line are consistent with MUTCD |
                        markings: no markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed because no markings restrict carrying on
                        straight along the lane.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 870, 13.71 s

bdd100k_val__be22a1e1-cbcd82a6 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching an intersection with a
                        traffic signal. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White broken lines
                        are correct for separating traffic flows in the same direction. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  change_right    allowed (correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right. Be mindful of the traffic signal ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 845, 13.98 s

bdd100k_val__be60191c-2dea5114 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a signalized intersection. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several long dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right edge of the roadway. Photo 2 shows a
                        white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line, and crossing it would leave the roadway, which is prohibited by the
                        definition of an edge line in [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no marking in my lane restricts going straight.
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
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 901, 14.79 s

bdd100k_val__be839b4c-fba3ea45 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street in the United States, approaching a crosswalk and
                        intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line to the left of the car, extending forward. Photo 2
                        shows the same white broken line next to the car, consisting of several short dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of the car, which ends as it reaches the
                        crosswalk. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the words 'BUS ONLY' painted in white in the
                        lane ahead of the car.; line:crosswalk (full): Photo 1 and Photo 2 show a white zebra-
                        style crosswalk extending across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a lane line on the left indicates another lane of the same
                        direction, and an edge line on the right indicates the roadway boundary. | roles: The
                        white dashed line on the left fits the role of a lane line, and the white solid line
                        on the right fits the role of an edge line. | markings: The 'BUS ONLY' text indicates
                        a preferential lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            text:bus: The word marking BUS ONLY designates a preferential lane reserved for buses.
                        [[US-3E.03-02]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians to cross the road. [null]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive [US-3A.04-01].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line [US-3B.09-01-02] and there is a curb/sidewalk beyond it.
Step 6  go_straight     prohibited (contested, label allowed): prohibited: the lane is marked 'BUS ONLY'
                        [US-3E.03-02], and my car is an ordinary car, meaning it is not allowed to occupy this
                        lane.
Step 6  turn_left       prohibited: prohibited: the lane is marked 'BUS ONLY' [US-3E.03-02] and there is no
                        turn arrow.
Step 6  turn_right      prohibited: prohibited: the lane is marked 'BUS ONLY' [US-3E.03-02] and there is no
                        turn arrow.
Step 6  u_turn          prohibited: prohibited: the lane is marked 'BUS ONLY' [US-3E.03-02] and there is no
                        U-turn arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a bus-only lane. You must change left into the general traffic lane
                        immediately before proceeding through the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        ['leftmost lane, but a lane line on the left', 'go_straight, turn_left, turn_right,
                        u_turn decided without an arrow or prohibited-movement marking']
Tokens                  in 9346, out 1179, 21.78 s

bdd100k_val__be926190-5293afb9 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with residential houses and trees on the sides. The
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 shows the same double solid yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, but a line of parked cars and a curb.
                        Photo 2 shows the edge of the roadway with no paint and a raised curb.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center line on the left and the edge/curb on the right | roles: the double
                        solid yellow line fits the role of a center line on a two-way road | markings: no
                        markings in lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The raised curb prohibits leaving the roadway to the right. [null]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited: prohibited by the raised curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow line or drive
                        onto the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 9346, out 795, 13.07 s

bdd100k_val__bfa92b30-f12f3535 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way road with one lane in each direction, traveling straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 shows two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows a single
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center line on the left and edge line on the right | roles: the double yellow
                        center line and solid white edge line fit their roles | markings: no markings in lane
                        to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 808, 8.74 s

bdd100k_val__bfe2b817-505676ef | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way residential road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows two yellow lines side by side, both solid, extending forward. Photo 2
                        confirms two solid yellow lines next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a single solid white line on the right. Photo 2 confirms a single solid
                        white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The double yellow line on the left and
                        solid white line on the right indicate my lane is the only lane for my direction of
                        travel. | roles: The double yellow center line and white edge line are consistent with
                        a two-way road with one lane per direction. | markings: No markings are present in the
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 830, 13.92 s

bdd100k_val__bff4bb8b-152c6105 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway heading towards a distant overpass or intersection
                        area. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a metal guardrail. Photo 2 confirms a solid
                        yellow line and the presence of a metal guardrail immediately to the left of the line.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane to the right.
                        Photo 2 shows a stretch of this broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The yellow solid edge line on the left and white dashed lane line
                        on the right fit their respective roles for a highway. | markings: No markings were
                        observed in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway and
                        indicates driving restrictions left of this marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow edge line
                        [US-3B.09-03] and a physical guardrail.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line
                        [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left edge line or guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 879, 14.2 s

bdd100k_val__c02d18db-f5278de0 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with an elevated railway structure on the left.
                        The road continues straight ahead toward a distant intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to my car that continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car that continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having white lane lines on both the left and right | roles: white
                        dashed lines are consistent with lane lines separating traffic in the same direction |
                        markings: no markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 834, 12.41 s

bdd100k_val__c068a67b-03b6e200 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a residential two-way city street. The road ahead is straight with no
                        immediate intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow broken line extending forward. Photo 2 shows a yellow broken
                        line next to the car, consisting of long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line extending forward. Photo 2 shows a white solid line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left and
                        white edge line on the right agree with my lane being the only lane of my direction. |
                        roles: The yellow dashed line fits the role of a center line for passing, and the
                        white solid line fits the role of a right edge line. | markings: No markings in the
                        lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A normal width broken yellow line permits crossing the center line for
                        passing with care. [[US-3B.01-04]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken yellow line, which permits
                        crossing for passing per [US-3B.01-04].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, and crossing it would move the car off the roadway per [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a single lane of travel. You may go straight or cross the center line to
                        pass oncoming traffic with care, but do not cross the right edge line into the parking
                        area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 877, 9.91 s

bdd100k_val__c07733d0-7525eae7 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead on a road
                        with a concrete barrier on the left and right. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, continuing forward. Photo 2
                        confirms a single solid yellow line next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing forward. Photo 2 shows a
                        broken white line with one visible dash and gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a yellow edge line on the left indicates the leftmost lane of the
                        direction of travel. | roles: the yellow solid line fits the role of a left edge line
                        on a divided highway, and the white broken line fits the role of a lane line
                        separating traffic in the same direction. | markings: no markings in the lane to
                        contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left edge of a divided highway delineates
                        the left-hand edge of the roadway and indicates driving restrictions left of the
                        marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03] and the
                        physical concrete barrier.
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow in view.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow in view.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or turn arrow in view.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right. Do not cross the left boundary due to
                        the solid yellow line and concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 873, 15.02 s

bdd100k_val__c07733d0-aebb8786 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car that continues ahead. Photo 2
                        confirms a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car that continues ahead. Photo 2
                        confirms a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are correct for separating lanes of traffic moving in the same direction | markings:
                        no markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 816, 13.72 s

bdd100k_val__c0e7271a-a3c8d55f | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading straight. There are no intersections or
                        ramps immediately ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a concrete barrier. Photo 2
                        shows the solid white line next to my car and the concrete barrier immediately to its
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and a concrete barrier, which prohibits leaving the roadway according to
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you cannot move to the right due to the road edge and barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 907, 14.56 s

bdd100k_val__c0efbe92-2ee3e529 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides, heading towards a straight
                        stretch of road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with one visible dash and one gap
                        next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the lane from a parking area. Photo 2
                        shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the boundaries: a lane line on the left suggests another lane of the same
                        direction, and an edge line on the right marks the roadway boundary. | roles: the
                        white color and patterns (dashed left, solid right) fit the roles of a lane line and
                        an edge line respectively. | markings: no markings in lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white right edge line delineates the right-hand edge of the
                        roadway. [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, label allowed): prohibited because the right boundary is a
                        solid white edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane to restrict
                        it.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the left. Do not cross the solid white
                        line on the right into the parking area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 9346, out 875, 13.26 s

bdd100k_val__c100db13-71b423e5 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead toward an
                        overhead sign indicating exits for Woodhaven Blvd and Queens Blvd. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one clear dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right, followed by a concrete barrier. Photo 2
                        shows a white solid line next to the car and a concrete barrier immediately to its
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        fits the role of a right edge line. | markings: no markings in lane to check. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and a concrete barrier, which prohibits leaving the roadway according to
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in the lane restrict going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you cannot move to the right due to the road edge and barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 906, 13.81 s

bdd100k_val__c107c2f1-b2b8fff0 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane divided highway. The road ahead is straight with
                        no immediate intersections or ramps visible. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating the roadway from a concrete barrier.
                        Photo 2 shows two solid yellow lines side by side next to the car.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundaries: a double yellow edge line on the left and a white lane
                        line on the right. | roles: the double yellow line fits the role of a left edge line
                        on a divided highway, and the broken white line fits the role of a lane line
                        separating traffic in the same direction. | markings: no markings are present in the
                        lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway and
                        indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow edge line [US-3B.09-03].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change
                        lanes to the right, but you must not cross the double yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 878, 12.45 s

bdd100k_val__c121b93f-b2ee73d4 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead toward a distant
                        intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from another lane to the left.
                        Photo 2 shows the same white broken line next to my car, consisting of one visible
                        dash and one gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating my lane from the right edge of the
                        roadway. Photo 2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, and crossing it would mean leaving the roadway, which is prohibited by the
                        definition of an edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no marking in my lane restricts going straight.
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
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 908, 15.08 s

bdd100k_val__c1589305-200e315b | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in the United States, approaching a crosswalk
                        and an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car, which continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car, which continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a wide white line extending across the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right | roles: white dashed
                        lines are correct for separating lanes of traffic moving in the same direction |
                        markings: the crosswalk is a standard marking across the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern the seven
                        vehicle actions. [null]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    allowed (contested, correct): allowed: the right boundary is a broken white line,
                        which is permissive according to [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed: no arrow in my lane restricts this movement.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right. Be mindful of the crosswalk ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions None, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 9346, out 970, 15.21 s

bdd100k_val__c15c29a5-74788f46 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on the right and a park area with trees on
                        the left. The road continues straight ahead toward a distant intersection. (lanes 1,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line separating my lane from a park area/shoulder. Photo
                        2 shows the same solid yellow line next to my car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a parking/stopping area on
                        the right. Photo 2 shows the same solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a yellow edge line on the left and a white edge line on the right
                        indicate a single-lane roadway. | roles: The yellow solid line on the left fits the
                        role of a left edge line for a one-way street or divided highway. The white solid line
                        on the right fits the role of a right edge line. | markings: There are no markings in
                        the lane to contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left edge of a one-way street delineates the
                        left-hand edge of the roadway. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03] and the
                        general rule that solid lines discourage or prohibit crossing [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line
                        [US-3B.09-01-02] and the general rule that solid lines discourage or prohibit crossing
                        [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited by the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 945, 14.83 s

bdd100k_val__c1627cd8-d8c10968 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a solid yellow line
                        next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a broken white line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 1 and Photo 2 both show the word 'ONLY' painted in white in
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and a lane line on the right indicate the car is in the
                        leftmost lane of its direction. | roles: the yellow solid center line and white dashed
                        lane line fit their roles. | markings: the 'ONLY' text is present, but there is no
                        accompanying arrow visible in the lane to specify the movement. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            right_boundary: A broken white lane line indicates a permissive condition for
                        crossing. [[US-3B.06-05-06]]
Step 5  Rule            text:only: The ONLY word marking is used to supplement lane-use arrows in lanes
                        designated for the exclusive use of a single movement. [[US-3B.21-04]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow center line
                        [US-3B.01-01], and crossing it into opposite traffic is prohibited.
Step 6  change_right    allowed (contested, correct): allowed: the right boundary is a broken white line
                        [US-3B.06-05-06], which indicates a permissive condition.
Step 6  go_straight     not_applicable (WRONG, label allowed): not_applicable: there is no arrow in the lane
                        to govern this movement, and the 'ONLY' text without an arrow is ambiguous.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable: there is no arrow in the
                        lane to govern this movement.
Step 6  turn_right      not_applicable (WRONG, label prohibited): not_applicable: there is no arrow in the
                        lane to govern this movement.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable: there is no arrow in the
                        lane to govern this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a lane marked 'ONLY', but the specific mandatory movement is not clear due
                        to the missing arrow. You may change lanes to the right if needed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 9346, out 1006, 19.6 s

bdd100k_val__c173438f-01b0b013 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway at night, moving straight ahead. (lanes
                        2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of a dash and a gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my lane. Photo 2 shows a solid white
                        line next to my car, continuing straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white broken line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, and crossing it would mean leaving the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 891, 14.96 s

bdd100k_val__c1b3582d-b9c87c82 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a single broken white line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line that delineates the right edge of the roadway. Photo
                        2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white broken line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in the lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line, and crossing the edge of the roadway is generally prohibited.
Step 6  go_straight     allowed (contested, correct): allowed: no marking in my lane restricts going straight.
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
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 878, 14.11 s

bdd100k_val__c1b5a91c-9e402e78 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or urban arterial road. The road
                        continues straight ahead with no immediate intersection or ramp visible. (lanes 3,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, continuing straight ahead. Photo 2
                        confirms a single solid yellow line immediately to the left of the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, with several dashes and gaps
                        visible. Photo 2 shows one white dash and one gap immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is an edge line
                        (yellow solid), and the right boundary is a lane line (white dashed), which is
                        consistent with being in the leftmost lane of a multi-lane road. | roles: The yellow
                        solid line on the left fits the role of an edge line for a divided highway or one-way
                        street. The white dashed line on the right fits the role of a lane line separating
                        traffic in the same direction. | markings: No markings are present in the lane, which
                        is consistent with a through lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway and
                        indicates driving restrictions left of this marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited; the left boundary is a solid yellow edge line
                        [US-3B.09-03] and solid lines discourage or prohibit crossing [US-3A.04-01].
Step 6  change_right    allowed (correct): allowed; the right boundary is a broken white lane line, which
                        indicates a permissive condition [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed; no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 936, 15.9 s

bdd100k_val__c2021c8c-474a8eda | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in the United States, driving straight ahead
                        toward an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that continues ahead. Photo 2 shows a
                        white broken line with one visible dash and one gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car that continues ahead. Photo 2 shows a
                        white broken line with one visible dash and one gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having white lane lines on both the left and right | roles: white
                        dashed lines are correct for separating lanes of traffic moving in the same direction
                        | markings: no markings are present in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 844, 14.34 s

bdd100k_val__c264943c-5e493c9f | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street with buildings on both sides, approaching an
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction of
                        traffic. Photo 2 shows the same double yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from a parking or auxiliary lane on the
                        right. Photo 2 shows a solid white line next to my car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 both show the word 'SCHOOL' painted in white
                        across my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the double yellow line on the left
                        indicates my lane is the leftmost of my direction, and the white line on the right
                        indicates another lane or area to the right; this agrees with lane_count 2 and
                        ego_lane_index 1. | roles: the double yellow center line and solid white lane line fit
                        their assigned roles. | markings: the word 'SCHOOL' is a guidance marking and does not
                        contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double yellow line indicates that crossing the center line for
                        passing is prohibited. [[US-3B.01-04]]
Step 5  Rule            right_boundary: A solid white line discourages crossing into the adjacent lane.
                        [[US-3B.06-05-06]]
Step 5  Rule            text:other: The word 'SCHOOL' is informative, warning the driver of a school zone.
Step 6  change_left     prohibited (correct): prohibited by the double yellow center line [US-3B.01-04].
Step 6  change_right    allowed (contested, label prohibited): allowed but discouraged by the solid white lane
                        line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be alert for children and pedestrians as you
                        are entering a school zone.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 945, 14.42 s

bdd100k_val__c28b60fb-a5e9b955 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane divided highway, traveling straight ahead on a road with a
                        concrete barrier to the left. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms a
                        single solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a single white dash and a gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a yellow edge line on the left indicates the leftmost lane of the
                        roadway. | roles: the yellow solid edge line and white broken lane line fit their
                        respective roles for a divided highway. | markings: no markings present in the lane. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway on a
                        divided highway. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow edge line next
                        to a concrete barrier, and [US-3A.04-01] states solid lines discourage or prohibit
                        crossing.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which
                        [US-3A.04-01] defines as a permissive condition.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict continuing straight in the
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left edge line into the barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 862, 14.48 s

bdd100k_val__c2fb790e-4cd5a630 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides, approaching an intersection.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and further ahead. Photo 2 shows a
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:only (full): Photo 2 shows a white word 'ONLY' painted in the lane to the left of
                        my car, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (2) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white color and patterns (dashed left, solid right) fit the roles of
                        lane_line and edge_line. | markings: the 'ONLY' text is in the adjacent left lane, not
                        my lane; my lane has no markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, label allowed): prohibited: the right boundary is a solid white
                        edge line, and crossing it would leave the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no marking in my lane restricts going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change left into the adjacent
                        lane, which is a mandatory turn lane (marked 'ONLY').
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:only'], missed []), actions None, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 9346, out 964, 15.45 s

bdd100k_val__c300fd4b-8ff92c2d | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road under an overpass, heading towards an intersection. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a single solid yellow
                        line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a concrete barrier on the right. Photo 2 shows the concrete barrier
                        immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a yellow edge line on the left and a barrier on the right
                        indicate a single-lane roadway. | roles: The yellow solid line on the left fits the
                        role of a left edge line for a one-way street or divided highway. The concrete barrier
                        on the right fits the role of a right edge boundary. | markings: No markings are
                        present in the lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left delineates the left-hand edge of the
                        roadway and indicates driving restrictions left of this marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: The right edge of the roadway is delineated by the boundary; crossing
                        it is prohibited by the physical barrier. [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03].
Step 6  change_right    prohibited (correct): prohibited by the concrete barrier.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Lane changes to either side are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 835, 28.54 s

bdd100k_val__c3026ac7-8105e9a9 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection with a traffic
                        signal ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which becomes a solid white line
                        further ahead as it approaches the intersection. Photo 2 shows the broken white line
                        next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        correctly serve as lane lines separating traffic in the same direction | markings: no
                        markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right. Be mindful of the traffic signal ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 828, 14.4 s

bdd100k_val__c308561a-1b698bb4 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a sound wall on the right, heading towards
                        a clear stretch of road. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, bordering a shoulder and a concrete
                        barrier/wall. Photo 2 shows the solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane_line on the left and an edge_line on the right | roles: the white
                        dashed line fits the role of a lane_line and the white solid line fits the role of an
                        edge_line | markings: no markings present in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and there is a physical barrier, and [US-3A.04-01] states solid lines discourage
                        or prohibit crossing.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line into the shoulder.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 905, 13.69 s

bdd100k_val__c31d9531-694298f0 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or arterial road with a concrete barrier
                        on the right. The road continues straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a series of white dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a concrete barrier. Photo 2 shows a solid
                        white line and the edge of the concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having a lane_line on the left and an edge_line on the right, as there is
                        one lane to the left and no lanes to the right. | roles: The white dashed line on the
                        left fits the role of a lane_line separating traffic in the same direction. The white
                        solid line on the right fits the role of an edge_line delineating the right edge of
                        the roadway. | markings: No markings are present in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is a
                        permissive condition [US-3A.04-01].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line [US-3B.09-01-02] and there is a physical concrete barrier.
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
Advice                  You can continue straight or change lanes to the left. Do not attempt to move to the
                        right as there is a concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 930, 15.14 s

bdd100k_val__c3321660-e6b60390 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that continues ahead. Photo 2 shows a
                        white broken line with one visible dash and one gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car that continues ahead. Photo 2 shows a
                        white broken line with one visible dash and one gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 show a white straight-ahead arrow in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right | roles: white dashed
                        lines are consistent with lane lines separating traffic in the same direction |
                        markings: the straight-ahead arrow is consistent with a through lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the permissible movement for
                        this lane is to go straight. [[US-3B.23-01]]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06]
Step 6  change_right    allowed (contested, correct): allowed because the right boundary is a broken white
                        line [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed because the lane-use arrow shows straight movement
                        [US-3B.23-01]
Step 6  turn_left       prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement [US-3B.23-01]
Step 6  turn_right      prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement [US-3B.23-01]
Step 6  u_turn          prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement [US-3B.23-01]
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may go straight or change lanes, but you cannot turn
                        left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 9346, out 998, 17.49 s

bdd100k_val__c3bb4925-f78e285a | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, likely a bridge or overpass, heading straight
                        toward a distant urban area. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line delineating the left edge of the roadway. Photo 2
                        shows the same solid yellow line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is an edge line and
                        the right is a lane line, which agrees with my lane being the leftmost of 3 lanes. |
                        roles: Yellow solid edge line on the left and white broken lane line on the right fit
                        their roles. | markings: No markings in lane, consistent with boundaries. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A solid yellow left edge line delineates the left-hand edge of the
                        roadway and indicates driving restrictions left of the marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
                        [US-3B.09-03].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this.
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 835, 14.01 s

bdd100k_val__c4057c0c-000a6aaf | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street in the United States, approaching an intersection with a
                        stop sign visible on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line that is solid next to my car and remains solid further
                        ahead. Photo 2 confirms a single solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car, which becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with one visible dash and one gap
                        next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:stop (full): Photo 2 shows the letters 'ST' of a word painted in white in my
                        lane; Photo 1 shows the full word 'STOP'.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and a lane line on the right indicate my lane is the leftmost
                        of my direction in a multi-lane setup, but since only one lane is counted for my
                        direction at the bottom, it is the only lane. | roles: the yellow solid line fits the
                        role of a center line; the white broken line fits the role of a lane line. | markings:
                        the STOP text is consistent with the approaching intersection. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            text:stop: The STOP marking requires the vehicle to come to a full stop.
                        [[US-3B.19-01-02]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid yellow
                        center line, and [US-3B.01-04] prohibits crossing center lines in no-passing zones
                        (solid lines discourage/prohibit crossing).
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which
                        [US-3A.04-01] defines as a permissive condition.
Step 6  go_straight     stop_first (contested, correct): stop_first: going straight is allowed as no arrow
                        restricts it, but the text:stop marking requires a full stop first per
                        [US-3B.19-01-02].
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You must come to a full stop at the STOP marking before proceeding straight. You may
                        change lanes to the right if clear, but do not cross the yellow center line to the
                        left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['rightmost lane, but
                        a lane line on the right']
Tokens                  in 9346, out 1076, 17.51 s

bdd100k_val__c47fb4ff-92db68d6 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road passing under a bridge, with a concrete wall on
                        the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to the car that continues ahead. Photo 2
                        confirms a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, with a concrete wall and curb
                        immediately to its right. Photo 2 confirms the solid white line and the raised
                        concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white broken line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings in lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and a physical curb, which prohibits leaving the roadway according to
                        [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 888, 13.57 s

bdd100k_val__c4b3ab99-a4a09eeb | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a stone wall on the right and an overpass
                        on the left, heading toward a distant intersection. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line extending from the bottom to the distance. Photo 2
                        shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego_lane_index
                        (3) agree with the right boundary being an edge_line and the left boundary being a
                        lane_line. | roles: the white color and dashed/solid patterns fit the roles of
                        lane_line and edge_line respectively. | markings: no markings in lane to check. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, and crossing it would leave the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in the lane restrict going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 889, 11.55 s

bdd100k_val__c4b3ce3d-cdc056ce | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line on the right, followed by a shoulder and a metal
                        guardrail. Photo 2 shows a white solid line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: no markings in my
                        lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, and crossing it to enter the shoulder is generally prohibited by its role as a
                        roadway edge [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in the lane restrict going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line on the right into the shoulder.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 912, 14.76 s

bdd100k_val__c4e97226-7be7eef5 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a brick wall on the right; the road
                        continues straight ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to my car that continues ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car that continues ahead, bordering a
                        narrow shoulder/curb area. Photo 2 shows a solid white line and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white broken line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings in my lane to
                        check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line and a curb, which prohibits leaving the roadway according to
                        [US-3B.09-01-02].
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
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line into the curb area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 901, 15.28 s

bdd100k_val__c4ee0cc4-b7af9602 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, traveling straight ahead. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a dark area to the left with no visible paint, bordered by a raised
                        curb. Photo 2 confirms the presence of a raised curb and no painted line next to the
                        car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white dash and a gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge line and the right boundary being a lane
                        line. | roles: The white dashed line on the right fits the role of a lane line
                        separating traffic in the same direction. | markings: No markings were observed in the
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The raised curb marks the edge of the roadway and prohibits leaving the
                        roadway to the left. [null]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a raised curb.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which is
                        permissive per [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 9346, out 822, 13.71 s

bdd100k_val__c5588233-b03622f3 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane divided highway, traveling straight ahead on a road
                        bordered by a concrete barrier on the left. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms a
                        single solid yellow line immediately to the left of the lane, adjacent to the concrete
                        barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a stretch of this broken white line with one visible dash and one gap next to
                        the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (1) agree with the boundaries: a yellow edge line on the left and a white lane line on
                        the right. | roles: the yellow solid edge line and white dashed lane line fit their
                        respective roles for a divided highway. | markings: no markings are present in the
                        lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid yellow line delineates the left-hand edge of the roadway on a
                        divided highway. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow edge line and a
                        concrete barrier, and [US-3A.04-01] states solid lines discourage or prohibit
                        crossing.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which
                        [US-3A.04-01] defines as a permissive condition.
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
Advice                  You are in the leftmost lane of a divided highway. You may continue straight or change
                        lanes to the right, but do not cross the left edge line or the concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 905, 14.78 s

bdd100k_val__c561cb9a-aafc0bad | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a signalized intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a broken white line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: white lines on both
                        sides are consistent with separating traffic in the same direction. | markings: the
                        straight-ahead arrow is consistent with a through lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white line indicates that crossing the lane line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line indicates that crossing the lane line is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the permissible movement for
                        this lane is to go straight. [[US-3B.23-01]]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    allowed (contested, label prohibited): allowed because the right boundary is a solid
                        white line, which only discourages crossing [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): allowed because the lane-use arrow shows straight movement
                        [US-3B.23-01].
Step 6  turn_left       prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement [US-3B.23-01].
Step 6  turn_right      prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement [US-3B.23-01].
Step 6  u_turn          prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight through the intersection. You may change lanes to the
                        left if needed.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['text:only']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 975, 15.09 s

bdd100k_val__c65c2462-96e8ae92 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or urban arterial road, traveling under an
                        overpass. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a concrete barrier. Photo 2
                        shows a solid white line next to the car and a concrete barrier immediately to its
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings in the lane
                        to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line [US-3B.09-01-02] and there is a physical concrete barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move right due to the edge line and concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 891, 13.84 s

bdd100k_val__c66d2237-f9c0a1ef | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having white lane lines on both the left and right boundaries. | roles: The
                        white color and dashed pattern fit the role of lane lines separating traffic in the
                        same direction. | markings: There are no markings in the lane to contradict the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line
                        [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or prohibited-movement marking in
                        the lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 9346, out 843, 12.97 s

bdd100k_val__c68f8fd2-61681484 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban highway heading towards an area with overhead signs
                        and potential exits. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2 shows
                        a white broken line with one visible dash and one gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2 shows
                        a white broken line with one visible dash and one gap.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with lane lines separating traffic in the same direction | markings: no
                        markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 814, 14.19 s

bdd100k_val__c6d77a40-03423c96 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings and trees on both sides, heading towards a
                        distant intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from another lane to the left.
                        Photo 2 shows a single white dash and a gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a parking or shoulder area.
                        Photo 2 shows a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and my position as
                        lane 2 agree with having a lane line on the left and an edge line on the right |
                        roles: the white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line | markings: no markings in my
                        lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white edge line [US-3B.09-01-02] and crossing it would leave the roadway.
Step 6  go_straight     allowed (contested, correct): allowed because no markings in my lane restrict it.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow or prohibited-movement
                        marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 889, 13.82 s

bdd100k_val__c6dca574-6e641016 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with parked cars on the left and a sidewalk on the
                        right. The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 shows two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a concrete curb on the right. Photo 2 shows a raised concrete curb
                        immediately to the right of the lane.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge curb on the right | roles: the double
                        yellow line fits the role of a center line on a two-way road, and the curb fits the
                        role of an edge line | markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The right edge of the roadway is delineated by the curb.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited (correct): prohibited by the raised curb [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines or drive
                        onto the curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 821, 13.9 s

bdd100k_val__c6dcc1a9-0fa80e62 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway, traveling straight ahead on a bridge or elevated
                        roadway. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of long white dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right | roles: the white color
                        and dashed pattern of both boundaries fit the role of lane lines separating traffic in
                        the same direction | markings: there are no markings in my lane to contradict |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [US-3B.06-05-06] "Where crossing the lane line markings
                        with care is not discouraged or prohibited, the lane line markings shall consist of a
                        normal width broken white line. Wher"
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [US-3B.06-05-06] "Where crossing the lane line markings
                        with care is not discouraged or prohibited, the lane line markings shall consist of a
                        normal width broken white line. Wher"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (US-3B.06-05-06)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (US-3B.06-05-06)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 863, 28.43 s

bdd100k_val__c6e1c974-906461f4 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a white solid line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car and continuing ahead. Photo 2 shows a
                        white solid line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow.; text:only (full):
                        Photo 2 shows the white word 'ONLY' painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; there is a lane to the left and a lane to the right. | roles: the
                        white color and patterns fit the role of lane lines separating traffic in the same
                        direction. | markings: the straight arrow and 'ONLY' text are consistent with a
                        mandatory through lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white line indicates that crossing the lane line with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line indicates that crossing the lane line is
                        discouraged. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the permissible movement in
                        this lane is to go straight. [[US-3B.23-01]]
Step 5  Rule            text:only: The 'ONLY' marking supplements the lane-use arrow to designate the lane for
                        the exclusive use of a single movement. [[US-3B.21-04]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    allowed (correct): allowed because the right boundary is a solid white line, which
                        only discourages crossing [US-3B.06-05-06].
Step 6  go_straight     allowed (correct): allowed because the lane-use arrow shows straight movement
                        [US-3B.23-01].
Step 6  turn_left       prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement and is marked 'ONLY' [US-3B.21-04].
Step 6  turn_right      prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement and is marked 'ONLY' [US-3B.21-04].
Step 6  u_turn          prohibited (correct): prohibited because the lane-use arrow only shows straight
                        movement and is marked 'ONLY' [US-3B.21-04].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a mandatory through lane. You may go straight or change lanes, but you
                        cannot turn left or right from this lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 1116, 15.53 s

bdd100k_val__c6ed8102-2bbcbcc2 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban roadway, approaching an area with overhead
                        structures and signage. The road continues straight ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car, and a metal guardrail running
                        parallel to it. Photo 2 shows the white solid line and the guardrail.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 3
                        agree with the right boundary being an edge_line and the left boundary being a
                        lane_line | roles: the white dashed line on the left fits the role of a lane_line, and
                        the white solid line on the right fits the role of an edge_line | markings: no
                        markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and a physical barrier (guardrail), which prohibits leaving the roadway according
                        to [US-3B.09-01-02].
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
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line into the guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 912, 15.5 s

bdd100k_val__c85416bd-db975d94 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        intersections or ramps immediately visible in the foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car that continues ahead. Photo 2
                        confirms a white solid line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings are present
                        in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, and crossing it would leave the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict carrying on straight along
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
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line on your right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 897, 15.83 s

bdd100k_val__c8a7a62d-e58e7297 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides, approaching an intersection.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line that is solid next to my car and remains solid further
                        ahead. Photo 2 shows a single solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, but a raised curb forming the edge of the
                        road. Photo 2 shows the road surface meeting a concrete curb.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show the word 'SCHOOL' painted in white across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge curb on the right | roles: the yellow solid
                        line fits the role of a center line on a two-way road, and the curb fits the role of
                        an edge boundary | markings: the word 'SCHOOL' is a guidance marking and does not
                        contradict the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow center line separates traffic traveling in opposite
                        directions. [[US-3B.01-01]]
Step 5  Rule            left_boundary: A solid line prohibits crossing. [[US-3A.04-01]]
Step 5  Rule            right_boundary: The right edge of the roadway is delineated by the curb.
                        [[US-3B.09-01-02]]
Step 5  Rule            text:other: The word 'SCHOOL' is used for the purpose of warning or guiding traffic.
                        [[US-3B.20-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [US-3A.04-01]
Step 6  change_right    prohibited (correct): prohibited by the physical curb [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be alert for children as you are entering a
                        school zone.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 981, 14.04 s

bdd100k_val__c8e01103-9ff8595d | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street approaching an intersection. There is a crosswalk and a
                        traffic signal ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car that continues forward. Photo 2
                        confirms a single solid white line immediately to the left of the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and a curb. Photo 2 shows a solid
                        white line and a raised curb to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in the
                        lane.; line:crosswalk (full): Photo 1 shows a white crosswalk line across the lane
                        ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and index 1 agree
                        with the left boundary being a lane line (separating from another lane of same
                        direction) and the right boundary being an edge line with a curb. | roles: The white
                        solid lines fit the roles of lane_line and edge_line respectively. | markings: The
                        straight-ahead arrow is consistent with the lane's position and boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: A solid white lane line discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that going straight is a
                        permissible movement. [[US-3B.23-01]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern vehicle
                        movement actions other than yielding. [null]
Step 6  change_left     prohibited (contested, label allowed): prohibited by the solid white lane line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line and
                        curb [US-3B.09-01-02].
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [US-3B.23-01].
Step 6  turn_left       prohibited (correct): prohibited because the lane-use arrow only shows straight
                        [US-3B.23-01].
Step 6  turn_right      prohibited (correct): prohibited because the lane-use arrow only shows straight
                        [US-3B.23-01].
Step 6  u_turn          prohibited (correct): prohibited because the lane-use arrow only shows straight
                        [US-3B.23-01].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight through the intersection. Do not change
                        lanes or turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['leftmost lane, but a
                        lane line on the left']
Tokens                  in 9346, out 1084, 20.01 s

bdd100k_val__c909551e-fb24caeb | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2 shows
                        a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2 shows
                        a white broken line with one visible dash and one gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with lane lines separating traffic in the same direction | markings: no
                        markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 818, 13.67 s

bdd100k_val__c90b5398-8d49f2f2 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead toward an area where
                        the road layout changes or an intersection begins. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of several short dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which continues forward. Photo 2 shows
                        a solid white line immediately to the right of my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white broken line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken white
                        line, which is permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        edge line, and crossing it would mean leaving the roadway [US-3B.09-01-02].
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
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 907, 17.44 s

bdd100k_val__c90c8198-f73aed79 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings and parked cars on the right. Ahead
                        is a straight stretch of road with no immediate intersection or ramp. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a double yellow line separating my lane from the opposite direction.
                        Photo 2 shows two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line separating my lane from the parking area/shoulder. Photo 2
                        shows a solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and position (1)
                        agree with the center line on the left and edge line on the right | roles: the double
                        yellow center line and solid white edge line fit their roles | markings: no markings
                        in lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: Crossing the double solid yellow center line for passing is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [US-3B.01-04]
Step 6  change_right    prohibited: prohibited by the solid white edge line [US-3B.09-01-02]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection in view
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection in view
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection in view
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 822, 13.52 s

bdd100k_val__c9283177-4ac407c3 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with buildings on the right and a guardrail on
                        the left, heading towards a distant intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a guardrail. Photo 2 confirms a single solid
                        yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with a clear gap and dash next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The left boundary is an edge line and
                        the right is a lane line, which agrees with my lane being the leftmost of two lanes in
                        my direction. | roles: The yellow solid edge line on the left and white broken lane
                        line on the right fit their roles. | markings: No markings are present in the lane. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left edge of a roadway indicates the left-
                        hand edge and restricts driving to the left of it. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the left boundary.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 849, 13.34 s

bdd100k_val__c94d8213-1f593522 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection or a ramp area with
                        a concrete barrier on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a white solid line
                        further ahead. Photo 2 shows a white broken line with one visible dash and one gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car and further ahead, with a concrete
                        barrier immediately to its right. Photo 2 shows a white solid line and the concrete
                        barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        broken line on the left fits a lane_line role; the white solid line on the right fits
                        an edge_line role | markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06]
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white edge line [US-3B.09-01-02] and there is a concrete barrier
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane to restrict
                        it
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move right due to the concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 880, 12.85 s

bdd100k_val__c9b099e4-6ab2e4f4 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or urban arterial road, approaching an
                        area with overhead signage and potential exits or intersections ahead. (lanes 3, mine
                        3, full)
Step 2  Left            Photo 1 shows a broken white line to the left of my car. Photo 2 shows a broken white
                        line with a visible dash and gap next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of my car, followed by a concrete
                        barrier/curb. Photo 2 shows a solid white line and the edge of a concrete curb next to
                        my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white broken line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings were observed
                        in my lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            right_boundary: The solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: A solid line discourages or prohibits crossing. [[US-3A.04-01]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line [US-3B.09-01-02] and a physical curb, and solid lines prohibit or discourage
                        crossing [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line into the curb area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 956, 14.81 s

bdd100k_val__ca146661-7f70d0c4 | lane | Test B | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road in the United States, heading towards a
                        distant intersection or highway merge area. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to my car that continues ahead, bordering a
                        shoulder/grass area. Photo 2 confirms a white solid line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings are present
                        in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing the line with care is
                        permitted. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway
                        and discourages crossing. [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, which discourages or prohibits crossing according to [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 9346, out 896, 16.27 s
```
