# Reasoning of lane run 20261117_151616_laneC_US

```text
bdd100k_val__b1c66a42-6f7d68ca | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street in the United States, driving straight ahead on a road
                        with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car and continuing ahead. Photo 2
                        confirms a single solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line next to the car and continuing ahead, with a curb
                        and sidewalk to its right. Photo 2 confirms a single solid yellow line next to the
                        car.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show the word 'SCHOOL' painted in white across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center line on the left and edge line on the right | roles: the yellow color
                        for both boundaries fits the role of center line (left) and edge line (right) in a
                        two-way street context | markings: the text 'SCHOOL' is a warning and does not
                        contradict the boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white, but here it is yellow, likely indicating a no-parking zone per [CN-6.3.1] or
                        local US rules; regardless, the curb prohibits leaving the roadway. [[CN-5.4.3]]
Step 5  Rule            text:other: The word 'SCHOOL' is informative, warning the driver of a school zone.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited: prohibited by the solid yellow edge line and the physical curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and drive straight. Be alert for children as you are entering a
                        school zone.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 954, 14.35 s

bdd100k_val__b1f0efd9-e900c6e5 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the edge of the roadway, followed by a curb.
                        Photo 2 shows a solid white line and a raised curb immediately to the right of the
                        car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line and curb on the right fit the role of an edge line. | markings: No markings were
                        observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a]
Step 6  change_left     allowed (WRONG, label prohibited): allowed because the left boundary is a broken white
                        line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white line [CN-4.2.2-a] and there is a curb.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in the lane to restrict
                        it.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may go straight or change to the left lane, but you
                        cannot move to the right due to the curb and solid edge line.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8136, out 857, 12.51 s

bdd100k_val__b1f4491b-dd8dfed5 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway or urban arterial road. The road continues
                        straight ahead with no immediate intersection or ramp visible. (lanes 3, mine 2, full)
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
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        a standard through-lane on a highway. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no turn arrows or intersection markings.
Step 6  turn_right      not_applicable: Not applicable as there are no turn arrows or intersection markings.
Step 6  u_turn          not_applicable: Not applicable as there are no U-turn arrows or intersection markings.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 845, 12.74 s

bdd100k_val__b20b69d2-e31380a7 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a road approaching a curved ramp or exit, with a large casino sign to
                        the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line along the left edge of the road, following the curve
                        of the median. Photo 2 shows the same solid yellow line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right edge of the road. Photo 2 shows the same
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The white edge line on the right marks the edge of the roadway.
                        [CN-5.4.3]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line (CN-4.2.2-a)
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line (CN-4.2.2-a)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict continuing along the
                        lane
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and follow the road ahead; lane changes to either side are
                        prohibited by the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 754, 11.72 s

bdd100k_val__b263f57d-1ccf6e51 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides | roles: white dashed
                        lines are consistent with lane lines separating traffic in the same direction |
                        markings: no markings were observed in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): the left boundary is a broken white line, which allows crossing per
                        [CN-5.2.1-2]
Step 6  change_right    allowed: the right boundary is a broken white line, which allows crossing per
                        [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed by
                        default
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable (WRONG, label allowed): no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 639, 10.56 s

bdd100k_val__b2fbf86d-d5de82a4 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban city street in the United States, heading towards an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car and further ahead. Photo 2 confirms
                        a broken white line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car and further ahead. Photo 2 confirms
                        a broken white line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings are present in the lane, which is consistent with the boundaries. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 784, 10.28 s

bdd100k_val__b3060c96-d2391b61 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane road with trees on both sides; the road continues
                        straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the road. Photo 2 confirms a
                        solid yellow line immediately to the left of the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dash and gap immediately to the right of the car.
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
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          prohibited: Prohibited by the solid yellow center line [CN-6.1.4].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Do not cross the solid yellow
                        line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8136, out 833, 13.21 s

bdd100k_val__b306fb3f-f02e46cc | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane road with a grassy shoulder on the left. The road
                        continues straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line marking the left edge of the roadway. Photo 2
                        confirms a single solid yellow line next to the car, bordering a grassy area.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left and a white lane line on the
                        right. | roles: The yellow solid line fits the role of a left edge line; the white
                        broken line fits the role of a crossable lane line. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The yellow edge line marks the left edge of the direction of travel.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow line, and
                        according to CN-4.2.2-a, a solid line means crossing is normally prohibited.
Step 6  change_right    allowed (WRONG, label not_determined): allowed: the right boundary is a broken white
                        line, which according to CN-5.2.1-2 and CN-4.2.2-a may be crossed.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you must not cross the solid yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 884, 12.97 s

bdd100k_val__b321c6b6-ab603d42 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road with construction barriers on the left. The road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues forward. Photo 2
                        confirms a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, continuing forward. Photo 2 confirms
                        a single solid white line next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a white edge line on the left and a white lane line on the right
                        (separating from a lane where other cars are stopped). | roles: The white color and
                        solid pattern fit the roles of edge line and lane line on an intersection approach or
                        construction zone. | markings: No markings are present in the lane. | unseen: No |
                        result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid white line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  change_right    prohibited (contested, label allowed): The right boundary is a solid white line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 8136, out 801, 13.38 s

bdd100k_val__b4542860-0b880bb4 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, approaching an intersection with a traffic
                        signal ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway, separating the
                        lane from a green-painted bike lane. Photo 2 shows the same solid white line next to
                        my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: There are no markings in
                        my lane to conflict with boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line on the right into the bike lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 839, 12.93 s

bdd100k_val__b48c7b5f-800d31b4 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road with a few lanes of traffic. Ahead is a clear stretch of
                        road with parked cars on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow broken line to the left of my car. Photo 2 shows the same
                        yellow broken line next to my car, consisting of long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line to the right of my car, which ends as it approaches a
                        curb. Photo 2 shows a white solid line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a yellow center line on the left and a white edge line
                        on the right indicate a single lane for my direction. | roles: the yellow dashed line
                        fits the role of a crossable center line, and the white solid line fits the role of a
                        road edge line. | markings: there are no markings in my lane to contradict the
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The crossable centre line allows vehicles to cross to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the yellow dashed center line
                        [CN-5.1.1].
Step 6  change_right    prohibited (contested, label allowed): prohibited by the white solid edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area in view.
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may change left across the center line if safe, but you
                        must not cross the right edge line into the parking/curb area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 866, 13.75 s

bdd100k_val__b49d6c0d-457e13b3 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, heading straight. There
                        are no immediate intersections or ramps visible ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car, which continues as a solid line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 and Photo 2 show a white bicycle symbol painted in the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and an edge line on the right indicate my lane is the
                        rightmost lane of my direction. | roles: the double solid yellow line fits the role of
                        a center line, and the solid white line fits the role of an edge line. | markings: the
                        bicycle symbol is a common marking for shared lanes or bike lanes; it does not
                        contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 5  Rule            symbol:bike: The bicycle symbol indicates that the lane is shared with or reserved for
                        bicycles, but does not prohibit motor vehicle travel. [null]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be mindful of cyclists as indicated by the
                        bicycle symbol in your lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:bike'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8136, out 764, 12.26 s

bdd100k_val__b4d18d1a-193e24a1 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 791, 10.96 s

bdd100k_val__b5042634-1034573c | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road under a large bridge structure, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with the role of crossable lane lines separating traffic in the same
                        direction. | markings: No markings were observed in the lane, which is consistent with
                        the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there are no guide arrows or waiting areas in the
                        lane.
Step 6  turn_right      not_applicable: Not applicable as there are no guide arrows or waiting areas in the
                        lane.
Step 6  u_turn          not_applicable: Not applicable as there are no guide arrows or waiting areas in the
                        lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 806, 12.64 s

bdd100k_val__b54c065e-8b13cfe7 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road, approaching an intersection. There is a vehicle
                        ahead in the same lane. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line extending from the bottom to the
                        intersection. Photo 2 confirms two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car, which continues straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking in the lane restricts it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 751, 11.69 s

bdd100k_val__b5661732-3684230b | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban city road in the United States, driving straight
                        ahead towards a distant intersection. (lanes 3, mine 2, full)
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
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        sides. | roles: the white dashed lines on both sides correctly fit the role of lane
                        lines separating traffic in the same direction. | markings: there are no markings in
                        my lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 850, 13.1 s

bdd100k_val__b577827c-28fc9b0d | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching an intersection with a traffic signal.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid yellow line on the right, which then ends as the road opens up
                        to the right. Photo 2 shows a solid yellow line next to my car.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position in
                        lane 2 agree with the boundaries: a lane line on the left and an edge line on the
                        right. | roles: The white dashed line fits the role of a lane line; the yellow solid
                        line fits the role of a left-hand edge line for opposing traffic or a right-hand edge
                        line in specific contexts, but here it marks the edge of the roadway. | markings: No
                        markings are present in my lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid yellow edge line
                        (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid yellow
                        line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 847, 13.32 s

bdd100k_val__b59e50fa-ca034dd0 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban city road in the United States, driving straight
                        ahead on a clear stretch of road. (lanes 3, mine 2, full)
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
                        the middle lane (index 2) agree with having a lane line on both the left and right
                        boundaries. | roles: The white dashed lines on both sides correctly fit the role of
                        lane lines separating traffic in the same direction. | markings: There are no markings
                        in my lane, which is consistent with the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area in view.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 859, 14.2 s

bdd100k_val__b5cd5f72-32232751 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching an intersection with a right turn ahead.
                        (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line marking the right edge of the road. Photo 2 shows
                        this white solid line continuing next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 1 and Photo 2 both show a white right-turn arrow painted in
                        my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane line, and the white solid line
                        fits the role of a right edge line. | markings: The right-turn arrow is consistent
                        with being in the rightmost lane bounded by an edge line. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 5  Rule            arrow:right: The right-turn arrow indicates that the lane is for turning right.
                        [[CN-5.13.1]]
Step 6  change_left     allowed (contested, correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white edge line [CN-4.2.2-a].
Step 6  go_straight     prohibited (correct): prohibited because the lane has a right-turn arrow which
                        restricts movement to the indicated direction [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the lane has a right-turn arrow [CN-5.13.1].
Step 6  turn_right      allowed (correct): allowed because the lane has a right-turn arrow [CN-5.13.1].
Step 6  u_turn          prohibited (correct): prohibited because the lane has a right-turn arrow [CN-5.13.1].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a right-turn-only lane. If you intend to go straight or turn left, you must
                        change to the left lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 993, 14.26 s

bdd100k_val__b5f84825-c97df380 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. There are multiple lanes of
                        travel in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): Photo 2 shows a white arrow pointing both straight and
                        left in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries | roles: white
                        dashed lines are consistent with the role of crossable lane lines | markings: the
                        straight-left arrow is consistent with a through lane that also allows left turns |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            arrow:straight_left: The guide arrow indicates that the vehicle may proceed straight
                        ahead or turn left. [CN-5.13.1]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (correct): allowed by the straight-left arrow (CN-5.13.1)
Step 6  turn_left       allowed (WRONG, label prohibited): allowed by the straight-left arrow (CN-5.13.1)
Step 6  turn_right      prohibited (WRONG, label allowed): prohibited by the straight-left arrow (CN-5.13.1)
                        as it does not show a right turn
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as no arrow or prohibition
                        governs it
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a lane that allows you to go straight or turn left. You may change lanes to
                        the left or right if safe to do so.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight_left'], missed ['arrow:straight_right', 'line:stop_line']), actions
                        False, unsafe ['turn_left'], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 932, 15.74 s

bdd100k_val__b65fd3df-87ed965a | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on the right, facing a straight road ahead.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line on the left. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries; the left boundary is a lane line, implying another lane of
                        the same direction exists to the left, but the image shows the car is in the leftmost
                        lane of the travel direction (the line on the left is the edge of the road/parking
                        area). Wait, looking closer at Photo 1, the line on the left is the edge of the
                        roadway. The lane count is 1 for the travel direction, or 2 if the left area is a
                        lane. Given the context of city parking, the left line is an edge line. | roles: The
                        white solid lines fit the role of lane or edge lines. | markings: No markings in the
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     prohibited (contested, label allowed): The left boundary is a solid white line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  change_right    prohibited (contested, label allowed): The right boundary is a solid white line, which
                        prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your current lane and proceed straight. Lane changes to the left or right are
                        prohibited by the solid white lines.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 8136, out 865, 13.74 s

bdd100k_val__b7041acc-6de39959 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway approaching an overpass with overhead
                        signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right, which continues ahead. Photo 2 shows a
                        solid white line immediately to the right of my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and position 2 agree
                        with the boundaries: a lane line on the left and an edge line on the right would
                        typically mean the rightmost lane, but here the right boundary is an edge line and the
                        left is a lane line, meaning I am in the rightmost lane of the motor vehicle travel
                        way. Wait, if there are 3 lanes and I am index 2, there should be a lane to my right.
                        Looking closer at Photo 1, there is a lane to my left and a shoulder to my right. My
                        lane is the rightmost lane. I will correct ego_lane_index to 3. | roles: The white
                        dashed line on the left fits the role of a lane line. The white solid line on the
                        right fits the role of an edge line. | markings: No markings are present in the lane.
                        | unseen: No | result: corrected ego_lane_index to 3
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white edge line marks the edge of the motor vehicle lanes.
                        [CN-5.4.1]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 991, 15.49 s

bdd100k_val__b7935597-13c4b9dd | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a residential urban road, driving straight ahead. There are parked cars
                        on the right side of the road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a dark area with trees and a curb separating the road from a sidewalk.
                        Photo 2 shows the same curb and the edge of the pavement next to the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating the driving lane from a parking area.
                        Photo 2 shows the same solid white line immediately to the right of the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a curb on the left and an edge line on the right. | roles: The
                        white solid line on the right fits the role of an edge line separating the lane from
                        parking. | markings: No markings are present in the lane. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway. [CN-5.4.1]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     prohibited (correct): prohibited by the physical curb (left_boundary).
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        (right_boundary) and rule [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the right boundary into the
                        parking area or the left boundary into the sidewalk.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 818, 13.16 s

bdd100k_val__b7aa329e-25d68dec | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           A two-lane two-way road in a residential area with trees and fences; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the road. Photo 2 shows a
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 759, 11.6 s

bdd100k_val__b80018ef-3a620af0 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a two-way road at night. Ahead is a straight stretch of road
                        with parked cars on both sides. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating the ego lane from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right edge of the road. Photo 2 shows a solid white
                        line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and position (1)
                        agree with the boundaries: a center line on the left and an edge line on the right. |
                        roles: the yellow double solid line fits the role of a center line; the white solid
                        line fits the role of an edge line. | markings: no markings in the lane to check. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8136, out 672, 11.26 s

bdd100k_val__b84146a1-a5f588ef | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead toward a distant
                        intersection. (lanes 3, mine 2, full)
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
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        sides. | roles: the white dashed lines on both sides correctly fit the role of lane
                        lines separating traffic in the same direction. | markings: there are no markings in
                        my lane to contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right as needed.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 839, 11.93 s

bdd100k_val__b8fe9f2b-d63131a3 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city street in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car and further ahead. Photo 2 confirms
                        a broken white line next to the car with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car and further ahead. Photo 2 confirms
                        a broken white line next to the car with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: the white dashed
                        lines fit the role of crossable lane lines separating traffic in the same direction |
                        markings: no markings were observed in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 785, 13.7 s

bdd100k_val__b91cdc5d-bce994ce | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with buildings on the right. The road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to my car and further ahead. Photo 2 shows a
                        broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to my car and further ahead. Photo 2 shows a
                        broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        lane 2 agree with having lane lines on both the left and right. | roles: The white
                        dashed lines fit the role of crossable lane lines separating traffic in the same
                        direction. | markings: There are no markings in my lane to contradict the boundaries.
                        | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 805, 10.41 s

bdd100k_val__b928271b-fe5cc5d1 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead toward a distant
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a single broken white line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway. Photo 2 shows
                        a single solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right
                        indicate my lane is the rightmost of the three lanes in my direction. | roles: The
                        white broken line on the left fits the role of a lane line; the white solid line on
                        the right fits the role of an edge line. | markings: No markings are present in the
                        lane, which is consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which may be
                        crossed according to CN-5.2.1-2.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, and crossing solid lines is normally prohibited according to CN-4.2.2-a.
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
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 884, 13.15 s

bdd100k_val__b9429f07-33ae3ff1 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way road in a residential or suburban area, heading towards an
                        intersection with traffic signals. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms the double solid yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway, with a curb
                        further right. Photo 2 shows the solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center line on the left and edge line on the right | roles: the yellow double
                        solid line fits the role of a center line, and the white solid line fits the role of
                        an edge line | markings: no markings in lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the solid white edge line and
                        the presence of a curb [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 814, 13.15 s

bdd100k_val__ba2db972-f29458c8 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road. The road continues straight ahead with
                        no immediate intersection or ramp visible. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a yellow broken line with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, but a raised curb separating the road from
                        the sidewalk. Photo 2 confirms the presence of a raised curb and no paint.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and ego position (2)
                        agree with the boundaries: a center line on the left and an edge line on the right. |
                        roles: the yellow color of the left boundary fits the role of a center line; the curb
                        on the right fits the role of an edge line. | markings: no markings in the lane to
                        contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken yellow center line allows crossing to overtake, turn, or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The curb marks the edge of the roadway. [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken yellow line, which
                        [CN-5.1.1] allows crossing.
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a raised curb, which
                        physically prohibits leaving the lane.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you cannot move to the right due to the curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 837, 12.47 s

bdd100k_val__ba9f6c98-2a75a096 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           A two-lane two-way road in a rural area, with a clear path ahead and no immediate
                        intersections. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line extending far ahead. Photo 2 shows the same
                        double solid yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the edge of the road. Photo 2 shows the same
                        solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and my lane position
                        of 1 agree with the center line on the left and edge line on the right | roles: the
                        yellow double solid line fits the role of a center line, and the white solid line fits
                        the role of an edge line | markings: no markings in my lane to check | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): the left boundary is a double solid yellow line, which prohibits
                        crossing according to [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): the right boundary is a solid white edge line; while
                        [CN-5.4.1] defines it, crossing a solid line is normally prohibited per [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          prohibited: the left boundary is a double solid yellow line, which prohibits crossing
                        according to [CN-6.1.2]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8136, out 680, 11.63 s

bdd100k_val__bab692c9-4d1f2bdd | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with streetcar tracks embedded in the road. The road
                        continues straight ahead towards a slight incline. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line to the left of the tracks. Photo 2 confirms
                        two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line to the right of the tracks. Photo 2 confirms a single
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the double yellow line on the left
                        indicates the center of a two-way road, and the white line on the right indicates the
                        edge of the roadway, consistent with being in the only lane for this direction. |
                        roles: yellow double solid for center_line and white solid for edge_line are
                        consistent with the roles. | markings: no markings in lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow line [CN-6.1.2]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          prohibited: prohibited by the double solid yellow line [CN-6.1.2]
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines to the
                        left or the white edge line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8136, out 820, 12.52 s

bdd100k_val__bb289fdb-4bc01501 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road at night, approaching an intersection.
                        (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car and further ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car and further ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with lane_line roles | markings: no markings present in the lane |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right, or continue
                        straight.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 633, 11.4 s

bdd100k_val__bb8dba97-3537805c | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards a distant intersection or junction.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left, bordering a shoulder with a metal
                        guardrail. Photo 2 confirms the line next to the car is a single solid yellow line.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a series of white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the boundaries; a yellow edge line on the left indicates the leftmost lane of the
                        direction of travel. | roles: the yellow solid line fits the role of a left edge line,
                        and the white broken line fits the role of a lane line. | markings: no markings are
                        present in the lane, which is consistent with the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and the physical
                        guardrail (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the left boundary due to the solid line and guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 851, 12.66 s

bdd100k_val__bbf0f5d7-ea2f1cc3 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead toward an intersection
                        or road transition. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms a
                        single solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The yellow edge line on the left
                        indicates my lane is the leftmost lane of my direction, which agrees with the lane
                        count and index. | roles: The yellow solid line on the left fits the role of a left
                        edge line; the white broken line on the right fits the role of a lane line. |
                        markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles from crossing it.
                        [CN-6.1.4]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow edge line (CN-6.1.4).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the left boundary.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 824, 12.74 s

bdd100k_val__bbf48d08-b6a11dd8 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way road in a residential area, approaching a T-junction or
                        intersection where the road ahead seems to curve or end. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line extending from the bottom to the
                        intersection. Photo 2 confirms two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to the car, which continues straight ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking in the lane restricts it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines to the
                        left or the white edge line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 771, 12.79 s

bdd100k_val__bbfe3b4f-5137ff9f | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection with a crosswalk and
                        traffic signals ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the lane. Photo 1
                        shows the same arrow further ahead.; line:crosswalk (full): Photo 1 and Photo 2 show a
                        white zebra-style crosswalk across the lane ahead.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        correctly serve as lane lines separating traffic in the same direction. | markings:
                        The straight-ahead arrow is consistent with the lane's position and boundaries. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            arrow:straight: The guide arrow indicates that the car is permitted to go straight
                        ahead. [CN-5.13.1]
Step 5  Rule            line:crosswalk: The crosswalk is an informative marking for pedestrian crossing and
                        does not govern the seven actions. [null]
Step 6  change_left     allowed (contested, label not_determined): allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (contested, label not_determined): allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1) which
                        restricts movement to straight only.
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed.
                        Be mindful of the crosswalk and traffic signals ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions True, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 8136, out 1065, 15.32 s

bdd100k_val__bc19c993-c0a0f85f | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['text:other']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8136, out 777, 12.97 s

bdd100k_val__bc9b5bfb-51ebcf39 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching an intersection. (lanes 2,
                        mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car and continuing ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (2) agree with the boundaries: a center line on the left and an edge line on the right
                        indicate my lane is the rightmost lane of my direction. | roles: The double solid
                        yellow line fits the role of a center line; the solid white line fits the role of an
                        edge line. | markings: No markings are present in my lane. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.1]
                        and the fact that it marks the edge of the roadway
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Lane changes to the left or right are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 821, 15.34 s

bdd100k_val__bcbf328d-953430de | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road approaching an intersection. There is a white car
                        directly ahead in the same lane. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms the double solid yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line next
                        to my car, which continues as a solid line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): Photo 2 shows a white right-turn arrow and the word 'ONLY' painted
                        in the lane.; text:only (full): Photo 2 shows the word 'ONLY' painted in the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (2)
                        agree with the boundaries: a center line on the left and an edge line on the right
                        indicate I am in the rightmost lane of my direction. | roles: The double solid yellow
                        line fits the role of a center line; the solid white line fits the role of an edge
                        line. | markings: The right-turn arrow and 'ONLY' text are consistent with each other
                        and with the right-edge boundary. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white edge line marks the boundary of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 5  Rule            arrow:right: The right-turn arrow indicates that the lane is for right turns.
                        [[CN-5.13.1]]
Step 5  Rule            text:only: The word 'ONLY' restricts the lane to the movement indicated by the
                        accompanying arrow. [null]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, label allowed): prohibited by the solid white edge line
                        [CN-5.4.1]
Step 6  go_straight     prohibited (contested, label allowed): prohibited by the right-turn arrow [CN-5.13.1]
                        and 'ONLY' text
Step 6  turn_left       prohibited: prohibited by the right-turn arrow [CN-5.13.1] and 'ONLY' text
Step 6  turn_right      allowed: allowed by the right-turn arrow [CN-5.13.1]
Step 6  u_turn          prohibited: prohibited by the right-turn arrow [CN-5.13.1] and 'ONLY' text
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a right-turn-only lane. You must turn right at the intersection; lane
                        changes and going straight are prohibited.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right', 'text:only'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8136, out 1082, 15.13 s

bdd100k_val__bd338426-4b27de63 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to the car, which continues ahead. Photo 2
                        confirms a single white solid line and a raised curb further to the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings were observed
                        in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [CN-5.4.1]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which may be
                        crossed according to CN-5.2.1-2.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and there is a curb, and crossing a solid line is normally prohibited per
                        CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the right edge line into the curb area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 866, 14.35 s

bdd100k_val__bd354e59-e5a9e8c6 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left side of the road, extending far ahead.
                        Photo 2 shows the same solid yellow line immediately to the left of the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line separating my lane from a line of parked cars. Photo
                        2 shows this solid white line immediately to the right of the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (1) are slightly inconsistent with the boundaries; the yellow center line on the left
                        indicates my lane is the leftmost of my direction, but the white line on the right is
                        an edge line, meaning there is only one travel lane in this direction. I correct
                        lane_count to 1 and ego_lane_index to 1. | roles: The yellow solid line on the left
                        fits the role of a center_line. The white solid line on the right fits the role of an
                        edge_line separating the travel lane from a parking area. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the boundary between motor vehicle lanes and
                        non-motorized lanes or parking. [[CN-5.4.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.1] as
                        it marks the edge of the roadway
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow line to the left or
                        the white line to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 912, 13.55 s

bdd100k_val__bd3bd3ab-8e38f822 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road, likely an airport access road given the 'Airport'
                        sign, heading towards a terminal or parking area. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to the car, with several dashes and gaps
                        visible.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway, next to a
                        sidewalk/curb area. Photo 2 shows the same solid white line and the edge of the
                        pavement.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane line, and the white solid line
                        fits the role of a right-hand edge line. | markings: No markings were observed in the
                        lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (contested, label prohibited): Allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): Prohibited by the solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there are no guide arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: Not applicable as there are no guide arrows governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there are no guide arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 855, 42.12 s

bdd100k_val__bd656105-ed6f8161 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. The road is wide with multiple
                        lanes in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 and Photo 2 show a wide white transverse line across
                        the lane ahead of the car.; line:crosswalk (full): Photo 1 and Photo 2 show a white
                        zebra-style crossing marking across the lane beyond the stop line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right boundaries. | roles: the white
                        dashed lines on both sides fit the role of lane lines separating traffic in the same
                        direction. | markings: the stop line and crosswalk are consistent with an intersection
                        approach. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 5  Rule            line:crosswalk: The crosswalk is an informative marking for pedestrian crossing and
                        does not govern the seven actions. [null]
Step 6  change_left     allowed (contested, label prohibited): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken white lane line
                        [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as there are no arrows restricting movement and
                        the boundaries do not prohibit it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may change lanes to the left or right, or proceed
                        straight through the intersection, stopping at the stop line if required by the
                        traffic signal.
Score                   lane False, boundaries {'left': None, 'right': None}, markings False (added
                        ['line:stop_line'], missed []), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8136, out 859, 13.32 s

bdd100k_val__bd65dd37-4c3cdf2d | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an overpass/bridge. (lanes 3,
                        mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, and a concrete barrier/curb
                        immediately to the right of that line. Photo 2 confirms the solid white line and the
                        adjacent concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (3)
                        agree with the boundaries: a lane line on the left and an edge line/barrier on the
                        right. | roles: The white dashed line on the left fits the role of a lane line; the
                        white solid line and curb on the right fit the role of an edge line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a]
                        and the physical concrete barrier.
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
                        but you cannot move to the right due to the solid line and concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 859, 13.63 s

bdd100k_val__bd8d420d-ec34c634 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides. Ahead is a clear stretch of
                        road with a parked delivery truck on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway, next to a
                        sidewalk. Photo 2 shows this solid white line clearly next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my position (2)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings in my lane to
                        check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line and the
                        presence of a curb [CN-4.2.2-a].
Step 6  go_straight     allowed (correct): allowed as there are no markings restricting forward movement.
Step 6  turn_left       not_applicable (WRONG, label prohibited): not_applicable as there is no arrow or
                        waiting area governing this movement.
Step 6  turn_right      not_applicable (WRONG, label allowed): not_applicable as there is no arrow governing
                        this movement.
Step 6  u_turn          not_applicable (WRONG, label prohibited): not_applicable as there is no arrow
                        governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the sidewalk/parking area.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:straight_right']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 858, 13.36 s

bdd100k_val__bdc0dc52-b4d05890 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, approaching an
                        intersection with traffic signals. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        correctly serve as lane lines separating traffic in the same direction. | markings: No
                        markings were observed in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that the lane may be crossed.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line indicates that the lane may be crossed.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line
                        (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right. Follow the traffic signals at the intersection.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8136, out 801, 11.07 s

bdd100k_val__bdf6ab8b-3ebe8356 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane road, possibly a bridge or highway, with a clear
                        path ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left, bordering a shoulder with a guardrail.
                        Photo 2 confirms this solid yellow line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, bordering a shoulder with a guardrail.
                        Photo 2 confirms this solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the presence of edge lines on both the left and right sides. | roles: The yellow
                        solid line on the left and white solid line on the right fit the roles of left and
                        right edge lines respectively. | markings: There are no markings in the lane to
                        contradict the boundaries. | unseen: No attributes were reported that were not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The white edge line on the right marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     prohibited (correct): Prohibited by the solid yellow left edge line (CN-4.2.2-a).
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white right edge line
                        (CN-4.2.2-a).
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
Advice                  Stay in your lane and proceed straight; do not cross the solid edge lines on either
                        side.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 931, 29.32 s

bdd100k_val__be0a188d-c47bac51 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a bridge. The road ahead continues straight through the bridge
                        structure. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from another lane to the left.
                        Photo 2 shows the same broken white line next to my car, with several distinct dashes
                        and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the road, followed by a
                        physical barrier/railing. Photo 2 shows the solid white line and the start of the
                        barrier next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position in
                        lane 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: There are no markings in
                        my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line (CN-4.2.2-a)
                        and the physical barrier.
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
Advice                  You are in the rightmost lane of the bridge. You may continue straight or change lanes
                        to the left, but you must not cross the right edge line.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 847, 12.78 s

bdd100k_val__be22a1e1-cbcd82a6 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching an intersection with
                        traffic signals ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        correctly serve as lane lines separating traffic in the same direction. | markings: No
                        markings were observed in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no guide arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right. Be mindful of the traffic signals at the intersection ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 810, 12.41 s

bdd100k_val__be60191c-2dea5114 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road approaching an intersection with traffic
                        signals. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were observed in the lane, which is consistent with the boundaries. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right. Be mindful of the traffic signals ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 795, 12.74 s

bdd100k_val__be839b4c-fba3ea45 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road in the United States, approaching a crosswalk and
                        intersection. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line to the left of the lane, which appears solid. Photo 2 does
                        not show the left boundary clearly as it is cut off or too far back.
                        yellow solid, curb no, center_line, evidence partial
Step 2  Right           Photo 1 shows a white line to the right, which is a solid edge line next to a curb.
                        Photo 2 confirms the presence of a white solid line and a raised curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 1 and Photo 2 show the words 'BUS ONLY' painted in white in the
                        lane.; line:crosswalk (full): Photo 1 and Photo 2 show a white zebra-style crosswalk
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right | roles: the yellow
                        center line and white edge line fit their roles | markings: the BUS ONLY text
                        indicates a reserved lane, which is consistent with the boundaries | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.4]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [CN-5.4.3]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the lane. [CN-6.9.1]
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians to cross; it does not govern
                        the seven actions but requires yielding. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow center line
                        [CN-6.1.4]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line and curb
                        [CN-5.4.3]
Step 6  go_straight     allowed (contested, correct): allowed as no arrow restricts it, though the lane is
                        reserved for buses [CN-6.9.1]
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a bus-only lane; you should not be in this lane unless you are driving a
                        bus. Do not change lanes as both boundaries are solid, and yield to pedestrians at the
                        crosswalk.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:bus'], missed []), actions False, unsafe [], citation unlisted, contradictions
                        []
Tokens                  in 8136, out 1053, 15.06 s

bdd100k_val__be926190-5293afb9 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with residential houses on the right. The road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating the car's lane from the opposite
                        direction. Photo 2 shows the same double solid yellow line next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, but the road edge is bordered by parked
                        cars and a curb. Photo 2 shows the road edge next to the car with no paint and a curb.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with the center line on the left and the edge/curb on the right | roles: the double
                        solid yellow line fits the role of a no-crossing center line; the curb fits the role
                        of an edge boundary | markings: no markings in the lane to contradict | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The edge of the roadway is marked by the curb. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited: prohibited by the physical curb [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines to the
                        left or drive onto the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 823, 12.72 s

bdd100k_val__bfa92b30-f12f3535 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-lane two-way road, traveling straight ahead on a clear day. (lanes
                        1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the road. Photo 2 confirms
                        a single solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 751, 10.62 s

bdd100k_val__bfe2b817-505676ef | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a residential two-way road. The road ahead is straight with no
                        immediate intersection or ramp visible. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line extending far ahead. Photo 2 shows the same
                        double solid yellow line immediately next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows a solid white line
                        immediately next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries: a center line on the left and an edge line on the right. | roles:
                        The yellow double solid line fits the role of a center line; the white solid line fits
                        the role of an edge line. | markings: No markings are present in the lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): Prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  change_right    prohibited (contested, correct): Prohibited by the solid white edge line [CN-5.4.1] as
                        it marks the boundary of the roadway.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings in the lane restricting
                        forward movement.
Step 6  turn_left       not_applicable: Not applicable as there is no intersection or turn arrow in view.
Step 6  turn_right      not_applicable: Not applicable as there is no intersection or turn arrow in view.
Step 6  u_turn          prohibited: Prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the center line or the right edge
                        line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8136, out 831, 13.38 s

bdd100k_val__bff4bb8b-152c6105 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway, traveling straight ahead on a road with no
                        immediate intersections or ramps visible. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a yellow solid line next to a metal guardrail. Photo 2 confirms the
                        yellow solid line and the guardrail immediately to the left of the lane.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a stretch of this white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left indicates the leftmost lane
                        of the direction of travel, and a white lane line on the right indicates another lane
                        of the same direction. | roles: The yellow solid line on the left fits the role of a
                        left edge line; the white broken line on the right fits the role of a crossable lane
                        line. | markings: No markings are present in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 5  Rule            right_boundary: A broken white lane line separates traffic flows in the same direction
                        and may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow edge line and the physical
                        guardrail (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or turn arrow.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right. Do not cross the left boundary due to
                        the solid line and guardrail.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 923, 14.24 s

bdd100k_val__c02d18db-f5278de0 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, heading towards an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car that continues ahead. Photo 2
                        confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 779, 11.0 s

bdd100k_val__c068a67b-03b6e200 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a residential city street with houses on both sides. The road ahead is a
                        straight stretch with parked cars along the right side. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow broken line extending ahead. Photo 2 shows a yellow broken line
                        next to the car with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white solid line separating the lane from a parking area. Photo 2
                        shows a white solid line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left and
                        white edge line on the right agree with my lane being the only lane of my direction. |
                        roles: The yellow dashed line fits the role of a crossable center line; the white
                        solid line fits the role of a road edge line. | markings: No markings in the lane to
                        contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: Crossing the solid white line is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken yellow center line [CN-5.1.1]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You can drive straight or move left across the center line if safe; do not cross the
                        right edge line into the parking area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 813, 41.63 s

bdd100k_val__c07733d0-7525eae7 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway or expressway, traveling straight ahead on a road
                        that appears to be a bridge or elevated section. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left, running along a concrete barrier. Photo
                        2 confirms a solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left indicates the leftmost lane
                        of the direction of travel, and a white lane line on the right indicates another lane
                        of the same direction. | roles: The yellow solid line on the left fits the role of a
                        left edge line; the white broken line on the right fits the role of a crossable lane
                        line. | markings: No markings are present in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow line and is
                        adjacent to a concrete barrier, which prohibits crossing.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which allows
                        crossing for lane changes.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no intersection or turn markings are present.
Step 6  turn_right      not_applicable: not_applicable: no intersection or turn markings are present.
Step 6  u_turn          not_applicable: not_applicable: no intersection or turn markings are present.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you cannot move further left due to the road edge and barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 879, 13.42 s

bdd100k_val__c07733d0-aebb8786 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road. The road continues straight ahead with
                        no immediate intersection or ramp visible. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the middle lane (index 2) agree with having a lane line on both the left and right. |
                        roles: White dashed lines are consistent with the role of crossable lane lines
                        separating traffic in the same direction. | markings: There are no markings in my
                        lane, which is consistent with a standard through lane. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
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
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 838, 12.56 s

bdd100k_val__c0e7271a-a3c8d55f | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a concrete barrier on the right. The road
                        continues straight ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a concrete barrier. Photo 2 shows the solid
                        white line and the concrete barrier immediately to the right of my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        next to a barrier fits the role of an edge line. | markings: no markings are present
                        in my lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white line [CN-4.2.2-a] and there is a concrete barrier.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move to the right due to the solid line and concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 869, 14.76 s

bdd100k_val__c0efbe92-2ee3e529 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings on both sides, driving straight ahead
                        towards a clear road. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a white broken line with long dashes and gaps next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a white broken line with long dashes and gaps next to the car.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries being edge lines. | roles: White broken lines on both sides are
                        consistent with edge lines in a low-traffic city environment where parking or roadside
                        access may be permitted. | markings: No markings are present in the lane, which is
                        consistent with the boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: A broken line means it may be crossed. [CN-4.2.2-a]
Step 5  Rule            right_boundary: A broken line means it may be crossed. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): The left boundary is a broken white line, which allows crossing
                        according to CN-4.2.2-a.
Step 6  change_right    allowed (contested, correct): The right boundary is a broken white line, which allows
                        crossing according to CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): No marking restricts going straight in this lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You are in a single lane. You may proceed straight or change lanes if safe to do so.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 819, 12.66 s

bdd100k_val__c100db13-71b423e5 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway approaching an exit or intersection, with a
                        concrete barrier on the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with a clear dash and gap next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white solid line next to a concrete barrier. Photo 2 shows a white
                        solid line and the edge of the concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (3) agree with the boundaries: a lane line on the left and an edge line on the right.
                        | roles: the white dashed line on the left fits the role of a lane line; the white
                        solid line on the right fits the role of an edge line. | markings: no markings in my
                        lane to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line (CN-4.2.2-a)
                        and the concrete barrier.
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move to the right due to the solid line and concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 836, 12.67 s

bdd100k_val__c107c2f1-b2b8fff0 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in the United States, moving straight
                        ahead on a clear road. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating the road from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to the car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white line with clear dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my lane position
                        (1) agree with the boundaries: a center line on the left and a lane line on the right.
                        | roles: the double solid yellow line fits the role of a center line; the broken white
                        line fits the role of a lane line. | markings: no markings are present in the lane,
                        which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.2]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not cross the double yellow lines to the
                        left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8136, out 837, 13.52 s

bdd100k_val__c121b93f-b2ee73d4 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, driving straight ahead. There are no immediate
                        intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway. Photo 2 shows
                        this solid white line next to my car, separating the lane from a shoulder/parking area
                        where a white car is parked.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and my position as
                        index 2 agree with having a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: There are no markings in
                        my lane to contradict. | unseen: No attributes were reported that were not visible. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane.
                        [CN-5.4.1]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not cross the solid white
                        line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 917, 13.36 s

bdd100k_val__c1589305-200e315b | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban city road in the United States, approaching a
                        crosswalk and intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): Photo 1 and Photo 2 show a solid white line across the lane,
                        just before the crosswalk.; line:crosswalk (full): Photo 1 and Photo 2 show a white
                        zebra-style crosswalk across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        correctly serve as lane lines separating traffic in the same direction. | markings:
                        The stop line and crosswalk are consistent with an urban intersection approach. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means the car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            line:stop_line: The stop line marks where the vehicle should stop when yielding or
                        waiting to proceed. [CN-6.4.1-2]
Step 5  Rule            line:crosswalk: The crosswalk is an area for pedestrians and does not govern the seven
                        specific vehicle actions. [null]
Step 6  change_left     allowed (contested, label not_determined): allowed: governed by a broken white lane
                        line [CN-5.2.1-2].
Step 6  change_right    allowed (contested, label not_determined): allowed: governed by a broken white lane
                        line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight, and the
                        boundaries do not prohibit it.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes. Be prepared to
                        stop at the stop line for the crosswalk and intersection.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions []
Tokens                  in 8136, out 1055, 14.68 s

bdd100k_val__c15c29a5-74788f46 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban city road in the United States, heading
                        straight toward a distant intersection. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow line separating my lane from the opposite direction of traffic.
                        Photo 2 shows this line is a single solid yellow line next to my car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line on the right. Photo 2 shows a single solid white line next
                        to my car, which continues as a solid white line further ahead.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and ego_lane_index
                        (2) are inconsistent with the boundaries. A yellow center line on the left and a white
                        edge line on the right indicate my lane is the only lane in my direction, or the
                        leftmost lane of a one-way street. However, the yellow line indicates opposing
                        traffic. Therefore, my lane is the only lane for my direction of travel. | roles: The
                        yellow solid line fits the role of a center_line; the white solid line fits the role
                        of an edge_line. | markings: No markings in lane; consistent with boundaries. |
                        unseen: no | result: corrected lane_count to 1 and ego_lane_index to 1
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: An edge line on the right side of the direction of travel shall be
                        white. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the yellow center line or the
                        white edge line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 879, 13.81 s

bdd100k_val__c1627cd8-d8c10968 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road at night, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a solid yellow line
                        next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a broken white line next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:only (full): Photo 1 and Photo 2 show the word 'ONLY' painted in white in the
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: The yellow center line on the left and
                        white lane line on the right agree that my lane is the leftmost lane of my direction.
                        | roles: The yellow color for the center line and white for the lane line fit their
                        roles. | markings: The word 'ONLY' is present, but there is no accompanying arrow to
                        specify the movement. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            text:only: The word 'ONLY' indicates the lane is restricted to a specific movement,
                        but the movement is not specified by an arrow.
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     not_determined (WRONG, label allowed): not_determined because the 'ONLY' text
                        restricts the lane but no arrow specifies if straight is allowed
Step 6  turn_left       not_determined (WRONG, label prohibited): not_determined because no arrow specifies if
                        left turn is allowed
Step 6  turn_right      not_determined (WRONG, label prohibited): not_determined because no arrow specifies if
                        right turn is allowed
Step 6  u_turn          not_determined (WRONG, label prohibited): not_determined because no arrow specifies if
                        U-turn is allowed
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a restricted lane ('ONLY'), but the specific allowed movement is not
                        visible. You cannot change left, but you can change right to a through lane if needed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['arrow:straight']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8136, out 927, 14.51 s

bdd100k_val__c173438f-01b0b013 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway at night, traveling straight ahead. (lanes 3, mine
                        3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway. Photo 2 shows
                        this solid white line continuing next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position as
                        the 3rd lane (rightmost) agree with having a lane line on the left and an edge line on
                        the right. | roles: The white broken line on the left fits the role of a lane line,
                        and the white solid line on the right fits the role of an edge line. | markings: There
                        are no markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lanes.
                        [CN-5.4.1]
Step 5  Rule            right_boundary: The solid line means crossing it is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which allows
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line, which prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on your right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings None (added None, missed
                        None), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 899, 14.14 s

bdd100k_val__c1b3582d-b9c87c82 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection. There is a yellow vehicle ahead
                        in the same direction. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a single broken white line with a clear gap and dash next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the edge of the roadway. Photo 2 shows a
                        solid white line next to the car, and further ahead it remains solid.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: white dashed
                        line as lane_line and white solid line as edge_line are consistent | markings: no
                        markings present in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 819, 12.72 s

bdd100k_val__c1b5a91c-9e402e78 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway with a concrete barrier on the left and a
                        wall on the right. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms a
                        single solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dash and a gap immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left indicates the leftmost lane
                        of the direction of travel, and a white lane line on the right indicates another lane
                        of the same direction. | roles: The yellow solid line on the left fits the role of a
                        left edge line; the white broken line on the right fits the role of a crossable lane
                        line. | markings: No markings are present in the lane, which is consistent with the
                        boundaries. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid line and a concrete
                        barrier, and CN-4.2.2-a prohibits crossing solid lines.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which
                        CN-5.2.1-2 allows crossing.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you cannot move left due to the concrete barrier and solid yellow line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 881, 13.66 s

bdd100k_val__c2021c8c-474a8eda | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban city street in the United States, driving straight
                        ahead towards a distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        sides. | roles: the white dashed lines on both sides fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: there are no markings in
                        my lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this
                        movement.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 834, 12.94 s

bdd100k_val__c264943c-5e493c9f | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street in the United States, driving straight ahead on a multi-
                        lane road with buildings on both sides. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms the double solid yellow line next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the rightmost lane. Photo 2
                        shows a white broken line with several dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 both show the word 'SCHOOL' painted in white
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my lane position
                        (2) agree with the boundaries: a center line on the left and a lane line on the right.
                        | roles: the double solid yellow line fits the role of a center line; the broken white
                        line fits the role of a lane line. | markings: the word 'SCHOOL' is a warning marking
                        and does not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            text:other: The word 'SCHOOL' is informative and does not restrict movement.
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  change_right    allowed (contested, label prohibited): allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this, though the center
                        line prohibits crossing to start one.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane if needed. Be alert for children as you
                        are approaching a school zone.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 8136, out 940, 20.21 s

bdd100k_val__c28b60fb-a5e9b955 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway heading towards an overpass or bridge structure.
                        (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms a
                        single solid yellow line immediately to the left of the car, running alongside a
                        concrete wall.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a single white dash and a gap immediately to the right of the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left indicates the leftmost lane
                        of the direction of travel, and a white lane line on the right indicates another lane
                        of the same direction. | roles: The yellow solid line on the left fits the role of a
                        left edge line; the white broken line on the right fits the role of a crossable lane
                        line. | markings: No markings are present in the lane, which is consistent with a
                        standard highway through-lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid line and is accompanied
                        by a concrete barrier [CN-4.2.2-a].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action here.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action here.
Step 6  u_turn          not_applicable: not_applicable: no arrow or intersection governs this action here.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right. Do not attempt to cross the left
                        boundary due to the solid line and concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 882, 14.42 s

bdd100k_val__c2fb790e-4cd5a630 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which remains broken further ahead.
                        Photo 2 confirms a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows the word 'ONLY' painted in white in the lane to the
                        left of my car, not in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: white broken
                        lines are consistent with lane_line roles separating traffic in the same direction. |
                        markings: the 'ONLY' text is in the adjacent left lane, not my lane; my lane has no
                        markings. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings in my lane restricting
                        this movement.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        action in my lane.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this action in my lane.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this action in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area in or next to my lane.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed []), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8136, out 901, 14.23 s

bdd100k_val__c300fd4b-8ff92c2d | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road under an overpass, traveling straight ahead. (lanes 1, mine
                        1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 confirms a solid yellow line
                        next to the car, extending further ahead.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a concrete barrier on the right. Photo 2 shows the concrete barrier
                        immediately next to the car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and a barrier on the right indicate a single lane of travel in
                        this direction. | roles: the yellow color of the left boundary fits the role of a
                        center line separating opposing traffic. | markings: no markings in the lane to
                        contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The concrete barrier physically prohibits leaving the lane to the
                        right. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4].
Step 6  change_right    prohibited (correct): prohibited by the concrete barrier.
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          prohibited: prohibited by the solid yellow center line [CN-6.1.4].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight; lane changes and U-turns are
                        prohibited.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 8136, out 769, 27.58 s

bdd100k_val__c3026ac7-8105e9a9 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road heading towards an intersection. There are
                        several vehicles ahead in the same direction. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car and further ahead. Photo 2 shows a
                        white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car and further ahead. Photo 2 shows a
                        white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right | roles: white dashed lines
                        are consistent with lane_line roles separating traffic in the same direction |
                        markings: no markings were observed in the lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this
Step 6  u_turn          not_applicable: not_applicable as there is no arrow governing this
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 787, 13.25 s

bdd100k_val__c308561a-1b698bb4 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a sound wall on the right; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the road, followed by a
                        concrete barrier/curb. Photo 2 shows the solid white line next to my car and the
                        concrete curb immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my position (2)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        fits the role of a right edge line. | markings: no markings in my lane to check. |
                        unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means I may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [[CN-4.2.2-a]]
Step 6  change_left     allowed (WRONG, label not_determined): allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 854, 13.01 s

bdd100k_val__c31d9531-694298f0 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway with a stone wall and barrier on the
                        right side. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a concrete barrier on the right. Photo 2
                        shows the solid white line and the concrete barrier immediately to the right of my
                        lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position in
                        the middle lane (index 2) agree with having a lane line on the left and an edge line
                        on the right | roles: the white dashed line on the left fits the role of a lane line,
                        and the white solid line on the right fits the role of an edge line | markings: no
                        markings in my lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by the solid white edge line
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection in view
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection in view
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection in view
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You may change lanes to the left, but you must not cross the solid white line to the
                        right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 733, 11.97 s

bdd100k_val__c3321660-e6b60390 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane city road at night, approaching an intersection. (lanes 3,
                        mine 2, full)
Step 2  Left            Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to the car, which continues ahead. Photo 2
                        confirms a white broken line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 1 and Photo 2 both show a white straight-ahead arrow in
                        my lane.; line:stop_line (full): Photo 1 and Photo 2 show a solid white line across
                        the lane ahead of the car.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the presence of lane lines on both sides | roles: white dashed lines correctly
                        serve as lane lines between lanes of the same direction | markings: the straight arrow
                        and stop line are consistent with a through lane at an intersection | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            arrow:straight: The guide arrow indicates the direction of travel is straight ahead.
                        [CN-5.13.1]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [CN-6.4.1-2]
Step 6  change_left     allowed (contested, correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (contested, correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may go straight or change lanes, but you cannot turn
                        left or right from this lane. Stop at the stop line and follow the traffic signal.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 1032, 14.97 s

bdd100k_val__c3bb4925-f78e285a | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, likely a bridge or overpass, heading straight
                        ahead. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the roadway. Photo 2 shows the
                        same solid yellow line next to the car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with several dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (3) and ego position (1)
                        agree with the boundaries: a yellow edge line on the left indicates the leftmost lane
                        of the direction of travel, and a white lane line on the right indicates another lane
                        of the same direction. | roles: The yellow solid line fits the role of a left edge
                        line; the white broken line fits the role of a crossable lane line. | markings: No
                        markings are present in the lane, which is consistent with the boundaries. | unseen:
                        No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid yellow
                        line, and according to CN-4.2.2-a, a solid line means crossing is normally prohibited.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which according
                        to CN-5.2.1-2 and CN-4.2.2-a may be crossed.
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
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 908, 16.37 s

bdd100k_val__c4057c0c-000a6aaf | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street in the United States, driving straight ahead towards an
                        intersection. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a yellow line to the left of my car, which is broken. Photo 2 confirms a
                        yellow broken line next to my car.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my car. Photo 2 shows a white broken
                        line with clear dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count (2) and my position (1)
                        agree with the boundaries: a center line on the left and a lane line on the right. |
                        roles: The yellow dashed line on the left fits the role of a crossable center line;
                        the white dashed line on the right fits the role of a crossable lane line. | markings:
                        There are no markings in my lane to contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The broken white lane line may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken yellow center line [CN-5.1.1]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, label stop_first): allowed as there are no markings restricting it
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may proceed straight or change
                        lanes to the right.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['text:stop']), actions False, unsafe ['change_left', 'change_right'], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 822, 12.46 s

bdd100k_val__c47fb4ff-92db68d6 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road passing under a bridge, with a concrete wall on
                        the right. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 confirms
                        a broken white line with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, bordering a concrete wall. Photo 2
                        confirms a solid white line and a raised concrete curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings in the lane
                        to contradict. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white edge line marks the right-hand edge of the direction
                        of travel. [CN-5.4.1]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white line (CN-4.2.2-a) and there is a physical curb.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not attempt to move right as it is the edge of the roadway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 854, 12.95 s

bdd100k_val__c4b3ab99-a4a09eeb | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a stone wall on the right and an overpass
                        on the left, heading towards a distant intersection. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white line that is broken near the car and becomes solid further
                        ahead. Photo 2 shows a white broken line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line along the edge of the road. Photo 2 shows a solid
                        white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        area:channelizing (full): Photo 1 shows a white area with diagonal lines (chevrons) to
                        the left of my lane, separating it from a merging or exiting area.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the right boundary being an edge_line and the left boundary being a
                        lane_line. | roles: The white color and dashed/solid patterns fit the roles of
                        lane_line and edge_line for traffic in the same direction. | markings: The
                        channelizing area is to the left of the lane, which is consistent with the lane
                        boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [[CN-4.2.2-a]]
Step 5  Rule            area:channelizing: Vehicles may not drive on or across the channelizing lines.
                        [[CN-6.6.1-3]]
Step 6  change_left     allowed (contested, correct): allowed: the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present in my lane.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['area:channelizing'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 981, 13.79 s

bdd100k_val__c4b3ce3d-cdc056ce | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in the United States, moving straight
                        ahead on a road with no immediate intersection or ramp. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of several long white
                        dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a shoulder and a metal
                        guardrail. Photo 2 shows the solid white line next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings in my lane to
                        check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  turn_right      not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  u_turn          not_applicable: not_applicable as there is no intersection or arrow governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 849, 16.12 s

bdd100k_val__c4e97226-7be7eef5 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a brick wall on the right; the road
                        continues straight ahead. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line next to my car and further ahead. Photo 2 shows a
                        white broken line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line next to my car and further ahead. Photo 2 shows a
                        white broken line with short dashes and short gaps.
                        white dotted, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a lane line on the left and an edge line on the right
                        indicate the rightmost lane. | roles: the white color and dashed/dotted patterns fit
                        the roles of lane line and edge line respectively. | markings: no markings in my lane
                        to check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken edge line indicates the edge of the roadway and may be
                        crossed. [CN-5.4.2]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white lane line
                        (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white edge line (CN-5.4.2).
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 828, 12.36 s

bdd100k_val__c4ee0cc4-b7af9602 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road at night, approaching a section with
                        other vehicles ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a dark area to the left with no visible paint, bordered by a curb and a
                        fence. Photo 2 confirms the absence of any painted line next to the car, showing only
                        the edge of the pavement and a raised curb.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line next to the car, with one clear dash and one gap visible.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a curb/edge on the left and a lane line on the right. |
                        roles: The white dashed line on the right fits the role of a lane line separating
                        traffic in the same direction. | markings: No markings were observed in the lane. |
                        unseen: No | result: consistent
Step 5  Rule            left_boundary: The left boundary is a road edge marked by a curb, which defines the
                        limit of the motor vehicle lane. [CN-5.4.1]
Step 5  Rule            right_boundary: A broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a raised curb, which physically
                        prevents leaving the lane to the left.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which allows
                        crossing according to rule [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right,
                        but you cannot move left due to the curb.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        []
Tokens                  in 8136, out 871, 15.65 s

bdd100k_val__c5588233-b03622f3 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway with a concrete barrier on the left, heading
                        towards a stretch of road with other vehicles. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 confirms the
                        solid yellow line and the concrete barrier immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with visible dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        yellow edge line on the left indicates the leftmost lane of the direction of travel. |
                        roles: the yellow solid line fits the role of a left edge line, and the white broken
                        line fits the role of a lane line. | markings: no markings are present in the lane,
                        which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow line and concrete barrier
                        (CN-4.2.2-a).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or intersection in view.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane or change to the right lane if needed. Do not cross the left
                        boundary due to the concrete barrier and solid line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 840, 8.84 s

bdd100k_val__c561cb9a-aafc0bad | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 2, mine 2,
                        full)
Step 2  Left            Photo 1 shows a white broken line next to the car that becomes a solid white line
                        further ahead. Photo 2 shows a white broken line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and continuing ahead. Photo 2 shows a
                        solid white line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white broken line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: The straight-ahead arrow
                        is consistent with the lane boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white edge line marks the boundary of the motor vehicle
                        lane. [CN-5.4.1]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the lane is for traveling
                        straight. [CN-5.13.1]
Step 6  change_left     allowed (contested, label prohibited): allowed because the left boundary is a broken
                        white line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (correct): allowed because the lane marking is a straight-ahead arrow
                        (CN-5.13.1).
Step 6  turn_left       prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only (CN-5.13.1).
Step 6  turn_right      prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only (CN-5.13.1).
Step 6  u_turn          prohibited (correct): prohibited because the lane marking is a straight-ahead arrow,
                        which restricts movement to straight only (CN-5.13.1).
Step 6  enter_waiting_areanot_applicable: not_applicable because there is no waiting area in or next to my
                          lane.
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change to the left lane if needed, but do
                        not cross the solid white line on the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['text:only']), actions True, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8136, out 1000, 16.4 s

bdd100k_val__c65c2462-96e8ae92 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway heading towards an overpass. (lanes 3, mine 3,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, followed by a concrete barrier. Photo 2
                        shows the solid white line next to my car and the concrete barrier immediately to its
                        right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and my position in
                        the 3rd lane agree with having a lane line on the left and an edge line on the right.
                        | roles: The white dashed line on the left fits the role of a lane line; the white
                        solid line and curb on the right fit the role of an edge line. | markings: No markings
                        were observed in my lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white line [CN-4.2.2-a] and there is a concrete barrier.
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but you cannot move further right due to the solid line and concrete barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 855, 13.64 s

bdd100k_val__c66d2237-f9c0a1ef | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, heading towards an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (WRONG, label prohibited): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8136, out 780, 12.63 s

bdd100k_val__c68f8fd2-61681484 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane highway in the United States, traveling straight ahead on a
                        road with several lanes of traffic in the same direction. (lanes 4, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line to the left of my car. Photo 2 shows a white broken
                        line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line to the right of my car, and further ahead, a
                        concrete barrier. Photo 2 shows a white broken line with long dashes and gaps next to
                        my car.
                        white dashed, curb yes, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (4) and my lane position
                        (3) agree with the boundaries; there are lane lines on both sides, meaning there are
                        lanes to my left and right. | roles: the white dashed lines fit the role of crossable
                        lane lines separating traffic in the same direction. | markings: there are no markings
                        in my lane to contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right allowed across a curb']
Tokens                  in 8136, out 838, 12.7 s

bdd100k_val__c6d77a40-03423c96 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city street with buildings and trees on both sides, driving straight
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white broken line extending forward. Photo 2 shows a white broken line
                        next to the car with one visible dash and one gap.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car and further ahead. Photo 2 shows a
                        solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and index 1 agree
                        with the boundaries: a lane line on the left indicates another lane of the same
                        direction, and an edge line on the right indicates the road edge. | roles: The white
                        dashed line on the left fits the role of a crossable lane line, and the white solid
                        line on the right fits the role of a road edge line. | markings: No markings are
                        present in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white edge line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there is no arrow or waiting area governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid white
                        line on the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['leftmost
                        lane, but a lane line on the left']
Tokens                  in 8136, out 847, 13.85 s

bdd100k_val__c6dca574-6e641016 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with parked cars on the left and a sidewalk on the
                        right. The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a concrete curb on the right. Photo 2 shows the concrete curb
                        immediately next to the car with no painted line on the pavement.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 1 and position 1 agree
                        with a center line on the left and a curb on the right | roles: the double solid
                        yellow line fits the role of a no-crossing center line; the curb fits the role of a
                        road edge | markings: no markings in lane to check | unseen: no | result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The curb marks the edge of the roadway. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the physical curb [CN-5.4.1]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or waiting area
Step 6  u_turn          not_applicable: not_applicable as there is no arrow or waiting area
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines or drive
                        onto the curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 804, 10.62 s

bdd100k_val__c6dcc1a9-0fa80e62 | lane | Test C | gemma4:31b
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
                        the middle lane (index 2) agree with having lane lines on both the left and right
                        sides. | roles: the white dashed lines on both sides fit the role of crossable lane
                        lines separating traffic in the same direction. | markings: there are no markings in
                        my lane, which is consistent with a standard highway through lane. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line means it may be crossed to change lanes.
                        [CN-5.2.1-2]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or intersection markings
                        governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area or two-way left-turn
                          lane.
Step 7  Reflect         consistent
Advice                  You are in the center lane of a three-lane highway. You may continue straight or
                        change lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 856, 28.84 s

bdd100k_val__c6e1c974-906461f4 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with several dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues ahead. Photo 2
                        confirms a single solid white line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the lane.;
                        text:only (full): Photo 2 shows the word 'ONLY' painted in white in the lane, above
                        the arrow.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right. | roles: White dashed and
                        solid lines are consistent with lane lines separating traffic in the same direction. |
                        markings: The straight arrow and 'ONLY' text are consistent with a dedicated through
                        lane. | unseen: no | result: consistent
Step 5  Rule            left_boundary: A broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: A solid white lane line prohibits crossing from the solid side.
                        [CN-6.2.1]
Step 5  Rule            arrow:straight: The arrow indicates the lane is for traveling straight ahead.
                        [CN-5.13.1]
Step 5  Rule            text:only: The text 'ONLY' indicates that only the movement shown by the associated
                        arrow is permitted. [CN-5.14.1]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (WRONG, label allowed): prohibited because the right boundary is a solid
                        white line [CN-6.2.1].
Step 6  go_straight     allowed (correct): allowed because the lane has a straight-ahead arrow [CN-5.13.1].
Step 6  turn_left       prohibited (correct): prohibited because the 'ONLY' text and straight arrow restrict
                        movement to straight ahead [CN-5.13.1, CN-5.14.1].
Step 6  turn_right      prohibited (correct): prohibited because the 'ONLY' text and straight arrow restrict
                        movement to straight ahead [CN-5.13.1, CN-5.14.1].
Step 6  u_turn          prohibited (correct): prohibited because the 'ONLY' text and straight arrow restrict
                        movement to straight ahead [CN-5.13.1, CN-5.14.1].
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  You are in a dedicated through lane. You may proceed straight or change to the left
                        lane, but you cannot change to the right or turn at the intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 1089, 16.73 s

bdd100k_val__c6ed8102-2bbcbcc2 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway or urban arterial road, approaching an
                        area with overhead structures and signage. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        confirms a broken white line with clear dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, with a metal guardrail running
                        parallel to it. Photo 2 shows the solid white line and the guardrail clearly.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings are present
                        in the lane, which is consistent with the boundaries. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white edge line marks the right-hand edge of the roadway.
                        [CN-5.4.1]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken white line, which allows
                        crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line and a physical guardrail, which prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the right edge line into the guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 867, 15.49 s

bdd100k_val__c85416bd-db975d94 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road in the United States, traveling straight ahead on a
                        clear stretch of road. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows the same white broken line next to the car, consisting of long dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway. Photo 2 shows
                        this solid white line next to the car, with no curb visible.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego_lane_index 3
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line fits the role of a lane line, and the white solid line
                        fits the role of a right edge line. | markings: There are no markings in the lane to
                        contradict. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line (CN-4.2.2-a).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 847, 12.84 s

bdd100k_val__c8a7a62d-e58e7297 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road with buildings on both sides, approaching an intersection.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line extending from the bottom towards the intersection.
                        Photo 2 shows the same solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows the road edge meeting a sidewalk with a curb. Photo 2 shows the pavement
                        ending at a raised concrete curb.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show the word 'SCHOOL' painted in white across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and a curb on the right indicate a single lane for my
                        direction. | roles: the yellow color of the left boundary fits the role of a center
                        line; the curb on the right fits the role of an edge line. | markings: the word
                        'SCHOOL' is informative and does not contradict the boundaries. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The physical curb prohibits leaving the roadway to the right. [null]
Step 5  Rule            text:other: The word 'SCHOOL' is informative and does not govern the seven actions.
                        [null]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by the physical curb
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as there is no arrow in my lane
Step 6  turn_right      not_applicable: not_applicable as there is no arrow in my lane
Step 6  u_turn          not_applicable: not_applicable as there is no arrow in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable as there is no waiting area
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be alert for children as you are entering a
                        school zone.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8136, out 880, 13.09 s

bdd100k_val__c8e01103-9ff8595d | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a city road approaching an intersection with a crosswalk and traffic
                        signals ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left. Photo 2 shows the same solid yellow
                        line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right. Photo 2 shows the same solid white line
                        next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow in the lane. Photo 1
                        shows the same arrow.; line:stop_line (full): Photo 1 shows a white solid stop line
                        across the lane before the crosswalk.; line:crosswalk (full): Photo 1 shows a white
                        zebra-style crosswalk across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with a center line on the left and an edge line on the right. | roles: The yellow
                        solid line on the left fits the role of a no-crossing center line; the white solid
                        line on the right fits the role of a road edge line. | markings: The straight arrow
                        and stop line are consistent with a single through lane. | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: The white edge line marks the boundary between motor vehicle lanes and
                        the roadside. [[CN-5.4.1]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [[CN-5.13.1]]
Step 5  Rule            line:stop_line: The stop line marks where vehicles stop when yielding or waiting to
                        proceed. [[CN-6.4.1-2]]
Step 5  Rule            line:crosswalk: The crosswalk is for pedestrians and does not govern vehicle movement
                        actions other than yielding. [null]
Step 6  change_left     prohibited (contested, label not_determined): prohibited by the solid yellow center
                        line [CN-6.1.4]
Step 6  change_right    prohibited (contested, label not_determined): prohibited by the solid white edge line
                        [CN-5.4.1]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Stop at the stop line for the traffic signal
                        and yield to pedestrians in the crosswalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8136, out 1135, 16.74 s

bdd100k_val__c909551e-fb24caeb | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban city road in the United States, approaching an
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car and further ahead. Photo 2 confirms
                        a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car and further ahead. Photo 2 confirms
                        a broken white line with several long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 3 and ego position 2
                        agree with having lane lines on both the left and right. | roles: White dashed lines
                        are consistent with lane lines separating traffic in the same direction. | markings:
                        No markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The broken white lane line may be crossed. [CN-5.2.1-2]
Step 6  change_left     allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    allowed (correct): Allowed by the broken white lane line (CN-5.2.1-2).
Step 6  go_straight     allowed (contested, correct): Allowed as there are no markings restricting it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow in the lane.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow in the lane.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow in the lane.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the center lane. You may proceed straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 777, 11.99 s

bdd100k_val__c90b5398-8d49f2f2 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road, traveling straight ahead. There are no
                        immediate intersections or ramps visible in the foreground. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to the car, with several distinct dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway, followed by a
                        curb. Photo 2 shows the solid white line and the edge of the pavement next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 2
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: The white dashed line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: No markings were observed
                        in the lane, which is consistent with the boundaries. | unseen: No attributes were
                        reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line indicates that vehicles may cross it to
                        change lanes. [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken white
                        line, which permits crossing per CN-5.2.1-2.
Step 6  change_right    prohibited (WRONG, label allowed): prohibited: the right boundary is a solid white
                        line, which prohibits crossing per CN-4.2.2-a.
Step 6  go_straight     allowed (contested, correct): allowed: no markings restrict going straight in this
                        lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change to the left lane. Do not cross the solid white
                        line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 872, 41.8 s

bdd100k_val__c90c8198-f73aed79 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with buildings and parked cars on the right. The
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a double solid yellow line separating my lane from the opposite
                        direction. Photo 2 confirms two solid yellow lines side by side next to my car.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, but a line of parked cars and a curb.
                        Photo 2 shows the asphalt ending at a concrete curb next to the car.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (1) and position (1)
                        agree with the center line on the left and the curb on the right. | roles: the double
                        solid yellow line fits the role of a no-crossing center line; the curb fits the role
                        of a road edge. | markings: no markings in the lane to contradict. | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: A double solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.2]]
Step 5  Rule            right_boundary: The road edge is marked by a curb, which defines the boundary of the
                        motor vehicle lane. [[CN-5.4.1]]
Step 6  change_left     prohibited (correct): prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  change_right    prohibited: prohibited by the physical curb [CN-5.4.1].
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow governing this movement.
Step 6  u_turn          prohibited: prohibited by the double solid yellow center line [CN-6.1.2].
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines to the
                        left or drive onto the curb to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions ['u_turn
                        decided without an arrow or prohibited-movement marking']
Tokens                  in 8136, out 838, 12.86 s

bdd100k_val__c9283177-4ac407c3 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane urban road. Ahead is a clear stretch of road with
                        other vehicles in the same direction. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the left edge of the road, next to a metal
                        guardrail. Photo 2 confirms the solid yellow line immediately to the left of the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a white dashed line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 2 and ego_lane_index 1
                        agree with the boundaries: a yellow edge line on the left and a white lane line on the
                        right. | roles: The yellow solid line on the left fits the role of a left edge line;
                        the white broken line on the right fits the role of a lane line. | markings: No
                        markings were observed in the lane. | unseen: No | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left marks the edge of the roadway.
                        [CN-5.4.3]
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2]
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow line, and
                        according to CN-4.2.2-a, crossing a solid line is normally prohibited.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which according
                        to CN-5.2.1-2 and CN-4.2.2-a may be crossed.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but do not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 891, 14.22 s

bdd100k_val__c94d8213-1f593522 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a junction or ramp area with
                        concrete barriers on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with clear gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a concrete barrier. Photo 2 shows a solid
                        white line and the base of the concrete barrier.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (2) and my position (2)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line fits the role of a lane line, and the white solid line
                        next to a barrier fits the role of an edge line. | markings: no markings in my lane to
                        check. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 6  change_left     allowed (contested, label not_determined): allowed by the broken white lane line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line [CN-4.2.2-a]
                        and the physical concrete barrier.
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict carrying on straight.
Step 6  turn_left       not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  turn_right      not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  u_turn          not_applicable: not_applicable as there are no arrows or waiting areas governing this.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change to the left lane. Do not attempt to move right due
                        to the solid line and concrete barrier.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 829, 12.18 s

bdd100k_val__c9b099e4-6ab2e4f4 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane highway with a concrete barrier and shoulder to the
                        right, approaching overhead signs. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to the car, with visible dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the edge of the roadway, followed by a
                        concrete barrier. Photo 2 shows the solid white line and the concrete barrier
                        immediately to the right of the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and ego position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white dashed line fits the role of a lane line; the white solid line fits
                        the role of an edge line. | markings: no markings in lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line means crossing it is normally prohibited.
                        [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2).
Step 6  change_right    prohibited (contested, correct): prohibited by the solid white edge line (CN-4.2.2-a)
                        and the physical concrete barrier.
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
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 849, 13.03 s

bdd100k_val__ca146661-7f70d0c4 | lane | Test C | gemma4:31b
-----------------------------------------------------------
Step 1  Scene           The car is traveling on a multi-lane highway in the United States, moving straight
                        ahead on a clear road. (lanes 3, mine 3, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 confirms this is a broken white line with clear gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the roadway. Photo 2 shows
                        this solid white line continuing next to my car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count (3) and my position (3)
                        agree with the boundaries: a lane line on the left and an edge line on the right. |
                        roles: the white broken line on the left fits the role of a lane line; the white solid
                        line on the right fits the role of an edge line. | markings: no markings are present
                        in my lane, which is consistent with the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed for lane changes.
                        [CN-5.2.1-2]
Step 5  Rule            right_boundary: The solid white line means crossing is normally prohibited.
                        [CN-4.2.2-a]
Step 6  change_left     allowed (correct): allowed because the left boundary is a broken white line
                        [CN-5.2.1-2].
Step 6  change_right    prohibited (contested, correct): prohibited because the right boundary is a solid
                        white line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  turn_right      not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  u_turn          not_applicable: not_applicable because there are no arrows or waiting areas governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable because no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change to the left lane,
                        but do not cross the solid white line to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8136, out 853, 12.8 s
```
