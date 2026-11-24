# Reasoning of lane run 20261116_003746_laneA_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues toward a distant signalized intersection. My
                        car is in the middle of three same-direction lanes, with a reserved bus lane on the
                        right. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A yellow broken line, with long dashes and visible gaps, separates my lane from the
                        bus-marked lane on the right; there is no curb at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle-lane position agrees with a same-direction lane on the left and a
                        reserved lane on the right. | roles: The white broken line fits an ordinary lane
                        divider, and the yellow broken boundary beside the bus-marked lane fits a reserved-
                        lane boundary. | markings: No guidance marking is readable within my lane; the bus-
                        lane writing is beyond its right boundary and does not belong to my lane. | unseen: No
                        distant arrow or intersection stop line is inferred; the far approach is too small to
                        inspect reliably. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits changing to the adjacent
                        lane when safe.
Step 5  Rule            right_boundary: The broken yellow bus-lane boundary does not authorize an ordinary car
                        to enter the reserved lane; with its operating status unverified, treat entry as
                        prohibited.
Step 6  change_left     allowed (WRONG, label prohibited): The white broken lane divider permits crossing when
                        safe.
Step 6  change_right    prohibited (WRONG, label not_determined): The adjacent bus lane is treated as
                        reserved, so its broken boundary does not permit entry by this ordinary car.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken white line when safe;
                        do not enter the reserved bus lane on the right. Recheck lane arrows, signs and
                        signals nearer the intersection before choosing a turning lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6396, out 850, 15.68 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues toward a distant signalized intersection. My
                        car is in the middle lane, with another general lane on the left and an apparent
                        special-use lane on the right. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A yellow broken line, with long dashes and gaps, separates my lane from a paved lane
                        on the right; the raised roadside curb is beyond that lane, not at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence partial
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible near the
                        bottom of my lane, but its lower portion is hidden by the hood.
Step 4  Cross-check     position: The lane on the left and the apparent special-use lane on the right place my
                        lane second among three same-direction lanes. | roles: The white broken left boundary
                        fits a normal lane divider. The yellow broken right boundary suggests a special-use
                        lane rather than an opposing-traffic boundary, since opposing traffic is beyond the
                        median fence. | markings: The visible forward arrowhead agrees with continuing along
                        this lane, but the hidden lower portion prevents ruling out an additional arrow
                        branch. | unseen: The right lane's reservation text and operating restrictions are not
                        readable, and the complete arrow and distant intersection markings cannot be seen. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane divider in China permits changing into the adjacent
                        same-direction lane when safe.
Step 5  Rule            right_boundary: A broken boundary does not itself prohibit crossing, but an ordinary
                        car must not enter a reserved special-use lane; the reservation here is not
                        conclusively readable.
Step 5  Rule            arrow:straight: A forward lane-use arrow permits going straight, while any additional
                        permitted movements depend on whether the partly hidden arrow has other branches.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe left lane change.
Step 6  change_right    not_determined (correct): The yellow broken boundary appears to border a special-use
                        lane, but its reservation cannot be confirmed from readable markings.
Step 6  go_straight     allowed (contested, correct): The visible forward arrowhead permits going straight.
Step 6  turn_left       not_determined: The lower arrow portion is hidden, so a possible left branch cannot be
                        checked.
Step 6  turn_right      not_determined: The lower arrow portion is hidden, so a possible right branch cannot
                        be checked.
Step 6  u_turn          not_determined: The complete arrow is hidden, so its full movement restrictions cannot
                        be established.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, observing the signals ahead; a safe left lane change
                        is permitted by the broken white line. Avoid entering the apparent special-use lane on
                        the right until its restrictions are clear, and confirm the complete arrows before
                        choosing a turning lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1113, 24.79 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight ahead, with a median fence on the
                        left and a curbside bus lane on the right. My car is in the middle of three same-
                        direction lanes; no intersection or lane ending is clearly visible. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line, with long painted segments and intervening gaps, separates my
                        lane from another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible segments and gaps separates my lane from the curbside
                        lane, identified as a bus lane by roadside bus-lane signage; no curb is on this
                        boundary itself.
                        white dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with a normal traffic lane to the left and a reserved
                        lane to the right. | roles: The broken white boundaries fit a same-direction lane
                        divider and the boundary of a same-direction bus lane. | markings: No guidance marking
                        is readable within my lane; markings in the curbside lane are outside my lane. |
                        unseen: No hidden arrow or distant intersection marking is assumed; the vehicle ahead
                        obscures some pavement. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: Although the broken boundary is crossable in principle, an ordinary
                        car must not enter the adjoining reserved bus lane under the reserved-lane assumption.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): The adjoining lane is reserved for buses, so
                        entering it is prohibited for this ordinary car.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No marking in view governs this action.
Step 6  turn_right      not_applicable: No marking in view governs this action.
Step 6  u_turn          not_applicable: No marking in view governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken line after checking
                        traffic; do not enter the reserved bus lane on the right. The bus-lane sign displays
                        6:00–22:00; check applicable restrictions and upcoming turn guidance before preparing
                        any turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 865, 15.11 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight beside an elevated structure, with no
                        intersection or lane ending visible. My car is in the leftmost lane; three same-
                        direction lanes appear present, though the rightmost lane is partly obscured. (lanes
                        3, mine 1, partial)
Step 2  Left            A solid white line runs beside a raised concrete median topped by a metal fence, with
                        opposing traffic beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction traffic lane; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is leftmost, consistent with the median-side edge on the left and a
                        same-direction lane on the right; the total lane count is less certain because of
                        right-side vehicle occlusion. | roles: The solid white line follows the physical
                        median edge, while the broken white line separates same-direction lanes. | markings:
                        No arrows, words, symbols or transverse markings are visible in my lane; the irregular
                        pale trace on the pavement is not a recognizable guidance marking. | unseen: No
                        intersection layout or markings beyond the visible stretch are inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The raised median forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits changing into the
                        adjacent same-direction lane when safe.
Step 6  change_left     prohibited (correct): The raised median at the left edge prohibits crossing out of my
                        lane.
Step 6  change_right    allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  go_straight     allowed (contested, correct): No lane-use marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; do not cross the median on the left. A rightward lane
                        change is permitted by the dashed line, but check the adjacent vehicles and blind spot
                        before moving.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 853, 16.28 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight alongside an elevated structure, with
                        construction fencing beside the roadway. My car is in the leftmost of three same-
                        direction lanes; no intersection or lane ending is visible ahead. (lanes 3, mine 1,
                        full)
Step 2  Left            A continuous solid white line borders my lane on the left, with a raised concrete edge
                        and metal fence immediately beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments, separated by clear gaps, divide my lane from the same-
                        direction traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the adjacent lane on the right agree with my car
                        occupying lane 1 of three. | roles: The solid white line beside the raised edge fits
                        an edge line, and the broken white line separating same-direction traffic fits a lane
                        line. | markings: No arrows, words, symbols, transverse lines or marked waiting areas
                        are visible in my lane; there is no conflicting lane guidance. | unseen: No distant
                        intersection layout or hidden lane-use marking has been inferred; the irregular pale
                        streaks on the pavement are not identifiable guidance markings. | result: consistent
Step 5  Rule            left_boundary: The roadway edge and raised physical barrier do not permit my car to
                        leave the lane to the left.
Step 5  Rule            right_boundary: A broken white lane divider in China permits changing to the adjacent
                        lane when safe and without interfering with its traffic.
Step 6  change_left     prohibited (correct): The raised roadway edge and fence prohibit leaving the lane to
                        the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a rightward lane change when
                        safe.
Step 6  go_straight     allowed (contested, correct): No lane-use marking restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not move left toward the raised edge. A
                        rightward lane change is permitted by the marking, but wait for a safe gap around the
                        vehicles beside you.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 828, 10.84 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues ahead, with a planted median on the left and
                        shops and roadside vehicles on the right. My car is in the middle of three same-
                        direction lanes; no intersection or lane ending is clearly visible. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line, with visible dashes and intervening gaps, separates my lane from
                        another traffic lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line has a visible foreground dash and further segments partly obscured
                        by scooters, with another traffic lane beyond it and no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying lane 2 of 3. | roles:
                        Both white broken boundaries fit same-direction lane separators. | markings: No
                        guidance markings are readable in my lane, so none contradict the boundaries. |
                        unseen: No hidden arrow or intersection marking is inferred; vehicles obscure portions
                        of the road ahead. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The white broken left lane separator permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane separator permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken boundary may be crossed only when safe.
                        Check especially carefully for the scooters on the right, and follow lane-use markings
                        when the next intersection becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 812, 12.49 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues toward a pedestrian overpass; no intersection
                        or lane ending is clearly visible. My car is in the middle of three same-direction
                        lanes, with a marked bus lane on the right. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction traffic lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A yellow broken line, with long dashes and clear gaps, separates my lane from the
                        right-hand lane bearing white bus-lane lettering; there is no curb on this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and the bus-lane boundary on the right agree with
                        my lane being second of three same-direction lanes. | roles: The white broken line
                        fits an ordinary lane divider; the yellow broken line and adjacent bus-lane lettering
                        support a reserved-lane boundary, not a center line. | markings: No guidance marking
                        is readable in my own lane; the bus-lane lettering is to the right of its boundary and
                        is not an ego-lane marking. | unseen: No distant intersection layout or hidden marking
                        is inferred; the vehicle ahead obscures some pavement. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: The adjoining bus lane is treated as reserved for this ordinary car,
                        so entry is prohibited despite the broken boundary.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change.
Step 6  change_right    prohibited (contested, correct): The right boundary leads into a reserved bus lane,
                        which this ordinary car must not enter.
Step 6  go_straight     allowed (contested, correct): No visible ego-lane marking restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No visible ego-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible ego-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible ego-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken white line only when safe; do
                        not enter the bus lane on the right. Turn-lane assignments and a stopping location are
                        not visible, so check subsequent markings before choosing a turning movement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 863, 14.99 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road runs straight beside an elevated roadway in China. My car is in
                        the middle of three same-direction lanes; no intersection or lane ending is clearly
                        visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the same-direction lane occupied by the
                        white car on the right; visible painted stretches are separated by gaps, and there is
                        no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane line
                        on each side. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No readable guidance markings appear in my lane, and none
                        contradict the boundaries. | unseen: No intersection layout or markings beyond the
                        visible road stretch have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No arrow or other visible marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken white boundary may be crossed only after
                        checking for a safe gap, particularly beside the white car on the right. No visible
                        markings establish a turning lane or stopping point here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 816, 14.83 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A barrier-lined urban road continues straight toward an overpass, with no intersection
                        or lane ending visible. My car is in the left lane of two lanes in its direction,
                        immediately to the right of a broken yellow center line. (lanes 2, mine 1, full)
Step 2  Left            A single yellow broken line, with several dashes and gaps visible, separates my lane
                        from the roadway on the left; no curb forms this immediate boundary.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A single white broken line, with long dashes and clear gaps, separates my lane from
                        another traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and same-direction lane line on the right agree
                        with my lane being lane 1 of 2. | roles: The broken yellow line fits a crossable
                        center line, and the broken white line fits a same-direction lane divider. | markings:
                        No guidance marking is visible within my lane; the hatched area farther right lies
                        outside it. | unseen: No hidden arrows, intersection controls, or lane-end markings
                        have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken yellow center line may be crossed for overtaking or
                        bypassing an obstruction when safe, while yielding to opposing traffic.
Step 5  Rule            right_boundary: A broken white lane divider may be crossed to change lanes when safe
                        without interfering with other traffic.
Step 6  change_left     allowed (contested, label prohibited): The broken yellow center line permits crossing
                        for safe overtaking or bypassing, subject to opposing traffic.
Step 6  change_right    allowed (correct): The broken white lane line permits a safe change into the adjacent
                        lane.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right when safe. Crossing the yellow line
                        enters the opposing side and is only appropriate for a safe, permitted overtaking or
                        bypassing maneuver; no intersection turn guidance or stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 941, 19.76 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight ahead, with three lanes in this
                        direction and a reserved bus lane on the right. My car is in the middle lane; no
                        intersection or lane ending is clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken yellow line, with visible long dashes and gaps, separates my lane from
                        the right-hand lane with large white bus-lane lettering; there is no curb at this
                        boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with an ordinary lane to the left and a reserved lane to
                        the right. | roles: The broken white line separates ordinary same-direction lanes; the
                        broken yellow line and adjacent bus-lane markings support a special-lane boundary. |
                        markings: No guidance marking is visible within my lane; the bus-lane lettering is
                        beyond its right boundary. | unseen: No distant intersection layout or obscured
                        guidance marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane line permits changing into the adjacent
                        same-direction lane when safe.
Step 5  Rule            right_boundary: The broken boundary does not override bus-lane reservation, so an
                        ordinary car must not enter the reserved lane under the stipulated reservation
                        assumption.
Step 6  change_left     allowed (correct): The broken white lane line permits crossing into the ordinary lane
                        on the left when safe.
Step 6  change_right    prohibited (contested, correct): The lane beyond the yellow broken boundary is
                        reserved for buses and is treated as unavailable to my ordinary car.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane, or change left across the broken white line after
                        checking traffic; do not enter the reserved bus lane on the right. The roadside bus
                        sign displays operating times, but no visible intersection markings establish turn
                        permissions ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 835, 15.05 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China has opposing traffic separated by a metal median fence. My car
                        is in the leftmost of three apparent same-direction lanes; vehicles and strong glare
                        obscure the road farther ahead, and no intersection or lane ending is clearly visible.
                        (lanes 3, mine 1, partial)
Step 2  Left            A metal median fence forms the left physical boundary, with opposing traffic beyond; a
                        pale line is partly visible along its base, but glare prevents reliable identification
                        of its paint colour and pattern.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A white broken line, showing a long dash and an intervening gap, separates my lane
                        from another same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left agrees with my lane being leftmost, and the
                        broken lane line on the right agrees with another same-direction lane there; the total
                        lane count is less certain because of glare and perspective. | roles: The physical
                        median forms a roadway edge, while the white broken line fits a same-direction lane
                        divider. | markings: No guidance marking can be positively identified in my lane;
                        markings in the lanes to the right do not govern my lane. | unseen: The left paint
                        colour and pattern are unresolved, not confirmed absent; vehicles and glare also hide
                        possible guidance markings farther ahead. | result: consistent
Step 5  Rule            left_boundary: A physical median barrier must not be crossed, so leaving my lane to
                        the left is prohibited.
Step 5  Rule            right_boundary: A white broken same-direction lane divider may be crossed to change
                        lanes when safe and without obstructing other traffic.
Step 6  change_left     prohibited (correct): The median fence physically separates the carriageways and must
                        not be crossed.
Step 6  change_right    allowed (correct): The white broken lane divider permits a safe change into the
                        adjacent ordinary lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane, and no lane ending is visible.
Step 6  turn_left       not_determined: Vehicles and glare obscure the farther lane surface where a movement
                        arrow could govern the next intersection.
Step 6  turn_right      not_determined: Vehicles and glare obscure the farther lane surface where a movement
                        arrow could govern the next intersection.
Step 6  u_turn          not_determined: Any governing movement marking farther ahead is obscured by traffic
                        and glare.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable in view.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change one lane right across the broken white line when safe;
                        do not cross the median fence. Reduce speed for glare and the vehicle ahead, and
                        confirm lane arrows before choosing a turning lane farther ahead.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 977, 16.29 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided three-lane urban road approaches an overpass, with no intersection or lane
                        ending visible. My car is in the leftmost lane, beside the median-side shoulder.
                        (lanes 3, mine 1, full)
Step 2  Left            A continuous white line borders the lane on the left, with yellow rectangular dashes
                        alongside it on the lane side; a narrow paved strip and concrete median barrier lie
                        beyond.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A yellow broken line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the right.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 1 agree with a left roadway edge and
                        a lane boundary on the right. | roles: The solid white line fits a roadway edge; the
                        yellow broken boundary and accompanying yellow edge-side dashes are consistent with a
                        bus-lane treatment, supported by the roadside bus-lane sign. | markings: No arrows,
                        words, symbols or transverse markings are visible in my lane; the yellow dashes run
                        along its boundaries. | unseen: No unseen lane-use arrow, bus word, intersection
                        marking or waiting area has been assumed. The concrete barrier is beyond the paved
                        strip, not directly at the lane boundary. | result: consistent
Step 5  Rule            left_boundary: The solid white roadway edge prohibits crossing left onto the median-
                        side strip in ordinary driving.
Step 5  Rule            right_boundary: The broken bus-lane boundary permits leaving this lane to the ordinary
                        lane on the right when safe; it does not by itself authorize an ordinary car to
                        continue using the reserved lane.
Step 6  change_left     prohibited (contested, correct): The solid white edge line prohibits crossing onto the
                        median-side strip.
Step 6  change_right    allowed (WRONG, label prohibited): The broken boundary permits leaving my lane for the
                        ordinary lane on the right when safe.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow restricts continuing straight, and no
                        lane ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  The roadside sign indicates bus-lane reservation on working days from 17:00 to 19:00;
                        an ordinary car should move right across the broken boundary when safe if that
                        restriction applies. Do not cross the solid left edge; no junction-turn guidance or
                        stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6396, out 917, 18.29 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues straight beneath a pedestrian overpass; no
                        intersection or lane ending is visible. My car is in the middle of three same-
                        direction lanes, with a bus lane on the right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken line with yellow sections and pale, nearly white foreground sections
                        separates my lane from the lane containing bus-lane lettering and a bus on the right;
                        there is no curb along this boundary.
                        yellow dashed, curb no, special_lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 2 agree with an ordinary lane to the left and a
                        reserved bus lane to the right. | roles: The broken white left boundary fits a same-
                        direction lane divider. The broken right boundary and bus-lane context fit a special-
                        lane boundary, although its paint color varies in appearance. | markings: No guidance
                        markings are visible inside my lane; the bus-lane lettering is beyond its right
                        boundary. | unseen: No arrow, stop line, waiting area, or intersection has been
                        inferred beyond the visible road. The right boundary's color is only partially clear.
                        | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: For this ordinary car, the adjacent bus lane is treated as reserved,
                        so entering it is prohibited despite the broken boundary.
Step 6  change_left     allowed (correct): The broken white lane divider permits a left lane change when safe.
Step 6  change_right    prohibited (contested, correct): The right boundary leads into a reserved bus lane,
                        which this ordinary car must not enter.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; change left only after checking traffic, and do not
                        enter the bus lane on the right. No stopping point or turn guidance is visible;
                        observe the posted bus-lane restrictions and the overpass clearance sign.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 890, 13.56 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           The car is on a narrow branch road passing to the right of a landscaped traffic
                        island, with a main carriageway to the left and a roadside non-motorized strip to the
                        right. One motor-vehicle lane is visible on this branch; its eventual junction is not
                        visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous white line borders a white-hatched gore on the left, then follows a
                        raised landscaped island; short yellow rectangular paint segments appear alongside the
                        boundary on the lane side.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates the lane from the roadside strip used by bicycles
                        and scooters, with short yellow rectangular segments alongside it on the lane side;
                        the sidewalk curb is beyond that strip, not at this line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (partial): Short yellow rectangular paint segments repeat along both
                        sides inside the white boundaries; their specific guidance function cannot be
                        identified confidently from this view.
Step 4  Cross-check     position: One motor-vehicle lane between two roadway edges is consistent with the car
                        occupying lane 1; the roadside strip is not counted as another motor-vehicle lane. |
                        roles: The continuous white lines fit roadway-edge roles, and the raised island
                        confirms the left physical edge. | markings: No lane-use arrow or readable word is
                        visible in the lane. The hatched gore is outside its left boundary, and the arrows on
                        the roadside sign are not pavement markings. | unseen: The yellow rectangles are
                        reported without assigning an uncertain function; no unseen intersection markings or
                        lane-use arrows are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge, channelized gore and raised island do not
                        permit a routine lane change to the left.
Step 5  Rule            right_boundary: The solid roadway edge separating the motor lane from the non-
                        motorized roadside strip does not permit a routine lane change into that strip.
Step 5  Rule            symbol:other: The unidentified yellow rectangular markings cannot reliably establish a
                        movement permission or prohibition.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid left edge leads beside a
                        channelized gore and raised island, not an available adjacent lane.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid right edge separates this lane
                        from the non-motorized roadside strip.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing along
                        this lane.
Step 6  turn_left       not_applicable: No marking in the lane governs this action.
Step 6  turn_right      not_applicable: No marking in the lane governs this action; the roadside sign is
                        context only.
Step 6  u_turn          not_applicable: No marking in the lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the white boundaries and follow the branch road, keeping clear of the
                        island and the bicycles and scooters on the right. The sign directs right-turning
                        traffic onto this branch, but the markings at its eventual junction are not visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1182, 26.26 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, three-lane road continues straight beneath an overpass, with traffic ahead
                        and no visible intersection, ramp or lane ending. My car is in the rightmost lane.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a long dash and intervening gap visible, separates my lane
                        from another same-direction traffic lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved shoulder
                        beyond it and a guardrail farther outside the shoulder.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider and right roadway edge agree with being lane 3 of 3. |
                        roles: The broken white line fits a same-direction lane divider, and the solid white
                        line alongside the shoulder fits a roadway edge line. | markings: No painted arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane; the overhead
                        arrows are signs, not pavement markings. | unseen: No hidden pavement marking or
                        unseen intersection layout has been inferred; the van obscures part of the road
                        farther ahead. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider may be crossed to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A solid white roadway edge line permits temporary crossing when
                        necessary, but does not authorize ordinary travel along the shoulder.
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        lane change to the left.
Step 6  change_right    allowed (WRONG, label not_determined): The roadway edge-line rule permits temporary
                        crossing onto the shoulder when necessary, not routine shoulder driving.
Step 6  go_straight     allowed (contested, correct): No visible pavement arrow restricts continuing straight,
                        and the lane does not visibly end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane and maintain a safe following distance; change left only after
                        checking traffic, and do not use the shoulder as a travel lane. The overhead sign
                        identifies this as a through lane with a posted maximum of 100 km/h and minimum of 60
                        km/h, subject to traffic and conditions.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 895, 17.81 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China approaches a signalized intersection. My car is in the
                        rightmost of three same-direction lanes, beside a raised strip separating the roadway
                        from a non-motorized path. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible painted segments and gaps, separates my lane from
                        another same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs beside a raised curb and planted separator, with a non-
                        motorized path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (partial): A white longitudinal guidance-marking stem is visible behind
                        the Audi, but the vehicle hides its arrowhead or heads, so its indicated directions
                        cannot be read.
Step 4  Cross-check     position: Three same-direction lanes and position 3 agree with a lane divider on the
                        left and the roadway edge on the right. | roles: The broken white left divider fits a
                        same-direction lane line; the solid white right line beside the curb fits a roadway
                        edge. | markings: The visible marking stem is within my lane, but its hidden heads
                        prevent checking its directional guidance. No waiting area is identifiable. | unseen:
                        No direction is inferred from the marking stem or from the neighboring lane. The Audi
                        and distance obscure the remaining lane surface toward the intersection. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe.
Step 5  Rule            right_boundary: The solid white roadway edge and raised curb prohibit leaving this
                        lane to the right into the separator or non-motorized path.
Step 5  Rule            symbol:other: A lane-use arrow requires following its indicated directions, but the
                        obscured heads prevent determining which movements this marking permits.
Step 6  change_left     allowed (correct): The broken white lane divider permits changing left when safe.
Step 6  change_right    prohibited (correct): The solid roadway edge and raised curb prohibit moving right
                        across this boundary.
Step 6  go_straight     not_determined (contested, label allowed): The guidance marking's heads are hidden by
                        the Audi, leaving straight-ahead permission undecided.
Step 6  turn_left       not_determined: The guidance marking's hidden heads leave left-turn permission
                        undecided.
Step 6  turn_right      not_determined: The guidance marking's hidden heads leave right-turn permission
                        undecided.
Step 6  u_turn          not_determined: The guidance marking's hidden heads leave U-turn permission undecided.
Step 6  enter_waiting_areanot_applicable: No identifiable left-turn waiting area or adjacent two-way left-turn
                          lane governs this action.
Step 7  Reflect         consistent
Advice                  Keep clear of the right curb and confirm the obscured lane arrow before choosing an
                        intersection movement; a left lane change is permitted only when safe. Obey the
                        intersection signals and stop at the stop line if required, although its location is
                        not readable here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1059, 17.25 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A multilane urban road in China approaches a signal-controlled intersection and zebra
                        crossing. My car is in the rightmost motor-vehicle lane; trucks and other vehicles
                        obscure the leftmost extent of the carriageway. (lanes None, mine None, insufficient)
