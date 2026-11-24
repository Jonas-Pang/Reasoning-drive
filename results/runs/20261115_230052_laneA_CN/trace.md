# Reasoning of lane run 20261115_230052_laneA_CN

```text
mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433609117850000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues toward an overpass, with no intersection or lane
                        ending visible. My car is in the rightmost of three same-direction traffic lanes,
                        beside a paved shoulder. (lanes 3, mine 3, full)
Step 2  Left            A single broken white line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line borders my lane on the right, with a paved shoulder and
                        then a guardrail beyond it; no curb forms the painted boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my lane being lane 3 of
                        3. | roles: The broken white line fits a same-direction lane divider, and the solid
                        white line fits the boundary to the shoulder. | markings: No readable guidance
                        markings are visible within my lane; nothing contradicts the boundary observations. |
                        unseen: No markings are inferred beneath vehicles or beyond the visible road; no
                        intersection markings are claimed. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge line must not ordinarily be crossed to
                        drive onto the shoulder.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change into the
                        adjacent ordinary traffic lane.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits an ordinary move onto the
                        shoulder.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow or lane ending restricts
                        continuing along my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change one lane left across the broken white line when safe;
                        do not cross the solid right edge onto the shoulder. Keep a safe following distance,
                        and observe the bus-lane restrictions indicated for the far-left lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 862, 19.54 s

mapdr__BusLane_156dfc0abe354cfbab4b501631382d4d_1709433612851257000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road continues toward an underpass, with no intersection or lane
                        ending visible. My car is in the rightmost of two visible lanes in this direction.
                        (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from the traffic
                        lane on the left; there is no curb along this line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved shoulder and
                        a metal guardrail beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with being in
                        lane 2 of 2. | roles: The broken white separator fits a same-direction lane line, and
                        the continuous white line beside the shoulder fits a roadway edge line. | markings: No
                        visible arrows, words, symbols, transverse lines or waiting areas in my lane conflict
                        with the boundaries. | unseen: No markings are inferred beneath the vehicles or beyond
                        the visible road; the next intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge does not permit ordinary driving out of
                        the traffic lane onto the shoulder.
Step 6  change_left     allowed (correct): The broken white lane line permits a safe lane change into the
                        adjacent traffic lane.
Step 6  change_right    prohibited (correct): The solid white edge line restricts ordinary crossing onto the
                        shoulder.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane toward the underpass, keeping off the right shoulder. A left
                        lane change is permitted across the broken line only when a safe gap exists; junction
                        movements cannot be selected from the markings visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1017, 26.08 s

mapdr__EmergencyLane_987cbcf5032841918cc3253559eba301_1710574770200029000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway continues straight ahead, with two regular travel lanes and an
                        emergency shoulder on the right. My car is in the right-hand travel lane; no
                        intersection or lane ending is visible. (lanes 2, mine 2, full)
Step 2  Left            A pale white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction travel lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous yellow-looking solid line separates my lane from a paved emergency
                        shoulder, with a guardrail beyond the shoulder rather than at the line.
                        yellow solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two travel lanes and ego lane index 2 agree with a lane divider on the left
                        and a shoulder edge on the right. | roles: The broken white line fits a same-direction
                        lane divider; the continuous right-hand line follows the shoulder edge, and its
                        observed yellow tint does not make it a center line. | markings: No pavement arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane. | unseen: No
                        markings are inferred beneath vehicles or beyond the visible road; overhead arrows are
                        signs, not pavement markings. | result: consistent
Step 5  Rule            left_boundary: In China, a broken lane divider permits crossing to change lanes when
                        safe without interfering with other traffic.
Step 5  Rule            right_boundary: The solid roadway edge beside an emergency shoulder must not be
                        crossed for ordinary driving or overtaking.
Step 6  change_left     allowed (correct): The broken left lane divider permits a safe lane change.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid right edge bounds the emergency
                        shoulder and prohibits ordinary movement onto it.
Step 6  go_straight     allowed (contested, correct): No pavement arrow restricts continuing straight in this
                        through lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane, or change left across the broken divider only after checking
                        traffic, especially the truck alongside. Keep out of the emergency shoulder; the
                        overhead signs show a 100 km/h maximum and a 60 km/h minimum for your lane, subject to
                        conditions.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 867, 19.36 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153748406702000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An elevated urban roadway continues ahead, with no intersection or lane ending
                        visible. My car is in the rightmost lane; traffic and the cropped left side prevent a
                        reliable count of all same-direction lanes. (lanes None, mine None, insufficient)
Step 2  Left            Yellow elongated broken markings, with clear gaps, separate my lane from the same-
                        direction lane occupied by the white sedan; no curb is present.
                        yellow dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders a narrow paved strip beside the bridge barrier, with
                        separate yellow rectangular paint marks immediately inside the white line.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        symbol:other (partial): Repeated yellow elongated rectangular marks run along the
                        right margin of my lane, just inside the solid white edge line; their specific
                        guidance function is unclear.
Step 4  Cross-check     position: The lane line on the left confirms another same-direction lane, and the
                        roadway edge on the right confirms that my lane is rightmost. The total lane count and
                        therefore its numerical index remain uncertain. | roles: The left markings are visibly
                        yellow and broken despite separating same-direction traffic; their color has not been
                        inferred from their position. The solid white right line fits a roadway-edge role. |
                        markings: No readable movement arrows, words, transverse lines, or waiting areas are
                        visible. The yellow rectangles beside the right edge do not clearly indicate a
                        permitted turning movement. | unseen: No intersection layout, distant movement
                        restriction, or precise meaning for the yellow right-margin rectangles is assumed. |
                        result: consistent
Step 5  Rule            left_boundary: A broken lane-separating marking permits crossing to change lanes when
                        safe; the visible adjacent traffic is traveling in the same direction.
Step 5  Rule            right_boundary: The solid roadway-edge line and bridge barrier prohibit moving out of
                        the traffic lane onto or beyond the right-hand road margin.
Step 5  Rule            symbol:other: These incompletely identified margin markings do not establish
                        permission for any of the seven movements.
Step 6  change_left     allowed (correct): The broken left lane boundary permits crossing when the adjacent
                        lane is clear.
Step 6  change_right    prohibited (WRONG, label not_determined): The solid right roadway edge and bridge
                        barrier prohibit leaving the lane to the right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the boundaries govern lateral departures only, and no turning permission
                        has been inferred from the absence of arrows.
Advice                  Continue along this lane, keeping inside the solid white right edge. A left lane
                        change is permitted by the broken marking, but wait for a safe gap beside the white
                        sedan; no turning lane or stopping point is identifiable here.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['symbol:other'], missed []), actions False, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1183, 29.13 s

mapdr__EmergencyLane_9ee796aad4664b568e71213ba4ffa24c_1711153752673414000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues ahead, with no intersection or lane end
                        visible. My car is in the rightmost of three same-direction lanes, marked for buses.
                        (lanes 3, mine 3, full)
Step 2  Left            A single yellow broken line, with clearly visible long dashes and gaps, separates my
                        lane from a general traffic lane on the left; there is no curb at this boundary.
                        yellow dashed, curb no, special_lane_line, evidence full
Step 2  Right           A continuous white line borders the paved shoulder on the right, with yellow
                        rectangular dashes immediately alongside it on my lane's side; a barrier stands beyond
                        the shoulder rather than directly at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        text:bus (partial): White longitudinal Chinese bus-reservation lettering is visible in
                        my lane: 交、专、用 are readable, while the nearest portion of 公交专用 is obscured by the
                        hood.
Step 4  Cross-check     position: Two lanes lie to my left and a shoulder lies to my right, consistent with my
                        lane being third and rightmost. | roles: The yellow broken boundary and bus lettering
                        identify a special lane, not an opposing-traffic boundary; the continuous white line
                        borders the shoulder. | markings: The bus-reservation lettering agrees with the yellow
                        broken special-lane boundary and adjacent yellow rectangular markings; no directional
                        arrow or waiting area is visible. | unseen: The closest part of the bus lettering is
                        hidden by the hood, and no intersection-end markings or reservation hours can be read.
                        | result: consistent
Step 5  Rule            left_boundary: In China, a broken boundary permits leaving this special lane for the
                        adjacent general lane when safe; bus reservation does not prohibit an ordinary car
                        from exiting.
Step 5  Rule            right_boundary: The solid white roadway edge does not permit an ordinary discretionary
                        move onto the shoulder.
Step 5  Rule            text:bus: The bus lettering reserves this lane for authorized vehicles during
                        applicable operating periods, but does not itself select a straight or turning
                        movement.
Step 6  change_left     allowed (contested, correct): The broken special-lane boundary permits exiting into
                        the general lane when safe.
Step 6  change_right    prohibited (contested, label allowed): The solid white edge bounds a shoulder and
                        prohibits an ordinary discretionary move across it.
Step 6  go_straight     allowed (contested, correct): No visible directional arrow restricts continuing
                        straight; bus lettering does not govern this movement classification.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: permission to continue straight describes directional markings only, not
                        authorization for an ordinary car to remain in the reserved bus lane.
Advice                  As an ordinary car, leave the bus lane across the broken yellow line when a safe gap
                        opens, treating its reservation as active unless verified otherwise. Do not move onto
                        the right shoulder; no visible intersection markings establish a turning lane or
                        stopping point.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1156, 27.54 s

mapdr__MultiLane_450e61de53db4b5a846882736f260709_1710126711598183000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           The car is in a single motor-vehicle lane approaching an underpass, separated by a
                        concrete barrier from parallel traffic on the left. A paved strip used by scooters
                        runs along the wall to the right; no intersection or lane ending is visible. (lanes 1,
                        mine 1, full)
Step 2  Left            A continuous white solid line borders a narrow margin and a raised concrete barrier on
                        the left, with parallel traffic beyond the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white solid line separates the lane from a paved roadside strip occupied
                        by scooters, with a curb and wall at the far side of that strip.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The two edge boundaries enclose one motor-vehicle lane, so the car is in
                        lane 1 of 1 on this separated carriageway. | roles: Both white solid lines fit
                        roadway-edge roles; the left barrier physically separates the parallel roadway. |
                        markings: No readable arrows, words, symbols, transverse lines or waiting areas appear
                        in the visible lane. | unseen: The lane continues into the dark underpass; no markings
                        or intersection movements beyond the visible stretch are inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The raised concrete barrier forms a physical roadway edge that the car
                        must not cross.
Step 5  Rule            right_boundary: The solid white boundary separating the motor lane from the roadside
                        non-motorized strip must not be crossed for an ordinary lane change.
Step 6  change_left     prohibited (correct): The concrete barrier prohibits crossing the left boundary.
Step 6  change_right    prohibited (correct): The solid white edge separates the motor lane from the roadside
                        non-motorized strip and prohibits changing into it.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in this lane toward the underpass without crossing either boundary, and watch
                        for scooters on the right. Observe the overhead clearance signs and lane-control
                        signals before entering.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 795, 16.93 s

mapdr__MultiLane_78d5ff12c78548088813ddb4467d0945_1711414356487925000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           An urban roadway in China continues straight past roadside shelters and bicycle
                        parking, with a pedestrian crossing ahead. My car is in the right-hand of two visible
                        same-direction lanes; no intersection or lane ending is clearly visible. (lanes 2,
                        mine 2, full)
Step 2  Left            A continuous solid white line separates my lane from the paved lane on the left; there
                        is no curb along this divider.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A raised curb with a yellowish face borders my lane, with parked bicycles and scooters
                        on the pavement beyond; no separate painted roadway boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (full): A thin solid white transverse line crosses my lane immediately
                        before the pedestrian crossing.; line:crosswalk (full): White zebra-crossing bars
                        extend across my lane ahead.
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 2 agree with a lane divider on
                        the left and a curb at the right roadway edge. | roles: The solid white divider fits a
                        same-direction lane line; the raised curb forms the right edge without requiring a
                        separate painted edge line. | markings: The transverse stopping line and pedestrian
                        crossing are compatible with these boundaries. No directional arrow, movement-
                        prohibition marking, or waiting area is visible in my lane. | unseen: The partial
                        marking at the bottom left lies outside my lane and is not used to determine my
                        movements; no hidden arrow or distant intersection layout is inferred. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a solid white same-direction lane divider prohibits crossing
                        it to change lanes.
Step 5  Rule            right_boundary: The raised roadway curb is not a traversable lane boundary and
                        prohibits moving out of my lane onto the pavement.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when stopping is required, but
                        does not by itself impose an unconditional stop or select a permitted movement.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires approaching cautiously and yielding
                        or stopping for pedestrians as required, without selecting a lane movement.
Step 6  change_left     prohibited (correct): The solid white lane divider prohibits crossing to the lane on
                        the left.
Step 6  change_right    prohibited (correct): The raised curb prohibits moving onto the pavement on the right.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and no lane
                        ending is visible.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight within this lane without crossing the solid left divider or the
                        right curb. Slow for the pedestrian crossing and stop before the transverse line if
                        required to yield; the visible markings do not establish a turning lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 6396, out 1098, 20.85 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261263869749000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           The car is in the left lane of a two-lane branch alongside a busier main carriageway,
                        with a painted separator developing on the left. Traffic continues ahead; no
                        intersection or lane end is visible. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line borders the lane on the left and leads into a narrow
                        diagonally hatched separator, with main-carriageway traffic beyond; no raised curb
                        forms this boundary.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           Broken white paint, with a visible dash and gap, separates this lane from another
                        traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes on this branch and position 1 agree with a left roadway edge and a
                        lane divider on the right; lanes across the painted separator belong to the adjacent
                        main carriageway. | roles: The continuous white line bordering the separator fits an
                        edge line, and the broken white right boundary fits a same-direction lane divider. |
                        markings: No guidance marking is visible within the ego lane; the diagonal hatching
                        lies outside its left boundary. | unseen: No hidden arrows or intersection markings
                        have been inferred; vehicles obscure some pavement farther ahead. | result: consistent
Step 5  Rule            left_boundary: In China, the solid white boundary of the channelized roadway
                        separation must not be crossed to enter the adjacent carriageway.
Step 5  Rule            right_boundary: A broken white same-direction lane divider may be crossed for a lane
                        change when safe and without impeding other traffic.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white boundary adjoining the painted
                        separator prohibits crossing left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change right.
Step 6  go_straight     allowed (contested, correct): No visible arrow restricts continuing straight along
                        this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue along this branch without crossing the solid left boundary or painted
                        separator. A right lane change is permitted when safe; leave space behind the vehicle
                        ahead and reassess any markings revealed beyond it.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 881, 18.0 s

mapdr__MultiLane_93e985a80fd04226af8647ea2004d077_1711261270536469000 | lane | Test A | gpt-6.1-sol
---------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, tree-lined urban road continues straight, with no intersection or lane
                        ending visible. My car is in the leftmost of two same-direction motor-vehicle lanes; a
                        separate roadside strip lies beyond the solid line farther right. (lanes 2, mine 1,
                        full)
Step 2  Left            A single solid white line runs beside a raised curb and planted median on the left.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another motor-vehicle lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median-side left edge and the adjacent lane on the right agree with
                        being lane 1 of 2. | roles: The solid white line beside the median curb fits a roadway
                        edge; the broken white line fits a same-direction lane divider. | markings: No
                        guidance markings are visible in my lane, so there is no conflict with the boundaries.
                        | unseen: No intersection layout or markings hidden beneath vehicles are inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The median curb and solid roadway edge prohibit leaving the lane to the
                        left.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing right when
                        safe and without interfering with other traffic.
Step 6  change_left     prohibited (correct): The solid median-side edge and raised curb prohibit crossing
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight along this lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken line after checking
                        for traffic. Do not cross the median-side boundary; no turn guidance or stopping point
                        is visible ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 763, 15.06 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069393822514000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           The car is within a broad urban signal-controlled intersection, following the silver
                        car toward the road ahead. The foreground is unmarked intersection pavement, so lanes
                        in this direction cannot be counted reliably at the car's position. (lanes None, mine
                        None, insufficient)
Step 2  Left            No painted line or physical boundary is visible immediately to the left of the car's
                        path across the intersection; opposing vehicles are farther left ahead.
                        none none, curb no, unknown, evidence full
Step 2  Right           No painted line or physical boundary is visible immediately to the right of the car's
                        path across the intersection; the taxi and roadside curb are farther right ahead.
                        none none, curb no, unknown, evidence full
Step 3  Markings        line:crosswalk (partial): White zebra-crossing stripes extend across the path ahead,
                        with portions obscured by the silver car and other vehicles.
Step 4  Cross-check     position: The unmarked intersection does not establish a lane count or lane index; the
                        distant roadway lanes cannot be treated as boundaries at the car's current position. |
                        roles: Neither side has a visible immediate boundary, so no lane-line, center-line or
                        edge-line role is assigned. | markings: The crosswalk is consistent with the
                        intersection; no lane-use arrow, word or waiting area is visible in the car's path. |
                        unseen: No hidden lane-use arrow or distant boundary pattern has been inferred;
                        vehicles obscure portions of the crosswalk. | result: consistent
Step 5  Rule            left_boundary: The absence of a visible left boundary supplies no marking-based
                        permission or prohibition for changing left.
Step 5  Rule            right_boundary: The absence of a visible right boundary supplies no marking-based
                        permission or prohibition for changing right.
Step 5  Rule            line:crosswalk: In China, drivers approaching a crosswalk must slow down and stop for
                        pedestrians crossing; the crosswalk does not itself designate permitted lane
                        movements.
Step 6  change_left     not_applicable: No painted boundary or curb governs this action in the visible
                        intersection.
Step 6  change_right    not_applicable: No painted boundary or curb governs this action in the visible
                        intersection.
Step 6  go_straight     allowed (contested, correct): No visible lane-use arrow restricts continuing straight
                        along the path ahead.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the unmarked sides do not establish lane-change permissions, and the
                        crosswalk is not used to decide directional movements.
Advice                  Continue predictably toward the receiving lane behind the silver car, subject to the
                        traffic signals, which appear green. Slow for the crosswalk and stop for pedestrians
                        crossing; no visible lane-use marking establishes a turning lane here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions None, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1049, 22.27 s

mapdr__Non_MotorizedLane_9f3c0c0a6ff4481488b410e657356dff_1711069399955886000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban road in China has two motor-vehicle lanes in this direction, separated from
                        opposing traffic by a low median fence. My car is in the leftmost lane; the road
                        continues toward a distant junction whose lane-end markings are not clearly visible.
                        (lanes 2, mine 1, full)
Step 2  Left            A continuous yellow line runs beside a raised median base and white metal fence, with
                        opposing traffic beyond.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           White broken lane-line segments with clear gaps separate my lane from the same-
                        direction lane occupied by the dark sedan; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        symbol:other (partial): A near group of worn, pale transverse rectangular paint blocks
                        spans my lane as a speed-reduction marking.; symbol:other (partial): Another group of
                        pale transverse rectangular paint blocks crosses my lane farther ahead.
Step 4  Cross-check     position: The median on the left and one same-direction lane on the right agree with
                        my lane being lane 1 of 2. | roles: The yellow solid median-side line fits a center
                        boundary; the white broken right boundary fits a same-direction lane divider. |
                        markings: The transverse speed-reduction markings do not prescribe a direction and do
                        not conflict with either boundary. | unseen: No lane-use arrow, stop line, or waiting
                        area can be identified; vehicles and distance obscure the lane's eventual junction
                        approach. | result: consistent
Step 5  Rule            left_boundary: In China, the solid yellow center boundary and physical median prohibit
                        crossing left into opposing traffic.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes when
                        it is safe and without obstructing other traffic.
Step 5  Rule            symbol:other: The near transverse speed-reduction marking calls for slowing down but
                        does not determine lane changes or junction movements.
Step 5  Rule            symbol:other: The farther transverse speed-reduction marking calls for slowing down
                        but does not determine lane changes or junction movements.
Step 6  change_left     prohibited (correct): The solid yellow center boundary and physical median prohibit
                        crossing left.
Step 6  change_right    allowed (correct): The broken white divider permits a safe lane change, although the
                        adjacent sedan currently occupies the space.
Step 6  go_straight     allowed (contested, label not_determined): No visible directional marking restricts
                        continuing straight along this lane.
Step 6  turn_left       not_determined: The eventual junction approach is obscured, so any lane-use marking
                        deciding this movement cannot be read.
Step 6  turn_right      not_determined: The eventual junction approach is obscured, so any lane-use marking
                        deciding this movement cannot be read.
Step 6  u_turn          not_determined: The eventual junction approach is obscured, so any lane-use marking
                        deciding this movement cannot be read.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary permissions govern only lane changes, continuing straight is
                        unrestricted by visible markings, and obscured junction movements remain undecided.
Advice                  Continue in this lane at a reduced speed over the transverse markings; do not cross
                        the median, and wait for a safe gap before changing right. Reassess junction arrows
                        and signals as they become visible, and note the roadside no-U-turn sign ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1112, 21.8 s

mapdr__SpeedLimitedLane_28031b5893a24e9f81f64237ed68d8bf_1709684738352944000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A single-lane ramp runs between concrete barriers and bends gently right ahead. My car
                        is in the ramp's only lane; no intersection or lane ending is visible. (lanes 1, mine
                        1, full)
Step 2  Left            A continuous solid white line follows the left side of the lane, with a narrow paved
                        margin and a concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line follows the right side of the lane, with a paved
                        shoulder and a concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two roadway edge lines and barriers agree with one lane and ego lane index
                        1; the pavement beyond the right edge line is a shoulder, not another travel lane. |
                        roles: Both white solid lines fit roadway edge lines on this separated ramp. |
                        markings: No readable arrows, words, symbols or waiting areas are visible in my lane.
                        | unseen: The lane's eventual end is outside view. Thin transverse bands ahead cannot
                        confidently be identified as painted guidance rather than pavement joints and are not
                        classified as markings. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge line does not permit an ordinary lane change
                        onto the margin, and the concrete barrier cannot be crossed.
Step 5  Rule            right_boundary: The solid roadway edge line does not permit an ordinary lane change
                        onto the shoulder, which is not a normal travel lane.
Step 6  change_left     prohibited (correct): The solid left edge line and concrete barrier prohibit leaving
                        the lane to the left.
Step 6  change_right    prohibited (correct): The solid right edge line separates the lane from a shoulder,
                        not an available travel lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing along
                        the ramp, including following its bend.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid white edge lines and follow the ramp's rightward bend; do not
                        use the shoulder as another lane. Observe the posted 40 km/h limit for this ramp.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 854, 17.12 s

mapdr__SpeedLimitedLane_63bab9ca228d43e696bb51f0409b6cc8_1710727788941398000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided highway continues straight beneath an overpass, with no intersection or lane
                        ending visible. My car is in the leftmost of two lanes in this direction. (lanes 2,
                        mine 1, full)
Step 2  Left            A continuous yellow solid line borders the left side, with a narrow paved margin and a
                        median guardrail beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction traffic lane on the right; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my lane being lane 1
                        of 2. | roles: The solid yellow line beside the median is a left edge line, not a
                        center line between adjacent opposing lanes; the broken white line separates same-
                        direction lanes. | markings: No arrows, words, symbols, transverse lines or waiting
                        areas are visible in my lane. | unseen: No intersection layout or markings beyond the
                        visible road have been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid left roadway edge and median barrier prohibit leaving the
                        lane to the left here.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe.
Step 6  change_left     prohibited (correct): The solid left edge and median barrier prohibit crossing to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (contested, correct): No arrow or lane-ending marking restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken white line after
                        checking traffic and blind spots. Do not cross the left edge toward the median
                        barrier.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 781, 17.72 s

mapdr__SpeedLimitedLane_92c36838dd5a494a9d590f908034be91_1709945751995536000 | lane | Test A | gpt-6.1-sol
----------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided expressway in China continues straight, with three travel lanes in this
                        direction and an emergency shoulder on the right. My car is in the leftmost travel
                        lane; no intersection, ramp or lane ending is visible. (lanes 3, mine 1, full)
Step 2  Left            A solid white line runs along the left edge of my lane beside a narrow median strip
                        and metal guardrail, with opposing traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken paint, with clearly visible long dashes and gaps, separates my lane from
                        the next same-direction travel lane; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three travel lanes and position 1 agree with a median-side edge on my left
                        and a same-direction lane divider on my right; the emergency shoulder is not counted
                        as a travel lane. | roles: The solid white median-side edge line and broken white
                        same-direction lane divider fit their assigned roles. | markings: No arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane; nothing conflicts
                        with its boundaries. | unseen: No hidden lane-use marking or intersection movement has
                        been inferred; overhead signs are context, not pavement markings. | result: consistent
Step 5  Rule            left_boundary: The solid expressway edge line and median barrier prohibit leaving my
                        lane across the left boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing into the
                        adjacent travel lane when safe.
Step 6  change_left     prohibited (correct): The solid median-side edge and guardrail prohibit crossing the
                        left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent travel lane.
Step 6  go_straight     allowed (contested, correct): No arrow restricts continuing straight, and the lane
                        visibly continues.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change right across the broken line only after
                        checking traffic; do not cross the left edge toward the median. Follow the overhead
                        lane-specific vehicle and speed restrictions, and keep out of the emergency shoulder
                        during normal driving.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 822, 16.82 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450109557000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A multilane urban road in China approaches a signal-controlled intersection with a
                        pedestrian crossing. My car is in the middle of three same-direction motor-vehicle
                        lanes. (lanes 3, mine 2, full)
Step 2  Left            A solid white line separates my lane from the same-direction lane on the left; short
                        white rectangular teeth lie along its far side, and there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the same-direction lane containing the
                        silver car on the right, with no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white arrow in my lane has a single head pointing straight
                        ahead; its lower shaft is partly hidden by the hood.; line:stop_line (full): A
                        transverse white stop line crosses my lane immediately before the pedestrian
                        crossing.; line:crosswalk (full): Broad white pedestrian-crossing stripes extend
                        across my lane beyond the stop line.
Step 4  Cross-check     position: One same-direction lane lies on each side, consistent with three lanes and
                        my lane being second from the left. | roles: Both white solid boundaries fit same-
                        direction lane separators on an intersection approach. | markings: The visible single
                        straight arrow agrees with a straight-through approach lane; neither boundary
                        contradicts it. | unseen: The arrow shaft is partly hidden, but its straight head and
                        absence of visible branches are clear; no hidden wording or waiting area is inferred.
                        | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        into the lane on the left.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        into the lane on the right.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal or
                        traffic control, but does not itself impose an unconditional stop.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires yielding to pedestrians as applicable
                        and keeping the crossing unobstructed.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The straight-only arrow permits straight travel.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane for straight travel and do not cross either solid separator; turns
                        require an appropriate lane selected before the solid-line approach. Obey the traffic
                        signal, stop before the stop line when required, and yield to pedestrians at the
                        crossing.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1105, 20.09 s

mapdr__VariableDirectionLane_6b9fe861b6c9413cbaabfb6f9af02b89_1711423450909576000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A broad urban road in China approaches a signal-controlled intersection with a zebra
                        crossing. My car is in the middle of three visible approach lanes, immediately before
                        the stop line. (lanes 3, mine 2, full)
Step 2  Left            A solid white line runs along the left side to the stop line, with short oblique white
                        strokes on its far side; another traffic lane lies beyond, with no curb at this
                        boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along the right side to the stop line, with another traffic
                        lane beyond and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A broad white transverse stop line spans my lane immediately
                        ahead.; line:crosswalk (full): White zebra-crossing stripes cross the roadway
                        immediately beyond the stop line.
Step 4  Cross-check     position: Lane lines on both sides agree with my lane being the middle of three same-
                        direction lanes. | roles: The white solid boundaries fit same-direction approach-lane
                        dividers. | markings: The stop line and crossing agree with an intersection approach;
                        no directional arrow, word, or waiting area is visible in my lane. | unseen: The hood
                        hides the nearest pavement, and no directional marking is inferred from that hidden
                        area. The oblique strokes lie beyond the left boundary, not inside my lane. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a solid white same-direction lane divider prohibits crossing
                        it to change lanes in this stretch.
Step 5  Rule            right_boundary: In China, a solid white same-direction lane divider prohibits crossing
                        it to change lanes in this stretch.
Step 5  Rule            line:stop_line: The stop line identifies where to stop when required by the signal or
                        traffic control; it does not itself require an unconditional stop or select a
                        movement.
Step 5  Rule            line:crosswalk: The zebra crossing requires attention and yielding to pedestrians as
                        applicable, but does not determine lane-use movements.
Step 6  change_left     prohibited (correct): The solid white left lane divider prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane divider prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (contested, correct): No visible directional marking restricts continuing
                        straight along my lane.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the solid boundaries restrict lane changes, while the stop line and
                        crossing do not independently prohibit or require a stop for any movement.
Advice                  Stay between the solid white lines; do not change lanes in this approach stretch.
                        Continue straight only as traffic control and pedestrian safety permit, stopping
                        before the stop line when required; the visible markings do not establish turn
                        permissions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1245, 27.2 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187253488645000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China has three lanes in this direction, with an intersection
                        approach visible in the distance. My car is in the middle lane; the distant lane end
                        is not clearly resolved. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with clearly visible long dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and gaps visible, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 2 agree with same-direction lane lines on both
                        sides. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No guidance marking is readable within my lane; the arrows on
                        the roadside sign are not pavement markings. | unseen: No distant arrow, stop line, or
                        waiting area is inferred; details at the distant lane end cannot be resolved. |
                        result: consistent
Step 5  Rule            left_boundary: In China, an ordinary white broken lane divider may be crossed to
                        change lanes when safe and without obstructing traffic.
Step 5  Rule            right_boundary: In China, an ordinary white broken lane divider may be crossed to
                        change lanes when safe and without obstructing traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible marking restricts continuing straight along
                        my lane.
Step 6  turn_left       not_determined: The distant lane-end markings that would determine this movement are
                        not readable.
Step 6  turn_right      not_determined: The distant lane-end markings that would determine this movement are
                        not readable.
Step 6  u_turn          not_determined: The distant lane-end markings that would determine this movement are
                        not readable.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: broken boundaries permit lane changes, continuing straight is unrestricted
                        by visible markings, and distant intersection movements remain undecided rather than
                        inferred from the sign.
Advice                  Continue in the middle lane for now; either broken divider may be crossed after
                        checking traffic. Read the approaching pavement arrows, lane-use signs and signals
                        before selecting a turning lane, and stop before any applicable stop line when
                        required.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 862, 15.7 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187254288664000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China approaches a distant intersection. My car is in the
                        middle of three same-direction lanes, with a median barrier to the far left and a
                        landscaped curb to the far right. (lanes 3, mine 2, full)
Step 2  Left            A single white broken line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with visible long dashes and gaps, separates my lane from
                        another same-direction lane; the roadside curb is beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A small white forward-pointing arrow is visible farther
                        ahead in my lane, though distance limits its detail.
Step 4  Cross-check     position: Two lane-line boundaries agree with my position in the middle of three same-
                        direction lanes. | roles: White broken lines fit the role of separators between same-
                        direction lanes. | markings: The visible straight arrow agrees with a continuing
                        through lane; the larger painted inscriptions on either side are outside my lane. |
                        unseen: The distant intersection approach and lane endpoint are not fully readable; no
                        stop line, additional arrow head, or waiting area has been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator may be crossed to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator may be crossed to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from that lane.
Step 6  change_left     allowed (correct): The visible broken white left lane line permits crossing when safe.
Step 6  change_right    allowed (correct): The visible broken white right lane line permits crossing when
                        safe.
Step 6  go_straight     allowed (contested, correct): The visible forward arrow permits straight travel.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the broken boundaries govern lane changes, the identifiable straight arrow
                        governs intersection movements, and no waiting-area permission is inferred.
Advice                  Stay in this lane to proceed straight, subject to the signals ahead. For a turn, move
                        safely across a broken line into an appropriately marked lane before any solid
                        approach markings, and check the adjacent lanes' posted variable-lane instructions.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 999, 20.07 s

mapdr__VariableDirectionLane_8c224bff3a284f00be33f7f361c9060c_1712187255355347000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China approaches an intersection. My car is in the third of
                        four lanes in this direction, with a median barrier to the left and a landscaped
                        roadside to the right. (lanes 4, mine 3, full)
Step 2  Left            A white continuous line borders my lane on the left in the foreground, with repeated
                        short rectangular projections on its far side; another same-direction lane lies
                        beyond, and there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white continuous line borders my lane on the right in the foreground, with repeated
                        short rectangular projections on its far side; another same-direction lane lies
                        between this line and the roadside curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white forward-pointing arrow is visible ahead in my lane,
                        with a straight shaft and no visible turning branch.
Step 4  Cross-check     position: Four lanes and ego position three agree with same-direction lane boundaries
                        on both sides: two lanes lie to the left and one to the right. | roles: The white
                        solid boundaries separate same-direction lanes; neither is the median boundary or the
                        roadside edge. | markings: The straight arrow agrees with a through lane. Large
                        painted characters and the rectangular boundary projections are outside my lane, not
                        additional movement instructions within it. | unseen: The distant intersection surface
                        is not clear enough to identify a stop line or crosswalk; neither is asserted. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a solid white same-direction lane divider prohibits crossing
                        it to change lanes in the visible solid-lined stretch.
Step 5  Rule            right_boundary: In China, a solid white same-direction lane divider prohibits crossing
                        it to change lanes in the visible solid-lined stretch.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 6  change_left     prohibited (contested, label allowed): The solid white left lane divider prohibits
                        crossing to the lane on the left.
Step 6  change_right    prohibited (contested, label allowed): The solid white right lane divider prohibits
                        crossing to the lane on the right.
Step 6  go_straight     allowed (contested, correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, and do not cross either solid divider. For a
                        turn, select an appropriately marked lane only where lane changing is permitted; obey
                        the intersection signals and stop before any applicable stop line.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions None, unsafe [], citation None, contradictions
                        []
Tokens                  in 6396, out 1260, 30.85 s

mapdr__VariableDirectionLane_c002a63d8292458fb36fb00aca153f97_1709777167709286000 | lane | Test A | gpt-6.1-sol
--------------------------------------------------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches an intersection farther ahead. My car is in
                        the third of four same-direction lanes, with one lane to its right. (lanes 4, mine 3,
                        full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from the
                        rightmost same-direction lane; the roadside curb is beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has a single head pointing straight
                        ahead.
Step 4  Cross-check     position: Lane 3 of 4 has another same-direction lane on each side, consistent with
                        both boundaries being lane lines. | roles: Both white broken boundaries fit separation
                        of same-direction traffic lanes. | markings: The straight-only arrow agrees with a
                        through lane; the straight-and-right arrow belongs to the adjacent right lane, not
                        mine. | unseen: No distant stop line, crosswalk, or waiting area is identifiable; none
                        has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane line permits crossing to change lanes
                        when safe and without obstructing traffic.
Step 5  Rule            right_boundary: In China, a broken white lane line permits crossing to change lanes
                        when safe and without obstructing traffic.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        prohibits turning left, turning right, or making a U-turn from this lane at the
                        intersection.
Step 6  change_left     allowed (correct): The broken white left lane boundary permits a safe lane change.
Step 6  change_right    allowed (correct): The broken white right lane boundary permits a safe lane change.
Step 6  go_straight     allowed (correct): The straight arrow expressly permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn from this
                        lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn from this
                        lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane, following the intersection signals. For a turn, move
                        safely across the broken line into an appropriately marked lane before the
                        intersection; the adjacent right lane visibly permits a right turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 911, 15.05 s

mapdr__VehicleLane_1b2c4e0578804ec38753f760c633b6ab_1710549573412872000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban arterial in China continues straight beneath overhead signals, with a
                        pedestrian bridge farther ahead. My car is in the second lane from the left; three
                        general-traffic lanes and a farther-right bus lane are visible, although the bus
                        obscures the outer road edge. (lanes 4, mine 2, partial)
Step 2  Left            White broken paint, with distinct dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           White broken paint, with visible dashes and gaps, separates my lane from the general-
                        traffic lane containing the taxi on the right; the bus and yellow marking are farther
                        right, beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The second-lane position agrees with an ordinary lane line on each side: one
                        same-direction lane lies to the left and another lies immediately to the right. A
                        farther-right bus lane is visible, but its outer extent is obscured. | roles: Both
                        boundaries are white broken lines, consistent with separation of same-direction
                        general-traffic lanes. | markings: No readable arrow, word, symbol, transverse line,
                        or waiting area is visible in my lane; markings farther right belong to other lanes. |
                        unseen: No unseen lane-use arrow or stop line is inferred. The far-right edge and
                        distant intersection markings are obscured or too distant to resolve. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing into the
                        adjacent same-direction lane when safe and without obstructing traffic.
Step 5  Rule            right_boundary: The broken white divider permits a safe change into the immediately
                        adjacent general-traffic lane; it does not authorize continuing across into the
                        farther-right reserved bus lane.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (WRONG, label not_determined): The broken white lane divider permits a safe
                        lane change into the immediately adjacent general-traffic lane.
Step 6  go_straight     allowed (contested, correct): No visible marking in my lane restricts continuing
                        straight.
Step 6  turn_left       not_applicable: No visible marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No visible marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No visible marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent general-traffic lane may be entered
                        across its broken white divider when safe, but avoid the farther-right bus lane. The
                        visible through signal is green; check traffic and upcoming lane arrows before
                        selecting any turning movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 1144, 28.61 s

mapdr__VehicleLane_3153623906844b34850b0d88037cd764_1711423473888839000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           An undivided urban road curves gently left, with a junction visible farther ahead. My
                        car is in the leftmost of two same-direction motor-vehicle lanes. (lanes 2, mine 1,
                        full)
Step 2  Left            A single continuous yellow line curves along my left, with opposing traffic lanes
                        beyond it and no curb at the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           White elongated dashes separated by clear gaps form my right boundary, with another
                        same-direction lane beyond and no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on my left and white lane divider on my right agree
                        with being lane 1 of 2 in my direction. | roles: The solid yellow line separates
                        opposing directions; the broken white line separates same-direction lanes. | markings:
                        No arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No distant or unreadable lane-use marking has been inferred; the far junction
                        details are not resolved. | result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing into the
                        opposing side for a lane change or overtaking.
Step 5  Rule            right_boundary: A broken white same-direction lane divider may be crossed to change
                        lanes when safe without interfering with other traffic.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent same-direction lane.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing along
                        my lane.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action; the center line governs crossing the
                        boundary, not an unseen junction movement.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within your lane around the curve; do not cross the solid yellow center line.
                        A right lane change is permitted only when safe, watching for the scooter; confirm
                        junction arrows, signs and signals before choosing a turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 816, 16.27 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391616984525000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A divided, elevated expressway in China continues straight ahead, with no visible
                        intersection, ramp or lane ending. There are five through lanes in this direction; my
                        car is in the second lane from the left, with an emergency shoulder farther right.
                        (lanes 5, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        through lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        through lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): Large white Chinese road lettering is visible at the bottom of
                        my lane, partly obscured by the hood; the complete wording cannot be read.
Step 4  Cross-check     position: The second of five through lanes has another same-direction lane on both
                        sides, agreeing with both boundaries being lane lines. | roles: Both white broken
                        boundaries fit ordinary same-direction lane dividers. | markings: The partially
                        visible road lettering does not establish any directional arrow or conflict with the
                        lane boundaries. | unseen: The obscured lettering has not been reconstructed; no
                        arrow, stop line or waiting area is claimed. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to the adjacent
                        lane when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to the adjacent
                        lane when safe and without obstructing other traffic.
Step 5  Rule            text:other: The partially visible ordinary road lettering does not independently
                        authorize or prohibit any of the seven assessed actions.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible directional arrow restricts continuing
                        straight, and the lane continues ahead.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; either adjacent lane may be entered across its broken
                        divider after checking traffic. Follow the overhead lane and speed signs; no
                        intersection turning opportunity or stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 900, 14.94 s

mapdr__VehicleLane_52cd1b9fb40d468e90e5a0b8ae9f57d7_1710391619384567000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           An elevated, divided multilane road in China continues straight toward overhead signs,
                        with no visible intersection or lane ending. My car is in the second of four lanes in
                        its direction. (lanes 4, mine 2, full)
Step 2  Left            A single white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; no curb borders my lane here.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the right; no curb borders my lane here.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 4 has a same-direction lane on its left and two on its right,
                        consistent with lane-line boundaries on both sides. | roles: Both white broken
                        boundaries fit ordinary same-direction lane dividers. | markings: No lane-use arrows,
                        words, symbols, or waiting areas are visible in my lane; nothing conflicts with the
                        boundary observations. | unseen: No distant unreadable guidance is inferred. The
                        transverse bridge joint is not treated as a painted stop line. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to the adjacent
                        ordinary lane when safe and without obstructing traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to the adjacent
                        ordinary lane when safe and without obstructing traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     allowed (contested, correct): No visible lane-use marking restricts continuing
                        straight, and my lane continues ahead.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in your present lane; either adjacent lane may be entered across the
                        broken divider after checking traffic and signaling. Read the overhead signs as you
                        approach; no turning lane or stopping requirement is established by the visible
                        pavement markings.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 846, 16.07 s

mapdr__VehicleLane_99899d036da944ceb41404c3ec3c9fa9_1710733702898064000 | lane | Test A | gpt-6.1-sol
-----------------------------------------------------------------------------------------------------
Step 1  Scene           A divided urban road in China has three lanes in this direction and a distant
                        signalized intersection ahead. My car is in the middle lane behind a dark car. (lanes
                        3, mine 2, full)
Step 2  Left            A white broken line, with visible dashes and gaps and no curb, separates my lane from
                        the lane occupied by the taxi.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible dashes and gaps and no curb, separates my lane from
                        the rightmost lane occupied by a scooter.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white single-headed straight-ahead arrow is painted in my
                        lane immediately behind the dark car; farther pavement is partly obscured by that car
                        and distance.
Step 4  Cross-check     position: Three lanes with my lane second from the left agree with a same-direction
                        lane line on each side. | roles: Both white broken boundaries fit ordinary same-
                        direction lane dividers. | markings: The straight-only arrow is compatible with both
                        lane boundaries; arrows in neighboring lanes and on the overhead sign are not pavement
                        markings in my lane. | unseen: No distant stop line or additional marking is inferred
                        from the obscured pavement. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to the adjacent
                        same-direction lane when safe without interfering with traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to the adjacent
                        same-direction lane when safe without interfering with traffic.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight from this
                        lane and excludes left turns, right turns and U-turns from it.
Step 6  change_left     allowed (correct): The broken white left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a safe lane change.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight and obey the signals ahead, stopping before the
                        stop line if required once it becomes visible. If intending to turn, first find an
                        appropriately marked lane; either visible broken divider permits a safe lane change,
                        but check carefully for the taxi and scooter.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 6396, out 867, 14.9 s
```
