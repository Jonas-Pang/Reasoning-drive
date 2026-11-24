# Reasoning of lane run 20261117_024654_laneB_UK

```text
lingoqa__train_27ca312fb6ce3cb70036e317c6c758ba_2 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street with shops on the left and buildings on the right. The road
                        ahead is a straight stretch of a single carriageway. (lanes 1, mine 1, full)
Step 2  Left            I see double yellow lines along the left edge of the road next to the pavement.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line or curb on the right side of my lane; it is bordered by
                        parked vehicles.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and my position as index 1 are consistent with the left
                        boundary being an edge line and the right boundary being undefined/parked cars. |
                        roles: The double yellow lines on the left correctly identify the edge of the
                        carriageway/pavement. | markings: There are no markings in my lane to contradict. |
                        unseen: No attributes were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [[UK-
                        HC_MARKINGS-p2-2]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the curb and the double yellow lines
                        which mark the edge of the carriageway.
Step 6  change_right    allowed (WRONG, label not_determined): Allowed as there is no marking or physical
                        barrier prohibiting it, though parked cars are present.
Step 6  go_straight     allowed (contested, label not_determined): Allowed as there are no markings in my lane
                        restricting forward movement.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or intersection marking governing
                        this movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or intersection marking governing
                        this movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow or intersection marking governing
                        this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as there is no waiting area present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park on the left side of the
                        road due to the double yellow lines.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 13644, out 751, 39.41 s

lingoqa__train_d21bf5635928983657b67b4aa8a13fac_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. The car is approaching a junction with traffic
                        signals; the road ahead appears to continue straight. (lanes 1, mine 1, full)
Step 2  Left            I see a curb and double yellow lines on the left edge of the road.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right, but a concrete pedestrian island/curb starts
                        further ahead.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 are consistent with the left edge line and
                        the absence of a lane line on the right. | roles: The double yellow lines on the left
                        are consistent with an edge line indicating waiting restrictions. | markings: There
                        are no markings in the lane to contradict the boundaries. | unseen: No attributes were
                        reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: Double yellow lines mean no waiting at any time. [UK-HC_MARKINGS-p2-2]
                        "Double yellow lines mean no waiting at any time, unless there are signs that
                        specifically indicate seasonal restrictions."
Step 6  change_left     prohibited (contested, correct): Prohibited by the curb and the double yellow lines
                        which mark the edge of the carriageway.
Step 6  change_right    allowed (contested, label prohibited): Allowed as there is no painted line or curb
                        immediately governing this action in the visible stretch.
Step 6  go_straight     allowed (contested, correct): Allowed as there are no arrows or markings prohibiting
                        it.
Step 6  turn_left       not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  turn_right      not_applicable: Not applicable as there is no arrow or waiting area governing this
                        movement.
Step 6  u_turn          not_applicable: Not applicable as there is no arrow governing this movement.
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not stop or park on the left due to the
                        double yellow lines.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 13644, out 728, 46.13 s

lingoqa__train_dde41275b6a47da6fe2992ae2f1b7673_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road in the UK. Ahead is a junction with traffic signals and a
                        pedestrian crossing. My car is in the leftmost lane of its direction. (lanes 2, mine
                        1, full)
Step 2  Left            A solid red line is painted on the edge of the road, next to a curb.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line divides my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the lane.; line:stop_line
                        (full): A white transverse line is painted across the lane before the junction.
Step 4  Cross-check     position: The lane count of 2 and my position as index 1 agree with the left edge line
                        and right lane line. | roles: The red edge line and white dashed lane line fit their
                        respective roles. | markings: The bike symbol indicates a cycle lane, and the stop
                        line is consistent with the upcoming junction. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: The red line indicates that stopping to park, load/unload or to board
                        and alight is prohibited. [[UK-HC_MARKINGS-p2-8]]
Step 5  Rule            right_boundary: I should keep between the broken white lane dividers. [[UK-Rule131]]
Step 5  Rule            symbol:bike: I should not drive in a cycle lane marked by a broken white line unless
                        it is unavoidable. [[UK-Rule140-2]]
Step 5  Rule            line:stop_line: This is a stop line at signals. [[UK-HC_MARKINGS-p1]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the red edge line and curb [UK-
                        HC_MARKINGS-p2-8].
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the broken white lane line [UK-
                        Rule131].
Step 6  go_straight     allowed (contested, correct): Allowed as no arrow restricts it, but I am in a cycle
                        lane [UK-Rule140-2].
Step 6  turn_left       not_applicable: Not applicable as no arrow governs this movement.
Step 6  turn_right      not_applicable: Not applicable as no arrow governs this movement.
Step 6  u_turn          not_applicable: Not applicable as no arrow governs this movement.
Step 6  enter_waiting_areanot_applicable: No marking governs this action.
Step 7  Reflect         consistent
Advice                  You are currently in a cycle lane; avoid driving in it unless unavoidable. Do not stop
                        on the red line. Follow the traffic signals at the stop line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 13644, out 990, 44.9 s

lingoqa__train_e12d585d1cf304230d7d39744f0797cd_0 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban road with buildings and parked vehicles on both sides. The road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            I see a grey raised curb and a sidewalk beyond it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           I see a dashed white line separating my lane from a parking area where vehicles are
                        stopped.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and position 1 agree with the boundaries: a curb on the
                        left and an edge line on the right. | roles: The dashed white line on the right fits
                        the role of an edge line separating the through lane from a parking/lay-by area. |
                        markings: There are no markings in the lane to contradict. | unseen: No attributes
                        were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway and prohibits leaving the road.
                        [null]
Step 5  Rule            right_boundary: This line divides the main carriageway from a lay-by or parking area.
                        [[UK-TSRGD-S11P4-item10]]
Step 6  change_left     prohibited (contested, label not_determined): prohibited by the curb (left_boundary).
Step 6  change_right    allowed (correct): allowed by the dashed white line (right_boundary) as it is not a
                        solid line prohibiting crossing.
Step 6  go_straight     allowed (contested, correct): allowed as no marking governs this action and it is the
                        natural path of the lane.
Step 6  turn_left       not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: not_applicable as no arrow or waiting area governs this action.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane to proceed straight. You may move to the right to enter the parking
                        area if safe to do so.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 13644, out 782, 34.74 s

lingoqa__train_f2b37a8b7f23380de3834e8165fd2620_1 | lane | Test B | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road with houses on the left and greenery on the right.
                        The road continues straight ahead with no immediate intersection or ramp. (lanes 1,
                        mine 1, full)
Step 2  Left            There is no painted line on the left, but a raised curb separates the road from the
                        sidewalk.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line on the right, and the road edge meets a grassy verge and
                        foliage.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): The word SLOW is painted in white across the lane.
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries being
                        edge lines on both sides. | roles: The absence of paint and presence of a curb/verge
                        fit the role of edge lines. | markings: The SLOW marking is a common warning and does
                        not contradict the boundaries. | unseen: No attributes were reported without being
                        seen. | result: consistent
Step 5  Rule            left_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            right_boundary: This is the edge of the carriageway. [UK-TSRGD-S11P4-item11] "Diagram
                        1012.1 (a) edge of the carriageway available for through traffic other than at a road
                        junction, an exit from a private drive onto a public road, lay-by "
Step 5  Rule            text:other: The SLOW marking warns that vehicular traffic should proceed with caution
                        because of potential danger ahead. [UK-TSRGD-S11P4-item15] "Diagram 1024 Vehicular
                        traffic should proceed with caution because of potential danger ahead"
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a raised curb.
Step 6  change_right    allowed: allowed: no marking governs this action, and there is no physical barrier.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight along
                        the lane.
Step 6  turn_left       not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  turn_right      not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  u_turn          not_applicable: not_applicable: no arrow or prohibited-movement marking in my lane.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area or two-way left-turn lane is
                          present.
Step 7  Reflect         consistent
Advice                  Proceed straight with caution as indicated by the SLOW marking. Do not attempt to move
                        left as there is a curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions
                        ['change_right decided with nothing marked on that side']
Tokens                  in 13644, out 909, 42.46 s
```