Step 2  Left            A solid white line separates my lane from another motor-vehicle lane on the left, with
                        no curb between them.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs beside a raised curb and planted separator, with a separate
                        paved path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead.; line:stop_line (full): A transverse white stop line crosses my lane before the
                        zebra crossing.; line:crosswalk (partial): White zebra-crossing stripes extend across
                        my lane ahead of the stop line, partly obscured by the car ahead.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to my left, and the
                        right curb and edge line establish that mine is the rightmost lane; the total count
                        and numerical index cannot be established through the vehicles on the left. | roles:
                        The solid white separator fits a same-direction lane line, and the white line beside
                        the curb fits a roadway edge. | markings: The straight-only arrow is compatible with
                        the lane boundaries and the stop line and crossing ahead; no waiting area is visible.
                        | unseen: No hidden lane count or additional arrow head is inferred; part of the
                        crossing is obscured. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: The raised curb forms a physical roadway edge that an ordinary car
                        must not cross onto the separator or path.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal or
                        traffic control, but does not itself require an unconditional stop.
Step 5  Rule            line:crosswalk: The zebra crossing requires attention to pedestrians and yielding as
                        required, without independently selecting a lane movement.
Step 6  change_left     prohibited (correct): Crossing the solid white lane-dividing line is prohibited.
Step 6  change_right    prohibited (correct): The raised curb prevents lawful movement out of the lane onto
                        the separator or path.
Step 6  go_straight     allowed (correct): The straight-only arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane when the signal and crossing are clear; do not change
                        lanes across the solid left boundary or cross the right curb. For a turn, select an
                        appropriately marked lane before the solid-line approach; stop before the stop line
                        whenever required.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1168, 22.1 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A multilane urban road in China carries traffic ahead between buildings. My car
                        follows a black sedan in the middle of three apparent same-direction lanes; the road
                        farther ahead is partly obscured by traffic. (lanes 3, mine 2, full)
Step 2  Left            A continuous solid white line separates my lane from the traffic lane on the left,
                        with no curb along it.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with diagonal white
                        hatching between it and another solid white line beside the right-hand traffic lane;
                        there is no curb at this boundary.
                        white solid, curb no, other, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane has a same-direction lane to its left and another to its right
                        beyond a painted separator, consistent with being lane 2 of 3. | roles: The solid
                        white left lane line and solid white border of the right-hand hatched separator fit
                        the visible layout. | markings: No guidance marking is readable inside my lane; the
                        diagonal hatching lies outside its right boundary. | unseen: The sedan conceals some
                        pavement ahead, and the lane's eventual end and any movement arrows there cannot be
                        inspected. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line must not be crossed to
                        change lanes.
Step 5  Rule            right_boundary: The solid border of a channelizing separator must not be crossed to
                        enter or traverse the hatched area.
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing to the left.
Step 6  change_right    prohibited (correct): The solid white border of the hatched separator prohibits
                        crossing to the right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The lane-end pavement and any movement arrow there are obscured.
Step 6  turn_right      not_determined: The lane-end pavement and any movement arrow there are obscured.
Step 6  u_turn          not_determined: The lane-end pavement and any movement restriction there are obscured.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within the solid boundaries and do not cross the hatched separator. Confirm
                        the lane-use arrows farther ahead before committing to a turn, and follow any traffic
                        officer's directions.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 948, 20.47 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China approaches a signal-controlled intersection. My car is
                        in the second of four same-direction lanes counted from the left. (lanes 4, mine 2,
                        full)
Step 2  Left            A white broken line with clearly separated long dashes divides my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with clearly visible dashes and gaps divides my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has one head pointing straight
                        ahead.; arrow:straight (full): A smaller, more distant white arrow in the same lane
                        also points straight ahead.
Step 4  Cross-check     position: Lane 2 of 4 has another same-direction lane on each side, consistent with
                        both boundaries being lane lines. | roles: Both white broken boundaries fit ordinary
                        same-direction lane dividers. | markings: The two straight arrows agree with each
                        other and do not conflict with either boundary. | unseen: No distant stop line,
                        crosswalk, or waiting area can be reliably identified; none is asserted. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight at the
                        intersection and excludes left turns, right turns, and U-turns from this lane.
Step 5  Rule            arrow:straight: The repeated straight-only arrow confirms that this lane is for
                        straight-ahead movement at the intersection.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (correct): Both lane-use arrows point straight ahead.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No identifiable waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, subject to the traffic signals. For a turn,
                        move safely into an appropriately marked lane while the broken divider permits it; do
                        not turn directly from this straight-only lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 980, 15.52 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signalized intersection in China. There are four
                        lanes in this direction, and my car is in the second lane from the left. (lanes 4,
                        mine 2, full)
Step 2  Left            A single solid white line separates my lane from another traffic lane on the left;
                        there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another traffic lane on the right;
                        there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in the foreground has one head pointing
                        straight ahead.; arrow:straight (full): A smaller white straight-ahead arrow is
                        repeated farther ahead in my lane.; line:stop_line (partial): A transverse white line
                        is visible at the intersection approach, although its detail is limited by distance.;
                        line:crosswalk (partial): White crosswalk bars extend across the approach ahead; the
                        portion across my lane is distant.
Step 4  Cross-check     position: The second of four lanes has a same-direction lane on each side, consistent
                        with both boundaries being lane lines. | roles: Both white solid boundaries fit same-
                        direction lane dividers on an intersection approach. | markings: The two straight
                        arrows agree with each other and do not conflict with the solid lane boundaries or
                        transverse markings. | unseen: Distant transverse markings have partial evidence; no
                        hidden words, turn-arrow heads, or waiting areas are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes on this approach.
Step 5  Rule            right_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes on this approach.
Step 5  Rule            arrow:straight: The straight-only lane arrow permits proceeding straight and prohibits
                        left turns, right turns, and U-turns from this lane.
Step 5  Rule            arrow:straight: The repeated straight-only arrow confirms that this lane is for
                        straight-ahead travel.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by traffic
                        control; it does not independently require every vehicle to stop.
Step 5  Rule            line:crosswalk: The crosswalk requires attention to and yielding for pedestrians and
                        should not be obstructed.
Step 6  change_left     prohibited (correct): The solid white left lane divider prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane divider prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): Both lane-use arrows explicitly permit straight travel.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, subject to the traffic signal, and do not cross
                        either solid divider. For a turn, select the appropriate lane before the solid-line
                        approach; stop before the stop line when required and keep the crosswalk clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1233, 21.0 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China approaches a signal-controlled intersection. My car is
                        in the second lane from the left; four same-direction approach lanes are visible,
                        although the rightmost lane is partly occupied by a nearby vehicle. (lanes 4, mine 2,
                        full)
Step 2  Left            A single continuous white line separates my lane from another same-direction lane on
                        the left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line separates my lane from another same-direction lane on
                        the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        above the hood; the lower portion of the arrow is hidden, so additional branches
                        cannot be verified.
Step 4  Cross-check     position: The second lane of four has a same-direction lane to its left and two to its
                        right, consistent with lane-line boundaries on both sides. | roles: Both continuous
                        white boundaries fit solid approach lane lines separating same-direction traffic. |
                        markings: The visible forward arrowhead is compatible with this approach lane; its
                        hidden lower portion prevents confirmation that it is straight-only. | unseen: No
                        arrow branches, stop line, crosswalk, or waiting area have been inferred from the
                        obscured portions of my lane. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-separation line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: In China, a solid white lane-separation line prohibits crossing it to
                        change lanes.
Step 5  Rule            arrow:straight: A forward lane-use arrow permits straight travel, but the obscured
                        portion must be visible before other indicated movements can be excluded.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left lane line prohibits crossing
                        into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right lane line prohibits crossing
                        into the adjacent lane.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel.
Step 6  turn_left       not_determined (WRONG, label prohibited): The arrow's lower portion is hidden,
                        preventing confirmation or exclusion of a left-turn branch.
Step 6  turn_right      not_determined (WRONG, label prohibited): The arrow's lower portion is hidden,
                        preventing confirmation or exclusion of a right-turn branch.
Step 6  u_turn          not_determined (WRONG, label prohibited): The arrow's hidden portion prevents complete
                        identification of its permitted movements.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain between the solid white lines and continue straight when the applicable signal
                        permits. Do not assume a turn is permitted from this lane until its complete arrow is
                        visible; the intersection stopping markings are obscured ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1047, 18.73 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China approaches a signalized intersection. My car is in the leftmost
                        of two same-direction lanes, beside a central separation fence. (lanes 2, mine 1,
                        full)
Step 2  Left            A solid yellow line runs beside a raised central separation fence on the left, with
                        opposing traffic beyond.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from another same-direction lane on
                        the right, without a curb between them.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): A large white arrow has one head pointing straight ahead
                        and a second head pointing left.
Step 4  Cross-check     position: The central separator on the left and one same-direction lane on the right
                        agree with lane 1 of 2. | roles: The yellow solid center line and separation fence fit
                        the opposing-direction boundary; the white solid line fits a same-direction lane
                        boundary. | markings: The straight-and-left arrow is consistent with this intersection
                        approach; neither boundary changes the movements indicated by the arrow. | unseen: No
                        hidden marking is asserted. The vehicle ahead and distance obscure parts of the lane
                        near the intersection, so a stop line or other transverse markings cannot be
                        confirmed. | result: consistent
Step 5  Rule            left_boundary: In China, the solid yellow center line prohibits crossing into opposing
                        traffic, and the central fence also prevents crossing.
Step 5  Rule            right_boundary: A solid white lane-dividing line prohibits changing lanes across it.
Step 5  Rule            arrow:straight_left: The combined straight-and-left lane-use arrow permits straight
                        travel or a left turn, but does not authorize a right turn or U-turn.
Step 6  change_left     prohibited (WRONG, label allowed): The solid yellow center line and separation fence
                        prohibit crossing the left boundary.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing the right boundary.
Step 6  go_straight     allowed (correct): The straight head of the combined arrow permits proceeding
                        straight.
Step 6  turn_left       allowed (correct): The left head of the combined arrow permits turning left.
Step 6  turn_right      prohibited (correct): The combined arrow does not include a right-turn movement.
Step 6  u_turn          prohibited (WRONG, label allowed): The combined arrow does not include a U-turn
                        movement.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Use this lane to proceed straight or turn left, following the applicable traffic
                        signal and yielding as required. Do not cross either boundary; if required to stop,
                        stop behind the intersection stop line when it becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 902, 16.52 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China approaches a signal-controlled intersection with a zebra
                        crossing. My car is in the leftmost of two visible same-direction lanes, beside a
                        central separation fence and behind a white SUV. (lanes 2, mine 1, full)
Step 2  Left            A continuous yellow line runs beside a central metal separation fence on the left,
                        with opposing traffic beyond the fence.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A continuous white line separates my lane from another same-direction lane on the
                        right, without a curb between them.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (partial): A transverse white line is partly visible ahead, before the
                        zebra crossing; the SUV hides its middle portion.; line:crosswalk (partial): White
                        zebra-crossing stripes extend across the road ahead, with some stripes in my lane
                        hidden by the SUV.
Step 4  Cross-check     position: The central separator on my left and a same-direction lane on my right agree
                        with my being lane 1 of 2. | roles: The yellow line and central fence fit a center
                        boundary; the solid white line fits an approach lane divider. | markings: The stop
                        line and crossing agree with the intersection approach. No lane-use arrow or waiting
                        area is visibly identifiable in my lane. | unseen: The SUV obscures part of the
                        approach pavement and transverse markings; no hidden arrow or word has been inferred.
                        | result: consistent
Step 5  Rule            left_boundary: In China, the solid yellow center boundary and physical separator
                        prohibit crossing to the left.
Step 5  Rule            right_boundary: A solid white lane divider prohibits changing lanes across it on this
                        visible approach.
Step 5  Rule            line:stop_line: The stop line indicates where to stop when stopping is required by the
                        signal or traffic control, but does not itself require every vehicle to stop.
Step 5  Rule            line:crosswalk: The zebra crossing requires attention to pedestrians and yielding as
                        required, without assigning a lane movement.
Step 6  change_left     prohibited (correct): The solid yellow center boundary and fence prohibit crossing
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white lane divider prohibits crossing
                        right.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight; the transverse lines do not assign movements.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-turn marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-turn marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-turn marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary restrictions apply only to crossing the boundaries, and the stop
                        line and crosswalk do not independently prohibit straight travel or require an
                        unconditional stop.
Advice                  Stay within the current solid boundaries and follow the intersection signals, stopping
                        before the stop line when required and yielding to pedestrians. Turn assignments are
                        not established by the visible markings; check the pavement currently hidden by the
                        SUV before committing to a turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1082, 15.62 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road approaches a bridge underpass, with a bridge-support island separating
                        the right-hand passage from the lanes to its left. My car is in the rightmost of three
                        visible motor-vehicle lanes, beside a roadside strip used by two-wheelers. (lanes 3,
                        mine 3, full)
Step 2  Left            A solid white line borders a tapering painted separation area on the left, leading to
                        a raised bridge-support island; other motor traffic is beyond it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with a long foreground segment and visible gaps farther ahead,
                        separates my lane from a narrow roadside strip occupied by a two-wheeler; the raised
                        sidewalk is beyond that strip.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white arrow in my lane has a bent shaft and a single head
                        pointing right.
Step 4  Cross-check     position: The car occupies the rightmost of three motor lanes. The left edge borders a
                        separation area rather than an adjacent lane directly across a lane divider; the right
                        edge borders the roadside strip. | roles: The solid white separation-area edge and
                        broken white roadside edge are consistent with their edge-line roles. | markings: The
                        right-only arrow is consistent with the separately channelized right-hand passage. The
                        arrows to the left and the painted separation area are outside my lane. | unseen: No
                        additional markings or intersection controls are inferred from the dark area under the
                        bridge. | result: consistent
Step 5  Rule            left_boundary: In China, the solid white edge of a channelized separation area must
                        not be crossed to change lanes.
Step 5  Rule            right_boundary: A broken white roadway edge may be crossed temporarily when safe and
                        necessary, yielding to roadside users, but does not authorize driving along a non-
                        motorized strip.
Step 5  Rule            arrow:right: The right-turn-only lane arrow requires a right turn and excludes
                        straight, left-turn and U-turn movements from this lane.
Step 6  change_left     prohibited: The solid white separation-area edge prohibits crossing left.
Step 6  change_right    allowed: The broken white edge permits temporary crossing when safe, with priority
                        given to users of the roadside strip.
Step 6  go_straight     prohibited (WRONG, label allowed): The right-only arrow does not permit straight
                        travel at the lane's exit.
Step 6  turn_left       prohibited (correct): The right-only arrow excludes a left turn.
Step 6  turn_right      allowed (correct): The right-only arrow permits a right turn.
Step 6  u_turn          prohibited (correct): The right-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Follow this lane for the right turn; do not cross the solid separation boundary to
                        reach the through lanes. Keep clear of the two-wheeler and pedestrian on the right,
                        and do not use the roadside strip as a driving lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1124, 18.02 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China has three lanes in this direction and a central separation
                        fence. My car is in the leftmost lane, approaching a distant signalized intersection.
                        (lanes 3, mine 1, full)
Step 2  Left            A solid white line runs along the left of my lane, with a narrow strip and a physical
                        central separation fence beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow ahead in my lane has a forward-pointing head and
                        no visible turning branch.
Step 4  Cross-check     position: The left roadway edge and the same-direction lane to the right agree with my
                        lane being lane 1 of 3. | roles: The solid white line beside the central fence fits a
                        roadway edge; the broken white line to the right fits a same-direction lane divider. |
                        markings: The straight arrow is consistent with a through lane and does not conflict
                        with either boundary. | unseen: The distant intersection markings cannot be resolved;
                        no stop line, crosswalk, or waiting area is inferred there. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and physical central fence prohibit leaving my
                        lane across its left side.
Step 5  Rule            right_boundary: A broken white same-direction lane divider may be crossed to change
                        lanes when safe without interfering with other traffic.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits turning left, turning right, or making a U-turn from this lane.
Step 6  change_left     prohibited (correct): The solid left roadway edge and central fence prohibit crossing
                        to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight; do not cross the left edge or fence. A
                        rightward lane change is permitted when safe, but use a lane with the appropriate
                        guidance before turning, and obey the intersection signals and any stop line as they
                        become clear.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 892, 14.33 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches a signalized intersection and pedestrian
                        crossing. My car is in the leftmost of three visible approach lanes, beside the
                        central fence. (lanes 3, mine 1, full)
Step 2  Left            A continuous white line runs along the left of my lane, with a narrow strip and a
                        raised central separation fence beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from the adjacent same-direction lane on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.;
                        line:stop_line (full): A transverse white stop line spans my lane immediately before
                        the pedestrian crossing.; line:crosswalk (full): White zebra-crossing stripes extend
                        across my lane beyond the stop line.
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car occupying
                        lane 1 of three same-direction lanes. | roles: The white solid line beside the central
                        barrier is a roadway edge; the white solid line on the right separates same-direction
                        lanes. | markings: The straight-only arrow agrees with the approach layout; the stop
                        line precedes the crosswalk, and no waiting area is visible. | unseen: No hidden arrow
                        heads, words, or waiting-area markings have been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and physical central barrier prohibit leaving
                        this lane to the left.
Step 5  Rule            right_boundary: A solid white lane divider in China prohibits crossing it to change
                        lanes.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns, and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by traffic
                        control; it does not independently require every vehicle to stop.
Step 5  Rule            line:crosswalk: The crosswalk requires attention and yielding to pedestrians but does
                        not select the lane's permitted movements.
Step 6  change_left     prohibited (correct): The solid roadway edge and central barrier prohibit crossing to
                        the left.
Step 6  change_right    prohibited (correct): The solid white lane divider prohibits changing right in the
                        visible stretch.
