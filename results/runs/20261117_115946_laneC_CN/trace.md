# Reasoning of lane run 20261117_115946_laneC_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a guardrail on the left and a barrier separating it from
                        another road or area on the right, heading straight ahead with no intersection visible
                        (lanes 3, mine 2, full)
Step 2  Left            a white solid line on the left side of my lane, with a guardrail beyond it
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a white solid line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not change lanes to the left across the solid white line
                        [[US-3B.06-01]]
Step 5  Rule            right_boundary: my car may not change lanes to the right across the solid white line
                        [[US-3B.06-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by left boundary, [US-3B.06-01]
Step 6  change_right    prohibited (correct): prohibited by right boundary, [US-3B.06-01]
Step 6  go_straight     allowed (contested, correct): not prohibited
Step 6  turn_left       not_applicable: not determined
Step 6  turn_right      not_applicable: not determined
Step 6  u_turn          not_applicable: not determined
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  stay in your lane, changing lanes is not allowed
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 587, 14.53 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a guardrail on the right, possibly merging with another road
                        or continuing straight ahead (lanes 3, mine 2, full)
Step 2  Left            a white dashed line on the left side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           a guardrail on the right side of my lane, with a solid white line marking the edge of
                        the roadway
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car is allowed to change lanes across this boundary with care
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car must not cross this boundary [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): left_ boundary [US-3B.06-05-06] allows it
Step 6  change_right    prohibited (correct): right boundary [US-3B.09-01-02] prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  you can change lanes to the left or continue straight ahead; changing lanes to the
                        right is prohibited
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 593, 13.34 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a guardrail on the right and a median with green posts on
                        the left, leading to a bridge or overpass with green directional signs (lanes 3, mine
                        2, full)
Step 2  Left            a green post and a guardrail on the median, with a broken white line on the road
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           a guardrail with a solid yellow line on the road
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line marking, but may cross a
                        broken white lane line marking with care [[US-3B.06-01]]
Step 5  Rule            right_boundary: my car must not drive left of the right edge line [[US-3B.09-01-02]]
Step 6  change_left     allowed (correct): left_ boundary is a broken white line [US-3B.06-05-06], so it is
                        allowed
Step 6  change_right    prohibited (WRONG, label not_determined): right boundary is a solid yellow line
                        [US-3B.09-01-02], so it is prohibited
Step 6  go_straight     allowed (contested, correct): no marking governs this action, so it is allowed
Step 6  turn_left       not_determined: no marking governs this action, so it is not determined
Step 6  turn_right      not_determined: no marking governs this action, so it is not determined
Step 6  u_turn          not_determined: no marking governs this action, so it is not determined
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane is visible, so it is not
                          applicable
Step 7  Reflect         consistent
Advice                  keep in your lane, do not change right; you may go straight or change left with care
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 660, 28.99 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with a barrier on one side, likely an urban highway or expressway
                        (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right side of my lane, with a barrier beyond it
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line to the left
                        [[US-3B.06-01]]
Step 5  Rule            right_boundary: my car may not cross a solid yellow edge line to the right
                        [[US-3B.09-01-02]]
Step 6  change_left     prohibited (contested, correct): left_boundary solid white line [US-3B.06-01]
                        prohibits it
Step 6  change_right    prohibited (contested, correct): right_boundary solid yellow line [US-3B.09-01-02]
                        prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action, it is allowed
Step 6  turn_left       not_determined: no arrow or prohibited- movement marking in my lane, not determined
Step 6  turn_right      not_determined: no arrow or prohibited- movement marking in my lane, not determined
Step 6  u_turn          not_determined: no arrow or prohibited- movement marking in my lane, not determined
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane next to my lane, not
                          applicable
Step 7  Reflect         consistent
Advice                  follow the lane markings and traffic rules, and be cautious when approaching
                        intersections or merging with other lanes
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 636, 16.23 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with a concrete barrier on the right, possibly an urban highway or
                        expressway (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right side of my lane, with a concrete barrier beyond it
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): two white characters in my lane, ahead of the vehicle
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on the left
                        [[US-3B.06-01]]
Step 5  Rule            right_boundary: my car may not cross a solid yellow edge line on the right
                        [[US-3B.09-01-02]]
Step 5  Rule            text:other: no rule found
Step 6  change_left     prohibited (contested, label allowed): left boundary prohibits it
Step 6  change_right    prohibited (contested, label allowed): right boundary prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_determined: no arrow or prohibited marking in my lane
Step 6  turn_right      not_determined: no arrow or prohibited marking in my lane
Step 6  u_turn          not_determined: no arrow or prohibited marking in my lane
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  follow the lane markings and do not change lanes
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:other'], missed ['text:bus']), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 643, 28.74 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test C | llama4:scout
----------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with a tunnel ahead, in a city (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane, a curb beyond it
                        white solid, curb yes, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: This solid white lane line marking discourages crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: This solid white lane line marking discourages crossing.
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): left_ boundary [US-3B.06-05-06] prohibits
Step 6  change_right    prohibited (correct): right boundary [US-3B.06-05-06] prohibits
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_determined: no arrow in my lane
Step 6  turn_right      not_determined: no arrow in my lane
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  Drive straight in your lane. Lane changes are not needed and are prohibited by solid
                        lines.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 572, 14.02 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test C | llama4:scout
----------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with trees and buildings on both sides (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane and a yellow curb beyond it
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on its left to change
                        lanes unless the rule for a special lane prohibits or restricts it more
                        [[US-3B.06-01]]
Step 5  Rule            right_boundary: my car may not cross a solid white edge line on its right to change
                        lanes [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): left_ boundary [US-3B.06-01] solid white line prohibits it
Step 6  change_right    prohibited (correct): right boundary [US-3B.09-01-02] solid white line prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane ahead of or to the left of
                          my lane
Step 7  Reflect         consistent
Advice                  keep in my lane and go straight ahead; do not change lanes
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 612, 13.58 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test C | llama4:scout
----------------------------------------------------------------------------------------------------
Step 1  Scene           This is a straight road with multiple lanes for traffic traveling in the same
                        direction. There are no intersections, ramps, or lane endings ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            A solid white line on the left side of my lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A broken white line on the right side of my lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane count and my lane position agree with the boundary roles. | roles:
                        The color and pattern of each boundary fit the role. | markings: No markings in my
                        lane. | unseen: No attributes reported that were not seen. | result: consistent
Step 5  Rule            left_boundary: My car is not allowed to cross the solid white line on the left.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: My car is allowed to cross the broken white line on the right.
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): The solid white line on the left prohibits it.
Step 6  change_right    allowed (correct): The broken white line on the right allows it.
Step 6  go_straight     allowed (contested, correct): No markings prohibit going straight.
Step 6  turn_left       not_determined: Not determined.
Step 6  turn_right      not_determined: Not determined.
Step 6  u_turn          not_determined: Not determined.
Step 6  enter_waiting_areanot_applicable: Not applicable.
Step 7  Reflect         consistent
Advice                  You can continue straight or change lanes to the right. Be cautious when changing
                        lanes.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 603, 13.49 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test C | llama4:scout
----------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes for traffic in the same direction (lanes 3, mine
                        2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on its left to change
                        lanes [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line on its right to change
                        lanes [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): left_ boundary is solid white line [US-3B.06-05-06], prohibited
Step 6  change_right    prohibited (WRONG, label allowed): right boundary is solid white line
                        [US-3B.06-05-06], prohibited
Step 6  go_straight     allowed (contested, correct): no marking governs this action, allowed
Step 6  turn_left       not_determined: no arrow in my lane, not determined
Step 6  turn_right      not_determined: no arrow in my lane, not determined
Step 6  u_turn          not_determined: no arrow in my lane, not determined
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane next to my lane,
                          not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; do not change lanes
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 614, 9.53 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test C | llama4:scout
------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes for traffic traveling in the same direction (lanes
                        4, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on its left to change
                        lanes [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line on its right to change
                        lanes [[US-3B.06-05-06]]
Step 6  change_left     prohibited: prohibited by left_boundary [US-3B.06-05-06]
Step 6  change_right    prohibited: prohibited by right_boundary [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): not prohibited
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane; you can go straight ahead
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9302, out 568, 26.3 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test C | llama4:scout
------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes for traffic traveling in the same direction (lanes
                        3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): left_ boundary [US-3B.06-05-06]: prohibited
Step 6  change_right    prohibited (WRONG, label allowed): right boundary [US-3B.06-05-06]: prohibited
Step 6  go_straight     allowed (contested, label not_determined): no marking governs this action
Step 6  turn_left       not_applicable: no arrow and no prohibited- movement marking in my lane; no waiting
                        area and no two-way left-turn lane
Step 6  turn_right      not_applicable: no arrow and no prohibited- movement marking in my lane; no waiting
                        area and no two-way left-turn lane
Step 6  u_turn          not_applicable: no arrow and no prohibited- movement marking in my lane; no waiting
                        area and no two-way left-turn lane
Step 6  enter_waiting_areanot_applicable: no waiting area and no two-way left-turn lane
Step 7  Reflect         consistent
Advice                  keep in your lane; you may go straight ahead
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['symbol:other']), actions False, unsafe [], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 9302, out 623, 14.03 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test C | llama4:scout
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway bridge with a cityscape ahead (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on its left
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line on its right
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited by left_boundary [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by right_boundary [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane; go straight ahead
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 563, 13.04 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test C | llama4:scout
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a bridge ahead, trees on both sides (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): left_ boundary [US-3B.06-05-06] prohibits it
Step 6  change_right    prohibited (WRONG, label allowed): right boundary [US-3B.06-05-06] prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane, do not change lanes
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 569, 12.78 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test C | llama4:scout
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a clear sky and sun (lanes 4, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on its left
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line on its right
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (correct): prohibited by left_boundary [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by right_boundary [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane, changing lanes is not allowed
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 560, 13.83 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with an intersection ahead (lanes None, mine None, insufficient)
Step 2  Left            a solid white line on the left
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): an arrow pointing straight ahead
Step 4  Cross-check     position: inconsistent | roles: consistent | markings: consistent | unseen:  | result:
                        inconsistent
Step 5  Rule            left_boundary: A solid white lane line marking discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line marking discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: This marking indicates the mandatory or permissible movements in this
                        lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): left_ boundary [US-3B.06-05-06] prohibits
Step 6  change_right    prohibited (correct): right boundary [US-3B.06-05-06] prohibits
Step 6  go_straight     allowed (correct): arrow:straight [US-3B.23-01] allows
Step 6  turn_left       not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  turn_right      not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  follow the straight arrow in your lane; do not change lanes.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['line:crosswalk', 'line:stop_line']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 642, 14.34 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road at an intersection with a traffic light (lanes None, mine None,
                        insufficient)
Step 2  Left            a solid white line on the left
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): an arrow pointing straight ahead
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line marking discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line marking discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: This marking indicates the mandatory or permissible movements in this
                        lane. [[US-3B.23-01]]
Step 6  change_left     prohibited (correct): prohibited by left boundary [US-3B.06-05-06]
Step 6  change_right    prohibited (correct): prohibited by right boundary [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): allowed by arrow:straight [US-3B.23-01]
Step 6  turn_left       not_applicable: not determined
Step 6  turn_right      not_applicable: not determined
Step 6  u_turn          not_applicable: not determined
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You can go straight ahead. Lane changes are not allowed.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['line:crosswalk', 'line:stop_line']), actions True, unsafe
                        [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 639, 14.19 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a median, going straight ahead (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane, a wide shoulder or parking area
                        beyond it
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: the solid white lane line marking on my left discourages crossing it
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: the solid white lane line marking on my right discourages crossing it
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): left_boundary solid white line [US-3B.06-05-06],
                        prohibited
Step 6  change_right    prohibited (WRONG, label allowed): right_boundary solid white line [US-3B.06-05-06],
                        prohibited
Step 6  go_straight     allowed (contested, correct): no marking governs this action, allowed
Step 6  turn_left       not_applicable: no marking governs this action, not_applicable
Step 6  turn_right      not_applicable: no marking governs this action, not_applicable
Step 6  u_turn          not_applicable: no marking governs this action, not_applicable
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane ahead of my lane,
                          not_applicable
Step 7  Reflect         consistent
Advice                  stay in your lane, as changing lanes is prohibited; follow the road ahead and traffic
                        signals for turning instructions
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 623, 13.91 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a median, straight ahead (lanes 4, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: A solid white lane line marking discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: A solid white lane line marking discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): left_boundary solid, [US-3B.06-05-06] prohibits
Step 6  change_right    prohibited (WRONG, label allowed): right_boundary solid, [US-3B.06-05-06] prohibits
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_determined: no marking governs this action
Step 6  turn_right      not_determined: no marking governs this action
Step 6  u_turn          not_determined: no marking governs this action
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  You are in a lane that is delineated by solid white lines on both sides. You can
                        continue straight ahead in this lane. Lane changes are prohibited.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 590, 13.16 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes, possibly an urban or suburban highway (lanes 4,
                        mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line [[US-3B.06-05-06]]
Step 6  change_left     prohibited (contested, correct): left_ boundary is solid white line [US-3B.06-05-06],
                        prohibited
Step 6  change_right    prohibited (contested, label allowed): right boundary is solid white line
                        [US-3B.06-05-06], prohibited
Step 6  go_straight     allowed (contested, correct): no markings prohibit it
Step 6  turn_left       not_applicable: no markings govern it
Step 6  turn_right      not_applicable: no markings govern it
Step 6  u_turn          not_applicable: no markings govern it
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  follow the lane markings and traffic rules, and be prepared for intersections or exits
                        ahead
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 583, 14.2 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test C | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes, approaching an intersection or a straight path
                        (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right side of my lane, with a curb beyond it
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): two white arrows pointing straight ahead in my lane
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not change lanes across the left boundary [[US-3B.06-01]]
Step 5  Rule            right_boundary: my car may not drive left of the right boundary [[US-3B.09-01-02]]
Step 5  Rule            arrow:straight: my car is expected to go straight ahead [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by left boundary [US-3B.06-01]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by right boundary [US-3B.09-01-02]
Step 6  go_straight     allowed (correct): allowed by arrow:straight [US-3B.23-01]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not determined
Step 6  turn_right      not_applicable (WRONG, label prohibited): not determined
Step 6  u_turn          not_applicable (WRONG, label prohibited): not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 650, 14.66 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test C | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes for traffic traveling in the same direction (lanes
                        None, mine None, insufficient)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: insufficient | roles: consistent | markings: consistent | unseen: no |
                        result: consistent
Step 5  Rule            left_boundary: This solid white line discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: This solid white line discourages or prohibits crossing.
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by left boundary [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label not_determined): prohibited by right boundary
                        [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): not determined
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  Drive in your lane and do not change lanes. Follow traffic signals and signs for
                        turning instructions.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 562, 11.91 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test C | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with a right turn ahead, my car is near the bottom of the photo (lanes
                        3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right side of my lane
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on its left to change
                        lanes [[US-3B.06-01]]
Step 5  Rule            right_boundary: my car may not cross a solid yellow edge line on its right to change
                        lanes [[US-3B.09-01-02]]
Step 6  change_left     prohibited (correct): left_ boundary [US-3B.06-01] prohibits it
Step 6  change_right    prohibited (WRONG, label allowed): right boundary [US-3B.09-01-02] prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no arrow and no prohibited- movement marking in my lane; no waiting
                        area and no two-way left-turn lane
Step 6  turn_right      not_applicable: no arrow and no prohibited- movement marking in my lane
Step 6  u_turn          not_applicable: no arrow and no prohibited- movement marking in my lane
Step 6  enter_waiting_areanot_applicable: no waiting area and no two-way left-turn lane
Step 7  Reflect         consistent
Advice                  keep in my lane and go straight ahead; do not change lanes
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 619, 13.81 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test C | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a bridge ahead (lanes None, mine None, insufficient)
Step 2  Left            a white solid line on the left side of my lane
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           a white solid line on the right side of my lane
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        arrow:straight (full): a white arrow pointing straight ahead
Step 4  Cross-check     position: insufficient evidence | roles: consistent | markings: consistent | unseen:
                        no | result: consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on its left
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line on its right
                        [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: my car is permitted to go straight ahead [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by left boundary, [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by right boundary, [US-3B.06-05-06]
Step 6  go_straight     allowed (contested, correct): permitted by arrow:straight, [US-3B.23-01]
Step 6  turn_left       not_applicable: not determined
Step 6  turn_right      not_applicable: not determined
Step 6  u_turn          not_applicable: not determined
Step 6  enter_waiting_areanot_applicable: not determined
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; do not change lanes
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 654, 14.48 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test C | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway bridge with a straight road ahead (lanes 3, mine 2, full)
Step 2  Left            a white solid line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a white solid line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line on its left
                        [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line on its right
                        [[US-3B.06-05-06]]
Step 6  change_left     prohibited (WRONG, label allowed): left_ boundary [US-3B.06-05-06] prohibits it
Step 6  change_right    prohibited (WRONG, label allowed): right boundary [US-3B.06-05-06] prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; do not change lanes
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 560, 14.23 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test C | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes for traffic traveling in the same direction (lanes
                        4, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): an arrow pointing straight ahead
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not cross a solid white lane line [[US-3B.06-05-06]]
Step 5  Rule            right_boundary: my car may not cross a solid white lane line [[US-3B.06-05-06]]
Step 5  Rule            arrow:straight: my car is permitted to go straight ahead [[US-3B.23-01]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by left boundary, [US-3B.06-05-06]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by right boundary, [US-3B.06-05-06]
Step 6  go_straight     allowed (correct): permitted by arrow:straight, [US-3B.23-01]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not determined
Step 6  turn_right      not_applicable (WRONG, label prohibited): not determined
Step 6  u_turn          not_applicable (WRONG, label prohibited): not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; do not change lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 9302, out 650, 14.52 s
```
