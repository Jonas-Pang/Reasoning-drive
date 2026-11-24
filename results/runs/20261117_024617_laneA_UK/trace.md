# Reasoning of lane run 20261117_024617_laneA_UK

```text
lingoqa__train_27ca312fb6ce3cb70036e317c6c758ba_2 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A city street in the UK with shops on the left and parked vehicles on the right; the
                        road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A double solid yellow line is painted along the left edge of the road next to the
                        sidewalk.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           No painted line is visible on the right, but vehicles are parked along the side of the
                        road.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and the right
                        edge of the roadway. | roles: The double yellow line on the left is a standard UK edge
                        marking for parking restrictions. | markings: There are no markings in the lane to
                        contradict the boundaries. | unseen: No attributes were reported without visual
                        evidence. | result: consistent
Step 5  Rule            left_boundary: Double yellow lines indicate no parking and prohibit crossing the
                        boundary to leave the roadway.
Step 5  Rule            right_boundary: The right edge of the roadway is the limit of the drivable lane.
Step 6  change_left     prohibited (contested, correct): The left boundary is a double solid yellow edge line
                        with a curb, which prohibits leaving the roadway.
Step 6  change_right    allowed (WRONG, label not_determined): No marking governs this action, but the
                        presence of parked cars and the road edge limits movement.
Step 6  go_straight     allowed (contested, label not_determined): No marking governs this action; carrying on
                        straight is allowed.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the scene.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight. Do not cross the double yellow lines on
                        the left.
Score                   lane True, boundaries {'left': True, 'right': None}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 2949, out 603, 12.68 s

lingoqa__train_d21bf5635928983657b67b4aa8a13fac_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with traffic signals.
                        (lanes 1, mine 1, full)
Step 2  Left            A double yellow line is painted on the edge of the road next to the curb on the left.
                        yellow double_solid, curb yes, edge_line, evidence full
Step 2  Right           There is no painted line or curb on the right side of the lane, only the road surface
                        continuing towards the junction.
                        none none, curb no, unknown, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the left edge line and the
                        absence of a right lane line. | roles: The double yellow edge line on the left is
                        consistent with a road edge in the UK. | markings: There are no markings in the lane
                        to contradict. | unseen: No attributes were reported without being seen. | result:
                        consistent
Step 5  Rule            left_boundary: The double yellow line and curb prohibit leaving the roadway to the
                        left.
Step 5  Rule            right_boundary: The absence of a marking on the right does not prohibit movement, but
                        there is no designated lane boundary.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb with double yellow lines,
                        which prohibits leaving the road.
Step 6  change_right    allowed (contested, label prohibited): No marking governs this action.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, and the lane does not
                        end in a merge.
Step 6  turn_left       not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  You can proceed straight or move to the right. Follow the traffic signals at the
                        junction.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 2949, out 610, 19.97 s

lingoqa__train_dde41275b6a47da6fe2992ae2f1b7673_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           The car is on a city road in the UK, approaching a junction with traffic signals.
                        (lanes 1, mine 1, full)
Step 2  Left            A solid red line marks the left edge of the roadway next to a sidewalk.
                        other solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from a traffic island and a white van.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:bike (full): A white bicycle symbol is painted in the lane.; line:stop_line
                        (full): A white stop line is painted across the lane before the junction.
Step 4  Cross-check     position: The lane count of 1 and index 1 agree with the edge lines on both sides. |
                        roles: The red line on the left and white line on the right both act as roadway
                        boundaries. | markings: The bike symbol indicates a cycle lane, and the stop line
                        marks the end of the lane at the junction. | unseen: No attributes were reported
                        without being seen. | result: consistent
Step 5  Rule            left_boundary: Crossing a solid red edge line into the sidewalk is prohibited.
Step 5  Rule            right_boundary: Crossing a solid white edge line into the traffic island or opposite
                        lane is prohibited.
Step 5  Rule            symbol:bike: The lane is designated for bicycles, but motorized vehicles may use it
                        unless signs prohibit it.
Step 5  Rule            line:stop_line: The vehicle must stop at this line when the signal is red.
Step 6  change_left     prohibited (contested, correct): The left boundary is a solid red edge line, which
                        prohibits leaving the roadway.
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary is a solid white edge
                        line, which prohibits crossing into the island/opposite lane.
Step 6  go_straight     allowed (contested, correct): No arrow prohibits going straight, and the stop line
                        only governs when to stop, not the direction.
Step 6  turn_left       not_applicable: No arrow governs this action.
Step 6  turn_right      not_applicable: No arrow governs this action.
Step 6  u_turn          not_applicable: No arrow governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area is present in the scene.
Step 7  Reflect         consistent
Advice                  Stay in the lane and proceed straight, stopping at the stop line if the traffic signal
                        is red. Note that this is a designated cycle lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 738, 18.9 s

lingoqa__train_e12d585d1cf304230d7d39744f0797cd_0 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           This is a two-way urban road in the UK with traffic keeping to the left; the road
                        ahead appears clear with parked vehicles on both sides. (lanes 1, mine 1, full)
Step 2  Left            A grey curb and a metal fence separate the road from the sidewalk on the left.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A dashed white line separates my lane from the opposite direction of traffic.
                        white dashed, curb no, center_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the left edge curb and
                        the right center line. | roles: The white dashed line on the right is consistent with
                        a center line in the UK. | markings: There are no markings in the lane to contradict
                        the boundaries. | unseen: No attributes were reported without being visible. | result:
                        consistent
Step 5  Rule            left_boundary: The curb prohibits leaving the roadway to the left.
Step 5  Rule            right_boundary: The dashed center line allows crossing into the opposite lane for
                        overtaking when safe.
Step 6  change_left     prohibited (contested, label not_determined): The left boundary is a curb, which
                        prohibits leaving the road.
Step 6  change_right    allowed (correct): The right boundary is a dashed center line, which allows crossing
                        into the opposite lane.
Step 6  go_straight     allowed (contested, correct): No marking governs this action, so it is allowed by
                        default.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in your lane to go straight. You may cross the center line to overtake if the
                        road ahead is clear and it is safe to do so.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 2949, out 602, 14.91 s

lingoqa__train_f2b37a8b7f23380de3834e8165fd2620_1 | lane | Test A | gemma4:31b
------------------------------------------------------------------------------
Step 1  Scene           A residential urban road in the UK with houses on the left and greenery on the right;
                        the road continues straight ahead. (lanes 1, mine 1, full)
Step 2  Left            A grey concrete curb separates the roadway from the sidewalk and parked cars.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           No painted line or curb is visible on the right side of the lane before it merges into
                        the greenery/sidewalk area.
                        none none, curb no, edge_line, evidence full
Step 3  Markings        text:other (full): The word SLOW is painted in white across the lane.
Step 4  Cross-check     position: The lane count of 1 and ego_lane_index 1 agree with the presence of edge
                        boundaries on both sides. | roles: The curb on the left and the lack of markings on
                        the right are consistent with a single-lane residential road. | markings: The SLOW
                        marking is a warning and does not contradict the boundaries. | unseen: No attributes
                        were reported without visual evidence. | result: consistent
Step 5  Rule            left_boundary: Crossing the curb to the left is prohibited.
Step 5  Rule            right_boundary: Leaving the roadway to the right is prohibited.
Step 5  Rule            text:other: The SLOW marking advises the driver to reduce speed but does not prohibit
                        any specific movement.
Step 6  change_left     prohibited (contested, correct): The left boundary is a curb, which prohibits leaving
                        the lane to the left.
Step 6  change_right    prohibited: The right boundary is the edge of the roadway, which prohibits leaving the
                        lane to the right.
Step 6  go_straight     allowed (contested, correct): No marking prohibits going straight, and the lane does
                        not end.
Step 6  turn_left       not_applicable: No arrow or waiting area governs this action.
Step 6  turn_right      not_applicable: No arrow or waiting area governs this action.
Step 6  u_turn          not_applicable: No arrow governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or two-way left-turn lane is present.
Step 7  Reflect         consistent
Advice                  Stay in the current lane and proceed straight, reducing speed as indicated by the SLOW
                        marking.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['change_right decided
                        with nothing marked on that side']
Tokens                  in 2949, out 672, 17.89 s
```
