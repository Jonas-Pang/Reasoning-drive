# Reasoning of lane run 20261118_001407_laneB_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road in China with traffic moving in the same direction; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken yellow line separating my lane from the lane to the left. Photo
                        2 shows the same broken yellow line next to my car, with long dashes and gaps.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, with a metal guardrail beyond it. Photo
                        2 shows the solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left indicates my lane is the
                        leftmost of the motor vehicle lanes in this direction, but the scene shows another
                        lane to the left, meaning the yellow line separates opposing traffic flows. | roles:
                        the yellow dashed line fits the role of a crossable center line, and the white solid
                        line fits the role of a road edge line. | markings: no markings in my lane to
                        contradict boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     allowed (correct): allowed: the left boundary is a broken yellow center line
                        [CN-5.1.1].
Step 6  change_right    prohibited (correct): prohibited: the right boundary is a solid white edge line
                        [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You may continue straight or change lanes to the left by crossing the yellow broken
                        line if safe. Do not cross the solid white line to the right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 888, 6.56 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane road in China with traffic moving in the same direction; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line marking the right edge of the road, with a metal
                        guardrail beyond it. Photo 2 shows the same solid white line next to my car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 2 and ego_lane_index 2
                        agree with a lane line on the left and an edge line on the right | roles: the white
                        dashed line fits the role of a crossable lane line, and the white solid line fits the
                        role of a road edge line | markings: no markings in my lane, consistent with
                        boundaries | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means it may be crossed to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line and physical guardrail
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane. You may continue straight or change lanes to the left,
                        but you must not cross the right edge line into the guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 840, 5.48 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China with traffic moving in the same direction; the road
                        continues straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long white dashes and
                        gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a solid white line on the right, with a metal guardrail further right.
                        Photo 2 shows the solid white line next to my car and the guardrail beside it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The solid white line marks the edge of the motor vehicle lane.
                        [[CN-5.4.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    prohibited (correct): prohibited by the solid edge line and physical guardrail
                        [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the rightmost lane of the carriageway. You may continue straight or change
                        into the left lane, but you cannot leave the road to the right due to the edge line
                        and guardrail.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 786, 19.88 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The road is a multi-lane urban road with a physical barrier on the right. My car is in
                        a lane traveling straight ahead. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a broken yellow line separating my lane from the lane to the left. Photo
                        2 shows a broken yellow line with long dashes and gaps next to my car.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a physical barrier. Photo 2 shows a solid white
                        line next to my car and a raised barrier/curb immediately to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a center line on the left indicates my lane is the
                        leftmost of the direction of travel (or the rightmost of a two-lane road where the
                        other lane is for opposite traffic, but here it separates flows in the same direction
                        as seen by the cars ahead), however, the yellow color indicates it separates opposite
                        directions, making my lane the leftmost of my direction. | roles: the yellow dashed
                        line fits the role of a crossable center line; the white solid line fits the role of
                        an edge line. | markings: no markings in my lane to contradict boundaries. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The white solid line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken yellow
                        line [CN-5.1.1].
Step 6  change_right    prohibited (contested, correct): prohibited: the right boundary is a solid white edge
                        line [CN-4.2.2-a] and there is a physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the left. Changing to the right is
                        prohibited due to the solid edge line and physical barrier.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 929, 5.1 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, traveling straight ahead on a road
                        with a concrete barrier on the right. (lanes 2, mine 2, full)
Step 2  Left            Photo 1 shows a yellow broken line separating my lane from the lane to the left. Photo
                        2 shows a yellow broken line with long dashes and gaps next to my car.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a solid white line and a concrete barrier. Photo 2 shows a solid white
                        line next to my car and a concrete barrier to its right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:bus (full): Photo 2 shows white characters '公交' (bus) painted vertically in my
                        lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent; a center line on the left
                        and an edge line on the right indicate my lane is the leftmost of my direction (though
                        lane_count is 2, the yellow line indicates the start of opposing traffic or a special
                        lane; however, looking at the flow, it's a bus lane separating from general traffic) |
                        roles: consistent | markings: consistent; the '公交' text identifies this as a bus lane
                        | unseen: none | result: consistent
Step 5  Rule            left_boundary: Vehicles may cross the broken yellow center line to overtake, turn or
                        make a U-turn when safe. [[CN-5.1.1]]
Step 5  Rule            right_boundary: The white edge line marks the right-hand edge of the direction of
                        travel. [[CN-5.4.3]]
Step 5  Rule            text:bus: Vehicles other than buses shall not enter the bus lane. [[CN-6.9.1]]
Step 6  change_left     allowed (contested, correct): allowed; the left boundary is a broken yellow line
                        [CN-5.1.1].
Step 6  change_right    prohibited (contested, label allowed): prohibited; the right boundary is a solid white
                        line [CN-4.2.2-a] and there is a concrete barrier.
Step 6  go_straight     prohibited (contested, label allowed): prohibited; my car is an ordinary car and the
                        lane is marked as a bus lane [CN-6.9.1].
Step 6  turn_left       prohibited: prohibited; my car is an ordinary car and the lane is marked as a bus lane
                        [CN-6.9.1].
Step 6  turn_right      prohibited: prohibited; my car is an ordinary car and the lane is marked as a bus lane
                        [CN-6.9.1].
Step 6  u_turn          prohibited: prohibited; my car is an ordinary car and the lane is marked as a bus lane
                        [CN-6.9.1].
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are currently in a reserved bus lane. Please change left into the general traffic
                        lane immediately.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation accepted, contradictions ['go_straight,
                        turn_left, turn_right, u_turn decided without an arrow or prohibited-movement
                        marking']
Tokens                  in 8459, out 1023, 8.35 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test B | gemma-4-31b-it
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane road heading towards an underpass. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, which continues as a solid white
                        line further ahead. Photo 2 shows a solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, which continues as a solid white
                        line further ahead. Photo 2 shows a solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white line marks the edge of the motor vehicle lane. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The white line marks the edge of the motor vehicle lane. [[CN-5.4.3]]
Step 6  change_left     prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  change_right    prohibited (correct): prohibited by the solid white edge line [CN-4.2.2-a]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight through the underpass; lane changes are
                        prohibited.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8459, out 741, 18.09 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test B | gemma-4-31b-it
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road with a bus stop on the left and parked scooters on the
                        right, approaching a crosswalk. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line separating the lane from a bus stop area. Photo 2
                        shows the same solid white line next to the car.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to a curb with parked scooters. Photo 2 shows a
                        solid white line and a raised curb next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 shows a white solid line across the lane further ahead,
                        which is a crosswalk.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A solid line means crossing is normally prohibited. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians to cross and does not restrict
                        the car's movement through the lane. [null]
Step 6  change_left     prohibited (correct): prohibited by the solid white left boundary (CN-4.2.2-a)
Step 6  change_right    prohibited (correct): prohibited by the solid white right boundary and curb
                        (CN-4.2.2-a)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Be cautious of pedestrians at the upcoming
                        crosswalk.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8459, out 855, 20.38 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test B | gemma-4-31b-it
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, driving straight ahead towards a
                        distant intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and ego_lane_index 2
                        agree with having lane lines on both the left and right sides. | roles: the white
                        dashed lines correctly fit the role of crossable lane lines separating traffic in the
                        same direction. | markings: consistent; no markings are present in the lane. | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation accepted, contradictions []
Tokens                  in 8459, out 822, 3.84 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test B | gemma-4-31b-it
------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road with a median on the left and a sidewalk on the
                        right, driving straight ahead. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, continuing as a solid yellow line
                        further ahead. Photo 2 shows a solid yellow line next to the car.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues as a broken white
                        line further ahead. Photo 2 shows a broken white line next to the car with several
                        long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and a lane line on the right indicate the leftmost lane of a
                        two-lane road in this direction | roles: the yellow solid line on the left correctly
                        serves as a no-crossing center line, and the white broken line on the right correctly
                        serves as a crossable lane line | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: A broken white lane line may be crossed to change lanes. [CN-5.2.1-2]
                        "The crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 835, 18.04 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection with
                        traffic signals ahead. (lanes 4, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line next to the car, which continues as a broken white
                        line further ahead. Photo 2 shows a broken white line with long dashes and gaps next
                        to the car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues as a broken white
                        line further ahead. Photo 2 shows a broken white line with long dashes and gaps next
                        to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 5  Rule            right_boundary: The broken white lane line separates traffic in the same direction and
                        may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the
                        same direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed: allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed: allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in a through lane; you may go straight or change lanes to the left or right.
                        Follow the traffic signals at the intersection ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8459, out 777, 3.93 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching an intersection. (lanes 2,
                        mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, which continues ahead. Photo 2
                        shows a single solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, which continues ahead. Photo 2
                        shows a broken white line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree; a
                        center line on the left and a lane line on the right indicate the leftmost lane of a
                        multi-lane road | roles: the yellow solid line on the left correctly serves as a no-
                        crossing center line, and the white broken line on the right correctly serves as a
                        crossable lane line | markings: no markings in the lane | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: A broken white lane line may be crossed. [CN-5.2.1-2] "The crossable
                        lane line separates traffic flows in the same direction and is placed between lanes of
                        the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change to the right lane,
                        but you must not cross the solid yellow line to the left.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['symbol:other']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 812, 19.08 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test B | gemma-4-31b-it
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is driving on a multi-lane road, possibly an overpass or highway, with a clear
                        path ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid white line next to the car, continuing ahead. Photo 2 shows a
                        solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a solid white line next to the car, continuing ahead. Photo 2 shows a
                        solid white line next to the car.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The white solid line marks the edge of the motor vehicle lane.
                        [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or non-
                        motorized vehicle lanes, or the boundary between motor vehicle lanes and non-motorized
                        ve"
Step 5  Rule            right_boundary: The white solid line marks the edge of the motor vehicle lane.
                        [CN-5.4.1] "The carriageway edge line marks the edge of motor vehicle lanes or non-
                        motorized vehicle lanes, or the boundary between motor vehicle lanes and non-motorized
                        ve"
Step 6  change_left     prohibited (correct): prohibited; the left boundary is a solid line [CN-4.2.2-a].
Step 6  change_right    prohibited (correct): prohibited; the right boundary is a solid line [CN-4.2.2-a].
Step 6  go_straight     allowed (contested, correct): allowed; no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable; no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable; no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight; lane changes to either side are prohibited by
                        the solid edge lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8459, out 774, 3.72 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test B | gemma-4-31b-it
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway passing under a bridge, with clear road ahead. (lanes 2, mine 1,
                        full)
Step 2  Left            Photo 1 shows a solid yellow line next to the car, continuing ahead. Photo 2 shows a
                        solid yellow line next to the car and a metal guardrail to its left.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [CN-5.2.1-2] "The
                        crossable lane line separates traffic flows in the same direction and is placed
                        between lanes of the same direction. It is a broken white line."
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right lane. Do not cross the solid yellow line to
                        the left.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 739, 15.13 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test B | gemma-4-31b-it
-------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China with overhead signs indicating through lanes and an
                        emergency vehicle lane. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line on the far left, separating the roadway from the
                        median/barrier. Photo 2 shows the same solid yellow line next to my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left side of the direction of travel marks
                        the boundary of the roadway. [CN-5.4.3] "An edge line on the right side of the
                        direction of travel shall be white, and an edge line on the left side of the direction
                        of travel shall be yellow; a motor/"
Step 5  Rule            right_boundary: The broken white lane line separates traffic flows in the same
                        direction and may be crossed. [CN-5.2.1-2] "The crossable lane line separates traffic
                        flows in the same direction and is placed between lanes of the same direction. It is a
                        broken white line."
Step 6  change_left     prohibited (correct): prohibited: the left boundary is a solid yellow line and a
                        physical barrier, and crossing is normally prohibited by CN-4.2.2-a.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line which may
                        be crossed according to CN-5.2.1-2.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost through lane. You may continue straight or change lanes to the
                        right, but you cannot cross the left boundary due to the solid line and barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 822, 4.83 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China, approaching an intersection with traffic signals and
                        buildings on both sides. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible in the center of my
                        lane in both Photo 1 and Photo 2.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
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
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (CN-5.13.1)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. Lane changes to the left or right are permitted.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_left',
                        'change_right'], citation accepted, contradictions []
Tokens                  in 8459, out 894, 16.39 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching an intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line next to the car, continuing ahead. Photo 2 shows a
                        broken white line with long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (full): Photo 1 and Photo 2 show a wide white striped area (crosswalk)
                        across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            line:crosswalk: A crosswalk is an area for pedestrians and does not govern vehicle
                        movements out of the lane. [null]
Step 6  change_left     allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (WRONG, label prohibited): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may proceed straight or change lanes to the left or
                        right. Be mindful of the crosswalk and pedestrians ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:stop_line']), actions False, unsafe ['change_left', 'change_right'],
                        citation unlisted, contradictions []
Tokens                  in 8459, out 854, 4.46 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China, heading straight toward an intersection or a managed
                        section of the road. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means vehicles may cross it to change lanes.
                        [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same direction
                        and is placed between lanes of the same direction. It is a broken white line."
Step 5  Rule            right_boundary: The broken white lane line means vehicles may cross it to change
                        lanes. [CN-5.2.1-2] "The crossable lane line separates traffic flows in the same
                        direction and is placed between lanes of the same direction. It is a broken white
                        line."
Step 6  change_left     allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (CN-5.2.1-2)
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 761, 5.27 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China, heading towards an intersection with overhead lane
                        guidance signs. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line allows crossing for lane changes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line allows crossing for lane changes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane. You may continue straight or change lanes to the left or
                        right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 609, 3.44 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with traffic keeping to the right; the road continues
                        straight ahead. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a white broken line separating my lane from the lane to the left. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken white
                        lane line [CN-5.2.1-2].
Step 6  change_right    allowed (contested, correct): allowed: the right boundary is a broken white lane line
                        [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8459, out 798, 19.19 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane city road in China, approaching an intersection with guide arrows painted
                        in the lanes. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the rightmost lane. Photo 2
                        shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 and Photo 1 show a white arrow pointing straight ahead
                        in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The guide arrow indicates that the lane is for traveling straight
                        ahead. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (correct): allowed by the straight guide arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight guide arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight guide arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight guide arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 884, 5.66 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           The road is a multi-lane urban road in China, straight ahead with an intersection
                        further in the distance. My car is in one of the lanes of travel. (lanes 3, mine 2,
                        full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count of 3 and my position as
                        index 2 agree with having lane lines on both the left and right boundaries | roles:
                        the white dashed pattern fits the role of a crossable lane line | markings: no
                        markings are present in my lane, which is consistent with the boundaries | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  turn_right      not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  u_turn          not_applicable: not_applicable as no arrow or prohibited-movement marking governs this
                        action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the middle lane of a three-lane road. You may continue straight or change
                        lanes to the left or right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 844, 3.32 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in China, approaching a wide intersection or a
                        junction where the road curves slightly to the right. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line that curves to the right. Photo 2 shows the same
                        solid yellow line next to the car.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A single solid yellow line prohibits vehicles in both directions from
                        crossing. [[CN-6.1.4]]
Step 5  Rule            right_boundary: A broken white lane line means it may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (correct): prohibited by the solid yellow center line [CN-6.1.4]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane of your direction. You may continue straight or change
                        lanes to the right, but you must not cross the solid yellow line to the left.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 762, 2.68 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China with an overhead gantry sign indicating through lanes.
                        My car is traveling straight on a wide road. (lanes 5, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line next to a concrete barrier. Photo 2 shows the same
                        solid yellow line and the concrete barrier immediately to the left of my car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the next lane. Photo 2 shows
                        a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and my lane position
                        agree with the boundary roles; a yellow edge line on the left indicates my lane is the
                        leftmost of my direction | roles: the yellow solid line on the left fits the role of a
                        left edge line, and the white broken line on the right fits the role of a crossable
                        lane line | markings: no markings in my lane | unseen: no | result: consistent
Step 5  Rule            left_boundary: An edge line on the left side of the direction of travel shall be
                        yellow. [[CN-5.4.3]]
Step 5  Rule            left_boundary: A solid line means crossing is normally prohibited. [[CN-4.2.2-a]]
Step 5  Rule            right_boundary: A broken white line separates traffic flows in the same direction and
                        may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by the solid yellow edge line and
                        concrete barrier [CN-4.2.2-a]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this action
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this action
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Do not cross the left boundary into the
                        barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added [],
                        missed ['text:other']), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 877, 22.21 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane highway in China, with a clear road ahead and overhead signs in the
                        distance. (lanes 3, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line marking the left edge of the roadway. Photo 2 shows
                        the same solid yellow line next to my car.
                        yellow solid, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows a broken white line with long dashes and gaps next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The yellow edge line on the left side of the direction of travel marks
                        the edge of the roadway. [[CN-5.4.3]]
Step 5  Rule            right_boundary: The broken white lane line separates traffic flows in the same
                        direction and may be crossed. [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a solid yellow
                        edge line, and crossing it would leave the roadway [CN-5.4.3].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line which may
                        be crossed [CN-5.2.1-2].
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  You are in the leftmost lane. You may continue straight or change lanes to the right.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 800, 3.56 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------------
Step 1  Scene           A multi-lane urban road in China with three lanes of travel in my direction, heading
                        towards an intersection. (lanes 3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the lane to the left. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the lane to the right. Photo
                        2 shows the same broken white line next to my car, consisting of long dashes and gaps.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white straight-ahead arrow painted in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: The broken white lane line means my car may cross it to change lanes.
                        [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: The straight-ahead arrow indicates that the lane is for going
                        straight. [[CN-5.13.1]]
Step 6  change_left     allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  change_right    allowed (correct): allowed by the broken white lane line [CN-5.2.1-2]
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow [CN-5.13.1]
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight. You may change lanes to the left or right if needed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8459, out 887, 19.95 s
```
