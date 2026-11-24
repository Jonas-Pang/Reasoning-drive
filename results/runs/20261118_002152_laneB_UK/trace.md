# Reasoning of lane run 20261118_002152_laneB_UK

```text
lingoqa__evaluation_images_val_a1109658670fb29d13ac113d322c004c_2 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, proceeding towards a junction. (lanes
                        3, mine 2, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from the left lane. Photo 2 shows
                        a short broken white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the right lane. Photo 2
                        shows a short broken white line next to my car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): Photo 2 shows a white arrow pointing straight ahead in my lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: I should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            right_boundary: I should keep between the lane dividers. [UK-Rule131] "Lane dividers.
                        These are short, broken white lines which are used on wide carriageways to divide them
                        into lanes. You should keep between them."
Step 5  Rule            arrow:straight: Vehicular traffic must only proceed ahead. [UK-TSRGD-Part6,item20]
                        "Vehicular traffic must only proceed ahead"
Step 6  change_left     allowed (correct): allowed by the broken white lane line (UK-Rule131)
Step 6  change_right    allowed (correct): allowed by the broken white lane line (UK-Rule131)
Step 6  go_straight     allowed (correct): allowed by the straight-ahead arrow (UK-TSRGD-Part6,item20)
Step 6  turn_left       prohibited (correct): prohibited by the straight-ahead arrow (UK-TSRGD-Part6,item20)
Step 6  turn_right      prohibited (correct): prohibited by the straight-ahead arrow (UK-TSRGD-Part6,item20)
Step 6  u_turn          prohibited (correct): prohibited by the straight-ahead arrow (UK-TSRGD-Part6,item20)
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  Stay in this lane to go straight ahead. If you need to turn left or right, you must
                        change lanes first.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['text:speed_limit']), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 14755, out 859, 5.3 s

lingoqa__evaluation_images_val_f6d832c4b3279c6491278500918e792e_2 | lane | Test B | gemma-4-31b-it
--------------------------------------------------------------------------------------------------
Step 1  Scene           Urban road in the UK with buildings on both sides; the road continues straight ahead.
                        (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the edge of the road. Photo 2 shows a double red line
                        next to my car, continuing as a double red line further ahead.
                        other double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line dividing the road. Photo 2 shows a broken white line
                        next to my car, consisting of long dashes and gaps, continuing as a broken white line
                        further ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:speed_limit (full): Photo 2 shows two white circles with the number '20' inside
                        them, one in my lane and one in the lane to the right.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Stopping to park, load/unload or to board and alight is prohibited.
                        [UK-HC_MARKINGS-p2-9] "The times that the red line prohibitions apply are shown on
                        nearby signs, but the double red line ALWAYS means no stopping at any time."
Step 5  Rule            right_boundary: I should keep between these lane dividers. [UK-Rule131] "Lane
                        dividers. These are short, broken white lines which are used on wide carriageways to
                        divide them into lanes. You should keep between them."
Step 5  Rule            text:speed_limit: This is an informative speed limit marking and does not govern the
                        seven actions. [null]
Step 6  change_left     prohibited (contested, label allowed): prohibited: the left boundary is an edge line
                        with a curb and double red lines, and crossing it would leave the carriageway.
Step 6  change_right    allowed (contested, correct): allowed: the right boundary is a broken white lane line,
                        which allows lane changes if safe.
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right if safe. Do not stop or park on the left due
                        to the double red lines. Observe the 20 mph speed limit.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['area:channelizing']), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 14755, out 892, 11.14 s

lingoqa__train_27ca312fb6ce3cb70036e317c6c758ba_2 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           A two-way urban street with buildings on both sides. My car is driving straight ahead
                        on a road where traffic keeps left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a solid yellow line and a solid yellow line next to it (double yellow
                        lines) along the left edge of the road. Photo 2 shows these two solid yellow lines
                        running parallel to the curb.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right side of my lane, only the road surface and
                        parked vehicles further ahead. Photo 2 shows no painted line to the right of my car.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [UK-HC_MARKINGS-p2-2]
                        "Double yellow lines mean no waiting at any time, unless there are signs that
                        specifically indicate seasonal restrictions."
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a curb and double
                        yellow lines, and there is no permissive rule to cross it into the pavement.
Step 6  change_right    allowed: allowed: no marking governs this action.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane in view.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park on the left due to the
                        double yellow lines.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 14755, out 743, 10.75 s

lingoqa__train_d21bf5635928983657b67b4aa8a13fac_0 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street in the UK, approaching an intersection with traffic
                        signals. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a curb with double yellow lines along the edge of the road. Photo 2
                        shows the same double yellow lines and a raised curb immediately to the left of the
                        car.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows the road widening into an intersection area with a pedestrian refuge
                        island to the right. Photo 2 shows no painted line immediately to the right, only the
                        open road leading toward the island.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [UK-HC_MARKINGS-p2-2]
                        "Double yellow lines mean no waiting at any time, unless there are signs that
                        specifically indicate seasonal restrictions."
Step 5  Rule            right_boundary: No marking governs this boundary. [null]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a raised curb and
                        double yellow lines [UK-HC_MARKINGS-p2-2].
Step 6  change_right    allowed (contested, label prohibited): allowed: no marking governs this action.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       prohibited: prohibited: the left boundary is a raised curb.
Step 6  turn_right      allowed: allowed: no marking governs this action.
Step 6  u_turn          allowed: allowed: no marking governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight or turn right as the traffic signals allow. Do
                        not stop or park along the left curb due to the double yellow lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['change_right decided
                        with nothing marked on that side', 'turn_left, turn_right, u_turn decided without an
                        arrow or prohibited-movement marking']
Tokens                  in 14755, out 750, 10.75 s

lingoqa__train_dde41275b6a47da6fe2992ae2f1b7673_1 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with traffic signals.
                        (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a red line along the edge of the road next to the curb. Photo 2 confirms
                        a solid red line next to the car, continuing further ahead.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from the area where a white van
                        is located. Photo 2 shows a series of short white dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 2 shows a white bicycle symbol painted in the lane ahead of
                        the car.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: Stopping to park, load/unload or to board and alight is prohibited on
                        red lines. [[UK-HC_MARKINGS-p2-8]]
Step 5  Rule            right_boundary: You should keep between these short, broken white lane dividers. [[UK-
                        Rule131]]
Step 5  Rule            symbol:bike: This marking indicates a cycle lane or route. [[UK-TSRGD-S11P4-item28]]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a curb and a red
                        edge line [UK-HC_MARKINGS-p2-8].
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white lane line [UK-
                        Rule131].
Step 6  go_straight     allowed (contested, correct): allowed: no marking prohibits going straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or move right if safe. Be aware of the cycle marking in your lane
                        and give way to cyclists.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:stop_line']), actions True, unsafe [], citation accepted, contradictions
                        ['rightmost lane, but a lane line on the right']
Tokens                  in 14755, out 875, 3.52 s

lingoqa__train_e0b3b51abefa2478a7a13edb958e8f33_1 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           A city street with buildings on both sides; my car is driving forward on a road with
                        parked vehicles on the right. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a grey raised curb separating the road from the sidewalk. Photo 2
                        confirms the raised curb next to my car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a line of parked vans on the right; there is no painted line between my
                        lane and the parked vehicles. Photo 2 shows the road surface next to the parked vans
                        with no painted markings.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the carriageway. [UK-TSRGD-S11P4-item11]
                        "Diagram 1012.1 (a) edge of the carriageway available for through traffic other than
                        at a road junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: No specific rule for an unpainted edge with parked vehicles, but it
                        defines the limit of the drivable lane. [null]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited: the left boundary is a raised curb.
Step 6  change_right    allowed (correct): allowed: no marking prohibits moving right, though parked vehicles
                        are present.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow governs this movement.
Step 6  turn_right      not_applicable: not_applicable: no arrow governs this movement.
Step 6  u_turn          not_applicable: not_applicable: no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the curb to the left.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 14755, out 746, 4.61 s

lingoqa__train_e12d585d1cf304230d7d39744f0797cd_0 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           A two-way urban road with parked cars on both sides; my car is in the single lane of
                        travel for its direction. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a broken white line separating my lane from a row of parked cars. Photo
                        2 shows the same broken white line next to my car, consisting of short dashes and
                        gaps.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a broken white line separating my lane from parked cars on the right.
                        Photo 2 shows the same broken white line next to my car, consisting of short dashes
                        and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: This is an edge line marking the boundary of the carriageway available
                        for through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the
                        carriageway available for through traffic other than at a road junction, an exit from
                        a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is an edge line marking the boundary of the carriageway available
                        for through traffic. [UK-TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the
                        carriageway available for through traffic other than at a road junction, an exit from
                        a private drive onto a public road, lay-by "
Step 6  change_left     allowed (contested, label prohibited): allowed: the left boundary is a broken white
                        line, which does not prohibit crossing if safe.
Step 6  change_right    allowed (correct): allowed: the right boundary is a broken white line, which does not
                        prohibit crossing if safe.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        my lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. You may move left or right if safe to do so,
                        for example to avoid parked vehicles.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 14755, out 819, 4.63 s

lingoqa__train_f2b37a8b7f23380de3834e8165fd2620_1 | lane | Test B | gemma-4-31b-it
----------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with parked cars on the left; the road continues
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a grey curb separating the road from the sidewalk and parked cars. Photo
                        2 confirms the presence of a raised grey curb immediately to the left of my car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right side of the lane, only the edge of the road
                        meeting a sidewalk/verge. Photo 2 shows no painted line next to my car on the right.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 2 shows the word 'SLOW' painted in white across the lane.
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the carriageway. [UK-TSRGD-S11P4-item11]
                        "Diagram 1012.1 (a) edge of the carriageway available for through traffic other than
                        at a road junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: The edge of the road marks the boundary of the lane. [UK-
                        TSRGD-S11P4-item11] "Diagram 1012.1 (a) edge of the carriageway available for through
                        traffic other than at a road junction, an exit from a private drive onto a public
                        road, lay-by "
Step 5  Rule            text:other: The word 'SLOW' is an advisory marking indicating the driver should reduce
                        speed. [null]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a physical curb.
Step 6  change_right    allowed: allowed: no marking prohibits leaving the lane to the right, though it is the
                        road edge.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts proceeding straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Reduce your speed as indicated by the 'SLOW'
                        marking on the road.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 14755, out 870, 4.12 s
```
