# Reasoning of lane run 20261115_230516_laneD_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely China, inferred from the Chinese writing on the roadside bus-lane sign,
                        with traffic keeping right. My car is in the rightmost of three same-direction lanes
                        on a divided road approaching an overpass; no intersection or lane ending is visible.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction traffic lane; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from a paved shoulder, with a guardrail
                        farther beyond the shoulder rather than directly on the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on my left and roadway edge on my right agree with being in
                        lane 3 of 3. | roles: The broken white line fits a same-direction lane divider, and
                        the solid white line fits a roadway edge beside a shoulder. | markings: No guidance
                        markings are visible within my lane, so none contradict the boundaries. | unseen: No
                        markings are inferred beneath vehicles or beyond the visible road; the next
                        intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits changing into the
                        adjacent ordinary traffic lane when safe.
Step 5  Rule            right_boundary: The solid white roadway edge does not permit an ordinary lane change
                        onto the shoulder during normal driving.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing into the adjacent
                        ordinary lane when safe.
Step 6  change_right    prohibited (correct): The solid white edge line bounds a shoulder, not a traffic lane
                        available for normal driving.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along my
                        lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change one lane left after checking traffic; do not cross
                        the right edge line onto the shoulder in normal driving. The far-left lane has a timed
                        bus-lane sign, so check its restrictions before considering that lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 838, 15.53 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        roadside writing, plates and road layout. My car is in the rightmost of two same-
                        direction lanes on a divided road approaching an underpass; no intersection or lane
                        ending is visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved shoulder and then a
                        metal guardrail beyond it; no curb forms the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider and right roadway edge agree with my car being in lane
                        2 of 2. | roles: The broken white line fits a same-direction lane divider, and the
                        continuous white line beside the shoulder fits a roadway edge. | markings: No guidance
                        markings are visible within my lane, so none conflict with the boundaries. | unseen:
                        No hidden arrow, intersection marking or lane ending has been assumed; distant
                        pavement is partly obscured by vehicles. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing to
                        change lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge separates the travel lane from the
                        shoulder, which must not be used for an ordinary lane change or routine driving.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent travel lane.
Step 6  change_right    prohibited (correct): The right edge borders a shoulder rather than another travel
                        lane; routine movement onto it is prohibited.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane toward the underpass; change left only after checking the nearby
                        vehicles and finding a safe gap. Keep off the right shoulder; no turning lane or
                        stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 986, 22.67 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the simplified
                        Chinese motorway signs and blue vehicle plates. My car is in the rightmost of two
                        regular traffic lanes on a divided expressway continuing ahead, with an emergency
                        shoulder on the right and no visible intersection or lane ending. (lanes 2, mine 2,
                        full)
Step 2  Left            A single broken white line, appearing cream-tinted in the image, has visible dashes
                        and gaps and separates my lane from another same-direction traffic lane; no curb forms
                        this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line, appearing cream-tinted in the image, separates my lane
                        from the paved emergency shoulder; the guardrail is beyond the shoulder rather than
                        directly at my lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two regular lanes and ego position 2 agree with a same-direction lane line
                        on the left and a roadway edge line on the right; the emergency shoulder is not
                        counted as a regular lane. | roles: The broken white separator fits a lane line, and
                        the continuous white shoulder boundary fits an edge line. | markings: No painted
                        arrows, words, symbols, transverse lines or waiting areas are visible in my lane; the
                        overhead arrows are signs, not pavement markings. | unseen: No unseen intersection,
                        pavement arrow or waiting area has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits changing to the
                        adjacent same-direction lane when safe without obstructing traffic.
Step 5  Rule            right_boundary: The solid expressway edge line bordering the emergency shoulder
                        prohibits crossing into that shoulder during ordinary driving.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid edge line prohibits ordinary
                        crossing into the emergency shoulder.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in your current lane; change left only after checking the truck and other
                        traffic, and do not enter the emergency shoulder during ordinary driving. Observe the
                        overhead lane-specific speed signs and maintain a safe following distance.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 860, 16.52 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese storefront
                        lettering and road context. My car is in the rightmost lane of a multilane urban
                        elevated road continuing ahead; the full lane count on the left is obscured by
                        vehicles. (lanes None, mine None, insufficient)
Step 2  Left            A yellow broken longitudinal line, with several dashes and gaps visible, separates my
                        lane from another same-direction traffic lane on the left; there is no curb here.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right roadway edge, with yellow longitudinal
                        dashes immediately inside it and a narrow paved margin and raised bridge barrier
                        beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (partial): Yellow elongated rectangular dashes run along the right side
                        of my lane, inside the white edge line; their precise marking function is uncertain.
Step 4  Cross-check     position: The left lane line and right roadway edge establish that my lane is
                        rightmost; vehicles obscure enough of the left roadway to prevent a reliable total
                        lane count or numerical lane index. | roles: The white solid line fits a roadway edge.
                        The yellow broken line is unusual for an ordinary same-direction separator, but
                        visible vehicle orientations support that role rather than a center line. | markings:
                        No directional arrow, word, transverse stop line, or waiting area is visible. The
                        yellow dashes beside the right edge do not establish a permitted turning movement. |
                        unseen: The exact function of the yellow edge-side dashes and the markings at any
                        eventual intersection are not readable; neither is inferred. | result: consistent
Step 5  Rule            left_boundary: A broken lane separator permits crossing to the adjacent same-direction
                        lane when safe, provided no other restriction applies.
Step 5  Rule            right_boundary: The solid roadway edge does not permit an ordinary lane change into
                        the paved margin or bridge barrier.
