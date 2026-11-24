# Reasoning of lane run 20261117_024821_laneC_UK

```text
lingoqa__train_27ca312fb6ce3cb70036e317c6c758ba_2 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is an urban street with shops on the left and parked vehicles on the right. The
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A double yellow solid line is painted along the left edge of the road next to the
                        curb.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line is visible on the right, but there are parked vehicles along the edge
                        of the roadway.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries, as both
                        sides are edge lines. | roles: The yellow double solid line on the left is a typical
                        edge line for parking restrictions in this region. | markings: There are no markings
                        in the lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule from the provided list governs a boundary with no
                        paint and no curb.
Step 6  change_left     prohibited (contested, correct): The left boundary is a double solid yellow line, and
                        [IN-6(6)] prohibits driving on or over a double solid line.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action.
Step 6  go_straight     allowed (contested, label not_determined): No marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a double solid line, and [IN-8(3)(a)(iv)] prohibits
                        U-turns across a double solid line.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines on the
                        left.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 5796, out 648, 37.46 s

lingoqa__train_d21bf5635928983657b67b4aa8a13fac_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on an urban road approaching an intersection with buildings on both sides.
                        (lanes 1, mine 1, full)
Step 2  Left            A double yellow solid line is painted along the left edge of the road next to the
                        curb.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line is visible on the right side of the lane, only the asphalt surface.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and the
                        absence of a right lane line. | roles: The yellow double solid line on the left fits
                        the role of an edge line (parking restriction). | markings: There are no markings in
                        the lane to contradict. | unseen: No attributes were reported without being seen. |
                        result: consistent
Step 5  Rule            left_boundary: Parking is prohibited where there is a continuous yellow line on the
                        kerb side. [[IN-22.(2)(j)]]
Step 5  Rule            right_boundary: No specific rule governs this boundary as no marking is present.
Step 6  change_left     prohibited (contested, correct): The left boundary is a double solid yellow line, and
                        [IN-6(6)] prohibits driving over a double solid line.
Step 6  change_right    allowed (contested, label prohibited): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking restricts carrying on straight along the
                        lane.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          prohibited: The left boundary is a double solid line, and [IN-8(3)(a)(iv)] prohibits
                        U-turns across a double solid line.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the double yellow lines on the
                        left.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation unlisted, contradictions ['change_right decided
                        with nothing marked on that side', 'u_turn decided without an arrow or prohibited-
                        movement marking']
Tokens                  in 5796, out 628, 31.5 s

lingoqa__train_dde41275b6a47da6fe2992ae2f1b7673_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a multi-lane urban road approaching a traffic signal intersection.
                        (lanes 2, mine 1, full)
Step 2  Left            A red solid line is painted along the left edge of the roadway next to a curb.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A white dashed line separates my lane from the lane to the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the lane.; line:stop_line
                        (full): A white solid line is painted across the lane before the pedestrian crossing.;
                        line:crosswalk (full): A white zebra-striped pedestrian crossing is painted across the
                        lane.
Step 4  Cross-check     position: The lane count of 2 and ego_lane_index 1 agree with the left edge_line and
                        right lane_line. | roles: The red solid edge line and white dashed lane line fit their
                        roles. | markings: The bicycle symbol and stop line are consistent with an urban road
                        lane. | unseen: No attributes were reported without being seen. | result: consistent
Step 5  Rule            left_boundary: The driver shall not drive on or over a single solid longitudinal line.
                        [[IN-6(6)]]
Step 5  Rule            right_boundary: The driver may change lanes after giving a proper signal. [[IN-6(1)]]
Step 5  Rule            symbol:bike: This is an informative marking indicating a cycle lane or shared space;
                        it does not prohibit motor vehicles unless specified by other signs.
Step 5  Rule            line:stop_line: The driver shall stop before the stop line when facing a red light.
                        [[IN-12(1)(a)]]
Step 5  Rule            line:crosswalk: The driver shall give way to pedestrians at the crossing.
                        [[IN-8(2)(e)]]
Step 6  change_left     prohibited (contested, correct): Prohibited by the solid red edge line [IN-6(6)].
Step 6  change_right    allowed (WRONG, label not_determined): Allowed by the dashed white lane line
                        [IN-6(1)].
Step 6  go_straight     allowed (contested, correct): Allowed as no marking prohibits it and it is the default
                        movement.
Step 6  turn_left       not_applicable: Not applicable as there is no left-turn arrow or waiting area.
Step 6  turn_right      not_applicable: Not applicable as there is no right-turn arrow or waiting area.
Step 6  u_turn          not_applicable: Not applicable as there is no U-turn arrow and it would require
                        crossing a solid line [IN-8(3)(a)(iv)].
Step 6  enter_waiting_areanot_applicable: Not applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane or change to the right. Stop at the stop line if the signal is red
                        and yield to pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 5796, out 857, 38.45 s

lingoqa__train_e12d585d1cf304230d7d39744f0797cd_0 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a two-way urban road with parked vehicles on both sides; the road
                        continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A grey curb with a small concrete gutter separates the road from a sidewalk and parked
                        cars.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A grey curb with a small concrete gutter separates the road from parked cars and a
                        sidewalk.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the presence of curbs on both
                        sides, indicating my lane is the only lane of my direction. | roles: The curbs
                        correctly serve as edge boundaries for the roadway. | markings: There are no markings
                        in the lane to contradict the boundaries. | unseen: No attributes were reported that
                        were not visible. | result: consistent
Step 5  Rule            left_boundary: The curb defines the edge of the roadway; crossing it is prohibited as
                        it leads to a sidewalk.
Step 5  Rule            right_boundary: The curb defines the edge of the roadway; crossing it is prohibited as
                        it leads to parked cars and a sidewalk.
Step 6  change_left     prohibited (contested, label not_determined): The left boundary is a curb, which
                        prohibits leaving the roadway.
Step 6  change_right    prohibited (WRONG, label allowed): The right boundary is a curb, which prohibits
                        leaving the roadway.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and there is no
                        restriction to continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and proceed straight. Do not cross the curbs on either side.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation none, contradictions []
Tokens                  in 5796, out 596, 27.14 s

lingoqa__train_f2b37a8b7f23380de3834e8165fd2620_1 | lane | Test C | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a residential urban road with houses on the left and greenery on the right.
                        The road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A grey concrete curb separates the road from the sidewalk and parked cars.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane before it merges into
                        the greenery/sidewalk area.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): The word SLOW is painted in white across the lane.
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the boundaries being
                        edge lines on both sides. | roles: The absence of paint and presence of a curb on the
                        left and a soft edge on the right fit the role of edge lines. | markings: The 'SLOW'
                        marking is a warning and does not contradict the boundaries. | unseen: No attributes
                        were reported that were not visible. | result: consistent
Step 5  Rule            left_boundary: The curb marks the edge of the roadway; crossing it is prohibited as it
                        leads to the sidewalk.
Step 5  Rule            right_boundary: The right edge of the road is the boundary of the carriageway.
Step 5  Rule            text:other: The 'SLOW' marking is informative and advises the driver to reduce speed.
Step 6  change_left     prohibited (contested, correct): prohibited by the left_boundary (curb) which
                        separates the road from the sidewalk.
Step 6  change_right    allowed: allowed as there is no marking or curb prohibiting movement to the right,
                        though it is the edge of the road.
Step 6  go_straight     allowed (contested, correct): allowed as no marking restricts carrying on straight
                        along the lane.
Step 6  turn_left       not_applicable: not_applicable as there is no arrow or intersection marking governing
                        this.
Step 6  turn_right      not_applicable: not_applicable as there is no arrow or intersection marking governing
                        this.
Step 6  u_turn          allowed: allowed as there are no solid lines prohibiting it.
Step 6  enter_waiting_areanot_applicable: not_applicable as no waiting area is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane and drive straight. Be mindful of the 'SLOW' marking and reduce your
                        speed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation none_needed, contradictions ['change_right
                        decided with nothing marked on that side', 'u_turn decided without an arrow or
                        prohibited-movement marking']
Tokens                  in 5796, out 705, 35.53 s
```
