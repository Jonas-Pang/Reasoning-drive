# Reasoning of lane run 20261117_122406_laneC_UK

```text
lingoqa__train_27ca312fb6ce3cb70036e317c6c758ba_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city street with shops on the left and parked vehicles on the right.
                        The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a yellow solid line along the left edge of the road. Photo 2 shows two
                        yellow solid lines side by side next to the curb.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right, only parked vehicles. Photo 2 shows no
                        painted line on the right.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: Photo 2 reveals the left boundary is a double yellow line, whereas Photo 1
                        looked like a single line; Photo 2 decides. | position: The lane count of 1 and
                        position 1 agree with the left and right boundaries being edge lines. | roles: The
                        yellow double solid line on the left is a typical edge line for parking restrictions
                        in the UK. | markings: No markings are present in the lane. | unseen: No | result:
                        consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule from the provided list governs a boundary with no
                        paint and no curb.
Step 6  change_left     prohibited (contested, correct): The left boundary is a double solid line, and
                        [IN-6(6)] prohibits driving over it.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action.
Step 6  go_straight     allowed (contested, label not_determined): No marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a double solid line, and [IN-8(3)(a)(iv)] prohibits
                        U-turns across it.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines on the
                        left.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 6489, out 680, 61.5 s

lingoqa__train_d21bf5635928983657b67b4aa8a13fac_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching an intersection with traffic signals.
                        The road ahead is a single-lane stretch leading into the junction. (lanes 1, mine 1,
                        full)
Step 2  Left            Photo 1 shows a grey curb with double yellow lines painted along the edge of the road.
                        Photo 2 confirms the presence of the raised grey curb and the double yellow lines
                        immediately next to the car.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows the road widening into an intersection area with a pedestrian crossing
                        island to the right. Photo 2 shows no painted line or curb immediately to the right of
                        the car's current position, only the asphalt of the road surface.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: consistent | roles: consistent |
                        markings: consistent | unseen: no | result: consistent
Step 5  Rule            left_boundary: A vehicle shall not be parked where there is a continuous yellow line
                        installed or painted on the carriageway on the kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs this boundary as there is no paint or curb.
Step 6  change_left     prohibited (contested, correct): prohibited by the raised curb and solid yellow lines
                        [IN-6(6)]
Step 6  change_right    allowed (contested, label prohibited): allowed as there are no markings or curbs
                        restricting movement to the right
Step 6  go_straight     allowed (contested, correct): allowed as no markings restrict continuing straight
Step 6  turn_left       not_applicable: not_applicable as no arrow governs this movement
Step 6  turn_right      not_applicable: not_applicable as no arrow governs this movement
Step 6  u_turn          not_applicable: not_applicable as no arrow governs this movement
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight through the intersection. Do not cross
                        the left boundary due to the curb and yellow lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side']
Tokens                  in 6489, out 789, 64.57 s

lingoqa__train_dde41275b6a47da6fe2992ae2f1b7673_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road in the UK, approaching an intersection with a
                        traffic signal and a pedestrian crossing. (lanes 2, mine 1, full)
Step 2  Left            Photo 1 shows a red solid line along the edge of the road next to a curb. Photo 2
                        confirms a red solid line and a raised curb immediately to the left of the car.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows a white broken line separating my lane from the lane to the right. Photo
                        2 shows a white broken line with long dashes and gaps next to the car.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): Photo 1 and Photo 2 show a white bicycle symbol painted in the
                        lane.; line:stop_line (full): Photo 1 and Photo 2 show a white solid line across the
                        lane, which is a stop line preceding a pedestrian crossing.; line:crosswalk (full):
                        Photo 1 and Photo 2 show a white zebra-style pedestrian crossing immediately after the
                        stop line.
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and ego_lane_index agree
                        with the left edge_line and right lane_line | roles: the red solid edge line and white
                        dashed lane line fit their roles | markings: the bicycle symbol and stop line are
                        consistent with an urban road approaching a crossing | unseen: no | result: consistent
Step 5  Rule            left_boundary: The red solid line and curb mark the edge of the roadway; crossing it
                        is prohibited as it leads off the road. [null]
Step 5  Rule            right_boundary: The white broken line allows lane changes after giving a proper
                        signal. [[IN-6(1)]]
Step 5  Rule            symbol:bike: The bicycle symbol indicates the lane is shared with or used by cyclists;
                        it does not prohibit motor vehicles from using the lane. [null]
Step 5  Rule            line:stop_line: The driver must stop before the stop line if the traffic signal is
                        red. [[IN-12(1)(a)]]
Step 5  Rule            line:crosswalk: The driver must give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): prohibited by the curb and red edge line
Step 6  change_right    allowed (WRONG, label not_determined): allowed by the white broken lane line [IN-6(1)]
Step 6  go_straight     allowed (contested, correct): allowed as no marking prohibits it, though subject to
                        the stop line and signal
Step 6  turn_left       not_applicable: not_applicable as there is no left-turn arrow and the boundary is a
                        curb
Step 6  turn_right      not_applicable: not_applicable as there is no right-turn arrow
Step 6  u_turn          not_applicable: not_applicable as there is no U-turn arrow and it would cross a
                        pedestrian crossing
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right if needed. Stop at the stop line for the red
                        light and yield to pedestrians at the crossing.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 6489, out 938, 16.18 s

lingoqa__train_e12d585d1cf304230d7d39744f0797cd_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with parked vehicles on both sides, proceeding
                        straight ahead. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a white dashed line separating the driving lane from a line of parked
                        cars. Photo 2 confirms a white dashed line next to the car with several short dashes
                        and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 2  Right           Photo 1 shows a white dashed line separating the driving lane from parked cars on the
                        right. Photo 2 shows a white dashed line next to the car with short dashes and gaps.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     close_up: the same in both photos | position: the lane count and position agree with
                        the boundaries; the car is in a single lane bounded by edge lines on both sides. |
                        roles: the white dashed lines fit the role of edge lines separating the travel lane
                        from parking/shoulder areas. | markings: no markings present in the lane. | unseen: no
                        | result: consistent
Step 5  Rule            left_boundary: A white dashed edge line allows crossing to access the shoulder or
                        parking area. [null]
Step 5  Rule            right_boundary: A white dashed edge line allows crossing to access the shoulder or
                        parking area. [null]
Step 6  change_left     allowed (contested, label not_determined): allowed by the white dashed edge line
                        (left_boundary).
Step 6  change_right    allowed (correct): allowed by the white dashed edge line (right_boundary).
Step 6  go_straight     allowed (contested, correct): allowed as there are no markings restricting forward
                        movement.
Step 6  turn_left       not_applicable: not_applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  turn_right      not_applicable: not_applicable as there are no turn arrows or intersection markings in
                        the lane.
Step 6  u_turn          allowed: allowed as there are no solid lines prohibiting it.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  You are in a single travel lane. You may proceed straight or move left or right across
                        the dashed lines to park or maneuver, provided it is safe to do so.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions ['u_turn decided
                        without an arrow or prohibited-movement marking']
Tokens                  in 6489, out 804, 64.56 s

lingoqa__train_f2b37a8b7f23380de3834e8165fd2620_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a residential urban road in the UK, driving forward on a straight
                        stretch with parked cars on the left. (lanes 1, mine 1, full)
Step 2  Left            Photo 1 shows a grey curb separating the road from the sidewalk and parked cars. Photo
                        2 confirms the presence of a raised grey curb immediately to the left of the car.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           Photo 1 shows no painted line on the right side of the lane, only the asphalt surface
                        extending towards the right edge of the road. Photo 2 also shows no paint or curb
                        immediately to the right of the car.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): Photo 1 and Photo 2 show the word 'SLOW' painted in white across
                        the lane.
Step 4  Cross-check     close_up: the same in both photos | position: The lane count of 1 and position 1 agree
                        with the boundaries, as both sides are edge boundaries (curb on left, road edge on
                        right). | roles: The roles fit; a curb on the left and no line on the right for a
                        single-lane residential road is consistent. | markings: The 'SLOW' marking is a
                        warning and does not contradict the boundaries. | unseen: no | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; crossing it is prohibited as it
                        leads to the sidewalk. [null]
Step 5  Rule            right_boundary: No painted line exists, but the driver should remain within the
                        roadway. [null]
Step 5  Rule            text:other: The 'SLOW' marking is informative, advising the driver to reduce speed.
                        [null]
Step 6  change_left     prohibited (contested, correct): prohibited: the left boundary is a raised curb.
Step 6  change_right    allowed: allowed: no marking governs this action.
Step 6  go_straight     allowed (contested, correct): allowed: no marking restricts carrying on straight.
Step 6  turn_left       not_applicable: not_applicable: no arrow or intersection governs this action here.
Step 6  turn_right      not_applicable: not_applicable: no arrow or intersection governs this action here.
Step 6  u_turn          allowed: allowed: no marking prohibits a U-turn in this stretch.
Step 6  enter_waiting_areanot_applicable: not_applicable: no waiting area is present.
Step 7  Reflect         consistent
Advice                  Drive straight and reduce speed as indicated by the 'SLOW' marking. Do not drive onto
                        the left curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['change_right decided
                        with nothing marked on that side', 'u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 6489, out 917, 17.44 s
```