Step 5  Rule            symbol:other: These incompletely identified longitudinal yellow dashes do not
                        establish permission for any of the seven assessed maneuvers.
Step 6  change_left     allowed (correct): The visible broken lane separator permits crossing into the same-
                        direction lane when safe.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid white roadway edge and bridge
                        barrier prohibit an ordinary move to the right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this continuing lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or move left across the broken separator only after checking
                        traffic; do not cross the right roadway edge. No intersection movement guidance or
                        stopping point is visible, so reassess when those markings come into view.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1370, 37.05 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        road lettering and surrounding signs. My car is in the rightmost of three same-
                        direction lanes on a divided urban road; no intersection or lane ending is clearly
                        visible ahead. (lanes 3, mine 3, full)
Step 2  Left            A yellow broken line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction traffic lane on the left; there is no curb.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 2  Right           Yellow broken segments lie immediately inside a continuous white road-edge line on the
                        right, with the yellow segments nearer my lane; a paved shoulder and then a concrete
                        barrier lie beyond.
                        white solid_dashed (near line dashed), curb no, edge_line, evidence full
Step 3  Markings        text:bus (partial): White Chinese lettering runs lengthwise along my lane and
                        identifies it as a bus-only lane; the nearest portion is cut off by the hood, while
                        交、专、用 are visible.
Step 4  Cross-check     position: Two same-direction lanes lie to the left, and the roadway edge lies to the
                        right, consistent with my lane being third and rightmost; its left boundary separates
                        a reserved lane from general traffic. | roles: The yellow broken reservation marking
                        agrees with the bus-lane lettering; the continuous white line on the right marks the
                        road edge, with additional yellow broken reservation segments immediately inside it. |
                        markings: The bus-only lettering and yellow broken reservation markings agree; no
                        directional arrow is visible in the unobstructed portion of my lane. | unseen: The
                        nearest part of the bus lettering and the distant lane surface are partly obscured; no
                        reserved operating hours or intersection movements have been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The broken boundary permits leaving this bus lane for the adjacent
                        general-traffic lane when safe; it does not make ordinary-car use of the bus lane
                        permissible.
Step 5  Rule            right_boundary: The continuous white roadway edge does not permit an ordinary lane
                        change onto the shoulder, despite the yellow broken reservation segments inside it.
Step 5  Rule            text:bus: The bus-only lettering reserves this lane for eligible vehicles during its
                        operating period; because that period is not visible, an ordinary car should treat it
                        as reserved.
Step 6  change_left     allowed (contested, correct): The broken special-lane boundary permits leaving for the
                        general-traffic lane when safe.
Step 6  change_right    prohibited (contested, label allowed): The solid white roadway edge bars an ordinary
                        move onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No visible directional arrow restricts continuing
                        straight; the bus reservation separately restricts ordinary-car occupancy of this
                        lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the broken left boundary permits exiting the reserved lane, the solid road
                        edge prohibits moving right onto the shoulder, and the straight-ahead classification
                        does not authorize ordinary-car use of the bus lane.
