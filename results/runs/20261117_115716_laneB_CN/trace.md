# Reasoning of lane run 20261117_115716_laneB_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with a central barrier, heading straight ahead (lanes 3, mine 2,
                        full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane, with a crash barrier beyond it
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right [[CN-5.2.2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by left_boundary, [CN-6.2.1]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by right_boundary, [CN-5.2.2]
Step 6  go_straight     allowed (contested, correct): not determined
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane; you may change right if necessary
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_right'], citation unlisted, contradictions
                        []
Tokens                  in 8374, out 559, 15.47 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with traffic moving in the same direction, straight ahead (lanes 3,
                        mine 2, full)
Step 2  Left            a broken white line on the left side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane, next to a shoulder or parking area
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may change lanes to the left across this broken line
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: my car must not change lanes to the right across this solid edge line
                        [[CN-5.4.3]]
Step 6  change_left     allowed (correct): left_boundary [CN-5.2.1-2], allowed
Step 6  change_right    prohibited (correct): right_boundary [CN-5.4.3], prohibited
Step 6  go_straight     allowed (contested, correct): no marking governs this action, allowed
Step 6  turn_left       not_applicable: no marking governs this action, not_applicable
Step 6  turn_right      not_applicable: no marking governs this action, not_applicable
Step 6  u_turn          not_applicable: no marking governs this action, not_applicable
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane ahead of my lane,
                          not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane; do not change lanes to the right
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8374, out 605, 16.19 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a guardrail on the right and a large truck on the left,
                        straight ahead (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane, with a lane of traffic to its left
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a guardrail on the right side of my lane, with no painted line
                        none none, curb no, other, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not change lanes to the left across the solid white line
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: there is no marking governing change_rite
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by left_boundary [CN-6.2.1]
Step 6  change_right    not_determined (correct): not_determined
Step 6  go_straight     allowed (contested, correct): not_applicable
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane; do not change lanes to the left
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8374, out 558, 28.63 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with a cityscape ahead (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right side of my lane, beyond which is a concrete barrier
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on its left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: the solid yellow line on the right marks the edge of the road and my
                        car must not cross it [[CN-5.4.3]]
Step 6  change_left     prohibited (contested, correct): prohibited by [CN-6.2.1] the solid white line on the
                        left
Step 6  change_right    prohibited (contested, correct): prohibited by [CN-5.4.3] the solid yellow line on the
                        right
Step 6  go_straight     allowed (contested, correct): not prohibited, nothing governs it
Step 6  turn_left       not_determined: not determined, no arrow or prohibited- movement marking in my lane
Step 6  turn_right      not_determined: not determined, no arrow or prohibited- movement marking in my lane
Step 6  u_turn          not_determined: not determined, no arrow or prohibited- movement marking in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable, no waiting area or two-way left- turn lane
Step 7  Reflect         consistent
Advice                  keep in your lane, do not change lanes; you can go straight ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions None, unsafe [], citation accepted, contradictions []
Tokens                  in 8374, out 623, 16.33 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with buildings on both sides, going straight ahead (lanes 3, mine 2,
                        full)
Step 2  Left            a solid white line on the left, with a broken white line to its left
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right, with a concrete barrier beyond it
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        text:keep_clear (full): two white lines forming a cross with an arrow pointing right
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not change lanes to the left across the solid line
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: the edge line on the right side of the direction of travel shall be
                        white, but it is yellow here [[CN-5.4.3]]
Step 5  Rule            right_boundary: a motor/ non-motor separation line between traffic in the same
                        direction shall be white, but it is yellow here [[CN-5.4.5]]
Step 5  Rule            right_boundary: the solid yellow line prohibits vehicles in both directions from
                        crossing [[CN-6.1.1]]
Step 5  Rule            text:keep_clear: vehicles must follow the set path and may not drive on or across the
                        lines [[CN-6.8.1]]
Step 6  change_left     prohibited (contested, label allowed): prohibited by left_boundary, [CN-6.2.1]
Step 6  change_right    prohibited (contested, label allowed): prohibited by right_boundary, [CN-6.1.1]
Step 6  go_straight     allowed (contested, correct): allowed
Step 6  turn_left       not_applicable: not_applicable
Step 6  turn_right      not_applicable: not_applicable
Step 6  u_turn          not_applicable: not_applicable
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in this lane and go straight; do not change lanes
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['text:keep_clear'], missed ['text:bus']), actions None, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8374, out 764, 33.75 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test B | llama4:scout
----------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with a tunnel ahead, part of a highway or expressway (lanes 3, mine
                        2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane and a wide shoulder or emergency lane
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: the edge line on the right marks the edge of the roadway and guides
                        vehicles to keep to the right [[CN-5.4.2]]
Step 6  change_left     prohibited (correct): prohibited by [CN-6.2.1] the solid lane line on the left
Step 6  change_right    allowed (WRONG, label prohibited): allowed by [CN-5.4.2] the broken line is not seen
                        but the edge line on the right does not prohibit it
Step 6  go_straight     allowed (contested, correct): not prohibited, nothing in view governs it
Step 6  turn_left       not_determined: not determined, no arrow or prohibited movement marking in my lane
Step 6  turn_right      not_determined: not determined, no arrow or prohibited movement marking in my lane
Step 6  u_turn          not_determined: not determined, no arrow or prohibited movement marking in my lane
Step 6  enter_waiting_areanot_applicable: not_applicable, no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  keep in the current lane; change to the right lane if necessary, but not to the left
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation in_pack_not_accepted,
                        contradictions []
Tokens                  in 8374, out 639, 16.81 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test B | llama4:scout
----------------------------------------------------------------------------------------------------
Step 1  Scene           a straight urban road with one lane in each direction (lanes 2, mine 1, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane, a curb, and a bike path
                        white dashed, curb yes, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may not change lanes across the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may change lanes across the broken white line on the right
                        [[CN-6.2.3]]
Step 6  change_left     prohibited (correct): prohibited by [CN-6.2.1], the solid line on the left
Step 6  change_right    allowed (WRONG, label prohibited): allowed by [CN-6.2.3], the broken line on the right
Step 6  go_straight     allowed (contested, correct): not determined
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in this lane; do not change lanes to the left; you may change lanes to the right
                        if it is safe
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions
                        ['leftmost lane, but a lane line on the left', 'change_right allowed across a curb']
Tokens                  in 8374, out 581, 15.76 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test B | llama4:scout
----------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with traffic moving in the same direction, approaching an
                        intersection or a merge (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): a solid white line across my lane in the distance
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right [[CN-5.2.2]]
Step 5  Rule            line:stop_line: my car must stop before this line if required to do so [[CN-6.4.1-2]]
Step 6  change_left     prohibited (correct): prohibited by left_boundary, [CN-6.2.1]
Step 6  change_right    allowed (correct): allowed by right_boundary, [CN-5.2.2]
Step 6  go_straight     not_determined (contested, label allowed): not determined
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  stay in your lane; you may change right if necessary, and follow traffic signals ahead
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation unlisted,
                        contradictions []
Tokens                  in 8374, out 651, 16.96 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test B | llama4:scout
----------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with traffic moving in the same direction, straight ahead (lanes 3,
                        mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right [[CN-5.2.2]]
Step 6  change_left     prohibited (correct): prohibited by [CN-6.2.1], the solid white line on the left
Step 6  change_right    allowed (correct): allowed by [CN-5.2.2], the broken white line on the right
Step 6  go_straight     not_applicable (contested, label allowed): not determined
Step 6  turn_left       not_applicable: not determined
Step 6  turn_right      not_applicable: not determined
Step 6  u_turn          not_applicable: not determined
Step 6  enter_waiting_areanot_applicable: not determined
Step 7  Reflect         consistent
Advice                  keep in your lane; you may change right when it is safe
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8374, out 562, 10.42 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test B | llama4:scout
------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes in the same direction (lanes 4, mine 2, full)
Step 2  Left            a solid white line on the left side
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 6  change_left     not_applicable: no marking governs this action
Step 6  change_right    not_applicable: no marking governs this action
Step 6  go_straight     allowed (contested, correct): no arrow in my lane is "allowed"
Step 6  turn_left       not_applicable: not determined
Step 6  turn_right      not_applicable: not determined
Step 6  u_turn          not_applicable: not determined
Step 6  enter_waiting_areanot_applicable: not determined
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; do not change lanes.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added [],
                        missed ['line:crosswalk']), actions None, unsafe [], citation none_needed,
                        contradictions []
Tokens                  in 8374, out 377, 23.6 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test B | llama4:scout
------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes for each direction, lined with trees and buildings
                        on both sides (lanes None, mine None, insufficient)
Step 2  Left            a white solid line on the left side of my lane, with a short white line and a blue
                        signboard with a white character on it to its left
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a yellow line on the right side of my lane, which seems to be a double yellow line
                        with a broken line on the right side of it
                        yellow double_solid, curb no, center_line, evidence full
Step 3  Markings        arrow:straight (full): an arrow pointing straight ahead in my lane
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on its left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: vehicles in both directions are prohibited from crossing the double
                        yellow line on its right [[CN-6.1.2]]
Step 5  Rule            arrow:straight: the arrow pointing straight ahead in my lane indicates that I am
                        allowed to go straight [[CN-5.13.2]]
Step 6  change_left     prohibited (correct): prohibited by [CN-6.2.1], the solid white line on its left
Step 6  change_right    not_determined (WRONG, label allowed): not determined, the feature that decides it is
                        hidden
Step 6  go_straight     allowed (contested, label not_determined): allowed by arrow:straight
Step 6  turn_left       not_applicable: not applicable, no arrow or prohibited- movement marking in my lane
Step 6  turn_right      not_applicable: not applicable, no arrow or prohibited- movement marking in my lane
Step 6  u_turn          not_applicable: not applicable, no arrow or prohibited- movement marking in my lane
Step 6  enter_waiting_areanot_applicable: not applicable, no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  follow the straight arrow in your lane and do not change lanes unless necessary; be
                        cautious of the double yellow line on your right and the solid white line on your left
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['symbol:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions ['change_right not_determined with full
                        evidence']
Tokens                  in 8374, out 752, 18.31 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test B | llama4:scout
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway or freeway with a concrete median barrier, heading straight ahead
                        with no intersection or ramp in view (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane, with a broken white line to its left
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane, with a concrete barrier beyond it
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on its left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car is prohibited from crossing the solid white line on its right
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): left_boundary [CN-6.2.1] prohibits it
Step 6  change_right    prohibited (correct): right_boundary [CN-6.2.1] prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; do not change lanes
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8374, out 582, 16.06 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test B | llama4:scout
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a bridge ahead, in a rural or suburban area (lanes 3, mine
                        2, full)
Step 2  Left            a solid white line on the left side of my lane, with a crash barrier beyond it
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on its left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on its right [[CN-5.2.2]]
Step 6  change_left     prohibited (correct): prohibited by left_boundary, [CN-6.2.1]
Step 6  change_right    allowed (correct): allowed by right_boundary, [CN-5.2.2]
Step 6  go_straight     allowed (contested, correct): not determined
Step 6  turn_left       not_applicable: not determined
Step 6  turn_right      not_applicable: not determined
Step 6  u_turn          not_applicable: not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane; you may change right at the next opportunity
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8374, out 566, 13.46 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test B | llama4:scout
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a central barrier, heading straight ahead (lanes 4, mine 2,
                        full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car is prohibited from crossing the solid white line on the right
                        [[CN-6.2.1]]
Step 6  change_left     prohibited (correct): prohibited by left_boundary, [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by right_boundary, [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): not determined
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane, do not change lanes
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8374, out 550, 16.42 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with an intersection ahead (lanes None, mine None, insufficient)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): an arrow pointing straight ahead
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: my car is guided to go straight ahead [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by left_boundary, [CN-6.2.1]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by right_boundary, [CN-5.2.1-2]
Step 6  go_straight     allowed (correct): guided by arrow:straight, [CN-5.13.1]
Step 6  turn_left       not_applicable (WRONG, label prohibited): not determined
Step 6  turn_right      not_applicable (WRONG, label prohibited): not determined
Step 6  u_turn          not_applicable (WRONG, label prohibited): not determined
Step 6  enter_waiting_areanot_applicable: not determined
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; changing lanes to the right is allowed.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added [],
                        missed ['line:crosswalk', 'line:stop_line']), actions False, unsafe ['change_right'],
                        citation accepted, contradictions []
Tokens                  in 8374, out 639, 17.9 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road that leads to an intersection ahead, my car is near the bottom of the
                        photo (lanes None, mine None, insufficient)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): a straight arrow pointing straight ahead
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        side of my lane [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right side of my lane
                        [[CN-6.2.2]]
Step 5  Rule            arrow:straight: my car is allowed to go straight ahead [[CN-5.13.1]]
Step 6  change_left     prohibited (correct): prohibited by left_boundary, [CN-6.2.1]
Step 6  change_right    allowed (WRONG, label prohibited): allowed by right_boundary, [CN-6.2.2]
Step 6  go_straight     allowed (contested, correct): allowed by arrow:straight, [CN-5.13.1]
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; changing lanes to the right is allowed
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['line:crosswalk', 'line:stop_line']), actions False,
                        unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8374, out 656, 17.07 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with a central median, heading straight ahead (lanes 3, mine 2,
                        full)
Step 2  Left            a broken white line on the left side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right side of my lane, separating it from a shoulder or
                        another lane
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may change lanes to the left across this broken line
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: this solid yellow line marks the right edge of my lane [[CN-5.4.3]]
Step 6  change_left     allowed (correct): left_ boundary is a broken line [CN-5.2.1-2]
Step 6  change_right    prohibited (WRONG, label allowed): no marking governs this action
Step 6  go_straight     allowed (contested, correct): no arrow in my lane
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  keep in your lane; do not change lanes to the right
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8374, out 567, 16.56 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane road with a straight path ahead, possibly an urban or suburban highway
                        (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right [[CN-5.2.2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by [CN-6.2.1] solid line
Step 6  change_right    allowed (correct): allowed by [CN-5.2.2] broken line
Step 6  go_straight     allowed (contested, correct): not determined
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane; changing lanes to the right is allowed
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation unlisted, contradictions []
Tokens                  in 8374, out 548, 15.27 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes, possibly an urban or suburban road (lanes 4, mine
                        2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): an arrow pointing straight ahead
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right [[CN-5.2.1-2]]
Step 5  Rule            arrow:straight: my car is guided to go straight ahead [[CN-5.13.1]]
Step 6  change_left     prohibited (contested, correct): prohibited by [CN-6.2.1], the solid white line on the
                        left
Step 6  change_right    allowed (contested, correct): allowed by [CN-5.2.1-2], the broken white line on the
                        right
Step 6  go_straight     allowed (contested, correct): guided by arrow:straight
Step 6  turn_left       not_determined: not determined, no arrow or prohibited marking
Step 6  turn_right      not_determined: not determined, no arrow or prohibited marking
Step 6  u_turn          not_determined: not determined, no arrow or prohibited marking
Step 6  enter_waiting_areanot_applicable: not applicable, no waiting area or two-way left-turn lane
Step 7  Reflect         consistent
Advice                  keep in your lane, you can go straight ahead; changing lanes to the right is allowed
                        but check for safety
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8374, out 678, 13.71 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test B | llama4:scout
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes in the same direction (lanes 3, mine 2, full)
Step 2  Left            a broken white line on the left side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right side of my lane, with a curb beyond it
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): two white arrows pointing straight ahead
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not change lanes across the left boundary [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: my car may not drive on the right side of the right boundary
                        [[CN-5.4.3]]
Step 5  Rule            arrow:straight: my car is guided to go straight ahead [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): left_ boundary [CN-5.2.1-2] prohibits it
Step 6  change_right    prohibited (WRONG, label allowed): right boundary [CN-5.4.3] prohibits it
Step 6  go_straight     allowed (correct): arrow:straight [CN-5.13.1] allows it
Step 6  turn_left       not_applicable (WRONG, label prohibited): no arrow or marking governs this action, not
                        determined
Step 6  turn_right      not_applicable (WRONG, label prohibited): no arrow or marking governs this action, not
                        determined
Step 6  u_turn          not_applicable (WRONG, label prohibited): no arrow or marking governs this action, not
                        determined
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left-turn lane ahead of my lane,
                          not_applicable
Step 7  Reflect         consistent
Advice                  keep in this lane and go straight ahead; do not change lanes
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions ['change_left
                        prohibited across a broken lane line']
Tokens                  in 8374, out 684, 20.38 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test B | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes for the same direction, approaching an
                        intersection (lanes 4, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane, with a broken white line to its left
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane, with a solid white line to its right
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right [[CN-6.2.2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by [CN-6.2.1], left boundary is solid
Step 6  change_right    allowed (WRONG, label not_determined): allowed by [CN-6.2.2], right boundary is broken
Step 6  go_straight     allowed (contested, correct): not determined
Step 6  turn_left       not_applicable: not determined
Step 6  turn_right      not_applicable: not determined
Step 6  u_turn          not_applicable: not determined
Step 6  enter_waiting_areanot_applicable: not determined
Step 7  Reflect         consistent
Advice                  keep in your lane; you may change right at the next intersection if necessary
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8374, out 576, 19.18 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test B | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with three lanes for traffic in the same direction, approaching an
                        intersection (lanes 3, mine 2, full)
Step 2  Left            a broken white line on the left side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           a solid yellow line on the right side of my lane, with a wide shoulder or parking area
                        beyond it
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen:  | result:
                        consistent
Step 5  Rule            left_boundary: my car may change lanes to the left across this broken line
                        [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: my car must not cross this edge line on the right side of the road
                        [[CN-5.4.3]]
Step 6  change_left     allowed (WRONG, label prohibited): left_ boundary [CN-5.2.1-2] allows it
Step 6  change_right    prohibited (WRONG, label allowed): right boundary [CN-5.4.3] prohibits it
Step 6  go_straight     allowed (contested, correct): no marking governs this action
Step 6  turn_left       not_applicable: no marking governs this action
Step 6  turn_right      not_applicable: no marking governs this action
Step 6  u_turn          not_applicable: no marking governs this action
Step 6  enter_waiting_areanot_applicable: no marking governs this action
Step 7  Reflect         consistent
Advice                  keep in your lane; you may turn right or go straight ahead at the intersection
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation accepted, contradictions
                        []
Tokens                  in 8374, out 588, 13.82 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test B | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with multiple lanes, leading to an intersection or a merge ahead
                        (lanes 4, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a solid white line on the right side of my lane
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): an arrow pointing straight ahead
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car is prohibited from crossing the solid white line on the right
                        [[CN-6.2.1]]
Step 5  Rule            arrow:straight: my car is allowed to go straight ahead [[CN-5.13.1]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by left_boundary, [CN-6.2.1]
Step 6  change_right    prohibited (WRONG, label allowed): prohibited by right_boundary, [CN-6.2.1]
Step 6  go_straight     allowed (contested, correct): allowed by arrow:straight, [CN-5.13.1]
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not applicable
Step 7  Reflect         consistent
Advice                  keep in your lane and go straight ahead; do not change lanes
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed ['text:other']), actions False, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8374, out 645, 17.92 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test B | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a multi-lane highway with a bridge ahead, in China (lanes 3, mine 2, full)
Step 2  Left            a solid white line on the left side of my lane
                        white solid, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car is prohibited from crossing the solid white line on the left
                        [[CN-6.2.1]]
Step 5  Rule            right_boundary: my car may cross the broken white line on the right [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): prohibited by [CN-6.2.1], left_boundary is solid
Step 6  change_right    allowed (correct): allowed by [CN-5.2.1-2], right_boundary is broken
Step 6  go_straight     allowed (contested, correct): not determined
Step 6  turn_left       not_determined: not determined
Step 6  turn_right      not_determined: not determined
Step 6  u_turn          not_determined: not determined
Step 6  enter_waiting_areanot_applicable: not_applicable
Step 7  Reflect         consistent
Advice                  keep in your lane; you may change right if necessary
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8374, out 561, 15.53 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test B | llama4:scout
------------------------------------------------------------------------------------------------------
Step 1  Scene           a straight road with three lanes for my direction (lanes 3, mine 1, full)
Step 2  Left            a broken white line on the left side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           a broken white line on the right side of my lane
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: consistent | roles: consistent | markings: consistent | unseen: no | result:
                        consistent
Step 5  Rule            left_boundary: my car may not change lanes to the left across this line [[CN-5.2.1-2]]
Step 5  Rule            right_boundary: my car may not change lanes to the right across this line
                        [[CN-5.2.1-2]]
Step 6  change_left     prohibited (WRONG, label allowed): left boundary prohibits it
Step 6  change_right    prohibited (WRONG, label allowed): right boundary prohibits it
Step 6  go_straight     allowed (correct): no marking governs this action
Step 6  turn_left       not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  turn_right      not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  u_turn          not_applicable (WRONG, label prohibited): no marking governs this action
Step 6  enter_waiting_areanot_applicable: no waiting area or two-way left turn lane ahead of my lane
Step 7  Reflect         consistent
Advice                  keep in this lane; go straight ahead
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:straight']), actions False, unsafe [], citation accepted, contradictions
                        ['leftmost lane, but a lane line on the left', 'change_left prohibited across a broken
                        lane line', 'change_right prohibited across a broken lane line']
Tokens                  in 8374, out 546, 15.11 s
```