Step 6  go_straight     allowed (correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane, subject to the traffic signals and yielding to
                        pedestrians. Do not cross either boundary here; if required to stop, remain behind the
                        stop line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1241, 23.18 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches a signal-controlled intersection with a
                        pedestrian crossing. My car is in the leftmost of three same-direction approach lanes,
                        beside a median fence. (lanes 3, mine 1, full)
Step 2  Left            A continuous white line runs along the left of my lane beside a narrow strip
                        containing yellow paint and a raised median fence; opposing traffic is beyond the
                        fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from the adjacent same-direction lane on the
                        right, with no curb between them.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow has a single head pointing straight ahead.;
                        line:stop_line (full): A transverse solid white stop line crosses my lane ahead of the
                        arrow.; line:crosswalk (full): White zebra-crossing stripes cross the road immediately
                        beyond the stop line.
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my position
                        as lane 1 of three same-direction lanes. | roles: The white line beside the median
                        forms the roadway edge; the solid white line on the right separates same-direction
                        approach lanes. | markings: The straight-only arrow is consistent with a through
                        approach lane; the stop line and pedestrian crossing do not contradict it. | unseen:
                        No hidden lane-use marking or waiting area is inferred, and arrows in adjacent lanes
                        are not assigned to my lane. | result: consistent
Step 5  Rule            left_boundary: The median barrier forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits changing lanes
                        across it.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the traffic
                        signal, but does not itself require every vehicle to stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires observing pedestrian priority and
                        keeping the crossing clear.
Step 6  change_left     prohibited (correct): The median barrier physically bounds the roadway and must not be
                        crossed.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing into the adjacent
                        lane.
Step 6  go_straight     allowed (correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel; do not cross either boundary or turn from
                        this lane. Obey the applicable signal, stop before the stop line when required, and
                        yield to pedestrians at the crossing.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1081, 14.79 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban two-way street approaches a side-road junction covered by a yellow keep-clear
                        grid. My car is in the left of two visible lanes in its direction, next to the yellow
                        centre line. (lanes 2, mine 1, full)
Step 2  Left            A single yellow broken line, with visible painted lengths and gaps, separates my lane
                        from oncoming traffic; there is no curb along it.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A white broken divider is visible ahead between my lane and the lane to its right,
                        although its near section is faint; the roadside curb is farther right.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        area:grid (full): A yellow crosshatched box extends across my lane at the side-road
                        junction.
Step 4  Cross-check     position: The centre line on the left places my car in the leftmost lane of its
                        direction, and the white divider has another same-direction lane beyond it on the
                        right. | roles: The broken yellow centre line and broken white lane divider fit their
                        respective roles. | markings: The yellow grid is a keep-clear area and does not
                        prescribe a turning direction; no lane-use arrow or waiting area is visible in my
                        lane. | unseen: The near section of the right divider is faint, so its evidence is
                        partial; its broken pattern is visible farther ahead. | result: consistent
Step 5  Rule            left_boundary: In China, a broken yellow centre line may be crossed for overtaking or
                        another lawful manoeuvre only when it is safe and does not interfere with opposing
                        traffic.
Step 5  Rule            right_boundary: A broken white lane divider permits changing lanes when safe without
                        obstructing other traffic.
Step 5  Rule            area:grid: The yellow grid must be kept clear: do not enter unless the exit is clear
                        enough to avoid stopping within it.
Step 6  change_left     allowed (WRONG, label not_determined): The broken yellow centre line permits crossing
                        when safe, but opposing traffic must not be obstructed.
Step 6  change_right    allowed (WRONG, label not_determined): The visible broken white divider permits a safe
                        lane change.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow restricts continuing straight; the
                        grid requires a clear exit rather than prohibiting this movement.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight only when you can clear the yellow box without stopping in it,
                        watching for the crossing car, scooters and pedestrians. A broken boundary permits
                        crossing only when safe; do not move left into the approaching traffic.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1164, 20.63 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A two-way urban street continues ahead, with two motor-vehicle lanes in this direction
                        and a bicycle area along the right side. My car is in the leftmost motor-vehicle lane;
                        no intersection stop line or lane ending is clearly visible ahead. (lanes 2, mine 1,
                        full)
Step 2  Left            A single solid yellow line runs along the left of my lane, with opposing traffic space
                        beyond and no curb at the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           White long dashes separated by clear gaps divide my lane from the same-direction lane
                        occupied by the gray sedan; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): A white hollow diamond is painted in the center of my lane in the
                        foreground.; symbol:other (partial): A smaller, more distant white hollow diamond is
                        visible farther ahead in my lane.
Step 4  Cross-check     position: The yellow center line on the left and the same-direction lane divider on
                        the right agree with my car occupying lane 1 of 2. | roles: The solid yellow line fits
                        an opposing-direction center line, and the broken white line fits a same-direction
                        lane divider. | markings: The hollow diamonds are pedestrian-crossing advance-warning
                        markings in China, not HOV designations; they do not conflict with either boundary. |
                        unseen: No turn arrows, stop line, waiting area, or readable crossing stripes are
                        identified in my lane; distant details are not inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing into the
                        opposing traffic space.
Step 5  Rule            right_boundary: A broken white lane divider permits changing to the adjacent same-
                        direction lane when safe.
Step 5  Rule            symbol:other: The hollow white diamond warns of an approaching pedestrian crossing and
                        calls for caution, without allocating lane movements.
Step 5  Rule            symbol:other: The repeated hollow diamond reinforces the pedestrian-crossing warning
                        and does not reserve the lane or prescribe a turn.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white divider permits a lane change when
                        safe.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight;
                        the warning diamonds do not govern this movement.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action at the next intersection; the center
                        line separately prohibits crossing it in the visible stretch.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not cross the solid yellow center line. A
                        rightward lane change is permitted by the dashed divider, but wait for a safe gap
                        around the gray sedan and slow down for the pedestrian-crossing warnings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6396, out 1015, 17.36 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road runs beside an elevated roadway toward a signalized intersection. My car
                        is in the rightmost of three motor-vehicle lanes, beside a roadside non-motorized
                        strip. (lanes 3, mine 3, full)
Step 2  Left            A single solid white line separates my lane from the adjacent traffic lane on the
                        left; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single white line is solid in the foreground, with short interruptions farther
                        ahead; beyond it is a roadside strip occupied by bicycles and scooters, with a
                        sidewalk curb farther right.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        arrow:right (full): A white arrow has a forward-running shaft that bends right and
                        ends in a right-pointing head, with no straight-ahead head.
Step 4  Cross-check     position: Two motor-vehicle lanes lie to my left, matching the left lane-line role and
                        my position as lane 3 of 3; the roadside strip to my right is outside the motor-
                        vehicle lanes. | roles: The solid white left line fits a same-direction lane
                        separator; the white right line fits the motor-roadway edge beside the non-motorized
                        strip. | markings: The right-only arrow is compatible with the rightmost motor-vehicle
                        lane; neither boundary supplies an additional permitted intersection movement. |
                        unseen: No stop line, crosswalk or waiting area can be identified in my lane; distant
                        pavement is partly obscured by traffic. The right boundary's distant pattern is not
                        fully clear. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white same-direction lane separator prohibits
                        crossing it to change lanes.
Step 5  Rule            right_boundary: A roadway edge line may be crossed temporarily when necessary and
                        safe, but does not authorize ordinary motor-vehicle travel along the non-motorized
                        strip.
Step 5  Rule            arrow:right: The right-only lane-use arrow permits a right turn and prohibits going
                        straight, turning left or making a U-turn from this lane.
Step 6  change_left     prohibited: The solid white lane separator prohibits crossing into the lane on the
                        left.
Step 6  change_right    allowed: The roadway edge line permits necessary temporary crossing, not continued
                        travel in the roadside non-motorized strip.
Step 6  go_straight     prohibited (correct): The right-only arrow does not permit straight-ahead movement.
Step 6  turn_left       prohibited (correct): The right-only arrow does not permit a left turn.
Step 6  turn_right      allowed (correct): The visible right-pointing arrow permits a right turn.
Step 6  u_turn          prohibited (correct): The right-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Use this lane for a right turn; do not cross the solid left divider to reach a through
                        lane here. Stay out of the roadside non-motorized strip, yield to cyclists and
                        pedestrians when turning, and obey the intersection signals and any stop line that
                        becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1279, 30.58 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signal-controlled intersection in China. My car is
                        in the leftmost lane beside a concrete median, behind a truck that obscures much of
                        the lane ahead. (lanes None, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised concrete median barrier, with opposing
                        traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from an adjacent same-direction lane
                        occupied by a white car.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (partial): Portions of a zebra crossing are visible near the
                        intersection, but the truck hides its passage across most of my lane.
Step 4  Cross-check     position: The median edge on my left establishes that my lane is leftmost; the lane
                        line on my right agrees with another same-direction lane there. Vehicles and the image
                        edge prevent a reliable total lane count. | roles: The white solid median-side edge
                        line and white solid separator between same-direction lanes fit their assigned roles.
                        | markings: The partially visible crossing does not conflict with the boundaries. No
                        lane-use arrow can be read in my lane; arrows in neighboring lanes are not mine. |
                        unseen: The truck conceals possible lane-use markings and the stopping position ahead;
                        no hidden arrow, stop line, or waiting area has been assumed. | result: consistent
Step 5  Rule            left_boundary: The raised median forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            right_boundary: In China, a solid white lane-separation line prohibits crossing it to
                        change lanes.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires attention and yielding to pedestrians
                        but does not itself select any of the seven lane movements.
Step 6  change_left     prohibited (WRONG, label not_determined): The concrete median physically bounds the
                        lane and must not be crossed.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white lane line prohibits crossing
                        into the adjacent lane.
Step 6  go_straight     not_determined (contested, label allowed): The truck hides the approach markings that
                        could determine the permitted movement.
Step 6  turn_left       not_determined: Any lane-use arrow governing a left turn is hidden by the truck.
Step 6  turn_right      not_determined: Any lane-use arrow governing a right turn is hidden by the truck.
Step 6  u_turn          not_determined: Any lane-use or prohibited-movement marking governing a U-turn is
                        hidden by the truck.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: boundary-crossing prohibitions are established, while intersection
                        movements remain undecided because the relevant lane surface is obscured.
Advice                  Remain between the median and the solid white line; do not change lanes across either
                        boundary. Leave enough space behind the truck to see your lane's arrows, crossing and
                        stopping position, and obey the signal while yielding to pedestrians.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 6396, out 1015, 19.0 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China approaches a signal-controlled intersection, with an
                        elevated roadway alongside on the right. My car is in the middle of three same-
                        direction lanes. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead.
Step 4  Cross-check     position: Lane lines on both sides agree with my position as lane 2 of 3. | roles:
                        White broken lines fit separators between same-direction lanes. | markings: The
                        straight-only arrow is consistent with the lane boundaries; no waiting area is
                        visible. | unseen: No hidden stop line or additional markings are inferred; vehicles
                        and distance obscure the final intersection approach. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            arrow:straight: The straight-only guidance arrow requires proceeding straight from
                        this lane at the intersection, rather than turning left, right, or making a U-turn.
Step 6  change_left     allowed (correct): The visible broken white left lane divider permits a safe lane
                        change.
Step 6  change_right    allowed (correct): The visible broken white right lane divider permits a safe lane
                        change.
Step 6  go_straight     allowed (correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane to go straight; for a turn, first select an appropriately marked lane,
                        changing only across broken lines when safe. The signals ahead appear red: stop before
                        the intersection stop line, which is not clearly visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 881, 14.93 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches a signal-controlled intersection, with an
                        elevated structure on the right. My car is in the middle of three same-direction
                        motor-vehicle lanes, behind a taxi. (lanes 3, mine 2, full)
Step 2  Left            A continuous white solid line separates my lane from another same-direction lane on
                        the left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from another same-direction lane on
                        the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible in my lane, with one
                        forward-pointing head and no turning branch.
Step 4  Cross-check     position: Lane 2 of 3 agrees with having a same-direction lane across each boundary. |
                        roles: Both white solid boundaries fit same-direction lane-dividing lines on an
                        intersection approach. | markings: The straight-only arrow agrees with the lane
                        layout; arrows in neighboring lanes do not govern my lane. | unseen: No hidden stop
                        line or markings behind the taxi are inferred; the far end of the lane is partly
                        obscured. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns, and U-turns from this lane.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing into the
                        neighboring lane.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing into the
                        neighboring lane.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits this movement.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight-ahead travel and do not cross either solid boundary
                        to change lanes. The signals ahead are red: stop behind the stop line when it becomes
                        visible, leaving a safe gap behind the taxi.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 877, 10.75 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China approaches a signalized intersection, with queued
                        vehicles obscuring the distant pavement. There are four lanes in this direction, and
                        my car is in the third lane from the left. (lanes 4, mine 3, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside curb and solid white edge line lie
                        beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane three of four has same-direction lanes on both sides, consistent with
                        both boundaries being lane lines. | roles: Both white broken boundaries fit ordinary
                        same-direction lane separators. | markings: No arrows, words, symbols or transverse
                        markings are readable in the exposed part of my lane; there is no visible conflict
                        with the boundaries. | unseen: Vehicles and distance obscure the lane near the
                        intersection, so its eventual movement arrows, stop line and any waiting area cannot
                        be established. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe without interfering with other traffic.
Step 6  change_left     allowed (correct): The visible broken white lane line permits a safe lane change to
                        the left.
Step 6  change_right    allowed (correct): The visible broken white lane line permits a safe lane change to
                        the right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The intersection-end pavement is obscured, so any arrow governing a
                        left turn cannot be read.
Step 6  turn_right      not_determined: The intersection-end pavement is obscured, so any arrow governing a
                        right turn cannot be read.
Step 6  u_turn          not_determined: The intersection-end pavement is obscured, so any marking governing a
                        U-turn cannot be read.
Step 6  enter_waiting_areanot_determined: The obscured intersection approach does not establish whether a
                          left-turn waiting area exists ahead.
Step 7  Reflect         Consistent: broken boundaries permit only the corresponding lane changes, straight
                        travel has no visible marking restriction, and obscured intersection markings leave
                        the other movements undecided.
Advice                  Continue cautiously in this lane; either visible broken boundary may be crossed only
                        when safe. Read the lane arrows as traffic clears before selecting a turning lane,
                        obey the signals, and stop behind the stop line when required.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 966, 15.42 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road in China approaches an intersection in the distance. My car is in
                        the leftmost of four lanes traveling in this direction, beside the painted central
                        separation. (lanes 4, mine 1, full)
Step 2  Left            A continuous white line immediately borders my lane on the left, with two continuous
                        yellow lines and another white line farther left; opposing traffic lies beyond this
                        painted separation, and there is no curb.
                        white solid, curb no, center_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from the
                        next same-direction lane on the right; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white arrow ahead has a shaft bending left and a single left-
                        pointing head.
Step 4  Cross-check     position: The central separation on the left and a same-direction lane line on the
                        right agree with my lane being lane 1 of 4. | roles: The nearest white solid line
                        borders a wider painted central separation containing double solid yellow lines; its
                        center-separation role follows the visible arrangement, not an assumed yellow color.
                        The broken white right boundary fits a same-direction lane divider. | markings: The
                        left-only pavement arrow is consistent with the leftmost approach lane. No waiting
                        area, conflicting arrow, or other readable guidance marking is visible in my lane. |
                        unseen: No hidden stop line or distant pavement marking has been inferred; the far
                        intersection pavement is not fully readable. | result: consistent
Step 5  Rule            left_boundary: The continuous painted central separation must not be crossed to leave
                        my lane on the left.
Step 5  Rule            right_boundary: A broken white same-direction lane divider may be crossed to change
                        lanes when safe and without obstructing traffic.
Step 5  Rule            arrow:left: The left-only lane-use arrow directs my car to turn left rather than
                        proceed straight, turn right, or make an unshown U-turn.
Step 6  change_left     prohibited (correct): The solid central separation prohibits crossing the left
                        boundary.
Step 6  change_right    allowed (correct): The broken white right boundary permits a safe lane change.
Step 6  go_straight     prohibited (contested, label allowed): The left-only arrow does not permit straight
                        travel from this lane.
Step 6  turn_left       allowed: The pavement arrow explicitly permits a left turn.
Step 6  turn_right      prohibited: The left-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The left-only arrow does not show a U-turn movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to turn left; to continue straight, change right across the broken
                        white line when safe, and do not cross the central separation. Follow the intersection
                        signals and any stop line as they become clearly visible; the overhead sign also
                        depicts this as the left-turn lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 981, 18.87 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road in China carries opposing traffic on the left, with an intersection
                        approach ahead. My car is in the leftmost same-direction lane; the outer lanes are
                        partly obscured, so their total cannot be counted confidently. (lanes None, mine 1,
                        partial)
Step 2  Left            A continuous white line borders my lane on the left, immediately alongside two
                        continuous yellow lines and another white line separating opposing traffic; there is
                        no curb.
                        white solid, curb no, center_line, evidence full
Step 2  Right           White broken line segments with clear gaps separate my lane from another same-
                        direction lane on the right; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (partial): A white directional arrow immediately ahead is partly concealed
                        by the hood; its visible head points left.; arrow:left (full): Farther ahead in my
                        lane, a white bent arrow has a left-pointing head.
Step 4  Cross-check     position: The center separation on the left and same-direction lane line on the right
                        support identifying my lane as the leftmost lane; the total lane count remains
                        uncertain. | roles: The continuous white line is part of the visibly continuous
                        center-separation arrangement alongside double yellow lines; the broken white line on
                        the right separates same-direction lanes. | markings: The visible left arrows agree
                        with one another and identify a left-turn lane; no waiting area is visible. | unseen:
                        The hood conceals part of the nearest arrow, and traffic and perspective obscure the
                        distant lane end and outer lane layout; no stop line or additional marking is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: In China, the continuous center-separation markings prohibit crossing
                        into opposing traffic.
Step 5  Rule            right_boundary: A broken white same-direction lane line may be crossed to change lanes
                        when safe.
Step 5  Rule            arrow:left: A left-turn lane-use arrow requires the left-turn movement rather than
                        straight travel, a right turn, or a U-turn.
Step 5  Rule            arrow:left: The repeated left-turn arrow confirms that this lane is designated for
                        turning left.
Step 6  change_left     prohibited (correct): The continuous center-separation boundary prohibits crossing
                        left.
Step 6  change_right    allowed (correct): The broken white lane line permits changing into the adjacent same-
                        direction lane when safe.
Step 6  go_straight     prohibited (correct): The fully visible left-only arrow does not permit straight
                        travel.
Step 6  turn_left       allowed (correct): The left-turn arrow permits turning left.
Step 6  turn_right      prohibited: The left-only arrow excludes a right turn.
Step 6  u_turn          prohibited: The left-only arrow does not show a U-turn movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to turn left, obeying the intersection signals and any stop line
                        as they become visible. For another movement, change right only where the broken line
                        permits and after checking traffic; do not cross the center separation.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:left_u_turn', 'arrow:straight']), actions True, unsafe
                        [], citation None, contradictions []
Tokens                  in 6396, out 1305, 30.53 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road runs alongside an elevated roadway on the left and approaches a
                        signalized intersection. My car is in the middle of five same-direction lanes, with a
                        fenced non-motorized roadway on the far right. (lanes 5, mine 3, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow ahead in my lane has one head pointing straight
                        forward.
Step 4  Cross-check     position: Lane 3 of 5 has same-direction lanes on both sides, consistent with both
                        boundaries being lane lines. | roles: Both white broken boundaries fit ordinary same-
                        direction lane separation. | markings: The straight-ahead arrow is consistent with a
                        through lane between ordinary lane lines; no conflicting word or area marking is
                        visible. | unseen: The distant intersection pavement is not clear enough to identify
                        additional transverse markings; none have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane line may be crossed to change lanes when
                        it is safe and does not obstruct other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane line may be crossed to change lanes when
                        it is safe and does not obstruct other traffic.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight at the
                        intersection and excludes left turns, right turns and U-turns from this lane.
Step 6  change_left     allowed (correct): The white broken left lane line permits crossing when safe.
Step 6  change_right    allowed (correct): The white broken right lane line permits crossing when safe.
Step 6  go_straight     allowed (contested, correct): The straight-ahead arrow permits this movement.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to go straight and obey the intersection signals. For a turn or
                        U-turn, move safely into an appropriately marked lane while the separating lines
                        remain broken; do not make those movements directly from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1106, 18.65 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A multilane urban road in China approaches a signal-controlled intersection beside an
                        elevated roadway. My car is in a middle through lane; glare and perspective make the
                        outer lane arrangement less certain. (lanes 4, mine 3, partial)
Step 2  Left            A single continuous white line separates my lane from another same-direction lane on
                        the left; there is no curb along this line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line separates my lane from another same-direction lane on
                        the right; the roadside fence is farther right, not on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible near the far end of my
                        lane.; line:crosswalk (partial): White pedestrian-crossing stripes extend across my
                        lane ahead; their distant edges are indistinct.
Step 4  Cross-check     position: Same-direction lanes are visible on both sides, consistent with an interior
                        lane; the estimated third-of-four position is less certain because of the outer road
                        layout. | roles: Both white solid boundaries fit approach lane lines separating same-
                        direction traffic. | markings: The straight arrow agrees with a through lane bounded
                        by solid approach lines; the crosswalk does not add a turning permission. | unseen:
                        The outer lane count is uncertain, and a separate stop line cannot be confidently
                        distinguished at this distance; neither is treated as fully observed. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            arrow:straight: The straight-only lane arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires appropriate yielding to pedestrians
                        but does not itself grant or prohibit any of the seven lane movements.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (contested, correct): The straight-ahead arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane when signals and pedestrian conditions permit; do not
                        cross either solid boundary. For a turn, select an appropriately marked lane earlier
                        rather than changing lanes here, and stop before the intersection crossing when
                        required by the signal.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:crosswalk'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1354, 29.14 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad divided urban road in China approaches a signalized intersection. My car is in
                        the third of five lanes traveling in this direction. (lanes 5, mine 3, full)
Step 2  Left            A single white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow ahead in my lane has a single head pointing
                        straight forward.; line:crosswalk (partial): White pedestrian-crossing stripes extend
                        across the road ahead, including my lane, although their distant edges are indistinct.
Step 4  Cross-check     position: Lane three of five has same-direction lanes on both sides, consistent with
                        both boundaries being lane lines. | roles: Both white broken boundaries fit ordinary
                        same-direction lane separators. | markings: The straight arrow agrees with a through
                        lane between ordinary lane boundaries; the crosswalk does not prescribe a turning
                        movement. | unseen: No words, waiting areas, or additional arrow heads are
                        identifiable in my lane; a separate stop line cannot be confidently resolved at this
                        distance. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to the adjacent
                        same-direction lane when safe and without obstructing traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to the adjacent
                        same-direction lane when safe and without obstructing traffic.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight from this
                        lane and excludes left turns, right turns, and U-turns from it.
Step 5  Rule            line:crosswalk: The crosswalk requires attention and yielding to pedestrians as
                        required, but does not itself select any of the seven lane maneuvers.
Step 6  change_left     allowed (correct): The broken white left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): The straight arrow explicitly permits this movement.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight, subject to the traffic signals and yielding
                        at the crosswalk. For another movement, change safely across a broken divider into an
                        appropriately marked lane before the intersection; obey the signs and stop before the
                        intersection stop line when required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:crosswalk'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1297, 26.04 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban divided road in China approaches a signal-controlled intersection. My
                        car is in a straight-ahead lane, with two same-direction lanes visible on each side.
                        (lanes 5, mine 3, full)
Step 2  Left            A continuous white line with repeated short white diagonal teeth on its far side
                        separates my lane from another same-direction lane; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from another same-direction lane on the
                        right, with no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in the foreground has a single head
                        pointing straight ahead.; arrow:straight (full): A second, smaller white straight-
                        ahead arrow is visible farther along my lane.; line:stop_line (partial): A transverse
                        white stop line lies across my lane immediately before the pedestrian crossing.;
                        line:crosswalk (full): White zebra-crossing stripes extend across my lane at the
                        intersection.
Step 4  Cross-check     position: The third of five lanes has same-direction lanes on both sides, consistent
                        with both boundaries being lane lines. | roles: Both white solid boundaries fit same-
                        direction lane separators on an intersection approach; the diagonal teeth on the left
                        do not make its continuous line broken. | markings: Both arrows indicate straight
                        ahead and agree with each other; the stop line and crossing are compatible with this
                        intersection approach. | unseen: The distant stop line is only partially resolved; no
                        hidden words, turn arrows, or waiting areas have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, the solid white lane separator prohibits crossing it to
                        change lanes on this approach.
Step 5  Rule            right_boundary: In China, the solid white lane separator prohibits crossing it to
                        change lanes on this approach.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits turning left, turning right, or making a U-turn from this lane.
Step 5  Rule            arrow:straight: The repeated straight-only arrow confirms that this lane is for
                        straight-ahead movement only.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the traffic
                        signal or traffic control, but does not independently require every vehicle to stop.
Step 5  Rule            line:crosswalk: The crossing requires attention and yielding to pedestrians as
                        applicable, without changing the lane's permitted direction.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing to the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing to the
                        adjacent lane.
Step 6  go_straight     allowed (correct): Both lane-use arrows explicitly permit straight-ahead travel.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight-ahead travel and do not cross either solid boundary
                        to change lanes. Obey the intersection signals, stop before the stop line when
                        required, and yield to pedestrians at the crossing.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1401, 27.08 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches a distant signal-controlled intersection. My
                        car is in the middle of three same-direction motor-vehicle lanes. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; the solid white line farther right is not my lane
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my lane being lane 2 of 3. | roles: Both
                        white broken lines fit separators between same-direction traffic lanes. | markings: No
                        guidance marking is readable in my lane, so there is no visible marking conflict. |
                        unseen: The vehicle ahead and distance obscure portions of the approach; no arrow,
                        stop line, or other distant marking is inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without obstructing traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without obstructing traffic.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe change into the
                        adjacent left lane.
Step 6  change_right    allowed (correct): The broken white lane separator permits a safe change into the
                        adjacent right lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: lane-change permissions follow the broken separators, while absent visible
                        turn guidance is not treated as permission to turn.
Advice                  Continue in this lane, or cross either broken separator only after checking traffic
                        and blind spots. Read the lane arrows and signals as the intersection becomes clearer;
                        turn-lane assignments and a stopping position cannot yet be identified.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 822, 17.96 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues straight, with a median fence on the left and
                        a side-road opening on the right. My car is in the middle of three same-direction
                        lanes; no lane end or marked intersection stop line is clearly visible ahead. (lanes
                        3, mine 2, full)
Step 2  Left            A white dashed line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white dashed line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane lies on each side, consistent with my lane being
                        second of three. | roles: Both white dashed boundaries fit ordinary same-direction
                        lane-divider roles. | markings: No arrows, words, symbols, transverse lines or waiting
                        areas are discernible in my visible lane. | unseen: No markings are inferred beneath
                        vehicles or beyond the clearly visible road surface; the next intersection layout is
                        not established. | result: consistent
Step 5  Rule            left_boundary: In China, a white dashed same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white dashed same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (WRONG, label prohibited): The white dashed left lane divider permits a safe
                        lane change.
Step 6  change_right    allowed (WRONG, label not_determined): The white dashed right lane divider permits a
                        safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or lane-ending marking
                        restricts continuing straight.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either dashed divider may be crossed only when safe.
                        Watch for cyclists and scooters on the right, and use the markings and controls at the
                        next intersection to select a turning lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6396, out 809, 10.77 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway with three lanes in this direction continues toward an overpass.
                        My car is in the rightmost lane, with a shoulder on the right and an exit advertised
                        700 metres ahead. (lanes 3, mine 3, full)
Step 2  Left            A white broken lane divider, with a visible dash and gap farther ahead and short
                        block-shaped markings alongside it nearby, separates my lane from another same-
                        direction lane.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with short block-shaped markings
                        alongside it; beyond it are a paved shoulder and a concrete roadside barrier.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Short white block-shaped markings repeat along the inside edges
                        of the lane near the foreground, forming longitudinal visual speed-reduction markings;
                        no directional arrow or word is visible.
Step 4  Cross-check     position: The third of three lanes has another same-direction lane on its left and a
                        roadway edge with a shoulder on its right. | roles: The white broken divider fits a
                        same-direction lane line, and the solid white line beside the shoulder fits an edge
                        line. | markings: The longitudinal speed-reduction blocks are compatible with both
                        boundaries and do not indicate a turn or merge. | unseen: No hidden arrow,
                        intersection marking, or exit-lane assignment has been inferred; the barrier is beyond
                        the shoulder rather than directly bounding my lane. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider may be crossed to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge line must not be crossed for ordinary
                        driving onto the expressway shoulder.
Step 5  Rule            symbol:other: Longitudinal visual speed-reduction markings prompt drivers to reduce
                        speed but do not assign permitted turning movements or independently prohibit lane
                        changes.
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        change into the adjacent ordinary lane.
Step 6  change_right    prohibited (correct): The solid roadway edge line prohibits an ordinary move onto the
                        shoulder.
Step 6  go_straight     allowed (contested, correct): No directional marking restricts continuing straight
                        along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, reduce speed appropriately, and maintain a safe gap to the
                        traffic ahead; a left lane change is permitted only when safe. Do not use the
                        shoulder, and follow subsequent exit signs and lane markings if taking the exit
                        advertised 700 metres ahead.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1020, 21.07 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight, with no intersection or lane ending
                        visible. My car is in the third of four same-direction lanes, behind a white car.
                        (lanes 4, mine 3, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; the solid roadway edge and curb lie beyond that
                        adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and ego position three agree with two lanes to the left and one
                        to the right; both immediate boundaries are lane lines. | roles: Both white broken
                        boundaries fit their roles as same-direction lane separators. | markings: No guidance
                        markings are visible in my lane, so none conflict with the boundaries. | unseen: No
                        hidden marking or intersection layout is inferred; vehicles obscure some pavement
                        farther ahead. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to the adjacent
                        same-direction lane when safe and without obstructing traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to the adjacent
                        same-direction lane when safe and without obstructing traffic.
Step 6  change_left     allowed (correct): The broken white left lane divider permits a safe lane change.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white right lane divider permits a safe
                        lane change.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; changing one lane left or right is permitted across
                        the broken lines when safe. Keep a safe following distance and use subsequent junction
                        markings to choose a lane for any turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6396, out 857, 15.82 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with no nearby intersection or lane
                        ending visible. My car is in the rightmost of three same-direction lanes, marked as a
                        bus lane. (lanes 3, mine 3, full)
Step 2  Left            A yellow broken line, with several long dashes and gaps visible, separates my lane
                        from another same-direction traffic lane; there is no curb on this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 2  Right           Yellow broken segments run just inside a continuous white line, beyond which there is
                        a narrow paved roadside strip and then a raised curb.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (partial): Large white numerals resembling a time restriction are partly
                        hidden by the hood; the complete inscription cannot be read.; text:bus (full): White
                        Chinese characters 公交专用 are painted longitudinally in my lane.
Step 4  Cross-check     position: Two traffic lanes lie to my left and the roadway edge lies to my right,
                        consistent with lane 3 of 3; the left boundary separates my reserved lane from general
                        traffic. | roles: The yellow broken boundary fits a bus-lane separator, not an
                        opposing-traffic center line; the continuous white line on the right follows the
                        roadway edge, with yellow bus-lane segments immediately inside it. | markings: The
                        bus-only wording agrees with the yellow broken lane delineation; no directional arrow,
                        stop marking, or waiting area is visible in my lane. | unseen: The partly obscured
                        numeric inscription is not assigned a definite time interval, and no unseen
                        intersection markings are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, the broken boundary of my bus lane permits leaving it for the
                        adjacent general-traffic lane when safe.
Step 5  Rule            right_boundary: The continuous white roadway-edge line restricts crossing out of the
                        traffic lane into the roadside strip.
Step 5  Rule            text:other: The incomplete numeric inscription cannot establish the bus-lane operating
                        hours or independently authorize any movement.
Step 5  Rule            text:bus: The bus-only inscription identifies a reserved lane that an ordinary car
                        should not use while its restriction applies, but it does not itself prescribe turning
                        directions or prohibit leaving across a broken boundary.
Step 6  change_left     allowed (contested, correct): The broken yellow bus-lane boundary permits leaving my
                        reserved lane for the general-traffic lane when safe.
Step 6  change_right    prohibited (contested, correct): The continuous white roadway-edge line restricts
                        crossing into the roadside strip.
Step 6  go_straight     allowed (contested, label prohibited): No directional arrow or lane-ending marking
                        restricts continuing straight; this does not authorize continued ordinary-car use of
                        the bus lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  As an ordinary car, move left into a general-traffic lane across the broken boundary
                        when safe rather than continue in the bus lane unless its operating restrictions
                        clearly permit it. Do not cross the solid right edge line; the painted time
                        restriction is partly obscured.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1269, 21.6 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane highway in China continues ahead, with a median barrier on the
                        left and a shoulder and guardrail on the right. My car is in the third of four same-
                        direction lanes; no intersection or lane ending is visible. (lanes 4, mine 3, full)
Step 2  Left            A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A pale yellow broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; the solid white outer edge and guardrail are
                        farther right.
                        yellow dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and ego position three agree with having a same-direction lane
                        immediately on each side. | roles: The white broken left boundary fits an ordinary
                        lane divider. The right boundary appears yellow, which is unusual for a same-direction
                        divider in China, but its position within this divided carriageway supports the lane-
                        line role rather than a center-line role. | markings: No arrows, words, symbols,
                        transverse lines or marked waiting areas are visible in my lane. | unseen: No markings
                        or intersection layout have been inferred beyond the visible road; the right line's
                        observed yellow tint has not been replaced with an assumed white color. | result:
                        consistent
Step 5  Rule            left_boundary: A broken lane divider in China permits crossing to change lanes when
                        safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The visible broken divider permits crossing into the adjacent same-
                        direction lane when safe; its yellow appearance alone does not make it a solid-line
                        crossing prohibition.
Step 6  change_left     allowed (correct): The white broken lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken right divider permits a safe lane change into the
                        adjacent same-direction lane.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary rules govern only lane changes, and the absence of turn guidance
                        does not establish permission to turn or make a U-turn.
Advice                  Continue in this lane, or change one lane left or right across the broken divider only
                        after checking traffic and blind spots. No turning location or stopping requirement is
                        shown.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 973, 19.84 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway in China continues ahead on a gentle bend, with no visible
                        intersection, ramp or lane ending. My car is in the third of four lanes in this
                        direction. (lanes 4, mine 3, full)
Step 2  Left            A single white broken line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane on the right; the roadside guardrail is beyond
                        that lane, not at my boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes with my car in lane 3 agrees with two lanes to my left, one to my
                        right, and lane-line boundaries on both sides. | roles: Both white broken lines fit
                        their roles as separators of same-direction traffic lanes. | markings: No arrows,
                        words, symbols, transverse lines or marked waiting areas are visible in my lane. |
                        unseen: No unseen intersection or distant lane-end markings have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane line permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane line permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken lane line permits a safe lane change to the left.
Step 6  change_right    allowed (correct): The white broken lane line permits a safe lane change to the right.
Step 6  go_straight     allowed (contested, correct): No arrow or lane-ending marking restricts continuing
                        along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane; either adjacent lane can be entered across the broken white
                        line after checking mirrors, blind spots and safe gaps. No turning location or
                        stopping requirement is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 822, 12.91 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane highway continues ahead on a gentle left bend, with no
                        intersection, ramp or lane ending visible. My car is in the middle of three lanes in
                        this direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with distinct long dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with distinct long dashes and gaps, separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane on each side agrees with three lanes and my lane being
                        second from the left. | roles: Both white broken boundaries fit ordinary same-
                        direction lane separators. | markings: No arrows, words, symbols, marked areas or
                        transverse lines are visible in my lane. | unseen: No features beyond the visible road
                        stretch or hidden beneath vehicles are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The left broken white lane separator permits a safe lane change.
Step 6  change_right    allowed (correct): The right broken white lane separator permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along my lane, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane along the bend; either adjacent lane may be entered across
                        the broken white line after checking traffic and signaling. No turn guidance or
                        stopping point is visible ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 725, 9.49 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a fork, with my car in the right-hand lane following a
                        branch that curves right. Two same-direction lanes are visible near the bottom; a
                        painted separation area develops to my left ahead. (lanes 2, mine 2, full)
Step 2  Left            A continuous white line, appearing cream-colored in the lighting, borders my lane on
                        the left; another same-direction lane lies beyond it near the car, and diagonal
                        separation hatching develops beyond it ahead.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line curves right along my lane, with a paved shoulder and then a
                        concrete barrier beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my car occupying lane 2
                        of 2. | roles: The solid white left line separates same-direction paths, while the
                        solid white right line separates the travel lane from the shoulder. | markings: No
                        guidance marking is visible inside my lane; the diagonal hatching is outside its left
                        boundary. | unseen: No hidden arrow or marking has been inferred beneath the vehicles
                        ahead. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: The solid white roadway edge line prohibits ordinary driving across it
                        onto the shoulder.
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing to the left.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits crossing onto the shoulder
                        in ordinary driving.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow restricts continuing along my lane as
                        it curves right.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action; the road's rightward curve is not a
                        right-turn arrow.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid white boundaries and follow your branch around the rightward
                        curve; do not cross the hatched separation area or enter the shoulder. Check the
                        overhead destination signs before continuing, and leave a safe gap behind the vehicle
                        ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 813, 17.03 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road in China continues straight ahead, with guardrails on both
                        sides and no visible intersection, ramp or lane ending. My car is in the middle of
                        three lanes traveling in this direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying lane 2 of 3. | roles:
                        Both white broken boundaries fit same-direction lane-divider roles. | markings: No
                        arrows, words, symbols, transverse lines or waiting areas are visible in my lane;
                        there is no conflict with the boundaries. | unseen: No hidden markings or intersection
                        layout have been inferred; the distant roadway is not fully readable. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing into the
                        adjacent same-direction lane when safe and without obstructing traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing into the
                        adjacent same-direction lane when safe and without obstructing traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along this
                        continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in the middle lane, or change one lane left or right only after
                        checking mirrors, blind spots and safe gaps. No turning or stopping location is
                        indicated by the visible lane markings.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 738, 12.98 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway in China continues ahead toward an overpass, with traffic queued
                        in the distance. My car is in the rightmost of three lanes; a paved shoulder lies to
                        the right. (lanes 3, mine 3, full)
Step 2  Left            A single white broken line, with visible long dashes and gaps, separates my lane from
                        another traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line separates my lane from a paved shoulder, with a
                        guardrail beyond the shoulder rather than at the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 3 agree with a same-direction lane line on the left
                        and a roadway edge line on the right. | roles: The broken white divider fits a same-
                        direction lane boundary; the solid white line beside the shoulder fits a roadway edge.
                        | markings: No discernible guidance markings in my lane conflict with either boundary.
                        | unseen: The vehicle ahead obscures some pavement, and no intersection or lane ending
                        is visible; no hidden markings are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: The solid white expressway edge line separates the traffic lane from
                        the shoulder, which an ordinary car must not enter for normal driving or overtaking.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge bounds the expressway
                        shoulder, which is not available for an ordinary lane change.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken divider only after checking
                        for a safe gap. Do not use the right shoulder; reduce speed and leave ample following
                        distance as traffic slows ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 822, 14.78 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A single-lane elevated ramp curves left between concrete barriers, with vehicles
                        ahead. My car is in the sole travel lane; a paved shoulder lies beyond its right edge.
                        (lanes 1, mine 1, full)
Step 2  Left            A continuous white edge line follows the left curve beside a concrete barrier, with
                        repeated short white rectangular markings on its lane side.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line borders the lane on the right, with repeated white rectangular
                        markings on its lane side and a paved shoulder extending to a concrete barrier beyond
                        it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Repeated short white rectangular blocks run longitudinally just
                        inside both lane edges along the curve, forming visual narrowing strips.
Step 4  Cross-check     position: One travel lane agrees with edge lines on both sides; the pavement to the
                        right is outside the solid edge line, not another marked travel lane. | roles: The
                        continuous white lines fit roadway-edge markings; the left barrier also physically
                        bounds the lane. | markings: The paired longitudinal deceleration markings agree with
                        the narrow curved ramp and do not indicate another lane or a turning movement. |
                        unseen: No intersection, lane-use arrow, stop marking or waiting area is visible; none
                        is inferred beyond the curve. | result: consistent
Step 5  Rule            left_boundary: The solid white roadway edge and concrete barrier prohibit leaving the
                        lane to the left in ordinary driving.
Step 5  Rule            right_boundary: The solid white roadway edge prohibits crossing into the shoulder in
                        ordinary driving.
Step 5  Rule            symbol:other: These longitudinal deceleration markings warn drivers to reduce speed
                        but do not assign or prohibit intersection movements.
Step 6  change_left     prohibited (WRONG, label allowed): The solid left edge and concrete barrier prohibit
                        leaving the lane to the left.
Step 6  change_right    prohibited (correct): The solid right edge prohibits moving onto the shoulder in
                        ordinary driving.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along the ramp; following
                        its leftward curve is continuing in the lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the solid white edges and follow the ramp around the left curve; do not
                        use the right shoulder as another lane. Reduce speed for the curve and deceleration
                        markings, and maintain a safe gap from the vehicles ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 932, 19.93 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road in China curves gently right, with traffic ahead and
                        guardrails on both sides. My car is in the rightmost of three same-direction lanes; no
                        intersection or lane ending is visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white lane line with visible dashes and gaps separates my lane from another
                        same-direction lane; additional short white rectangular markings run alongside it, and
                        there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane, with repeated white rectangular markings
                        immediately inside it and a paved shoulder and guardrail beyond.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Repeated short white rectangular blocks run longitudinally along
                        both sides inside my lane, forming visual lane-narrowing speed-reduction markings.
Step 4  Cross-check     position: Three lanes and position 3 agree with a same-direction lane line on the left
                        and a roadway edge line on the right. | roles: The broken white left line fits a same-
                        direction lane divider; the solid white right line fits the boundary to the shoulder.
                        | markings: The repeated speed-reduction blocks supplement the boundaries and do not
                        indicate a turn or merge. | unseen: No arrows, turn prohibitions, stop markings, or
                        waiting areas are identified; the distant road is partly obscured by traffic. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without interfering with traffic.
Step 5  Rule            right_boundary: The solid white roadway edge line must not ordinarily be crossed to
                        drive onto the shoulder.
Step 5  Rule            symbol:other: Longitudinal speed-reduction markings warn drivers to reduce speed and
                        do not independently authorize or prohibit the seven assessed maneuvers.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line prohibits an ordinary
                        move onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane and reduce speed for the marked section and traffic ahead.
                        Change left only when safe; do not cross the solid right edge line onto the shoulder.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 928, 14.38 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway in China continues ahead, with guardrails and an exit sign in the
                        distance; no intersection or lane ending is visible. My car is in the middle of three
                        lanes travelling in this direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with clearly visible dashes and gaps, separates my lane from
                        another traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with clearly visible dashes and gaps, separates my lane from
                        another traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One same-direction lane on each side agrees with three lanes total and my
                        lane being second from the left. | roles: Both white broken boundaries fit same-
                        direction lane dividers. | markings: No visible in-lane guidance markings conflict
                        with the boundaries or lane position. | unseen: No hidden markings or unseen
                        intersection layout have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No in-lane arrow restricts continuing straight, and the
                        lane visibly continues.
Step 6  turn_left       not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken divider may be crossed after checking
                        traffic and signalling. If taking an upcoming exit, follow the exit signs and move
                        right safely; no stopping point is marked in the visible lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 762, 9.56 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A three-lane divided highway with roadside noise barriers continues ahead on a gentle
                        curve; no intersection or lane ending is visible. My car is in the middle lane. (lanes
                        3, mine 2, full)
Step 2  Left            A single white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane 2 agree with a same-direction lane across each
                        boundary. | roles: Both white broken boundaries fit ordinary same-direction lane-
                        divider roles. | markings: No visible in-lane guidance markings contradict the
                        boundaries or continued travel. | unseen: No unseen lane-end markings or distant
                        restrictions have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (WRONG, label not_determined): The white broken right lane divider permits a
                        safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along this lane, and no
                        lane ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either adjacent lane may be entered across its broken
                        white divider after checking mirrors, blind spots and traffic gaps. No turn facility
                        or stopping point is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 714, 11.0 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane highway in China curves gently left ahead, with no visible
                        intersection or lane ending. My car is in the rightmost of three lanes in this
                        direction. (lanes 3, mine 3, full)
Step 2  Left            A white broken line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved shoulder and
                        then a guardrail beyond it; no curb forms the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 3 agree with a lane divider on the left and a
                        roadway edge line on the right. | roles: The broken white lane divider and solid white
                        edge line fit their observed roles. | markings: No arrows, words, symbols, transverse
                        lines or waiting areas are visible in my lane. | unseen: No markings or intersection
                        layout beyond the visible highway have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits changing
                        lanes across it when safe.
Step 5  Rule            right_boundary: The solid white highway edge line prohibits ordinary driving across it
                        onto the shoulder.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits an ordinary move onto the
                        shoulder.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along the visible lane,
                        which does not visibly end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane through the gentle left curve, or change left across the broken
                        line after checking traffic. Do not cross the solid right edge line onto the shoulder
                        during normal driving.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 783, 10.39 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A barrier-lined urban roadway curves left ahead, with no intersection or lane ending
                        visible. My car is in the left of two same-direction lanes. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line follows the left side of my lane beside a raised concrete
                        barrier and guardrail; repeated white rectangular blocks lie just inside the line.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from another paved lane on the right, with
                        repeated white rectangular blocks on my side of the line and a concrete barrier beyond
                        the adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Repeated white rectangular blocks run along both sides inside my
                        lane, forming longitudinal speed-reduction markings.; symbol:other (full): A group of
                        closely spaced pale transverse strips crosses my lane ahead, forming transverse speed-
                        reduction markings.
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 1 agree with a left roadway edge
                        and a right lane separator. | roles: The solid white left edge line and solid white
                        right lane line fit their respective roles; the rectangular blocks are supplementary
                        markings rather than gaps in either boundary. | markings: The longitudinal blocks and
                        transverse strips consistently warn of speed reduction on the curve; no directional
                        arrow or waiting area is visible. | unseen: No intersection movements or markings
                        beyond the visible curve have been inferred. | result: consistent
Step 5  Rule            left_boundary: The roadway edge and physical barrier prohibit moving out of the lane
                        to the left.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            symbol:other: Longitudinal speed-reduction markings call for reduced speed and caution
                        but do not assign permitted turning movements.
Step 5  Rule            symbol:other: Transverse speed-reduction markings warn drivers to slow down but do not
                        themselves require a full stop or restrict direction.
Step 6  change_left     prohibited (WRONG, label allowed): The left roadway edge is bounded by a physical
                        barrier.
Step 6  change_right    prohibited (correct): The solid white lane-dividing line prohibits crossing into the
                        right lane.
Step 6  go_straight     allowed (contested, correct): No directional marking restricts continuing along my
                        lane around the curve.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Stay in your lane and follow the left curve without crossing either boundary. Slow for
                        the speed-reduction markings and observe the posted 30 km/h limit.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1060, 15.05 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow, single-lane carriageway or ramp in China continues ahead between guardrails,
                        with a bus directly ahead. No intersection, merge or lane ending is visible. (lanes 1,
                        mine 1, full)
Step 2  Left            A continuous white solid line borders the lane on the left, with a narrow paved
                        margin, raised curb and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white solid line borders the lane on the right, with a paved shoulder,
                        raised curb and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane, indexed 1, agrees with roadway edge lines on both sides and no
                        adjacent traffic lanes. | roles: Both white solid lines fit roadway edge-line roles
                        rather than lane-divider or center-line roles. | markings: No guidance markings are
                        visible within the lane, so none contradict the boundaries. | unseen: The bus hides
                        part of the roadway ahead; no markings or lane-end configuration are inferred beneath
                        or beyond it. | result: consistent
Step 5  Rule            left_boundary: In China, a solid roadway edge line restricts ordinary driving across
                        it; the roadside curb and guardrail also prevent a normal leftward exit.
Step 5  Rule            right_boundary: In China, a solid roadway edge line restricts ordinary driving onto
                        the shoulder; the shoulder is not an additional traffic lane.
Step 6  change_left     prohibited (correct): The solid left edge line prohibits an ordinary crossing out of
                        the carriageway.
Step 6  change_right    prohibited (correct): The solid right edge line prohibits an ordinary crossing onto
                        the shoulder.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along this lane,
                        and no lane ending is visible.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the edge lines and keep a safe following distance behind the bus; do
                        not use either roadside margin to overtake. The bus obscures the road ahead, so
                        reassess guidance markings as they become visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 827, 12.26 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An elevated divided expressway continues straight ahead, with four general-traffic
                        lanes in this direction and an emergency shoulder on the right. My car is in the
                        second lane from the left; no intersection, ramp or lane ending is visible. (lanes 4,
                        mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        general-traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        general-traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The second of four general-traffic lanes has one lane to its left and two to
                        its right, consistent with lane-line boundaries on both sides. | roles: Both
                        boundaries are white broken lines, consistent with separators between lanes traveling
                        in the same direction. | markings: No arrows, words, symbols, transverse lines or
                        marked waiting areas are visible in my lane; there is no conflict with the boundaries.
                        | unseen: No unseen pavement marking is inferred; the arrows on the overhead signs are
                        not pavement arrows. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing into the
                        adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing into the
                        adjacent same-direction lane when safe.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe change into the
                        adjacent general-traffic lane.
Step 6  change_right    allowed (correct): The broken white lane separator permits a safe change into the
                        adjacent general-traffic lane.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight, and the
                        lane visibly continues.
Step 6  turn_left       not_applicable: No marking governs this action; no intersection is visible.
Step 6  turn_right      not_applicable: No marking governs this action; no intersection is visible.
Step 6  u_turn          not_applicable: No pavement arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; changing one lane left or right is permitted by the
                        markings when safe. Follow the overhead lane-specific speed signs and keep out of the
                        emergency shoulder during ordinary driving.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 862, 14.9 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban roadway in China continues toward an overpass; no intersection or lane ending
                        is clearly visible. My car is in the left of two same-direction lanes, beside a raised
                        planted divider, with vehicles stopped or parked in the right lane. (lanes 2, mine 1,
                        full)
Step 2  Left            A faded pale-yellow solid line follows a raised curb on the left, with a planted
                        divider beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A worn white solid line separates my lane from the lane containing the vans on the
                        right; no curb lies along this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and edge line agree with my lane being leftmost; the right
                        lane line separates it from the second same-direction lane. | roles: The solid line
                        beside the divider functions as an edge line, while the white solid line between the
                        two lanes functions as a lane line. | markings: No arrows, words, symbols, marked
                        areas or transverse lines are visible in my lane. | unseen: No intersection layout or
                        markings beyond the visible road stretch have been inferred. | result: consistent
Step 5  Rule            left_boundary: The raised divider forms a physical roadway edge and must not be
                        crossed or mounted to leave the lane.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 6  change_left     prohibited (WRONG, label not_determined): The raised divider prohibits leaving the
                        lane across its left boundary.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white lane line prohibits changing
                        into the right lane across the visible stretch.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the current lane without crossing the right solid line or mounting the
                        left divider. Turn-lane guidance and any required stopping point are not visible;
                        reassess as you approach the road ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 839, 15.18 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China has a narrow carriageway separated from the parallel roadway on
                        the left by raised planters. My car follows a black car in the single motor-vehicle
                        lane here, with scooters travelling in the strip to the right; the lane's eventual end
                        is not clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A raised concrete planter edge runs along the left, with a narrow pale solid painted
                        line at its base and a separate parallel roadway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A faded but continuous white solid line separates my lane from the roadside strip
                        occupied by scooters; the raised sidewalk curb is farther right, not at this line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane between the planter edge and the roadside-strip
                        boundary agrees with my lane being the leftmost and rightmost lane of this separated
                        carriageway; lanes beyond the planter are not counted as adjacent lanes. | roles: The
                        white solid lines fit roadway-edge roles, and the raised planter physically bounds the
                        left side. | markings: No readable arrows, words, symbols, transverse lines or waiting
                        areas appear in the visible part of my lane. | unseen: No movement arrows or markings
                        hidden by the leading vehicle or beyond the visible stretch have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The raised planter is a physical roadway edge and must not be crossed
                        to leave this lane.
Step 5  Rule            right_boundary: The solid white boundary separates the motor-vehicle lane from the
                        roadside non-motorized strip and prohibits an ordinary car from crossing into that
                        strip here.
Step 6  change_left     prohibited (correct): The raised planter edge prohibits crossing to the left.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white boundary to the non-
                        motorized roadside strip prohibits moving into it.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight
                        along this lane.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane without crossing the planter edge or the solid white
                        boundary beside the scooters. Keep a safe following distance and reassess turn
                        permissions when the junction and its lane markings become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 868, 14.71 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead beneath a pedestrian footbridge, with no
                        intersection or lane ending visible. My car is in the leftmost of two same-direction
                        motor-vehicle lanes, beside a planted raised median. (lanes 2, mine 1, full)
Step 2  Left            A continuous yellow line runs alongside the raised curb of a planted median on the
                        left.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction motor-vehicle lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and an adjacent lane on the right agree with my
                        lane being lane 1 of 2. | roles: The solid yellow marking beside the median curb fits
                        a roadway edge; the broken white marking separates same-direction lanes. | markings:
                        No arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No markings are inferred beyond the visible road; the next intersection is not
                        visible. | result: consistent
Step 5  Rule            left_boundary: The solid median-edge marking and raised curb prohibit leaving my lane
                        across the left boundary.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits changing into the
                        adjacent same-direction lane when safe.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid median edge and raised curb
                        prohibit crossing the left boundary.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        change into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change right across the broken white line only after checking
                        nearby traffic, including the two-wheelers. Do not cross the median boundary; choose
                        any turning lane according to markings when an intersection comes into view.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 777, 15.16 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues straight beneath a 2.5 m height-restriction gantry; no
                        intersection or lane ending is clearly visible. My car is in the single motor-vehicle
                        lane, with a raised divider on the left and a narrow roadside strip used by a scooter
                        on the right. (lanes 1, mine 1, full)
Step 2  Left            A faint continuous white line follows a raised paved divider with railings on the
                        left; another roadway lies beyond it.
                        white solid, curb yes, edge_line, evidence partial
Step 2  Right           A continuous solid white line separates my lane from a narrow paved roadside strip
                        occupied by a scooter; the sidewalk curb is beyond that strip, not at this line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left divider and right roadway edge bound one motor-vehicle lane,
                        consistent with my lane being lane 1 of 1. | roles: The white longitudinal lines fit
                        roadway-edge roles rather than a center line or a division between two ordinary motor-
                        vehicle lanes. | markings: No arrows, words, symbols, transverse lines or waiting
                        areas are visible in my lane. | unseen: The left paint is faint and partly affected by
                        glare, so its evidence is partial; no markings are inferred in the distant roadway. |
                        result: consistent
Step 5  Rule            left_boundary: The raised divider forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            right_boundary: The solid white roadway-edge line separates the motor-vehicle lane
                        from the roadside strip and prohibits crossing into it in ordinary driving.
Step 6  change_left     prohibited (correct): The raised divider prohibits leaving the lane to the left.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits crossing into the roadside
                        strip.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the lane without crossing either boundary, and leave clearance for the
                        scooter on the right. Check your vehicle's height against the posted 2.5 m restriction
                        before passing beneath the gantry.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 799, 14.98 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban roadway continues straight beside a raised divider on the left and a sidewalk
                        on the right, with a pedestrian footbridge overhead. My car follows a taxi in the left
                        of two visible lanes; the next intersection is not clearly visible. (lanes 2, mine 1,
                        full)
Step 2  Left            A continuous raised concrete divider forms the left edge of my lane; no painted
                        boundary line is clearly visible, and another carriageway lies beyond it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A worn white solid line runs from the foreground toward the taxi, with another strip
                        of roadway beyond it and a raised sidewalk farther right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left physical edge and right lane line agree with my car occupying the
                        leftmost of two visible lanes. | roles: The concrete divider fits a roadway edge; the
                        white solid line fits a same-direction lane separator. | markings: No arrows, words,
                        symbols, or transverse markings are readable in the visible portion of my lane. |
                        unseen: No unseen arrows or lane-end markings are inferred; the taxi and distance
                        obscure the farther roadway. | result: consistent
Step 5  Rule            left_boundary: The raised concrete divider is a physical roadway boundary and must not
                        be crossed.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 6  change_left     prohibited (correct): The raised concrete divider prohibits leaving the lane to the
                        left.
Step 6  change_right    prohibited (correct): The solid white lane separator prohibits crossing to the right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane behind the taxi without crossing the divider or solid white
                        line. Check the markings and controls farther ahead before choosing any turn; no
                        stopping position is visible here.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 853, 17.91 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues straight ahead, with two motor-vehicle lanes on this
                        carriageway. My car is in the left lane beside a raised planted divider; no
                        intersection or lane ending is visible. (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs alongside a raised curb and planted divider on the left, with
                        a separate roadway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and adjoining gaps, separates my lane from
                        the lane occupied by the black sedan on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane divider on the right agree with my car
                        being in lane 1 of two lanes. | roles: The solid white line beside the raised divider
                        fits an edge line; the broken white line between same-direction lanes fits a lane
                        line. | markings: No lane-use arrows, words, symbols, transverse lines, or waiting
                        areas are visible in my lane. | unseen: No movement marking or intersection layout has
                        been inferred beyond the visible road. | result: consistent
Step 5  Rule            left_boundary: The raised divider forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits changing into the
                        adjacent same-direction lane when safe.
Step 6  change_left     prohibited (WRONG, label allowed): The raised divider at the left edge prohibits
                        crossing to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a rightward lane change when
                        safe.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; do not cross the raised divider on the left. A
                        rightward lane change is permitted by the markings, but check the black sedan and
                        other traffic before moving.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 779, 11.1 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road continues ahead, with a planted median on the left and a narrow
                        roadside strip used by scooters on the right. My car is in the single visible motor-
                        vehicle lane; no intersection or lane ending is visible. (lanes 1, mine 1, full)
Step 2  Left            A raised concrete curb beside the planted median forms the left boundary; no distinct
                        painted boundary line can be identified along it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from a narrow paved roadside strip
                        occupied by scooters, with the sidewalk curb farther to the right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median curb on the left and roadway edge line on the right agree with
                        one motor-vehicle lane, indexed 1. | roles: The raised median edge and solid white
                        roadside boundary fit edge roles rather than same-direction lane dividers. | markings:
                        No arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No intersection layout or distant movement restrictions have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The raised median curb is a physical roadway boundary and must not be
                        crossed to leave this lane.
Step 5  Rule            right_boundary: The solid white roadway edge marking prohibits crossing into the
                        roadside strip during ordinary driving.
Step 6  change_left     prohibited (correct): The raised median curb prohibits leaving the lane to the left.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white edge line prohibits crossing
                        into the roadside strip.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the lane between the median curb and solid white edge line, watching
                        for scooters near the right boundary. No turning guidance or stopping point is
                        visible; assess those when approaching an intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 800, 14.21 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road runs alongside an elevated roadway, with three motor-vehicle lanes in
                        this direction and a separated non-motorized strip on the right. My car is in the
                        middle lane; the road continues ahead, with no clear intersection or lane ending
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        motor-vehicle lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        motor-vehicle lane on the right; the solid white line and roadside curb are farther
                        beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small white forward-pointing arrow is visible farther
                        ahead in my lane; its detail is reduced by distance.
Step 4  Cross-check     position: Two lane-line boundaries agree with my position in lane 2 of three motor-
                        vehicle lanes. | roles: Both broken white boundaries fit divisions between lanes
                        travelling in the same direction. | markings: The visible straight arrow is compatible
                        with the continuing lane and its two broken white boundaries. | unseen: The distant
                        arrow has limited detail; no unseen intersection, stop line, or waiting area is
                        assumed. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider may be crossed to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider may be crossed to enter the
                        adjacent motor-vehicle lane when safe.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and does
                        not permit left turns, right turns, or U-turns from this lane.
Step 6  change_left     allowed (correct): The broken white left lane divider permits a safe lane change.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white right lane divider permits a safe
                        lane change into the adjacent motor-vehicle lane.
Step 6  go_straight     allowed (contested, correct): The visible forward arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken divider may be crossed after checking
                        traffic. For a turn, move safely into an appropriately marked lane before reaching the
                        junction, and do not enter the non-motorized strip on the far right.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 6396, out 1056, 19.41 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China continues straight toward a pedestrian overpass. My car is in
                        the single motor-vehicle lane, with a planted divider on the left and a separate non-
                        motorized lane on the right. (lanes 1, mine 1, full)
Step 2  Left            A solid white line runs beside a raised curb and planted divider on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the strip used by bicycles and scooters on
                        the right; riders obscure portions of the line, and there is no curb at this boundary.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        arrow:straight (full): A large white arrow with a single straight-ahead head is
                        painted immediately ahead of the car.
Step 4  Cross-check     position: One motor-vehicle lane agrees with a left roadway edge and a right boundary
                        to a non-motorized lane. | roles: The white solid lines fit roadway-edge and
                        motor/non-motor separation roles; neither is a center line. | markings: The straight-
                        ahead arrow agrees with the continuing motor-vehicle lane. No waiting area or
                        conflicting lane-use marking is visible. | unseen: Riders conceal portions of the
                        right boundary, so its evidence is partial. No hidden intersection markings are
                        assumed. | result: consistent
Step 5  Rule            left_boundary: The solid roadway-edge marking and raised divider do not permit leaving
                        the lane across its left side.
Step 5  Rule            right_boundary: The solid separation from the non-motorized lane prohibits an ordinary
                        motor vehicle from crossing into that lane here.
Step 5  Rule            arrow:straight: A straight-only guidance arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 6  change_left     prohibited (correct): The solid left edge and raised divider prohibit crossing to the
                        left.
Step 6  change_right    prohibited (contested, correct): The solid boundary to the non-motorized lane
                        prohibits crossing to the right.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits straight travel.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the boundaries govern lateral departures, the arrow governs directional
                        movements, and no waiting-area action is inferred.
Advice                  Continue straight within the motor-vehicle lane; do not cross the left divider or
                        enter the non-motorized lane on the right. Leave ample space for the cyclists and
                        scooter riders ahead, and seek a suitably marked lane farther along if you need to
                        turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1111, 18.7 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China with a narrow through lane between a planted physical divider
                        on the left and a curbside parking strip on the right. My car is behind a sedan; the
                        lane continues ahead, but its eventual intersection or end is obscured. (lanes 1, mine
                        1, full)
Step 2  Left            A single continuous pale-yellow line runs beside a raised curb and concrete planting
                        divider, with another roadway beyond the divider.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A single continuous pale-yellow line separates my lane from a strip occupied by parked
                        cars; the sidewalk curb is beyond that strip rather than directly on this boundary.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One through lane, indexed 1, agrees with edge boundaries on both sides; the
                        parked-car strip is not counted as another through lane. | roles: The continuous
                        painted lines follow the edges of the usable through roadway; the left physical
                        divider additionally establishes its edge. | markings: No arrow, word, symbol, waiting
                        area or transverse marking is readable in the visible part of my lane. | unseen: The
                        sedan and more distant vehicles obscure the pavement ahead, so no marking or
                        intersection layout is inferred beneath or beyond them. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised physical divider prohibit leaving the
                        lane across its left boundary.
Step 5  Rule            right_boundary: The solid roadway-edge line must not be crossed for an ordinary lane
                        change into the curbside strip.
Step 6  change_left     prohibited (correct): The solid edge and raised divider prohibit crossing the left
                        boundary.
Step 6  change_right    prohibited (contested, correct): The solid right edge prohibits an ordinary move into
                        the curbside strip.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the boundaries govern only lateral departures, and no unseen directional
                        marking is used to decide a turn.
Advice                  Continue within the narrow lane behind the sedan without crossing either boundary.
                        Watch for pedestrians emerging beside the parked vehicles, and reassess turn guidance
                        when the road ahead becomes visible.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 889, 18.02 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues straight ahead alongside buildings. My car is
                        beside the landscaped median, with a row of vehicles occupying the roadway to the
                        right; their presence obscures the outer road layout. (lanes None, mine 1, partial)
Step 2  Left            A continuous solid white line runs along the left side of my lane beside a raised curb
                        and landscaped median, with opposing traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears continuous along the right side, with portions obscured by a
                        rider and vehicles; whether the space beyond is a traffic lane or roadside parking is
                        unclear.
                        white solid, curb no, unknown, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median-side edge places my lane leftmost; the obscured use and outer
                        boundary of the space to the right prevent a reliable total lane count. | roles: The
                        solid white left edge line agrees with the median curb; the right line's role cannot
                        be established confidently from the vehicles beyond it. | markings: No readable
                        arrows, words, symbols, waiting areas or transverse traffic-control lines are visible
                        in my lane. | unseen: No intersection layout or distant lane-use marking is inferred;
                        the right-side space is not assumed to be either parking or another travel lane. |
                        result: consistent
Step 5  Rule            left_boundary: The raised median curb is a physical road boundary and must not be
                        crossed to leave this lane.
Step 5  Rule            right_boundary: In China a solid white traffic-lane dividing line prohibits crossing,
                        but the line's uncertain role here prevents confidently applying that rule rather than
                        a roadway-edge rule.
Step 6  change_left     prohibited (correct): The raised median curb prohibits leaving the lane to the left.
Step 6  change_right    not_determined (WRONG, label prohibited): The right boundary's role and the use of the
                        space beyond are uncertain.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the visible lane, allowing space for the rider ahead; do not cross the
                        median curb. Avoid moving right until the boundary's function and the space beyond are
                        clear, and check the markings at the next intersection before choosing a turn.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 887, 19.69 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China has opposing traffic separated by a metal fence. My car is in
                        the left of two visible same-direction lanes; traffic continues ahead, but the next
                        intersection and lane end are not visible. (lanes 2, mine 1, full)
Step 2  Left            A metal separation fence forms the left boundary, with yellow paint visible along its
                        base, partly hidden by fence supports; opposing traffic lies beyond.
                        yellow solid, curb yes, center_line, evidence partial
Step 2  Right           A white broken line, with several visible dashes and gaps, separates my lane from
                        another same-direction traffic lane, with no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 1 agree with the opposing-
                        traffic separator on the left and a same-direction lane line on the right. | roles:
                        The yellow paint and physical separator fit the center boundary; the broken white line
                        fits a same-direction lane divider. | markings: No guidance markings are visible on
                        the exposed pavement of my lane, so there is no marking conflict. | unseen: The yellow
                        line is partly obscured by the fence, and distant pavement is obscured by vehicles; no
                        distant arrow or intersection marking is inferred from the roadside sign. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a central physical separation barrier must not be crossed, so
                        my car cannot leave the lane to the left.
Step 5  Rule            right_boundary: A broken white same-direction lane divider may be crossed to change
                        lanes when safe and without obstructing other traffic.
Step 6  change_left     prohibited (WRONG, label not_determined): The central physical separation fence
                        prohibits crossing the left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent same-direction lane.
Step 6  go_straight     allowed (contested, correct): No visible lane arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible in-lane arrow or prohibited-movement marking governs this
                        action at the next intersection.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change right across the broken white line when safe; do not
                        cross the central fence. The visible 40 km/h sign and lane-direction sign provide
                        additional guidance, but check the actual intersection markings before selecting a
                        turning lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 905, 14.66 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China has two motor-vehicle lanes in this direction, with opposing
                        traffic separated by a fenced median and a non-motorized lane on the right. My car is
                        in the rightmost motor-vehicle lane; the road continues ahead, with no intersection or
                        lane ending clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A white broken line, with multiple dashes and gaps visible, separates my lane from
                        another motor-vehicle lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line borders my lane on the right, with a non-motorized lane
                        beyond it; farther ahead, a raised separator follows this boundary.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two motor-vehicle lanes and ego position 2 agree with a lane line on the
                        left and a roadway edge adjoining the non-motorized lane on the right. | roles: The
                        broken white left line fits a same-direction lane divider; the solid white right line
                        and raised separator fit the motor-vehicle roadway edge. | markings: No guidance
                        markings are visible in my lane, so none conflict with the boundaries. | unseen: No
                        distant lane-end marking or movement arrow has been inferred; vehicles obscure some
                        pavement farther ahead. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider may be crossed to
                        change lanes when safe.
Step 5  Rule            right_boundary: The solid boundary and raised separator to the non-motorized lane
                        prohibit an ordinary car from moving right into that lane along this stretch.
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        lane change to the left.
Step 6  change_right    prohibited (correct): The solid boundary and raised separator prohibit moving into the
                        non-motorized lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this motor-vehicle lane, or change left across the broken line when safe;
                        do not move right into the non-motorized lane. Turn-lane choices and any stopping
                        requirement must be checked farther ahead because no intersection guidance or stop
                        line is visible here.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 848, 15.45 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban two-way street in China continues ahead, with a separated bicycle/non-
                        motorized strip on the right. My car is in the single visible motor-vehicle lane of
                        its direction, behind a sedan; no intersection stop line is visible. (lanes 1, mine 1,
                        full)
Step 2  Left            A single yellow broken line, with visible dashes and gaps, separates my lane from the
                        opposing side of the road; there is no curb along this line.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A white line is visible beside a low separation fence, with a non-motorized strip
                        beyond; the fence obscures enough of the line that its complete pattern is uncertain.
                        white dashed, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:straight (partial): Immediately above the hood, a partially visible white
                        forward-pointing arrowhead appears in my lane; its shaft and any additional branches
                        are hidden.
Step 4  Cross-check     position: One motor-vehicle lane in my direction agrees with a center line on the left
                        and a physically separated non-motorized strip on the right. | roles: The yellow
                        broken line fits a center line. The white marking and fence fit the right roadway
                        edge, although the white line's full pattern is obscured. | markings: The visible
                        forward arrowhead agrees with the continuing lane, but the hidden portion prevents
                        confirming whether it also has turning branches. | unseen: The right line's pattern is
                        only tentative, and no hidden arrow branches, distant intersection markings, or stop
                        line are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken yellow center line may be crossed temporarily for
                        overtaking or avoiding an obstruction when safe and without interfering with opposing
                        traffic.
Step 5  Rule            right_boundary: The physical separation fence must not be crossed to enter the non-
                        motorized strip.
Step 5  Rule            arrow:straight: A forward arrowhead permits proceeding straight, but hidden branches
                        prevent establishing the arrow's complete set of permitted movements.
Step 6  change_left     allowed (WRONG, label prohibited): The broken yellow center line permits temporary
                        crossing when safe, yielding to opposing traffic.
Step 6  change_right    prohibited (WRONG, label not_determined): The separation fence prohibits crossing into
                        the non-motorized strip.
Step 6  go_straight     allowed (contested, correct): The visible forward arrowhead permits proceeding
                        straight.
Step 6  turn_left       not_determined: The arrow's hidden portion prevents determining whether a left-turn
                        branch exists.
Step 6  turn_right      not_determined: The arrow's hidden portion prevents determining whether a right-turn
                        branch exists.
Step 6  u_turn          not_determined: The incomplete arrow prevents determining its complete movement
                        restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight behind the sedan and stay left of the separation fence. Cross the
                        broken yellow center line only for a safe, lawful temporary maneuver; confirm the
                        complete lane arrow and intersection controls before attempting any turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_left'], citation None,
                        contradictions []
Tokens                  in 6396, out 1172, 26.86 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China approaches a signalized intersection. My car is in the
                        rightmost motor-vehicle lane, beside a separated bicycle lane; vehicles obscure the
                        full number of motor-vehicle lanes to the left. (lanes None, mine None, insufficient)
Step 2  Left            White broken paint, with a long dash and gaps visible, separates my lane from the
                        motor-vehicle lane occupied by the white car and bus; there is no curb on this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Two parallel continuous white lines border my lane on the right, with a bicycle lane
                        beyond and separator posts farther ahead; the sidewalk curb lies beyond the bicycle
                        lane.
                        white double_solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (insufficient): A small, distant white directional marking is visible
                        ahead in my lane, but its arrowhead and any branches cannot be read reliably.
Step 4  Cross-check     position: A same-direction lane lies to my left and a bicycle lane lies to my right,
                        consistent with being the rightmost motor-vehicle lane; the total count and numerical
                        index remain obscured. | roles: The broken white left divider fits a same-direction
                        lane line, and the paired continuous white right lines fit separation from the bicycle
                        lane. | markings: The distant directional marking is not sufficiently clear to
                        establish its complete permitted directions. | unseen: The arrow:right label is only a
                        tentative identification, not a confirmed right-only instruction; no stop line,
                        crosswalk, or waiting area can be identified reliably. | result: Consistent with
                        insufficient evidence for the distant arrow and lane count.
Step 5  Rule            left_boundary: A broken white lane divider permits changing into the adjacent motor-
                        vehicle lane when safe.
Step 5  Rule            right_boundary: The continuous boundary separating the motor-vehicle lane from the
                        bicycle lane must not be crossed for a lane change.
Step 5  Rule            arrow:right: A confirmed right-only arrow would require turning right, but this
                        distant marking is too unclear to establish that restriction.
Step 6  change_left     allowed (correct): The visible broken white lane divider permits crossing when safe.
Step 6  change_right    prohibited (correct): The continuous white boundary separates my lane from the bicycle
                        lane and prohibits crossing.
Step 6  go_straight     not_determined (contested, label allowed): The distant lane-use arrow cannot be read
                        well enough to establish whether straight travel is permitted.
Step 6  turn_left       not_determined: The distant lane-use arrow cannot be read well enough to determine
                        whether it includes a left turn.
Step 6  turn_right      not_determined: The apparent right-turn arrow is too distant to confirm its permitted
                        movements reliably.
Step 6  u_turn          not_determined: The distant lane-use arrow cannot be read well enough to determine its
                        complete movement restrictions.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable.
Step 7  Reflect         Consistent: crossing permissions follow the visible boundaries, while intersection
                        movements remain undecided because the directional marking is unreadable.
Advice                  Do not cross the paired white lines into the bicycle lane; a left lane change is
                        possible only after checking traffic. Confirm the lane arrow as you approach, consult
                        the overhead lane-direction sign, and obey the intersection signals.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1093, 21.35 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           A tree-lined urban road in China continues straight ahead, with opposing traffic on
                        the left and a sidewalk on the right. My car is in the single visible lane of its
                        direction; no intersection or lane ending is clearly visible ahead. (lanes 1, mine 1,
                        full)
Step 2  Left            A yellow broken line, with visible long dashes and gaps, separates my lane from the
                        roadway carrying opposing traffic on the left; there is no curb along this boundary.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A raised curb borders my lane on the right, with a paved sidewalk and trees beyond; no
                        separate painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and curb on the right agree with my lane being
                        the only visible lane of my direction. | roles: The yellow broken line fits an
                        opposing-traffic center line, and the curb forms the right roadway edge. | markings:
                        No arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No marking is inferred beneath the van or beyond the clearly visible road. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken yellow center line may be crossed temporarily for
                        overtaking or avoidance when safe and without obstructing opposing traffic.
Step 5  Rule            right_boundary: The raised roadway curb must not be crossed to drive onto the
                        sidewalk.
Step 6  change_left     allowed (correct): The broken yellow center line permits temporary crossing when safe,
                        subject to opposing traffic.
Step 6  change_right    prohibited (correct): The raised curb prohibits leaving the roadway onto the sidewalk.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane and keep clear of the right curb. Crossing the broken yellow
                        line would enter opposing traffic, so do so only for a lawful maneuver with ample
                        visibility and clearance; no intersection-turn guidance is visible.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1018, 23.75 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight ahead, with a planted median on the
                        left and a curb on the right. My car is in the middle of five same-direction lanes; no
                        intersection or lane ending is clearly visible. (lanes 5, mine 3, full)
Step 2  Left            A white broken line, with long dashes and visible gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and visible gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 3 of 5 has same-direction lanes on both sides, consistent with both
                        boundaries being lane lines. | roles: Both white broken boundaries fit same-direction
                        lane separators. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are visible in my lane. | unseen: No hidden marking or distant
                        intersection layout has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane line may be crossed to change lanes when
                        safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane line may be crossed to change lanes when
                        safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The white broken lane line permits a safe change into the adjacent
                        left lane.
Step 6  change_right    allowed (correct): The white broken lane line permits a safe change into the adjacent
                        right lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight, and my lane does not visibly end.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change lanes across either broken white boundary
                        after checking for a safe gap. Turning arrangements and any stopping requirement at
                        the next intersection are not established by this view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 837, 10.39 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China approaches a signal-controlled intersection. My car is in a
                        lane beside a curbside strip on the right; vehicles obscure the full extent of the
                        same-direction lanes to the left. (lanes None, mine None, insufficient)
Step 2  Left            A continuous white solid line separates my lane from an occupied motor-vehicle lane on
                        the left; parts are obscured by vehicles.
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           A continuous white solid line borders my lane on the right, with a paved curbside
                        strip and then a raised yellow-painted curb beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A large white arrow has one head pointing straight ahead
                        and a branch with a head pointing right.; line:stop_line (partial): A faint transverse
                        white line appears across the lane immediately before the pedestrian crossing.;
                        line:crosswalk (full): White zebra-crossing bars extend across my lane ahead.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane on the left, while
                        the right edge line bounds the motor-vehicle roadway; the total count and numerical
                        lane position remain obscured. | roles: The solid white left separator fits a lane
                        line, and the solid white right boundary fits an edge line adjoining the curbside
                        strip. | markings: The straight-and-right arrow is compatible with this approach lane;
                        the stop line and crosswalk do not contradict it. | unseen: No exact lane count or
                        numerical lane position is inferred, and the faint stop line is recorded with partial
                        evidence. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: A white roadway edge line is not itself a blanket prohibition on
                        crossing, but does not authorize driving in a reserved non-motorized strip.
Step 5  Rule            arrow:straight_right: This lane-use arrow permits straight-ahead and right-turn
                        movements, not left turns or U-turns.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal or
                        traffic control, rather than independently requiring a stop.
Step 5  Rule            line:crosswalk: Drivers must protect and yield to pedestrians using the marked
                        crossing.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white lane-dividing line prohibits
                        crossing to the left.
Step 6  change_right    not_determined (correct): The edge line alone does not prohibit crossing, but the
                        curbside strip's designation is not sufficiently visible to determine whether entry is
                        permitted.
Step 6  go_straight     allowed (correct): The straight head of the lane-use arrow permits proceeding
                        straight.
Step 6  turn_left       prohibited (correct): The straight-and-right arrow does not permit a left turn.
Step 6  turn_right      allowed (correct): The right-pointing head of the lane-use arrow permits a right turn.
Step 6  u_turn          prohibited (correct): The straight-and-right arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for straight travel or a right turn, without crossing the solid left
                        divider or entering the curbside strip. Obey the traffic signals, stop before the stop
                        line when required, and yield to pedestrians and curbside riders before turning.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        None, contradictions ['change_right not_determined with full evidence']
Tokens                  in 6396, out 1232, 23.82 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided-by-markings urban road in China descends toward an underpass, with opposing
                        traffic to the left. My car is in the middle of three lanes in its direction; no
                        intersection or lane ending is visible. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with being in lane 2 of 3 in my direction. |
                        roles: Both white broken boundaries fit same-direction lane-divider roles; the yellow
                        center markings are farther left, not my lane boundary. | markings: No arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. | unseen: No hidden
                        markings or intersection layout have been inferred; the road beyond the underpass is
                        not fully visible. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken same-direction lane line permits crossing to
                        change lanes when safe without impeding other traffic.
Step 5  Rule            right_boundary: In China, a white broken same-direction lane line permits crossing to
                        change lanes when safe without impeding other traffic.
Step 6  change_left     allowed (WRONG, label prohibited): The white broken lane divider permits a safe change
                        into the adjacent left lane.
Step 6  change_right    allowed (WRONG, label not_determined): The white broken lane divider permits a safe
                        change into the adjacent right lane.
Step 6  go_straight     allowed (contested, correct): No arrow or other visible lane marking restricts
                        continuing straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane toward the underpass; either adjacent lane may be entered across
                        its broken white divider after checking traffic and blind spots. No visible markings
                        establish turning movements or a stopping point; reassess when the road ahead becomes
                        visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6396, out 801, 11.45 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road descends toward an underpass, with three lanes in this direction.
                        My car is in the middle lane; no intersection or lane ending is visible. (lanes 3,
                        mine 2, full)
Step 2  Left            A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 2 agree with a same-direction lane across each
                        boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No guidance markings are visible inside my lane; the hatched
                        area farther left is outside it. | unseen: No hidden markings or intersection
                        movements have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe without obstructing traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe without obstructing traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along this
                        continuing lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane toward the underpass. Either adjacent lane may be entered
                        across the broken white line after checking traffic and signaling; no lane change is
                        required.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 753, 10.49 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban two-way road in China continues ahead, with no clearly visible intersection
                        or lane ending. My car is in the rightmost of two general-traffic lanes in this
                        direction, beside a separated roadside strip. (lanes 2, mine 2, full)
Step 2  Left            A white broken line, with several clear dashes and gaps, separates my lane from
                        another same-direction traffic lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous broad white solid line separates my lane from a narrow roadside strip
                        used by bicycles and scooters; the raised sidewalk curb is beyond that strip, not at
                        my lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two general-traffic lanes and ego lane index 2 agree with a lane divider on
                        the left and a roadway-edge boundary on the right. | roles: The broken white line fits
                        a same-direction lane divider; the solid white line fits separation from the roadside
                        non-motorized strip. | markings: No readable arrows, words, symbols, waiting areas, or
                        transverse lines are visible in my lane. | unseen: No lane-use instruction has been
                        inferred from the distant signs or from markings beyond readable range. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white boundary separating the motor-vehicle lane from the
                        roadside non-motorized strip must not be crossed for an ordinary lane change.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (correct): The solid white separation from the non-motorized strip
                        prohibits an ordinary lane change right.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: each boundary governs only crossing on its own side, and no intersection
                        movement permission is inferred from the boundaries.
Advice                  Continue straight in this lane, or change left across the broken line when safe; do
                        not move right into the non-motorized strip. No visible marking establishes a turning
                        lane or stopping point, so reassess as the next junction comes into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 933, 19.21 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           My car is in a narrow, single-lane roadway between a planted divider and a sidewalk,
                        following a van toward an elevated structure. No intersection or lane ending is
                        visible; other traffic is beyond the planted divider. (lanes 1, mine 1, full)
Step 2  Left            An unpainted raised curb borders the planted divider on the left, with traffic beyond
                        the vegetation; no painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           An unpainted raised curb separates the roadway from a paved sidewalk beside a red
                        wall; no painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The two curb-defined roadway edges agree with a single lane and ego lane
                        index 1; traffic beyond the planted divider is outside this roadway. | roles: Both
                        boundaries are physical roadway edges, not painted lane or center lines. | markings:
                        No guidance markings are visible on the exposed pavement, and none conflict with the
                        boundaries. | unseen: The van obscures some pavement ahead, and the lane's eventual
                        outlet is not visible; no markings or outlet layout are inferred there. | result:
                        consistent
Step 5  Rule            left_boundary: The raised curb and planted divider form a physical roadway edge that
                        the car must not cross.
Step 5  Rule            right_boundary: The raised curb separates the roadway from the sidewalk, which an
                        ordinary car must not enter.
Step 6  change_left     prohibited (correct): Crossing the raised curb into the planted divider is prohibited.
Step 6  change_right    prohibited (correct): Crossing the raised curb onto the sidewalk is prohibited.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other marking restricts continuing
                        along this lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within the curb-defined lane, keeping a safe distance behind the van; do not
                        cross either curb. Reassess turning options when the outlet and any markings become
                        visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 736, 12.7 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           A wide urban road approaches a signal-controlled intersection in China. My car is in
                        the rightmost motor-vehicle lane, beside a separating railing; the full number of
                        approach lanes is outside the view. (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; there is no curb along this line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A pale yellow solid line runs alongside the separating railing on the right, with a
                        separate paved corridor beyond the railing.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white bent arrow has a single head pointing right.;
                        line:stop_line (partial): A transverse white stop line is visible ahead of the arrow,
                        although glare reduces its contrast.; line:crosswalk (full): Broad white zebra-
                        crossing stripes cross the approach immediately beyond the stop line.
Step 4  Cross-check     position: The left lane line and right physical edge identify my lane as the rightmost
                        lane; the cropped left side prevents a reliable total count or numerical index. |
                        roles: The solid white divider fits a same-direction lane boundary, and the yellow
                        line beside the railing fits the roadway edge. | markings: The right-turn-only arrow
                        is compatible with the rightmost lane; the stop line and crosswalk do not add other
                        permitted movements. | unseen: No lane count or numerical index is inferred from the
                        cropped roadway; glare limits the stop-line observation. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes.
Step 5  Rule            right_boundary: The solid yellow roadway edge and physical railing prohibit leaving
                        the lane across this side.
Step 5  Rule            arrow:right: The right-turn lane-use arrow requires turning right and excludes
                        straight, left-turn and U-turn movements from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the traffic
                        control, but does not independently require every vehicle to stop.
Step 5  Rule            line:crosswalk: The crosswalk requires attention and yielding to pedestrians and must
                        not be obstructed.
Step 6  change_left     prohibited (correct): The solid white lane divider prohibits crossing to the left.
Step 6  change_right    prohibited (correct): The solid yellow edge and physical railing prohibit crossing to
                        the right.
Step 6  go_straight     prohibited (correct): The right-only arrow does not permit going straight.
Step 6  turn_left       prohibited (correct): The right-only arrow does not permit turning left.
Step 6  turn_right      allowed (correct): The arrow explicitly permits turning right.
Step 6  u_turn          prohibited (correct): The right-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane only to turn right; do not cross either boundary in the visible
                        approach. Obey the applicable signals, stop before the stop line when required, and
                        yield to pedestrians and other crossing traffic.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1129, 22.1 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight beneath an overpass, with no intersection,
                        ramp or lane ending visible. My car is in the leftmost of three lanes in this
                        direction. (lanes 3, mine 1, full)
Step 2  Left            A single solid white line runs along the left of my lane, with a narrow paved margin
                        and a median guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single broken white line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane on the right; there is no curb here.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane divider on the right agree with my lane
                        being lane 1 of 3. | roles: The solid white line beside the median is a roadway edge
                        line, not an opposing-traffic center line; the broken white line separates same-
                        direction lanes. | markings: No arrows, words, symbols or transverse markings are
                        visible in my lane. | unseen: No unseen intersection layout or distant guidance
                        marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, the solid roadway edge line must not be crossed for an
                        ordinary lane change, and the median guardrail is not traversable.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes when
                        safe without interfering with other traffic.
Step 6  change_left     prohibited (WRONG, label allowed): The solid left edge line and median barrier
                        prohibit leaving the lane to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and the lane
                        visibly continues.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken white line after
                        checking traffic and blind spots. Do not cross the solid left edge line toward the
                        median.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 815, 10.77 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, multilane highway in China continues straight ahead, with guardrails on
                        both sides and a marked shoulder on the right. My car is in the rightmost of four
                        same-direction lanes; no intersection or lane ending is visible. (lanes 4, mine 4,
                        full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved shoulder bearing
                        diagonal painted bars and a guardrail farther beyond it; no curb forms the lane
                        boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A large blue circular pavement marking contains the clearly
                        visible number 60.; text:speed_limit (partial): Farther ahead is a red-bordered
                        circular speed marking; its numeral is too small to read confidently.
Step 4  Cross-check     position: Four lanes and an ego position of four agree with a same-direction lane line
                        on the left and a roadway edge line on the right. | roles: The broken white divider
                        fits a lane line, and the continuous white line adjoining the shoulder fits an edge
                        line. | markings: The speed markings are compatible with this highway lane; no clearly
                        readable lane-use arrow or waiting area is visible. | unseen: The distant speed
                        numeral and smaller distant pavement details are not inferred; the shoulder's diagonal
                        bars are outside my lane. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe.
Step 5  Rule            right_boundary: The solid white roadway edge must not ordinarily be crossed to drive
                        on the shoulder.
Step 5  Rule            text:speed_limit: The blue circular 60 marking indicates a minimum speed of 60 km/h
                        under normal conditions, rather than a permitted turning movement.
Step 5  Rule            text:speed_limit: A red-bordered circular speed marking imposes a maximum speed, but
                        its unreadable numeral cannot establish the numerical limit here.
Step 6  change_left     allowed (correct): The broken white lane line permits a safe change into the adjacent
                        ordinary lane.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line prohibits an ordinary
                        move onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No readable lane-use arrow restricts continuing straight
                        along this continuing lane.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary rules govern only lateral crossing, speed markings do not
                        determine turning permissions, and no unreadable speed value is assumed.
Advice                  Continue in this lane, or change left across the broken divider after checking
                        traffic; do not cross the solid right edge onto the shoulder. Observe the marked
                        minimum speed when conditions permit and verify the maximum speed from readable
                        markings or signs ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1191, 23.15 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with three visible lanes traveling in
                        this direction. My car is in the middle lane; no nearby intersection or lane ending is
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A yellowish broken painted line, with visible long dashes and gaps, separates my lane
                        from a lane carrying vehicles in the same direction; no curb forms this boundary.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and gaps, separates my lane from the lane
                        occupied by the bus; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One same-direction lane lies on each side, consistent with being lane 2 of 3
                        and with both boundaries functioning as lane dividers. | roles: The right white broken
                        line fits an ordinary lane divider. The left line appears yellow, which is unusual for
                        an ordinary same-direction divider, but the vehicles beyond it visibly travel in the
                        same direction; no reserved-lane marking is readable. | markings: No arrows, words,
                        symbols, transverse lines, or waiting areas are visible in my lane. | unseen: No
                        unseen lane-use arrows or reserved-lane restrictions have been inferred; the distant
                        road surface is too small to read. | result: Consistent with the visible traffic
                        arrangement, with the unusual yellow left divider explicitly noted.
Step 5  Rule            left_boundary: A broken divider permits crossing when safe and when doing so does not
                        conflict with any applicable lane restriction.
Step 5  Rule            right_boundary: A broken white lane divider permits changing lanes when safe without
                        interfering with traffic in the adjoining lane.
Step 6  change_left     allowed (correct): The visible left boundary is broken and no visible marking reserves
                        the adjacent lane, so crossing it is permitted when safe.
Step 6  change_right    allowed (correct): The white broken right boundary permits a lane change when safe.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No visible marking governs a left turn.
Step 6  turn_right      not_applicable: No visible marking governs a right turn.
Step 6  u_turn          not_applicable: No visible marking governs a U-turn.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: broken boundaries govern only lane changes, and the absence of turn
                        guidance is not treated as permission to turn.
Advice                  Continue straight in this lane; either lane change requires checking for a safe gap,
                        particularly beside the bus and minibus. Check roadside lane-control signs before
                        crossing the unusual yellow broken divider; no turning or stopping location is
                        established by this view.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 970, 20.55 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues ahead with no visible intersection, ramp or lane
                        ending. My car is in the middle of three lanes traveling in this direction. (lanes 3,
                        mine 2, full)
Step 2  Left            White broken paint with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           White broken paint with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with a same-direction lane across each boundary. | roles:
                        Both white dashed boundaries fit ordinary same-direction lane dividers. | markings: No
                        visible in-lane guidance markings conflict with the boundaries or continuing lane. |
                        unseen: No hidden lane-end markings or distant road features have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a white dashed lane divider permits crossing to the adjacent
                        same-direction lane when safe.
Step 5  Rule            right_boundary: In China, a white dashed lane divider permits crossing to the adjacent
                        same-direction lane when safe.
Step 6  change_left     allowed (correct): The white dashed left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white dashed right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): The lane continues and no visible arrow restricts
                        proceeding straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either dashed boundary may be crossed after checking
                        mirrors, blind spots and safe gaps. Watch the vehicles ahead, including the motorcycle
                        in the right lane; no turn location or stop line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 708, 11.8 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road in China continues straight ahead, with guardrails on both
                        sides of this carriageway. My car is in the middle of three lanes; no intersection or
                        lane ending is visible. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane across
                        each boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No hidden lane-end markings or distant intersection
                        layout have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in the current lane. Either broken divider permits a lane change,
                        but vehicles are close on both sides, so check mirrors and blind spots and wait for a
                        safe gap.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 724, 11.24 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined road curves gently right, with no intersection or lane ending
                        visible ahead. My car is in the rightmost of three lanes in this direction. (lanes 3,
                        mine 3, full)
Step 2  Left            A white broken line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line borders my lane on the right, with a narrow paved
                        shoulder and a concrete barrier beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 3 agree with a same-direction lane divider on the
                        left and the roadway edge on the right. | roles: The broken white line fits a same-
                        direction lane divider, and the solid white line fits the shoulder-side roadway edge.
                        | markings: No arrows, words, symbols or transverse markings are visible in my lane,
                        so none contradict the boundaries. | unseen: No hidden markings or intersection layout
                        have been inferred; the barrier is beyond the shoulder rather than directly forming my
                        lane boundary. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge line prohibits ordinary crossing into the
                        shoulder.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white edge line prohibits ordinary
                        crossing onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow or lane ending restricts continuing
                        along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane around the gentle right-hand curve, or change left across the
                        broken line when safe. Do not cross the solid right edge line onto the shoulder; no
                        intersection turn guidance or stopping point is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 843, 14.42 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues beneath several flyovers, with no intersection or
                        lane ending visible ahead. My car is in the leftmost of three lanes traveling in this
                        direction. (lanes 3, mine 1, full)
Step 2  Left            A single solid line appears pale yellow along the left side of my lane, with a narrow
                        paved margin and a metal guardrail beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from the
                        next same-direction lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my lane being the
                        leftmost of three same-direction lanes. | roles: The solid left line follows the
                        guarded roadway edge; the broken white right line separates same-direction lanes. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are visible in
                        my lane. | unseen: No markings or intersection movements have been inferred beyond the
                        visible road. | result: consistent
Step 5  Rule            left_boundary: In China, a solid roadway edge line is not to be crossed for an
                        ordinary lane change or overtaking maneuver, and the guardrail also prevents passage
                        to the left.
Step 5  Rule            right_boundary: A broken white lane divider permits changing to the adjacent same-
                        direction lane when safe and without obstructing traffic.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid left roadway edge and guardrail
                        prohibit moving out to the left.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white right lane divider permits a
                        safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along this
                        continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change right across the broken white line after checking
                        traffic and blind spots. Do not cross the left edge line toward the guardrail; no
                        turning or stopping location is marked ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 933, 20.17 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane expressway in China continues straight ahead, with no visible
                        intersection, ramp or lane ending. My car is in the leftmost of four lanes in this
                        direction. (lanes 4, mine 1, full)
Step 2  Left            A continuous white line runs along the left of my lane, with a narrow paved margin and
                        a metal median guardrail beyond it; glare gives the paint a warm tint.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction traffic lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car occupying
                        lane 1 of four. | roles: The solid white line beside the median margin fits an edge
                        line, and the broken white line between traffic lanes fits a lane line. | markings: No
                        arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No guidance markings or intersection features have been inferred from the
                        distant roadway; the overhead signs are not readable. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge line beside the median prohibits crossing left
                        onto the median-side margin during ordinary driving.
Step 5  Rule            right_boundary: The broken white lane divider permits a rightward lane change when
                        safe and without interfering with traffic.
Step 6  change_left     prohibited (correct): The solid left edge line prohibits crossing onto the median-side
                        margin.
Step 6  change_right    allowed (correct): The broken white right lane line permits changing into the adjacent
                        ordinary lane when safe.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along this
                        continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken white divider after
                        checking traffic and blind spots; do not cross the solid left edge line. Reduce speed
                        as necessary for the strong glare and follow expressway signs.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 864, 18.61 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined expressway in China continues straight ahead, with no visible
                        intersection, lane ending or ramp split. My car is in the third of four lanes
                        travelling in this direction. (lanes 4, mine 3, full)
Step 2  Left            A single white broken line, with clear long dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with clear long dashes and gaps, separates my lane from
                        another same-direction lane on the right; the solid roadway edge line and concrete
                        barrier lie beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and ego position three agree with two lanes to my left and one to
                        my right, with lane lines on both sides. | roles: Both white broken boundaries fit
                        their roles as same-direction lane dividers. | markings: No arrows, words, symbols,
                        transverse lines or marked waiting areas are visible in my lane. | unseen: No hidden
                        markings or distant junction movements have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe without interfering with other traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change right.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and my lane
                        visibly continues.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent lane may be entered across its broken
                        white divider after signalling and checking for a safe gap. No turn lane, waiting area
                        or stopping line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 780, 13.38 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, two-lane carriageway in China continues ahead without a visible
                        intersection or lane ending. My car is in the left lane, with a truck ahead in the
                        right lane. (lanes 2, mine 1, full)
Step 2  Left            A continuous solid white line borders the lane on the left, with a narrow paved margin
                        and a metal median guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        the adjacent same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego position 1 agree with a left roadway edge
                        and a lane divider on the right. | roles: The solid white left line fits a roadway
                        edge, and the broken white right line fits a same-direction lane divider. | markings:
                        No arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No distant intersection layout or hidden guidance markings have been inferred;
                        the guardrail is beyond the left painted boundary, not directly on it. | result:
                        consistent
Step 5  Rule            left_boundary: In China, the solid white roadway edge prohibits crossing it into the
                        median-side margin during ordinary driving.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes
                        across it when safe and without interfering with other traffic.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white left edge prohibits crossing
                        into the median-side margin.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within your lane and do not cross the solid left edge. You may change into
                        the right lane across the broken line when safe, allowing adequate clearance from the
                        truck.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 822, 13.81 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway in China continues straight ahead, with two travel lanes and an
                        emergency shoulder on the right. My car is in the leftmost travel lane; no
                        intersection, exit or lane ending is visible. (lanes 2, mine 1, full)
Step 2  Left            A solid white line borders my lane on the left, with a narrow paved margin and the
                        median guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           White elongated dashes separated by clear gaps divide my lane from another travel lane
                        on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): Part of a large white Chinese pavement inscription is visible
                        immediately ahead of the hood, resembling the character 小; the remaining wording is
                        obscured and cannot be read.
Step 4  Cross-check     position: Two travel lanes and ego lane index 1 agree with a left roadway edge and a
                        right lane divider; the emergency shoulder is not counted as a travel lane. | roles:
                        The solid white left line fits a roadway edge, and the broken white right line fits a
                        same-direction lane divider. | markings: The partially visible inscription supplies no
                        readable directional instruction and does not contradict either boundary. | unseen:
                        The complete pavement inscription is hidden by the hood and is not inferred; no
                        directional arrow is identifiable. | result: consistent
Step 5  Rule            left_boundary: In China, the solid roadway edge line must not be crossed for an
                        ordinary lane change or overtaking manoeuvre.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing into the
                        adjacent ordinary travel lane when safe.
Step 5  Rule            text:other: This incomplete inscription cannot establish a specific lane-use
                        instruction and does not itself govern any of the seven movement decisions.
Step 6  change_left     prohibited (correct): The solid white roadway edge prohibits crossing to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent travel lane.
Step 6  go_straight     allowed (contested, correct): No visible directional arrow restricts continuing
                        straight along this continuing lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change right across the broken line when safe; do not cross
                        the solid left edge. Observe the overhead lane and speed signs, keep out of the
                        emergency shoulder, and reassess the pavement inscription when it becomes fully
                        visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 979, 15.57 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway in China continues ahead with three same-direction travel lanes
                        and an emergency shoulder on the right. My car is in the rightmost travel lane; no
                        intersection or lane ending is visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction travel lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved emergency
                        shoulder beyond it and a guardrail at the shoulder's outer edge.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The third of three travel lanes has a same-direction lane on its left and a
                        roadway edge adjoining the emergency shoulder on its right. | roles: The broken white
                        lane divider and solid white roadway edge fit their assigned roles. | markings: No
                        guidance markings are visible within my lane; the overhead arrows are signs, not
                        pavement markings. | unseen: No hidden pavement arrows or distant intersection
                        markings have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe.
Step 5  Rule            right_boundary: The solid white expressway edge borders an emergency shoulder, which
                        an ordinary car must not enter for routine driving or overtaking.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): The right edge borders an emergency shoulder, so
                        routine movement onto it is prohibited.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken line after checking traffic.
                        Keep out of the emergency shoulder and observe the overhead lane and speed signs.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 772, 10.83 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, three-lane urban road in China continues straight ahead, with guardrails on
                        both sides and traffic ahead. My car is in the middle lane; no intersection or lane
                        ending is visible. (lanes 3, mine 2, full)
Step 2  Left            White broken lane-line segments are visible on the left, partly obscured by the car
                        ahead, with another same-direction lane beyond and no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible dashes and gaps, separates my lane from the same-
                        direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): White road-text strokes are visible ahead in my lane, but the
                        vehicle ahead obscures much of the inscription and the complete wording cannot be
                        read.
Step 4  Cross-check     position: The middle position among three same-direction lanes agrees with a lane line
                        on each side. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: The partially obscured road text supplies no readable movement
                        instruction; no identifiable directional arrow or waiting area is visible. | unseen:
                        No wording or arrow direction is inferred from the obscured paint, and no intersection
                        layout is inferred beyond the visible road. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider may be crossed to change lanes
                        when it is safe and does not interfere with other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider may be crossed to change lanes
                        when it is safe and does not interfere with other traffic.
Step 5  Rule            text:other: The incomplete road inscription cannot be reliably interpreted and does
                        not establish permission or prohibition for any of the seven assessed actions.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing into the adjacent
                        ordinary lane when safe.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing into the adjacent
                        ordinary lane when safe.
Step 6  go_straight     allowed (contested, correct): No identifiable directional marking restricts continuing
                        straight along the lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the broken boundaries permit only the corresponding lane changes, the
                        unreadable text is not treated as a directional instruction, and no unseen junction
                        movement is authorized.
Advice                  Continue straight in this lane; either lane change is permitted by the visible
                        markings, but check adjacent vehicles and blind spots first. No junction turn
                        allocation or stopping point is visible, and the obscured road text should be
                        reassessed as it becomes readable.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1202, 19.36 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided highway continues straight ahead with no visible intersection or lane
                        ending. My car is in the right lane of two lanes in this direction. (lanes 2, mine 2,
                        full)
Step 2  Left            A white broken line with visible long dashes and gaps separates my lane from the lane
                        occupied by the blue truck; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved shoulder and a
                        guardrail farther beyond it rather than a curb immediately at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A large white numeral 60 is painted in my lane immediately
                        ahead of the hood.; text:speed_limit (full): A yellow numeral 100 is painted farther
                        ahead in my lane.
Step 4  Cross-check     position: Two lanes and an ego position of 2 agree with a same-direction lane line on
                        the left and a roadway edge on the right. | roles: The broken white divider fits a
                        lane line, and the continuous white line beside the shoulder fits an edge line. |
                        markings: The white 60 and yellow 100 are compatible minimum- and maximum-speed
                        pavement markings; neither specifies a turning movement. | unseen: Distant small paint
                        details are not sufficiently readable to classify as additional guidance markings; no
                        intersection or waiting area is visible. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing traffic.
Step 5  Rule            right_boundary: A solid white roadway edge line may be crossed temporarily when
                        necessary, but this does not authorize ordinary driving along the highway shoulder.
Step 5  Rule            text:speed_limit: The white 60 indicates a minimum speed of 60 km/h under conditions
                        permitting that speed and does not govern the seven movement decisions.
Step 5  Rule            text:speed_limit: The yellow 100 indicates a maximum speed of 100 km/h and does not
                        govern the seven movement decisions.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  change_right    allowed (correct): The roadway edge-line rule permits necessary temporary crossing,
                        not routine shoulder travel.
Step 6  go_straight     allowed (contested, correct): No readable directional marking restricts continuing
                        straight along this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, observing the painted 60–100 km/h speed range as conditions
                        permit. Check carefully for the truck before changing left; do not use the right
                        shoulder as a travel lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1208, 27.97 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches an overhead lane-control gantry. My car is in a yellow-
                        bounded reversible lane, with opposing traffic to the left and same-direction traffic
                        to the right; the current directional lane allocation is not fully clear. (lanes None,
                        mine 1, partial)
Step 2  Left            Two parallel yellow broken lines separate my lane from the roadway carrying
                        approaching vehicles on the left; no curb forms this boundary.
                        yellow double_dashed, curb no, center_line, evidence full
Step 2  Right           Two parallel yellow broken lines separate my lane from a lane carrying vehicles away
                        from the camera on the right; no curb forms this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The opposing traffic beyond the left boundary places my lane at the left of
                        the visible same-direction stream; reversible allocation prevents a confident total
                        lane count. | roles: Paired broken yellow boundaries and overhead lane-control
                        equipment support identification of a reversible lane, with opposing traffic beyond
                        its left side. | markings: No readable arrow, word, symbol, waiting area or transverse
                        marking is visible in my lane. | unseen: No lane-use arrow or distant intersection
                        marking has been inferred; the current allocation of all reversible lanes remains
                        uncertain. | result: consistent
Step 5  Rule            left_boundary: In China, a double broken yellow reversible-lane boundary must be used
                        according to lane allocation, and it does not authorize moving into the opposing
                        traffic visible on the left.
Step 5  Rule            right_boundary: The broken reversible-lane boundary permits leaving this special lane
                        for the ordinary same-direction lane on the right when safe.
Step 6  change_left     prohibited (WRONG, label not_determined): The left reversible-lane boundary adjoins
                        opposing traffic, so moving across it into that traffic is prohibited.
Step 6  change_right    allowed (WRONG, label not_determined): The right broken boundary permits leaving the
                        reversible lane for the ordinary same-direction lane.
Step 6  go_straight     allowed (contested, correct): No visible in-lane arrow restricts continuing straight;
                        this is a markings-only assessment.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary decisions concern crossing only, and the straight-ahead marking
                        assessment does not override overhead lane-control signals.
Advice                  The overhead red X appears to close your lane, so do not treat the absence of a
                        restrictive pavement arrow as permission to continue under it. Follow the lane-control
                        signals and move into an open lane to the right only when safe.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1201, 28.93 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A two-way urban road in China has three lanes in our direction. Our car is in the
                        middle lane behind a black SUV; the road continues ahead, with no clearly visible
                        intersection or lane ending. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible dashes and gaps separates our lane from another same-
                        direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates our lane from another same-
                        direction lane on the right; the roadside curb and fence are beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane on each side agrees with three lanes and our position
                        as lane 2. | roles: Both broken white boundaries fit same-direction lane separators. |
                        markings: No guidance markings are visible inside our lane, so none conflict with the
                        boundaries. | unseen: No hidden markings have been inferred; vehicles obscure portions
                        of the road farther ahead. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator may be crossed to change lanes
                        when safe without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator may be crossed to change lanes
                        when safe without obstructing other traffic.
Step 6  change_left     allowed (contested, correct): The broken white left lane separator permits a safe lane
                        change.
Step 6  change_right    allowed (correct): The broken white right lane separator permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or cross either broken white separator only after
                        checking for a safe gap. Turn permissions at the next intersection are not established
                        by the visible markings; check the guidance farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 771, 12.19 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China continues ahead, with oncoming traffic immediately to the left
                        and a large trolleybus alongside on the right. My car is in the left lane of two
                        visible lanes travelling in this direction; the bus obscures much of the right lane
                        and the distant approach. (lanes 2, mine 1, partial)
Step 2  Left            Two parallel yellow broken lines, with aligned dashes and gaps, run along the left of
                        my lane; an oncoming car occupies the lane beyond them, and there is no curb at this
                        boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Short stretches of a pale white broken divider are visible to the right ahead, beside
                        the trolleybus, but the bus hides most of the nearby boundary and the roadway edge.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The ego lane is immediately right of the yellow special-lane boundary, with
                        another same-direction lane occupied by the bus on the right; this supports an ego
                        index of 1, although the complete lane count is partly obscured. | roles: The paired
                        broken yellow lines fit a Chinese reversible-lane boundary; the white broken line on
                        the right fits a same-direction lane divider. | markings: No readable arrows, words,
                        symbols, waiting areas or transverse markings are visible in my lane. | unseen: The
                        bus conceals much of the right boundary, and distant lane-use markings cannot be read;
                        no bus-lane designation is inferred merely from the bus. | result: consistent
Step 5  Rule            left_boundary: In China, paired yellow broken lines identify a reversible lane
                        boundary; under the reserved-special-lane assumption, my ordinary car must not enter
                        the reversible lane to the left.
Step 5  Rule            right_boundary: A white broken lane divider permits changing into the adjacent
                        ordinary lane when safe, but the obscured nearby portion must be checked before
                        crossing.
Step 6  change_left     prohibited (correct): The double broken yellow boundary borders a reversible special
                        lane, which must be treated as reserved.
Step 6  change_right    not_determined (contested, label prohibited): The visible white broken divider permits
                        crossing, but the bus hides the nearby boundary and any continuation that could govern
                        the manoeuvre.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or lane ending restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: entry into the reversible lane is prohibited, the obscured right-side
                        crossing remains undecided, and no intersection-turn permission is inferred from the
                        boundaries.
Advice                  Continue in your present lane without entering the reversible lane on the left. Do not
                        move right alongside the bus; wait until the divider, adjacent space and any lane
                        restrictions are clearly visible, and check the junction markings and signals farther
                        ahead.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1133, 22.09 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban two-way road in China continues toward a distant junction. My car is in the
                        leftmost of two lanes in its direction, with opposing traffic beyond double yellow
                        lines and another same-direction lane on the right. (lanes 2, mine 1, full)
Step 2  Left            Two parallel solid yellow lines separate my lane from opposing traffic; neither is
                        broken, and no curb forms this boundary.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and intervening gaps, separates my lane
                        from the same-direction lane occupied by the van; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and lane line on the right agree with my
                        position as lane 1 of 2. | roles: Double solid yellow paint fits a separation of
                        opposing traffic, and broken white paint fits a same-direction lane divider. |
                        markings: No guidance markings are visible within my lane; there is no conflict with
                        the boundaries. | unseen: No arrows, stop lines or waiting areas are inferred from the
                        distant junction or from portions obscured by vehicles. | result: consistent
Step 5  Rule            left_boundary: In China, double solid yellow center lines prohibit crossing into the
                        opposing side for a lane change or overtaking.
Step 5  Rule            right_boundary: A broken white same-direction lane divider may be crossed to change
                        lanes when it is safe.
Step 6  change_left     prohibited (correct): The double solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent right lane.
Step 6  go_straight     allowed (contested, correct): No visible lane arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action at the next intersection.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken white line only
                        after checking clearance; do not cross the double yellow lines. The roadside sign
                        directs left-turning vehicles toward the auxiliary road, so follow that routing and
                        verify the junction markings before attempting a turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 850, 15.28 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China has a reversible lane alongside a curbside bus lane and a bus
                        platform ahead. My car is in the reversible lane, with opposing traffic immediately to
                        the left. (lanes 2, mine 1, full)
Step 2  Left            Two parallel yellow broken lines, with visible gaps between paired segments, separate
                        my lane from the lane carrying approaching vehicles; there is no curb on this
                        boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A yellow broken line separates my lane from the curbside lane with yellow bus-lane
                        lettering; there is no curb directly on this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white straight-ahead arrowhead is visible immediately
                        ahead of the hood; the lower shaft is obscured by the hood.
Step 4  Cross-check     position: My lane is the leftmost of the two lanes serving this direction; the lane to
                        its right is reserved for buses, while approaching traffic is beyond its left
                        reversible-lane boundary. | roles: The paired yellow broken lines fit a reversible-
                        lane boundary, and the yellow broken line on the right borders the bus lane. |
                        markings: The visible straight arrow agrees with the longitudinal lane layout; the
                        yellow bus lettering is outside my lane and is not an ego-lane marking. | unseen: The
                        arrow shaft is partly hidden, and distant pavement details are not readable; no unseen
                        stop line, turn arrow, or waiting area has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken reversible-lane boundary permits crossing when the
                        reversible-lane controls and receiving traffic direction permit it; leaving this lane
                        is not prohibited merely because it is reversible.
Step 5  Rule            right_boundary: An ordinary car must not enter the adjoining reserved bus lane,
                        despite its broken boundary.
Step 5  Rule            arrow:straight: The straight-ahead lane-use arrow permits continuing straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 6  change_left     allowed (WRONG, label prohibited): The broken boundary of my reversible lane permits
                        crossing, subject to lane-direction controls and a lawful, safe receiving lane.
Step 6  change_right    prohibited (contested, correct): The adjoining lane is reserved for buses, so an
                        ordinary car must not enter it.
Step 6  go_straight     allowed (correct): The visible straight-ahead arrow permits this movement.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane only when the reversible-lane controls permit it, and
                        keep out of the bus lane. Although the left boundary is broken, approaching traffic is
                        immediately beyond it: do not cross into an opposing lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6396, out 1311, 33.35 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road continues ahead past a raised transit platform on the left, with no
                        intersection or lane ending clearly visible. My car is between paired broken yellow
                        boundaries, indicating a reversible-lane arrangement; the directional lane allocation
                        cannot be established from this photograph. (lanes None, mine None, insufficient)
Step 2  Left            Two parallel broken yellow lines, with repeated dashes and gaps, border my lane on the
                        left; another paved traffic lane lies beyond, with no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel broken yellow lines, with repeated dashes and gaps, border my lane on the
                        right; another paved lane with large yellow lettering lies beyond, with no curb at
                        this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The special-lane boundaries do not establish the number of lanes currently
                        assigned to my direction, so neither the directional lane count nor my index is
                        asserted. | roles: Paired broken yellow boundaries on both sides fit a reversible or
                        tidal lane rather than ordinary same-direction lane dividers. | markings: No guidance
                        marking is readable inside my lane; the large yellow lettering to the right is outside
                        it. | unseen: No current reversible-lane direction, unreadable lettering, or obscured
                        downstream marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, paired broken yellow lines delineate a reversible lane; their
                        broken pattern permits crossing when the adjacent lane is legally available and the
                        maneuver is safe.
Step 5  Rule            right_boundary: In China, paired broken yellow lines delineate a reversible lane;
                        their broken pattern permits crossing when the adjacent lane is legally available and
                        the maneuver is safe.
Step 6  change_left     allowed (contested, correct): The broken reversible-lane boundary permits leaving my
                        lane; it is not a solid-line crossing prohibition.
Step 6  change_right    allowed (contested, label prohibited): The broken reversible-lane boundary permits
                        leaving my lane; no readable marking establishes the adjacent lane as reserved.
Step 6  go_straight     allowed (contested, correct): No arrow or visible lane ending restricts continuing
                        straight within my lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the crossing permissions describe the broken markings only and do not
                        establish the current reversible-lane direction or permission to enter opposing
                        traffic.
Advice                  Confirm the reversible-lane direction from lane-control signals or signs before
                        proceeding or changing lanes, and verify that the destination lane permits ordinary
                        cars. No visible marking assigns a turning movement or stopping point to your lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1298, 33.01 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road in China has queued traffic ahead, with strong low-sun glare and
                        vehicles obscuring the distant lane ends. My car is between paired broken lines on the
                        left and a single broken line on the right; the complete lane count and my lane's
                        index cannot be established reliably. (lanes None, mine None, insufficient)
Step 2  Left            Two parallel pale-yellow broken lines, with visible dashes and gaps, run along the
                        left of my lane; there is no curb, and vehicles occupy the roadway beyond them.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A single white broken line with long dashes and gaps separates my lane from the
                        adjacent traffic lane on the right, without a curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: There is roadway to the left and at least one same-direction lane to the
                        right; obscured outer boundaries prevent a reliable total count or lane index. |
                        roles: The paired yellow broken lines identify a reversible-lane boundary in China;
                        the single white broken line fits an ordinary same-direction lane divider. | markings:
                        No arrows, words, symbols, or transverse markings are readable in the visible part of
                        my lane. | unseen: No distant arrow, stop line, intersection layout, or reversible-
                        lane operating status has been inferred through the queued vehicles and glare. |
                        result: consistent
Step 5  Rule            left_boundary: China's paired yellow broken lines delineate a reversible lane, which
                        must not be entered without confirmation that it is open to my direction; under the
                        reserved-lane assumption, changing left is prohibited.
Step 5  Rule            right_boundary: A broken white lane divider permits crossing to change lanes when safe
                        and without interfering with other traffic.
Step 6  change_left     prohibited (WRONG, label allowed): The paired yellow broken boundary borders a
                        reversible lane, treated as reserved when its operating status is unknown.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The distant lane end is obscured, so any movement arrow governing a
                        left turn cannot be checked.
Step 6  turn_right      not_determined: The distant lane end is obscured, so any movement arrow governing a
                        right turn cannot be checked.
Step 6  u_turn          not_determined: The distant lane end is obscured, so any marking governing a U-turn
                        cannot be checked.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue cautiously in your lane and do not enter the reversible lane on the left
                        without confirmed authorization. A right lane change is permitted by the dashed line
                        only when safe; reassess turn guidance and stopping requirements as the queue clears.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1262, 30.37 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China approaches a distant signalized intersection. My car is behind
                        a coach in the middle of three same-direction lanes; the rightmost lane has reddish
                        surfacing. (lanes 3, mine 2, full)
Step 2  Left            A pale white broken line, with a long dash and a gap visible, separates my lane from
                        another same-direction lane on the left; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Broad pale yellow broken segments separate my lane from a reddish-surfaced lane on the
                        right; vehicles obscure much of that lane and its markings, and there is no curb at
                        this boundary.
                        yellow dashed, curb no, unknown, evidence partial
Step 3  Markings        arrow:straight (full): A white arrow immediately behind the coach has a single head
                        pointing straight ahead.
Step 4  Cross-check     position: The ego lane is second of three lanes, with a same-direction lane on each
                        side; neither immediate boundary is the road centre or a curb. | roles: The white
                        broken left boundary fits an ordinary lane divider. The yellow broken right boundary
                        and reddish adjacent surface suggest a special lane, but its designation cannot be
                        confirmed from readable markings. | markings: The straight-only arrow is consistent
                        with continuing along this lane; no other readable guidance marking contradicts it. |
                        unseen: No bus-lane wording is claimed. The coach obscures the farther portion of my
                        lane, including any distant transverse markings. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits changing into the
                        adjacent ordinary lane when safe.
Step 5  Rule            right_boundary: A broken boundary may permit crossing, but entry into a reserved lane
                        is restricted, so the obscured designation of the right-hand lane prevents confirming
                        permission.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires proceeding straight from this
                        lane rather than turning left, turning right or making a U-turn.
Step 6  change_left     allowed (correct): The broken white left lane divider permits a safe lane change.
Step 6  change_right    not_determined (WRONG, label allowed): The adjacent lane's potentially reserved
                        designation is obscured, so crossing permission cannot be established.
Step 6  go_straight     allowed (correct): The visible straight-only arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight, obeying the signals ahead and stopping before the
                        stop line if required once it becomes visible. A safe left lane change is permitted,
                        but do not enter the reddish right-hand lane until its access restrictions are clear.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1094, 23.71 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This is a multilane urban road in China, continuing toward a distant intersection. My
                        car is in the leftmost of three regular forward lanes, beside a separately marked
                        reversible-lane section on the left. (lanes 3, mine 1, full)
Step 2  Left            Two parallel yellow broken lines, with visible gaps in both, separate my lane from the
                        reversible-lane section on the left; there is no curb.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and clear gaps, separates my lane from another
                        forward traffic lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is the leftmost regular forward lane, with a reversible section
                        across its left boundary and additional regular lanes to its right. | roles: The
                        paired broken yellow lines fit a reversible-lane boundary, while the broken white line
                        separates ordinary same-direction lanes. | markings: No guidance marking is readable
                        on the visible pavement within my lane; there is no observed marking that contradicts
                        the boundaries. | unseen: The vehicle ahead conceals some pavement, and distant
                        intersection markings cannot be read; no arrows or transverse markings have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: In China, paired broken yellow lines identify a reversible-lane
                        boundary; the adjacent controlled lane is treated as reserved, so my ordinary car must
                        not change into it without confirmed authorization.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent
                        ordinary lane when safe and without obstructing traffic.
Step 6  change_left     prohibited (WRONG, label allowed): The paired broken yellow boundary leads into a
                        controlled reversible lane, treated as reserved.
Step 6  change_right    allowed (correct): The broken white divider permits a safe change into the ordinary
                        lane on the right.
Step 6  go_straight     allowed (contested, correct): No observed lane-use arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane for straight travel, or change right across the broken white
                        line when safe; do not enter the reversible section on the left. Obey the overhead
                        lane-control signals and check the presently obscured intersection markings before
                        choosing a turning lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1089, 27.05 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           The car appears to be within a broad signal-controlled urban intersection, with a
                        zebra crossing and the continuing roadway ahead. Glare, vehicles and the unmarked
                        intersection surface prevent a reliable count of the approach lanes or identification
                        of the car's lane index. (lanes None, mine None, insufficient)
Step 2  Left            No continuous left boundary can be traced beside the car; glare and a vehicle to the
                        left obscure the approach markings, and no curb immediately bounding this side is
                        identifiable.
                        none none, curb no, unknown, evidence insufficient
Step 2  Right           No reliable right boundary can be traced across the open junction surface; faint pale
                        patches do not establish a line pattern, and the distant roadside curb is not an
                        identifiable boundary of this lane.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        line:crosswalk (full): A white zebra crossing spans the roadway ahead, including the
                        car's projected path.
Step 4  Cross-check     position: Neither lane count nor lane index can be established, and neither boundary
                        has a confirmed role. | roles: No boundary colour or pattern is sufficiently
                        identifiable to assign a lane-line, centre-line or edge-line role. | markings: The
                        visible crosswalk does not specify lane movements; no readable lane-use arrow, word or
                        waiting area is visible in the car's path. | unseen: No hidden line type, arrow or
                        lane count has been inferred; boundary colour 'none' records no identifiable paint,
                        not proof that approach boundaries do not exist. | result: consistent
Step 5  Rule            left_boundary: Because the left boundary cannot be identified, its permission or
                        restriction on crossing cannot be determined.
Step 5  Rule            right_boundary: Because the right boundary cannot be identified, its permission or
                        restriction on crossing cannot be determined.
Step 5  Rule            line:crosswalk: In China, drivers must slow when approaching a pedestrian crossing and
                        stop to yield to pedestrians crossing it; the crossing itself does not assign lane
                        movements.
Step 6  change_left     not_determined (correct): The left boundary and its crossing rule are not
                        identifiable.
Step 6  change_right    not_determined (correct): The right boundary and its crossing rule are not
                        identifiable.
Step 6  go_straight     allowed (contested, label not_determined): No visible arrow or other lane marking
                        restricts continuing straight across the junction.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: unidentified boundaries leave lateral crossing permissions undecided, and
                        the crosswalk is not used to infer turn permissions or an unconditional stop
                        requirement.
Advice                  Continue predictably through the junction only as the applicable signal and traffic
                        conditions permit; this view does not establish a suitable turning lane or safe
                        lateral crossing. Slow for the zebra crossing and stop to yield to pedestrians
                        crossing it, watching closely for cyclists and scooters.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1027, 20.94 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road in China continues toward distant overhead lane-control signals. My
                        car is in the left of two clearly visible ordinary forward lanes, with a separately
                        controlled lane to the left and a red-paved roadside strip to the right. (lanes 2,
                        mine 1, partial)
Step 2  Left            Two parallel yellow broken lines, with visible gaps between paired segments, separate
                        my lane from a lane occupied by a taxi; no curb separates these lanes.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A single white broken line, with long dashes and clear gaps, separates my lane from
                        another forward lane; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is the leftmost clearly identifiable ordinary forward lane, with
                        another ordinary forward lane to its right; the separately controlled lane to the left
                        is excluded from the count because its current directional allocation is uncertain. |
                        roles: The paired yellow broken lines and overhead lane-control context support a
                        reversible-lane boundary; the white broken line fits a same-direction lane divider. |
                        markings: No guidance marking is readable within my lane, so there is no visible
                        conflict with the boundaries. | unseen: No lane-use arrow or intersection-end marking
                        is inferred from the distant, traffic-obscured road; the controlled lane's current
                        directional allocation is not assumed. | result: consistent
Step 5  Rule            left_boundary: In China, paired yellow broken lines identify a reversible-lane
                        boundary; under the reserved-lane treatment, my ordinary car must not enter that
                        controlled lane.
Step 5  Rule            right_boundary: A white broken same-direction lane divider permits changing lanes
                        across it when safe.
Step 6  change_left     prohibited (WRONG, label allowed): The paired yellow broken boundary borders a
                        controlled reversible lane, which is treated as reserved.
Step 6  change_right    allowed (correct): The white broken lane divider permits crossing into the adjacent
                        ordinary lane when safe.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change right only when safe; do not enter the controlled lane
                        across the paired yellow broken lines. Observe the overhead lane-control signals and
                        reassess intersection arrows and stopping requirements when they become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1039, 19.86 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China continues toward a distant junction, with a transit platform on
                        the left and a fenced roadside on the right. My car is between paired yellow broken
                        lines; the permitted directions of the neighboring lanes cannot be established, so the
                        same-direction lane count and my index are uncertain. (lanes None, mine None,
                        insufficient)
Step 2  Left            Two parallel yellow broken lines, with repeated dashes and gaps, separate my lane from
                        another paved lane on the left; there is no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel yellow broken lines, with repeated dashes and gaps, separate my lane from
                        a paved lane carrying large yellow lettering on the right; there is no curb at this
                        boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The paired broken boundaries identify a special central lane, but do not
                        establish which neighboring lanes currently carry traffic in my direction; leaving the
                        count and index unknown avoids a contradiction. | roles: Double yellow broken lines on
                        both sides fit Chinese reversible-lane boundaries rather than ordinary same-direction
                        lane dividers. | markings: No readable arrow, word, symbol, waiting area or transverse
                        line is visible inside my lane. The large yellow lettering is outside its right
                        boundary. | unseen: No current reversible-lane direction, operating schedule or
                        distant lane-use arrow has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, paired yellow broken lines mark a reversible-lane boundary;
                        leaving my own lane across this broken boundary is permitted when the adjacent lane is
                        legally available and the maneuver is safe.
Step 5  Rule            right_boundary: In China, paired yellow broken lines mark a reversible-lane boundary;
                        leaving my own lane across this broken boundary is permitted when the adjacent lane is
                        legally available and the maneuver is safe.
Step 6  change_left     allowed (correct): The left reversible-lane boundary is broken, so its marking permits
                        leaving my lane.
Step 6  change_right    allowed (contested, label prohibited): The right reversible-lane boundary is broken,
                        so its marking permits leaving my lane; the adjacent lettering is not sufficiently
                        readable to establish a reserved lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow or lane-ending marking restricts
                        continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary permissions concern crossing the lines only, not authorization to
                        enter opposing or reserved traffic, and no unseen movement arrow has been assumed.
Advice                  Confirm the reversible lane's current direction using its signs and signals before
                        proceeding. Although the broken boundaries permit crossing, verify the neighboring
                        lane's direction and any reservation before changing lanes; no visible marking
                        establishes a turning lane or stopping point.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1117, 19.71 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road runs between concrete roadside barriers, with no intersection or lane
                        ending visible. My car occupies the central reversible lane, with an opposing lane to
                        the left and a same-direction lane to the right. (lanes 2, mine 1, full)
Step 2  Left            Two parallel yellow broken lines, with visible dashes and gaps, separate my lane from
                        the lane carrying approaching traffic; there is no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel yellow broken lines, with visible dashes and gaps, separate my lane from
                        the lane on the right; there is no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is the leftmost of the two lanes currently carrying traffic in my
                        direction; its special boundaries enclose the central reversible lane rather than
                        ordinary same-direction lanes on both sides. | roles: Paired yellow broken lines on
                        both sides fit the boundaries of a reversible lane in China. | markings: No arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane. | unseen: No
                        operating schedule or lane-control indication is readable; the lane's continuation
                        beyond the vehicles is obscured. | result: consistent
Step 5  Rule            left_boundary: The broken reversible-lane boundary does not itself prohibit leaving
                        the lane, but crossing must comply with reversible-lane controls and must not take the
                        car into opposing traffic.
Step 5  Rule            right_boundary: An ordinary car already in a reversible lane may leave across its
                        broken boundary when safe and consistent with lane controls.
Step 6  change_left     prohibited (correct): Although broken, the left boundary leads into visibly opposing
                        traffic, so it does not authorize an ordinary lane change into that lane.
Step 6  change_right    allowed (WRONG, label not_determined): The right reversible-lane boundary is broken,
                        permitting departure into the adjacent same-direction lane when safe.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other in-lane marking restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the broken boundaries permit crossing only where the destination is
                        lawful, and no intersection movements have been inferred from unseen arrows.
Advice                  Confirm that lane-control signals permit your direction in this reversible lane; the
                        photo does not establish its current operating rules. Do not move into the approaching
                        traffic on the left; a safe move into the same-direction lane on the right is possible
                        across the broken boundary.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1018, 18.89 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China approaches a signal-controlled intersection. My car is in the
                        through lane immediately right of a yellow-bordered reversible lane, with another
                        same-direction lane occupied by a bus on the right. (lanes 2, mine 1, partial)
Step 2  Left            Two parallel yellow broken lines, with paired dashes and gaps visible, separate my
                        lane from a lane bordered by similar yellow markings on its far side; there is no
                        curb.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A white broken line with clearly visible dashes and gaps separates my lane from the
                        lane containing the bus; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has a single head pointing
                        straight ahead.
Step 4  Cross-check     position: My lane is the leftmost of the two ordinary same-direction lanes visible.
                        The reversible lane to its left is excluded from that count because its current
                        direction is not established. | roles: The paired broken yellow boundaries identify a
                        reversible lane, while the broken white boundary separates ordinary same-direction
                        lanes. | markings: The straight-only arrow agrees with a through lane; no turning
                        arrow or waiting-area marking is visible in my lane. | unseen: The reversible lane's
                        current assignment and the distant end of my lane are not readable. No bus-only
                        designation is visible in the lane on the right, and the bus alone does not establish
                        one. | result: consistent
Step 5  Rule            left_boundary: In China, paired broken yellow lines delineate a reversible lane; its
                        unresolved operating assignment means my ordinary car must not enter it under the
                        reserved-lane treatment.
Step 5  Rule            right_boundary: A broken white lane divider permits crossing to change lanes when
                        safe.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 6  change_left     prohibited (correct): The left boundary borders a reversible special lane whose
                        current assignment is unresolved; treat entry as prohibited.
Step 6  change_right    allowed (correct): The broken white divider permits a lane change when safe.
Step 6  go_straight     allowed (correct): The single-headed straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight and obey the intersection signals, stopping before
                        the stop line when required. Do not enter the reversible lane on the left; a rightward
                        lane change is permitted only when clear of the bus and other traffic.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1053, 20.09 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A wide urban road in China approaches a signal-controlled junction beneath elevated
                        structures. My car is in the lane with a straight-ahead arrow; two lanes are visible
                        to its left, but the far-right roadway division is unclear. (lanes None, mine 3,
                        partial)
Step 2  Left            A single white broken line, with visible long painted segments and intervening gaps,
                        separates my lane from another traffic lane on the left; there is no curb along this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with long painted segments and visible gaps, separates my
                        lane from another traffic lane on the right; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow immediately ahead has one head pointing
                        straight forward.
Step 4  Cross-check     position: Lane lines on both sides agree with an interior lane; two lanes are visible
                        to the left, making my lane third from the left. The total count remains uncertain
                        because of the far-right division. | roles: Both white broken boundaries fit ordinary
                        same-direction lane dividers. | markings: The straight-only arrow agrees with a
                        through lane between ordinary lane lines; adjacent-lane arrows do not govern my lane.
                        | unseen: No distant stop line or obscured marking is asserted. The far-right lane
                        classification and markings hidden by vehicles ahead remain unresolved. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 5  Rule            arrow:straight: The straight-ahead lane-use arrow permits proceeding straight from
                        this lane and prohibits left turns, right turns and U-turns from it.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (correct): The single straight-ahead arrow permits this movement.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn from this
                        lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn from this
                        lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight; change lanes across a broken divider only when
                        safe, and select a suitably marked lane before attempting a turn. Obey the signals
                        ahead and stop before the stop line when required; the stop line is not clearly
                        visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1386, 30.94 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road in China approaches a signal-controlled intersection. My car
                        is in the straight-ahead lane, with queued traffic to the left and another lane to the
                        right. (lanes 4, mine 3, partial)
Step 2  Left            A continuous white line with repeated short diagonal teeth separates my lane from the
                        lane on the left; there is no curb between them.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from another paved traffic lane on the right,
                        with no curb along this dividing line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow ahead in my lane has a single head pointing
                        straight forward.; line:stop_line (partial): A transverse white stop line is visible
                        at the intersection approach, just before the pedestrian crossing.; line:crosswalk
                        (full): White zebra-crossing bars extend across the road ahead.
Step 4  Cross-check     position: There are lanes on both sides of my lane, consistent with both boundaries
                        being lane dividers. Four approach lanes and position three appear likely, but queued
                        vehicles obscure parts of the left-side layout. | roles: Both boundaries are white
                        lane dividers; the toothed treatment on the left indicates variable-guidance treatment
                        rather than an opposing-traffic center line. | markings: The straight arrow agrees
                        with continuing within this lane; no conflicting arrow, prohibited-turn marking, or
                        waiting area is visible. | unseen: The obscured left-side lane layout and the distant
                        stop line are not treated as fully established. No reserved-lane status is inferred
                        from the toothed line. | result: consistent
Step 5  Rule            left_boundary: In China, this solid white lane boundary must not be crossed to change
                        lanes; its toothed treatment does not authorize crossing.
Step 5  Rule            right_boundary: A solid white lane divider prohibits changing lanes across it.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 5  Rule            line:stop_line: When a stop is required by the traffic controls, stop before this
                        line; the line alone does not impose an unconditional stop.
Step 5  Rule            line:crosswalk: Keep the pedestrian crossing clear and yield to pedestrians as
                        required.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white left boundary prohibits
                        crossing into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white right boundary prohibits
                        crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): The single straight-ahead arrow permits proceeding
                        straight.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the boundaries govern lane changes, the arrow governs intersection
                        movements, and the stop line and crosswalk do not independently require stop_first.
Advice                  Continue straight from this lane only when the applicable signal permits, without
                        crossing either solid boundary. For a turn, select the appropriate lane earlier where
                        lane changes are permitted; stop before the stop line when required and keep the
                        crossing clear.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:crosswalk', 'line:stop_line'], missed []), actions False,
                        unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1314, 26.89 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight ahead, with a central fence on the
                        left and a bus in the curbside lane on the right. My car is in the second of four
                        visible same-direction lanes; no intersection or lane ending is clearly visible.
                        (lanes 4, mine 2, full)
Step 2  Left            A broken white line, with distinct dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with distinct dashes and gaps, separates my lane from another
                        same-direction lane on the right; the yellow marking beside the bus is farther right
                        and is not my boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The second-of-four position agrees with ordinary same-direction lanes
                        immediately to both sides. | roles: Both white broken boundaries fit same-direction
                        lane-divider roles. | markings: No guidance arrows, words, symbols, transverse lines
                        or waiting areas are visible in my lane. | unseen: No distant lane-end markings are
                        inferred; vehicles and distance limit visibility farther ahead. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to the adjacent
                        same-direction lane when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to the
                        immediately adjacent same-direction lane when safe and without obstructing other
                        traffic.
Step 6  change_left     allowed (WRONG, label prohibited): The broken white left lane divider permits a safe
                        lane change.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white right lane divider permits a
                        safe change into the immediately adjacent lane, not directly into the farther curbside
                        lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or cross either broken white divider only after checking
                        traffic and a safe gap. The next junction's turn assignments and stopping requirements
                        are not visible; reassess them before choosing a turning lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6396, out 825, 14.93 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road at a signalized intersection in China, with a zebra crossing
                        immediately ahead. Vehicles and the intersection opening obscure the approach-lane
                        layout, so the lane count and my lane's index cannot be established reliably. (lanes
                        None, mine None, insufficient)
Step 2  Left            A short curved sequence of white broken paint is visible ahead to the left of the
                        white sedan, but its connection to my lane is obscured by vehicles and the crossing; a
                        raised island lies farther left, not clearly at my lane's boundary.
                        white dashed, curb no, unknown, evidence partial
Step 2  Right           The taxi and other vehicles obscure the right side of my lane; no continuous stretch
                        of its boundary paint or physical edge can be identified.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        line:crosswalk (full): Broad parallel white zebra-crossing stripes extend across the
                        roadway immediately ahead, including my vehicle's path.
Step 4  Cross-check     position: Neither nearby same-direction lanes nor my lane index can be counted
                        reliably; neither boundary is assigned a definite lane-separating or road-edge role. |
                        roles: The visible white broken paint could be intersection guidance, but its
                        relationship to my lane is uncertain; the right boundary is hidden. | markings: The
                        crosswalk is identifiable, but no lane-use arrow, word, or waiting area can be read in
                        my lane. | unseen: No hidden arrow, stop line, or boundary pattern is inferred. The
                        right-side color and curb fields record no visible feature, not proof that none
                        exists. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator generally permits crossing when
                        safe, but this fragment cannot confidently be identified as my lane boundary, so it
                        does not establish permission to change left.
Step 5  Rule            right_boundary: Because the right boundary is obscured, its crossing restrictions
                        cannot be established.
Step 5  Rule            line:crosswalk: Drivers must protect and yield to pedestrians at the crosswalk as
                        required; the crossing itself does not assign lane movements.
Step 6  change_left     not_determined (correct): The visible broken white fragment cannot reliably be linked
                        to my lane's left boundary.
Step 6  change_right    not_determined (correct): The right boundary is hidden by vehicles.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight;
                        the crosswalk does not prohibit that movement.
Step 6  turn_left       not_determined: The approach-lane guidance is obscured, so a governing turn arrow
                        cannot be established.
Step 6  turn_right      not_determined: The approach-lane guidance is obscured, so a governing turn arrow
                        cannot be established.
Step 6  u_turn          not_determined: The approach-lane guidance is obscured, so a governing arrow or
                        prohibition cannot be established.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable.
Step 7  Reflect         consistent
Advice                  Continue only when the signal governing your movement permits and the crosswalk is
                        clear, yielding to pedestrians as required. Avoid lateral moves or turns until the
                        lane boundaries and lane-use guidance can be confirmed; the visible signals alone do
                        not establish your lane's permitted turns.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1052, 22.82 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A busy urban road in China carries opposing traffic on the left and several same-
                        direction lanes ahead. My car is beside the rightmost through lane, behind the red
                        taxi; traffic obscures the distant junction and lane ends. (lanes 3, mine 3, partial)
Step 2  Left            A broken white longitudinal line separates the taxi's lane from the lane containing
                        the silver car; its nearer continuation is partly obscured by the hood.
                        white dashed, curb no, lane_line, evidence partial
Step 2  Right           A solid white line borders a narrow diagonally hatched white strip on the right, with
                        the concrete mixer and roadside pavement beyond.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The apparent rightmost through lane has another same-direction lane to its
                        left and a hatched roadside separation to its right; the exact lane count and near-
                        field alignment are partly obscured. | roles: The broken white line fits a same-
                        direction lane divider, and the solid white line beside roadside hatching fits a
                        roadway edge. | markings: No arrow, word, symbol, or transverse marking is readable
                        inside this lane; the diagonal hatching lies outside its right boundary. | unseen: The
                        distant lane-use markings and junction layout are obscured by traffic; no directions
                        or stop requirement have been inferred from them. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe.
Step 5  Rule            right_boundary: The solid white boundary of the hatched roadside separation must not
                        be crossed for an ordinary lane change.
Step 6  change_left     allowed (correct): The visible broken white lane divider permits a safe change into
                        the adjacent same-direction lane.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white boundary beside the hatched
                        separation prohibits crossing to the right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along the
                        lane.
Step 6  turn_left       not_determined: Traffic hides the distant lane end and any lane-use arrow that would
                        decide this movement.
Step 6  turn_right      not_determined: Traffic hides the distant lane end and any lane-use arrow that would
                        decide this movement.
Step 6  u_turn          not_determined: Traffic hides the distant lane end and any marking that would decide
                        this movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within the lane and do not cross the solid boundary into the hatched strip. A
                        leftward lane change is permitted by the broken line when safe; confirm lane-use
                        arrows and junction controls before choosing a turning movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1320, 25.68 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight toward distant overhead lane-control
                        signs. My car is in the rightmost of four same-direction lanes, with variable-lane
                        pavement markings and a curb on the right; no intersection stop line is clearly
                        visible. (lanes 4, mine 4, full)
Step 2  Left            A continuous white line with repeated short diagonal teeth separates my lane from
                        another same-direction lane on the left; there is no curb on this boundary.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A continuous white line with repeated diagonal teeth runs along the right side of my
                        lane beside a raised curb, with landscaping and a sidewalk beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): White Chinese characters reading 可变车道 are painted lengthwise in my
                        lane; no complete pavement direction arrow is clearly readable.
Step 4  Cross-check     position: The rightmost position agrees with a special-lane separator on the left and
                        a curbed roadway edge on the right. | roles: The white toothed boundary treatment and
                        可变车道 text agree with variable-lane operation; the right boundary also follows the
                        physical road edge. | markings: The variable-lane text agrees with the toothed
                        boundary treatment. No readable pavement arrow, STOP marking, or waiting area is
                        visible. | unseen: No permitted turning direction is inferred from the lane's position
                        or its variable-lane text; the distant lane-end layout is unresolved. | result:
                        consistent
Step 5  Rule            left_boundary: In China, the solid toothed boundary of a variable lane must not be
                        crossed to change lanes.
Step 5  Rule            right_boundary: The curbed road edge is not a permissible route for leaving this lane.
Step 5  Rule            text:other: 可变车道 identifies a variable-use lane whose current operation must be
                        checked against lane-control indications, but the text itself does not specify a
                        turning movement.
Step 6  change_left     prohibited (contested, label allowed): The solid toothed variable-lane boundary
                        prohibits crossing to the left.
Step 6  change_right    prohibited (correct): The raised curb prevents a permissible move out of the lane to
                        the right.
Step 6  go_straight     allowed (contested, correct): No readable pavement arrow restricts continuing straight
                        along this lane.
Step 6  turn_left       not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay within the toothed boundaries and do not cross toward the curb. Check the
                        overhead controls for the variable lane's current permitted use; the pavement text
                        alone does not authorize a turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1101, 22.21 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban multilane road in China approaches a signal-controlled intersection with a
                        pedestrian crossing. My car is behind the pale green car in a through lane; vehicles
                        obscure some of the lanes farther left. (lanes None, mine None, insufficient)
Step 2  Left            A continuous white line borders my lane on the left, with repeated short white
                        transverse teeth on its far side; another same-direction traffic lane lies beyond,
                        with no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from the same-direction lane occupied by the
                        coach on the right; no curb forms this lane boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has one head pointing straight
                        ahead.; line:stop_line (partial): A white transverse stop line is visible near the
                        intersection, but the car ahead hides its middle portion across my lane.;
                        line:crosswalk (partial): White pedestrian-crossing stripes extend across the road
                        ahead; the car ahead obscures the portion directly in front of my lane.
Step 4  Cross-check     position: Same-direction lanes are visible on both sides, consistent with both
                        boundaries being lane lines; occlusion prevents confidently counting all lanes or
                        assigning an exact index. | roles: The white solid lines fit same-direction lane
                        separators on an intersection approach; the teeth beside the left line do not make
                        that continuous line dashed. | markings: The straight-only arrow agrees with a through
                        lane bounded by solid approach lane lines; the stop line and crossing are compatible
                        with the intersection ahead. | unseen: No markings hidden beneath the vehicles are
                        inferred, and the total lane count and exact lane index are left unknown. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by traffic
                        control, but does not itself impose an unconditional stop.
Step 5  Rule            line:crosswalk: The crosswalk requires attention and yielding to pedestrians, without
                        changing the lane's permitted directions.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The straight-only arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible marked waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane when traffic control and the crossing are clear; do
                        not cross either solid lane boundary. For a turn, select an appropriately marked lane
                        before the solid-line section, and stop before the stop line whenever required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1149, 20.9 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           The car is in a single motor-vehicle lane on a separated urban carriageway approaching
                        a signal-controlled intersection. A planted divider separates it from the wider
                        roadway on the left, and a bicycle lane runs along the right. (lanes 1, mine 1, full)
Step 2  Left            A continuous solid white line follows a raised planted divider on the left, with a
                        separate roadway beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from the paved strip occupied by
                        cyclists on the right; the sidewalk curb is beyond that strip, not at my lane
                        boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow with a single forward-pointing head is clearly
                        visible in the lane behind the vehicle transporter.
Step 4  Cross-check     position: One motor-vehicle lane on this separated carriageway agrees with roadway-
                        edge boundaries on both sides; the cyclist strip is not another motor-vehicle lane. |
                        roles: The white solid lines fit the edges of the motor-vehicle carriageway, with a
                        raised divider on the left and a non-motorized lane on the right. | markings: The
                        straight-only arrow is consistent with this through lane; no conflicting guidance
                        marking is visible. | unseen: The transporter obscures the farther lane surface, so no
                        hidden stop line, crosswalk, or additional marking is asserted. | result: consistent
Step 5  Rule            left_boundary: The raised divider and solid white roadway edge must not be crossed to
                        leave this lane on the left.
Step 5  Rule            right_boundary: The solid white separation from the non-motorized lane prohibits
                        moving across it into that lane.
Step 5  Rule            arrow:straight: In China, this lane-use arrow requires proceeding straight at the
                        intersection rather than turning left, turning right, or making a U-turn.
Step 6  change_left     prohibited (correct): The raised divider and solid left edge prohibit crossing to the
                        left.
Step 6  change_right    prohibited (correct): The solid boundary to the non-motorized lane prohibits crossing
                        to the right.
Step 6  go_straight     allowed (correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to continue straight, without crossing either boundary or entering
                        the cyclists' lane. Obey the traffic signal and leave space behind the transporter;
                        any stopping position farther ahead is obscured.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 942, 16.73 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow, two-way urban street in China continues straight between residential
                        buildings. My car is in the single motor-vehicle lane in its direction, with opposing
                        traffic on the left and a narrow roadside strip on the right; the next intersection is
                        not clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line separates my lane from oncoming scooters and opposing
                        traffic, with no curb along the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single broken white line, with visible painted lengths and intervening gaps,
                        separates my lane from a narrow roadside strip; the raised sidewalk curb is beyond
                        that strip rather than on the line.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane in my direction agrees with a center line on the left
                        and an edge line on the right; the narrow roadside strip is not counted as another
                        motor-vehicle lane. | roles: The solid yellow center line separates opposing
                        directions, and the broken white edge line separates the motor-vehicle lane from the
                        roadside strip. | markings: No readable arrows, words, symbols, transverse lines or
                        waiting areas are visible in my lane. | unseen: The leading vehicle hides some
                        pavement, and distant markings cannot be resolved; no markings have been inferred in
                        those areas. | result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing into the
                        opposing side for a lane change or overtaking.
Step 5  Rule            right_boundary: A broken white roadway edge line may be crossed when necessary and
                        safe, but does not turn the roadside strip into a normal motor-vehicle travel lane.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing to the left.
Step 6  change_right    allowed (correct): The broken white edge line permits crossing when necessary and
                        safe.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: each boundary governs only crossing on its own side, and the absence of
                        visible movement markings does not establish permission for turns at an unseen
                        intersection.
Advice                  Continue in the motor-vehicle lane without crossing the solid yellow center line,
                        allowing space for scooters and pedestrians. Cross the broken white edge only when
                        necessary and safe; reassess turn guidance and stopping requirements when the next
                        intersection becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 904, 17.08 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches a signal-controlled intersection. The car is
                        in the rightmost of three lanes travelling in this direction, beside a raised
                        sidewalk. (lanes 3, mine 3, full)
Step 2  Left            A continuous white line separates this lane from the same-direction lane containing
                        the white sedan; no curb is present on this side.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white edge marking runs alongside a raised curb, with a paved sidewalk
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow ahead has a forward-pointing head and a straight
                        stem.; line:stop_line (partial): A faint transverse white line appears across the lane
                        before the pedestrian crossing; its outline is indistinct at this distance.;
                        line:crosswalk (partial): White pedestrian-crossing stripes extend across the road
                        ahead, including this lane.
Step 4  Cross-check     position: Three same-direction lanes and position 3 agree with a lane divider on the
                        left and the roadway edge on the right. | roles: The solid white left divider fits an
                        intersection-approach lane line; the white line beside the right curb fits a roadway
                        edge. | markings: The straight arrow is compatible with this through lane; the
                        transverse markings identify the intersection approach without adding turning
                        permissions. | unseen: The distant stop line and crosswalk are not sharply resolved,
                        so their evidence is partial; no hidden arrow heads or waiting areas are inferred. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes in the visible approach.
Step 5  Rule            right_boundary: The raised curb forms a physical roadway edge and prohibits moving out
                        of this lane onto the sidewalk.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal,
                        but does not itself impose an unconditional stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires respecting pedestrian priority and
                        keeping the crossing clear.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white lane divider prohibits crossing
                        into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label not_determined): The raised curb prohibits moving onto the
                        sidewalk.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits this movement.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane for straight travel; do not cross the solid left divider or turn
                        from this lane. The visible signal is red: stop before the stop line and keep the
                        pedestrian crossing clear.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:crosswalk', 'line:stop_line'], missed []), actions False,
                        unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1250, 22.56 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches a signal-controlled intersection with a
                        pedestrian crossing. My car is in the rightmost of three same-direction lanes, beside
                        a raised island on the right. (lanes 3, mine 3, full)
Step 2  Left            A single solid white line separates my lane from the same-direction lane occupied by
                        the white car on the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs beside a raised paved island and curb on the right.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible in my lane;
                        its lower shaft is obscured by the hood.; line:stop_line (full): A solid white
                        transverse stop line crosses my lane before the pedestrian crossing.; line:crosswalk
                        (full): White zebra-crossing stripes extend across my lane beyond the stop line.
Step 4  Cross-check     position: The rightmost lane position agrees with a same-direction lane line on the
                        left and a roadway edge beside a raised island on the right. | roles: The solid white
                        lane divider and solid white edge marking fit their observed roles. | markings: The
                        visible straight arrow is consistent with the lane continuing across the intersection;
                        the stop line precedes the crosswalk. | unseen: The lower portion of the arrow is
                        hidden by the hood; no additional arrowhead or marking is inferred there. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes.
Step 5  Rule            right_boundary: The roadway edge and raised curb do not permit leaving the lane across
                        this side.
Step 5  Rule            arrow:straight: A straight-ahead lane-use arrow requires proceeding straight rather
                        than turning left, right, or making a U-turn.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the traffic
                        signal, but does not itself require an unconditional stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires attention to pedestrians and yielding
                        or stopping as required, without assigning a turning movement.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white lane divider prohibits
                        crossing into the lane on the left.
Step 6  change_right    prohibited (WRONG, label not_determined): The right roadway edge is bounded by a
                        raised curb, prohibiting a move across it.
Step 6  go_straight     allowed (correct): The visible straight-ahead arrow permits continuing straight.
Step 6  turn_left       prohibited (correct): The straight-ahead lane-use arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-ahead lane-use arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-ahead lane-use arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight; do not cross the solid left divider or the
                        right curb. Obey the applicable vehicle signal, stop before the stop line when
                        required, and yield to pedestrians at the crossing.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1191, 20.57 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow two-way urban street with one travel lane in each direction and parked cars
                        along both sides. My car is following a bus; no intersection or lane ending is
                        visible. (lanes 1, mine 1, full)
Step 2  Left            A single continuous yellow line runs along the left of my lane, with opposing traffic
                        beyond it; no curb forms this boundary.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single continuous white line runs along the right of my lane, with a roadside
                        parking strip and a raised sidewalk farther beyond it; the curb does not directly
                        bound my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on the left and white roadway edge line on the right
                        agree with one travel lane in my direction and my lane being lane 1. | roles: The
                        solid yellow line separates opposing directions; the solid white line separates the
                        travel lane from the roadside strip. | markings: No guidance markings are visible
                        within the exposed portion of my lane. | unseen: The bus hides the road immediately
                        ahead, and the next intersection is not visible; no markings beneath or beyond the bus
                        are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing into the
                        opposing side for a lane change or overtaking.
Step 5  Rule            right_boundary: The solid white roadway edge line prohibits crossing out of the travel
                        lane in the visible stretch.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing to the opposing
                        side.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits crossing into the roadside
                        strip.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_determined: No visible marking governs this movement; the next intersection and
                        any approach arrows are hidden.
Step 6  turn_right      not_determined: No visible marking governs this movement; the next intersection and
                        any approach arrows are hidden.
Step 6  u_turn          not_determined: No visible marking governs this movement; the next intersection and
                        any approach markings are hidden.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the boundaries govern crossing only, straight travel remains allowed, and
                        intersection turns remain undecided because their governing markings are not visible.
Advice                  Continue within the two solid boundaries and leave sufficient space behind the bus. Do
                        not cross either boundary; reassess turn guidance when the road ahead becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 861, 16.17 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A narrow, single-lane urban ramp continues downhill between concrete barriers. My car
                        occupies its only lane; no intersection or lane ending is clearly visible ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A continuous pale white line, tinted green by the image, runs beside a concrete
                        barrier with a metal screen; no adjacent drivable lane lies across it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line runs beside a raised concrete barrier topped by railings, with a
                        separated walkway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Road edges and physical barriers on both sides agree with one lane and ego
                        lane index 1. | roles: The solid white lines beside the barriers fit roadway edge
                        lines, not lane dividers or a centre line. | markings: No arrows, words, symbols,
                        transverse lines or waiting areas are visible in my lane. | unseen: No markings or
                        junction arrangement are inferred beyond the visible stretch. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and concrete barrier do not permit leaving the
                        lane to the left.
Step 5  Rule            right_boundary: The solid roadway edge and raised barrier do not permit leaving the
                        lane to the right.
Step 6  change_left     prohibited (correct): The left roadway edge is bounded by a concrete barrier and
                        cannot be crossed.
Step 6  change_right    prohibited (correct): The right roadway edge is bounded by a raised concrete barrier
                        and cannot be crossed.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Continue within this narrow lane and keep clear of both barriers; moving out to either
                        side is prohibited. Reassess the signs and markings as the road ahead becomes clearer.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 737, 14.36 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues straight ahead, with a pedestrian crossing
                        visible in the distance. My car is in the rightmost of two motor-vehicle lanes, beside
                        a bicycle lane. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another
                        motor-vehicle lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white line is solid beside the red bicycle-lane surface in the foreground and broken
                        farther ahead; a bicycle symbol lies beyond it, and there is no curb at the line
                        itself.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (full): White pedestrian-crossing bars extend across my lane farther
                        ahead.
Step 4  Cross-check     position: Two motor-vehicle lanes, a lane divider on my left, and a bicycle-lane edge
                        on my right agree with my position as lane 2. | roles: The broken white left line
                        separates same-direction lanes; the white right line separates the motor roadway from
                        a bicycle lane. | markings: The crossing is compatible with both boundaries; no
                        directional arrow is visible in my lane, and the bicycle symbol belongs to the
                        adjacent bicycle lane. | unseen: No hidden arrows, stop lines, or waiting areas have
                        been inferred; the right boundary's change from solid to broken is explicitly noted. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits changing into the
                        adjacent motor-vehicle lane when safe.
Step 5  Rule            right_boundary: The solid white motor-roadway edge must not be crossed here, and its
                        broken continuation does not authorize ordinary driving in the adjacent bicycle lane.
Step 5  Rule            line:crosswalk: Approach the pedestrian crossing slowly and stop to yield to
                        pedestrians using it.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (correct): The solid white edge beside my car prohibits crossing into the
                        bicycle lane.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow restricts continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken divider when safe; do
                        not cross the solid right edge into the bicycle lane. Slow for the pedestrian crossing
                        and stop before it when necessary to yield.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1076, 23.2 s
```