Advice                  As an ordinary car, move safely left across the broken yellow boundary into a general-
                        traffic lane rather than continuing in the marked bus lane. Do not move onto the right
                        shoulder; no visible arrow establishes a turning lane or a stopping point here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions ['change_right prohibited
                        with the broken line of a solid-and-broken pair nearer my lane']
Tokens                  in 6424, out 1161, 24.41 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese road
                        signs and road layout. My car is in a single motor-vehicle lane approaching an
                        underpass, separated by a barrier from the parallel roadway on the left and by a
                        painted line from a scooter/non-motorized strip on the right; no intersection is
                        visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous solid white line runs beside a raised concrete barrier on the left, with
                        a parallel roadway beyond the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from a paved roadside strip occupied
                        by scooters; the raised sidewalk curb lies beyond that strip, not directly against my
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One motor-vehicle lane between two roadway edges agrees with my lane being
                        both the leftmost and rightmost lane of this separated carriageway; lanes beyond the
                        concrete barrier are not counted as adjacent lanes. | roles: The solid white paint is
                        consistent with roadway-edge boundaries, and the left barrier confirms a physical
                        separation. | markings: No arrows, words, symbols, transverse lines or waiting areas
                        are visible in my lane. | unseen: No markings are inferred inside the dark underpass;
                        the eventual intersection and its lane guidance are not visible. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and concrete barrier do not permit my car to
                        leave the lane across the left side.
Step 5  Rule            right_boundary: The solid white roadway edge separating the motor-vehicle lane from
                        the roadside non-motorized strip prohibits crossing into that strip in ordinary
                        driving.
Step 6  change_left     prohibited (correct): The concrete barrier and solid left roadway edge prohibit
                        crossing left.
Step 6  change_right    prohibited (correct): The solid right roadway edge prohibits crossing into the
                        roadside strip.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the boundaries govern only lateral departures, and the absence of visible
                        movement arrows does not establish permission to turn at an unseen intersection.
Advice                  Continue within the solid white edges toward the underpass; do not cross the barrier
                        side or enter the scooter strip. Check the overhead restrictions and watch for
                        scooters near the right boundary; no visible marking identifies a turning lane or
                        stopping point.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 885, 18.48 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese writing and
                        road setting. My car is in the right-hand lane of a narrow urban road approaching a
                        pedestrian crossing, with bus shelters to the left and a raised bicycle-parking
                        sidewalk to the right; no intersection is clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A continuous white line separates my lane from another paved lane on the left; no curb
                        lies along this dividing line.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A raised curb with a continuous yellow-painted roadside face borders my lane, with
                        parked bicycles and scooters on the raised pavement beyond.
                        yellow solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A thin white transverse line crosses my lane immediately before
                        the pedestrian crossing.; line:crosswalk (full): White zebra-crossing bars extend
                        across my lane ahead.
Step 4  Cross-check     position: Two lanes and position 2 agree with a lane divider on the left and the
                        roadway curb on the right. | roles: The white solid divider fits a same-direction lane
                        boundary; the yellow-painted curb marks the physical roadway edge rather than an
                        opposing-traffic center line. | markings: The transverse line and pedestrian crossing
                        are compatible; no directional arrow or word is visible in my lane. The partial
                        foreground arrow is left of my lane boundary. | unseen: No reservation of the left
                        lane is inferred from the bus shelters alone, and no unseen intersection movements are
                        assumed. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white same-direction lane divider prohibits crossing
                        it to change lanes.
Step 5  Rule            right_boundary: The raised roadway curb is not a traversable lane boundary and
                        prohibits moving out of this lane onto the sidewalk.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when stopping is required, but
                        does not by itself impose a mandatory stop or select a movement.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires approaching cautiously and yielding
                        to pedestrians, without assigning a lane movement.
Step 6  change_left     prohibited (correct): The solid white lane divider prohibits crossing into the left
                        lane.
Step 6  change_right    prohibited (correct): The raised curb prohibits moving onto the sidewalk.
Step 6  go_straight     allowed (contested, correct): No directional marking restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within this lane without crossing the solid left divider or mounting the
                        right curb. Slow for the pedestrian crossing, yield to pedestrians, and stop before
                        the transverse line when required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1114, 22.96 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, likely Beijing, based on the Chinese place names and blue
                        vehicle plates; traffic keeps right. My car is in the left lane of a two-lane branch
                        beside a busier parallel carriageway, with a painted separation area on the left;
                        traffic obscures the road farther ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line borders my lane on the left, with a tapered, diagonally hatched
                        separation area and parallel same-direction traffic beyond; no curb forms this
                        boundary.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with visible long segments and intervening gaps, separates my
                        lane from another same-direction motor-vehicle lane on the right; there is no curb at
                        this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The two-lane count refers to this branch, not the parallel carriageway
                        beyond the painted separation. A left edge boundary and a right lane divider agree
                        with my lane being lane 1 of 2. | roles: The solid white boundary borders the painted
                        separation, while the dashed white boundary divides adjacent same-direction lanes. |
                        markings: No readable arrow, word, symbol, or transverse line is visible inside my
                        lane; the hatching is outside its left boundary. | unseen: Vehicles conceal pavement
                        farther ahead, so no assertion is made about markings beneath them or at an unseen
                        intersection. | result: consistent
Step 5  Rule            left_boundary: In China, the solid white boundary of a channelized separation area
                        must not be crossed to move into the parallel carriageway.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes when
                        safe and without obstructing other traffic.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white boundary adjoining the channelized
                        separation prohibits crossing left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change into the
                        adjacent lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight
                        along this lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary rules govern only lateral crossings, and no unseen lane-use
                        marking has been assumed.
Advice                  Continue within this branch and do not cross the solid boundary or hatched separation
                        on the left. A rightward lane change is permitted when safe; keep a safe following
                        distance and reassess turn guidance when the obscured pavement becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 986, 23.38 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test D | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the road
                        layout, vehicles and roadside setting. My car is in the leftmost of two motor-vehicle
                        lanes on a divided urban road; a separated roadside lane is on the right, and no
                        intersection or lane ending is visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A continuous solid white line runs beside a raised curb and planted median on the
                        left, with the opposite carriageway beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and intervening gaps, separates my lane
                        from another motor-vehicle lane traveling in the same direction; there is no curb at
                        this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median-side edge on the left and a same-direction lane on the right
                        agree with my lane being lane 1 of 2. | roles: The solid white line beside the median
                        is an edge line, not a center line; the broken white line on the right is consistent
                        with a same-direction lane divider. | markings: No arrows, words, symbols, transverse
                        lines or waiting areas are visible in my lane. | unseen: No distant intersection
                        layout or obscured pavement marking has been inferred; vehicles obscure portions of
                        the road farther ahead. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese road rules, the solid median-side edge and
                        raised curb do not permit leaving the lane to the left.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing right when
                        safe and without interfering with other traffic.
Step 6  change_left     prohibited (correct): The solid median-side boundary and raised curb prohibit crossing
                        to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent motor-vehicle lane.
Step 6  go_straight     allowed (contested, correct): No visible arrow or lane-ending marking restricts
                        continuing along my lane.
Step 6  turn_left       not_applicable: No visible marking governs a left turn at a lane end.
Step 6  turn_right      not_applicable: No visible marking governs a right turn at a lane end.
Step 6  u_turn          not_applicable: No visible marking governs a U-turn.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change one lane right across the broken white line after
                        checking traffic; do not cross the median-side boundary. No intersection turn guidance
                        or stopping point is visible, so reassess the markings as you approach the next
                        junction.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 867, 17.29 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese road sign,
                        vehicle plates and traffic arrangement. My car is within a broad signal-controlled
                        intersection, following the silver car; lane divisions are absent in the foreground,
                        so the number of approach lanes and my lane index cannot be reliably counted. (lanes
                        None, mine None, insufficient)
Step 2  Left            No painted boundary or curb immediately borders my path on the left within the
                        intersection; opposing vehicles are visible farther left.
                        none none, curb no, unknown, evidence full
Step 2  Right           No painted boundary or curb immediately borders my path on the right within the
                        intersection; a taxi travels ahead to the right, and the roadside curb is farther
                        away.
                        none none, curb no, unknown, evidence full
Step 3  Markings        line:crosswalk (partial): White zebra-crossing stripes extend across the road ahead,
                        with the portion directly ahead partly obscured by the silver car.
Step 4  Cross-check     position: The unmarked intersection foreground does not support a reliable lane count
                        or lane index; no lane-boundary roles have been inferred from vehicle positions. |
                        roles: Neither side has a visible immediate painted boundary or physical edge, so
                        neither is classified as a lane line or center line. | markings: The crosswalk is
                        consistent with the intersection; no lane-use arrow, word or waiting area is visible
                        in my path. | unseen: No approach-lane markings or markings beneath the vehicles have
                        been inferred. | result: consistent
Step 5  Rule            left_boundary: No visible left boundary marking governs crossing this side within the
                        intersection; its absence does not establish that a lateral maneuver is safe or
                        otherwise lawful.
Step 5  Rule            right_boundary: No visible right boundary marking governs crossing this side within
                        the intersection; its absence does not establish that a lateral maneuver is safe or
                        otherwise lawful.
Step 5  Rule            line:crosswalk: In China, the zebra crossing identifies a pedestrian crossing where
                        drivers must yield as required, but it does not prescribe any of the seven lane
                        movements.
Step 6  change_left     not_applicable: No painted boundary or curb governs this side in the visible
                        intersection stretch.
Step 6  change_right    not_applicable: No painted boundary or curb governs this side in the visible
                        intersection stretch.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight through the intersection.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Maintain a predictable straight path through the intersection and yield to anyone
                        using the crosswalk; the signals ahead appear green. The visible markings do not
                        establish a turning lane or authorize lateral movements, so do not infer turn
                        permission from the open pavement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1028, 20.07 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is most likely mainland China, inferred from the Chinese flags, Chinese writing
                        and road furniture; traffic keeps right. My car is in the leftmost of two same-
                        direction lanes on a divided urban road, with a junction visible in the distance.
                        (lanes 2, mine 1, full)
Step 2  Left            A continuous yellow line runs beside a physical central divider with white metal
                        fencing; opposing traffic is beyond the divider.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A broken white line, with multiple visible dashes and gaps, separates my lane from
                        another same-direction lane occupied by the black sedan.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Repeated groups of pale transverse rectangular paint blocks cross
                        my lane, forming speed-reduction markings; more distant pavement is partly obscured by
                        the car ahead.
Step 4  Cross-check     position: Two lanes and position 1 agree with a central divider on the left and a
                        same-direction lane line on the right. | roles: The solid yellow line beside the
                        central barrier fits separation from opposing traffic; the broken white line fits
                        separation of same-direction lanes. | markings: The transverse speed-reduction
                        markings do not specify a turning direction and do not conflict with either boundary.
                        | unseen: No distant arrow, stop line or waiting area is claimed; the vehicle ahead
                        and distance limit inspection of the lane near the junction. | result: consistent
Step 5  Rule            left_boundary: In China, the solid yellow opposing-traffic separation and physical
                        central barrier prohibit crossing this boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes when
                        safe without obstructing traffic.
Step 5  Rule            symbol:other: Transverse speed-reduction markings advise reducing speed but do not
                        assign permitted turning movements.
Step 6  change_left     prohibited (correct): The solid yellow central boundary and physical barrier prohibit
                        crossing left.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  go_straight     allowed (contested, label not_determined): No visible directional arrow restricts
                        continuing straight along this lane.
Step 6  turn_left       not_determined: The distant junction approach is partly hidden, so any lane-use arrow
                        governing a left turn cannot be established.
Step 6  turn_right      not_determined: The distant junction approach is partly hidden, so any lane-use arrow
                        governing a right turn cannot be established.
Step 6  u_turn          not_determined: The distant junction approach is partly hidden, so any pavement
                        marking governing a U-turn cannot be established.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Reduce speed over the transverse warning markings and do not cross the central
                        divider. A right lane change is permitted by the dashed line, but the black sedan is
                        alongside; wait for a safe gap and check the junction's arrows, signs and signals
                        before choosing a turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 980, 20.54 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, inferred from the road
                        layout, signs and surrounding urban infrastructure, though the country is not certain.
                        My car is on a single-lane, barrier-lined ramp that descends and bends right; no
                        intersection or lane ending is visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous solid white line runs along the left of my lane, with a narrow paved
                        margin and a concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line runs along the right of my lane, with a wider paved
                        shoulder and a concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (partial): Closely spaced pale transverse bands are visible across the
                        lane ahead; their exact construction and marking type cannot be resolved at this
                        distance.
Step 4  Cross-check     position: Both boundaries are roadway edges, consistent with one lane and my car
                        occupying lane 1. | roles: The solid white lines, paved margins and barriers support
                        edge-line roles rather than lane-line or center-line roles. | markings: No directional
                        arrows, words or waiting areas are visible; the transverse bands do not contradict the
                        single-lane ramp layout. | unseen: The country remains an inference, and the
                        transverse bands are not identified more specifically than the image supports. |
                        result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, the solid roadway edge prohibits
                        crossing left into the margin, and the barrier also prevents passage.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, the solid roadway edge prohibits
                        crossing right onto the shoulder in ordinary driving.
Step 5  Rule            symbol:other: The incompletely identified transverse bands establish no directional
                        permission or stop-first requirement for the seven assessed actions.
Step 6  change_left     prohibited (correct): The solid white left edge prohibits crossing into the margin.
Step 6  change_right    prohibited (correct): The solid white right edge prohibits crossing onto the shoulder.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing along the ramp, including
                        its rightward bend.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid white edges and follow the ramp around the right-hand bend;
                        do not use the shoulder as another lane. Observe the visible 40 speed-limit sign and
                        approach the transverse bands cautiously; no marked stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 997, 20.15 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, inferred from the expressway
                        signs and median anti-glare screens, though the country is not certain. My car is in
                        the leftmost of two through lanes on a divided expressway approaching an overpass; no
                        intersection or lane ending is visible. (lanes 2, mine 1, full)
Step 2  Left            A continuous yellow-looking solid line borders the narrow median strip, with a raised
                        edge and metal barrier beyond; the windshield tint affects the apparent colour.
                        yellow solid, curb yes, edge_line, evidence partial
Step 2  Right           A white broken line, with several visible dashes and gaps, separates my lane from
                        another through lane travelling in the same direction; there is no curb on this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego position 1 agree with a median edge on the left and a
                        same-direction lane on the right. | roles: The continuous left marking follows the
                        median edge; the broken white right marking separates through lanes. | markings: No
                        guidance markings are visible within my lane; the markings farther right are outside
                        it. | unseen: The country is inferred, not confirmed, and the left paint colour is
                        qualified because of the image tint. No unseen intersection markings are assumed. |
                        result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese expressway rules, the solid median edge and
                        physical median boundary must not be crossed.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent
                        ordinary traffic lane when safe.
Step 6  change_left     prohibited (correct): The solid median edge and physical barrier prohibit leaving the
                        lane to the left.
Step 6  change_right    allowed (correct): The broken white divider permits a safe change into the adjacent
                        through lane.
Step 6  go_straight     allowed (contested, correct): No in-lane marking restricts continuing straight, and
                        the lane visibly continues.
Step 6  turn_left       not_applicable: No in-lane arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No in-lane arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No in-lane arrow or prohibited-movement marking governs this action;
                        crossing the median is separately prohibited.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary rules govern only their respective crossing actions, and no
                        unseen intersection or guidance marking has been used to decide a movement.
Advice                  Continue along the expressway; change right only after checking traffic and clearance,
                        and never cross the median boundary. Follow the upcoming signs for exits; no stopping
                        point or turning facility is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 987, 22.93 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test D | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely mainland China, inferred from the simplified Chinese highway signs and
                        road layout; traffic keeps right. My car is in the leftmost of three same-direction
                        lanes on a divided expressway continuing straight, with no junction or lane ending
                        visible. (lanes 3, mine 1, full)
Step 2  Left            A single solid white line runs along the left of my lane beside a narrow paved margin
                        and a metal median barrier; opposing traffic is beyond the barrier, and sunlight
                        reduces the paint's contrast.
                        white solid, curb yes, edge_line, evidence partial
Step 2  Right           A broken white line, with long painted dashes and clear gaps, separates my lane from
                        another same-direction traffic lane; there is no physical barrier on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego lane 1 agree with a median-side edge on
                        the left and another traffic lane on the right. | roles: The solid white left edge and
                        broken white right lane divider fit their respective roles on a divided Chinese
                        expressway. | markings: No guidance markings are visible on the pavement within my
                        lane; the arrows on the overhead signs are not pavement markings. | unseen: No hidden
                        pavement markings are inferred; glare reduces certainty about the left edge paint, and
                        the distant roadway cannot be inspected completely. | result: consistent
Step 5  Rule            left_boundary: The expressway's solid roadway edge and median barrier prohibit leaving
                        the lane to the left.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent
                        ordinary traffic lane when safe.
Step 6  change_left     prohibited (correct): The median barrier and solid roadway edge prohibit moving left
                        out of the lane.
Step 6  change_right    allowed (correct): The broken white divider permits crossing into the adjacent traffic
                        lane when safe.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight, and the
                        lane visibly continues.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary rules govern only lateral departures, no overhead arrow is
                        treated as a pavement marking, and unmarked turning movements are not assigned
                        permission.
Advice                  Continue straight, or change right across the broken line only after checking traffic;
                        do not move left toward the median. Observe the overhead lane-use and speed
                        restrictions, keep out of the emergency lane, and increase caution because of the
                        glare.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 862, 18.01 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        signage and road layout. My car is in the middle of three same-direction lanes
                        approaching a signal-controlled urban intersection. (lanes 3, mine 2, full)
Step 2  Left            A continuous white line separates my lane from another motor lane on the left; short
                        white teeth project into that adjacent lane, and there is no curb at my boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from the motor lane containing the silver
                        car on the right, with no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A large white arrow in my lane has a single head pointing
                        straight ahead; its lower stem is partly hidden by the hood.; line:stop_line (full): A
                        white transverse stop line crosses my lane immediately before the pedestrian
                        crossing.; line:crosswalk (full): Broad white pedestrian-crossing stripes extend
                        across my lane beyond the stop line.
Step 4  Cross-check     position: Two lane-line boundaries agree with my position in lane 2 of 3, with one
                        same-direction lane on each side. | roles: Both boundaries are white solid lane
                        separators, consistent with lanes approaching an intersection. | markings: The single
                        straight-ahead arrow agrees with a through lane; the stop line precedes the crosswalk.
                        The teeth beside the left boundary lie outside my lane. | unseen: The hood hides the
                        bottom of the arrow stem, but its single straight head is visible; no hidden
                        directional head or waiting area has been assumed. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a solid white lane separator prohibits crossing it
                        to change lanes.
Step 5  Rule            right_boundary: In mainland China, a solid white lane separator prohibits crossing it
                        to change lanes.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the traffic
                        controls, but does not itself require stopping on every approach.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires attention and yielding to pedestrians
                        as required, without selecting the lane's permitted direction.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The visible single straight-ahead arrow permits proceeding
                        straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the visible arrow head determines the movements despite its obscured stem,
                        both solid boundaries prohibit lane changes, and the stop line alone does not impose a
                        mandatory full stop.
Advice                  Continue straight in this lane subject to the traffic signals, and do not cross either
                        solid boundary. If required to stop, stop before the stop line and keep the pedestrian
                        crossing clear; turning requires selecting an appropriate lane before the solid-line
                        approach.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1210, 22.56 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese signs
                        and traffic layout. My car is approaching a broad signalized urban intersection;
                        adjacent lanes are visible, but the complete lane count and my lane's index cannot be
                        established confidently from this view. (lanes None, mine None, insufficient)
Step 2  Left            A white solid line runs along the left side of my lane to the transverse stop line,
                        with short diagonal white strokes on its far side; another traffic lane lies beyond,
                        and there is no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white solid line runs along the right side of my lane toward the stop line, with
                        another traffic lane beyond and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A broad continuous white transverse stop line crosses my lane
                        immediately before the pedestrian crossing.; line:crosswalk (full): White zebra-
                        crossing stripes cross the roadway immediately beyond the stop line.
Step 4  Cross-check     position: Both boundaries separate my lane from adjacent traffic lanes, so my lane is
                        an interior lane; the complete lane count and numerical position remain uncertain. |
                        roles: White solid boundaries are consistent with same-direction lane separation on an
                        intersection approach. | markings: The stop line and crosswalk are consistent with the
                        intersection approach; no lane-use arrow or waiting area is visible. | unseen: No
                        arrow hidden under the hood or outside the image is inferred, and the complete lane
                        count is not guessed. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a solid white lane-dividing line prohibits crossing
                        it to change lanes.
Step 5  Rule            right_boundary: In mainland China, a solid white lane-dividing line prohibits crossing
                        it to change lanes.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal or
                        traffic control, but does not by itself require every vehicle to stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires protecting and yielding to
                        pedestrians as applicable, rather than determining the lane's permitted turning
                        movements.
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: solid boundaries prohibit lane changes but do not prohibit proceeding
                        straight, and the stop line alone does not impose a mandatory stop.
Advice                  Stay between the solid white boundaries and obey the signal controlling your lane;
                        stop before the stop line when required and keep the crosswalk clear. The visible
                        markings do not establish a permitted turn from this lane.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1206, 25.59 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, inferred from the simplified Chinese signs and road
                        layout, with traffic keeping right. My car is in the middle of three same-direction
                        lanes on a divided urban road approaching a distant intersection. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside curb is beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 2 agree with a same-direction lane across each
                        boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No pavement arrow, word, symbol, waiting area, or transverse
                        line can be reliably identified in my lane. | unseen: The distant approach is too
                        small and partly obscured by vehicles to establish its pavement markings; arrows on
                        the roadside sign are not pavement markings. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing into
                        the adjacent ordinary lane when safe.
Step 5  Rule            right_boundary: In mainland China, a broken white lane divider permits crossing into
                        the adjacent ordinary lane when safe.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change right.
Step 6  go_straight     allowed (contested, correct): No visible pavement arrow restricts continuing straight
                        along my lane.
Step 6  turn_left       not_determined: Pavement guidance at the distant intersection is not readable, leaving
                        the permitted left-turn movement undecided.
Step 6  turn_right      not_determined: Pavement guidance at the distant intersection is not readable, leaving
                        the permitted right-turn movement undecided.
Step 6  u_turn          not_determined: Pavement guidance at the distant intersection is not readable, leaving
                        U-turn permission undecided.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable.
Step 7  Reflect         Consistent: lane changes follow the visible broken dividers, straight travel is
                        unrestricted by visible pavement markings, and intersection turns remain undecided
                        because distant guidance is unreadable.
Advice                  Continue in the middle lane for now; either broken divider may be crossed after
                        checking traffic. The roadside sign indicates lane selection ahead, so confirm the
                        approaching pavement arrows and signals before choosing a turning lane or stopping
                        position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 913, 17.96 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the simplified Chinese road signs and road
                        layout, with traffic keeping right. My car is in the middle of three lanes on a
                        divided urban road approaching an intersection; additional lane organization is
                        visible farther ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with long painted dashes separated by gaps, separates my lane
                        from another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with long painted dashes separated by gaps, separates my lane
                        from another same-direction lane on the right; the roadside curb is beyond that
                        adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small white forward-pointing arrow is visible farther
                        ahead in my lane; its forward head is discernible, but the distant marking is not
                        fully clear.
Step 4  Cross-check     position: The middle position among three lanes agrees with a same-direction lane
                        beyond each boundary. | roles: Both white broken boundaries fit ordinary same-
                        direction lane dividers. | markings: The visible forward arrow agrees with a
                        continuing through lane, but distance limits confirmation of the complete arrow. |
                        unseen: No words from neighboring lanes or arrows on the roadside sign have been
                        treated as markings in my lane; the complete distant arrow and intersection stop line
                        cannot be confirmed. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A broken white lane divider permits crossing into the neighboring
                        ordinary lane when safe.
Step 5  Rule            arrow:straight: A forward lane-use arrow permits proceeding straight; other movements
                        require confirmation of whether the complete arrow contains any additional heads.
Step 6  change_left     allowed (correct): The visible broken white lane divider permits a safe left lane
                        change.
Step 6  change_right    allowed (correct): The visible broken white lane divider permits a safe right lane
                        change.
Step 6  go_straight     allowed (contested, correct): The discernible forward arrowhead permits proceeding
                        straight.
Step 6  turn_left       not_determined: The distant arrow is not clear enough to exclude an additional left-
                        turn head.
Step 6  turn_right      not_determined: The distant arrow is not clear enough to exclude an additional right-
                        turn head.
Step 6  u_turn          not_determined: The complete distant arrow cannot be read sufficiently to determine
                        U-turn guidance.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable.
Step 7  Reflect         consistent
Advice                  Continue in this lane for straight travel, checking traffic before crossing either
                        broken divider. For a turn, confirm the pavement arrows and lane-assignment signs as
                        you approach; obey the intersection signals and stop at the stop line if required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6424, out 1063, 23.65 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese direction
                        signs and roadway markings. My car is in the middle of three same-direction lanes on a
                        divided urban road approaching an intersection. (lanes 3, mine 2, full)
Step 2  Left            A continuous white line borders my lane on the left, with repeated short white bars
                        alongside it; another same-direction traffic lane lies beyond, with no curb between
                        the lanes.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with repeated short white bars
                        alongside it; another same-direction traffic lane lies beyond, with no curb between
                        the lanes.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (full): Repeated short white bars run along both sides of my lane,
                        forming longitudinal speed-reduction markings.; arrow:straight (full): A white
                        forward-pointing arrow is visible farther ahead in my lane.
Step 4  Cross-check     position: The middle position in three lanes agrees with a same-direction lane across
                        each boundary. | roles: White solid lines fit same-direction lane separators; the
                        short adjacent bars are speed-reduction markings rather than gaps in the boundary
                        lines. | markings: The straight arrow and speed-reduction markings are compatible with
                        the lane boundaries. | unseen: No stop line or crosswalk can be identified reliably at
                        the distant intersection; neither is asserted. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-separation line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: In China, a solid white lane-separation line prohibits crossing it to
                        change lanes.
Step 5  Rule            symbol:other: Longitudinal speed-reduction markings prompt reduced speed and do not
                        independently authorize or prohibit any of the seven movements.
Step 5  Rule            arrow:straight: The straight-only lane arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane.
Step 6  change_left     prohibited (contested, label allowed): The solid white left lane line prohibits
                        crossing into the adjacent lane.
Step 6  change_right    prohibited (contested, label allowed): The solid white right lane line prohibits
                        crossing into the adjacent lane.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel, reduce speed through the marked approach, and
                        do not cross either solid boundary. For a turn, select an appropriately marked lane
                        only where changing lanes is permitted; obey the intersection signals and stop line
                        when they become clearly visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight', 'symbol:other'], missed []), actions None, unsafe [], citation
                        None, contradictions []
Tokens                  in 6424, out 1110, 23.47 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test D | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the simplified
                        Chinese signs and road layout. The car is in the third of four same-direction lanes on
                        a divided urban road approaching an intersection; the distant intersection markings
                        are obscured by traffic. (lanes 4, mine 3, full)
Step 2  Left            A white broken line, with long dashes and visible gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and visible gaps, separates my lane from the
                        rightmost same-direction lane; the yellow-painted curb lies beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead,
                        with no turning branch.
Step 4  Cross-check     position: Lane 3 of 4 has a same-direction lane on each side, consistent with both
                        boundaries being lane lines. | roles: The white broken lines fit ordinary same-
                        direction lane separators. | markings: The straight-only arrow agrees with a through
                        lane; the straight-and-right arrow to the right belongs to the adjacent lane. |
                        unseen: No stop line, crosswalk, or waiting area can be identified in my lane ahead;
                        traffic and distance obscure the intersection approach. | result: consistent
Step 5  Rule            left_boundary: In mainland China, an ordinary broken white lane line permits crossing
                        to change lanes when safe and without obstructing traffic.
Step 5  Rule            right_boundary: An ordinary broken white lane line permits crossing into the adjacent
                        ordinary lane when safe.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits turning left, turning right, or making a U-turn from this lane.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane separator permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (correct): The straight-only arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to continue straight; for a right turn, change safely into the
                        rightmost lane while the separator remains broken. Use a designated left-turn lane for
                        a left turn, and obey the intersection signals and any stop line that becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1004, 20.59 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be Beijing, China, with right-hand traffic, supported by the Chinese
                        signs and the Zhongguancun South Street sign. My car is in the second lane from the
                        left on a divided urban boulevard; the bus obscures the far-right roadway, so the
                        total same-direction lane count is uncertain. (lanes None, mine 2, partial)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, visible in the foreground and partly obscured farther ahead by
                        the taxi, separates my lane from another traffic lane on the right; the bus and
                        additional painted markings lie farther right.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The lane to my left makes my lane second from the left; another lane is
                        visible immediately to my right, but the bus prevents a reliable total count. | roles:
                        The white broken boundaries fit ordinary same-direction lane dividers; neither is the
                        central divider or a curb. | markings: No readable arrow, word, symbol, transverse
                        line, or waiting area is visible within my lane; markings farther right do not govern
                        my lane. | unseen: No total lane count or distant intersection marking is inferred
                        from the obscured roadway. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to the adjacent
                        same-direction lane when safe.
Step 5  Rule            right_boundary: The visible broken white lane divider permits moving into the
                        immediately adjacent ordinary lane when safe, without authorizing entry into any
                        reserved lane farther right.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent left lane.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        change into the immediately adjacent right lane.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or cross a broken white divider only after checking
                        adjacent traffic; do not assume that a lane farther right is open to ordinary cars.
                        The forward signal is green and the left-turn signal is red, but no visible lane-use
                        arrow establishes a turning movement from your lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1343, 36.09 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, based on the Chinese direction signs and streetscape, with
                        traffic keeping right. The car is in the leftmost of two apparent same-direction motor
                        lanes on a broad urban road curving left; the distant junction details are indistinct.
                        (lanes 2, mine 1, partial)
Step 2  Left            A single continuous yellow line curves along the left of my lane, with opposing-
                        direction roadway beyond and no curb at the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           White elongated dashes separated by clear gaps border my lane on the right, with
                        another same-direction lane beyond and no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line places my lane leftmost, and the white dashed line
                        establishes another same-direction lane to the right; the outer roadway allocation is
                        less clear. | roles: The solid yellow center line and broken white same-direction lane
                        divider fit their observed roles. | markings: No arrows, words, symbols, transverse
                        lines or waiting areas are discernible in my lane. | unseen: No distant guidance
                        markings or intersection controls have been inferred; the total motor-lane count
                        remains less certain than my lane position. | result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing into the
                        opposing roadway.
Step 5  Rule            right_boundary: A broken white lane divider permits changing to the adjacent same-
                        direction lane when safe.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing into the adjacent
                        lane when safe.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing along my
                        lane.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action; the center line governs
                        crossing the boundary, not an unseen junction movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue with the road's leftward curve without crossing the solid yellow center line;
                        a right lane change is permitted only when clear. Turn permissions and any stopping
                        requirement must be checked closer to the junction, where the markings and controls
                        can be read.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 1030, 23.36 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This is likely China, with traffic keeping right, indicated by the simplified Chinese
                        signs and roadway layout. My car is in the second of five same-direction lanes on a
                        divided elevated expressway continuing straight ahead; an emergency shoulder lies on
                        the far right. (lanes 5, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): Large white Chinese pavement lettering is partially visible
                        immediately ahead of the hood; the complete inscription is cropped or obscured and
                        cannot be read confidently.
Step 4  Cross-check     position: The second of five lanes has another same-direction lane on each side,
                        consistent with both boundaries being lane lines. | roles: Both white dashed
                        boundaries fit same-direction lane dividers. | markings: The visible pavement
                        lettering does not establish a directional arrow or contradict the lane boundaries; no
                        waiting area is visible. | unseen: The obscured pavement inscription has not been
                        completed by inference, and the overhead sign arrows have not been treated as pavement
                        arrows. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 5  Rule            text:other: The partially readable pavement lettering does not independently authorize
                        or prohibit any of the seven assessed actions.
Step 6  change_left     allowed (correct): The white dashed left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white dashed right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible pavement arrow restricts continuing straight
                        along this continuing lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or cross either dashed divider only after checking clearance
                        and blind spots. Follow the overhead lane and speed signs, keep out of the emergency
                        shoulder, and do not treat the absence of turn markings as permission to turn on the
                        expressway.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 938, 16.92 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese overhead
                        signs and road layout. My car is in the second of four same-direction lanes on an
                        elevated divided road, approaching overhead signs with no visible intersection or lane
                        ending. (lanes 4, mine 2, full)
Step 2  Left            A white broken line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; no curb forms my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The second of four lanes has a same-direction lane to its left and two to
                        its right, consistent with lane-line boundaries on both sides. | roles: Both white
                        dashed boundaries fit ordinary same-direction lane dividers. | markings: No lane-use
                        arrows, words, symbols or waiting areas are visible in my lane; the transverse bridge
                        joint is not a traffic marking. | unseen: No unreadable distant marking or sign has
                        been treated as a lane restriction; the road's eventual endpoint is outside the
                        visible stretch. | result: consistent
Step 5  Rule            left_boundary: In China, a white dashed lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a white dashed lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The white dashed left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white dashed right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane; either adjacent lane may be entered across the dashed divider
                        after checking traffic and signaling. Read the overhead signs as you approach, since
                        their detailed instructions are too distant to establish here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 922, 18.19 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test D | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the road-sign style,
                        lane markings and central pedestrian-style divider. My car is in the middle of three
                        same-direction lanes on an urban arterial approaching a distant signalized
                        intersection. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        lane beside the central divider; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        traffic lane containing a scooter; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow immediately ahead points straight forward, with
                        one straight shaft and a forward-facing head.
Step 4  Cross-check     position: The middle position among three lanes agrees with an ordinary lane line on
                        each side. | roles: Both white broken boundaries fit separators between lanes
                        traveling in the same direction. | markings: The straight-only pavement arrow agrees
                        with the through-lane layout; no conflicting word, symbol or waiting area is visible.
                        | unseen: No distant stop line or additional marking concealed by the car ahead has
                        been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane separator permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: In China, a broken white same-direction lane separator permits
                        crossing to change lanes when safe.
Step 5  Rule            arrow:straight: A straight-only guidance arrow permits proceeding straight from this
                        lane and excludes left turns, right turns and U-turns from it.
Step 6  change_left     allowed (correct): The broken white left lane line permits a safe lane change.
Step 6  change_right    allowed (correct): The broken white right lane line permits a safe lane change.
Step 6  go_straight     allowed (correct): The pavement arrow expressly permits straight travel.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight and obey the intersection signals, stopping at
                        the stop line if required once it becomes visible. Lane changes across either broken
                        line are permitted when safe, but check especially for the scooter on the right; use
                        an appropriately marked lane for any turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6424, out 864, 14.93 s
```
