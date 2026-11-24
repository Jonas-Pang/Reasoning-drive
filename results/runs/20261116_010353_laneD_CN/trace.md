# Reasoning of lane run 20261116_010353_laneD_CN

```text
mapdr__BusLane_082905737c59400ab39b52f935ca913d_1711845479559752000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        writing and road layout. My car is in the middle of three same-direction lanes on a
                        divided urban road approaching a distant intersection; the rightmost lane appears
                        reserved for buses. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken yellow line, with long dashes and gaps, separates my lane from a right-hand
                        lane bearing bus-related Chinese road text; there is no curb at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three lanes agrees with a general traffic lane on
                        the left and a reserved lane on the right. | roles: The broken white line fits an
                        ordinary lane divider; the broken yellow line and bus-related context fit a reserved-
                        lane boundary rather than a center line. | markings: No guidance marking is readable
                        in my own lane; the visible road text belongs to the lane on the right. | unseen: No
                        distant lane-use arrow or intersection stop line has been inferred; the intersection
                        approach is too distant to resolve completely. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits changing to the adjacent
                        general traffic lane when safe.
Step 5  Rule            right_boundary: The broken reserved-lane boundary does not authorize an ordinary car
                        to enter the bus lane during its reserved operation, which is treated as applicable
                        here.
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane divider permits crossing into
                        the adjacent general traffic lane when safe.
Step 6  change_right    prohibited (WRONG, label not_determined): The adjacent bus lane is treated as
                        reserved, so an ordinary car must not enter it.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_determined: Any lane-use marking governing a left turn at the distant intersection
                        cannot be resolved.
Step 6  turn_right      not_determined: Any lane-use marking governing a right turn at the distant
                        intersection cannot be resolved.
Step 6  u_turn          not_determined: Any marking governing a U-turn at the distant intersection cannot be
                        resolved.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: lane changes follow their respective boundary rules, continuing straight
                        is unrestricted by visible markings, and intersection turns remain undecided because
                        the distant approach markings are unresolved.
Advice                  Continue in this lane, or change left across the broken white line when safe; do not
                        enter the bus lane on the right. Before making any turn, confirm the lane arrows and
                        signals closer to the intersection and stop at its stop line if required.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6424, out 918, 14.83 s

mapdr__BusLane_0cdea530a3c24022b22a7320ad2e4818_1711619299216507000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely China, with traffic keeping right, judging from the road layout, median
                        fencing and blue overhead lane-direction sign. My car is in the middle of three same-
                        direction lanes on a divided urban road approaching a distant signalized intersection;
                        the rightmost lane appears to be a reserved lane. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb borders my lane here.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broad broken yellow line, with several visible dashes and gaps, separates my lane
                        from a paved lane on the right; the raised roadside curb is beyond that lane, not at
                        this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible at the bottom
                        of my lane, but its shaft and lower portion are hidden by the dashboard.
Step 4  Cross-check     position: The middle position agrees with a same-direction lane on the left and an
                        additional, apparently reserved lane on the right. | roles: The broken white line fits
                        an ordinary lane divider; the broad broken yellow line is consistent with a Chinese
                        reserved-lane boundary rather than a centre line. | markings: The visible forward
                        arrowhead agrees with continuing along this lane; its hidden lower portion prevents
                        confirming whether it also has a turning branch. | unseen: No reserved-lane wording or
                        operating hours can be read, and no stop line or crosswalk can be resolved at the
                        distant intersection. The arrow's hidden portion has not been assumed to lack
                        branches. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        changing into the adjacent ordinary lane when safe.
Step 5  Rule            right_boundary: The yellow broken reserved-lane boundary does not authorize an
                        ordinary car to enter the reserved lane when its eligibility and operating hours are
                        unknown.
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but the hidden
                        remainder prevents establishing whether additional movements are permitted.
Step 6  change_left     allowed (correct): The broken white ordinary lane divider permits crossing when safe.
Step 6  change_right    prohibited (WRONG, label not_determined): The right boundary leads into an apparently
                        reserved lane, which must be treated as reserved for this ordinary car.
Step 6  go_straight     allowed (contested, correct): The visible forward arrowhead permits proceeding
                        straight.
Step 6  turn_left       not_determined: The lower portion of the lane-use arrow is hidden, so a possible left
                        branch cannot be checked.
Step 6  turn_right      not_determined: The lower portion of the lane-use arrow is hidden, so a possible right
                        branch cannot be checked.
Step 6  u_turn          not_determined: The partly hidden arrow does not establish whether a U-turn movement
                        is included.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or cross the broken white line to the left only when
                        safe; do not enter the apparent reserved lane on the right. Before turning, confirm
                        the complete lane arrows farther ahead and obey the intersection signals and any stop
                        line as they become visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 6424, out 1124, 15.63 s

mapdr__BusLane_15514670dcde4a41bd9bfa135d4c4c2f_1711768724703636000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        signs, blue plates and traffic arrangement. My car is in the middle of three same-
                        direction lanes on a divided urban road; the road continues ahead, with a signed bus
                        lane on the right. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with a long dash and a visible gap, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with a long foreground dash and a gap ahead, separates my lane
                        from the right-hand lane indicated by the roadside bus-lane sign; there is no curb at
                        this boundary.
                        white dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position in three lanes agrees with a same-direction lane on the
                        left and a special same-direction lane on the right. | roles: Broken white paint is
                        consistent with both the ordinary lane divider and the boundary of the signed bus
                        lane. | markings: No guidance marking is readable within my lane; the visible paint
                        farther right belongs to the adjacent lane. | unseen: No hidden arrow or distant
                        intersection marking has been inferred; the car ahead obscures part of the lane
                        surface. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe.
Step 5  Rule            right_boundary: Although the broken line can be crossed by eligible traffic, an
                        ordinary car must not enter the adjacent reserved bus lane under the reserved-lane
                        assumption.
Step 6  change_left     allowed (correct): The broken white ordinary lane divider permits a safe lane change
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): The adjacent lane is signed as a reserved bus lane,
                        so entry by this ordinary car is prohibited.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left only after checking traffic; do not
                        enter the bus lane on the right. The bus sign displays 6:00–22:00, and turn-lane
                        guidance at the next intersection is not yet visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 853, 10.54 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790652568285000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese writing, blue vehicle plates
                        and road infrastructure; traffic keeps right. My car is in the leftmost lane of a
                        three-lane divided urban road, continuing straight beside an elevated structure, with
                        no intersection or lane end visible. (lanes 3, mine 1, full)
Step 2  Left            A solid white line runs beside a raised concrete divider topped by a metal fence, with
                        opposing traffic beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and intervening gaps, separates my lane
                        from another same-direction lane; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the same-direction lane on the right agree with my
                        lane being the leftmost of three lanes. | roles: The solid white line beside the
                        physical median is an edge line, not a painted center line; the broken white line on
                        the right is a lane divider. | markings: No guidance markings are visible within my
                        lane; the irregular pale streak on the pavement is not a readable guidance marking. |
                        unseen: No intersection layout or distant lane-use markings have been inferred beyond
                        the visible stretch. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised median prohibit leaving my lane
                        across the left boundary.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits changing into the
                        adjacent ordinary lane when safe without obstructing other traffic.
Step 6  change_left     prohibited (correct): The solid left edge and physical median prohibit crossing to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and no lane end
                        is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right only after checking mirrors, blind
                        spots and traffic gaps. Do not cross the left median; choose a turning lane only when
                        an actual junction and its guidance become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 840, 10.77 s

mapdr__BusLane_1af9cc80e9dd41bda208c413b4d7dd6e_1711790656568323000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese writing and road environment,
                        with traffic keeping right. My car is in the leftmost of three same-direction lanes on
                        a divided urban road beside an elevated structure; no intersection or lane ending is
                        visible ahead. (lanes 3, mine 1, partial)
Step 2  Left            A continuous white solid line runs beside a raised concrete edge topped by a metal
                        fence, with a separated paved area beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments separated by clear gaps divide my lane from the same-
                        direction lane occupied by the white SUV.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider place my car in the leftmost
                        lane; three lanes appear present, although the outer-right roadway is partly obscured
                        by vehicles and the image edge. | roles: The solid white line beside the physical
                        divider fits an edge line, and the broken white line between same-direction vehicles
                        fits a lane line. | markings: No arrows, words, symbols, waiting areas or transverse
                        markings are visible in my lane; the irregular pale streaks appear to be pavement
                        repairs rather than guidance markings. | unseen: The next intersection and its lane-
                        use controls are not visible; no attributes have been assigned to them. | result:
                        consistent
Step 5  Rule            left_boundary: The roadway edge and raised fenced divider do not permit my car to move
                        left across this boundary.
Step 5  Rule            right_boundary: In China, a broken white same-direction lane divider permits changing
                        lanes when safe without interfering with other traffic.
Step 6  change_left     prohibited (correct): The raised fenced roadway edge prohibits crossing to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a rightward lane change when
                        safe.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or lane ending restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action in the visible stretch.
Step 6  turn_right      not_applicable: No marking governs this action in the visible stretch.
Step 6  u_turn          not_applicable: No marking governs this action in the visible stretch.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not cross the fenced left edge. A rightward lane
                        change is permitted by the markings, but wait for a safe gap around the SUV; turn-lane
                        choices must be checked when intersection markings come into view.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 913, 15.7 s

mapdr__BusLane_1bc12c43c65140b49aa35fae20bada91_1711352278937239000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        storefront lettering, blue license plates and traffic arrangement. My car is in the
                        middle of three same-direction lanes on a divided urban street; traffic continues
                        ahead, but no intersection or lane end is clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with a visible foreground dash and a gap before the next dash,
                        separates my lane from another traffic lane beside the planted median; no curb forms
                        my lane's immediate left boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with a foreground dash and a visible gap, separates my lane from
                        the lane occupied by scooters and cars on the right; traffic obscures portions farther
                        ahead, and no curb forms this immediate boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane line
                        on each side. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No readable arrow, word, symbol, transverse line or waiting area
                        is visible in my lane. | unseen: No markings beneath the vehicles or beyond the
                        visible stretch are inferred; the next intersection's lane-use markings cannot be
                        assessed. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese road-marking rules, a broken white lane divider
                        may be crossed to change lanes when safe without obstructing other traffic.
Step 5  Rule            right_boundary: Under mainland Chinese road-marking rules, a broken white lane divider
                        may be crossed to change lanes when safe without obstructing other traffic.
Step 6  change_left     allowed (correct): The broken white left lane divider permits crossing when safe.
Step 6  change_right    allowed (correct): The broken white right lane divider permits crossing when safe.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: lane-change permissions follow the broken dividers, and no intersection-
                        turn permission is inferred from the boundaries or unseen markings.
Advice                  Continue in the middle lane; either broken divider permits a lane change only after
                        checking traffic, especially the scooters on the right. Choose a turning lane only
                        after the next intersection's markings and controls become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 868, 12.15 s

mapdr__BusLane_27b8601f20dd4bd487a2eae8f21cea1c_1709518351221799000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, with right-hand traffic, based on the Chinese road lettering,
                        streetscape and traffic arrangement. My car is in the middle of three same-direction
                        lanes on a divided urban road approaching a pedestrian overpass; the rightmost lane
                        appears reserved for buses. (lanes 3, mine 2, full)
Step 2  Left            A single broken white line, with visible dashes and gaps, separates my lane from
                        another general-traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single broken yellow line, with long dashes and gaps, separates my lane from a lane
                        bearing white Chinese lettering and time numerals consistent with a bus lane; there is
                        no curb at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The white lane line on my left and reserved-lane boundary on my right agree
                        with my position as lane 2 of 3. | roles: The broken white line fits an ordinary lane
                        divider; the broken yellow line and adjacent bus-lane lettering support a special-lane
                        boundary rather than a center line. | markings: No guidance marking is discernible
                        within my own lane; the lettering and time numerals belong to the lane on the right. |
                        unseen: The car ahead hides part of my lane and distant pavement cannot be read; no
                        hidden arrows or intersection markings are assumed. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing to
                        change lanes when safe.
Step 5  Rule            right_boundary: Although the yellow boundary is broken, an ordinary car must not enter
                        the adjacent reserved bus lane under the reserved-lane assumption.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (contested, correct): The adjacent lane is reserved for buses, so its
                        special-lane restriction prohibits entry by my ordinary car.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken white line after checking
                        traffic; do not enter the reserved lane on the right. No turn guidance or stopping
                        point is visible for your lane, so reassess as the road ahead becomes clearer.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 863, 16.84 s

mapdr__BusLane_27f7c53a5d4a4bd3832faf7b6e2a632a_1711670013574098000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        vehicle lettering, plates and road layout. My car is in the middle of three same-
                        direction lanes on an urban road beside an elevated roadway; the road continues ahead,
                        with no clear intersection or lane ending visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        lane containing the dark estate car on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the lane containing the white car on the
                        right; successive painted stretches and gaps are visible ahead, with no curb at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position in three lanes agrees with a same-direction lane across
                        each boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No readable lane-use arrows, words, symbols, transverse lines or
                        waiting areas are visible in my lane. | unseen: No movement restriction is inferred
                        from distant or vehicle-obscured pavement; the next intersection is not visible. |
                        result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider may be crossed to change
                        lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In mainland China, a broken white lane divider may be crossed to
                        change lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the boundary permissions govern lane changes only, and no intersection-
                        turn permission is inferred from them.
Advice                  Continue straight in this lane; either broken divider permits a lane change only after
                        checking for a safe gap, especially beside the white car on the right. Follow the lane
                        arrows and controls when an intersection comes into view; this image establishes no
                        turning lane or stopping point.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 850, 9.59 s

mapdr__BusLane_318cb11d50954093bb129118b8bd2ca4_1711600837938350000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be Beijing, China, with traffic keeping right, based on the skyline
                        and road layout. My car is in the middle of three same-direction lanes on a divided
                        urban expressway approaching an overpass. (lanes 3, mine 2, full)
Step 2  Left            A yellow broken line, with several visible dashes and gaps, separates my lane from a
                        lane on the left containing partially visible white pavement markings; no curb forms
                        this boundary.
                        yellow dashed, curb no, special_lane_line, evidence partial
Step 2  Right           A white broken line, with clear long dashes and gaps, separates my lane from another
                        traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lanes visible on both sides agree with my position as lane 2 of 3. |
                        roles: The white broken right boundary fits an ordinary lane divider. The yellow
                        broken left boundary suggests a Chinese reserved-lane boundary, but the adjacent
                        lane's pavement text is not readable enough to confirm its designation. | markings: No
                        guidance marking is readable within my lane. The white markings to the left and the
                        hatched area farther right are outside it. | unseen: The left lane's precise
                        reservation and operating times cannot be read; its special-lane classification
                        remains tentative. | result: Consistent, with uncertainty retained about the left
                        lane's designation.
Step 5  Rule            left_boundary: In China, a broken yellow reserved-lane boundary permits crossing only
                        when eligible to enter that lane; an ordinary car must not enter an operating reserved
                        lane.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent lane
                        when safe.
Step 6  change_left     not_determined (contested, label prohibited): The yellow broken boundary appears to
                        border a reserved lane, but its designation is not sufficiently readable to determine
                        entry permission.
Step 6  change_right    allowed (correct): The white broken lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow or other marking in my lane restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: leftward entry remains undecided because the possible reserved-lane
                        designation is unconfirmed, and markings outside my lane do not govern its forward
                        movements.
Advice                  Continue straight in this lane; a rightward lane change is permitted by the broken
                        white line when safe. Avoid entering the apparent reserved lane on the left until its
                        designation and eligibility requirements are confirmed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1116, 26.41 s

mapdr__BusLane_3f63f9a1c884494d9788a8041542d427_1711167006977722000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        streetscape, registration plates and timed bus-lane signage. My car is in the middle
                        of three same-direction lanes on a divided urban road; the road continues ahead, but
                        the next intersection is not clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken yellow line, with visible dashes and gaps, separates my lane from the right-
                        hand lane bearing large painted characters and a timed bus-lane sign; there is no curb
                        at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle lane of three has an ordinary traffic lane to its left and a
                        reserved lane to its right, consistent with the observed boundaries. | roles: The
                        broken white line fits an ordinary lane divider; the broken yellow line and adjacent
                        bus-lane context fit a special-lane boundary. | markings: No guidance marking is
                        visible within my lane; the large painted characters to the right belong to the
                        adjacent lane. | unseen: No arrow, stop line or waiting area is identifiable in my
                        lane; distant pavement and parts obscured by vehicles cannot be inspected fully. |
                        result: consistent
Step 5  Rule            left_boundary: A broken white lane divider permits changing into the adjacent ordinary
                        lane when safe.
Step 5  Rule            right_boundary: The adjacent bus lane is treated as reserved for this ordinary car, so
                        entering it is prohibited despite its broken boundary.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing into the ordinary
                        lane when safe.
Step 6  change_right    prohibited (contested, correct): The right boundary leads into a reserved bus lane,
                        which this ordinary car must not enter.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken white line when safe; do not
                        enter the reserved lane on the right. The bus-lane sign shows timed restrictions, and
                        the next junction's movement markings are not yet readable.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 858, 15.81 s

mapdr__BusLane_413817bcf2784b99aa6b7ece511bfe01_1709887687980147000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese writing, road
                        markings and opposing traffic to the left of the median fence. My car is in the
                        leftmost of three same-direction lanes on an urban road; glare and vehicles obscure
                        the distant road layout. (lanes 3, mine 1, partial)
Step 2  Left            A metal median fence on a raised base runs along the left, with opposing traffic
                        beyond; strong glare prevents reliable identification of paint alongside its base.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A white broken line, with a visible long dash and intervening gap, separates my lane
                        from another same-direction lane on the right; there is no curb here.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and same-direction lane divider on the right
                        agree with my lane being leftmost; the apparent third lane lies farther right. |
                        roles: The physical median forms the roadway edge, while the broken white line fits a
                        same-direction lane divider. | markings: No guidance marking is readable within my
                        lane; markings farther right belong to other lanes. | unseen: No arrow or distant
                        junction marking is inferred beneath the vehicle ahead or through the glare; paint at
                        the median base remains unreadable. | result: consistent
Step 5  Rule            left_boundary: In China, a raised median and separating fence must not be crossed to
                        leave the lane.
Step 5  Rule            right_boundary: A broken white same-direction lane divider may be crossed to change
                        lanes when safe and without interfering with other traffic.
Step 6  change_left     prohibited (correct): The physical median fence and raised base prohibit crossing the
                        left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change one lane right across the broken white line only when
                        safe; do not cross the median. Reduce speed for the glare and traffic ahead, and
                        confirm junction arrows and any reserved-lane restrictions before positioning for a
                        turn.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 939, 15.27 s

mapdr__BusLane_93157115d08543f2bf77126674d5e284_1710305343884150000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely China, with traffic keeping right, based on the Chinese signs and road
                        layout. My car is in the leftmost of three same-direction lanes on a divided
                        expressway approaching an overpass; a sign indicates a timed bus-lane restriction for
                        this lane. (lanes 3, mine 1, full)
Step 2  Left            A continuous white line borders the lane on the left, with yellow broken segments
                        immediately alongside it on the lane side; a narrow paved strip and concrete median
                        barrier lie beyond.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A yellow broken line, with several clearly visible dashes and gaps, separates my lane
                        from the adjacent same-direction lane on the right; there is no curb.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the adjacent lane to the right agree with my lane
                        being lane 1 of three. | roles: The solid white line fits a roadway edge; the yellow
                        broken right boundary and timed bus-lane sign support a special-lane boundary rather
                        than a center line. | markings: No readable arrows, words, symbols, transverse lines
                        or waiting areas are visible in my lane. | unseen: No bus word or lane-use arrow is
                        inferred from the sign; the lane's eventual end is outside the visible stretch. |
                        result: consistent
Step 5  Rule            left_boundary: Under Chinese marking rules, the solid white roadway edge prohibits
                        crossing onto the strip beside the median in ordinary driving.
Step 5  Rule            right_boundary: The broken boundary permits leaving this special lane to the right
                        when safe; the bus-lane reservation does not itself prohibit exiting it.
Step 6  change_left     prohibited (contested, correct): The solid white roadway edge prohibits crossing to
                        the median-side strip.
Step 6  change_right    allowed (WRONG, label prohibited): The broken special-lane boundary permits leaving
                        the lane to the right when safe.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  The sign indicates a bus-lane restriction on working days from 17:00 to 19:00; an
                        ordinary car should use a general lane during those hours, moving right across the
                        broken boundary when safe. Do not cross the solid left edge; no stop location or
                        turning guidance is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6424, out 1017, 23.7 s

mapdr__BusLane_98cd173888e8492cb807ed54a72ee3d7_1710809843204902000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        bus-lane sign and road layout. My car is in the middle of three same-direction lanes
                        on a divided urban road approaching a pedestrian bridge and a bus stop; no
                        intersection or lane ending is clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken line separates my lane from the right-hand bus lane, appearing white in the
                        nearest visible dash and yellow farther ahead; dashes and gaps are visible, and there
                        is no curb at this boundary.
                        white dashed, curb no, special_lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three lanes agrees with a general traffic lane on
                        the left and a bus lane on the right. | roles: The broken white left boundary fits a
                        lane divider; the right boundary separates a bus lane, although its paint colour is
                        not uniform in the image. | markings: No guidance markings are visible inside my lane;
                        the bus-lane lettering lies to its right. | unseen: No unseen arrows or intersection
                        controls are inferred; uncertainty about the right boundary's colour is retained. |
                        result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing to
                        change lanes when safe.
Step 5  Rule            right_boundary: The adjacent lane is a reserved bus lane, so an ordinary car must not
                        enter it under the reserved-lane interpretation, despite the broken boundary.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (contested, correct): The adjacent bus lane is treated as reserved for
                        eligible vehicles.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken line only when safe; do not
                        enter the bus lane on the right. The roadside sign indicates timed bus-lane operation,
                        but no visible junction markings establish which lane to use for turns.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 935, 13.75 s

mapdr__BusLane_9a6818a05d6d43708d1fb1d1a7ffa3e8_1711693892899118000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, with traffic keeping right, based on the simplified Chinese
                        signs and road layout. My car is in a single motor-vehicle lane on a separated branch
                        curving right, with the main carriageway to the left and a bicycle/scooter strip to
                        the right; the next junction is not visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous white line borders a white diagonally hatched wedge on the left, then
                        follows a raised landscaped island; yellow rectangular paint marks appear alongside
                        the lane edge.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line curves ahead on the right, with spaced yellow rectangular
                        paint marks on its lane-facing side and a strip used by bicycles and scooters beyond;
                        the sidewalk curb is beyond that strip.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edges rather than dividers between ordinary
                        motor lanes, consistent with one motor lane on this separated branch. | roles: The
                        continuous white lines fit the edges of the motor-vehicle lane beside an island and a
                        non-motorized strip. | markings: No lane-use arrow, word, transverse line or waiting
                        area is visible inside my lane. The white hatching is outside its left boundary; the
                        arrows on the blue sign are not pavement markings. | unseen: No movement arrow or
                        junction layout is inferred beyond the visible stretch. The yellow edge rectangles are
                        observed but not assigned an unsupported guidance meaning. | result: consistent
Step 5  Rule            left_boundary: Under the likely Chinese rules, the solid channelizing edge and raised
                        island are not to be crossed to leave this lane.
Step 5  Rule            right_boundary: Under the likely Chinese rules, the solid boundary separating the
                        motor lane from the non-motorized strip must not be crossed for an ordinary lane
                        change.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid channelizing edge and raised
                        island prohibit leaving the lane to the left.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid boundary to the non-motorized
                        strip prohibits leaving the lane to the right.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing along the lane,
                        including its curve.
Step 6  turn_left       not_applicable: No visible pavement marking governs this movement.
Step 6  turn_right      not_applicable: No visible pavement marking governs this movement; the roadside sign
                        is context only.
Step 6  u_turn          not_applicable: No visible pavement marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary restrictions govern only lateral departures, and the roadside
                        arrows have not been treated as pavement markings.
Advice                  Stay between the solid white boundaries and follow this branch without crossing the
                        island hatching or entering the bicycle/scooter strip. The blue sign directs right-
                        turn traffic onto this branch, but the next junction and any stopping requirement are
                        not visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 988, 13.82 s

mapdr__BusLane_9ff2df0e8cf04c7fa72ac9ceb928f324_1709457275071657000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely mainland China, inferred from the simplified Chinese road signs, with
                        traffic keeping right. My car is in the rightmost of three same-direction lanes on a
                        divided expressway, approaching an overpass; no intersection or lane ending is
                        visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a long dash and gaps visible, separates my lane from another
                        same-direction traffic lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from a paved shoulder, with a guardrail
                        farther beyond the shoulder rather than directly on the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my lane
                        being the third and rightmost of three lanes. | roles: The broken white line fits a
                        same-direction lane divider, and the solid white line fits the shoulder edge. |
                        markings: No guidance markings are visible on the pavement within my lane; the
                        overhead arrows are signs, not lane-surface arrows. | unseen: No markings are inferred
                        beneath vehicles or beyond the visible road; no intersection layout is inferred. |
                        result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white same-direction lane divider permits
                        crossing to change lanes when safe.
Step 5  Rule            right_boundary: The solid white roadway edge does not permit an ordinary lane change
                        onto the expressway shoulder.
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        lane change left.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white roadway edge prohibits an
                        ordinary move onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No visible pavement arrow restricts continuing straight
                        along this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this through lane, or change left across the broken line only when safe;
                        do not move onto the right shoulder. The overhead sign for this lane shows a 100 km/h
                        maximum and 60 km/h minimum, but slow appropriately for the traffic ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 822, 15.01 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850371779181000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the blue
                        registration plates, road infrastructure and separated non-motorized path. My car is
                        in the rightmost of three apparent lanes on a divided road approaching a signalized
                        intersection. (lanes 3, mine 3, partial)
Step 2  Left            A white broken line, with visible painted segments and gaps, separates my lane from
                        another traffic lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right side of my lane beside a raised curb and
                        planted separator, with a separate path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (partial): A white longitudinal painted stem is visible immediately
                        behind and beneath the vehicle ahead, apparently part of a guidance arrow, but its
                        head and any branches are hidden by that vehicle.
Step 4  Cross-check     position: The left lane line and right roadway edge agree with being in the rightmost
                        lane; perspective and vehicles make the total lane count less certain. | roles: The
                        broken white line fits a same-direction lane divider, and the solid white line beside
                        the curb fits a roadway edge. | markings: The obscured marking cannot establish
                        permitted directions; arrows visible farther left belong to other lanes and are not
                        applied to my lane. | unseen: No arrowhead or branch is inferred from the visible
                        stem. The vehicle ahead also hides part of the approach, so a stop line or other
                        markings there cannot be confirmed. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white same-direction lane divider permits
                        crossing to change lanes when safe.
Step 5  Rule            right_boundary: The roadway edge and raised curb do not permit an ordinary lane change
                        onto the separated path.
Step 5  Rule            symbol:other: The obscured guidance marking cannot establish which intersection
                        movements its arrowheads permit or prohibit.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (correct): The roadway edge and raised curb prohibit moving into the
                        separated path.
Step 6  go_straight     not_determined (contested, label allowed): The apparent guidance arrow's head is
                        hidden, so its permission for straight travel cannot be determined.
Step 6  turn_left       not_determined: The hidden arrowhead and branches prevent determining whether this
                        lane permits a left turn.
Step 6  turn_right      not_determined: The hidden arrowhead and branches prevent determining whether this
                        lane permits a right turn.
Step 6  u_turn          not_determined: The hidden guidance marking prevents determining whether this lane
                        permits a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Wait until the vehicle ahead reveals your lane's guidance arrow before choosing an
                        intersection movement, and obey the traffic signals. A safe lane change left is
                        permitted across the broken line; do not cross the right curb into the separated path.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1211, 19.03 s

mapdr__DirectionLane_09c3f48ec59b4d96b691a64c4562e3f0_1711850376979277000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        writing, blue vehicle plates and road layout. My car is in the rightmost motor-vehicle
                        lane approaching a signal-controlled intersection; vehicles and the cropped left edge
                        prevent a reliable count of all lanes in this direction. (lanes None, mine None,
                        insufficient)
Step 2  Left            A continuous white solid line separates my lane from another motor-vehicle lane on the
                        left; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line runs beside a raised curb and planted separator, with a
                        separate path carrying a scooter beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead.; line:stop_line (full): A solid white transverse stop line crosses my lane
                        ahead of the arrow and before the zebra crossing.; line:crosswalk (partial): White
                        zebra-crossing stripes extend across my lane beyond the stop line, with some stripes
                        obscured by the vehicle ahead.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to my left, and the
                        right curb and edge line confirm that my lane is rightmost; the total lane count and
                        numerical lane index remain uncertain. | roles: The solid white lane divider and solid
                        white roadway edge fit their observed roles. | markings: The straight-only arrow is
                        consistent with a through lane approaching a stop line and pedestrian crossing; no
                        waiting area is visible. | unseen: No exact lane count or numerical lane index is
                        inferred from the obscured left side, and the partly obscured crossing is identified
                        as partial evidence. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a solid white lane divider prohibits crossing it to
                        change lanes along this stretch.
Step 5  Rule            right_boundary: The roadway edge and raised curb do not permit driving out of this
                        lane onto the planted separator or separate path.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by traffic
                        control; it does not independently require a stop on every approach.
Step 5  Rule            line:crosswalk: The zebra crossing requires attention to pedestrians and yielding as
                        required, without independently changing the lane's permitted direction.
Step 6  change_left     prohibited (correct): The solid white lane divider prohibits crossing to the adjacent
                        lane.
Step 6  change_right    prohibited (correct): The raised curb and roadway edge prohibit moving onto the
                        separator or separate path.
Step 6  go_straight     allowed (correct): The straight-only arrow permits straight travel.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, subject to the traffic signal, and do not cross either
                        boundary here. Stop before the stop line when required and yield to pedestrians at the
                        crossing; turning requires an appropriate lane reached before the solid-line section.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1178, 13.44 s

mapdr__DirectionLane_10c76981b5474a0fba1167e2c9edfc70_1711089649734886000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese building
                        lettering, road furniture and vehicle arrangement. My car is on an urban multilane
                        road approaching a junction, behind the black sedan, with a painted separator to the
                        right. (lanes 3, mine 2, partial)
Step 2  Left            A continuous white line runs along the left of my lane, with another same-direction
                        traffic lane beyond it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, alongside a diagonally hatched
                        strip bounded by another white line, with same-direction vehicles beyond the strip.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The apparent arrangement is one lane to my left and one beyond the separator
                        to my right, placing my lane second from the left; traffic and perspective make the
                        total count less certain. | roles: Both white solid boundaries fit separation of same-
                        direction traffic, with a painted buffer on the right. | markings: No guidance marking
                        is readable inside my lane. The right-hand hatching is outside its nearest boundary
                        and is not an in-lane marking. | unseen: The sedan hides part of the lane ahead, and
                        distant junction markings cannot be read; no hidden arrows or stop line have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese marking rules, a solid white lane-dividing
                        line prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: The solid white boundary alongside the channelizing strip prohibits
                        crossing into the strip or the traffic lane beyond it.
Step 6  change_left     prohibited (correct): The solid white lane boundary prohibits crossing to the left.
Step 6  change_right    prohibited (correct): The solid white boundary and adjacent channelizing strip
                        prohibit crossing to the right.
Step 6  go_straight     allowed (contested, correct): No visible in-lane arrow restricts continuing straight
                        along this lane.
Step 6  turn_left       not_determined: The vehicle ahead and distance hide the junction-end lane guidance
                        that could govern a left turn.
Step 6  turn_right      not_determined: The vehicle ahead and distance hide the junction-end lane guidance
                        that could govern a right turn.
Step 6  u_turn          not_determined: The vehicle ahead and distance hide any junction-end marking that
                        could govern a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: both boundary crossings are prohibited, straight travel is unrestricted by
                        the visible markings, and junction turns remain undecided because the relevant lane
                        surface is obscured.
Advice                  Stay between the solid white boundaries and keep off the hatched separator. Continue
                        cautiously behind the sedan, checking the lane arrows and junction controls as they
                        become visible before committing to a turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1149, 31.1 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802400356714000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the road layout,
                        blue direction signs and roadside infrastructure. My car is in the second of four
                        same-direction lanes on a divided urban road approaching a signalized intersection.
                        (lanes 4, mine 2, full)
Step 2  Left            A white broken line with clearly visible long dashes and gaps separates my lane from
                        another traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with clearly visible long dashes and gaps separates my lane from
                        another traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in the foreground has a single head pointing
                        straight ahead.; arrow:straight (full): A smaller white arrow farther ahead in my lane
                        also points straight ahead.
Step 4  Cross-check     position: The second of four lanes has one same-direction lane to its left and two to
                        its right, consistent with lane-line boundaries on both sides. | roles: Both white
                        broken boundaries fit ordinary same-direction lane dividers. | markings: The two
                        straight-ahead arrows agree; arrows in neighboring lanes are outside my lane. |
                        unseen: No stop line or crosswalk can be confidently resolved at the distant
                        intersection, and none is asserted. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a broken white lane divider
                        permits crossing to change lanes when safe.
Step 5  Rule            right_boundary: Under mainland Chinese marking rules, a broken white lane divider
                        permits crossing to change lanes when safe.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight at the
                        intersection and excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            arrow:straight: The repeated straight-only arrow confirms the same straight-ahead
                        movement restriction.
Step 6  change_left     allowed (correct): The broken white left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a safe lane change.
Step 6  go_straight     allowed (correct): Both lane-use arrows permit straight-ahead travel.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to go straight, obeying the intersection signals. For a turn, move
                        safely across the broken dividers into the appropriate marked turn lane before the
                        intersection; the distant stopping position is not clearly visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1000, 12.05 s

mapdr__DirectionLane_20d1964b84ce4f418a9395d1658c8ec2_1710802401956712000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the road layout,
                        blue Chinese-style direction signs and intersection equipment. My car is in the second
                        of four same-direction lanes approaching a signal-controlled intersection. (lanes 4,
                        mine 2, full)
Step 2  Left            A single continuous white line separates my lane from the left-turn lane on the left;
                        no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line separates my lane from another forward lane on the
                        right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in the foreground has one head pointing
                        straight ahead.; arrow:straight (full): A smaller, more distant white arrow in my lane
                        also points straight ahead.; line:stop_line (partial): A transverse white line is
                        visible at the end of the approach, though its detail is limited by distance.;
                        line:crosswalk (partial): White pedestrian-crossing stripes extend across my lane at
                        the intersection beyond the approach line.
Step 4  Cross-check     position: Lane lines on both sides agree with my lane being second from the left among
                        four same-direction lanes. | roles: Both boundaries are white solid lane separators,
                        consistent with an intersection approach where lane changes are restricted. |
                        markings: Both straight arrows agree; the stop line and crossing are compatible with
                        this signal-controlled straight-ahead approach. | unseen: No hidden turn arrows or
                        waiting areas are inferred; the distant transverse markings have reduced evidence. |
                        result: consistent
Step 5  Rule            left_boundary: In mainland China, a solid white lane separator prohibits crossing it
                        to change lanes.
Step 5  Rule            right_boundary: In mainland China, a solid white lane separator prohibits crossing it
                        to change lanes.
Step 5  Rule            arrow:straight: The straight-only lane arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane.
Step 5  Rule            arrow:straight: The repeated straight arrow confirms the same straight-only lane-use
                        requirement.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal or
                        traffic control, rather than independently requiring a stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires attention to and yielding for
                        pedestrians, but does not independently assign a lane movement.
Step 6  change_left     prohibited (correct): The solid white lane separator prohibits crossing to the left.
Step 6  change_right    prohibited (correct): The solid white lane separator prohibits crossing to the right.
Step 6  go_straight     allowed (correct): The straight arrows permit proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane, subject to the traffic signal and pedestrians; stop
                        before the stop line when required. Turning requires the appropriate turn lane
                        selected before the solid-line approach, not a lane change across either visible
                        boundary.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1158, 12.8 s

mapdr__DirectionLane_24c04ccef0e44052966189681baeacdf_1712135288834200000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese roadside
                        writing, vehicle plates and road layout. My car is in the middle of three same-
                        direction lanes approaching a signal-controlled intersection on a divided urban road.
                        (lanes 3, mine 2, full)
Step 2  Left            A continuous white solid line separates my lane from another same-direction lane on
                        the left; the median barrier is farther left, not on my lane boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from the same-direction lane occupied
                        by the white vehicles on the right, with no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        above the hood; its shaft and any possible additional branches are hidden by the hood.
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying lane 2 of 3; the
                        leftmost lane lies between my left boundary and the median-side edge. | roles: Both
                        white solid lines fit same-direction lane separators on the intersection approach. |
                        markings: The visible forward arrowhead agrees with continuing in this lane; the
                        curved marking farther left belongs to the adjacent lane, not mine. | unseen: The
                        complete arrow is not visible, so additional arrowheads cannot be excluded; the
                        vehicle ahead also obscures the farther lane surface and any stop line. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            arrow:straight: A forward lane-use arrow permits straight travel, but the concealed
                        remainder prevents establishing whether it also permits another movement.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left lane separator prohibits
                        crossing into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right lane separator prohibits
                        crossing into the adjacent lane.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel.
Step 6  turn_left       not_determined (WRONG, label prohibited): The hood conceals the remainder of the
                        arrow, so a left-turn branch cannot be confirmed or excluded.
Step 6  turn_right      not_determined (WRONG, label prohibited): The hood conceals the remainder of the
                        arrow, so a right-turn branch cannot be confirmed or excluded.
Step 6  u_turn          not_determined (WRONG, label prohibited): The complete directional marking is hidden,
                        preventing a definitive determination of its movement restrictions.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid white lines for straight travel; do not change lanes across
                        them. Follow the intersection signals and stop before the stop line when required, and
                        confirm the complete lane arrow before attempting any turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1003, 11.05 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907381140136000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, inferred from the Chinese storefront lettering and
                        road layout; traffic keeps right. My car is in the leftmost of two same-direction
                        lanes approaching a signalized intersection. (lanes 2, mine 1, full)
Step 2  Left            A continuous yellow line runs beside a white central separation fence, with opposing
                        traffic beyond the fence.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A continuous white line separates my lane from the adjacent same-direction lane on the
                        right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight_left (full): A large white arrow in my lane has one head pointing
                        straight ahead and a second head pointing left.
Step 4  Cross-check     position: The central separation fence on the left and another same-direction lane on
                        the right agree with my lane being lane 1 of 2. | roles: The yellow solid central
                        boundary separates opposing directions, while the white solid boundary separates same-
                        direction lanes. | markings: The straight-and-left arrow is consistent with an
                        intersection approach lane; the solid boundaries restrict lane changes, not the
                        indicated intersection movements. | unseen: The vehicle ahead obscures part of the
                        distant lane surface; no hidden stop line, crosswalk, or waiting area is asserted. |
                        result: consistent
Step 5  Rule            left_boundary: In China, the solid central boundary and physical separation prohibit
                        crossing left into the opposing carriageway.
Step 5  Rule            right_boundary: A solid white lane-dividing line prohibits changing lanes across it in
                        the visible approach.
Step 5  Rule            arrow:straight_left: The lane-use arrow permits proceeding straight or turning left,
                        excludes a right turn, and does not by itself establish whether a U-turn is permitted.
Step 6  change_left     prohibited (WRONG, label allowed): The solid central boundary and separation fence
                        prohibit crossing left.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing right.
Step 6  go_straight     allowed (correct): The straight head of the lane-use arrow permits proceeding
                        straight.
Step 6  turn_left       allowed (correct): The left head of the lane-use arrow permits turning left.
Step 6  turn_right      prohibited (correct): The lane-use arrow does not include a right-turn movement.
Step 6  u_turn          not_determined (WRONG, label allowed): The straight-and-left arrow does not establish
                        U-turn permission, and the intersection geometry and any applicable restrictions are
                        not fully visible.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: lane-change restrictions are kept separate from intersection movements,
                        and U-turn permission remains undetermined rather than inferred from the left-turn
                        arrow.
Advice                  Stay in this lane to proceed straight or turn left, subject to the traffic signals and
                        yielding requirements; do not cross either solid boundary. The vehicle ahead hides the
                        precise stopping position, so look for the stop line as visibility improves.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 998, 19.65 s

mapdr__DirectionLane_2da8b419155e4dd38a3a28fbd7fd37b7_1710907382473496000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese shop signs
                        and road layout. My car is in the leftmost of two apparent same-direction lanes
                        approaching a signal-controlled intersection, with a central railing on the left.
                        (lanes 2, mine 1, partial)
Step 2  Left            A continuous yellow line runs beside a metal central railing on the left, with
                        opposing traffic beyond; glare and the railing obscure some of the paint.
                        yellow solid, curb yes, center_line, evidence partial
Step 2  Right           A continuous white line runs along the right side of my lane toward the intersection,
                        with another paved traffic lane beyond and no physical divider on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:crosswalk (partial): White zebra-crossing bars extend across the approach ahead;
                        the vehicle in front hides the central portion across my lane.
Step 4  Cross-check     position: The central railing on the left places my lane leftmost; the white boundary
                        and paved lane to the right support two apparent same-direction lanes, though the
                        outer lane layout is less clear. | roles: The yellow continuous marking and central
                        railing fit separation from opposing traffic; the solid white line fits a same-
                        direction lane divider near an intersection. | markings: The visible crossing does not
                        conflict with either boundary. No readable lane-use arrow or waiting area is visible.
                        | unseen: No arrow, stop word, or stop-line configuration has been inferred beneath
                        the leading vehicle; some paint beside the railing and the middle of the crossing are
                        obscured. | result: consistent
Step 5  Rule            left_boundary: In China, the solid yellow central boundary and physical railing
                        prohibit crossing left into opposing traffic.
Step 5  Rule            right_boundary: A solid white lane divider in China prohibits changing lanes across
                        it.
Step 5  Rule            line:crosswalk: A pedestrian crossing requires attention to pedestrians and yielding
                        as required, but does not itself prescribe a lane-use movement.
Step 6  change_left     prohibited (correct): The solid yellow central boundary and railing prohibit crossing
                        left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white lane divider prohibits crossing
                        right in the visible stretch.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight; the longitudinal boundaries do not prohibit it.
Step 6  turn_left       not_applicable: No readable arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No readable arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No readable arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay within the current lane rather than crossing either solid boundary. Follow the
                        traffic signals, yield to pedestrians at the crossing, and check for lane arrows or a
                        stop line revealed as the vehicle ahead moves.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 6424, out 1114, 18.53 s

mapdr__DirectionLane_38c846f3de1148d898b44814ee21a590_1709882978567210000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        bridge sign, national flag and road layout. My car is in the rightmost of three motor-
                        vehicle lanes approaching a split beneath Dashan Bridge, with a right-turn arrow in my
                        lane. (lanes 3, mine 3, full)
Step 2  Left            A solid white line borders a tapered painted divider on the left, leading toward a
                        raised island around the bridge pier; other motor-vehicle lanes lie beyond the
                        divider.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible painted segments and gaps, separates my lane from a
                        narrow roadside strip occupied by a scooter; the sidewalk curb lies beyond that strip.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white bent arrow has a single head pointing right.
Step 4  Cross-check     position: My lane is the rightmost motor-vehicle lane; the right edge separates it
                        from the roadside non-motorized strip. The left edge borders a divider at the split,
                        rather than directly adjoining another lane. | roles: The solid white divider edge and
                        broken white roadside edge fit their respective roles at this split. | markings: The
                        right-only arrow agrees with the lane passing to the right of the bridge-pier island.
                        The arrow in the lane to the left does not govern my car. | unseen: No stop line or
                        additional guidance marking can be identified in the shaded distance; none has been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: In China, the solid boundary of a channelizing divider must not be
                        crossed, and the raised island cannot be driven over.
Step 5  Rule            right_boundary: A broken roadside boundary permits crossing when necessary and safe,
                        without obstructing users of the non-motorized strip; it does not authorize ordinary
                        travel along that strip.
Step 5  Rule            arrow:right: The right-turn-only lane arrow requires a right turn and excludes
                        straight, left-turn and U-turn movements from this lane.
Step 6  change_left     prohibited: The solid divider boundary and raised island prohibit crossing left.
Step 6  change_right    allowed: The broken roadside boundary permits a necessary safe crossing, with priority
                        given to non-motorized users.
Step 6  go_straight     prohibited (WRONG, label allowed): The right-only arrow excludes straight travel.
Step 6  turn_left       prohibited (correct): The right-only arrow excludes a left turn.
Step 6  turn_right      allowed (correct): The arrow explicitly permits a right turn.
Step 6  u_turn          prohibited (correct): The right-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Follow this lane to turn right; do not cross the solid divider to reach the through
                        lanes. Yield to the scooter and pedestrians, do not use the roadside strip as a travel
                        lane, and check for controls hidden beneath the bridge.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1200, 21.51 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544474099074000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, judging from the road
                        furniture, markings and signs, although the country is not certain. My car is in the
                        leftmost of three same-direction lanes on a divided urban road approaching a
                        signalized intersection. (lanes 3, mine 1, full)
Step 2  Left            A continuous white solid line runs beside a central metal separation fence, with
                        opposing traffic space beyond; the fence forms a physical boundary.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white broken line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane, with no curb between them.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small white forward-pointing arrow is visible ahead in my
                        lane; its distant head and shaft indicate straight travel, but fine details are
                        indistinct.
Step 4  Cross-check     position: The fenced left roadway edge and right lane divider agree with my car
                        occupying lane 1 of three same-direction lanes. | roles: The white solid line beside
                        the central fence fits a roadway edge, while the white broken line fits a same-
                        direction lane divider. | markings: The visible straight arrow is compatible with
                        continuing along this lane; no conflicting word, symbol or waiting area is
                        discernible. | unseen: The arrow is distant, so additional arrowhead detail and
                        markings at the intersection cannot be resolved; no stop line or crosswalk is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, the solid roadway edge and central
                        separation fence prohibit leaving the lane to the left.
Step 5  Rule            right_boundary: A white broken same-direction lane divider permits changing right when
                        safe and without interfering with other traffic.
Step 5  Rule            arrow:straight: A straight-only guidance arrow permits straight travel and excludes
                        turns, provided its complete shape is confirmed.
Step 6  change_left     prohibited (correct): The solid roadway edge and central fence prohibit crossing left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent ordinary lane.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel.
Step 6  turn_left       not_determined (WRONG, label prohibited): The distant arrow cannot be inspected
                        closely enough to exclude an additional left branch with confidence.
Step 6  turn_right      not_determined (WRONG, label prohibited): The distant arrow cannot be inspected
                        closely enough to exclude an additional right branch with confidence.
Step 6  u_turn          not_determined (WRONG, label prohibited): The distant arrow's complete shape cannot be
                        confirmed well enough to determine U-turn permission.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: straight travel follows the visible forward arrowhead, while turn
                        decisions remain unresolved because the complete arrow detail is distant.
Advice                  Continue straight in this lane and do not cross the fenced left edge; changing right
                        is permitted only when safe. Confirm the arrow and intersection markings closer ahead
                        before attempting any turn, and obey the traffic signals and any stop line that
                        becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 999, 19.94 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478099110000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        signage, road markings and traffic arrangement. My car is in the leftmost of three
                        visible same-direction lanes approaching a signal-controlled intersection on a divided
                        urban road. (lanes 3, mine 1, full)
Step 2  Left            A continuous white solid line borders my lane on the left, with a narrow strip and a
                        physical median fence beyond it separating opposing traffic.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from another same-direction lane on
                        the right; there is no curb along this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.;
                        line:stop_line (full): A transverse white stop line crosses my lane just before the
                        pedestrian crossing.; line:crosswalk (full): White zebra-crossing stripes extend
                        across my lane immediately beyond the stop line.
Step 4  Cross-check     position: The left roadway edge and median fence agree with my lane being leftmost;
                        the right lane line separates it from the remaining same-direction lanes. | roles: The
                        white solid left line marks the edge beside the median barrier, rather than an exposed
                        painted center line; the white solid right line is an approach lane divider. |
                        markings: The straight-only arrow agrees with a through lane bounded by solid approach
                        lines; the stop line and crosswalk are compatible with the signal-controlled
                        intersection. | unseen: No obscured arrow heads, words or waiting areas have been
                        inferred; markings in neighboring lanes are not attributed to my lane. | result:
                        consistent
Step 5  Rule            left_boundary: The median edge and physical fence do not permit my car to leave the
                        lane to the left.
Step 5  Rule            right_boundary: Under mainland Chinese marking rules, the solid white lane divider
                        prohibits changing lanes across it.
Step 5  Rule            arrow:straight: The straight-only lane arrow permits proceeding straight and prohibits
                        left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal or
                        traffic control, but does not independently require every vehicle to stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires yielding to pedestrians and keeping
                        the crossing clear.
Step 6  change_left     prohibited (correct): The left edge is bounded by a physical median fence, so leaving
                        to the left is prohibited.
Step 6  change_right    prohibited (correct): The solid white lane divider prohibits crossing into the lane on
                        the right.
Step 6  go_straight     allowed (correct): The single straight-ahead arrow permits continuing straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight; do not cross either boundary or turn from it.
                        Obey the traffic signal, stop before the stop line when required, and yield to
                        pedestrians at the crossing.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1249, 16.16 s

mapdr__DirectionLane_4b981cd0989f4cfaabff379758d180d8_1710544478365779000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the road
                        markings, Chinese-style signs and median fencing. My car is in the leftmost of three
                        same-direction approach lanes at a signal-controlled intersection. (lanes 3, mine 1,
                        full)
Step 2  Left            A continuous white solid line borders my lane on the left, with a metal median barrier
                        immediately beyond it; yellow paint is visible farther left beneath the barrier, and
                        opposing traffic is beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white solid line runs along the right side of my lane up to the intersection
                        approach, separating it from another same-direction lane, with no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has a single head pointing
                        straight ahead.; line:stop_line (full): A white transverse stop line crosses my lane
                        ahead of the arrow and before the pedestrian crossing.; line:crosswalk (full): White
                        zebra-crossing stripes extend across the roadway immediately beyond the stop line.
Step 4  Cross-check     position: The median edge on the left and a same-direction lane line on the right
                        agree with my lane being lane 1 of 3. | roles: The white solid line beside the
                        physical median functions as an edge line; the white solid line on the right separates
                        approach lanes. | markings: The straight-only arrow agrees with a through approach
                        lane; the stop line and crosswalk do not add turning permissions. | unseen: No hidden
                        arrow heads or waiting areas are inferred; the country is an inference from visible
                        context rather than a confirmed location. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and physical median barrier prohibit leaving
                        this lane across its left boundary.
Step 5  Rule            right_boundary: Under mainland Chinese marking rules, a solid white lane separator
                        prohibits changing lanes across it.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal or
                        traffic control, but does not itself require every vehicle to stop.
Step 5  Rule            line:crosswalk: The zebra crossing requires attention and yielding to pedestrians as
                        applicable, without changing the lane's permitted directions.
Step 6  change_left     prohibited (correct): The solid edge and physical median barrier prohibit crossing the
                        left boundary.
Step 6  change_right    prohibited (correct): The solid white lane separator prohibits crossing into the lane
                        on the right.
Step 6  go_straight     allowed (correct): The straight-only arrow permits continuing straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane only when the applicable signal and crossing are
                        clear; stop before the stop line when required. Do not cross either boundary here to
                        reposition for a turn, and watch for pedestrians on the zebra crossing.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1147, 15.64 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789157159392000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, inferred from the
                        Chinese writing, street furniture and vehicle positions. My car is in the left of two
                        same-direction lanes, approaching a side-road junction marked with a yellow keep-clear
                        grid. (lanes 2, mine 1, full)
Step 2  Left            A broken yellow line, with visible painted segments and gaps, separates my lane from
                        oncoming traffic on the left; there is no curb along it.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A faint broken white line separates my lane from another same-direction lane on the
                        right; its dashes and gaps are clearer farther ahead, and no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        area:grid (full): A yellow diagonal crosshatched box extends across my lane at the
                        junction ahead.
Step 4  Cross-check     position: The yellow center line makes my lane the leftmost same-direction lane, and
                        the white lane divider places another same-direction lane to my right, consistent with
                        lane 1 of 2. | roles: The broken yellow center line separates opposing traffic; the
                        broken white line separates same-direction lanes. | markings: The yellow keep-clear
                        grid is compatible with both boundaries and does not prescribe a direction of travel.
                        | unseen: No lane-use arrow, STOP word, stop line or left-turn waiting area is visibly
                        identifiable in my lane. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken yellow center line may be crossed for an
                        otherwise lawful maneuver only when opposing traffic conditions make it safe.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent same-
                        direction lane when safe.
Step 5  Rule            area:grid: The yellow grid prohibits stopping within the marked junction area and must
                        be kept clear, but does not itself restrict turning movements.
Step 6  change_left     allowed (WRONG, label not_determined): The broken yellow center line permits crossing
                        when lawful and safe, but it leads into opposing traffic rather than another same-
                        direction lane.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        change to the adjacent same-direction lane.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow restricts continuing straight; the
                        grid requires keeping the junction clear.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane for straight travel, entering the yellow grid only when you can
                        clear it without stopping. A right lane change is permitted when safe; crossing left
                        would enter opposing traffic, and the visible markings do not establish turn
                        permissions.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1019, 16.28 s

mapdr__DirectionLane_55ec13980f824f72999db9c341658d27_1709789159559456000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        writing, road signs and markings. My car is in the left of two same-direction motor-
                        vehicle lanes on an urban two-way street; the road continues ahead, but the next
                        intersection is not clearly visible. (lanes 2, mine 1, full)
Step 2  Left            A single continuous yellow line separates my lane from opposing traffic on the left;
                        no curb forms this boundary.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           White long dashes separated by clear gaps divide my lane from another same-direction
                        motor-vehicle lane, occupied by the gray sedan; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): A white hollow diamond is painted centrally in my lane in the
                        foreground.; symbol:other (full): A second, smaller-in-perspective white hollow
                        diamond is visible farther ahead in my lane.
Step 4  Cross-check     position: The yellow center line on the left and white lane divider on the right agree
                        with my lane being lane 1 of two same-direction lanes. | roles: The solid yellow line
                        fits separation of opposing traffic, and the broken white line fits separation of
                        same-direction lanes. | markings: The hollow diamonds are pedestrian-crossing advance-
                        warning markings in the inferred Chinese setting, not HOV restrictions; they do not
                        conflict with the boundaries. | unseen: No directional arrow, stop line or waiting
                        area is identifiable in my lane; the distant intersection and any markings there
                        cannot be resolved. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a solid yellow center line prohibits crossing into
                        the opposing side to overtake or change position.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent same-
                        direction lane when safe.
Step 5  Rule            symbol:other: The hollow diamond warns of a pedestrian crossing ahead and calls for
                        caution, without assigning a lane movement.
Step 5  Rule            symbol:other: The repeated hollow diamond reinforces the pedestrian-crossing warning
                        and does not reserve this lane or restrict its turning movements.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white divider permits a lane change when
                        safe.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action;
                        the center line governs crossing the visible left boundary, not a movement at an
                        unseen intersection.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the boundary decisions apply only to crossing those boundaries, and the
                        warning diamonds do not determine intersection movements.
Advice                  Continue in this lane without crossing the solid yellow center line; change right only
                        after checking the gray sedan and other traffic. Slow for the warned pedestrian
                        crossing, and check the signs, signals and lane arrows nearer the next intersection
                        before choosing a turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6424, out 1083, 10.74 s

mapdr__DirectionLane_5bc683cf2728478fb495b2b9a275a28b_1711429408205130000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        signage, vehicles and road layout. My car is in the rightmost of three motor-vehicle
                        lanes approaching a signalized intersection beside an elevated road; a red-surfaced
                        strip used by two-wheelers lies to the right. (lanes 3, mine 3, full)
Step 2  Left            A single solid white line separates my lane from the same-direction lane on the left;
                        no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white line, solid alongside the car with an interruption farther ahead near the red
                        surfacing, separates my lane from a roadside strip occupied by two-wheelers; the
                        sidewalk curb is beyond that strip rather than directly bounding my lane.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        arrow:right (full): A white arrow has a forward-running stem that bends right and ends
                        in a right-pointing head; it has no straight-ahead head.
Step 4  Cross-check     position: The lane line on the left and roadside edge on the right agree with my lane
                        being the rightmost of three motor-vehicle lanes. | roles: The white solid left line
                        fits a same-direction lane separator, and the white right line fits the edge beside a
                        non-motorized roadside strip. | markings: The right-turn-only arrow is consistent with
                        this rightmost approach lane; no conflicting guidance marking is visible in my lane. |
                        unseen: The intersection-end markings are obscured by vehicles and distance, and the
                        right boundary's farther continuation is not fully clear; no stop line or crosswalk is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, the solid white lane separator
                        prohibits crossing it to change lanes in the visible solid-lined approach.
Step 5  Rule            right_boundary: The roadway edge beside the non-motorized strip does not permit an
                        ordinary car to move into that strip as a traffic lane.
Step 5  Rule            arrow:right: The right-turn lane-use arrow requires a right turn from this lane and
                        does not permit straight travel, a left turn or a U-turn at the intersection.
Step 6  change_left     prohibited: The solid white lane separator prohibits crossing into the lane on the
                        left.
Step 6  change_right    prohibited: The right edge borders the non-motorized roadside strip, which is not
                        available as an ordinary-car lane.
Step 6  go_straight     prohibited (correct): The right-turn-only arrow does not show straight travel.
Step 6  turn_left       prohibited (correct): The right-turn-only arrow does not show a left turn.
Step 6  turn_right      allowed (correct): The lane-use arrow explicitly permits a right turn.
Step 6  u_turn          prohibited (correct): The right-turn-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a right turn, yielding to pedestrians and two-wheelers beside and
                        across the turn, and obey the applicable signals. For straight travel or a left turn,
                        select the appropriate lane before the solid-line approach; do not cross the solid
                        separator here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1148, 26.59 s

mapdr__DirectionLane_5e9d9ed0d5194ce795fa8fd51eacd541_1711614607274696000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        writing and vehicles traveling to the right of the central divider. My car is in the
                        leftmost lane of a divided urban road approaching a signalized intersection; vehicles
                        obscure the full lane count and much of my lane ahead. (lanes None, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised concrete median barrier on the left, with
                        opposing traffic beyond the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from another same-direction lane on the
                        right; its farther continuation is obscured by vehicles.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median-side edge makes my lane the leftmost, and the right lane line
                        confirms another same-direction lane; the total count remains obscured. | roles: The
                        white left edge line beside a physical median and the solid white right lane divider
                        fit their assigned roles. | markings: No guidance marking is readable in the exposed
                        portion of my lane; the visible arrow to the right belongs to another lane. | unseen:
                        No arrow, stop line, crosswalk, or waiting area is inferred beneath the truck or
                        beyond the obscured approach. | result: consistent
Step 5  Rule            left_boundary: The raised median prohibits leaving my lane to the left.
Step 5  Rule            right_boundary: In mainland China, a solid white lane divider prohibits crossing it to
                        change lanes.
Step 6  change_left     prohibited (WRONG, label not_determined): The raised median blocks and prohibits
                        crossing the left boundary.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white lane divider prohibits
                        crossing to the right.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The truck hides the approach pavement where lane-use arrows could
                        determine this movement.
Step 6  turn_right      not_determined: The truck hides the approach pavement where lane-use arrows could
                        determine this movement.
Step 6  u_turn          not_determined: The truck hides the approach pavement where movement restrictions
                        could determine this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: neither boundary permits a lane change, straight continuation has no
                        visible restriction, and intersection turns remain undecided because relevant pavement
                        is obscured.
Advice                  Stay between the median and the solid white divider; do not change lanes across either
                        boundary. Leave enough space behind the truck to see your lane's arrows, stop line,
                        and applicable signal before committing to an intersection movement.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 997, 13.0 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997080632482000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the road layout,
                        signals and vehicle plates. My car is in the middle of three same-direction lanes on a
                        divided urban road approaching a signalized intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead.
Step 4  Cross-check     position: Lane lines on both sides agree with my lane being second of three same-
                        direction lanes. | roles: Both white broken boundaries fit ordinary same-direction
                        lane dividers. | markings: The straight-only arrow is consistent with a through lane;
                        no conflicting words, symbols or waiting areas are visible. | unseen: The
                        intersection-end pavement is partly obscured by vehicles and distance; no hidden stop
                        line or additional marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, an ordinary broken white lane divider may be crossed to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, an ordinary broken white lane divider may be crossed to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 6  change_left     allowed (correct): The broken white left lane divider permits crossing when safe.
Step 6  change_right    allowed (correct): The broken white right lane divider permits crossing when safe.
Step 6  go_straight     allowed (correct): The lane arrow explicitly permits straight travel.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Use this lane for straight travel; change lanes across the broken lines only when
                        safe, and find an appropriately marked lane before attempting a turn. The signals
                        ahead appear red: stop behind the stop line when it becomes visible and wait for
                        permission to proceed.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 902, 14.83 s

mapdr__DirectionLane_62b71b376d334fecbc1c4f8f434063f7_1710997082499180000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the road-marking style,
                        signals and streetscape. My car is in the middle of three same-direction lanes
                        approaching a signal-controlled intersection. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead.
Step 4  Cross-check     position: Lane lines on both sides agree with my position in lane 2 of 3. | roles:
                        Both white solid lines separate same-direction lanes and fit their lane-line roles. |
                        markings: The straight-only arrow agrees with a through lane bounded by solid approach
                        lane lines; adjacent-lane arrows do not govern my lane. | unseen: No stop line or
                        crosswalk can be identified confidently behind the vehicles ahead, and none is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: Under Chinese marking rules, a solid white lane divider prohibits
                        crossing it to change lanes to the left.
Step 5  Rule            right_boundary: Under Chinese marking rules, a solid white lane divider prohibits
                        crossing it to change lanes to the right.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The straight-only arrow permits this movement.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel and do not cross either solid divider; turns
                        require an appropriate lane reached before the solid-line section. The signals ahead
                        are red: stop behind the queue and the stop line when visible, and proceed only when
                        permitted.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 877, 10.61 s

mapdr__DirectionLane_79e9c06f70c1441b82762c324facbb34_1711000813221111000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the road layout,
                        vehicles, roadside signs and streetscape. The car is in the third of four same-
                        direction lanes on a divided urban road approaching a distant signal-controlled
                        intersection. (lanes 4, mine 3, full)
Step 2  Left            A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the roadside solid white line and curb are beyond that
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes with my car in lane three agrees with same-direction lane lines
                        on both sides: two lanes lie to the left and one to the right. | roles: Both white
                        broken boundaries fit ordinary same-direction lane-divider roles. | markings: No
                        guidance arrows, words, symbols or transverse markings are readable in the visible
                        portion of my lane, so none contradict the boundaries. | unseen: The vehicles ahead
                        and distance obscure the intersection approach; no unseen arrows, stop line or waiting
                        area have been inferred. | result: consistent
Step 5  Rule            left_boundary: Under Chinese road-marking rules, a broken white lane divider permits
                        crossing into the adjacent ordinary lane when safe without interfering with traffic.
Step 5  Rule            right_boundary: Under Chinese road-marking rules, a broken white lane divider permits
                        crossing into the adjacent ordinary lane when safe without interfering with traffic.
Step 6  change_left     allowed (correct): The visible broken white lane divider permits a safe lane change
                        left.
Step 6  change_right    allowed (correct): The visible broken white lane divider permits a safe lane change
                        right.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or lane ending restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: lane changes follow the broken boundary rules, straight travel is
                        unrestricted by visible markings, and no turn or waiting-area permission is inferred.
Advice                  You may continue straight or change one lane either way across the visible broken
                        lines when safe. Before choosing a turning lane, check the markings closer to the
                        intersection, which are not readable here, and obey the signals and any stop line.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 897, 12.74 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414757233772000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the road-sign style,
                        markings and streetscape. My car is in the leftmost of four same-direction lanes on a
                        broad urban road approaching an intersection. (lanes 4, mine 1, full)
Step 2  Left            A continuous white line nearest my lane borders two parallel solid yellow lines with
                        another white line on their far side; opposing traffic lies beyond, and there is no
                        raised divider.
                        white solid, curb no, center_line, evidence full
Step 2  Right           A white broken line, with a long dash and clear gaps visible, separates my lane from
                        another same-direction lane; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (full): A white arrow ahead in my lane has a bent shaft and a single head
                        pointing left.
Step 4  Cross-check     position: The center-line boundary on the left and same-direction lane line on the
                        right agree with my lane being first from the left among four lanes. | roles: The
                        continuous white border is part of the visibly double-yellow center separation; the
                        broken white right boundary fits an ordinary lane divider. | markings: The left-only
                        pavement arrow is consistent with the leftmost lane and the contextual lane-direction
                        sign. | unseen: No stop line or waiting area is identifiable in the distant
                        intersection approach; none has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, the solid center separation, including the double-yellow
                        lines alongside its white border, prohibits crossing into opposing traffic.
Step 5  Rule            right_boundary: A broken white ordinary lane divider permits changing to the adjacent
                        lane when safe.
Step 5  Rule            arrow:left: A left-only lane-use arrow requires a left turn from this lane and does
                        not authorize straight, right-turn or U-turn movements.
Step 6  change_left     prohibited (correct): The continuous center separation prohibits crossing to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change right.
Step 6  go_straight     prohibited (contested, label allowed): The left-only arrow does not permit continuing
                        straight from this lane.
Step 6  turn_left       allowed: The pavement arrow explicitly permits a left turn.
Step 6  turn_right      prohibited: The left-only arrow excludes a right turn.
Step 6  u_turn          prohibited: The arrow shows only a left turn, not a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to turn left; to continue straight, change right across the broken
                        white line when safe before reaching the intersection. Do not cross the center
                        separation, and obey the intersection signals and any stop line as they become
                        visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 940, 20.41 s

mapdr__DirectionLane_8c3777cc0b944f12a8ebb5034248e4d0_1711414759900456000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be an urban arterial in mainland China, with traffic keeping right,
                        inferred from the road markings, vehicles and roadside signs. My car is in the
                        leftmost of three lanes in its direction, approaching a distant intersection. (lanes
                        3, mine 1, full)
Step 2  Left            A continuous white line lies nearest my lane, alongside two continuous yellow lines
                        and another white line farther left; opposing traffic is beyond this painted central
                        separation, with no raised curb.
                        white solid, curb no, center_line, evidence full
Step 2  Right           White broken lane-divider segments, with clear gaps between them, separate my lane
                        from another same-direction lane on the right; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:left (partial): A large white left-turn arrow is partly hidden by the hood at
                        the bottom of my lane.; arrow:left (full): Farther ahead in my lane, a white bent
                        arrow has a left-pointing head.
Step 4  Cross-check     position: The central separation on the left agrees with my lane being leftmost; the
                        broken divider on the right leads to the other same-direction lanes. | roles: The
                        nearest white solid line forms part of a wider painted central separation containing
                        double yellow lines, rather than dividing two same-direction lanes; the broken white
                        line on the right is a lane divider. | markings: The repeated left-turn arrows agree
                        with each other and designate this leftmost lane for left turns. | unseen: The nearest
                        arrow is partly covered by the hood, and the distant intersection's transverse
                        markings cannot be resolved; no hidden stop line or waiting area is assumed. | result:
                        consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, the solid painted central separation
                        must not be crossed to leave this lane.
Step 5  Rule            right_boundary: A broken white lane divider may be crossed to change lanes when safe
                        and without interfering with other traffic.
Step 5  Rule            arrow:left: The partially visible left-turn arrow directs this lane to turn left
                        rather than proceed straight, turn right or make a U-turn.
Step 5  Rule            arrow:left: The complete left-turn arrow confirms that the designated movement from
                        this lane is a left turn.
Step 6  change_left     prohibited (correct): The solid central separation prohibits crossing the left
                        boundary.
Step 6  change_right    allowed (correct): The broken white divider permits a safe lane change to the right.
Step 6  go_straight     prohibited (correct): The left-turn arrows do not include a straight-ahead movement.
Step 6  turn_left       allowed (correct): The left-turn arrows explicitly allow a left turn.
Step 6  turn_right      prohibited: The left-turn arrows do not include a right turn.
Step 6  u_turn          prohibited: The lane arrows designate left turns, not U-turns.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for a left turn, obeying the intersection signals and any
                        applicable turn restrictions. For another movement, change right across the broken
                        divider only when safe and select the appropriately marked lane; do not cross the
                        central separation.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:left'], missed ['arrow:left_u_turn', 'arrow:straight']), actions True, unsafe
                        [], citation None, contradictions []
Tokens                  in 6424, out 1167, 25.66 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517073665698000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, suggested by the Chinese
                        writing, road markings and vehicle positions. My car is in the middle lane of a five-
                        lane urban carriageway beside an elevated road, approaching a distant signalized
                        intersection. (lanes 5, mine 3, full)
Step 2  Left            A white broken line, with long dashes and visible gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and visible gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead; markings at the distant intersection are too small to resolve.
Step 4  Cross-check     position: Lane 3 of 5 has same-direction lanes on both sides, consistent with both
                        boundaries being lane lines. | roles: Both white broken boundaries fit ordinary same-
                        direction lane dividers. | markings: The straight-ahead arrow is consistent with a
                        through lane bounded by broken lane lines. | unseen: No distant stop line, crosswalk
                        or waiting area is asserted; the intersection pavement is not sufficiently resolved. |
                        result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In mainland China, a broken white lane divider permits crossing to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            arrow:straight: The straight-only lane arrow permits proceeding straight from this
                        lane and excludes left turns, right turns and U-turns from it.
Step 6  change_left     allowed (correct): The broken white left lane divider permits a lane change when safe.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a lane change when
                        safe.
Step 6  go_straight     allowed (contested, correct): The single straight-ahead arrow permits proceeding
                        straight.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight, obeying the signals and stopping at the
                        intersection stop line if required. For a turn or U-turn, first identify an
                        appropriately marked lane and change lanes only when safe across the broken lines.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1118, 17.18 s

mapdr__DirectionLane_8c55eb645a084d67b4ef46c21f3e12a5_1709517075665723000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This is probably China, with traffic keeping right, suggested by the Chinese national
                        flag, road furniture and vehicle arrangement. My car is in the third of four same-
                        direction lanes approaching a signal-controlled intersection beside an elevated
                        roadway. (lanes 4, mine 3, full)
Step 2  Left            A single continuous white painted line separates my lane from another traffic lane on
                        the left; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single continuous white painted line separates my lane from another traffic lane on
                        the right; the roadside fence is farther right, not on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small white forward-pointing arrow is visible near the
                        intersection approach; its distant head and shaft indicate straight ahead.;
                        line:crosswalk (full): White pedestrian-crossing stripes extend across my lane ahead.
Step 4  Cross-check     position: Two lanes lie to my left and one to my right, consistent with lane lines on
                        both sides and position three of four. | roles: The white continuous boundaries fit
                        same-direction lane separators on an intersection approach. | markings: The visible
                        straight arrow is consistent with a through lane bounded by solid approach lines. |
                        unseen: The arrow is distant, so its evidence is partial; no unreadable pavement text
                        or indistinct transverse line has been classified. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        prohibits turning left, turning right or making a U-turn from this lane.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires attention to pedestrians and must not
                        be obstructed; it does not itself select a permitted turning movement.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (contested, correct): The visible straight-ahead arrow permits continuing
                        straight.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane only when the signal and pedestrian conditions
                        permit; do not cross either solid lane separator. For a turn, select the appropriate
                        designated lane before the solid-line approach section, and keep the crosswalk clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:crosswalk'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1214, 27.57 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311757749160000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely mainland China, with traffic keeping right, based on the Chinese
                        writing, blue registration plates and road layout. My car is on a broad divided urban
                        road approaching a signal-controlled intersection, apparently in the third of five
                        same-direction lanes. (lanes 5, mine 3, partial)
Step 2  Left            A white broken line, with visible long painted segments and intervening gaps,
                        separates my lane from another traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line separates my lane from another traffic lane on the right, with
                        painted segments and gaps visible in perspective; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow farther ahead in my lane has a forward-pointing
                        head and no visible turning branch.; line:crosswalk (partial): A distant row of white
                        crossing bars extends across the approach, including my lane; its details are reduced
                        by distance.
Step 4  Cross-check     position: Lane lines on both sides establish that my lane is an interior lane. Five
                        lanes and position three appear consistent with the visible roadway, although
                        perspective makes the overall count less certain. | roles: White broken boundaries fit
                        separators between lanes travelling in the same direction. | markings: The straight
                        arrow agrees with an interior through lane; the crossing ahead does not change its
                        permitted direction. | unseen: The exact distant transition of the boundaries and any
                        separate stop line cannot be resolved reliably; neither has been invented. | result:
                        consistent
Step 5  Rule            left_boundary: In mainland China, a broken white ordinary lane separator permits
                        crossing to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A broken white ordinary lane separator permits a safe lane change into
                        the adjacent ordinary traffic lane.
Step 5  Rule            arrow:straight: The straight-only lane arrow permits proceeding straight at the
                        intersection and excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires attention to and yielding for
                        pedestrians as applicable, but does not itself select a permitted turning movement.
Step 6  change_left     allowed (correct): The broken white left lane separator permits crossing when safe.
Step 6  change_right    allowed (correct): The broken white right lane separator permits crossing when safe.
Step 6  go_straight     allowed (contested, correct): The forward-pointing lane arrow permits straight travel.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight, obeying the traffic signals and yielding at the
                        crossing. For a turn, move safely into an appropriately marked lane before the
                        intersection and before any solid approach markings begin; the distant stop-line
                        position is not clear enough to specify.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight', 'line:crosswalk'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1630, 43.83 s

mapdr__DirectionLane_8db7574779504f58bbe9126598a116a5_1710311760549212000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese writing,
                        road layout and vehicles. My car is in a straight-ahead lane approaching a broad
                        signalized intersection; four approach lanes appear visible, with my lane third from
                        the left. (lanes 4, mine 3, partial)
Step 2  Left            A continuous white line borders my lane on the left, with repeated short oblique white
                        teeth on its far side; another same-direction lane lies beyond, without a curb between
                        the lanes.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from the adjacent same-direction lane on the
                        right, with no intervening curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow near the car has one head pointing straight
                        ahead.; arrow:straight (full): A smaller, more distant white arrow in the same lane
                        points straight ahead.; line:stop_line (partial): A faint transverse white line
                        appears across the lane immediately before the pedestrian crossing; its detail is
                        limited by distance.; line:crosswalk (full): White pedestrian-crossing stripes extend
                        across my lane at the intersection.
Step 4  Cross-check     position: Same-direction lanes on both sides agree with an interior lane position; the
                        precise count on the far left is less certain because vehicles obscure portions of the
                        approach. | roles: Both white continuous boundaries fit solid lane-dividing lines; the
                        oblique teeth beside the left line do not make that line broken. | markings: Both
                        arrows indicate straight ahead and agree with each other; the transverse line and
                        crossing do not add turning permissions. | unseen: The lane count is tentative and the
                        distant stop line is only partially resolved; no unseen arrow heads or waiting areas
                        are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            arrow:straight: A straight-only lane arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane.
Step 5  Rule            arrow:straight: The repeated straight-only arrow confirms that this lane is for
                        straight-ahead movement.
Step 5  Rule            line:stop_line: A stop line identifies where to stop when required by traffic control,
                        rather than independently requiring every vehicle to stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires care and yielding to pedestrians as
                        applicable, without changing the lane's permitted directions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): Both straight-ahead arrows permit continuing straight.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight, subject to the traffic signals and
                        pedestrians; stop before the stop line when required. Do not cross either solid
                        boundary to seek a turning lane in this visible approach.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1355, 17.68 s

mapdr__DirectionLane_8f2aaef21ebc4abeb5f4ff26653f3db5_1710896687128840000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        roadside text and road layout. My car is in the middle of three same-direction motor-
                        vehicle lanes on a divided urban road approaching a signal-controlled intersection; a
                        separate roadside strip lies farther right. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with a clearly visible dash and gap, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible dashes and gaps, separates my lane from another
                        motor-vehicle lane on the right; the solid white line and roadside strip are farther
                        right, not my immediate boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two immediate lane-line boundaries agree with my car occupying lane 2 of 3
                        same-direction motor-vehicle lanes. | roles: Both white broken boundaries fit ordinary
                        same-direction lane dividers. | markings: No readable guidance marking is visible in
                        my lane; markings farther ahead may be concealed by vehicles or distance. | unseen: No
                        arrow, stop line, or waiting area has been inferred from the nearby signs or traffic
                        signals. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white ordinary lane divider permits
                        crossing to change lanes when safe without obstructing traffic.
Step 5  Rule            right_boundary: In mainland China, a broken white ordinary lane divider permits
                        crossing to change lanes when safe without obstructing traffic.
Step 6  change_left     allowed (correct): The immediate broken white lane divider permits a safe lane change
                        left.
Step 6  change_right    allowed (correct): The immediate broken white lane divider permits a safe lane change
                        right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The intersection-end portion of my lane is obscured by vehicles and
                        distance, so any governing arrow cannot be established.
Step 6  turn_right      not_determined: The intersection-end portion of my lane is obscured by vehicles and
                        distance, so any governing arrow cannot be established.
Step 6  u_turn          not_determined: The intersection-end portion of my lane is obscured by vehicles and
                        distance, so any governing movement marking cannot be established.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You may continue along this lane or change to an adjacent motor-vehicle lane when
                        safe, checking carefully for the nearby cars and scooter. Confirm the lane arrows and
                        obey the intersection signals before choosing a turn; the roadside U-turn sign alone
                        does not establish permission from your lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 880, 16.93 s

mapdr__DirectionLane_9c5c7c2e398649fab673af4b39b71ccd_1710893238070992000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, with traffic keeping right, based on the Chinese signage, road
                        layout and vehicle positions. The car is in the middle of three same-direction lanes
                        on a divided urban road; the road continues ahead, but the next intersection and lane
                        endpoint are not clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane
                        across each boundary. | roles: Both white broken boundaries fit ordinary same-
                        direction lane dividers. | markings: No arrows, words, symbols or transverse markings
                        are discernible in my lane. | unseen: No markings are inferred beneath vehicles or
                        beyond the visible stretch; the lane endpoint is not visible. | result: consistent
Step 5  Rule            left_boundary: In mainland China, an ordinary broken white lane divider permits
                        crossing to change lanes when safe without obstructing other traffic.
Step 5  Rule            right_boundary: In mainland China, an ordinary broken white lane divider permits
                        crossing to change lanes when safe without obstructing other traffic.
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane divider permits changing into
                        the adjacent ordinary lane when safe.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits changing
                        into the adjacent ordinary lane when safe.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either broken divider may be crossed only after
                        checking that the adjacent lane is clear, especially for cyclists on the right. Turn-
                        lane requirements and any stopping point cannot be established from this view; follow
                        the markings and controls as they become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6424, out 802, 10.32 s

mapdr__EmergencyLane_00de2c5ef1554c3baf47ce85cfd98f67_1709711014547398000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese/English
                        Beichen West Road sign and road layout. My car is in the rightmost of three same-
                        direction expressway lanes, approaching an overpass, with an exit advertised 700 m
                        ahead. (lanes 3, mine 3, full)
Step 2  Left            A white broken line with visible dashes and gaps separates my lane from another
                        traffic lane on the left; white trapezoidal blocks flank the line in the foreground,
                        and there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with white trapezoidal blocks
                        alongside it; beyond it is a paved shoulder and then a concrete barrier, rather than a
                        curb directly bordering my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Repeated white trapezoidal blocks run along the inside edges of
                        my lane in the foreground, forming longitudinal speed-reduction markings; no
                        directional arrow or readable pavement text is visible.
Step 4  Cross-check     position: The lane line on the left and shoulder edge line on the right agree with my
                        lane being lane 3 of 3. | roles: The broken white divider fits a same-direction lane
                        line; the solid white line beside the shoulder fits an edge line. | markings: The
                        longitudinal speed-reduction blocks are compatible with both boundaries and do not
                        specify a turning movement. | unseen: No arrow, intersection stop line, or waiting
                        area is inferred beyond the visible road. | result: consistent
Step 5  Rule            left_boundary: Under Chinese road-marking rules, a broken white lane divider permits
                        changing into the adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: The solid white roadway edge line is not to be crossed into the
                        shoulder for ordinary driving.
Step 5  Rule            symbol:other: Longitudinal speed-reduction markings prompt drivers to reduce speed and
                        exercise caution without assigning a permitted turning direction.
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        lane change left.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits an ordinary move onto the
                        shoulder.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, reducing speed for the marked section and traffic ahead; change
                        left only when a safe gap exists, and stay off the shoulder. The sign advertises an
                        exit 700 m ahead, but no exit movement or turn permission is established by the
                        visible lane markings.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1024, 20.67 s

mapdr__EmergencyLane_01a2822a642a447286c55eeedab682e0_1710911921307783000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese roadside
                        signage and road layout. My car is in the third of four same-direction lanes on a
                        divided urban arterial continuing straight; no intersection or lane ending is clearly
                        visible ahead. (lanes 4, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; the solid white line and roadside curb lie farther
                        right, beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four same-direction lanes and ego position three agree with two lanes to the
                        left and one to the right; both immediate boundaries are lane lines. | roles: Both
                        boundaries are broken white lines, consistent with separation of ordinary same-
                        direction lanes. | markings: No arrows, words, symbols, transverse lines or waiting
                        areas are discernible in my lane; nothing conflicts with the boundary observations. |
                        unseen: No markings beneath vehicles or beyond the visible road have been inferred,
                        and no unseen intersection layout is assumed. | result: consistent
Step 5  Rule            left_boundary: Under Chinese road-marking rules, a broken white lane divider may be
                        crossed to change lanes when safe and without obstructing traffic.
Step 5  Rule            right_boundary: Under Chinese road-marking rules, a broken white lane divider may be
                        crossed to change lanes when safe and without obstructing traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing into the adjacent
                        ordinary lane when safe.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white lane divider permits crossing into
                        the adjacent ordinary lane when safe.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking in view governs this action.
Step 6  turn_right      not_applicable: No marking in view governs this action.
Step 6  u_turn          not_applicable: No marking in view governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent lane may be entered across its broken
                        white divider after checking traffic and blind spots. No turn guidance or stopping
                        point is visible, so reassess signs, signals and lane arrows when approaching the next
                        intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6424, out 920, 18.3 s

mapdr__EmergencyLane_063d5bdc545a47a9bf8c83a7fab5f7de_1709528622976528000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese bus-lane
                        lettering and road layout. My car is in the rightmost of three same-direction lanes on
                        a divided urban road; no intersection or lane ending is clearly visible ahead. (lanes
                        3, mine 3, full)
Step 2  Left            A yellow broken line, with several long painted blocks and intervening gaps visible,
                        separates my lane from another same-direction lane on the left.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 2  Right           A continuous white line runs along the right edge, with yellow broken blocks
                        immediately inside it; a paved roadside strip and then a raised curb lie beyond.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:other (partial): Partly cropped white numerals near the hood appear to form a
                        time restriction, but the complete inscription cannot be read.; text:bus (full): White
                        Chinese lettering running along the lane reads 公交专用, identifying a bus-only lane.
Step 4  Cross-check     position: Two lanes lie to the left, and the roadway edge lies to the right,
                        consistent with my lane being third and rightmost; its left boundary separates the bus
                        lane from general traffic. | roles: The yellow broken boundary fits a reserved-lane
                        boundary, while the continuous white line fits the roadway edge; the yellow blocks
                        beside that edge reinforce the reserved-lane delineation. | markings: The bus-only
                        lettering agrees with the yellow boundary treatment; no directional arrow or waiting
                        area is visible. | unseen: The full time inscription and any distant intersection
                        controls cannot be read and have not been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken reserved-lane boundary permits a vehicle already in
                        the lane to leave across it when safe.
Step 5  Rule            right_boundary: The continuous white roadway edge line must not be crossed for an
                        ordinary lane change or movement onto the roadside strip.
Step 5  Rule            text:other: A bus-lane time inscription specifies when the reservation operates, but
                        this incomplete inscription does not establish an exemption for my car.
Step 5  Rule            text:bus: The bus-only inscription identifies a reserved lane that an ordinary car
                        should not occupy during its reserved operation, but does not itself prescribe a
                        turning direction.
Step 6  change_left     allowed (contested, correct): The broken yellow reserved-lane boundary permits leaving
                        my lane for the general-traffic lane when safe.
Step 6  change_right    prohibited (contested, correct): The continuous white roadway edge prohibits crossing
                        onto the roadside strip.
Step 6  go_straight     allowed (contested, label prohibited): No visible directional marking restricts
                        continuing straight; the bus inscription governs lane eligibility rather than
                        direction.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: permission to proceed straight is directional only, not permission for an
                        ordinary car to remain in the reserved lane.
Advice                  As an ordinary car, move left into a general-traffic lane when safe rather than
                        assuming the bus-lane restriction is inactive. Do not cross the solid right edge;
                        turning permissions and any stopping point are not established by this view.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1242, 20.41 s

mapdr__EmergencyLane_065c41e605264418ad3dd675a41e3a2a_1711084342774609000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a divided expressway in mainland China, with right-hand traffic;
                        the blue registration plates and road infrastructure support that inference, though
                        the country is not certain. My car is in the third of four same-direction lanes, with
                        overhead gantries ahead and no visible intersection or lane ending. (lanes 4, mine 3,
                        full)
Step 2  Left            A single white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb borders my lane.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single pale yellowish broken line, with visible dashes and gaps, separates my lane
                        from the lane on the right; its paint colour is uncertain under the image tint, and no
                        curb borders my lane.
                        yellow dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and position three agree with a same-direction lane immediately
                        on each side of my lane. | roles: The left white broken line fits a lane divider. The
                        right line is also spatially a lane divider, although its yellowish appearance is
                        unusual and may reflect discolouration or image tint rather than yellow paint. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are visible in
                        my lane. | unseen: No intersection layout or movement restriction beyond the visible
                        road is inferred; the uncertainty in the right boundary's paint colour is retained. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken lane divider permits crossing to change lanes when
                        safe and without interfering with other traffic.
Step 5  Rule            right_boundary: The visible broken divider permits crossing when safe; its uncertain
                        white-versus-yellow colour does not by itself establish a no-crossing restriction.
Step 6  change_left     allowed (correct): The white broken lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken divider permits crossing into the adjacent lane when
                        safe; no solid line or reserved-lane marking is visible.
Step 6  go_straight     allowed (contested, correct): No visible arrow or lane-ending marking restricts
                        continuing along my lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the broken boundaries govern only lateral changes, and no unseen
                        intersection movements have been treated as permitted.
Advice                  Continue in this lane, or change one lane left or right only after checking traffic
                        and blind spots. No turn lane, waiting area or stopping point is visible; follow the
                        upcoming signs for any exit.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1031, 16.61 s

mapdr__EmergencyLane_0e7f925072374a2b95aad5b44a1e6b95_1711868840772150000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a divided expressway in China, with traffic keeping right, inferred
                        from the road layout, roadside infrastructure and distant signs; the country
                        identification is tentative. My car is in the third of four lanes in its direction,
                        with the roadway continuing ahead and no visible intersection or lane ending. (lanes
                        4, mine 3, full)
Step 2  Left            A broken white line, with long painted dashes and clear gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with long painted dashes and clear gaps, separates my lane from
                        another same-direction lane on the right; the shoulder and guardrail are beyond that
                        lane, not at my boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and position three agree with two same-direction lanes to the
                        left and one to the right; both immediate boundaries are lane lines. | roles: Both
                        white broken lines fit ordinary same-direction lane separators. | markings: No arrows,
                        words, symbols, transverse lines or marked waiting areas are visible in my lane, so
                        none contradict the boundaries. | unseen: No hidden lane markings or intersection
                        features have been inferred; the country identification remains tentative. | result:
                        consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane separator permits
                        crossing to change lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, a broken white lane separator
                        permits crossing to change lanes when safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane separator permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight, and the
                        lane continues ahead.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in your lane; either adjacent lane may be entered across its broken white
                        separator after checking mirrors, blind spots and safe gaps. No turning facility or
                        stopping point is visible, and the distant signs are too small to read reliably.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 879, 11.56 s

mapdr__EmergencyLane_1076a5f7a4cb4e80b5567db2953310a3_1711702619480155000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a divided expressway in China, with traffic keeping right; the
                        green-and-white chevron board and road layout support that inference, though the
                        country is not certain. My car is in the middle of three lanes approaching a gentle
                        left bend, with no intersection or lane ending visible. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane on the right; the shoulder and guardrail lie beyond that
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 2 agree with a same-direction lane across each
                        boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No obscured markings have been inferred; the distant
                        continuation is too small to inspect, and the country identification remains
                        tentative. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a white broken lane divider permits
                        crossing to change lanes when safe.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, a white broken lane divider permits
                        crossing to change lanes when safe.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane through the gentle left bend; either adjacent lane may be
                        entered after checking traffic and signalling. These lane markings do not authorize
                        turns or a U-turn across the expressway.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 789, 10.28 s

mapdr__EmergencyLane_12b11a695e1b4c9b82921a9180a2fc53_1711327197777677000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely China, with right-hand traffic, based on the Chinese/English direction
                        signs and road layout. My car is in the rightmost of two lanes on a barrier-lined road
                        approaching a fork, following the branch curving right. (lanes 2, mine 2, full)
Step 2  Left            A continuous white line borders my lane on the left, with another same-direction lane
                        beyond; farther ahead, white diagonal hatching opens outside this boundary at the
                        fork.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line curves right along my lane, with a paved shoulder and then a
                        concrete barrier beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my car
                        occupying lane 2 of 2. | roles: The solid white left line separates the same-direction
                        paths before the fork, while the solid white right line marks the shoulder edge. |
                        markings: No guidance marking is readable inside my lane; the diagonal hatching is
                        outside its left boundary. | unseen: Vehicles obscure some pavement ahead, and the
                        branch's eventual intersection or termination is not visible; no hidden arrows or
                        transverse lines are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes, and the channelized separation ahead must also be kept clear.
Step 5  Rule            right_boundary: The solid roadway edge line separates the travel lane from the
                        shoulder and prohibits crossing onto the shoulder in ordinary driving.
Step 6  change_left     prohibited (correct): The solid white lane boundary prohibits crossing left.
Step 6  change_right    prohibited (correct): The solid roadway edge prohibits moving onto the shoulder in
                        ordinary driving.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing along
                        this lane as it curves right.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action; following the road's curve is
                        not an intersection turn.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid white boundaries and follow the right-curving branch; do not
                        cross the hatched separation or enter the shoulder. Check the overhead destination
                        signs, and maintain space behind the vehicles ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 857, 18.58 s

mapdr__EmergencyLane_1a986017e476416fa6c2fc2bfe9fa1a8_1709705848977891000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a divided expressway in China, with traffic keeping right; the road
                        layout, roadside fittings and vehicle plates support this inference, but do not
                        establish the country conclusively. My car is in the middle of three lanes, with the
                        roadway continuing ahead and no visible intersection or lane ending. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the solid shoulder line and guardrail are beyond that
                        adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego lane index 2 agree with a lane line and
                        an adjacent traffic lane on each side. | roles: Both white broken boundaries fit
                        ordinary same-direction lane dividers. | markings: No arrows, words, symbols,
                        transverse lines or waiting areas are visible in my lane. | unseen: No distant or
                        vehicle-obscured marking has been inferred; the country identification remains
                        tentative. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        changing into the adjacent left lane when safe and without obstructing traffic.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        changing into the adjacent right lane when safe and without obstructing traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No arrow or other visible marking restricts continuing
                        straight along this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action, and no intersection is visible.
Step 6  turn_right      not_applicable: No marking governs this action, and no intersection is visible.
Step 6  u_turn          not_applicable: No marking governs this action; no U-turn opening is visible.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: lane-change permissions follow the broken dividers, straight travel is
                        unrestricted by visible markings, and ungoverned turning and waiting-area actions are
                        not applicable.
Advice                  Continue in the middle lane; either adjacent lane may be entered across its broken
                        white divider after checking mirrors, blind spots and available space. No stop
                        location or turning facility is visible; these marking-based permissions do not
                        authorize turning or making a U-turn on the expressway.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 839, 15.59 s

mapdr__EmergencyLane_2a1f8894096d46a29efc130923b0ea53_1711583176493111000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, with traffic keeping right, suggested by the green vehicle
                        plates, motorway signs and road layout. My car is in the rightmost of three lanes on a
                        divided motorway, with slow traffic and an overpass ahead; no intersection or lane
                        ending is visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with clear dashes and gaps, separates my lane from another same-
                        direction traffic lane; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved shoulder and then a
                        guardrail beyond it; no curb forms the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 3 agree with a same-direction lane on the left and
                        a shoulder on the right. | roles: The broken white divider fits a lane line, and the
                        continuous white shoulder boundary fits an edge line. | markings: No recognizable
                        guidance markings are visible within my lane, so none conflict with the boundaries. |
                        unseen: No hidden arrows or lane-end features are inferred; vehicles obscure the more
                        distant pavement. | result: consistent
Step 5  Rule            left_boundary: Under the inferred mainland Chinese rules, the broken white lane
                        divider permits changing left when safe and without obstructing traffic.
Step 5  Rule            right_boundary: The motorway edge line separates the traffic lane from the shoulder,
                        which an ordinary car must not enter for routine driving or overtaking.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (WRONG, label allowed): The right edge bounds a motorway shoulder, which is
                        not available for routine driving.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along my lane, and
                        no lane ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, allowing extra stopping distance for the slowing traffic ahead.
                        Change left only after checking the adjacent traffic and blind spot; do not use the
                        right shoulder for ordinary travel.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 812, 16.22 s

mapdr__EmergencyLane_2cdbb32e26484b9ea447532500f89f36_1710919190859410000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, inferred from the Chinese writing
                        and road infrastructure. My car is on a single-lane elevated ramp curving left, with
                        barriers on both sides and no visible intersection or lane ending. (lanes 1, mine 1,
                        full)
Step 2  Left            A continuous white edge line follows the left curve beside a concrete barrier and
                        metal rail; short white rectangular blocks run alongside it on the lane side.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white edge line follows the right side, with short white rectangular
                        blocks on its lane side and a paved shoulder extending to a concrete barrier beyond.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Repeated short white rectangular blocks run longitudinally along
                        both sides inside the solid edge lines, forming visual narrowing markings through the
                        curve.
Step 4  Cross-check     position: One lane and ego position 1 agree with edge lines on both sides; the
                        pavement outside the right edge line is a shoulder, not another marked travel lane. |
                        roles: The continuous white lines fit roadway edge lines; the separate rectangular
                        blocks do not make these boundaries dashed. | markings: The paired rows of narrowing
                        blocks are consistent with a curved ramp and do not indicate turn choices or another
                        lane. | unseen: No arrows, words, stop lines, intersection or waiting area are
                        visible; none have been inferred. The reddish pavement patches are not interpreted as
                        directional markings. | result: consistent
Step 5  Rule            left_boundary: On this Chinese ramp, the solid roadway edge and physical barrier
                        prohibit leaving the travel lane to the left.
Step 5  Rule            right_boundary: The solid roadway edge separates the travel lane from the shoulder,
                        which is not available for ordinary driving or a lane change.
Step 5  Rule            symbol:other: The longitudinal visual-narrowing markings warn drivers to reduce speed
                        through the curve but do not assign permitted turning movements.
Step 6  change_left     prohibited (WRONG, label allowed): The solid left roadway edge and barrier prohibit
                        leaving the lane to the left.
Step 6  change_right    prohibited (correct): The solid right roadway edge borders a shoulder, not an
                        available traffic lane.
Step 6  go_straight     allowed (contested, correct): No directional arrow restricts continuing along this
                        lane; following its leftward curve is continuing along the lane, not a left turn.
Step 6  turn_left       not_applicable: No marking governs this action, and no intersection is visible.
Step 6  turn_right      not_applicable: No marking governs this action, and no intersection is visible.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the single marked lane and follow the leftward curve at reduced speed,
                        maintaining space behind the vehicles ahead. Do not cross either edge line or use the
                        right shoulder as a travel lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 978, 21.19 s

mapdr__EmergencyLane_329feffbfc454c62a33eec5906e4ba06_1709888677701261000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the road-marking style,
                        vehicles and roadside signs. My car is in the rightmost of three lanes on a divided
                        road curving gently right; no intersection or lane ending is clearly visible ahead.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane; broad white rectangular markings run alongside it.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane, with repeated broad white blocks on its lane-
                        facing side and a paved shoulder followed by a guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        symbol:other (full): Repeated broad white rectangular blocks run longitudinally along
                        both margins inside my lane, forming a visual narrowing pattern.
Step 4  Cross-check     position: The lane line on the left and shoulder edge line on the right agree with my
                        car occupying lane 3 of 3. | roles: The broken white separator fits a same-direction
                        lane line, and the solid white line beside the shoulder fits a roadway edge line. |
                        markings: The paired rows of rectangular blocks are consistent with longitudinal
                        speed-reduction markings, not additional lanes or movement arrows. | unseen: No
                        directional arrow or transverse stopping marking is readable in my lane; the distant
                        road beyond the visible stretch is not assessed. | result: consistent
Step 5  Rule            left_boundary: Under Chinese marking rules, a broken white lane divider permits
                        crossing to change lanes when safe.
Step 5  Rule            right_boundary: The solid white roadway edge line must not be crossed for ordinary
                        driving onto the shoulder.
Step 5  Rule            symbol:other: Longitudinal speed-reduction markings prompt drivers to slow down but do
                        not assign permitted turning movements.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid roadway edge line prohibits an ordinary
                        move onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue along the right-curving lane and slow appropriately for the speed-reduction
                        markings and traffic ahead; the roadside sign appears to show a 60 km/h limit. Change
                        left only when safe, and do not cross the right edge line onto the shoulder.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 939, 12.5 s

mapdr__EmergencyLane_3acbbcc1e38b4321810120e62c24d64f_1710734161121759000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           Likely China, with right-hand traffic, judging from the Chinese-script green highway
                        sign and divided-road layout. My car is in the middle of three same-direction lanes on
                        an expressway; the roadway continues ahead, with no visible intersection or lane
                        ending. (lanes 3, mine 2, full)
Step 2  Left            A single white broken line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane on the right; the solid outer edge line and
                        guardrail lie farther beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lane-line boundaries agree with my car occupying lane 2 of 3, with one
                        same-direction lane on each side. | roles: Both white broken boundaries fit ordinary
                        same-direction lane separators. | markings: No arrows, words, symbols, transverse
                        lines or marked waiting areas are visible in my lane. | unseen: No distant
                        intersection layout or unreadable sign instruction has been inferred; the country
                        identification is tentative. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The broken white left lane separator permits a safe lane change.
Step 6  change_right    allowed (correct): The broken white right lane separator permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow or lane-ending marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane; either broken boundary permits a lane change after checking
                        mirrors, blind spots and safe gaps, especially beside the car on the left. No stopping
                        point or turning facility is visible; follow highway signs for upcoming exits.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 771, 10.82 s

mapdr__EmergencyLane_3bb16e3f99b54b9cbe2ce804992d6343_1709700343511596000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           Likely China, with traffic keeping right, based on the expressway layout, roadside
                        structures and surrounding buildings, although the country is not certain. My car is
                        in the middle of three same-direction lanes on a barrier-lined urban expressway; the
                        road continues ahead with no visible intersection or lane ending. (lanes 3, mine 2,
                        full)
Step 2  Left            A single white broken line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane across
                        each boundary. | roles: Both white broken boundaries fit ordinary same-direction lane-
                        divider roles. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are discernible in my lane. | unseen: No distant intersection layout or
                        hidden marking is inferred; the country identification remains tentative. | result:
                        consistent
Step 5  Rule            left_boundary: Under the likely Chinese rules, a white broken lane divider permits
                        crossing to the adjacent lane when safe and without interfering with traffic.
Step 5  Rule            right_boundary: Under the likely Chinese rules, a white broken lane divider permits
                        crossing to the adjacent lane when safe and without interfering with traffic.
Step 6  change_left     allowed (correct): The white broken lane divider permits a safe change into the
                        adjacent ordinary lane.
Step 6  change_right    allowed (WRONG, label not_determined): The white broken lane divider permits a safe
                        change into the adjacent ordinary lane.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along the visible
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action, and no intersection is visible.
Step 6  turn_right      not_applicable: No marking governs this action, and no intersection is visible.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either adjacent lane may be entered across its broken
                        divider after checking mirrors, blind spots and available space. No turn or stopping
                        location is shown; follow subsequent signs and markings.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 780, 13.61 s

mapdr__EmergencyLane_4cee791d67694060a619326f3bf99d76_1709869395130753000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the divided-road
                        layout, roadside signs and barrier design, though the country is not certain. My car
                        is in the rightmost of three lanes on a divided highway bending gently left, with no
                        intersection or lane ending visible. (lanes 3, mine 3, full)
Step 2  Left            A single white broken line, with clearly visible dashes and gaps, separates my lane
                        from another same-direction lane on the left; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous single white line borders my lane on the right, with a paved shoulder and
                        then a guardrail and noise barrier beyond it; no curb directly borders the lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 3 agree with a same-direction lane line on the
                        left and a roadway edge line on the right. | roles: The broken white line fits a same-
                        direction lane separator, and the continuous white line alongside the shoulder fits a
                        roadway edge. | markings: No arrows, words, symbols or transverse markings are visible
                        in my lane; nothing contradicts the boundaries. | unseen: No markings are inferred
                        beyond the visible stretch; the country identification remains tentative. | result:
                        consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane separator permits
                        changing left when safe.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, the solid roadway edge line
                        prohibits crossing onto the shoulder during ordinary driving.
Step 6  change_left     allowed (correct): The broken white lane separator permits crossing into the adjacent
                        lane when safe.
Step 6  change_right    prohibited (correct): The solid white roadway edge line prohibits an ordinary move
                        onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along my lane, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the current lane through the gentle left bend, or change left across the
                        broken line after checking traffic. Stay inside the solid right edge line and keep the
                        shoulder clear.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 830, 12.39 s

mapdr__EmergencyLane_4ff65188dbf04bf1a5a6840cd07de3fc_1709873700987803000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, suggested by the simplified Chinese
                        construction sign and road-marking style. My car is on a single-lane, barrier-lined
                        ramp curving left, with a broad paved strip outside the right edge line and no
                        intersection visible. (lanes 1, mine 1, partial)
Step 2  Left            A continuous white line follows the left concrete barrier, with repeated white
                        rectangular markings just inside it; a guardrail and separated roadway lie beyond the
                        barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line curves left, with repeated white rectangular markings on its
                        lane side; a broad paved strip extends beyond it to a concrete barrier.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        symbol:other (full): Repeated white rectangular blocks run along the inside of the
                        left boundary as longitudinal speed-reduction markings.; symbol:other (full): Repeated
                        white rectangular blocks run along the inside of the right boundary as longitudinal
                        speed-reduction markings.; symbol:other (partial): A group of closely spaced pale
                        transverse bars spans the lane ahead, with a reddish pavement band beside them; these
                        are speed-reduction markings rather than a single stop line.
Step 4  Cross-check     position: The left barrier makes this the leftmost lane. The solid right line and
                        paired speed-reduction blocks suggest a single marked travel lane, although the
                        function of the broad paved strip to the right is not fully established. | roles:
                        White continuous lines fit ramp edge lines; neither boundary visibly separates
                        opposing traffic. | markings: The longitudinal blocks and transverse bars consistently
                        warn of reduced speed on the curve; no directional arrow or waiting area is visible. |
                        unseen: The right paved strip is provisionally treated as a shoulder, not asserted to
                        be a confirmed second travel lane. The distant continuation is not fully visible. |
                        result: Consistent, with partial evidence for the right boundary's role and the total
                        lane count.
Step 5  Rule            left_boundary: The solid edge line and concrete barrier prohibit leaving the lane to
                        the left.
Step 5  Rule            right_boundary: Under the apparent Chinese ramp marking arrangement, the solid roadway
                        edge line is not to be crossed for ordinary driving onto the paved shoulder.
Step 5  Rule            symbol:other: The left longitudinal speed-reduction blocks prompt reduced speed but do
                        not assign a turning movement.
Step 5  Rule            symbol:other: The right longitudinal speed-reduction blocks prompt reduced speed but
                        do not independently govern lane changes or turns.
Step 5  Rule            symbol:other: The transverse speed-reduction bars warn drivers to slow down and do not
                        require a full stop.
Step 6  change_left     prohibited (WRONG, label allowed): The solid left edge line and concrete barrier
                        prohibit crossing to the left.
Step 6  change_right    prohibited (correct): The continuous right edge line prohibits ordinary movement onto
                        the apparent shoulder.
Step 6  go_straight     allowed (contested, correct): No directional arrow restricts continuing along the
                        ramp; following its leftward curve is continuing in the lane.
Step 6  turn_left       not_applicable: No marking governs a left turn at an intersection.
Step 6  turn_right      not_applicable: No marking governs a right turn at an intersection.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary restrictions govern only lateral departures, the speed-reduction
                        markings do not require stopping, and continuing means following the ramp rather than
                        driving geometrically straight.
Advice                  Stay between the solid white lines and follow the leftward curve; do not use the paved
                        strip on the right as another lane. Slow for the reduction markings and the posted 30
                        km/h limit; no mandatory stopping marking is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1239, 17.57 s

mapdr__EmergencyLane_50aad8191b454f58b226fce7d06ee921_1711342170440912000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely China, with right-hand traffic, suggested by the Chinese writing on the
                        coach and the road layout. My car is following the coach on a single-lane, guardrail-
                        lined ramp or connector; its continuation is partly hidden, and no intersection is
                        visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous pale white solid line borders the lane on the left, with a narrow paved
                        margin, raised curb and metal guardrail beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white solid line borders the lane on the right, with a paved shoulder,
                        raised curb and metal guardrail beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Edge lines on both sides agree with one lane in this direction and my car
                        occupying lane 1. | roles: The continuous white lines beside narrow margins and
                        guardrails fit roadway edge lines rather than lane dividers. | markings: No guidance
                        markings are visible within my lane, so there is no conflict with the boundaries. |
                        unseen: The coach hides part of the roadway ahead; no markings or junction arrangement
                        are inferred beneath or beyond it. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, the solid roadway edge line restricts
                        ordinary crossing onto the margin, and the curb and guardrail are not a drivable lane.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, the solid roadway edge line
                        restricts ordinary crossing onto the shoulder, and the curb and guardrail prevent
                        leaving the roadway.
Step 6  change_left     prohibited (correct): The solid left edge line and physical roadway edge prohibit an
                        ordinary move out to the left.
Step 6  change_right    prohibited (correct): The solid right edge line prohibits an ordinary move onto the
                        shoulder.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along this lane;
                        its edge lines do not prohibit forward travel.
Step 6  turn_left       not_applicable: No marking governs this action in the visible stretch.
Step 6  turn_right      not_applicable: No marking governs this action in the visible stretch.
Step 6  u_turn          not_applicable: No marking governs this action in the visible stretch.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within this single lane without crossing either solid edge line. Keep
                        sufficient distance behind the coach to see the road ahead; no turning facility or
                        stopping location is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 832, 12.67 s

mapdr__EmergencyLane_80df0005fc3d450fae05a675aebf7994_1710212735808183000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, inferred from the
                        simplified Chinese overhead signs and expressway layout. My car is in the second of
                        four general-traffic lanes on an elevated divided expressway continuing straight, with
                        an emergency lane on the far right and no visible junction or lane ending. (lanes 4,
                        mine 2, full)
Step 2  Left            A single white broken line, with long dashes and visible gaps, separates my lane from
                        another general-traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with long dashes and visible gaps, separates my lane from
                        another general-traffic lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The second of four general-traffic lanes has an adjacent same-direction lane
                        on each side, consistent with both boundaries being lane lines. | roles: Both white
                        broken boundaries fit same-direction lane separation. | markings: No pavement arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane; the overhead
                        arrows are signs, not pavement markings. | unseen: No unseen pavement markings or
                        intersection layout have been inferred; the distant continuation is too small to
                        inspect in detail. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing into
                        the adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: In mainland China, a broken white lane divider permits crossing into
                        the adjacent same-direction lane when safe.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        general-traffic lane on the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        general-traffic lane on the right.
Step 6  go_straight     allowed (contested, correct): No pavement arrow or lane-ending marking restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No pavement marking governs this action, and no intersection is
                        visible.
Step 6  turn_right      not_applicable: No pavement marking governs this action, and no intersection is
                        visible.
Step 6  u_turn          not_applicable: No pavement marking governs this action; this is not permission to
                        make a U-turn on the expressway.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in your current lane; either adjacent general-traffic lane may be entered
                        after checking traffic and signalling. Observe the overhead lane-specific speed signs,
                        keep out of the emergency lane, and use a designated exit rather than attempting a
                        turn or U-turn here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 862, 15.53 s

mapdr__MultiLane_054e381d007742419c83604796aef772_1709777355676042000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           Likely China, with traffic keeping right, supported by Chinese signage and the vehicle
                        layout. My car is in the leftmost of two lanes on an urban side roadway beside a
                        planted divider, approaching an overpass; no intersection or lane ending is clearly
                        visible. (lanes 2, mine 1, full)
Step 2  Left            A faded solid yellow line runs beside a raised planted-divider curb on the left, with
                        a separate roadway beyond.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A worn but continuous solid white line separates my lane from the lane on the right,
                        where several vans are visible.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my car
                        occupying lane 1 of 2. | roles: The yellow line beside the divider is consistent with
                        a roadway edge, and the white line separates lanes traveling in the same direction. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are visible in
                        my lane. | unseen: No movement restrictions or intersection layout have been inferred
                        from the distant, partly obscured roadway. | result: consistent
Step 5  Rule            left_boundary: The raised divider and its yellow edge prohibit leaving the lane across
                        the left boundary.
Step 5  Rule            right_boundary: Under Chinese road-marking rules, a solid white lane-separation line
                        prohibits crossing it to change lanes.
Step 6  change_left     prohibited (WRONG, label not_determined): The raised divider prevents crossing the
                        left boundary.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white lane line prohibits crossing
                        to the right.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or lane ending restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane without crossing the solid white line or the divider edge.
                        No turn guidance or stopping point is visible; reassess the markings as the roadway
                        ahead becomes clearer.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 776, 10.49 s

mapdr__MultiLane_08b632e49f4743498ed405f0c22928df_1709685444115806000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the blue plates,
                        Chinese roadside writing and road layout. My car is in a single motor-vehicle lane on
                        a separated side carriageway, with a parallel carriageway beyond the left divider and
                        a strip used by scooters on the right; the next intersection is not clearly visible.
                        (lanes 1, mine 1, full)
Step 2  Left            A continuous white line runs beside a raised concrete planted divider on the left,
                        with a parallel carriageway beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from a roadside strip occupied by scooters;
                        the raised sidewalk curb is beyond that strip, not directly against my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane, indexed 1, agrees with a divider-side edge on the
                        left and an edge adjoining the scooter strip on the right; the parallel carriageway is
                        physically separate. | roles: The white continuous lines fit roadway-edge boundaries
                        rather than an opposing-traffic center line. | markings: No readable arrows, words,
                        symbols or transverse markings are visible in my lane. | unseen: No intersection
                        layout or guidance hidden beneath the vehicle ahead is inferred. | result: consistent
Step 5  Rule            left_boundary: In China, the raised divider is a physical roadway boundary and must
                        not be crossed to leave this lane.
Step 5  Rule            right_boundary: The continuous white boundary separating the motor-vehicle lane from
                        the roadside non-motorized strip prohibits an ordinary car from moving across it along
                        this stretch.
Step 6  change_left     prohibited (correct): The raised divider prohibits crossing the left boundary.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white edge separates my lane from
                        the non-motorized strip and prohibits crossing here.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane, keeping clear of the divider and scooters; do not cross
                        either boundary here. Turning arrangements and any required stopping point are not
                        visible, so reassess when the next junction comes into view.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 877, 13.24 s

mapdr__MultiLane_098a159b6c274183a94acd1983790d70_1711157385414762000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, suggested by the Chinese writing
                        and traffic arrangement. My car is in the leftmost of two same-direction motor-vehicle
                        lanes on a divided urban road beneath a pedestrian bridge; no intersection or lane
                        ending is visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A single solid yellow line follows the raised curb of a planted median on the left,
                        with the opposite carriageway beyond the median.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with long dashes and clear gaps, separates my lane from another
                        same-direction lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and a same-direction lane on the right agree
                        with my lane being lane 1 of 2. | roles: The solid yellow median-edge marking and
                        broken white lane divider fit their assigned roles. | markings: No guidance markings
                        are visible within my lane, so none conflict with the boundaries. | unseen: No
                        markings or intersection features have been inferred beyond the visible road; the
                        country identification is an inference. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, the solid median-edge line and raised
                        median prohibit leaving the lane across this boundary.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent
                        ordinary lane when safe and without interfering with traffic.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid median-edge line and raised curb
                        prohibit crossing the left boundary.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        lane change to the right.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane for the visible straight route; do not cross the median
                        boundary. A rightward lane change is permitted by the dashed line, but check carefully
                        for scooters and other traffic before moving.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 792, 14.91 s

mapdr__MultiLane_17ec82fa09a8451ab2e2b464343ad02c_1709855464277303000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese writing and road furniture,
                        with traffic keeping right. My car is in a single motor-vehicle lane on a narrow urban
                        roadway approaching a 2.5 m height-restriction gantry; no intersection or lane ending
                        is clearly visible ahead. (lanes 1, mine 1, full)
Step 2  Left            A continuous white line runs beside a raised paved divider with a metal fence; another
                        roadway lies beyond the divider.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from a narrow roadside strip occupied by a
                        scooter rider, with a raised sidewalk farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane, bounded by roadway edges on both sides, agrees with
                        my lane being the first and only lane of my direction here. | roles: The white
                        continuous lines fit roadway-edge boundaries; the left boundary also has a physical
                        divider. | markings: No readable arrows, words, symbols, transverse lines or waiting
                        areas are visible in my lane. | unseen: The roadside strip has no readable bicycle
                        symbol, so its exact designation is not asserted; the distant lane endpoint is not
                        visible clearly. | result: consistent
Step 5  Rule            left_boundary: The raised divider forms a physical roadway edge and prohibits leaving
                        my lane across it.
Step 5  Rule            right_boundary: The solid white roadway-edge line does not permit an ordinary lane
                        change into the roadside strip.
Step 6  change_left     prohibited (correct): The raised divider at the left edge prohibits crossing.
Step 6  change_right    prohibited (correct): The solid white right edge separates the travel lane from the
                        roadside strip and prohibits an ordinary lane change across it.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other lane marking restricts
                        continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the marked motor-vehicle lane without crossing either edge, keeping
                        clear of the scooter rider on the right. Check that your vehicle clears the posted 2.5
                        m restriction before proceeding beneath the gantry; no turning guidance or stopping
                        line is visible here.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 818, 17.05 s

mapdr__MultiLane_2091fbc8531b4d4788d8f5faac11e5a1_1709693251047744000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese writing,
                        streetscape and vehicle positioning. My car is in the left of two apparent lanes on a
                        barrier-separated side carriageway, following a taxi past a pedestrian footbridge; no
                        intersection or lane ending is clearly visible ahead. (lanes 2, mine 1, partial)
Step 2  Left            A continuous raised concrete barrier forms the left side of my lane, with another
                        carriageway beyond; no painted boundary is clearly visible beside it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A worn white line appears continuous along the right side of my lane, with a paved
                        strip or possible second lane beyond it and a raised sidewalk farther right; the
                        line's distant continuation is obscured.
                        white solid, curb no, unknown, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left barrier places my car at the left edge of this side carriageway.
                        Two lanes are apparent, but whether the paved space beyond the right white line is
                        another motor-vehicle lane is uncertain. | roles: The physical left barrier fits a
                        roadway edge. The white right line is visible, but its role as a lane divider or a
                        boundary to a non-motorized strip cannot be established. | markings: No readable
                        arrows, words, symbols or transverse markings are visible in my lane. | unseen: No
                        lane-use designation is assumed for the paved strip on the right, and no intersection
                        markings are inferred beyond the taxi. | result: consistent
Step 5  Rule            left_boundary: A raised concrete barrier is a physical roadway boundary that my car
                        must not cross.
Step 5  Rule            right_boundary: In China a solid white lane divider prohibits crossing, but an edge
                        marking has a different function, so the uncertain role of this worn line prevents a
                        firm crossing decision.
Step 6  change_left     prohibited (correct): The raised concrete barrier prohibits leaving my lane to the
                        left.
Step 6  change_right    not_determined (WRONG, label prohibited): The right line's role and the designation of
                        the paved strip beyond it are uncertain.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other lane-use marking restricts
                        continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the left barrier prohibits crossing, uncertainty about the right boundary
                        leaves crossing undecided, and no unseen turn restriction or permission is inferred.
Advice                  Continue behind the taxi within the present lane; do not cross the left barrier, and
                        avoid moving right until the line and adjacent strip's designation are clear. No turn
                        lane or stopping point can be identified from this view.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 972, 13.83 s

mapdr__MultiLane_4bbd379e3c274e198dea80522b9967aa_1710219509478038000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely mainland China, with right-hand traffic, supported by the Chinese
                        storefront text and Bank of Beijing signs. My car is in the leftmost of two same-
                        direction motor-vehicle lanes on a divided urban road continuing ahead; no
                        intersection or lane ending is clearly visible. (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs beside a raised median curb with planting beyond it; the
                        opposite carriageway lies beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and intervening gaps, separates my lane from
                        the same-direction lane occupied by the black sedan; there is no curb at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median-side left edge and a same-direction lane across the right
                        boundary agree with my lane being lane 1 of 2. | roles: The solid white median-side
                        edge line and broken white same-direction lane divider fit their assigned roles. |
                        markings: No guidance markings are visible within my lane, so there is no conflict
                        with the boundaries. | unseen: No markings or intersection layout beyond the visible
                        stretch have been inferred; glare obscures some foreground pavement. | result:
                        consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised median prohibit leaving my lane
                        across the left boundary.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent
                        ordinary traffic lane when safe.
Step 6  change_left     prohibited (WRONG, label allowed): The solid left edge and raised median prohibit
                        crossing this boundary.
Step 6  change_right    allowed (correct): The broken white divider permits a safe lane change to the right.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane; do not cross the median-side boundary. A right lane change is
                        permitted only when clear of the black sedan and other traffic; the roadside speed-
                        limit sign shows 50 km/h.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 835, 11.89 s

mapdr__MultiLane_58ca0d6f04fc4605a76bc1b7899b0dfe_1709854271926265000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the vehicle
                        plates, Chinese lettering and road layout. My car is in the single motor-vehicle lane
                        of this carriageway, with a planted divider on the left and a separated non-motorized
                        strip on the right; no intersection or lane ending is clearly visible ahead. (lanes 1,
                        mine 1, full)
Step 2  Left            A continuous raised concrete curb borders the planted divider on the left; a pale
                        strip at its base is indistinct and cannot confidently be identified as painted road
                        marking.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A single continuous white solid line separates my lane from the paved strip used by
                        scooters on the right; the sidewalk curb lies beyond that strip, not directly against
                        my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane, bounded by a planted-divider curb on the left and a
                        non-motorized strip on the right, agrees with ego lane index 1. | roles: The raised
                        left edge and solid white right edge fit roadway-edge roles rather than same-direction
                        motor-lane dividers. | markings: No readable arrows, words, symbols, transverse lines
                        or waiting areas are visible in my lane. | unseen: The pale strip beside the left curb
                        is not treated as confirmed paint, and no markings are inferred beyond the visible
                        stretch. | result: consistent
Step 5  Rule            left_boundary: The raised divider curb is a physical roadway boundary that my car must
                        not cross.
Step 5  Rule            right_boundary: Under the inferred Chinese road rules, the solid white boundary to the
                        non-motorized strip prohibits my car from crossing into that strip along this stretch.
Step 6  change_left     prohibited (correct): The raised divider curb prohibits crossing the left boundary.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white boundary separates my car
                        from the non-motorized strip and prohibits crossing it here.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or other marking restricts
                        continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within the motor-vehicle lane without crossing the divider curb or the solid
                        white line beside the scooters. No turning guidance or stopping line is visible;
                        reassess when the next junction and its markings become clear.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 901, 12.57 s

mapdr__MultiLane_6085c35e887343e79989022e3a580bad_1711172164820827000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, with right-hand traffic, based on the Chinese writing, blue
                        lane-allocation sign and road layout. My car is in the middle of three motor-vehicle
                        lanes on a straight urban road beside an elevated roadway; no intersection or lane
                        ending is clearly visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A white broken line with visible dashes and gaps separates my lane from another motor-
                        vehicle lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with visible dashes and gaps separates my lane from another motor-
                        vehicle lane on the right; the solid white line and roadside curb lie farther right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small, distant white arrow appears to point straight ahead
                        in my lane; its detail is limited by distance.
Step 4  Cross-check     position: Three motor-vehicle lanes and position 2 agree with having an ordinary lane
                        line on each side. | roles: Both white broken boundaries fit separators between lanes
                        travelling in the same direction. | markings: The apparent straight-ahead arrow is
                        compatible with the lane continuing between the two broken boundaries. | unseen: The
                        distant arrow's complete head configuration and the eventual junction markings cannot
                        be confirmed; neither is inferred from the overhead sign. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane separator permits crossing to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A broken white lane separator permits changing into the adjacent
                        ordinary traffic lane when safe.
Step 5  Rule            arrow:straight: A straight-only lane arrow requires proceeding straight, but
                        additional arrowheads must be ruled out before treating this distant marking as a
                        confirmed turning restriction.
Step 6  change_left     allowed (correct): The white broken left lane separator permits a safe lane change.
Step 6  change_right    allowed (WRONG, label prohibited): The white broken right lane separator permits a
                        safe lane change.
Step 6  go_straight     allowed (contested, correct): The visible forward-pointing portion of the arrow
                        supports continuing straight.
Step 6  turn_left       not_determined: The distant arrow's complete head configuration is not clear enough to
                        confirm whether a left branch exists.
Step 6  turn_right      not_determined: The distant arrow's complete head configuration is not clear enough to
                        confirm whether a right branch exists.
Step 6  u_turn          not_determined: The distant guidance marking is not sufficiently resolved to decide
                        all permitted movements.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent motor-vehicle lane can be reached
                        across the broken line after checking for traffic. Confirm the distant arrows before
                        selecting a turning lane, and keep clear of the non-motorized space beyond the far-
                        right solid line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions False, unsafe ['change_right'], citation None,
                        contradictions []
Tokens                  in 6424, out 1054, 14.38 s

mapdr__MultiLane_69f3684158b54119b533ae2fc2455671_1711065856681727000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely mainland China, with right-hand traffic, based on the Chinese writing
                        and road signs. My car is in the single motor-vehicle lane of a separated urban
                        roadway, with a non-motorized lane to the right; the road continues ahead, but the
                        next intersection is not visible. (lanes 1, mine 1, full)
Step 2  Left            A solid white line runs along the left side of my lane, beside a raised curb and
                        planted separation strip.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the paved strip used by bicycles and
                        scooters on the right; there is no curb at this line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow near the bottom of my lane has a single head
                        pointing straight ahead.
Step 4  Cross-check     position: One motor-vehicle lane, indexed 1, agrees with an edge boundary on each
                        side; the strip to the right is a non-motorized lane, not another general-traffic
                        lane. | roles: The solid white boundaries fit the roadway edge on the left and
                        motor/non-motor separation on the right. | markings: The straight arrow agrees with
                        continuing along the motor-vehicle lane; no conflicting words, arrows, or waiting-area
                        markings are visible. | unseen: No unseen intersection markings have been inferred;
                        the distant roadway is too small and partly obscured to inventory beyond the visible
                        stretch. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised curb do not permit my car to leave
                        the lane to the left.
Step 5  Rule            right_boundary: The solid motor/non-motor separation line prohibits crossing right
                        into the non-motorized lane.
Step 5  Rule            arrow:straight: The straight-only guidance arrow permits straight-ahead travel and
                        excludes left turns, right turns, and U-turns from this lane.
Step 6  change_left     prohibited (correct): The solid edge line and raised curb prohibit leaving the lane to
                        the left.
Step 6  change_right    prohibited (contested, correct): The solid boundary to the non-motorized lane
                        prohibits crossing right.
Step 6  go_straight     allowed (correct): The single straight-ahead arrow permits continuing straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight within the motor-vehicle lane without crossing either boundary. Give
                        ample space to the cyclists and scooter riders ahead, and reassess any intersection
                        controls when they become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1003, 14.28 s

mapdr__MultiLane_6d78ed924c8f490081cf9750e1f0d0da_1710733680991016000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be Beijing, China, with right-hand traffic, based on the Chinese
                        street names and road layout. My car is in a narrow, barrier-separated roadside
                        carriageway with one moving lane; parked vehicles occupy the strip on the right, and
                        the lane continues ahead with its distant end obscured. (lanes 1, mine 1, full)
Step 2  Left            A continuous yellow line follows the raised concrete barrier on the left, with a
                        separate carriageway beyond the barrier.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous yellow line separates my lane from a curbside strip occupied by parked
                        cars; the sidewalk curb is beyond that strip, not immediately beside my lane.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One moving lane bounded by roadway edges agrees with my lane being both the
                        leftmost and rightmost lane of this separated carriageway. | roles: The left barrier
                        establishes a physical roadway edge; the right line borders a parked-vehicle strip
                        rather than another moving lane. Yellow edge paint is compatible with roadside
                        stopping restrictions in China. | markings: No guidance marking is visible in the
                        exposed portion of my lane. | unseen: The vehicle ahead hides some pavement, and the
                        distant intersection and lane-end markings cannot be read; no hidden arrows or
                        transverse lines are assumed. | result: consistent
Step 5  Rule            left_boundary: The raised barrier forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            right_boundary: A yellow solid roadside edge line in China indicates a no-stopping
                        restriction rather than, by itself, a prohibition on crossing the edge to access the
                        roadside.
Step 6  change_left     prohibited (correct): The concrete barrier prohibits leaving the lane to the left.
Step 6  change_right    allowed (contested, label prohibited): The roadside edge line does not itself prohibit
                        crossing it, although parked vehicles obstruct the strip beyond it.
Step 6  go_straight     allowed (contested, correct): No visible lane arrow or other marking restricts
                        continuing straight along this lane.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: crossing permission is distinguished from a safe opportunity, and no
                        unseen intersection movement is inferred.
Advice                  Continue cautiously behind the car ahead; do not cross the left barrier or move into
                        the occupied curbside strip. Do not stop along the yellow edge, and reassess turn
                        guidance when the intersection and its markings become visible.
Score                   lane False, boundaries {'left': False, 'right': None}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 999, 15.88 s

mapdr__MultiLane_7f0434d460cb4b92b68544ef77217c50_1709798720694368000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese storefront lettering and road
                        signs, with traffic keeping right. My car is in a single through lane on a landscaped
                        urban side roadway, with a row of parked vehicles on the right; the next intersection
                        is not clearly visible. (lanes 1, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised curb and landscaped strip on the left,
                        with another roadway beyond the strip.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears continuous along the right side of my lane, with a closely spaced
                        row of stationary vehicles beyond it; vehicles obscure portions of the line and the
                        outer road edge.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left edge beside landscaping makes my lane the leftmost lane on this
                        roadway; treating the space occupied by the stationary vehicles as roadside parking
                        gives one through lane, although its parking status is not completely established. |
                        roles: White continuous lines fit roadway edges; the right line's role is less certain
                        because vehicles obscure the roadside layout. | markings: No readable arrows, words,
                        symbols, waiting areas, or transverse control markings are visible in my lane. |
                        unseen: The right-side parking interpretation and total travel-lane count are
                        provisional; the distant lane end and obscured roadside features are not inferred. |
                        result: Consistent, with partial evidence for the right boundary role and lane count.
Step 5  Rule            left_boundary: The raised curb and landscaped edge are not a traversable lane
                        boundary, so my car must not leave the lane across this side.
Step 5  Rule            right_boundary: In China, a roadway edge line is not permission to use roadside space
                        as a travel lane; because the obscured layout does not conclusively distinguish
                        parking access from a solid lane separator, crossing permission is unresolved here.
Step 6  change_left     prohibited (correct): The raised curb and landscaped strip prohibit leaving the lane
                        to the left.
Step 6  change_right    not_determined (WRONG, label prohibited): Vehicles obscure the roadside layout,
                        leaving uncertain whether this is an accessible parking edge or a solid separator.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or lane-ending marking
                        restricts continuing straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the curb prohibits crossing left, uncertainty on the right remains
                        unresolved, and no unseen intersection markings are used to decide turning movements.
Advice                  Continue within the visible through lane, keeping clear of the rider and parked
                        vehicles; do not cross the left curb or treat the roadside space as another travel
                        lane. Check the right-side layout before entering it, and look for intersection
                        markings before choosing a turn.
Score                   lane True, boundaries {'left': True, 'right': None}, markings None (added None, missed
                        None), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1097, 16.25 s

mapdr__Non_MotorizedLane_06ac8e9ffc9f4a48b15e7266e9fbc065_1711669708398811000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese-
                        style signs, plates and road layout. My car is in the left of two visible same-
                        direction lanes on an urban road with a central fence; the road continues ahead, but
                        the next intersection is not clearly visible. (lanes 2, mine 1, full)
Step 2  Left            A metal central barrier forms the left boundary, with yellow paint visible along its
                        base, partly obscured by the barrier supports; opposing traffic is beyond it.
                        yellow solid, curb yes, center_line, evidence partial
Step 2  Right           A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction motor-vehicle lane, with no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego position 1 agree with a central barrier on
                        the left and a lane divider on the right. | roles: The yellow marking beside the
                        central barrier fits separation of opposing directions; the broken white right
                        boundary fits separation of same-direction lanes. | markings: No guidance markings are
                        visible on my lane surface; the overhead lane-direction sign is context, not an arrow
                        painted in my lane. | unseen: The central marking is partly obscured by barrier
                        supports, and distant pavement is obscured by vehicles; no distant arrows or
                        intersection markings are inferred. | result: consistent
Step 5  Rule            left_boundary: Under Chinese road rules, the central barrier must not be crossed, so
                        leaving my lane across its left boundary is prohibited.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes when
                        it is safe and without interfering with other traffic.
Step 6  change_left     prohibited (WRONG, label not_determined): The central barrier prohibits crossing the
                        left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent same-direction lane.
Step 6  go_straight     allowed (contested, correct): No visible pavement arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible pavement arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the boundaries govern only crossing their respective sides, and the
                        overhead sign has not been treated as a pavement marking.
Advice                  Continue in this lane or change right only after checking traffic; do not cross the
                        central barrier. Observe the posted 40 km/h limit and confirm lane directions as you
                        approach the junction, because the overhead diagram shows a lane arrangement not yet
                        fully visible on the pavement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 934, 14.29 s

mapdr__Non_MotorizedLane_0b32e42c00214d90b0c122dc79f9e3a6_1710461292870577000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the simplified
                        Chinese signs and road layout. My car is in the rightmost of two motor-vehicle lanes
                        on a divided urban road; a separate non-motorized lane is on the right, and the
                        distant intersection approach is partly obscured. (lanes 2, mine 2, full)
Step 2  Left            A white broken line, with several dashes and gaps visible, separates my lane from
                        another motor-vehicle lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from the paved non-motorized lane
                        carrying bicycles and scooters on the right; no curb lies along the near stretch of
                        this painted boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my lane being lane 2 of
                        two motor-vehicle lanes. | roles: The broken white line fits a same-direction lane
                        divider, and the solid white line fits the boundary with a non-motorized lane. |
                        markings: No readable guidance markings are visible within my lane; the arrows on the
                        distant sign are not pavement markings. | unseen: No pavement arrows or intersection-
                        end markings are inferred beneath the vehicles or beyond the readable stretch. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: The boundary to the designated non-motorized lane does not permit an
                        ordinary motor vehicle to move into that lane for normal travel.
Step 6  change_left     allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        lane change into the adjacent motor-vehicle lane.
Step 6  change_right    prohibited (correct): The right edge borders a designated non-motorized lane, which is
                        not available for ordinary motor-vehicle travel.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The distant lane-end pavement is obscured by vehicles and distance, so
                        any governing arrow cannot be determined.
Step 6  turn_right      not_determined: The distant lane-end pavement is obscured by vehicles and distance, so
                        any governing arrow cannot be determined.
Step 6  u_turn          not_determined: The distant lane-end pavement is obscured by vehicles and distance, so
                        any governing arrow or prohibition cannot be determined.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in the motor-vehicle lane, or change left across the broken line only when
                        safe; do not enter the non-motorized lane on the right. Check the lane arrows, signs
                        and signals nearer the intersection before choosing a turn, since the turning
                        permissions and stopping position are not readable here.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 870, 16.08 s

mapdr__Non_MotorizedLane_0f80edcf297c4187829dd012d9966e8e_1710038985287087000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        storefront lettering, road markings and traffic arrangement. My car is in the single
                        motor-vehicle lane in this direction on an urban two-way street; a separated non-
                        motorized strip is on the right, and no intersection or lane ending is clearly visible
                        ahead. (lanes 1, mine 1, full)
Step 2  Left            A single yellow broken line, with visible painted lengths and gaps, separates my lane
                        from the opposing side of the road; there is no curb along it.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           White broken paint marks the right side of my lane, and a low white physical separator
                        follows this boundary farther ahead, separating it from the non-motorized strip.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on the left and the boundary to the non-motorized
                        strip on the right agree with one motor-vehicle lane in my direction, indexed 1. |
                        roles: The broken yellow line fits an opposing-traffic separator; the white marking
                        and physical separator fit the edge of the motor-vehicle roadway. | markings: No
                        complete guidance arrow, word, symbol, transverse line or waiting area can be
                        identified in my lane. | unseen: A small white paint fragment immediately above the
                        hood is too cropped to classify; no arrow direction is inferred from it. The vehicle
                        ahead also conceals some pavement. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken yellow center line permits crossing for
                        overtaking or avoiding an obstruction when safe and without interfering with opposing
                        traffic.
Step 5  Rule            right_boundary: The physical separator must not be crossed, and the adjacent non-
                        motorized strip is not an ordinary motor-vehicle lane into which my car may change.
Step 6  change_left     allowed (WRONG, label prohibited): The broken yellow center line permits crossing when
                        safe, subject to yielding to opposing traffic.
Step 6  change_right    prohibited (WRONG, label not_determined): The physical separator blocks movement into
                        the non-motorized strip.
Step 6  go_straight     allowed (contested, correct): No identifiable lane-use marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No identifiable marking governs this action.
Step 6  turn_right      not_applicable: No identifiable marking governs this action.
Step 6  u_turn          not_applicable: No identifiable marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: permission to cross the broken center line is conditional on safety, the
                        right-side separator prohibits crossing, and no turn permission is inferred from
                        unreadable paint.
Advice                  Continue within the motor-vehicle lane and stay left of the right-side separator.
                        Cross the yellow broken center line only when safe and necessary; reassess turn
                        markings when the obscured pavement and next junction become visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6424, out 1138, 28.17 s

mapdr__Non_MotorizedLane_25dae80194fc4b428cb2579b95ed4292_1710299204968700000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be Guangzhou, China, with traffic keeping right; the Chinese road
                        names include Zhongshan 8th Road and Kangwang Road. My car is in the rightmost motor-
                        vehicle lane approaching an intersection, beside a separated bicycle lane; vehicles
                        obscure the full count of motor lanes to the left. (lanes None, mine None,
                        insufficient)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from a same-
                        direction lane occupied by a white sedan and a bus; there is no curb along this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Two parallel solid white lines separate my lane from the bicycle lane on the right,
                        with separator posts farther ahead; the sidewalk curb is beyond the bicycle lane.
                        white double_solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (partial): A small white arrow ahead appears to point right, but its head
                        and full shape are too distant to resolve confidently.
Step 4  Cross-check     position: The left lane line establishes another same-direction motor lane to my left,
                        while the right boundary adjoins the bicycle lane. The total number of motor lanes and
                        therefore my numerical lane index remain obscured. | roles: The broken white left
                        boundary fits a same-direction lane divider; the double solid white right boundary
                        fits separation from the bicycle lane. | markings: The distant apparent right-turn
                        arrow is compatible with the rightmost motor lane, but its complete set of heads
                        cannot be verified. | unseen: No additional arrow heads, stop line, crosswalk, or
                        waiting area can be identified confidently in my lane; the overhead sign is context,
                        not a substitute for reading pavement markings. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits changing into the
                        adjacent motor lane when safe.
Step 5  Rule            right_boundary: The solid separation from the non-motorized lane prohibits my ordinary
                        car from crossing into that lane here.
Step 5  Rule            arrow:right: A confirmed right-only lane arrow requires turning right, but this arrow
                        is not clear enough to establish whether it has additional heads.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  change_right    prohibited (correct): The solid white boundary separates my lane from the bicycle lane
                        and prohibits crossing here.
Step 6  go_straight     not_determined (contested, label allowed): The distant arrow's full set of heads is
                        unresolved, so straight-ahead permission cannot be established.
Step 6  turn_left       not_determined: The distant arrow cannot be read completely enough to determine the
                        permitted movements.
Step 6  turn_right      not_determined: The apparent right-pointing head is not sufficiently clear to confirm
                        the movement.
Step 6  u_turn          not_determined: The distant lane-use arrow is incompletely resolved, leaving its
                        movement restriction uncertain.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Do not cross into the bicycle lane; a left lane change is possible only after checking
                        traffic and cyclists. The overhead sign suggests this is the right-turn lane, so
                        confirm the pavement arrow as you approach and select the appropriate motor lane
                        before the intersection, obeying the signals.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1100, 14.58 s

mapdr__Non_MotorizedLane_286a400725cd4ba9aca2e6d5148f8851_1711588100576079000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese streetscape
                        and vehicles passing to the left of the yellow road marking. My car is in the single
                        visible lane of its direction on an urban two-way street; the road continues ahead,
                        but no intersection or lane end is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A faded yellow broken line, with several long dashes and intervening gaps visible,
                        borders my lane on the left; opposing traffic and a more distant white line lie beyond
                        it.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A raised curb borders my lane on the right beside a paved sidewalk and trees; no
                        painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on the left and curb on the right agree with my lane
                        being the only visible lane in this direction. | roles: The yellow broken line fits a
                        traversable center line separating opposing directions; the curb forms the right
                        roadway edge. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are visible in my lane. | unseen: No hidden markings have been inferred;
                        markings beyond the visible road stretch or behind the van cannot be assessed. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken yellow center line may be crossed temporarily for
                        overtaking or avoiding an obstruction when safe and without interfering with opposing
                        traffic.
Step 5  Rule            right_boundary: The raised curb is the roadway limit and must not be crossed to drive
                        onto the sidewalk.
Step 6  change_left     allowed (correct): The broken yellow center line permits temporary crossing when safe,
                        but the space beyond carries opposing traffic.
Step 6  change_right    prohibited (correct): The raised curb prohibits leaving the roadway onto the sidewalk.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action; permission to cross the center
                        line alone does not establish U-turn permission.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: crossing the broken center line is only conditionally permitted, the curb
                        prohibits moving right, and no unseen intersection movements have been inferred.
Advice                  Continue in your lane behind the van and keep clear of the right curb. The broken
                        yellow line permits temporary crossing only when safe; with opposing traffic visible,
                        do not treat the space to the left as another lane in your direction.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1004, 27.53 s

mapdr__Non_MotorizedLane_3fba9a5e18764a0f99610e0d2575b946_1710386997905413000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, inferred from the simplified Chinese storefront
                        text and road layout, with traffic keeping right. My car is in the middle of five
                        same-direction lanes on a divided urban road; the road continues ahead, but the next
                        intersection and lane-end markings are not clearly visible. (lanes 5, mine 3, full)
Step 2  Left            A single white broken line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Five lanes with my lane third from the left agrees with same-direction lane
                        lines on both sides and two lanes beyond each. | roles: Both white broken boundaries
                        fit ordinary same-direction lane dividers. | markings: No arrows, words, symbols,
                        waiting areas or transverse markings are discernible in my lane, so none conflicts
                        with the boundaries. | unseen: No distant intersection layout or hidden lane-use
                        marking has been inferred; the lane-end markings cannot be assessed. | result:
                        consistent
Step 5  Rule            left_boundary: In mainland China, a broken white same-direction lane divider permits
                        crossing to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In mainland China, a broken white same-direction lane divider permits
                        crossing to change lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or cross either broken divider only after checking
                        that the adjacent lane is clear. Turning-lane assignments and any stopping position
                        are not visible here; check the markings and controls as you approach the next
                        junction.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 885, 11.79 s

mapdr__Non_MotorizedLane_4ea09ef56d74498899ea4759eb326fd2_1711415187080137000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese signage and
                        traffic layout. My car is approaching a signalized urban intersection in a lane marked
                        for straight or right travel; vehicles obscure the full lane arrangement to the left.
                        (lanes None, mine None, insufficient)
Step 2  Left            A continuous solid white line separates my lane from an adjacent traffic lane on the
                        left; vehicles partly obscure its farther portion, and no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a roadside strip
                        beyond it and a yellow-painted raised sidewalk curb farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A white arrow has one head pointing straight and a second
                        head branching right.; line:stop_line (partial): A transverse white stop line is
                        visible ahead of the arrow, immediately before the pedestrian crossing; portions are
                        faint or obscured.; line:crosswalk (full): White zebra-crossing bars extend across my
                        lane beyond the stop line.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to the left, while
                        the right edge line places my lane beside the roadside strip; obscuration prevents a
                        reliable total count or numerical lane index. | roles: The solid white left line fits
                        an intersection-approach lane divider, and the solid white right line fits the
                        boundary to the roadside strip; the yellow curb is beyond that line, not my immediate
                        boundary. | markings: The straight-right arrow is consistent with this right-side
                        approach lane, and the stop line and crosswalk do not contradict it. | unseen: No
                        exact total lane count, roadside-strip designation, or hidden lane guidance is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes.
Step 5  Rule            right_boundary: A solid white roadway edge line must not normally be crossed to move
                        into the roadside strip.
Step 5  Rule            arrow:straight_right: The lane-use arrow permits straight and right movements, but not
                        left turns or U-turns.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the traffic
                        signal or traffic control; it does not itself require every vehicle to stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires attention and yielding to
                        pedestrians, without independently selecting a lane movement.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white lane divider prohibits
                        crossing into the lane on the left.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white edge line prohibits moving
                        into the roadside strip.
Step 6  go_straight     allowed (correct): The straight head of the lane-use arrow permits this movement.
Step 6  turn_left       prohibited (correct): The straight-right arrow does not permit a left turn.
Step 6  turn_right      allowed (correct): The right head of the lane-use arrow permits this movement.
Step 6  u_turn          prohibited (correct): The straight-right arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for straight travel or a right turn, and do not cross either solid
                        boundary. Obey the signals and traffic officer, stop before the stop line when
                        required, and yield to pedestrians and roadside two-wheelers.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1184, 23.57 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005238793896000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese supplementary
                        sign text and vehicles travelling to the right of the double centre lines. My car is
                        in the middle of three same-direction lanes on an urban road approaching an underpass;
                        no intersection or lane ending is visible. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside curb lies beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego lane index 2 agree with ordinary lane
                        lines and adjacent lanes on both sides. | roles: Both white broken boundaries fit
                        same-direction lane-divider roles. | markings: No arrows, words, symbols, transverse
                        lines or waiting areas are visible in my lane. | unseen: No markings are inferred
                        beneath vehicles or beyond the visible road under the bridge. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane divider permits a safe change
                        into the adjacent ordinary lane.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        change into the adjacent ordinary lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight, and no lane ending is visible.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane toward the underpass; either broken white boundary may be
                        crossed after checking mirrors, blind spots and available gaps. No visible marking
                        assigns turning movements, so reassess the lane guidance when an intersection comes
                        into view.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6424, out 843, 10.84 s

mapdr__Non_MotorizedLane_84ed44fcda554100a15272f3df855733_1711005241460616000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, with traffic keeping right, based on the road layout, vehicles
                        and infrastructure. My car is in the middle of three same-direction lanes on a divided
                        road approaching an underpass; no intersection or lane ending is visible. (lanes 3,
                        mine 2, full)
Step 2  Left            A white broken line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane on the right; the roadside curb is beyond that adjacent
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 2 agree with a lane line and an
                        adjacent same-direction lane on each side. | roles: Both white dashed boundaries fit
                        ordinary same-direction lane dividers. | markings: No guidance markings are visible
                        inside my lane; the diagonal channelizing area is outside it, beyond the left adjacent
                        lane. | unseen: No markings or intersection movements have been inferred beneath
                        vehicles or beyond the visible road. | result: consistent
Step 5  Rule            left_boundary: In the inferred Chinese setting, a white broken lane divider permits
                        crossing to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In the inferred Chinese setting, a white broken lane divider permits
                        crossing to change lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white dashed lane divider permits a safe change into the
                        adjacent ordinary lane.
Step 6  change_right    allowed (correct): The white dashed lane divider permits a safe change into the
                        adjacent ordinary lane.
Step 6  go_straight     allowed (contested, correct): No arrow or lane-ending marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane through the underpass; either dashed divider may be
                        crossed after checking traffic and signaling. No turn guidance or stopping point is
                        visible, so do not infer permission to turn from this image.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 766, 9.13 s

mapdr__Non_MotorizedLane_86e2ab7b4a8d4f78a3dce852ff9c1d82_1711149624116337000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, with traffic keeping right, based on Chinese signage, road
                        markings and the opposing traffic on the left. My car is in the rightmost of two same-
                        direction motor-vehicle lanes on an urban road continuing toward a distant junction.
                        (lanes 2, mine 2, full)
Step 2  Left            A white broken line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction motor-vehicle lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broad solid white line borders my lane on the right, with a narrow roadside strip
                        beyond it and a raised sidewalk farther right; the curb does not directly bound my
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two motor-vehicle lanes and ego position 2 agree with a same-direction lane
                        line on the left and a roadway edge line on the right. | roles: The broken white
                        divider fits a same-direction lane line, and the solid white outer boundary fits an
                        edge line rather than a center line. | markings: No readable arrow, word, symbol,
                        waiting area or transverse marking is visible in my lane. | unseen: No movement arrow
                        or stop line is inferred from the distant junction; its detailed markings are not
                        readable. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing into
                        the adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: A solid white roadway edge line generally prohibits crossing into the
                        roadside strip during ordinary driving.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits an ordinary move into the
                        roadside strip.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane, or change left across the broken divider only when safe; do
                        not cross the solid right edge line. Check the junction's signs, signals and any later
                        lane arrows before selecting a turning lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 822, 15.93 s

mapdr__Non_MotorizedLane_8ba12b7f9c1c4f799b997b7b201e70aa_1710718607114715000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, where traffic keeps right, inferred from the streetscape,
                        tactile sidewalk paving and vehicles, though the country is uncertain. My car follows
                        a van along a narrow, single-lane roadway between a planted divider and a sidewalk,
                        approaching an elevated structure; no intersection or lane end is visible. (lanes 1,
                        mine 1, full)
Step 2  Left            An unpainted raised curb borders a planted strip on the left, with a separate roadway
                        beyond; no painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           An unpainted raised curb borders the sidewalk beside a red wall on the right; no
                        painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane, indexed 1, agrees with physical roadway edges on both sides; the
                        roadway beyond the planted divider is separate. | roles: Both boundaries are unpainted
                        curb-defined roadway edges, not painted lane separators. | markings: No guidance
                        markings are visible on the exposed lane surface, so none conflict with the
                        boundaries. | unseen: The van obscures some pavement ahead, and the next intersection
                        is not visible; no hidden marking or intersection layout is inferred. | result:
                        consistent
Step 5  Rule            left_boundary: Under the inferred Chinese road rules, the raised curb and planted
                        divider are physical roadway limits and may not be crossed to leave this lane.
Step 5  Rule            right_boundary: Under the inferred Chinese road rules, the sidewalk curb is a physical
                        roadway limit and ordinary cars may not cross it to drive onto the sidewalk.
Step 6  change_left     prohibited (correct): The raised curb and planted divider prohibit leaving the roadway
                        to the left.
Step 6  change_right    prohibited (correct): The raised curb and sidewalk prohibit leaving the roadway to the
                        right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along this lane,
                        and no lane end is visible.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the curbs prohibit lateral departures but do not prohibit continuing along
                        the lane, and no unseen intersection movements are inferred.
Advice                  Continue within the curb-bounded lane and maintain clearance behind the van; do not
                        cross either curb. Reassess turning options when the road ahead and any intersection
                        markings become visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 803, 15.95 s

mapdr__Non_MotorizedLane_9b6b5daea5164914ae24a8bd5423bccb_1710730488312000000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the road
                        layout, Chinese-style blue signs and roadside infrastructure. My car is in the
                        rightmost lane approaching a large signal-controlled intersection; the full number of
                        same-direction lanes is not reliably visible at the left edge. (lanes None, mine None,
                        insufficient)
Step 2  Left            A continuous solid white line separates my lane from another same-direction lane on
                        the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A pale yellow continuous line runs beside a physical metal railing, with a separated
                        paved area beyond; glare reduces confidence in the paint colour.
                        yellow solid, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:right (full): A white bent arrow has a single head pointing right.;
                        line:stop_line (partial): A faint transverse white line appears across the lane
                        immediately before the pedestrian crossing.; line:crosswalk (full): Broad white
                        pedestrian-crossing stripes extend across the lane ahead.
Step 4  Cross-check     position: The right-side railing and edge line place my car in the rightmost lane; the
                        left lane line confirms another same-direction lane, but the leftmost extent cannot be
                        counted reliably. | roles: The solid white divider fits a same-direction lane line,
                        and the railing-side continuous marking fits a roadway edge. | markings: The right-
                        only arrow is consistent with this rightmost approach lane; the stop line and
                        crosswalk do not conflict with it. | unseen: The total lane count and numerical lane
                        index are left unknown; glare makes the right-edge paint and stop line partly
                        uncertain. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes on this approach.
Step 5  Rule            right_boundary: The physical roadside railing prevents leaving the lane across this
                        edge, regardless of uncertainty about the paint colour.
Step 5  Rule            arrow:right: The right-only lane-use arrow requires a right turn and excludes
                        straight, left-turn and U-turn movements from this lane.
Step 5  Rule            line:stop_line: The stop line indicates where to stop when required by the applicable
                        signal or traffic control; it does not itself require every vehicle to stop.
Step 5  Rule            line:crosswalk: The crossing requires attention and yielding to pedestrians as
                        applicable, without changing the lane's permitted turning direction.
Step 6  change_left     prohibited (correct): The solid white lane divider prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The physical railing blocks departure across the right edge.
Step 6  go_straight     prohibited (correct): The right-only arrow excludes straight travel.
Step 6  turn_left       prohibited (correct): The right-only arrow excludes a left turn.
Step 6  turn_right      allowed (correct): The right-only arrow permits a right turn.
Step 6  u_turn          prohibited (correct): The right-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for a right turn; do not cross the solid left divider or the
                        right-side railing. Check the applicable signal before proceeding, stop before the
                        crossing when required, and yield to pedestrians and other crossing traffic.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1159, 12.63 s

mapdr__SpeedLimitedLane_112ec2107aaf4bf196e351e045d452bb_1711167820291325000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the divided-
                        highway layout, median anti-glare panels and roadside infrastructure; the country
                        identification is tentative. My car is in the leftmost of three same-direction lanes
                        on a highway continuing straight beneath an overpass, with no visible intersection or
                        lane ending. (lanes 3, mine 1, full)
Step 2  Left            A single solid white line borders my lane on the left, with a narrow paved margin and
                        a metal median guardrail beyond it; opposing traffic is beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single broken white line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane on the right; there is no curb along this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego position 1 agree with a median-side edge
                        line on the left and a lane divider on the right. | roles: The solid white median-side
                        edge line and broken white same-direction lane divider fit their assigned roles. |
                        markings: No arrows, words, symbols or transverse markings are visible in my lane, so
                        none conflict with the boundaries. | unseen: No hidden guidance markings are assumed;
                        the country identification remains tentative. | result: consistent
Step 5  Rule            left_boundary: Under the inferred mainland Chinese rules, the solid roadway edge line
                        does not permit an ordinary lane change onto the median-side margin, and the guardrail
                        is a physical boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe.
Step 6  change_left     prohibited (WRONG, label allowed): The solid left edge line and median barrier
                        prohibit leaving the lane to the left.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and the lane
                        visibly continues.
Step 6  turn_left       not_applicable: No marking governs this action; no intersection is visible.
Step 6  turn_right      not_applicable: No marking governs this action; no intersection is visible.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight within this lane, or move right across the broken white divider
                        after checking traffic and blind spots. Do not cross the solid left edge toward the
                        median; no turn location or stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 892, 12.53 s

mapdr__SpeedLimitedLane_153c9b0831774a17b6d206ea65cb9b67_1710890517158418000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a divided expressway in China, with traffic keeping right, based on
                        the Chinese-style green signs and pavement speed markings. My car is in the rightmost
                        of four same-direction lanes, with the road continuing ahead and a hatched shoulder on
                        the right. (lanes 4, mine 4, full)
Step 2  Left            A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with diagonal shoulder hatching
                        and a guardrail farther beyond; the guardrail does not directly bound my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A large blue circular pavement marking contains the clearly
                        readable number 60.; text:speed_limit (partial): Farther ahead is a red-bordered
                        circular speed marking whose numeral is too small to read confidently.; text:other
                        (partial): Additional white pavement characters are visible farther ahead in my lane,
                        but their wording and shapes cannot be resolved reliably.
Step 4  Cross-check     position: Four lanes and position four agree with a same-direction lane line on the
                        left and a roadway edge on the right. | roles: The broken white left line fits a lane
                        divider, and the solid white right line fits the boundary to the hatched shoulder. |
                        markings: The speed markings do not conflict with the boundaries; no directional arrow
                        can be identified confidently in the distant markings. | unseen: The distant speed
                        numeral and white characters are not inferred, and the shoulder hatching is outside my
                        lane. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits changing into the
                        adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: The solid white expressway edge line prohibits an ordinary
                        discretionary crossing onto the shoulder.
Step 5  Rule            text:speed_limit: The blue circular 60 marking indicates a minimum speed of 60 km/h
                        under normal conditions, not a direction restriction.
Step 5  Rule            text:speed_limit: The red-bordered speed marking indicates a maximum speed, but its
                        unreadable numeral prevents identifying that limit.
Step 5  Rule            text:other: The unreadable pavement text cannot establish a specific instruction and
                        does not itself determine the seven movement actions.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white expressway edge line prohibits
                        moving onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No identifiable directional arrow restricts continuing
                        straight along this continuing lane.
Step 6  turn_left       not_applicable: No identifiable arrow or prohibited-turn marking governs this action.
Step 6  turn_right      not_applicable: No identifiable arrow or prohibited-turn marking governs this action.
Step 6  u_turn          not_applicable: No identifiable arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary rules govern only crossing their respective sides, speed markings
                        do not determine direction, and not_applicable turn results do not imply that
                        expressway turns are legally available.
Advice                  Continue in this lane or change left only after checking traffic; do not cross the
                        solid right edge onto the hatched shoulder. Observe the indicated 60 km/h minimum when
                        conditions permit, confirm the maximum-speed instruction ahead, and use a designated
                        exit for leaving the expressway.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['text:other'], missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1369, 18.5 s

mapdr__SpeedLimitedLane_159b10a3d6574fa4b3f3043e91435066_1709537194987486000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese bus
                        lettering and road layout. My car is in the middle of three same-direction lanes on a
                        divided urban arterial; the road continues ahead, with no clear intersection or lane
                        ending visible. (lanes 3, mine 2, full)
Step 2  Left            A faded, yellowish broken line with visible dashes and gaps separates my lane from a
                        lane carrying vehicles in the same direction; there is no curb at this boundary.
                        yellow dashed, curb no, lane_line, evidence partial
Step 2  Right           A white broken line, with visible dashes and gaps, separates my lane from the lane
                        occupied by the bus; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane on each side agrees with my lane being second of
                        three. | roles: The white broken right boundary fits a lane divider. The left boundary
                        appears yellowish, which is atypical for an ordinary same-direction divider in China;
                        fading and image colour make its paint colour uncertain, but vehicles beyond it
                        visibly travel in the same direction. | markings: No readable arrows, words, symbols,
                        waiting areas or transverse lines are visible in my lane. | unseen: The left paint
                        colour is uncertain, and distant markings cannot be resolved; no special-lane
                        designation or intersection movement restriction is inferred. | result: Consistent,
                        with reduced evidence for the left boundary because of its uncertain paint colour.
Step 5  Rule            left_boundary: A broken divider between same-direction lanes may be crossed to change
                        lanes when safe, provided no separate lane restriction applies.
Step 5  Rule            right_boundary: A white broken lane divider may be crossed to change lanes when safe;
                        the presence of a bus alone does not establish a reserved bus lane.
Step 6  change_left     allowed (correct): The visible broken divider permits crossing into the adjacent same-
                        direction lane when safe.
Step 6  change_right    allowed (correct): The white broken divider permits crossing, and no reserved-lane
                        marking is visible.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: broken boundaries govern lane changes only, and no intersection-turn
                        permission or reserved-lane status is inferred from the surrounding vehicles.
Advice                  Continue straight in your current lane; either broken divider permits a lane change
                        only after checking clearance, particularly beside the minibus and bus. Check upcoming
                        signs and clearer pavement markings before selecting a lane for a turn or entering any
                        restricted lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 999, 14.56 s

mapdr__SpeedLimitedLane_1ba4905f0cd94230a4e87293c44bfd49_1709693417745813000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the motorway layout, green
                        signs and median screening, although the country is not certain. My car is in the
                        middle of three lanes on a divided highway bending gently left; no intersection, ramp
                        or lane ending is visible. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane across
                        each boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No hidden markings or distant intersection layout have
                        been inferred; the country identification remains tentative. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        changing into the adjacent lane when safe and without obstructing traffic.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        changing into the adjacent lane when safe and without obstructing traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing into the adjacent
                        ordinary lane when safe.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing into the adjacent
                        ordinary lane when safe.
Step 6  go_straight     allowed (contested, correct): No arrow or other visible marking restricts continuing
                        along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane around the gentle left bend; no lane change or stop is
                        required by the visible markings. Either adjacent lane may be entered after signalling
                        and checking clearance, especially around the motorcycle to the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 808, 13.91 s

mapdr__SpeedLimitedLane_4c16c3f61cd5432abf11bab4d55f0507_1710821166609878000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the road
                        layout, vehicles and distant signage, although the country is not certain. My car is
                        in the middle of three lanes on a divided road continuing ahead; no intersection or
                        lane ending is visible. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with long dashes and clear gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and clear gaps, separates my lane from another
                        same-direction lane on the right; the solid road-edge line and guardrail lie beyond
                        that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane line on
                        each side. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No guidance markings are visible within my lane, and none
                        contradict the boundaries. | unseen: The road continues beyond the readable stretch;
                        no intersection markings or hidden lane-end features have been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: Under the inferred mainland Chinese rules, a white broken lane divider
                        permits crossing to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: Under the inferred mainland Chinese rules, a white broken lane divider
                        permits crossing to change lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a lane change when safe.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a lane change when
                        safe.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in the current lane; no lane change is required by the visible
                        markings. Either broken divider may be crossed when safe, but check mirrors and blind
                        spots carefully because vehicles are alongside on both sides.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 828, 15.48 s

mapdr__SpeedLimitedLane_5761b550887c494396dfbdfab57e3658_1709871635336045000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, although the country cannot be
                        confirmed from readable signs. My car is in the rightmost of three lanes on a divided,
                        barrier-lined elevated road curving gently right, with no visible intersection or lane
                        ending ahead. (lanes 3, mine 3, full)
Step 2  Left            A single white broken line, with several long dashes and intervening gaps visible,
                        separates my lane from another same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line follows the right-hand curve, with a narrow paved
                        shoulder and a raised concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 3 agree with a same-direction lane line on the
                        left and a roadway edge on the right. | roles: The broken white line fits a same-
                        direction lane divider; the continuous white line beside the shoulder fits a roadway
                        edge. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No hidden markings or intersection movements have been
                        inferred; the country identification remains tentative. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider may be
                        crossed to change lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, the solid white roadway edge must
                        not be crossed for an ordinary lane change or to drive along the shoulder.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white roadway edge prohibits an ordinary
                        move onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No lane-use arrow restricts continuing along this lane,
                        which does not visibly end.
Step 6  turn_left       not_applicable: No marking governs this action, and no intersection is visible.
Step 6  turn_right      not_applicable: No marking governs this action, and no intersection is visible.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within your lane around the right-hand curve; a left lane change is permitted
                        only after checking traffic. Do not cross the solid right edge onto the shoulder; no
                        stopping point or turn facility is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 883, 11.69 s

mapdr__SpeedLimitedLane_5a47c462b2144775a6e68fd921b4bb1e_1709957383712615000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, inferred from the road layout,
                        vehicle plates and interchange infrastructure, though the country is not certain. My
                        car is in the leftmost of three lanes on a divided roadway continuing beneath an
                        interchange; no intersection or lane ending is visible ahead. (lanes 3, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane, with a narrow paved margin
                        and metal median guardrail beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        lane traveling in the same direction; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and two lanes to the right agree with my lane being
                        lane 1 of 3. | roles: The solid yellow median-side edge line and broken white same-
                        direction lane divider fit their assigned roles. | markings: No arrows, words, symbols
                        or transverse markings are visible in my lane. | unseen: No unseen lane-end markings
                        are inferred; the roadway continues beyond the visible stretch. The left physical
                        boundary is a guardrail, not a raised curb. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, the solid yellow roadway edge must
                        not be crossed for an ordinary maneuver, and the median guardrail is not traversable.
Step 5  Rule            right_boundary: The broken white lane divider permits changing to the adjacent same-
                        direction lane when safe.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid yellow edge line and median
                        guardrail prohibit leaving the lane to the left.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        rightward lane change.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change right across the broken white line when safe; do not
                        cross the left yellow edge line. No turn guidance or stopping point is visible, so
                        follow later lane guidance for your intended exit.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 865, 10.07 s

mapdr__SpeedLimitedLane_5b6e1c0c6a2f485f96aa3989e0fc550a_1710979257785896000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be a divided expressway in China, with traffic keeping right; the road
                        layout, median screening and roadside equipment support that inference, but do not
                        establish the country conclusively. My car is in the leftmost of apparently four same-
                        direction lanes, with the expressway continuing ahead and no intersection or lane
                        ending visible. (lanes 4, mine 1, partial)
Step 2  Left            A single continuous pale white line runs along the left of my lane, with a narrow
                        paved shoulder and a metal median guardrail beyond; sunlight gives the paint a yellow-
                        green cast.
                        white solid, curb no, edge_line, evidence partial
Step 2  Right           A single broken white line, with visible long dashes and intervening gaps, separates
                        my lane from another same-direction lane; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my lane being the
                        leftmost lane; the farther-right lanes appear to bring the total to four, although
                        glare reduces confidence in that count. | roles: The continuous white left marking
                        fits a roadway edge, and the broken white right marking fits a same-direction lane
                        divider. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: The country is inferred rather than confirmed, and glare
                        limits the left paint colour and distant lane count; no intersection markings or
                        hidden lane ending have been assumed. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese marking rules, the solid roadway edge does
                        not permit an ordinary manoeuvre across it onto the median shoulder.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing right when
                        it is safe.
Step 6  change_left     prohibited (correct): The visible solid left roadway edge prohibits an ordinary
                        crossing onto the shoulder.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible arrow or lane ending restricts continuing
                        along my lane.
Step 6  turn_left       not_applicable: No marking governs this action; no junction is visible.
Step 6  turn_right      not_applicable: No marking governs this action; no junction is visible.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within your lane, or change right across the broken line after checking
                        traffic; do not cross the left solid edge onto the median shoulder. Reduce speed as
                        necessary for the strong glare, and follow upcoming signs for exits.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 993, 21.94 s

mapdr__SpeedLimitedLane_5fd2028ab8f941b7957e541cb1eefcfc_1710919631201752000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese roadside
                        signs and road layout. My car is in the third of four lanes on a divided expressway
                        continuing straight ahead; no intersection or lane ending is visible. (lanes 4, mine
                        3, full)
Step 2  Left            A single white broken line, with clearly visible long dashes and gaps, separates my
                        lane from another same-direction lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with clearly visible long dashes and gaps, separates my
                        lane from the rightmost traffic lane; the shoulder and concrete barrier are farther
                        right, not at my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes and an ego position of third from the left agree with two lanes
                        to my left and one to my right, with lane-line boundaries on both sides. | roles: Both
                        white broken boundaries fit same-direction lane separators. | markings: No arrows,
                        words, symbols, transverse lines or marked waiting areas are visible in my lane. |
                        unseen: No unseen markings or intersection layout have been inferred; distant sign
                        text is not treated as a lane marking. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing into the
                        adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing into the
                        adjacent same-direction lane when safe.
Step 6  change_left     allowed (correct): The white broken left lane separator permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane separator permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No arrow or other lane marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action, and no intersection is visible.
Step 6  turn_right      not_applicable: No marking governs this action, and no intersection is visible.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent lane may be entered across the broken
                        white separator after checking traffic and signalling. For a different route, follow
                        the upcoming destination signs and use a designated exit rather than attempting a
                        direct turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 846, 16.35 s

mapdr__SpeedLimitedLane_6417acfdac2148e6a13a5c5416c67f88_1711089077689520000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           Likely mainland China, with traffic keeping right, inferred from the divided
                        expressway layout and median anti-glare panels, though the country is not certain. My
                        car is in the left lane of a two-lane carriageway continuing ahead, with no visible
                        intersection or lane ending. (lanes 2, mine 1, full)
Step 2  Left            A continuous white solid line borders the lane on the left, with a narrow paved margin
                        and a raised median guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white broken line, with long dashes and clear gaps, separates my lane from the
                        adjacent same-direction lane on the right; there is no physical barrier at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and position 1 agree with a median-side edge on the
                        left and a lane divider on the right. | roles: The solid white roadway edge and broken
                        white same-direction lane divider fit their assigned roles. | markings: No arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane. | unseen: No
                        unseen intersection markings or distant lane arrangements have been inferred; the
                        country identification remains tentative. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese expressway rules, the solid roadway edge and
                        median barrier prohibit leaving the lane to the left.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent
                        ordinary lane when safe.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid left roadway edge and median
                        barrier prohibit crossing to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight along this
                        continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight within the lane, or move right across the broken divider after
                        checking traffic and clearance from the truck. Do not cross the left edge toward the
                        median; no turn facility or stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 809, 9.99 s

mapdr__SpeedLimitedLane_694b51c337864180b0af1b273beb1d3d_1709771819737819000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is most likely China, with traffic keeping right, inferred from the
                        Chinese/English motorway signs and the median on the left. My car is in the leftmost
                        of two through lanes on a divided motorway continuing straight, with an emergency
                        shoulder on the right and no intersection or lane ending visible. (lanes 2, mine 1,
                        full)
Step 2  Left            A continuous solid white line borders a narrow median-side strip, with a raised
                        concrete edge and metal median barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        the other through lane; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): Part of a large white Chinese pavement inscription is visible
                        immediately ahead of the hood, resembling the character 小; the rest is obscured and
                        cannot be read completely.
Step 4  Cross-check     position: Two through lanes and ego lane index 1 agree with a median-side edge on the
                        left and a same-direction lane divider on the right. | roles: The solid white median-
                        side edge and broken white lane divider fit their assigned roles. | markings: The
                        partially visible pavement text provides no readable directional instruction and does
                        not contradict the boundaries. | unseen: The obscured remainder of the pavement
                        inscription is not inferred; no directional arrow or waiting area is identified. |
                        result: consistent
Step 5  Rule            left_boundary: On a Chinese motorway, the solid median-side edge line must not be
                        crossed for an ordinary lane change or to enter the median-side strip.
Step 5  Rule            right_boundary: A broken white same-direction lane divider may be crossed to change
                        lanes when safe.
Step 5  Rule            text:other: The incomplete pavement inscription does not establish a readable movement
                        instruction and does not itself authorize or prohibit any of the seven actions.
Step 6  change_left     prohibited (correct): The solid median-side edge line prohibits crossing to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change into the
                        adjacent through lane.
Step 6  go_straight     allowed (contested, correct): No visible directional arrow restricts continuing
                        straight along this continuing lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in your lane or move right across the broken line only after checking
                        traffic; do not cross the solid left edge. Observe the overhead lane-specific speed
                        and vehicle-use signs, and keep out of the emergency shoulder.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1008, 13.85 s

mapdr__SpeedLimitedLane_74ce826f2e9441c593a69281963aa557_1711085029860869000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the
                        simplified-Chinese expressway signs and roadway layout. My car is in the rightmost of
                        three through lanes on a divided expressway continuing ahead, with an emergency
                        shoulder on the right and no visible intersection or lane ending. (lanes 3, mine 3,
                        full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane occupied by a white van; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from the paved emergency shoulder,
                        with a guardrail beyond the shoulder rather than directly at the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider and right roadway edge agree with my lane being the
                        third and rightmost through lane; the shoulder is not counted as a traffic lane. |
                        roles: The broken white separator fits a same-direction lane line, and the solid white
                        line beside the shoulder fits a roadway edge line. | markings: No guidance markings
                        are visible on the pavement within my lane; the overhead arrows are signs, not
                        pavement markings. | unseen: No hidden pavement arrows or downstream junction features
                        have been inferred. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white same-direction lane divider permits
                        crossing to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The expressway edge bounds an emergency shoulder, which an ordinary
                        car must not enter for routine driving or overtaking.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (WRONG, label allowed): The right edge bounds an emergency shoulder, which
                        is not available for an ordinary lane change.
Step 6  go_straight     allowed (contested, correct): No pavement marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the current through lane and keep the emergency shoulder clear. A left
                        lane change is permitted by the markings, but check the van and other adjacent traffic
                        first; follow the posted lane-specific speed signs.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 829, 11.49 s

mapdr__SpeedLimitedLane_9bcaa7405b7943e89db2eb67d3163825_1709782706558838000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, inferred from the blue license
                        plates, Chinese vehicle badging and road environment. My car is in the middle of three
                        lanes on a divided urban road continuing straight; no intersection or lane ending is
                        visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line separates my lane from the lane occupied by the silver car on the
                        left; portions are obscured by the black Toyota, and there is no curb along this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps ahead, separates my lane from the
                        lane occupied by the black Volkswagen on the right; there is no curb along this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): Large white painted characters are visible in my lane around and
                        beyond the black Toyota, but the vehicle obscures enough of them that the wording
                        cannot be read reliably.
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane line
                        on each side. | roles: Both boundaries have white dashes and gaps consistent with
                        same-direction lane dividers. | markings: The partly obscured painted characters do
                        not establish a directional restriction or contradict the lane boundaries. | unseen:
                        The obscured wording is not reconstructed, and no arrow, intersection stop line or
                        waiting area is identified. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when it is safe and does not interfere with other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when it is safe and does not interfere with other traffic.
Step 5  Rule            text:other: The partly hidden wording cannot establish a specific instruction and does
                        not independently authorize or prohibit any of the seven assessed actions.
Step 6  change_left     allowed (correct): The broken white left lane divider permits crossing when safe.
Step 6  change_right    allowed (correct): The broken white right lane divider permits crossing when safe.
Step 6  go_straight     allowed (contested, correct): No visible directional marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-turn marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-turn marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-turn marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: lane changes follow the broken boundaries, continuing straight is
                        unrestricted by the observed markings, and no intersection-turn permission is
                        inferred.
Advice                  Continue in the middle lane and maintain a safe following distance behind the Toyota.
                        Either broken divider may be crossed only after checking for a safe gap; cars are
                        close on both sides, and the photo does not establish lanes for turning.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1263, 21.68 s

mapdr__SpeedLimitedLane_9c677d0c0c0942cda69ffa5059152fd8_1710895405943707000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese-style
                        roadside signs and pavement speed markings. The car is in the rightmost of two lanes
                        on a divided highway continuing straight, with a truck in the lane to the left and no
                        visible intersection or lane ending. (lanes 2, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates this lane from the
                        lane occupied by the truck; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders the lane on the right, with a striped paved shoulder
                        and a guardrail farther beyond it; the guardrail does not directly bound the travel
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:speed_limit (full): A large white numeral 60 is painted in this lane immediately
                        ahead of the car.; text:speed_limit (full): A yellow numeral 100 is painted farther
                        ahead in this lane.
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 2 agree with a lane separator on
                        the left and a roadway edge on the right. | roles: The white broken separator fits a
                        same-direction lane line; the continuous white line beside the shoulder fits an edge
                        line. | markings: The white 60 and yellow 100 are compatible minimum- and maximum-
                        speed pavement markings in China; neither specifies a turning movement. | unseen: No
                        arrows, stop markings, waiting areas or intersection controls are identifiable in this
                        lane; more distant pavement details are too small to interpret reliably. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane separator permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge does not permit ordinary driving onto the
                        highway shoulder, which is reserved for exceptional or emergency use.
Step 5  Rule            text:speed_limit: The white 60 indicates a minimum speed of 60 km/h under normal
                        conditions, without authorizing unsafe speed in adverse conditions.
Step 5  Rule            text:speed_limit: The yellow 100 indicates a maximum speed of 100 km/h and does not
                        prescribe a turning movement.
Step 6  change_left     allowed (correct): The broken white lane separator permits changing left when safe.
Step 6  change_right    prohibited (WRONG, label allowed): The solid roadway edge borders a shoulder, which is
                        not available for an ordinary lane change.
Step 6  go_straight     allowed (contested, correct): No directional arrow restricts continuing straight, and
                        the lane visibly continues.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, observing the indicated 60–100 km/h range when
                        conditions permit and checking roadside speed signs. A left lane change is permitted
                        only after checking clearance around the truck; do not use the right shoulder for
                        ordinary travel.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1438, 36.16 s

mapdr__TidalFlowLane_164dc888bc3b4955a6ca27293a2d514e_1709885288453032000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese signs,
                        plates and opposing traffic positions. My car is in the leftmost of three apparent
                        forward lanes on a broad urban road approaching a bridge; paired yellow markings and
                        overhead lane-control signals suggest that my lane is reversible. (lanes 3, mine 1,
                        partial)
Step 2  Left            Two parallel yellow lines run along the left, apparently in broken sections, with
                        opposing vehicles beyond them and no curb.
                        yellow double_dashed, curb no, special_lane_line, evidence partial
Step 2  Right           Two parallel yellow lines appear in separated sections on the right, with a pale white
                        line alongside their outer edge, forward-moving traffic beyond and no curb.
                        yellow double_dashed, curb no, special_lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The apparent leftmost forward position agrees with opposing traffic beyond
                        the left boundary and two forward lanes to the right, but the reversible lane's
                        current allocation is uncertain. | roles: Paired broken yellow boundaries fit a
                        Chinese reversible lane; distance, worn paint and shadows make their exact pattern
                        less certain. | markings: No readable arrow, word, symbol or transverse marking is
                        visible within my lane. | unseen: The current reversible-lane allocation and distant
                        pavement details cannot be established; no unseen lane-use arrow or stop line is
                        assumed. | result: consistent
Step 5  Rule            left_boundary: In China, paired broken yellow reversible-lane boundaries must be used
                        according to lane controls, and they do not authorize moving into visibly opposing
                        traffic.
Step 5  Rule            right_boundary: A broken reversible-lane boundary permits leaving for an ordinary
                        same-direction lane when lane controls permit and it is safe, but the uncertain
                        pattern and current control prevent confirming permission here.
Step 6  change_left     prohibited (WRONG, label not_determined): The left boundary separates my lane from
                        visibly opposing traffic; crossing into that traffic is prohibited.
Step 6  change_right    not_determined (correct): The apparent broken reversible-lane boundary could permit
                        leaving, but its pattern and applicable lane control are not sufficiently clear.
Step 6  go_straight     allowed (contested, correct): No visible pavement arrow restricts continuing straight;
                        lane-control signals must be checked separately.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: straight-ahead permission describes the pavement markings only, not
                        authorization to use a potentially closed reversible lane.
Advice                  Check the overhead control for this apparent reversible lane before proceeding;
                        pavement markings alone do not establish that it is open. Do not move left into
                        opposing traffic, and verify the right boundary and lane controls before moving into
                        an ordinary forward lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1185, 20.89 s

mapdr__TidalFlowLane_1dae4caa72a34e5cbf2ebe696b6e3de0_1709952541106346000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on Chinese
                        roadside writing, blue license plates and opposing traffic on the left. My car is in
                        the middle of three same-direction lanes on a broad urban road; the distant junction
                        or lane end is not clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from the
                        same-direction lane containing the small silver van on the right; the roadside barrier
                        lies beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego lane index 2 agree with ordinary lane
                        lines on both sides. | roles: Both white broken boundaries fit same-direction lane-
                        divider roles. | markings: No guidance markings are visible within my lane, so none
                        contradict the boundaries. | unseen: The vehicles and distance obscure the farther
                        lane surface and next junction; no arrows, stop lines or waiting areas are inferred
                        there. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white ordinary lane divider permits
                        crossing to change lanes when safe and without obstructing traffic.
Step 5  Rule            right_boundary: In mainland China, a broken white ordinary lane divider permits
                        crossing to change lanes when safe and without obstructing traffic.
Step 6  change_left     allowed (contested, correct): The broken white lane divider permits a safe lane change
                        to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The next junction and any lane-use markings governing a left turn are
                        not clearly visible.
Step 6  turn_right      not_determined: The next junction and any lane-use markings governing a right turn are
                        not clearly visible.
Step 6  u_turn          not_determined: The next junction and any markings governing a U-turn are not clearly
                        visible.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or cross either broken divider only after checking surrounding
                        traffic and blind spots. Do not assume this lane permits a turn at the next junction;
                        check the approaching arrows, signs and signals before selecting a turn lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 886, 15.99 s

mapdr__TidalFlowLane_265c2ea27db0409b840de267e9cd64af_1711000444306818000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the blue plates,
                        streetscape and traffic arrangement. My car is in the left of two apparent same-
                        direction lanes on an urban road, with an opposing or reversible lane immediately to
                        the left and a trolleybus alongside on the right; the distant junction is indistinct.
                        (lanes 2, mine 1, partial)
Step 2  Left            Two parallel yellow broken lines, with repeated aligned dashes and gaps, run along the
                        left side; an oncoming car is beyond them, and there is no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A faint white broken line separates my lane from the trolleybus lane on the right; the
                        bus hides much of its length, and no curb separates the two lanes.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: My lane appears leftmost among the current same-direction lanes: the double
                        yellow broken boundary separates it from a lane carrying opposing traffic, while the
                        white boundary separates it from the same-direction trolleybus. | roles: Double yellow
                        broken lines are consistent with a Chinese reversible-lane boundary; the white broken
                        line is consistent with an ordinary same-direction lane divider. | markings: No
                        readable arrow, word, symbol or transverse marking is visible in my lane. | unseen:
                        The bus obscures much of the right boundary and the far-right roadway, so the lane
                        count remains tentative; no bus-only designation or distant lane-use arrow is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: In China, double yellow broken lines identify a reversible-lane
                        boundary, and an ordinary car must not enter that lane without its applicable
                        directional authorization.
Step 5  Rule            right_boundary: A white broken lane divider permits a lane change when safe, yielding
                        to traffic already in the adjacent lane.
Step 6  change_left     prohibited (correct): The double yellow broken boundary adjoins a reversible lane,
                        treated as reserved, with opposing traffic visible.
Step 6  change_right    allowed (contested, label prohibited): The visible white broken lane divider permits
                        crossing when safe; the trolleybus currently occupies the adjacent lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the current lane and do not enter the reversible lane to the left.
                        Although the right divider permits changing lanes, remain clear of the trolleybus and
                        check for a safe gap; reassess turn markings and signals as the junction becomes
                        visible.
Score                   lane False, boundaries {'left': False, 'right': None}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1063, 18.03 s

mapdr__TidalFlowLane_2c85182201fd4f8faefc551f0cfe0bfa_1709687101136571000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the simplified
                        Chinese signs, vehicle plates and opposing traffic to the left of the double yellow
                        lines. My car is in the leftmost of three apparent same-direction lanes on a broad
                        urban road; the distant junction and lane ends are not clearly visible. (lanes 3, mine
                        1, partial)
Step 2  Left            Two parallel solid yellow lines separate my lane from oncoming traffic on the left;
                        neither line has a visible gap, and there is no curb along this boundary.
                        yellow double_solid, curb no, center_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and intervening gaps, separates my lane
                        from the same-direction lane containing the van; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left places my lane leftmost, while the white lane
                        line confirms another same-direction lane to the right; the outermost lane count is
                        less certain. | roles: The double solid yellow center line and broken white same-
                        direction lane divider fit their observed roles. | markings: No guidance arrow, word,
                        symbol, waiting area or transverse line is readable in the visible portion of my lane.
                        | unseen: The distant lane end is obscured by traffic and perspective; no markings
                        there are inferred, and the outer lane count remains tentative. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a double solid yellow center line prohibits crossing
                        into the opposing side.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent
                        ordinary same-direction lane when safe.
Step 6  change_left     prohibited (correct): The double solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    allowed (correct): The broken white divider permits crossing into the adjacent same-
                        direction lane when safe.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The lane-end guidance is too distant and obscured to determine the
                        permitted intersection movement.
Step 6  turn_right      not_determined: The lane-end guidance is too distant and obscured to determine the
                        permitted intersection movement.
Step 6  u_turn          not_determined: The lane-end guidance is too distant and obscured to determine whether
                        a U-turn is permitted.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: boundary-crossing decisions follow the visible lines, continuing straight
                        is unrestricted by visible markings, and intersection turns remain undecided because
                        the lane end is not visible.
Advice                  Continue in this lane or change right across the broken white line only when safe; do
                        not cross the double yellow center line. The roadside sign directs left-turning
                        vehicles toward the auxiliary road on the right, so follow the signed route and
                        confirm junction markings before turning.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1153, 28.09 s

mapdr__TidalFlowLane_4842d1c117a44b17872fc225243a1b71_1711000625776249000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese signs
                        and road layout. My car is in the left of two forward lanes, apparently a direction-
                        controlled tidal lane, with an oncoming lane to the left and a bus lane beside the
                        platform to the right. (lanes 2, mine 1, full)
Step 2  Left            Two parallel yellow broken lines, with visible gaps between their paired segments,
                        separate my lane from the lane carrying oncoming vehicles; there is no curb.
                        yellow double_dashed, curb no, center_line, evidence full
Step 2  Right           A yellow broken line separates my lane from the lane with yellow bus-related road
                        lettering beside the raised platform; the platform curb is beyond that adjacent lane.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow directly ahead has one head pointing straight
                        forward.
Step 4  Cross-check     position: The center-line boundary on the left makes my lane the leftmost forward
                        lane; the reserved lane on the right accounts for the second forward lane. | roles:
                        The paired broken yellow center markings fit the visibly signed tidal-lane
                        arrangement, and the yellow broken right boundary separates the adjacent bus lane. |
                        markings: The straight arrow agrees with the forward alignment of my lane; the yellow
                        bus lettering is outside my lane and does not describe my lane. | unseen: No
                        intersection stop line or waiting area is visible, and none is inferred; distant road
                        details are not readable. | result: consistent
Step 5  Rule            left_boundary: The broken yellow tidal-lane boundary is not itself a no-crossing line,
                        but crossing is permitted only when the direction controls and opposing traffic allow
                        a lawful, safe maneuver.
Step 5  Rule            right_boundary: Although its boundary is broken, the adjacent bus lane is treated as
                        reserved, so an ordinary car must not change into it.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits continuing straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 6  change_left     allowed (WRONG, label prohibited): The broken yellow boundary permits crossing in
                        principle, subject to tidal-lane direction controls and a safe gap in opposing
                        traffic.
Step 6  change_right    prohibited (contested, correct): The adjacent lane is reserved for buses, so its
                        broken boundary does not authorize entry by this car.
Step 6  go_straight     allowed (correct): The white straight arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent; permission to cross the broken left boundary is not permission to enter
                        opposing traffic unsafely or disregard tidal-lane controls.
Advice                  Continue straight in this lane only while its direction-control signal permits; the
                        overhead forward indication is visible. Stay out of the bus lane and do not move left
                        into the visible oncoming traffic.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6424, out 1354, 19.47 s

mapdr__TidalFlowLane_7b2732cd56c1441ba9f22e7dee246990_1710041475468370000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, suggested by the Chinese
                        shop signs, blue vehicle plates and road layout. My car is in an apparent reversible
                        lane between paired yellow broken boundaries on an urban transit corridor; no
                        intersection or lane end is clearly visible ahead. (lanes None, mine None,
                        insufficient)
Step 2  Left            Two parallel yellow broken lines, with repeated dashes and gaps, separate my lane from
                        another paved lane on the left; a raised platform lies farther left, not at my lane
                        boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel yellow broken lines, with repeated dashes and gaps, separate my lane from
                        a paved lane bearing large yellow writing; the roadside curb is beyond that lane.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is between two marked lanes, but their permitted directions cannot
                        be established, so neither the same-direction lane count nor my index is assigned. |
                        roles: Paired yellow broken boundaries on both sides fit a reversible-lane arrangement
                        rather than ordinary same-direction lane dividers. | markings: No readable arrow, word
                        or transverse marking is visible inside my lane; the large yellow writing is beyond
                        its right boundary. | unseen: The reversible-lane operating directions, adjacent-lane
                        restrictions and the eventual intersection markings are not readable or visible. |
                        result: consistent
Step 5  Rule            left_boundary: In China, paired yellow broken lines identify a reversible-lane
                        boundary whose use depends on the indicated operating direction; the paint alone does
                        not establish that my car may enter the lane beyond it.
Step 5  Rule            right_boundary: In China, paired yellow broken lines identify a reversible-lane
                        boundary whose use depends on the indicated operating direction; crossing also
                        requires establishing that the adjacent lane is available to my car.
Step 6  change_left     not_determined (contested, label allowed): The reversible-lane boundary is visible,
                        but the permitted direction and availability of the lane beyond it cannot be
                        established.
Step 6  change_right    not_determined (contested, label prohibited): The reversible-lane boundary is visible,
                        but the adjacent lane's direction and restrictions cannot be established.
Step 6  go_straight     allowed (contested, correct): No visible arrow or lane-ending marking restricts
                        continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: straight travel is unrestricted by the visible pavement markings, while
                        lane changes remain undecided because the reversible-lane allocation is not
                        established.
Advice                  Check the reversible-lane signals and signs before proceeding or crossing either
                        yellow boundary; the broken lines alone do not confirm an available adjacent lane. No
                        visible marking establishes a turning lane or stopping point.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['change_left
                        not_determined with full evidence', 'change_right not_determined with full evidence']
Tokens                  in 6424, out 1240, 32.65 s

mapdr__TidalFlowLane_85010d619c45485e9ac6d170a345154a_1710976194093153000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be an urban arterial in China, with traffic keeping right; the bus,
                        road furniture and paired broken white markings support that inference, though the
                        country is not certain. My car is in a through lane amid queued traffic; the far-left
                        roadway edge and the next junction are not clearly visible. (lanes None, mine None,
                        insufficient)
Step 2  Left            Two parallel broken lines, apparently white under the warm sunlight, run along the
                        left of my lane, with aligned dashes and gaps; vehicles traveling in the same
                        direction are beyond them, and there is no curb.
                        white double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A single broken white line separates my lane from another lane carrying vehicles in
                        the same direction; a long dash and a gap are visible, with no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: There are lanes on both sides of my lane, but the full same-direction lane
                        count and therefore my numerical position cannot be established confidently. | roles:
                        The paired broken white boundary is consistent with a Chinese reversible-lane
                        boundary; the single broken white right boundary is consistent with an ordinary lane
                        divider. | markings: No guidance arrow, word, symbol, transverse line or waiting area
                        is readable in the visible portion of my lane. | unseen: The lane beyond the queue and
                        its junction markings are obscured; no arrows or stop lines are inferred there. The
                        reversible lane's operating direction and hours cannot be read. | result: consistent
Step 5  Rule            left_boundary: In China, paired broken white lines identify a reversible-lane
                        boundary; because its operating controls are not established, the special lane beyond
                        is treated as reserved and my car must not enter it.
Step 5  Rule            right_boundary: An ordinary broken white lane divider permits crossing into the
                        adjacent lane when safe.
Step 6  change_left     prohibited (WRONG, label allowed): The paired broken white boundary borders a
                        reversible lane whose availability is unknown, so entry is treated as prohibited.
Step 6  change_right    allowed (correct): The broken white ordinary lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The queue hides the lane-end markings that could determine whether
                        this lane permits a left turn.
Step 6  turn_right      not_determined: The queue hides the lane-end markings that could determine whether
                        this lane permits a right turn.
Step 6  u_turn          not_determined: The lane-end markings are obscured, so any U-turn guidance cannot be
                        established.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue cautiously with the queue, or change right only after checking traffic; do
                        not enter the reversible lane on the left without confirmed operating controls.
                        Reassess the lane arrows, signals and stopping position when the traffic ahead reveals
                        them.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1171, 22.01 s

mapdr__TidalFlowLane_8f5b7fa125df46d58641796df45384cb_1710048090674402000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        lettering, vehicle plates and road layout. My car is in the middle of three same-
                        direction lanes on an urban road approaching a signalized intersection, behind a
                        coach. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with a visible long dash and gap, separates my lane from the lane
                        occupied by the gray SUV; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broad broken white line, with visible painted segments and gaps, separates my lane
                        from a reddish-surfaced lane occupied by cars; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow immediately behind the coach has a single head
                        pointing straight ahead.
Step 4  Cross-check     position: Two lane-line boundaries agree with my position in lane 2 of 3, with another
                        same-direction lane on each side. | roles: The white broken boundaries fit same-
                        direction lane dividers; the reddish surface on the right does not by itself establish
                        a reserved lane. | markings: The straight-ahead arrow agrees with a continuing through
                        lane; no conflicting marking is visible in my lane. | unseen: The coach obscures the
                        farther portion of my lane and its intersection-end markings. No hidden stop line,
                        additional arrow, or reserved-lane designation has been assumed. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing into the
                        adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: A broken white lane divider permits crossing when safe, but the
                        reddish pavement alone does not establish whether an additional lane-use restriction
                        applies.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight from this
                        lane and excludes left turns, right turns and U-turns from it.
Step 6  change_left     allowed (correct): The broken white left lane divider permits crossing when safe.
Step 6  change_right    allowed (correct): The broken white right lane divider permits crossing; no reserved-
                        lane designation is visible.
Step 6  go_straight     allowed (correct): The single straight-ahead arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary decisions follow the visible broken lines, movement decisions
                        follow the straight-only arrow, and no permission is inferred from hidden markings.
Advice                  Use this lane to proceed straight; for a turn, move safely into an appropriately
                        marked lane before the intersection, checking any restrictions on the reddish right
                        lane. Signals ahead appear red: stop at the applicable stop line, whose position is
                        obscured by traffic.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1039, 20.62 s

mapdr__TidalFlowLane_a6c934f5c4ab4fc2ad1970be0259d642_1711410698324105000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        writing and road-control signs. My car is on an urban multilane road beside a yellow-
                        marked reversible-lane area; traffic obscures the distant approach, and the reversible
                        lanes make the total same-direction lane count uncertain. (lanes None, mine None,
                        insufficient)
Step 2  Left            Two parallel yellow broken lines run along the left of my lane, with repeated painted
                        sections and gaps; a white SUV occupies the lane beyond, and there is no curb at this
                        boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and clear gaps, separates my lane from another
                        motor-traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: There is another ordinary traffic lane on the right and a reversible-lane
                        area on the left; its current directional allocation cannot be established confidently
                        enough to give a total lane count or index. | roles: The paired broken yellow markings
                        and overhead lane controls support a reversible-lane boundary on the left; the broken
                        white line fits an ordinary lane divider on the right. | markings: No guidance marking
                        is readable on the exposed pavement within my lane; markings in other lanes have not
                        been assigned to mine. | unseen: Vehicles conceal pavement ahead, including any lane-
                        use arrow or transverse marking near the eventual intersection. | result: consistent
Step 5  Rule            left_boundary: The paired broken yellow lines identify a reversible-lane boundary; an
                        ordinary car must not enter that special lane without confirmed authorization from its
                        lane controls.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjoining
                        ordinary lane when safe.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary borders a reversible special
                        lane, which must be treated as reserved without confirmed authorization.
Step 6  change_right    allowed (correct): The broken white divider permits a safe change into the ordinary
                        lane on the right.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        the present lane.
Step 6  turn_left       not_determined: Traffic hides the downstream pavement where a lane-use arrow could
                        determine this movement.
Step 6  turn_right      not_determined: Traffic hides the downstream pavement where a lane-use arrow could
                        determine this movement.
Step 6  u_turn          not_determined: Traffic hides the downstream pavement where a movement arrow or
                        prohibition could determine this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane or change right only when safe; do not cross left into the
                        reversible-lane area without confirmed lane-control authorization. Follow the overhead
                        controls and check the pavement markings revealed ahead before selecting a turning
                        lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1335, 37.53 s

mapdr__TidalFlowLane_dce62010e5e946f789dfd62b34bfb201_1711068060437800000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        signage and traffic arrangement. My car is approaching or crossing a broad signal-
                        controlled intersection toward a zebra crossing; glare and indistinct foreground
                        markings prevent a reliable count of the approach lanes or identification of my lane's
                        index. (lanes None, mine None, insufficient)
Step 2  Left            No continuous, reliably identifiable boundary can be traced immediately left of my car
                        through the sun glare; vehicles are visible farther left, but neither paint colour nor
                        line pattern can be established.
                        none none, curb no, unknown, evidence insufficient
Step 2  Right           Faint pale patches appear on the pavement to the right, but they do not establish a
                        definite boundary or a dash-and-gap pattern; no curb immediately bounding my lane is
                        discernible.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        line:crosswalk (partial): A white zebra crossing extends across the roadway ahead,
                        including the path straight ahead of my car; some stripes are obscured by vehicles.
Step 4  Cross-check     position: Neither boundary role nor the lane count is established, so a numerical lane
                        position cannot be checked. | roles: No centre-line, lane-line or edge-line role is
                        assigned without identifiable paint. | markings: The visible crossing does not
                        establish lane direction; no readable lane-use arrow, word or waiting area is visible
                        in my path. | unseen: No boundary pattern or lane-use arrow has been inferred from
                        vehicle positions; 'none' records no identifiable paint, not proof that paint is
                        absent. | result: consistent
Step 5  Rule            left_boundary: Because the left boundary cannot be identified, its crossing permission
                        under Chinese road-marking rules cannot be established.
Step 5  Rule            right_boundary: Because the right boundary cannot be identified, its crossing
                        permission under Chinese road-marking rules cannot be established.
Step 5  Rule            line:crosswalk: The zebra crossing requires attention to pedestrians and yielding as
                        required, but does not itself prescribe a lane movement or require an unconditional
                        full stop.
Step 6  change_left     not_determined (correct): The left boundary is obscured and cannot establish whether
                        crossing it is permitted.
Step 6  change_right    not_determined (correct): The right boundary is indistinct and cannot establish
                        whether crossing it is permitted.
Step 6  go_straight     allowed (contested, label not_determined): No visible lane-use marking restricts
                        continuing straight; the crosswalk does not prohibit this movement.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable.
Step 7  Reflect         Consistent: lane changes remain undecided because the boundaries are unreadable, and
                        the crossing is not treated as a directional restriction or an unconditional stop
                        requirement.
Advice                  Keep a predictable course rather than changing lanes across unreadable boundaries;
                        this image does not identify a suitable turning lane. Follow the applicable signals
                        and yield to pedestrians and cyclists at the crossing, stopping if required.
Score                   lane None, boundaries {'left': None, 'right': None}, markings None (added None, missed
                        None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1098, 22.69 s

mapdr__TidalFlowLane_ef4e7607ebb748b391255f4275607ea7_1709628255495496000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, likely Beijing, with traffic keeping right, based on the
                        taxis, road layout and overhead lane-control displays. My car is on a broad urban road
                        approaching distant signals, in the left ordinary through lane, with a reversible lane
                        immediately to the left and another ordinary lane to the right. (lanes 3, mine 2,
                        partial)
Step 2  Left            Two parallel broken yellow lines, with visible gaps between paired segments, separate
                        my lane from a lane occupied by a taxi; overhead lane-control displays indicate a
                        reversible-lane arrangement.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A single broken white line, with long dashes and clear gaps, separates my lane from
                        another traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane has an ordinary lane to its right and a reversible lane to its left,
                        agreeing with position 2 of three lanes when the reversible lane is included; its
                        currently authorized direction is uncertain. | roles: Paired broken yellow lines fit a
                        reversible-lane boundary, while the broken white line fits a same-direction lane
                        divider. | markings: No arrows, words, symbols or transverse markings are readable in
                        my lane; none contradict the boundary interpretation. | unseen: The distant end of the
                        lane is obscured by traffic and distance, and the reversible lane's current
                        authorization cannot be confidently established. | result: consistent
Step 5  Rule            left_boundary: The paired broken yellow lines delineate a reversible lane; under the
                        reserved-special-lane convention, my ordinary car must not change into it.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent
                        ordinary lane when safe.
Step 6  change_left     prohibited (WRONG, label allowed): The left boundary leads into a reversible special
                        lane, which is treated as reserved.
Step 6  change_right    allowed (correct): The broken white divider permits a safe lane change to the ordinary
                        lane on the right.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_determined: The lane-end guidance is too distant and obscured to establish whether
                        a left turn is permitted.
Step 6  turn_right      not_determined: The lane-end guidance is too distant and obscured to establish whether
                        a right turn is permitted.
Step 6  u_turn          not_determined: The lane-end guidance is too distant and obscured to establish whether
                        a U-turn is permitted.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in your ordinary lane, or change right across the broken white line only when
                        safe; do not enter the reversible lane on the left. Check the overhead controls and
                        upcoming lane arrows before choosing a turning lane, and obey the signals ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1065, 17.67 s

mapdr__TidalFlowLane_fcf0b941d7a04592b2be351c3de0618b_1711596818438262000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        lettering and road environment. My car is in the middle of three visible lane
                        corridors on an urban road, apparently in a reversible lane approaching a distant
                        junction; the directional allocation of all three corridors cannot be confirmed.
                        (lanes None, mine None, insufficient)
Step 2  Left            Two parallel yellow broken lines, with repeated dashes and gaps, separate my lane from
                        another paved lane beside the platform on the left; there is no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel yellow broken lines, with repeated dashes and gaps, separate my lane from
                        a paved lane containing large yellow Chinese lettering on the right; there is no curb
                        at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: My lane is between two visible lane corridors, but the double broken yellow
                        boundaries indicate reversible operation, so three visible corridors cannot
                        confidently be counted as three lanes of my direction. | roles: Paired broken yellow
                        lines on both sides fit the Chinese marking for a reversible lane rather than ordinary
                        same-direction lane dividers. | markings: No readable arrow, word, symbol, transverse
                        line or waiting area is visible inside my lane; the large yellow lettering is beyond
                        its right boundary. | unseen: The neighboring lane lettering and distant junction
                        details are not sufficiently readable to establish additional restrictions or
                        directional lane allocation. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a double broken yellow reversible-lane boundary
                        permits crossing when the adjoining lane is operating in the same direction and the
                        maneuver is otherwise lawful and safe.
Step 5  Rule            right_boundary: In mainland China, a double broken yellow reversible-lane boundary
                        permits crossing when the adjoining lane is operating in the same direction and is not
                        reserved for another vehicle class.
Step 6  change_left     not_determined (WRONG, label allowed): The broken reversible-lane boundary is
                        crossable, but the adjoining lane's current direction and reservation status cannot be
                        established.
Step 6  change_right    not_determined (contested, label prohibited): The broken reversible-lane boundary is
                        crossable, but the adjacent lane's yellow lettering is not sufficiently readable to
                        determine whether ordinary cars may enter.
Step 6  go_straight     allowed (contested, correct): No visible arrow or other in-lane marking restricts
                        continuing straight along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the broken boundaries do not themselves prohibit crossing, but unresolved
                        adjacent-lane operation prevents an unconditional lane-change permission; no turn
                        permission is inferred from the boundaries.
Advice                  Confirm that this reversible lane is open in your direction using its operating
                        signals or signs, and verify adjacent-lane direction and reservation rules before
                        changing lanes. Continue within your lane only when authorized, and check the distant
                        junction controls before proceeding.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions ['change_left
                        not_determined with full evidence', 'change_right not_determined with full evidence']
Tokens                  in 6424, out 1309, 23.1 s

mapdr__VariableDirectionLane_44993ba8e34c47b4856cd979c5dc2c08_1710301217970650000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese building
                        signs and the opposing traffic on the left. The car is in the middle, apparently
                        reversible lane of a three-lane urban road; two lanes currently appear to carry
                        traffic in our direction, with no intersection or lane end visible. (lanes 2, mine 1,
                        partial)
Step 2  Left            Two parallel yellow broken lines, with clear gaps between paired dashes, separate my
                        lane from the lane containing approaching vehicles; there is no curb at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           Two parallel yellow broken lines, with clear gaps between paired dashes, separate my
                        lane from the right-hand lane carrying traffic away from the camera; there is no curb
                        at this boundary.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The car occupies the middle of three physical lanes, apparently the leftmost
                        of two currently forward-moving lanes; the reversible lane's actual directional
                        assignment is not confirmed. | roles: Paired broken yellow boundaries on both sides
                        fit a Chinese reversible-lane arrangement rather than ordinary same-direction lane
                        dividers. | markings: No visible arrow, word, symbol or transverse marking contradicts
                        the boundary observations. | unseen: No lane-control indication confirming the
                        reversible lane's current assignment is readable; the lane count in our direction
                        remains provisional. | result: consistent
Step 5  Rule            left_boundary: Chinese paired broken yellow lines delineate a reversible lane; leaving
                        it across the broken boundary is permitted by the marking, but does not authorize
                        driving against opposing traffic.
Step 5  Rule            right_boundary: The broken reversible-lane boundary permits leaving this lane to the
                        right when the adjacent lane is available and the maneuver is safe.
Step 6  change_left     allowed (WRONG, label prohibited): The broken reversible-lane boundary permits
                        crossing out of this lane, although approaching traffic makes the adjacent lane
                        unsuitable for ordinary forward travel.
Step 6  change_right    allowed (WRONG, label not_determined): The broken reversible-lane boundary permits
                        leaving for the adjacent right-hand lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary permissions describe crossing the markings only, not permission
                        to enter opposing traffic or disregard reversible-lane controls.
Advice                  Confirm that lane-control signals authorize your direction before continuing in this
                        reversible lane; the vehicle ahead alone does not establish permission. Do not move
                        left into approaching traffic; if necessary and safe, leave across the broken right
                        boundary for the regular forward lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6424, out 1088, 20.26 s

mapdr__VariableDirectionLane_5b6edf5a25944e3484c3ecefb077d38c_1711441031907099000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese signs
                        and road-marking style. My car is in the left of two ordinary lanes approaching a
                        signalized intersection; a yellow-bordered reversible lane appears to lie immediately
                        to the left. (lanes 2, mine 1, partial)
Step 2  Left            Two parallel yellow broken lines, with repeated paired dashes and gaps, separate my
                        lane from an apparent reversible lane on the left; there is no curb.
                        yellow double_dashed, curb no, special_lane_line, evidence full
Step 2  Right           A white broken line with visible long dashes and gaps separates my lane from the lane
                        occupied by the bus; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow directly ahead has a single straight-ahead
                        head.
Step 4  Cross-check     position: The white lane divider confirms another ordinary lane on the right. The
                        yellow double-broken boundary places a reversible lane, rather than another confirmed
                        ordinary lane of my direction, on the left; the count excludes that direction-
                        dependent lane. | roles: Yellow double-broken lines fit a reversible-lane boundary in
                        China, while the white broken line fits an ordinary same-direction lane divider. |
                        markings: The straight-ahead arrow is consistent with the ordinary through lane
                        between these boundaries. | unseen: The reversible lane's current operating direction
                        is not established. Vehicles obscure the distant end of my lane, so no stop line or
                        crosswalk across my lane is confidently identified. | result: consistent
Step 5  Rule            left_boundary: The double-broken yellow boundary identifies a reversible lane, which
                        is treated as reserved here, so my ordinary car must not cross into it without
                        established authorization.
Step 5  Rule            right_boundary: A broken white ordinary lane divider permits a lane change when safe
                        and without interfering with other traffic.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight at the
                        intersection and prohibits turning left, turning right, or making a U-turn from this
                        lane.
Step 6  change_left     prohibited (correct): The left boundary borders a reversible lane treated as reserved,
                        so entering it is prohibited.
Step 6  change_right    allowed (correct): The broken white ordinary lane divider permits crossing when safe.
Step 6  go_straight     allowed (correct): The arrow explicitly permits straight-ahead travel.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identified.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane, obeying the intersection signals and stopping at the
                        stop line if required once it becomes visible. Do not enter the reversible lane on the
                        left; a rightward lane change is permitted only when clear of the bus and other
                        traffic.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1112, 24.26 s

mapdr__VariableDirectionLane_694d73de4c424c7b9931647af982de41_1711426714893192000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be Shanghai, China, with traffic keeping right, based on the Chinese
                        road signs naming Longyang Road and Gaoke Road West. My car is in a straight-ahead
                        lane on a broad divided urban road approaching an elevated crossing; the far-right
                        roadway layout and the distant intersection are partly obscured. (lanes None, mine 3,
                        partial)
Step 2  Left            A white broken line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the right; the roadside curb is beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has one head pointing straight
                        ahead.
Step 4  Cross-check     position: Two lanes appear to lie to my left, consistent with my lane being third from
                        the left; another lane lies to my right. The complete lane count is uncertain because
                        the far-right layout is unclear. | roles: White broken boundaries fit separators
                        between lanes traveling in the same direction. | markings: The straight-only arrow
                        agrees with a through lane bounded by ordinary lane separators; the arrow visible to
                        the right belongs to the neighboring lane. | unseen: No distant stop line, waiting
                        area, or obscured pavement marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, an ordinary broken white lane separator permits crossing to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: An ordinary broken white lane separator permits a safe lane change
                        into the adjacent unrestricted lane.
Step 5  Rule            arrow:straight: The straight-ahead lane-use arrow permits proceeding straight and
                        prohibits turning left, turning right, or making a U-turn from this lane.
Step 6  change_left     allowed (correct): The broken white left lane separator permits a safe lane change.
Step 6  change_right    allowed (correct): The broken white right lane separator permits a safe lane change.
Step 6  go_straight     allowed (correct): The straight-ahead arrow explicitly permits this movement.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn from this
                        lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn from this
                        lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight, obeying the signals and traffic ahead. For a
                        turn, move safely across a broken separator into a lane whose markings permit that
                        turn before reaching the intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1288, 18.11 s

mapdr__VariableDirectionLane_6fa7c4b986204f518c266a6727fea22b_1712030568103240000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely mainland China, inferred from the simplified Chinese signs and road
                        markings, with traffic keeping right. My car is approaching a signal-controlled
                        intersection in a straight-ahead lane, with queued lanes to the left and a right-turn
                        lane to the right. (lanes 4, mine 3, partial)
Step 2  Left            A solid white line with repeated short perpendicular white teeth separates my lane
                        from the queued variable-direction lane on the left; there is no curb.
                        white solid, curb no, special_lane_line, evidence full
Step 2  Right           A solid white line separates my lane from another traffic lane on the right, with no
                        curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow ahead in my lane has one head pointing straight
                        forward.; line:stop_line (partial): A transverse white stop line is visible ahead of
                        my lane immediately before the pedestrian crossing, although its detail is small at
                        this distance.; line:crosswalk (full): White pedestrian-crossing stripes extend across
                        my lane at the intersection.
Step 4  Cross-check     position: The apparent four-lane arrangement places my lane third from the left, with
                        two queued lanes to the left and one lane to the right; vehicles partially obscure the
                        far-left layout. | roles: The toothed solid white boundary fits the adjacent variable
                        lane, and the plain solid white boundary separates my lane from the right-hand lane. |
                        markings: The straight-only arrow agrees with the lane continuing toward the
                        intersection; the right-turn arrow belongs to the neighboring lane, not mine. |
                        unseen: The far-left roadway is partly obscured, so the lane count and lane index are
                        tentative; distant stop-line detail is also limited. | result: consistent
Step 5  Rule            left_boundary: In China, the solid white variable-lane boundary must not be crossed
                        here, so my car cannot change left.
Step 5  Rule            right_boundary: A solid white lane-separation line prohibits changing lanes across it.
Step 5  Rule            arrow:straight: The straight-ahead lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the traffic
                        signal, rather than independently requiring every vehicle to stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing must be kept clear and pedestrians must be
                        given the required priority.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white variable-lane boundary
                        prohibits crossing to the left.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white lane boundary prohibits
                        crossing to the right.
Step 6  go_straight     allowed (contested, correct): The straight-ahead arrow permits this movement.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, subject to the applicable signal, and stop
                        before the stop line when required. Do not cross either solid boundary here; a turn
                        requires selecting an appropriate lane before the solid-line approach.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:crosswalk', 'line:stop_line'], missed []), actions False,
                        unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1513, 19.79 s

mapdr__VariableDirectionLane_81e98f3adc2e4013ad438f51e47f80ca_1709698755700928000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese writing,
                        vehicle plates and road layout. My car is in the second of four same-direction lanes
                        on a divided urban road continuing ahead; the next intersection and lane end are not
                        clearly visible. (lanes 4, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        traffic lane on the right; the yellow broken line beside the bus is farther right and
                        is not my boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my position in lane 2 of 4; one lane is
                        to my left and two are to my right. | roles: Both white broken boundaries fit
                        separation of same-direction lanes. | markings: No guidance arrows, words, symbols or
                        transverse markings are visible in my lane; there is no conflict with the boundaries.
                        | unseen: No markings are inferred beneath vehicles or in the distant, obscured lane
                        end; the outermost lane's reservation status is not assigned to my adjacent lane. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe without interfering with other traffic.
Step 6  change_left     allowed (WRONG, label prohibited): The white broken left lane divider permits a safe
                        lane change.
Step 6  change_right    allowed (WRONG, label not_determined): The white broken right lane divider permits a
                        safe lane change into the immediately adjacent lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The lane end is distant and obscured, so any movement-defining marking
                        there cannot be checked.
Step 6  turn_right      not_determined: The lane end is distant and obscured, so any movement-defining marking
                        there cannot be checked.
Step 6  u_turn          not_determined: The lane end is distant and obscured, so any movement-defining marking
                        there cannot be checked.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight or change into either immediately adjacent lane only when safe,
                        checking especially for traffic near the bus on the right. Confirm intersection arrows
                        and signs farther ahead before choosing a turning lane; the yellow-marked outer lane
                        is not the lane immediately beside you.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_left'], citation None, contradictions []
Tokens                  in 6424, out 887, 16.86 s

mapdr__VariableDirectionLane_852b46659aec46258cf6752a3e40cbe4_1711608460555996000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely China, with traffic keeping right, based on the Chinese writing,
                        vehicle plates and intersection layout. My car is at a broad signal-controlled urban
                        intersection with a zebra crossing immediately ahead; vehicles and the foreground
                        obscure the approach-lane layout. (lanes None, mine None, insufficient)
Step 2  Left            A short curved sequence of white broken markings is visible ahead to the left of the
                        white car, but its connection to my lane is obscured; a raised island lies farther
                        left beyond another vehicle.
                        white dashed, curb no, unknown, evidence partial
Step 2  Right           The vehicles on the right and the foreground obscure my lane's right boundary; no
                        paint pattern or physical edge can be established.
                        none none, curb no, unknown, evidence insufficient
Step 3  Markings        line:crosswalk (partial): Broad parallel white zebra-crossing stripes extend across
                        the path directly ahead, with parts hidden by vehicles.
Step 4  Cross-check     position: The visible vehicles suggest multiple parallel traffic streams, but the
                        nearest lane boundaries cannot be traced well enough to establish a lane count or my
                        lane index. | roles: The white broken markings could provide lane guidance, but their
                        relationship to my lane is uncertain; neither boundary is assigned a definite role. |
                        markings: The visible crosswalk does not establish any permitted turning direction and
                        does not contradict the uncertain boundaries. | unseen: No lane-use arrow, stop word,
                        stop line or waiting area can be positively identified; the obscured boundary
                        attributes are not evidence that those features are absent. | result: consistent
Step 5  Rule            left_boundary: In China an ordinary broken white lane divider generally permits
                        crossing when safe, but the visible broken markings cannot confidently be identified
                        as my lane's boundary.
Step 5  Rule            right_boundary: Because the right boundary is obscured, its applicable crossing
                        restriction cannot be established.
Step 5  Rule            line:crosswalk: A zebra crossing requires attention and yielding to pedestrians, but
                        does not itself authorize or prohibit any of the seven lane movements.
Step 6  change_left     not_determined (correct): The visible broken markings cannot be confidently connected
                        to my lane's left boundary.
Step 6  change_right    not_determined (correct): The right boundary and any crossing restriction are
                        obscured.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight; the
                        crosswalk does not govern this movement permission.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-turn marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable.
Step 7  Reflect         Consistent: lateral crossing permissions remain undecided, and the crosswalk is not
                        used to infer turning permissions or a mandatory full stop.
Advice                  Maintain your established traffic stream and avoid lateral movement until the lane
                        boundaries are clear; turning-lane assignments cannot be established from this image.
                        Obey the signal controlling your movement and yield to pedestrians at the zebra
                        crossing without blocking it.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1148, 28.86 s

mapdr__VariableDirectionLane_dc7e02beddc6497eab4aeefd0ddb8fb9_1709695347140121000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be an urban road in China, with traffic keeping right, inferred from
                        the Chinese writing and vehicle arrangement. My car is behind the red taxi; traffic
                        obscures the road ahead, and the status of the separated strip on the right makes the
                        same-direction lane count uncertain. (lanes None, mine None, insufficient)
Step 2  Left            A white broken line, with a long dash and intervening gap visible beside the taxi,
                        separates my lane from the lane containing the silver car; there is no curb.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line borders a narrow strip of white diagonal hatching on the right,
                        with another white line and the concrete mixer beyond it; there is no curb at this
                        boundary.
                        white solid, curb no, other, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to the left; the
                        function of the separated roadway on the right and additional markings farther left
                        prevent a reliable total count. | roles: The broken white line fits a same-direction
                        lane divider; the solid white border and diagonal hatching fit a separating
                        channelized strip. | markings: No readable arrow, word, or transverse marking is
                        visible inside my lane; the diagonal hatching lies beyond its right boundary. |
                        unseen: No lane-use arrow or intersection stop line is inferred beneath the vehicles;
                        the lane count and the function of the roadway beyond the right-hand strip remain
                        unresolved. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: The solid border of the channelized separating strip must not be
                        crossed to move into the roadway on its far side.
Step 6  change_left     allowed (correct): The visible broken white lane divider permits a lane change when
                        safe.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white boundary of the channelized strip
                        prohibits crossing to the right.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing along my lane.
Step 6  turn_left       not_determined: The lane's distant end is obscured by traffic, so any governing arrow
                        cannot be checked.
Step 6  turn_right      not_determined: The lane's distant end is obscured by traffic, so any governing arrow
                        cannot be checked.
Step 6  u_turn          not_determined: The lane's distant end is obscured by traffic, so any governing
                        movement marking cannot be checked.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the lane and do not cross the hatched separator on the right; change
                        left only after checking for a safe gap. Wait until the obscured lane markings and
                        intersection controls become visible before selecting a turning movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1339, 26.55 s

mapdr__VariableDirectionLane_dca4739c4a80441ab59dfcd945fe9ab2_1712125867456978000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese road
                        lettering, blue plates and road layout. My car is in the rightmost of four same-
                        direction lanes on a divided urban road, approaching an overhead lane-control
                        installation; the lane is marked as a variable-direction lane. (lanes 4, mine 4, full)
Step 2  Left            A solid white longitudinal line with repeated short diagonal teeth separates my lane
                        from another same-direction lane on the left; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line with repeated short diagonal teeth runs beside a raised roadside
                        curb, with planting and a sidewalk beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        text:other (full): Large white Chinese characters read 可变车道, meaning variable lane; no
                        complete lane-use arrow or transverse stopping line can be resolved farther ahead.
Step 4  Cross-check     position: The lane line on the left and roadside edge on the right agree with my car
                        occupying lane 4 of 4. | roles: The white left boundary separates same-direction
                        lanes, while the white right boundary follows the roadside curb; their toothed
                        treatment is consistent with the variable-lane lettering. | markings: The variable-
                        lane text and toothed boundaries agree; the text does not itself specify a permitted
                        intersection movement. | unseen: No pavement arrow, current variable-lane direction,
                        or distant stop line has been inferred from unreadable details. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking conventions, the solid white variable-
                        lane boundary must not be crossed to change lanes.
Step 5  Rule            right_boundary: The roadside edge and raised curb do not permit leaving the traffic
                        lane to the right.
Step 5  Rule            text:other: The variable-lane lettering identifies a lane whose current movement must
                        be checked against its lane-control indications, but the lettering alone authorizes no
                        particular turn.
Step 6  change_left     prohibited (contested, label allowed): The solid white left boundary prohibits
                        crossing into the adjacent lane.
Step 6  change_right    prohibited (correct): The right boundary follows a raised curb and does not permit
                        driving out to the right.
Step 6  go_straight     allowed (contested, correct): No readable pavement arrow restricts continuing straight
                        along the lane; the variable-lane control must still be checked.
Step 6  turn_left       not_applicable: No readable lane-use arrow or prohibited-turn pavement marking governs
                        this action.
Step 6  turn_right      not_applicable: No readable lane-use arrow or prohibited-turn pavement marking governs
                        this action.
Step 6  u_turn          not_applicable: No readable lane-use arrow or prohibited-turn pavement marking governs
                        this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary restrictions apply only to leaving the lane, and the marking-only
                        straight-ahead allowance does not establish permission under the variable-lane
                        control.
Advice                  Stay within the solid boundaries and verify the current overhead variable-lane
                        direction before proceeding. The pavement text alone does not establish which turns
                        this lane currently serves, and no stopping position is clearly visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1351, 35.79 s

mapdr__VariableDirectionLane_df2cf4e1441940b080bbfce49fca8a15_1709882701082446000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely China, inferred from the Chinese writing on the coach and the road
                        layout; traffic keeps right. My car is approaching a signalized urban intersection in
                        a through lane, with vehicles obscuring the full lane count and its exact position
                        from the left. (lanes None, mine None, insufficient)
Step 2  Left            A continuous white line with repeated short, angled white teeth alongside it separates
                        my lane from same-direction traffic on the left; no curb is visible.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from the lane occupied by the coach on the
                        right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has a single head pointing
                        straight ahead.; line:stop_line (partial): A transverse white stop line is visible on
                        either side of the vehicle ahead, which hides its central portion across my lane.;
                        line:crosswalk (partial): White zebra-crossing stripes extend across the approach
                        beyond the stop line; the vehicle ahead hides part of the crossing in my lane.
Step 4  Cross-check     position: Both boundaries separate same-direction lanes, so my lane is an interior
                        lane; the obscured outer lanes prevent a reliable total count or index. | roles: The
                        white solid boundaries fit same-direction lane separators on a Chinese intersection
                        approach; the teeth on the left are supplementary markings, not gaps in the line. |
                        markings: The straight-only arrow agrees with an intersection through lane bounded by
                        solid approach lines; the stop line and crosswalk do not contradict it. | unseen: No
                        outer lane count, hidden arrow, reserved-lane designation, or waiting area has been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes; the supplementary teeth encourage reduced speed.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            arrow:straight: The straight-only lane arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when stopping is required by
                        the signal or traffic control, but does not itself require every vehicle to stop.
Step 5  Rule            line:crosswalk: The crosswalk requires attention to and yielding for pedestrians and
                        must not be blocked.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The single straight-ahead arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight and do not cross either solid boundary;
                        turning requires selecting an appropriate lane before the solid-line approach. Follow
                        the signals, stop before the stop line when required, and keep the pedestrian crossing
                        clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1243, 26.17 s

mapdr__VehicleLane_019e550228d74df1b84f85116d54d61e_1711416452149561000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        road signs and road layout. My car is in the single motor-vehicle lane of a separated
                        side carriageway approaching traffic lights, with a planted divider on the left and a
                        bicycle lane on the right; the parallel main carriageway is separate. (lanes 1, mine
                        1, full)
Step 2  Left            A continuous white line follows a raised curb beside a planted divider, with a
                        separate motor carriageway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from the strip used by cyclists on the
                        right; the sidewalk curb lies beyond that strip.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow directly ahead has one head pointing straight
                        forward; the vehicle transporter obscures the lane surface farther ahead.
Step 4  Cross-check     position: There is one motor-vehicle lane on this separated carriageway, consistent
                        with roadway edges on both sides; the bicycle strip is not another motor-vehicle lane.
                        | roles: The continuous white markings fit roadway edges, with a physical divider on
                        the left and a bicycle lane on the right. | markings: The straight-only arrow is
                        consistent with continuing along the separated motor lane. | unseen: No markings
                        beneath or beyond the transporter are inferred, and no stop line or waiting area can
                        be identified. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised divider prohibit leaving this lane
                        across its left boundary.
Step 5  Rule            right_boundary: The solid boundary to the non-motorized lane prohibits an ordinary car
                        from crossing into that lane here.
Step 5  Rule            arrow:straight: Under Chinese lane-direction marking rules, the straight-only arrow
                        permits proceeding straight and prohibits left turns, right turns and U-turns from
                        this lane.
Step 6  change_left     prohibited (correct): The solid edge and raised divider prohibit crossing the left
                        boundary.
Step 6  change_right    prohibited (correct): The solid edge separates a bicycle lane that an ordinary car may
                        not enter here.
Step 6  go_straight     allowed (correct): The visible straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain between the white boundaries and use this lane for straight travel, keeping
                        clear of cyclists on the right. Obey the traffic signals and maintain enough distance
                        behind the transporter to see any stop line or crossing it currently hides.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 988, 20.9 s

mapdr__VehicleLane_03d33a54b23744cc8cfc1faa1c730f57_1711513674435018000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the simplified Chinese roadside notice and
                        streetscape; traffic keeps right. My car is in the single motor-vehicle lane in this
                        direction on a narrow two-way urban street, with a junction or signal farther ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A single continuous yellow line separates my lane from approaching scooters and
                        opposing traffic on the left.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A white broken line, with a visible dash and gap, separates my lane from a narrow
                        roadside strip used by scooters; the sidewalk curb is beyond that strip.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line places my lane leftmost in this direction, and the
                        right edge line bounds the single motor-vehicle lane. | roles: The solid yellow center
                        line and broken white roadside edge line fit their observed roles. | markings: No
                        readable guidance marking in my lane contradicts the boundaries. | unseen: The car
                        ahead and distance obscure the far end of the lane; no arrow, stop line or waiting
                        area is inferred there. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a solid yellow center line prohibits crossing into
                        the opposing side for overtaking or changing position.
Step 5  Rule            right_boundary: A broken white roadway edge line permits crossing when necessary and
                        safe, while yielding to roadside and non-motorized traffic; it does not authorize
                        ordinary travel along that strip.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing to the left.
Step 6  change_right    allowed (correct): The broken white edge line permits a safe crossing when necessary,
                        subject to yielding to non-motorized traffic.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_determined: The distant lane-end markings are obscured by the vehicle ahead and
                        cannot be read.
Step 6  turn_right      not_determined: The distant lane-end markings are obscured by the vehicle ahead and
                        cannot be read.
Step 6  u_turn          not_determined: The distant lane-end markings are obscured by the vehicle ahead and
                        cannot be read.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within the motor-vehicle lane without crossing the yellow center line; cross
                        the broken right edge only when necessary and safe, yielding to scooters and cyclists.
                        Check the junction markings and signal as they become clear before selecting a turn or
                        stopping position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 870, 16.7 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866900144753000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, judging from the road
                        layout, median fencing and traffic-signal design. My car is in the rightmost of three
                        same-direction lanes approaching a signal-controlled intersection. (lanes 3, mine 3,
                        full)
Step 2  Left            A continuous white solid line separates my lane from another same-direction lane on
                        the left.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs alongside a raised curb, with a paved sidewalk and trees
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow with a forward-pointing head and straight shaft
                        is painted ahead in my lane.; line:stop_line (partial): A transverse white stop line
                        is faintly visible ahead of the arrow, near the intersection approach.; line:crosswalk
                        (partial): White pedestrian-crossing stripes extend across the road ahead; their
                        distant portions are difficult to distinguish.
Step 4  Cross-check     position: Two same-direction lanes lie to the left, and the curb is immediately to the
                        right, consistent with lane 3 of 3. | roles: The solid white separator fits a lane
                        line on the intersection approach; the curbside white line fits a roadway edge. |
                        markings: The straight arrow agrees with a through lane; the stop line and crossing do
                        not supply additional permitted turn directions. | unseen: The country is inferred
                        rather than confirmed, and the distant transverse markings have only partial evidence.
                        | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a solid white lane separator
                        prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: The curb forms a physical roadway boundary that my car must not cross
                        onto the sidewalk.
Step 5  Rule            arrow:straight: A straight-only lane arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line indicates where to stop when required by the signal or
                        traffic control, but does not independently require every vehicle to stop.
Step 5  Rule            line:crosswalk: The crosswalk requires attention to pedestrians and yielding as
                        required, without changing the lane's permitted directions.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white lane separator prohibits crossing
                        to the left.
Step 6  change_right    prohibited (WRONG, label not_determined): The raised curb prohibits moving onto the
                        sidewalk.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel; do not cross its solid left boundary or turn
                        from it. The signal ahead appears red: stop before the stop line, keep the pedestrian
                        crossing clear, and proceed only when permitted.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['arrow:straight', 'line:crosswalk', 'line:stop_line'], missed []), actions False,
                        unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1173, 16.31 s

mapdr__VehicleLane_1036e89588864e379ce8660a432e9b10_1711866903744814000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the road layout, median
                        fencing and signal design. My car is in the rightmost approach lane of a divided urban
                        road at a signal-controlled intersection; three same-direction lanes appear present,
                        although the car on the left obscures part of the approach. (lanes 3, mine 3, partial)
Step 2  Left            A single solid white line runs along the left of my lane toward the stop line, with
                        another same-direction traffic lane and a white car beyond it.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line borders the right of my lane beside a raised paved island
                        and curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is clearly visible in my
                        lane; its lower shaft is obscured by the hood.; line:stop_line (full): A solid white
                        transverse stop line crosses my lane immediately before the pedestrian crossing.;
                        line:crosswalk (full): White zebra-crossing stripes extend across my lane beyond the
                        stop line.
Step 4  Cross-check     position: The left lane divider and right roadway edge place my car in the rightmost
                        lane; the total of three lanes is less certain because the adjacent car obscures the
                        left portion. | roles: The solid white left divider fits a same-direction approach
                        lane boundary, and the solid white right line beside a curb fits a roadway edge. |
                        markings: The visible straight arrow agrees with a through approach lane ending at a
                        stop line and pedestrian crossing; no waiting area is visible. | unseen: The arrow
                        shaft and parts of the adjacent lanes are obscured; no additional arrowhead or hidden
                        marking has been assumed. | result: consistent
Step 5  Rule            left_boundary: Under Chinese road-marking rules, the solid white lane divider
                        prohibits crossing into the adjacent lane.
Step 5  Rule            right_boundary: The raised curb forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            arrow:straight: The straight-ahead lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the traffic
                        signal, rather than independently requiring a stop on every approach.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires yielding to pedestrians and keeping
                        the crossing unobstructed.
Step 6  change_left     prohibited (WRONG, label not_determined): The solid white lane divider prohibits
                        crossing to the left.
Step 6  change_right    prohibited (WRONG, label not_determined): The raised curb prohibits leaving the lane
                        to the right.
Step 6  go_straight     allowed (correct): The clearly visible forward arrowhead permits straight travel.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the visible arrowhead determines the permitted movement despite its hidden
                        shaft, boundaries govern only lateral changes, and the stop line does not
                        independently impose stop_first.
Advice                  Use this lane only to proceed straight, without crossing either boundary. Obey the
                        applicable traffic signal, stopping before the stop line when required, and keep the
                        pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1362, 17.19 s

mapdr__VehicleLane_adbfaa44038e457ea9871c13ec8fbfbe_1711407599241124000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely mainland China, inferred from the simplified Chinese advertising and
                        right-hand traffic. My car follows a bus in the single through lane of its direction
                        on a two-way urban street; the bus obscures the road farther ahead, and no
                        intersection is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A single continuous yellow line runs along my left, with opposing vehicles beyond it;
                        no curb forms this boundary.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single continuous white line runs along my right, separating the through lane from a
                        roadside strip occupied by parked cars; the sidewalk curb is beyond that strip.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One through lane in my direction agrees with a center line on the left and a
                        roadway edge line on the right; the parking strip is not counted as another through
                        lane. | roles: The solid yellow center line separates opposing traffic, and the solid
                        white edge line separates the through lane from the roadside strip. | markings: No
                        guidance markings are visible within the exposed part of my lane. | unseen: The bus
                        hides the farther lane surface, so no arrows, transverse lines, intersection layout,
                        or lane ending beneath or beyond it have been inferred. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a solid yellow center line prohibits crossing into
                        the opposing-traffic side for overtaking or changing position.
Step 5  Rule            right_boundary: A solid white roadway edge line permits temporary crossing for a
                        lawful roadside stop where otherwise permitted, but does not make the roadside strip a
                        through lane.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing to the left.
Step 6  change_right    allowed (WRONG, label prohibited): The white edge line permits temporary crossing to
                        pull over where stopping is otherwise lawful, not continued driving in the roadside
                        strip.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along the
                        lane.
Step 6  turn_left       not_determined: The bus hides the lane farther ahead and any movement markings at its
                        end.
Step 6  turn_right      not_determined: The bus hides the lane farther ahead and any movement markings at its
                        end.
Step 6  u_turn          not_determined: The bus hides the lane farther ahead and any movement markings at its
                        end; the center line governs crossing the current boundary, not an unseen intersection
                        movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue behind the bus without crossing the yellow center line, leaving enough space
                        to see upcoming markings. Do not use the parked-car strip as a travel lane; roadside
                        signs may prohibit stopping, and turn choices must wait until the road ahead is
                        visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 6424, out 1004, 22.08 s

mapdr__VehicleLane_b4cc0a67c39b467a9b43113660cf42ed_1710812102619029000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, suggested by the Chinese
                        signs and road layout. My car is in the sole lane of a narrow, barrier-enclosed ramp
                        continuing downhill; its eventual junction is too distant to resolve. (lanes 1, mine
                        1, full)
Step 2  Left            A pale, apparently white continuous solid line runs beside a raised concrete barrier
                        topped by a guardrail, with a screened structure beyond; sunlight gives this side a
                        yellow-green cast.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white continuous solid line runs beside a raised concrete wall topped by metal
                        railings, with a separate paved walkway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane, indexed 1, agrees with physical roadway edges on both sides and no
                        adjacent traffic lane. | roles: The continuous white lines beside the concrete
                        barriers fit roadway edge lines. | markings: No arrows, words, symbols or transverse
                        markings are discernible in the visible lane. | unseen: No junction layout or distant
                        lane-use marking is inferred; the far end is unresolved. | result: consistent
Step 5  Rule            left_boundary: The roadway edge and concrete barrier do not permit driving out of the
                        lane to the left.
Step 5  Rule            right_boundary: The roadway edge and concrete barrier do not permit driving out of the
                        lane to the right.
Step 6  change_left     prohibited (correct): The concrete barrier physically closes the left roadway edge.
Step 6  change_right    prohibited (correct): The concrete wall physically closes the right roadway edge.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing along this lane,
                        and neither edge line prohibits forward travel.
Step 6  turn_left       not_determined: The eventual junction and any markings governing a left turn are too
                        distant to resolve.
Step 6  turn_right      not_determined: The eventual junction and any markings governing a right turn are too
                        distant to resolve.
Step 6  u_turn          not_determined: The eventual junction and any markings governing a U-turn are too
                        distant to resolve.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within this single confined lane; neither side offers a lane-change
                        opportunity. Reassess the signs, markings and junction layout when closer, since the
                        eventual turning arrangements cannot yet be read.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 838, 18.42 s

mapdr__VehicleLane_b60541c776134f089e676ba51ee4417f_1709865113125919000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the blue
                        license plates, road layout and shared bicycles. My car is in the rightmost of two
                        motor-vehicle lanes on a divided urban road, with a bicycle lane to the right and a
                        pedestrian crossing ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line with long dashes and visible gaps separates my lane from the
                        motor-vehicle lane containing the blue car; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with long dashes and gaps separates my lane from a red-surfaced
                        bicycle lane with a bicycle symbol; the roadside curb is beyond that lane.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        line:crosswalk (partial): White pedestrian-crossing stripes extend across my lane
                        ahead, with part of the crossing obscured by the car ahead.
Step 4  Cross-check     position: Two motor-vehicle lanes and position 2 agree with a same-direction lane on
                        the left and a bicycle lane beyond the right roadway boundary. | roles: The broken
                        white left line fits a same-direction lane divider; the broken white right line
                        borders the visibly marked bicycle lane. | markings: The pedestrian crossing is
                        compatible with both boundaries. The bicycle symbol is outside my lane and is not an
                        ego-lane marking. | unseen: No arrows or words are readable in my lane; the crossing
                        is partly obscured, and the more distant intersection layout cannot be established. |
                        result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese rules, a broken white same-direction lane
                        divider permits changing lanes when safe without obstructing other traffic.
Step 5  Rule            right_boundary: The adjacent lane is designated for non-motorized traffic, so its
                        broken boundary does not authorize an ordinary car to change into it for normal
                        travel.
Step 5  Rule            line:crosswalk: Approach the pedestrian crossing slowly and stop to yield to
                        pedestrians crossing; the crossing itself does not prescribe a lane-exit direction.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change into the
                        adjacent motor-vehicle lane.
Step 6  change_right    prohibited (correct): The right boundary leads into a marked bicycle lane, which an
                        ordinary car may not use as a travel lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this motor-vehicle lane, or change left only when safe; do not move into
                        the bicycle lane. Slow for the pedestrian crossing and stop for crossing pedestrians;
                        determine any turning lane requirements farther ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1086, 14.49 s
```
