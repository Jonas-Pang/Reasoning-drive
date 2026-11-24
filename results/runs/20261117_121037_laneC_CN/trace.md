# Reasoning of lane run 20261117_121037_laneC_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards a bridge or overpass. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a metal guardrail. Photo 2
                        shows a solid white line next to my car and a metal guardrail further right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right |
                        roles: white dashed line for lane separation and white solid line for roadway edge fit
                        their roles | markings: no markings present in my lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): prohibited because the right boundary is a solid white edge line
                        [US-3B.09-01-02] and there is a guardrail.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there are no turn arrows or waiting areas
                        governing this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no turn arrows or waiting areas
                        governing this movement.
Step 6  u_turn          not_applicable: not_applicable because there are no U-turn arrows governing this
                        movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the guardrail.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 884, 12.67 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane road with a bridge ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a shoulder and a metal
                        guardrail. Photo 2 shows the solid white line next to my car and the guardrail further
                        right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (2) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: no markings in my
                        lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which is
                        permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line, and
                        crossing it would move the car off the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in my lane restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the shoulder.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 895, 12.55 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or carriageway, moving straight ahead on
                        a clear road. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which continues ahead. Photo 2 shows a
                        solid white line next to my car, and a metal guardrail is visible further to the
                        right.
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
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited: the right boundary is a solid
                        white edge line, and crossing it would move the car off the roadway [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed: no markings in the lane restrict going
                        straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 906, 30.31 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with high-rise buildings on both sides,
                        traveling straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line separating my lane from the lane to the left. Photo
                        2 shows the same yellow broken line next to my car, consisting of long dashes and
                        gaps.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, which continues forward. Photo 2 shows
                        a solid white line next to my car and a raised concrete barrier/curb immediately to
                        the right of the line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The yellow broken line on the left is unusual for a same-direction lane line
                        (usually white), but the white solid line on the right fits the role of an edge line.
                        | markings: No markings in the lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken line indicates a permissive condition, allowing crossing for
                        lane changes. [US-3A.04-01]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 5  Rule            right_boundary: A solid line discourages or prohibits crossing. [US-3A.04-01]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken line,
                        which is permissive according to [US-3A.04-01].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line [US-3B.09-01-02] and a solid line prohibits crossing [US-3A.04-01], further
                        reinforced by a physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not attempt to move right as
                        there is a solid edge line and a concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 954, 13.42 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 confirms a broken white line next to my car, consisting of long white dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a concrete barrier. Photo 2
                        shows a solid white line immediately to the right of my car and a concrete barrier
                        further right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows white Chinese characters '专用' and '交' painted in the
                        lane. Photo 1 shows these characters are part of a larger marking, likely '公交专用' (Bus
                        Only).
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego position (2)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: the 'BUS ONLY' text
                        indicates this is a preferential lane, which is consistent with the boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            text:bus: The word marking BUS ONLY designates a preferential lane reserved for buses.
                        [[US-3E.03-02]]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line, which
                        is permissive according to [US-3B.06-05-06].
Step 6  change_right    prohibited (contested, label allowed): prohibited: the right boundary is a solid white
                        edge line [US-3B.09-01-02] and is further blocked by a concrete barrier.
Step 6  go_straight     prohibited (contested, label allowed): prohibited: my car is an ordinary car in a lane
                        reserved for buses (text:bus), and [US-3H.07-01] prohibits general-purpose traffic
                        from occupying such lanes.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a bus-only lane. You should change left into the general-purpose
                        lane immediately, as ordinary vehicles are prohibited from using this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['go_straight decided without an arrow or prohibited-movement marking']
Tokens                  in 9314, out 1071, 33.37 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an underpass. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a single
                        solid white line immediately to the left of the lane, adjacent to a raised concrete
                        barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line. Photo 2 shows a single solid white line next to the
                        car, which continues as a solid line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries, as both sides are edge lines (barrier on left, road edge on
                        right). | roles: The white solid lines on both sides fit the role of edge lines for a
                        single-lane road or a separated roadway. | markings: No markings are present in the
                        lane, which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A solid white line delineates the edge of the roadway; crossing it is
                        discouraged or prohibited. [US-3B.09-01-02]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway;
                        crossing it is discouraged or prohibited. [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line and concrete barrier
                        [US-3B.09-01-02].
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [US-3B.09-01-02].
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
Advice                  Stay in your lane and proceed straight through the underpass. Do not cross the solid
                        white edge lines on either side.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 867, 12.6 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus stop on the left and parked scooters on the
                        right. The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car that continues straight. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and a raised curb. Photo 2 confirms a
                        single solid white line and a raised yellow curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the boundaries being edge lines on both sides | roles: the white solid lines on
                        both sides fit the role of edge lines for a single-lane road | markings: no markings
                        present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid white line delineates the edge of the roadway. [US-3B.09-01-02]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line (US-3A.04-01)
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and raised curb
                        (US-3A.04-01)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not cross the boundaries on either
                        side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 806, 11.54 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. (lanes 3, mine
                        3, full)
Step 2  Left            Photo 1 shows a white broken line next to my car that continues ahead. Photo 2
                        confirms a white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to my car that continues ahead. Photo 2 confirms
                        a single solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        lane 3 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: No markings were
                        observed in my lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white edge line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        this movement.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9314, out 853, 12.27 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a median on the left and a sidewalk/curb on
                        the right, traveling straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a left edge line and a right lane line. | roles: The white
                        solid left boundary acts as an edge line (roadway edge), and the white broken right
                        boundary acts as a lane line (separating same-direction traffic). | markings: No
                        markings are present in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left edge of the roadway, and
                        crossing it is generally prohibited. [US-3B.09-01-02]
Step 5  Rule            right_boundary: The broken white line indicates that crossing into the adjacent lane
                        with care is permitted. [US-3B.06-05-06]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line (US-3B.09-01-02).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (US-3B.06-05-06).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but do not cross the left boundary into the median.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 860, 9.21 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a wide urban road in China, approaching a signalized intersection.
                        (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my car. Photo 2 confirms a white
                        broken line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my car. Photo 2 confirms a white
                        broken line next to my car with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 4 and my position in
                        lane 3 agree with having white lane lines on both sides | roles: white dashed lines
                        are consistent with lane lines separating traffic in the same direction | markings: no
                        markings present in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 6  change_left     allowed: allowed by the broken white lane line (US-3B.06-05-06)
Step 6  change_right    allowed: allowed by the broken white lane line (US-3B.06-05-06)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through lane. You may continue straight or change lanes to the left or
                        right. Be mindful of the traffic signal ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9314, out 819, 28.41 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a white fence. Photo 2 confirms a single
                        solid yellow line immediately to the left of the lane.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The yellow line on the left indicates
                        the edge of the roadway or a separation from opposite traffic, making my lane the
                        leftmost of my direction. The broken white line on the right indicates another lane of
                        the same direction. This is consistent with lane_count 2 and ego_lane_index 1. |
                        roles: The yellow solid line fits the role of an edge_line or center_line; the broken
                        white line fits the role of a lane_line. | markings: No markings were observed in the
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A yellow line delineates the separation of traffic traveling in
                        opposite directions or the left-hand edge of the roadway. [[US-3A.03-03-04]]
Step 5  Rule            right_boundary: A broken line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow left_boundary [US-3A.04-01]
Step 6  change_right    allowed (correct): allowed by the broken white right_boundary [US-3A.04-01]
Step 6  go_straight     allowed (contested, label not_determined): allowed as no marking restricts carrying on
                        straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['symbol:other']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9314, out 861, 12.41 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road or ramp, heading towards a slight curve or
                        intersection ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 confirms a solid white line next
                        to the car, continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 confirms a solid white line
                        next to the car, continuing forward.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries being edge lines on both sides. | roles: The white solid lines on
                        both sides fit the role of edge lines for a single-lane road or ramp. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: A solid white line delineates the edge of the roadway; crossing it is
                        discouraged or prohibited. [US-3B.09-01-02]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway;
                        crossing it is discouraged or prohibited. [US-3B.09-01-02]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line (US-3B.09-01-02).
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line (US-3B.09-01-02).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the solid white edge lines on
                        either side.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 839, 11.94 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway passing under an overpass. (lanes 2, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid white line on the left, bordering a shoulder with a guardrail.
                        Photo 2 confirms a solid white line immediately to the left of the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from another lane to the right.
                        Photo 2 shows a gap and a dash of a white broken line.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid left boundary fits the role of an edge_line for a
                        divided highway/one-way street, and the white broken right boundary fits the role of a
                        lane_line. | markings: No markings are present in the lane, which is consistent with
                        the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line is used for left edges of divided highways;
                        however, this line is white, and per [US-3A.03-03-04], white lines delineate the
                        right-hand edge or both edges of a reversible roadway. Given the context of a highway,
                        this solid white line marks the left edge of the roadway. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid white edge line, and
                        crossing it would lead off the roadway into a shoulder/guardrail.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line, which is a
                        permissive condition [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict continuing straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of the highway. You may continue straight or change lanes
                        to the right, but do not cross the left edge line into the shoulder.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 946, 13.3 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test C | gemma4:31b
---------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, which continues ahead. Photo 2
                        confirms a single solid yellow line immediately to the left of the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a white broken line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a yellow edge line on the left indicates the leftmost lane of the
                        direction of travel. | roles: the yellow solid line fits the role of a left edge line
                        on a divided highway, and the white broken line fits the role of a lane line between
                        lanes of the same direction. | markings: no markings are present in the lane, which is
                        consistent with a through lane on a highway. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid yellow line on the left edge of a divided highway delineates
                        the left-hand edge of the roadway and indicates driving restrictions left of the
                        marking. [[US-3B.09-03]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing the line with care is
                        not discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line [US-3B.09-03].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no turn arrows or intersection markings.
Step 6  turn_right      not_applicable: not_applicable as there are no turn arrows or intersection markings.
Step 6  u_turn          not_applicable: not_applicable as there are no U-turn arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting areas are present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right. Do not cross the yellow line to the
                        left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 878, 12.57 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the center of the
                        lane. Photo 1 also shows this arrow.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: white
                        dashed lines are consistent with lane lines separating traffic in the same direction |
                        markings: the straight-ahead arrow is consistent with a through lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that going straight is a
                        permissible movement. [[US-3B.23-01]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line
                        [US-3B.06-05-06]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [US-3B.23-01]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        left turn [US-FIG-3B-21]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        right turn [US-FIG-3B-21]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        U-turn [US-FIG-3B-21]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may proceed straight or change lanes. Do not attempt to
                        turn left or right from this lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 979, 13.28 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a large intersection. (lanes 3, mine
                        1, full)
Step 2  Left            Photo 1 shows a yellow line to the left of the car, which is solid near the car and
                        becomes a solid-and-broken line further ahead. Photo 2 shows a solid yellow line
                        immediately to the left of the car.
                        yellow solid_dashed (near line solid), curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of the car. Photo 2 shows a white
                        broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 2 shows a white crosswalk (zebra stripes) across the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a center line on the left indicates the leftmost lane of the
                        direction. | roles: the yellow center line and white lane line fit their roles. |
                        markings: the crosswalk is a standard marking across the lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: Crossing the solid yellow line of a center line is prohibited.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: A broken white line indicates a permissive condition for crossing.
                        [[US-3A.04-01]]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern vehicle
                        movements out of the lane. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [US-3B.01-04].
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line
                        [US-3A.04-01].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may proceed straight or change to the right lane,
                        but you must not cross the yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_right'], citation unlisted,
                        contradictions []
Tokens                  in 9314, out 919, 12.86 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane urban road. The road continues straight ahead
                        with no immediate intersection or ramp visible. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my lane. Photo 2 shows a white broken
                        line next to my car, consisting of several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my lane, which continues ahead. Photo
                        2 shows a white solid line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        lane 3 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line, and the white
                        solid line on the right fits the role of an edge line. | markings: There are no
                        markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white line delineates the right-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [US-3B.06-05-06].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white edge line [US-3B.09-01-02].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 873, 12.43 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. There are
                        overhead lane-use signs indicating the allowed movements for the lanes ahead. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index
                        of 2 agree with having lane lines on both the left and right boundaries | roles: the
                        white dashed lines fit the role of lane lines separating traffic in the same direction
                        | markings: there are no markings in my lane to contradict | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (US-3B.06-05-06)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (US-3B.06-05-06)
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right. Note the overhead signs to determine which lane you need for your intended turn
                        at the intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 868, 12.22 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, heading towards an intersection with
                        overhead signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were detected in my lane, which is consistent with the boundaries. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line
                        [US-3B.06-05-06].
Step 6  change_right    allowed (contested, correct): Allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no lane-use arrow in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no lane-use arrow in my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no lane-use arrow in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 852, 10.96 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test C | gemma4:31b
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with several long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right sides | roles: white
                        dashed lines are consistent with lane lines separating traffic in the same direction |
                        markings: the straight-ahead arrow is consistent with a through lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that going straight is a
                        permissible movement in this lane. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [US-3B.23-01]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        left turn [US-3B.23-01]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        right turn [US-3B.23-01]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        U-turn [US-3B.23-01]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may go straight or change lanes. To turn left or right,
                        you must change to the corresponding outer lanes.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 989, 13.16 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with a
                        traffic signal overhead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows the same white broken line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having a lane line on both the left and right. |
                        roles: White dashed lines are consistent with lane lines separating traffic in the
                        same direction. | markings: No markings were observed in my lane, which is consistent
                        with a general through lane. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [US-3B.06-05-06]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (US-3B.06-05-06).
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        (US-3B.06-05-06).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no lane-use arrow governing this movement.
Step 6  turn_right      not_applicable: Not applicable as there is no lane-use arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no lane-use arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right. Follow the overhead traffic signal at the intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 876, 12.35 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a wide intersection or
                        open area. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line that is solid next to the car and continues as a solid
                        line ahead. Photo 2 confirms a single solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car and further ahead. Photo 2 shows a
                        white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (2)
                        are inconsistent with the boundaries. A yellow center line on the left and a white
                        lane line on the right indicate the car is in the leftmost lane of its direction
                        (index 1), not index 2. | roles: The yellow solid line on the left fits the role of a
                        center line; the white broken line on the right fits the role of a lane line. |
                        markings: No markings in the lane to contradict. | unseen: no | result: corrected
                        ego_lane_index to 1
Step 5  Rule            left_boundary: A solid yellow center line prohibits crossing for passing.
                        [[US-3B.01-04]]
Step 5  Rule            right_boundary: A broken white lane line indicates a permissive condition for
                        crossing. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [US-3B.01-04]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 859, 12.26 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in China, moving straight ahead on a
                        clear road. (lanes 5, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier. Photo 2 confirms a solid
                        white line immediately to the left of the car, bordering a raised concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a series of white dashes and gaps immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 and Photo 2 show large white chevron-like diagonal
                        markings (channelizing lines) across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 5 and ego_lane_index 1
                        agree with the left boundary being an edge_line and the right boundary being a
                        lane_line. | roles: The white solid edge line on the left and white dashed lane line
                        on the right fit their roles for a multi-lane highway. | markings: The channelizing
                        area is consistent with a high-speed roadway layout. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left edge of the roadway, and
                        crossing it is prohibited by the presence of the concrete barrier. [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates a permissive condition, allowing lane
                        changes with care. [[US-3B.06-05-06]]
Step 5  Rule            area:channelizing: Chevron markings are used to discourage travel on certain paved
                        areas, but here they are painted within the lane as guidance/warning. [[US-3B.25-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line and the
                        physical concrete barrier [US-3B.09-01-02].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings prohibiting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or move to the right. Do not attempt to move left due to the
                        concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing'], missed ['text:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 994, 13.68 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or expressway. The road ahead is straight
                        and clear, with overhead gantries in the distance. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to a concrete barrier on the left. Photo 2
                        confirms a solid white line immediately to the left of the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating the current lane from the lane to the
                        right. Photo 2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (1)
                        agree with the left boundary being an edge line and the right boundary being a lane
                        line. | roles: the white solid left boundary fits the role of an edge line for a one-
                        way road, and the white dashed right boundary fits the role of a lane line. |
                        markings: no markings are present in the lane, which is consistent with a standard
                        highway through lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The solid white line delineates the left-hand edge of the roadway.
                        [[US-3B.09-01-02]]
Step 5  Rule            right_boundary: The broken white line indicates that crossing the lane line with care
                        is permitted. [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid white edge line and
                        concrete barrier [US-3B.09-01-02].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [US-3B.06-05-06].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or move to the right lane if needed. Do not cross the left
                        boundary as it is the edge of the roadway.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 874, 12.46 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test C | gemma4:31b
----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead toward an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        lane 2 agree with having lane lines on both my left and right | roles: white dashed
                        lines are consistent with lane lines separating traffic in the same direction |
                        markings: the straight-ahead arrow is consistent with a through lane | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A broken white lane line indicates that crossing with care is not
                        discouraged or prohibited. [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the permissible movement for
                        this lane is to go straight. [[US-3B.23-01]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [US-3B.06-05-06]
Step 6  change_right    allowed (correct): allowed by the broken white line [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [US-3B.23-01]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        left turn [US-3B.23-01]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        right turn [US-3B.23-01]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow which does not show a
                        U-turn [US-3B.23-01]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes. Do not attempt
                        to turn left or right from this lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9314, out 997, 13.27 s
```
