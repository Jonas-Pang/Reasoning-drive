# Reasoning of lane run 20261105_074605_laneA_CN

```text
culane_test__d100_05251207_0380_01410 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead; no intersection or lane
                        ending is clearly visible. My car is in the rightmost of three same-direction motor-
                        vehicle lanes, beside a roadside strip used by a cyclist. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with clearly visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved roadside
                        strip and a cyclist beyond it; the raised roadside curb lies farther right, not at
                        this line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego position 3 agree with a lane divider on
                        the left and a roadway edge line on the right. | roles: The broken white left line
                        fits a same-direction lane divider, and the solid white right line fits the edge
                        beside the roadside strip. | markings: No arrows, words, symbols, transverse lines, or
                        marked waiting areas are visible in my lane. | unseen: No intersection layout or
                        distant lane-use marking is inferred from the small, distant road features. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, the solid white roadway edge line prohibits crossing into
                        the roadside strip during ordinary driving.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits crossing into the roadside
                        strip.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay inside the solid right edge line and leave room for the cyclist beyond it; change
                        left only after checking that the adjacent lane is clear. No visible turn guidance or
                        stop line establishes where to turn or stop, so reassess as the next junction comes
                        into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 880, 16.6 s

culane_test__d100_05251207_0380_02130 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China with three lanes in this direction continues ahead; no
                        intersection or lane ending is visible. My car is in the middle lane. (lanes 3, mine
                        2, full)
Step 2  Left            A white broken line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; the roadside fence is beyond that lane, not on my
                        lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego position 2 agree with a same-direction
                        lane line on each side. | roles: Both white broken boundaries fit ordinary same-
                        direction lane separators. | markings: No arrows, words, symbols, transverse lines or
                        waiting areas are visible in my lane. | unseen: No markings or intersection geometry
                        beyond the visible stretch have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane separator permits crossing to change
                        lanes when safe without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane separator permits crossing to change
                        lanes when safe without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken left lane separator permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane separator permits a safe lane change.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You may remain in the middle lane or cross either broken separator when safe after
                        checking traffic and signaling. No intersection movement guidance or stopping line is
                        visible; follow the markings and signs that appear farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 750, 10.77 s

culane_test__d100_05251207_0380_02190 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China has three lanes in this direction, with no intersection
                        or lane ending clearly visible ahead. My car is in the middle lane. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 2 agree with a lane line and another
                        same-direction lane on each side. | roles: Both white broken boundaries fit same-
                        direction lane-divider roles. | markings: No arrows, words, symbols, transverse lines
                        or waiting areas are visible in my lane. | unseen: No unseen markings or intersection
                        layout have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken left lane divider permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane divider permits a safe lane change.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the broken boundaries permit lane changes, while no visible marking
                        governs intersection movements or entry into a waiting area.
Advice                  You may remain in the middle lane or cross either broken divider when safe, checking
                        nearby vehicles and smaller road users first. No visible arrows establish turn-lane
                        assignments or require a lane change.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 770, 10.74 s

culane_test__d100_05251207_0380_02400 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight ahead, with no intersection or lane
                        ending visible. My car is in the middle of three same-direction lanes. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from the lane
                        occupied by the white van; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from the right-
                        hand lane occupied by the small delivery vehicle; the roadside curb is farther right,
                        not on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car being in lane 2 of 3. | roles:
                        Both white broken boundaries fit same-direction lane-divider roles. | markings: No
                        guidance arrows, words, symbols, transverse lines or waiting areas are visible in my
                        lane. | unseen: No markings or intersection geometry have been inferred beyond the
                        visible road. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing into the
                        adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing into the
                        adjacent same-direction lane when safe.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may remain in the middle lane or cross either broken divider after checking
                        traffic, especially the van to the left and delivery vehicle to the right. No visible
                        marking establishes turn permissions or a stopping point; follow the markings and
                        controls encountered farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 806, 14.42 s

culane_test__d100_05251207_0380_03270 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban road in China continues straight ahead; no intersection or lane
                        ending is visible. My car is in the rightmost of three visible same-direction motor-
                        vehicle lanes. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved roadside
                        strip beyond it and a raised sidewalk curb farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 3 agree with a lane divider on my
                        left and a roadway edge line on my right. | roles: The broken white divider fits a
                        same-direction lane line; the solid white line beside the roadside strip fits an edge
                        line. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No movement instruction is inferred from the overhead
                        signs or from the distant road, and the roadside strip is not assumed to be another
                        motor-vehicle lane. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing traffic.
Step 5  Rule            right_boundary: A solid white roadway edge line restricts ordinary crossing onto the
                        roadside strip.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid white edge line restricts crossing onto the roadside
                        strip.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Keep within the right edge line; a left lane change is permitted only after checking
                        traffic and clearance. No visible pavement arrows assign movements at the next
                        intersection, so follow upcoming lane guidance rather than treating this lane as a
                        designated turning lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 856, 14.26 s

culane_test__d100_05251222_0385_01140 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues ahead beside an elevated structure, with no
                        intersection or lane ending visible. My car is in the leftmost of three same-direction
                        lanes. (lanes 3, mine 1, full)
Step 2  Left            A solid white line follows the left edge of my lane beside a raised curb and a
                        guardrail, with vegetation beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken paint, with multiple dashes and intervening gaps visible, separates my
                        lane from another same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left edge and right lane divider agree with my car occupying lane 1 of
                        three same-direction lanes. | roles: The solid white line beside the curb fits a
                        roadway edge, and the dashed white line fits a same-direction lane divider. |
                        markings: No arrows, words, symbols, transverse lines, or waiting areas are visible in
                        my lane. | unseen: No intersection layout or guidance beyond the visible road stretch
                        has been inferred. | result: consistent
Step 5  Rule            left_boundary: The raised curb and guardrail form a physical roadway edge that my car
                        must not cross.
Step 5  Rule            right_boundary: In China, a dashed white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 6  change_left     prohibited (correct): The raised curb and guardrail prohibit leaving the lane across
                        its left edge.
Step 6  change_right    allowed (correct): The dashed white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: only boundary-crossing actions are governed here, and the absence of
                        movement markings does not establish permission for intersection movements.
Advice                  Remain within the left roadway edge; you may change into the lane on your right after
                        checking traffic and blind spots. No visible arrows or stop line establish turn-lane
                        use or a stopping point ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 840, 13.81 s

culane_test__d100_05251222_0385_01710 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road in China runs beside an elevated structure toward an
                        intersection. My car is in the second lane from the left, behind a silver sedan.
                        (lanes 4, mine 2, full)
Step 2  Left            A continuous white solid line separates my lane from another same-direction lane on
                        the left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from the same-direction lane occupied
                        by the dark sedan on the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white longitudinal arrow shaft is visible behind the
                        silver sedan, but its head and any possible branches are obscured; a straight
                        indication cannot be confirmed completely.; line:crosswalk (partial): White
                        pedestrian-crossing stripes are visible across the approach ahead, but the portion
                        directly in my lane is partly obscured by the silver sedan.
Step 4  Cross-check     position: The second of four same-direction lanes has another lane on each side,
                        consistent with both boundaries being lane lines. | roles: White solid lines fit same-
                        direction lane separators that prohibit crossing on this approach. | markings: The
                        partially obscured arrow cannot establish the complete permitted movement set; the
                        crossing does not determine turning permissions. | unseen: The arrow head and possible
                        branches are not visible, so the straight-arrow classification is provisional; no
                        hidden stop line or waiting area is asserted. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes to the left.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes to the right.
Step 5  Rule            arrow:straight: Chinese lane-use arrows require following their indicated directions,
                        but the obscured arrow head prevents establishing this lane's complete permitted
                        directions.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires attention to pedestrians and yielding
                        as required, but does not itself authorize any of the seven assessed actions.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing.
Step 6  go_straight     not_determined (WRONG, label allowed): The arrow head is obscured, preventing
                        confirmation of the indicated movement.
Step 6  turn_left       not_determined (WRONG, label prohibited): The obscured arrow head and possible
                        branches leave left-turn permission undecided.
Step 6  turn_right      not_determined (WRONG, label prohibited): The obscured arrow head and possible
                        branches leave right-turn permission undecided.
Step 6  u_turn          not_determined (WRONG, label prohibited): The obscured arrow head leaves any U-turn
                        indication undecided.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid white boundaries and confirm the full lane arrow when the sedan
                        clears it before choosing an intersection movement. Approach the pedestrian crossing
                        cautiously, yield as required, and obey the intersection signals.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 4505, out 1162, 22.86 s

culane_test__d100_05251222_0385_02280 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs beside and beneath an elevated structure in China. My car
                        is in the leftmost lane; traffic hides the distant road surface and the next
                        intersection, and the rightmost extent of the carriageway is obscured. (lanes None,
                        mine 1, partial)
Step 2  Left            A single solid white line follows a raised curb on the left, with a planted strip and
                        metal guardrail beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments with clear intervening gaps separate my lane from another
                        same-direction traffic lane on the right; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge establishes my lane as the leftmost lane, and the
                        right lane line confirms another same-direction lane to my right; the total lane count
                        remains uncertain. | roles: The solid white line beside the curb fits a roadway edge,
                        while the broken white line fits a same-direction lane separator. | markings: No
                        guidance marking is readable on the exposed surface of my lane; vehicles obscure the
                        farther surface. | unseen: No lane-use arrow, intersection stop line, or waiting area
                        has been inferred from the overhead signs or hidden pavement. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised curb do not permit my car to leave
                        the lane across the left boundary.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe without interfering with other traffic.
Step 6  change_left     prohibited (correct): The solid left roadway edge and raised curb prohibit crossing to
                        the left.
Step 6  change_right    allowed (correct): The broken white lane separator permits a safe lane change to the
                        right.
Step 6  go_straight     not_determined (WRONG, label prohibited): Traffic hides the farther pavement where any
                        lane-use arrow governing the next intersection would be.
Step 6  turn_left       not_determined (WRONG, label allowed): Traffic hides the farther pavement where any
                        lane-use arrow governing the next intersection would be.
Step 6  turn_right      not_determined (WRONG, label prohibited): Traffic hides the farther pavement where any
                        lane-use arrow governing the next intersection would be.
Step 6  u_turn          not_determined (WRONG, label allowed): Traffic hides the farther pavement where any
                        lane-use arrow or prohibited-movement marking would be.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: boundary decisions follow the visible lines and curb, intersection
                        movements remain undecided because their governing pavement is obscured, and signs
                        have not been treated as lane markings.
Advice                  Do not cross the left curb; a rightward lane change is permitted by the dashed line
                        only when a safe gap exists. Check the overhead lane-direction signs and the U-turn-
                        ahead sign, and confirm the pavement arrows before choosing an intersection movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left', 'arrow:u_turn']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 4505, out 945, 17.34 s

culane_test__d100_05251222_0385_02400 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs alongside an elevated structure in China, with traffic
                        ahead and lane guidance approaching a junction whose details are distant. My car is in
                        the second of four same-direction lanes. (lanes 4, mine 2, full)
Step 2  Left            A continuous white solid line separates my lane from another traffic lane on the left;
                        no curb forms my lane boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from the adjacent lane containing the
                        white sedan; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is obscured by the hood.
Step 4  Cross-check     position: The second-of-four position agrees with ordinary traffic lanes beyond both
                        boundaries. | roles: Both white solid lines fit same-direction lane separators. |
                        markings: The visible straight arrow agrees with the continuing lane; the large
                        turning arrow to the left belongs to the neighboring lane, not mine. | unseen: The
                        arrow shaft is hidden by the hood, and junction details are too distant to describe;
                        neither has been invented. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes to the left.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes to the right.
Step 5  Rule            arrow:straight: A straight-ahead lane-use arrow directs traffic to proceed straight
                        rather than turn left, turn right, or make a U-turn.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing.
Step 6  go_straight     allowed (correct): The identifiable forward arrowhead indicates straight-ahead travel.
Step 6  turn_left       prohibited (correct): The straight-ahead lane-use arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-ahead lane-use arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-ahead lane-use arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary rules govern only lane changes, the identifiable arrow governs
                        junction movements, and no waiting-area marking governs entry.
Advice                  Stay between the solid white lines and continue straight, subject to traffic controls
                        ahead. For a turn, select an appropriately marked lane where changing lanes is
                        permitted, rather than crossing either solid boundary here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1081, 21.26 s

culane_test__d100_05251222_0385_04920 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road in China approaches a signal-controlled intersection beneath an
                        elevated railway. My car is in the straight-ahead lane behind the dark sedan, with a
                        left-turn lane to its left; the truck obscures the full lane arrangement on the right.
                        (lanes None, mine 2, partial)
Step 2  Left            A single solid white line runs along the left of my lane, with a lane bearing a left-
                        turn arrow beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, with another traffic lane
                        beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrow has a straight shaft and a
                        single straight-ahead head, partly obscured at its far end by the sedan.;
                        line:stop_line (partial): A transverse white stop line is visible ahead, with its
                        right portion obscured by the sedan.; line:crosswalk (partial): Broad white
                        pedestrian-crossing stripes are visible beyond the stop line, partly hidden by
                        vehicles.
Step 4  Cross-check     position: One same-direction lane is visible to the left, consistent with ego lane
                        index 2; another lane is visible on the right, but the total count is obscured. |
                        roles: Both white solid boundaries separate same-direction approach lanes, consistent
                        with lane-line roles. | markings: The straight arrow agrees with this approach lane;
                        the left-turn arrow belongs to the adjacent lane, not mine. | unseen: The total lane
                        count and obscured portions of the arrow, stop line and crossing are not treated as
                        fully visible. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-separation line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: In China, a solid white lane-separation line prohibits crossing it to
                        change lanes.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before the stop line.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires observing pedestrian priority and
                        keeping the crossing clear.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The identifiable straight-ahead arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight and do not cross either solid boundary;
                        turning requires selecting the appropriate lane before the solid-line section. Follow
                        the traffic signals, stop before the stop line when required, and keep the pedestrian
                        crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4505, out 1244, 22.43 s

culane_test__d100_05251222_0385_05250 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight, with an elevated structure alongside
                        the right side. My car is in the leftmost of three same-direction lanes; no
                        intersection or lane ending is visible ahead. (lanes 3, mine 1, full)
Step 2  Left            A solid white line borders my lane on the left, with a diagonally striped paved
                        exclusion area and then a median guardrail beyond it; the guardrail does not directly
                        border my lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car occupying
                        lane 1 of three same-direction lanes. | roles: The solid white left line fits a
                        roadway edge beside an exclusion area, and the broken white right line fits a same-
                        direction lane divider. | markings: No guidance markings are visible inside my lane;
                        the diagonal stripes lie outside its left boundary. | unseen: No unseen arrows,
                        intersection markings, or waiting areas have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, the solid white roadway edge bordering the marked exclusion
                        area prohibits crossing left into that area during ordinary driving.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 6  change_left     prohibited (correct): The solid white left edge bordering the exclusion area prohibits
                        crossing left.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a safe lane change.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the solid left edge and striped exclusion area; change right only after
                        checking traffic and blind spots. No intersection movement arrows or stop line are
                        visible, so this image does not establish a lane for turning.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 853, 14.82 s

culane_test__d100_05251309_0397_03150 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China with three lanes in this direction; my car is in the
                        rightmost lane. Traffic continues ahead, but the next intersection and the lane's end
                        are not clearly visible. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line runs along the right edge beside a raised curb and grass
                        verge, with a separate paved path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (partial): A white combined straight-and-right arrow is painted
                        in my lane; the right-pointing head is clear, while the forward portion is partly
                        obscured by the vehicle ahead.
Step 4  Cross-check     position: The rightmost position among three lanes agrees with a same-direction lane
                        line on the left and a curbside roadway edge on the right. | roles: The broken white
                        separator fits a lane line, and the solid white line beside the curb fits an edge
                        line. | markings: The combined straight-and-right arrow is compatible with the
                        rightmost lane; no conflicting word, symbol, or waiting area is visible. | unseen: The
                        forward portion of the arrow is partly obscured, and markings farther ahead cannot be
                        inspected reliably; no additional markings are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane separator permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: The curb forms a physical roadway edge that my car must not cross to
                        leave the lane.
Step 5  Rule            arrow:straight_right: A combined straight-and-right lane-use arrow permits straight
                        travel or a right turn, not a left turn or U-turn.
Step 6  change_left     allowed (correct): The broken white lane line permits a safe lane change to the left.
Step 6  change_right    prohibited (correct): The raised curb at the right edge prohibits crossing out of the
                        lane.
Step 6  go_straight     allowed (correct): The identifiable combined straight-and-right arrow permits straight
                        travel.
Step 6  turn_left       prohibited (correct): The combined straight-and-right arrow does not permit a left
                        turn.
Step 6  turn_right      allowed (correct): The clearly visible right branch of the arrow permits a right turn.
Step 6  u_turn          prohibited (correct): The combined straight-and-right arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the partly obscured arrow remains identifiable, each movement follows its
                        indicated directions, and boundary rules govern only their respective crossing
                        actions.
Advice                  Use this lane for straight travel or a right turn, subject to controls ahead; do not
                        cross the right curb. For a left turn or U-turn, move safely across the broken left
                        separator into an appropriately marked lane before any solid approach markings.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1052, 21.63 s

culane_test__d100_05251309_0397_03390 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road in China approaches a signal-controlled intersection. My car is in
                        a through lane, with two apparent same-direction lanes to its left and a rightmost
                        lane beside the traffic island. (lanes 4, mine 3, partial)
Step 2  Left            A single white solid line runs along the left of my lane, with another same-direction
                        lane and a white van beyond it; there is no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single white solid line runs along the right of my lane, separating it from another
                        same-direction lane; the raised traffic island is beyond that adjacent lane, not on my
                        boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): The head of a white forward-pointing arrow is visible
                        immediately ahead of the hood; its lower shaft is hidden by the hood.; arrow:straight
                        (full): Farther ahead in my lane, a white arrow has a single head pointing straight
                        forward.; line:stop_line (partial): A transverse white stopping line is visible near
                        the intersection, although its distant edges are indistinct.; line:crosswalk
                        (partial): Distant white crosswalk stripes extend across the approach beyond the
                        stopping line; their complete extent is difficult to resolve.
Step 4  Cross-check     position: The lane lines on both sides agree with an interior lane. The apparent count
                        is four lanes with my lane third from the left, but the far-left layout is less clear
                        than my immediate boundaries. | roles: Both white solid boundaries fit same-direction
                        approach lane separators; neither is a center line or the curb-side roadway edge. |
                        markings: The two forward arrows agree and indicate a through lane. The stop line and
                        crosswalk do not change the arrow's movement instruction. | unseen: The near arrow's
                        shaft is hidden by the hood, and distant transverse markings are only partially
                        resolved. The far-left lane count remains less certain; no hidden arrow branches or
                        waiting area have been assumed. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires proceeding straight from this
                        lane rather than turning left, right, or making a U-turn.
Step 5  Rule            arrow:straight: The repeated straight-only arrow confirms that this lane is designated
                        for straight movement.
Step 5  Rule            line:stop_line: When required to stop at the intersection, the vehicle must stop
                        before the stop line.
Step 5  Rule            line:crosswalk: The crosswalk requires yielding to pedestrians and must not be
                        obstructed.
Step 6  change_left     prohibited (correct): The solid white lane separator prohibits crossing the left
                        boundary.
Step 6  change_right    prohibited (correct): The solid white lane separator prohibits crossing the right
                        boundary.
Step 6  go_straight     allowed (correct): The clearly visible straight-only arrow permits straight movement.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, subject to the traffic signal, and do not cross
                        either solid lane separator. For a turn, select an appropriately marked lane before
                        the solid-line section; stop before the stop line when required and keep the crosswalk
                        clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4505, out 1657, 36.87 s

culane_test__d100_05251327_0403_00180 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China has three lanes in this direction and continues toward a
                        distant overhead structure. My car is in the leftmost lane; the next intersection and
                        the lane's terminal markings are not clearly visible. (lanes 3, mine 1, full)
Step 2  Left            A continuous solid white line runs along the left of my lane beside a raised curb,
                        with a paved verge and trees beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from the
                        same-direction lane occupied by the dark sedan.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is obscured by the hood, and no branching head is
                        visible.
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my car occupying
                        lane 1 of three same-direction lanes. | roles: The solid white line beside the curb
                        fits a roadway edge, and the broken white line fits a same-direction lane divider. |
                        markings: The visible straight arrowhead agrees with a through lane; the other visible
                        arrows belong to adjacent lanes. | unseen: The arrow shaft is obscured by the hood,
                        and distant terminal markings cannot be read; neither is treated as fully observed. |
                        result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised curb do not permit my car to move
                        left onto the verge.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires proceeding straight rather
                        than turning left, turning right, or making a U-turn.
Step 6  change_left     prohibited (correct): The solid roadway edge and raised curb prohibit leaving the lane
                        to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (correct): The clearly visible forward arrowhead permits straight travel.
Step 6  turn_left       prohibited (correct): The visible straight-only arrow does not permit a left turn.
Step 6  turn_right      prohibited (correct): The visible straight-only arrow does not permit a right turn.
Step 6  u_turn          prohibited (correct): The visible straight-only arrow does not permit a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent: the arrow's forward head is readable despite its obscured lower shaft, and
                        each decision follows the boundary or marking that governs it.
Advice                  Continue straight in this lane and do not cross the left curb. If a different movement
                        is needed, change right across the broken divider only when safe, then follow the
                        markings of the appropriate lane; the sedan occupies the adjacent lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 986, 16.58 s

culane_test__d100_05251327_0403_00630 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An elevated, divided urban road continues ahead with no visible intersection or lane
                        ending. My car is in the left lane of two lanes traveling in this direction. (lanes 2,
                        mine 1, full)
Step 2  Left            A continuous solid white line runs along the left side of my lane, with a narrow
                        margin and a concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction traffic lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane divider on the right agree with my car
                        occupying lane 1 of 2. | roles: The solid white line beside the barrier fits a roadway
                        edge; the broken white line separates same-direction lanes. | markings: No guidance
                        arrows, words, symbols, waiting areas or transverse markings are visible in my lane. |
                        unseen: No hidden intersection layout or distant lane-use marking has been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white roadway edge and concrete barrier prohibit moving out
                        of my lane to the left.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing to the
                        right when safe and without obstructing other traffic.
Step 6  change_left     prohibited (correct): The solid roadway edge and physical barrier prohibit crossing to
                        the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain within the roadway edge on the left; you may change to the right lane across
                        the broken white line when safe. No intersection movement or stopping point is
                        indicated by the visible markings.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 781, 11.22 s

culane_test__d100_05251327_0403_00930 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues straight ahead; no intersection or lane
                        ending is clearly visible. My car is in the leftmost of three visible same-direction
                        lanes. (lanes 3, mine 1, full)
Step 2  Left            A solid white line follows the left edge of my lane beside a raised curb and planted
                        median; no adjacent traffic lane lies immediately beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White elongated dashes separated by gaps divide my lane from another same-direction
                        lane on the right, with no curb between them.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has a single head pointing
                        straight ahead.
Step 4  Cross-check     position: The left edge line and median place my lane leftmost; the right lane line
                        separates it from the other same-direction lanes, consistent with lane index 1 of 3. |
                        roles: The solid white roadside line fits an edge line, and the broken white right
                        boundary fits a same-direction lane divider. | markings: The straight-only arrow is
                        consistent with the lane continuing forward; no conflicting marking or waiting area is
                        visible. | unseen: No distant stop line or intersection marking is inferred; the next
                        intersection is outside the clearly readable stretch. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge beside the raised median does not permit leaving
                        the lane to the left or driving onto the median.
Step 5  Rule            right_boundary: A broken white same-direction lane line permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 5  Rule            arrow:straight: In China, a straight-only lane-use arrow requires proceeding straight
                        from this lane rather than turning left, right, or making a U-turn.
Step 6  change_left     prohibited (correct): The solid left roadway edge and raised median prohibit moving
                        out of the lane to the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     allowed (correct): The single straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; do not cross the left edge or median. If a different
                        movement is needed, change right only when safe and seek a lane explicitly marked for
                        that movement farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 979, 17.64 s

culane_test__d100_05251327_0403_01200 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined urban expressway in China continues ahead without a visible
                        intersection or lane ending. My car is in the middle of three lanes travelling in this
                        direction. (lanes 3, mine 2, full)
Step 2  Left            White broken lane markings, with visible dashes and gaps, separate my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           White broken lane markings, with visible dashes and gaps, separate my lane from
                        another same-direction lane on the right; the concrete roadside barrier is beyond that
                        lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): White Chinese-character road text is painted longitudinally in
                        my lane ahead; the characters cannot all be read reliably at this distance.
Step 4  Cross-check     position: Three lanes and position 2 agree with a same-direction lane line on each
                        side. | roles: Both white broken boundaries fit ordinary same-direction lane
                        separators. | markings: The partially readable road text does not conflict with either
                        boundary; no lane-use arrow or marked waiting area is discernible in my lane. |
                        unseen: The road text has not been guessed, and no intersection markings or directions
                        have been inferred beyond the visible stretch. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane separator permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane separator permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 5  Rule            text:other: The incompletely readable road text does not establish permission or
                        prohibition for any of the seven assessed actions.
Step 6  change_left     allowed (correct): The white broken lane line permits a safe lane change to the left.
Step 6  change_right    allowed (correct): The white broken lane line permits a safe lane change to the right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: both lane changes follow the broken-line rules, and the absence of
                        movement-governing markings is not treated as permission to turn.
Advice                  Continue in the middle lane unless a lane change is needed; either broken boundary may
                        be crossed after checking traffic and signalling. No intersection, turning
                        opportunity, or stopping line is visible, and the distant road text should be read
                        when closer.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 992, 17.75 s

culane_test__d100_05251327_0403_02340 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban roadway in China continues ahead with a gentle left bend; no intersection or
                        lane ending is visible. My car is in the left lane of two apparent same-direction
                        lanes, beside a fenced divider. (lanes 2, mine 1, partial)
Step 2  Left            A solid white line follows a raised curb and fenced divider on the left; another
                        roadway lies beyond the divider.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from a paved strip on the right extending to
                        the sidewalk curb; no designation for that strip is readable.
                        white solid, curb no, unknown, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and edge line place my lane leftmost; two lanes are apparent,
                        but the function of the paved strip on the right is uncertain. | roles: The white
                        solid left line fits a roadway edge; the right white solid line is visible, but its
                        role as a lane divider or an edge adjoining a separate-use strip cannot be
                        established. | markings: No arrows, words, symbols, waiting areas, or transverse
                        markings are visible in my lane. | unseen: The right-hand strip is not assumed to be a
                        normal traffic lane or a bicycle lane; the distant lane end is not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The raised curb forming the left roadway edge prohibits moving out of
                        my lane across that boundary.
Step 5  Rule            right_boundary: In China a solid white lane divider prohibits crossing, but an edge
                        line has a different function, so the unresolved role of this line prevents a definite
                        crossing decision.
Step 6  change_left     prohibited (correct): The raised curb on the left prohibits crossing this boundary.
Step 6  change_right    not_determined (WRONG, label prohibited): The solid white line is visible, but its
                        lane-divider or edge-line role is unresolved.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Follow the current lane around the bend and do not cross the left curb; avoid crossing
                        the right solid line until the adjacent strip's function is clear. The visible speed-
                        limit sign indicates 30 km/h; no turn-selection markings or stopping point are
                        visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 980, 18.68 s

culane_test__d100_05251327_0403_03870 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A narrow urban road runs alongside an elevated structure, with a car immediately ahead
                        and sidewalks on both sides. My car is next to the left roadway edge; the function of
                        the paved strip to the right and the lane's eventual end are not clearly visible.
                        (lanes None, mine 1, partial)
Step 2  Left            A continuous white line borders my lane on the left beside a raised curb and narrow
                        sidewalk, with a wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white longitudinal line is visible to the right of the car ahead, with more paved
                        roadway beyond; the car and hood obscure its continuation, so a dash-and-gap pattern
                        cannot be confirmed.
                        white solid, curb no, unknown, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left edge line and curb place my lane leftmost in my direction; the
                        uncertain function of the roadway beyond the right line prevents a reliable lane
                        count. | roles: The white left line beside the curb fits an edge line. The right
                        line's color alone does not establish whether it separates motor lanes or marks
                        another roadway division. | markings: No arrows, words, symbols, waiting areas or
                        transverse markings are readable in the visible portions of my lane. | unseen: The
                        right line looks continuous in its exposed segment, but its complete pattern and role
                        are unconfirmed; the vehicle ahead also hides part of my lane. | result: consistent
Step 5  Rule            left_boundary: The raised curb forms a physical roadway edge and prohibits leaving my
                        lane across it.
Step 5  Rule            right_boundary: In China, a solid lane-dividing line prohibits crossing while an
                        ordinary broken lane line permits a safe lane change, but the obscured pattern and
                        uncertain role here prevent choosing the applicable rule.
Step 6  change_left     prohibited (correct): The raised curb at the left roadway edge prohibits crossing.
Step 6  change_right    not_determined (WRONG, label prohibited): The right boundary's complete pattern and
                        function are obscured, so permission to cross is undetermined.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the curb prohibits leaving to the left, the uncertain right boundary
                        leaves crossing undecided, and no unseen movement marking is treated as permission.
Advice                  Remain behind the vehicle ahead and do not cross the left curb or assume the paved
                        strip on the right is another motor-vehicle lane. Confirm the right boundary and any
                        downstream lane-use markings before changing lanes or selecting a turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1119, 24.72 s

culane_test__d100_05251327_0403_03960 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road in China runs beside an elevated structure, with two apparent same-
                        direction lanes. My car is in the left lane behind a sedan; the road continues ahead,
                        but the lane's distant end is obscured. (lanes 2, mine 1, partial)
Step 2  Left            A solid white line follows a raised curb on the left, with a narrow paved walkway and
                        the elevated structure's wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears continuous over the exposed stretch to the right of the sedan,
                        with another paved travel strip beyond; the sedan hides its continuation ahead.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge agrees with my lane being leftmost; the apparent lane
                        divider on the right agrees with another lane to the right, although that strip's
                        designation is not visible. | roles: The white left edge line and curb fit a roadway
                        edge; the visible solid white right line fits a lane divider prohibiting crossing. |
                        markings: No guidance markings are readable in the exposed part of my lane. | unseen:
                        The sedan and hood obscure part of the lane surface, and the distant lane end cannot
                        be inspected; no hidden arrows, stop lines, or waiting areas are assumed. | result:
                        consistent
Step 5  Rule            left_boundary: The raised curb forms a physical roadway edge and prohibits leaving the
                        lane to the left onto the walkway.
Step 5  Rule            right_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes in the visible solid-lined stretch.
Step 6  change_left     prohibited (correct): The raised curb prohibits leaving the roadway to the left.
Step 6  change_right    prohibited (correct): The visible solid white lane divider prohibits crossing to the
                        right.
Step 6  go_straight     not_determined: The lane end and potentially governing arrows are obscured.
Step 6  turn_left       not_determined: The lane end and potentially governing arrows are obscured.
Step 6  turn_right      not_determined: The lane end and potentially governing arrows are obscured.
Step 6  u_turn          not_determined: The lane end and potentially governing movement markings are obscured.
Step 6  enter_waiting_areanot_determined: No waiting area is visible, but the obscured road ahead prevents
                          determining whether one serves this lane.
Step 7  Reflect         consistent
Advice                  Stay between the left curb and the solid white divider; do not change lanes across
                        either boundary here. Keep a safe gap behind the sedan and reassess intersection
                        movements when the lane markings ahead become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 935, 19.98 s

culane_test__d100_05251627_0452_02850 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road approaches a signalized intersection beneath an overpass. My car
                        is in the leftmost lane beside a central separator; traffic and the right edge obscure
                        the total number of same-direction lanes. (lanes None, mine 1, partial)
Step 2  Left            A continuous yellow painted line runs beside a raised central separator with a white
                        metal fence; opposing traffic is visible beyond it.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A faded white line separates my lane from the same-direction lane containing the
                        yellow taxi; the visible near stretch appears continuous, while vehicles obscure its
                        farther continuation.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The central separator on the left places my lane leftmost, and the white
                        lane divider on the right agrees with another same-direction lane there; the total
                        lane count remains uncertain. | roles: The yellow line and physical separator fit a
                        center boundary, and the white divider fits a same-direction lane boundary. |
                        markings: No guidance marking can be read in the exposed part of my lane; the hood,
                        lead vehicle and distant traffic obscure other portions. | unseen: No arrow, stop line
                        or waiting area is inferred from the intersection context; the right boundary's
                        distant pattern remains obscured. | result: consistent
Step 5  Rule            left_boundary: In China, the solid yellow center boundary and physical separator
                        prohibit crossing left into opposing traffic.
Step 5  Rule            right_boundary: In China, a solid white lane divider prohibits changing lanes across
                        its solid stretch.
Step 6  change_left     prohibited (correct): The solid yellow center boundary and physical separator prohibit
                        crossing left.
Step 6  change_right    prohibited (correct): The visible solid white divider prohibits crossing right along
                        the exposed stretch.
Step 6  go_straight     not_determined: The lane-end guidance markings are obscured, so any straight-ahead
                        permission cannot be established.
Step 6  turn_left       not_determined: The lane-end guidance markings are obscured, so left-turn permission
                        cannot be established.
Step 6  turn_right      not_determined: The lane-end guidance markings are obscured, so right-turn permission
                        cannot be established.
Step 6  u_turn          not_determined: The lane-end guidance markings are obscured, so U-turn permission
                        cannot be established.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: crossing decisions follow the visible boundaries, intersection movements
                        remain undecided because guidance is obscured, and no waiting area is inferred.
Advice                  Stay within the visible boundaries and do not cross the central separator or solid
                        white divider. Approach cautiously, obey the signals, and confirm lane arrows and the
                        stopping position as traffic exposes them.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 996, 19.66 s

culane_test__d100_05251718_0469_00390 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road in China approaches a signal-controlled intersection with a
                        pedestrian crossing. My car is in an interior approach lane; the lane arrangement
                        farther left is not clear enough to count all same-direction lanes reliably. (lanes
                        None, mine None, insufficient)
Step 2  Left            A continuous white line runs along the left of my lane toward the stop line, with
                        another traffic lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane toward the stop line, with
                        another traffic lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible directly
                        ahead; the lower portion of the arrow is obscured by the hood, and no branching head
                        is visible.; line:stop_line (full): A transverse white stop line crosses my lane
                        before the pedestrian crossing.; line:crosswalk (full): Broad white pedestrian-
                        crossing stripes extend across my lane beyond the stop line.
Step 4  Cross-check     position: Both boundaries separate my lane from neighboring same-direction lanes,
                        establishing an interior position without establishing its exact index or the total
                        lane count. | roles: The white solid lines fit approach lane separators rather than a
                        center line or roadway edge. | markings: The visible straight arrow agrees with an
                        interior through lane; the stop line precedes the crosswalk. | unseen: The arrow's
                        lower portion is hidden by the hood, and the full lane arrangement to the left is
                        uncertain; neither is treated as completely observed. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        prohibits turning left, turning right, or making a U-turn from this lane.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before this line.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires yielding to pedestrians and must not
                        be obstructed.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel.
Step 6  turn_left       prohibited (correct): The straight-only lane arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only lane arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only lane arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the visible arrowhead establishes the lane direction despite its obscured
                        lower stem, and neither the stop line nor the crosswalk is used to decide a turning or
                        lane-change action.
Advice                  Stay in this lane for straight travel and do not cross either solid separator; turning
                        requires an appropriate lane selected before the solid-line approach. Obey the
                        applicable signal, stop before the stop line when required, and yield to pedestrians
                        without blocking the crossing.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4505, out 1329, 28.01 s

culane_test__d100_05251718_0469_01320 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road in China continues straight beneath a pedestrian footbridge; no
                        intersection or lane ending is visible. My car is in the leftmost of two same-
                        direction lanes, behind a sedan. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line runs beside a raised curb on the left, with a paved pedestrian
                        area and planting beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white broken line, with a visible dash and gap, separates my lane from another
                        traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane divider on the right agree with my lane
                        being lane 1 of 2. | roles: The white solid line beside the curb fits a roadway edge,
                        and the broken white line fits a same-direction lane divider. | markings: No arrows,
                        words, symbols, waiting areas or transverse lines are visible in my lane. | unseen:
                        The lead vehicle hides part of the road ahead; no markings beneath it or beyond the
                        visible stretch are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white roadway edge and raised curb prohibit leaving my lane
                        across the left boundary.
Step 5  Rule            right_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 6  change_left     prohibited (correct): The solid roadway edge and raised curb prohibit crossing the
                        left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the left curb; change right only after checking traffic and yielding to
                        vehicles already in that lane. No visible markings establish turn permissions at the
                        next intersection, so reassess as it comes into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 859, 14.5 s

culane_test__d100_05251718_0469_02040 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road in China has two lanes in this direction. My car is in
                        the leftmost lane; the road continues ahead with no visible intersection or lane
                        ending. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line follows a raised curb on the left, with a planted median
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken lane markings, with visible dashes and gaps, separate my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego lane index 1 agree with a median-side edge on the left and
                        a same-direction lane divider on the right. | roles: The white solid line beside the
                        median curb fits an edge line; the white dashed divider fits a lane line. | markings:
                        No guidance markings are visible within my lane, so none conflict with the boundaries.
                        | unseen: No intersection, lane-end markings, or hidden guidance markings have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised median curb prohibit leaving my lane
                        across this boundary.
Step 5  Rule            right_boundary: In China, a white dashed lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 6  change_left     prohibited (correct): The solid edge and raised median curb prohibit crossing the left
                        boundary.
Step 6  change_right    allowed (correct): The white dashed lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the median curb; you may change into the right lane across the dashed
                        line when safe. No intersection guidance is visible, so do not infer turning
                        permissions from this view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 762, 12.56 s

culane_test__d100_05251718_0469_02250 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road in China continues straight ahead; no intersection or
                        lane ending is visible. My car is in the left of two same-direction lanes. (lanes 2,
                        mine 1, full)
Step 2  Left            A raised curb borders the lane on the left, with grass, trees and hedges beyond; no
                        painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane; vehicles obscure part of its distant stretch.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and right lane divider agree with my car occupying lane 1 of
                        two same-direction lanes. | roles: The curb forms the left roadway edge; the broken
                        white line separates same-direction lanes. | markings: No visible in-lane guidance
                        marking conflicts with the boundaries. | unseen: No markings or intersection layout
                        beyond the visible stretch have been inferred. | result: consistent
Step 5  Rule            left_boundary: The raised roadway curb is a physical edge that my car must not cross.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing traffic.
Step 6  change_left     prohibited (correct): The raised left curb prohibits leaving the lane across that
                        edge.
Step 6  change_right    allowed (correct): The broken white right divider permits a safe lane change.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the left curb; change right only after checking the vehicles alongside
                        and behind. No intersection movement or stopping position is established by the
                        visible markings, so follow the lane guidance encountered farther ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 792, 13.76 s

culane_test__d100_05251718_0469_05070 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road in China continues ahead, with vehicles obscuring the
                        more distant roadway; no intersection or lane end is clearly visible. My car is in the
                        leftmost of two visible lanes in this direction. (lanes 2, mine 1, full)
Step 2  Left            A solid white edge marking follows a raised curb on the left, with a planted strip
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments, with visible gaps between them, separate my lane from
                        another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and edge line place my lane at the left edge of this
                        carriageway; the right lane line separates it from the second same-direction lane. |
                        roles: The solid white marking beside the curb fits an edge line, and the broken white
                        marking on the right fits a same-direction lane divider. | markings: No guidance
                        markings are readable on the visible pavement in my lane; the overhead sign is not a
                        pavement marking. | unseen: No distant arrows, stop line, or intersection layout has
                        been inferred; traffic and distance obscure the lane farther ahead. | result:
                        consistent
Step 5  Rule            left_boundary: The raised curb forms a physical roadway edge that my car must not
                        cross to leave the lane on the left.
Step 5  Rule            right_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 6  change_left     prohibited (correct): The raised curb on the left prohibits leaving the roadway across
                        this boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_determined: The lane's eventual approach markings are obscured by traffic and
                        distance, so its intersection movement permissions cannot be determined.
Step 6  turn_left       not_determined: The lane's eventual approach markings are obscured, so a left-turn
                        permission or restriction cannot be determined.
Step 6  turn_right      not_determined: The lane's eventual approach markings are obscured, so a right-turn
                        permission or restriction cannot be determined.
Step 6  u_turn          not_determined: The lane's eventual approach markings are obscured, so a U-turn
                        permission or restriction cannot be determined.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary decisions follow the visible curb and broken divider, while
                        unseen intersection markings are not treated as granting movement permissions.
Advice                  Stay clear of the left curb; you may change right across the broken white line after
                        checking for traffic, including the vehicle alongside. Confirm the upcoming lane
                        arrows and junction controls before choosing a turning lane; no stopping position is
                        visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 977, 17.89 s

culane_test__d100_05251718_0469_05190 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban road in China has three lanes in this direction. My car is in the
                        middle lane; the road continues ahead, with no clearly visible intersection or lane
                        ending. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another
                        traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        traffic lane on the right; the roadside curb is beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 2 agree with a lane line and an
                        adjacent same-direction lane on each side. | roles: Both white broken boundaries fit
                        same-direction lane-divider roles. | markings: No arrows, words, symbols, waiting
                        areas or transverse markings are readable in my visible lane. | unseen: No lane-use
                        restriction or marking at a distant intersection is inferred; the lane's eventual end
                        is not visible. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No visible marking governs this action.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: lane changes are permitted by the visible broken dividers; no intersection
                        movement permission is inferred from the absence of visible guidance markings.
Advice                  You may change lanes across either broken white divider after checking traffic and
                        signalling. Stay in your lane unless a change is needed, and follow upcoming lane-use
                        markings before choosing a turning lane; no stop line is visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 845, 14.5 s

culane_test__d100_05251947_0499_00840 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided multilane road in China continues ahead beside an elevated roadway,
                        with no intersection or lane ending visible. My car is in the leftmost of three
                        visible same-direction lanes. (lanes 3, mine 1, full)
Step 2  Left            A single solid white line runs beside a raised concrete median on the left, with
                        opposing traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left median edge and right lane divider agree with my car occupying lane
                        1 of three same-direction lanes. | roles: The solid white line beside the median is a
                        roadway edge line, not an opposing-traffic center line; the broken white line
                        separates same-direction lanes. | markings: No arrows, words, symbols, transverse
                        lines or marked waiting areas are visible in my lane. | unseen: No markings are
                        inferred beyond the visible stretch; the next intersection is not visible. | result:
                        consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised median prohibit leaving my lane
                        across its left boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes when
                        safe without obstructing other traffic.
Step 6  change_left     prohibited (correct): The solid left edge and raised median prohibit crossing this
                        boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No visible marking governs this action.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the median; change right across the broken line only after checking
                        traffic and blind spots. No intersection guidance or stop line is visible, so choose a
                        turning lane only when the relevant markings and signs come into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 798, 13.95 s

culane_test__d100_05251947_0499_04830 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A multi-lane divided urban road in China continues straight ahead, with vehicles in
                        the distance. The car appears to be in the rightmost of three same-direction lanes;
                        darkness limits visibility of the distant roadway. (lanes 3, mine 3, partial)
Step 2  Left            A faded white broken line, with visible painted segments and gaps, separates this lane
                        from another traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line follows the right side of the lane beside a raised curb and
                        planted roadside strip, although parts are dimly lit.
                        white solid, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:straight (partial): A small, faint white forward-pointing arrow is visible ahead
                        in this lane; its distant outline is not completely clear.
Step 4  Cross-check     position: The lane line on the left and curb-side edge on the right agree with the car
                        occupying the rightmost lane; the total of three lanes is less certain in the
                        darkness. | roles: The white broken divider fits a same-direction lane line, and the
                        white continuous curb-side marking fits an edge line. | markings: The apparent
                        straight arrow agrees with the lane continuing forward, but its incomplete outline
                        limits movement interpretation. | unseen: No stop line, crosswalk, waiting area, or
                        additional arrow head can be confirmed; the distant end of the lane is not clearly
                        visible. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: The continuous roadway edge and raised curb do not permit a normal
                        lane change onto the planted roadside.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires proceeding straight rather
                        than turning, but that restriction depends on confirming that no additional arrow head
                        is present.
Step 6  change_left     allowed (correct): The visible white broken lane divider permits a safe lane change
                        left.
Step 6  change_right    prohibited (correct): The right roadway edge and raised curb prohibit moving onto the
                        roadside.
Step 6  go_straight     allowed (WRONG, label prohibited): The visible forward arrow head permits straight
                        travel.
Step 6  turn_left       not_determined (WRONG, label prohibited): The distant arrow outline is incomplete, so
                        a straight-only restriction cannot be confirmed.
Step 6  turn_right      not_determined (WRONG, label allowed): The distant arrow outline is incomplete, so a
                        straight-only restriction cannot be confirmed.
Step 6  u_turn          not_determined (WRONG, label prohibited): The incompletely visible lane-use arrow does
                        not establish the full movement restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: straight travel follows the visible arrow head, while turn restrictions
                        remain undecided because the complete arrow outline is unclear.
Advice                  Continue straight and do not cross the right curb-side boundary; a left lane change is
                        possible across the broken divider when safe. Confirm the complete lane arrow and
                        junction layout before choosing any turning movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation None, contradictions []
Tokens                  in 4505, out 1111, 22.93 s

culane_test__d100_05252026_0512_00450 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China at night, with three lanes in this direction and traffic
                        ahead. My car is in the rightmost lane; the distant intersection approach is not
                        clearly readable. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with a visible dash and gap, separates my lane from another same-
                        direction traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line borders my lane on the right, with a narrow roadside
                        strip and a raised roadside edge farther beyond the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The rightmost position among three lanes agrees with a same-direction lane
                        line on the left and a roadway edge line on the right. | roles: The broken white lane
                        divider and solid white roadway edge fit their observed roles. | markings: No readable
                        guidance markings appear in the visible portion of my lane; markings at its distant
                        end cannot be verified. | unseen: No arrows, stop line, or waiting area have been
                        inferred from the distant, poorly resolved approach. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge restricts ordinary crossing onto the
                        roadside strip; it is not an additional traffic lane.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid white roadway edge restricts crossing onto the
                        roadside strip.
Step 6  go_straight     not_determined: The lane-end guidance is too distant to read, so any governing arrow
                        cannot be verified.
Step 6  turn_left       not_determined: The lane-end guidance is too distant to read, so any governing arrow
                        or prohibition cannot be verified.
Step 6  turn_right      not_determined: The lane-end guidance is too distant to read, so any governing arrow
                        or prohibition cannot be verified.
Step 6  u_turn          not_determined: The lane-end guidance is too distant to read, so any governing arrow
                        or prohibition cannot be verified.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay inside the right edge line; a left lane change is permitted only when safe. Read
                        the lane arrows and intersection controls as you approach before choosing a turning
                        movement; no stop line is currently readable.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 944, 18.52 s

culane_test__d100_05252026_0512_01020 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road in China at night, with traffic traveling in both directions. My
                        car appears to be in the second lane from the left in its direction; darkness prevents
                        a reliable count of all lanes on the right, and no intersection or lane ending is
                        clearly visible. (lanes None, mine 2, partial)
Step 2  Left            A white broken line is visible to my left, with a painted segment and a darker gap;
                        another same-direction lane containing a car lies beyond it, with no curb along this
                        boundary.
                        white dashed, curb no, lane_line, evidence partial
Step 2  Right           A white broken line, including a bright dash ahead and a gap, separates my lane from
                        another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane on the left supports the second-from-left position,
                        and the right lane line confirms another lane on the right; the total lane count
                        remains uncertain. | roles: White broken boundaries fit separators between same-
                        direction traffic lanes. | markings: No readable arrows, words, symbols, waiting
                        areas, or transverse markings are visible in my lane. | unseen: The distant road and
                        rightmost roadway edge are poorly resolved; no unseen lane count, intersection layout,
                        or guidance marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The visible broken white lane separator permits a safe lane change
                        to the left.
Step 6  change_right    allowed (correct): The broken white lane separator permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the broken lane separators permit only the corresponding lane changes,
                        while no visible marking determines intersection movements or waiting-area entry.
Advice                  Either lane change is permitted by the visible broken separators, but check
                        surrounding traffic carefully. Continue watching for clearer lane-use arrows,
                        intersection controls, and stop lines before choosing a turning lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1100, 23.53 s

culane_test__d100_05252026_0512_01350 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China at night, continuing ahead with vehicles in the
                        distance; no intersection or lane ending is clearly visible. My car is in the
                        rightmost of three apparent same-direction lanes. (lanes 3, mine 3, partial)
Step 2  Left            A broken white line, with a visible dash and intervening gap, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with a narrow roadside strip
                        and a raised roadside edge farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider and right roadway edge agree with a rightmost lane;
                        the total lane count is less certain because the farther-left markings are dark and
                        blurred. | roles: The broken white line fits a same-direction lane divider, and the
                        continuous white line fits the roadway edge. | markings: No guidance marking is
                        readable within my lane, so none contradicts the boundaries. | unseen: The next
                        intersection and its lane-use markings are not visible; no arrows, stop line, or
                        waiting area have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: The solid white roadway edge restricts ordinary crossing onto the
                        roadside strip.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid white roadway edge restricts crossing onto the
                        roadside strip.
Step 6  go_straight     not_determined: The next intersection and any lane-use marking governing its movements
                        are beyond the visible stretch.
Step 6  turn_left       not_determined: The next intersection and any lane-use marking governing its movements
                        are beyond the visible stretch.
Step 6  turn_right      not_determined: The next intersection and any lane-use marking governing its movements
                        are beyond the visible stretch.
Step 6  u_turn          not_determined: The next intersection and any lane-use marking governing its movements
                        are beyond the visible stretch.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay inside the right edge line; a left lane change is permitted only after checking
                        traffic. Continue watching for lane-use arrows and intersection controls ahead before
                        choosing a turning lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 996, 20.93 s

culane_test__d193_06042058_0527_02610 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit, divided road continues straight at night, with no intersection or lane ending
                        visible. My car is in the right lane of two lanes traveling in this direction. (lanes
                        2, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; the paint has a yellowish cast under the lighting.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved roadside
                        strip beyond it; no raised curb forms the lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider and right roadway edge agree with my lane being second
                        from the left on a two-lane carriageway. | roles: The broken white line fits a same-
                        direction lane divider, and the continuous white line fits a roadway edge. | markings:
                        No arrows, words, symbols, waiting areas or transverse markings are visible in my
                        lane. | unseen: No intersection, downstream lane-use markings or hidden roadway
                        features have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge prohibits an ordinary lane change across
                        it onto the roadside strip.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  change_right    prohibited (correct): The solid white roadway edge prohibits an ordinary crossing onto
                        the roadside strip.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary decisions follow their respective rules, and no intersection
                        movement is authorized or prohibited by an absent marking.
Advice                  Stay within the right edge line; you may change into the left lane across the broken
                        line after checking traffic. No intersection or turn guidance is visible, so do not
                        infer permission to turn or make a U-turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 832, 15.28 s

culane_test__d193_06042058_0527_03240 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit divided road at night continues ahead, with no intersection or lane ending
                        visible. My car is in the right lane of two lanes in this direction. (lanes 2, mine 2,
                        full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        lane occupied by the white vehicle on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved shoulder and
                        roadside reflectors beyond; no raised curb is visible along the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego position 2 agree with a same-direction lane line on the
                        left and a roadway edge line on the right. | roles: The broken white separator fits a
                        lane line, and the continuous white shoulder boundary fits an edge line. | markings:
                        No guidance markings are visible within my lane, so none conflict with the boundaries.
                        | unseen: No intersection layout or markings beyond the visible road are inferred. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge line must not ordinarily be crossed to
                        drive onto the shoulder.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (correct): The solid white roadway edge line prohibits ordinary crossing
                        onto the shoulder.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay within the right edge line; a left lane change is permitted by the markings, but
                        the vehicle alongside must clear before you move. No intersection movement guidance or
                        stopping line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 755, 11.78 s

culane_test__d193_06051114_0632_02790 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road in China approaches a signalized intersection. My car appears to be
                        in the middle of three same-direction lanes, behind the red car; some paint is worn
                        and the distant lane end is obscured. (lanes 3, mine 2, partial)
Step 2  Left            A faint white line runs along my lane's left side and appears continuous over the
                        visible approach, with another same-direction lane beyond it and no curb on this
                        boundary.
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           A white solid line runs diagonally forward along my lane's right side, separating it
                        from another same-direction lane; there is no curb at this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A worn white straight-ahead arrow is visible in my lane
                        behind the red car; its forward head and shaft are discernible.
Step 4  Cross-check     position: Lane lines on both sides agree with my lane being the middle lane; the total
                        count is less certain because the outer approach markings are faint. | roles: White
                        longitudinal lines between same-direction lanes fit lane-line roles; the left line's
                        worn appearance reduces certainty about its pattern. | markings: The visible straight
                        arrow agrees with a through lane bounded by approach lane lines. | unseen: The left
                        boundary pattern is tentative, and the red car and distance obscure the lane end; no
                        stop line or waiting area is asserted. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing, but the
                        worn left line cannot be classified with enough certainty to decide a left lane
                        change.
Step 5  Rule            right_boundary: A solid white lane-dividing line in China prohibits crossing it to
                        change lanes.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires proceeding straight from this
                        lane rather than turning left, turning right or making a U-turn.
Step 6  change_left     not_determined (WRONG, label prohibited): The worn left boundary appears solid, but
                        its pattern is insufficiently clear to determine whether crossing is permitted.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing to the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The discernible straight-ahead arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible marked waiting area governs this action.
Step 7  Reflect         consistent: the uncertain left boundary remains undecided, while the visible right
                        solid line and readable straight-arrow direction govern their respective actions.
Advice                  Use this lane to proceed straight, subject to the traffic signal and vehicles ahead;
                        do not cross the right solid line, and treat the worn left boundary cautiously. For a
                        turn, use an appropriately marked lane reached where lane changes are permitted, and
                        stop before the intersection's stop line when required.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1149, 24.39 s

culane_test__d193_06051114_0632_04320 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This is a tree-lined urban road in China, with opposing traffic separated by a metal
                        median fence. My car is in the left lane of two lanes in this direction; the road
                        continues ahead, with no intersection clearly visible. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line runs beside the median fence on the left, with opposing
                        traffic beyond the fence.
                        white solid, curb yes, center_line, evidence full
Step 2  Right           A worn white broken line, with visible painted segments and gaps, separates my lane
                        from the lane occupied by the black sedan on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower portion of the arrow is obscured, so additional branches
                        cannot be checked.
Step 4  Cross-check     position: The median boundary on the left and a same-direction lane on the right agree
                        with my car being in lane 1 of 2. | roles: The left boundary separates opposing
                        directions physically; its visible paint is white, not inferred to be yellow. The
                        broken white right boundary fits a same-direction lane divider. | markings: The
                        visible forward arrowhead is compatible with continuing along this lane, but its
                        obscured lower portion prevents confirming whether it also has turning branches. |
                        unseen: No additional arrow branches, intersection markings, or waiting areas are
                        claimed; the hood hides part of the nearest arrow. | result: consistent
Step 5  Rule            left_boundary: In China, the physical median barrier and continuous separation
                        prohibit leaving the lane across this boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe.
Step 5  Rule            arrow:straight: A forward lane-use arrow permits straight travel, but the obscured
                        portion must be checked before concluding whether any turning movement is also
                        permitted.
Step 6  change_left     prohibited (correct): The median fence and continuous left boundary prohibit crossing
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change right.
Step 6  go_straight     allowed: The visible forward arrowhead permits straight travel.
Step 6  turn_left       not_determined: The obscured lower arrow may conceal a branch, so left-turn permission
                        cannot be determined.
Step 6  turn_right      not_determined: The obscured lower arrow may conceal a branch, so right-turn
                        permission cannot be determined.
Step 6  u_turn          not_determined: The complete lane-use arrow is not visible, so its restriction on a
                        U-turn cannot be determined.
Step 6  enter_waiting_areanot_applicable: No visible waiting-area marking or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not cross the median boundary. A rightward lane
                        change is permitted only when clear of the black sedan; confirm the complete lane
                        arrows before choosing a turning lane.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 4505, out 1069, 22.65 s

culane_test__d193_06051123_0635_00450 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road in China approaches a broad intersection with a zebra crossing.
                        My car is in the leftmost of two apparent motor-vehicle lanes in this direction; an
                        additional curbside strip lies farther right. (lanes 2, mine 1, partial)
Step 2  Left            A single continuous yellow line runs along my lane's left side to the stop line, with
                        opposing-direction roadway beyond and no curb.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single continuous white line runs from beside the hood to the stop line, separating
                        my lane from another same-direction lane; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid transverse white stop line spans my lane before the
                        zebra crossing.; line:crosswalk (full): Broad white zebra-crossing stripes extend
                        across my lane immediately beyond the stop line.
Step 4  Cross-check     position: The yellow center line makes my lane the leftmost in this direction, and the
                        white lane line confirms another same-direction lane on the right. The classification
                        of the farther curbside strip is less certain, so the total lane count is tentative. |
                        roles: The solid yellow center line and solid white same-direction lane separator fit
                        their assigned roles. | markings: The stop line precedes the crosswalk. No directional
                        arrow, movement-prohibition marking, or left-turn waiting area is visible in my lane.
                        | unseen: The hood hides the nearest pavement, and the curbside strip's use is not
                        clearly identified; no unseen arrow or special-lane symbol has been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing into the
                        opposing-direction roadway.
Step 5  Rule            right_boundary: In China, a solid white lane-separation line prohibits changing lanes
                        across it.
Step 5  Rule            line:stop_line: When required to stop for intersection control, stop before this line.
Step 5  Rule            line:crosswalk: Yield to pedestrians using the crossing and do not stop on the
                        crossing.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white lane line prohibits crossing the
                        right boundary.
Step 6  go_straight     not_applicable: No visible directional arrow or prohibited-movement marking governs
                        this action.
Step 6  turn_left       not_applicable: No visible directional arrow or prohibited-movement marking governs
                        this action.
Step 6  turn_right      not_applicable: No visible directional arrow or prohibited-movement marking governs
                        this action.
Step 6  u_turn          not_applicable: No visible directional arrow or prohibited-movement marking governs
                        this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: both boundary-crossing actions are prohibited, while movements without
                        governing visible markings are not applicable rather than assumed permitted.
Advice                  Stay between the solid boundaries; do not change lanes in this approach. The visible
                        markings do not establish permitted intersection movements, so check applicable signs
                        and signals, stop before the stop line when required, and yield to pedestrians.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 4505, out 1213, 23.38 s

culane_test__d193_06051123_0635_00900 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A two-way urban road in China curves gently left ahead, with no intersection or lane
                        ending visible. My car is in the single visible motor-vehicle lane in its direction,
                        between a yellow center line and a white roadside edge line. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane, with opposing traffic space
                        beyond it; no curb forms this boundary.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, with a paved roadside strip
                        beyond it and a raised sidewalk curb farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and edge line on the right agree with my car
                        occupying the only motor-vehicle lane in its direction. | roles: The solid yellow line
                        fits separation of opposing traffic; the solid white line fits the roadway edge beside
                        the roadside strip. | markings: No arrows, words, symbols, transverse lines or waiting
                        areas are visible in my lane. | unseen: No unseen intersection layout or markings
                        beyond the visible road are inferred; the sidewalk curb is beyond, not on, my lane
                        boundary. | result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing into the
                        opposing side for overtaking or other lateral movement.
Step 5  Rule            right_boundary: In China, a solid white roadway edge line must not ordinarily be
                        crossed to leave the motor-vehicle travel lane.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits ordinary movement across the
                        right boundary.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the center line governs lateral crossing here, not an unseen intersection
                        movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Follow the lane around the gentle bend without crossing either solid boundary. No
                        intersection movement guidance or stopping line is visible; assess turn permissions
                        when an intersection comes into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 836, 14.16 s

culane_test__d193_06051123_0635_00990 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road in China continues ahead, with no clearly visible intersection
                        or lane ending. The car is in the leftmost of two visible lanes in its direction,
                        beside the yellow centre line. (lanes 2, mine 1, full)
Step 2  Left            A single yellow broken line, with visible long painted segments and gaps, separates
                        this lane from opposing traffic; no curb forms this boundary.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A white broken line, with visible painted segments and gaps, separates this lane from
                        another lane on the right; the roadside curb lies beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The centre line on the left and lane line on the right agree with being lane
                        1 of two same-direction lanes. | roles: The yellow broken centre line separates
                        opposing directions, and the white broken lane line separates same-direction lanes. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are visible in
                        this lane. | unseen: No movement restrictions or distant intersection markings have
                        been inferred from features that cannot be seen. | result: consistent
Step 5  Rule            left_boundary: In China, a broken yellow centre line permits crossing for overtaking
                        or avoidance when safe and without interfering with opposing traffic.
Step 5  Rule            right_boundary: A broken white lane line permits changing into the adjacent same-
                        direction lane when safe.
Step 6  change_left     allowed (correct): The broken yellow centre line permits crossing when safe, but the
                        space beyond carries opposing traffic.
Step 6  change_right    allowed (correct): The broken white lane line permits a safe change into the lane on
                        the right.
Step 6  go_straight     not_applicable: No marking in view governs this movement.
Step 6  turn_left       not_applicable: No marking in view governs this movement.
Step 6  turn_right      not_applicable: No marking in view governs this movement.
Step 6  u_turn          not_applicable: No marking in view governs this movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Keep to the right of the yellow centre line unless safely crossing it for a permitted
                        manoeuvre; it is not another same-direction lane. A safe lane change to the right is
                        permitted, but no visible arrows establish turn permissions at an upcoming junction.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 868, 16.29 s

culane_test__d193_06051123_0635_01980 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road in China approaches an intersection. There are three lanes in this
                        direction, and my car is in the middle lane. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible in the middle of my
                        lane, with one forward-pointing head and no turning branch.
Step 4  Cross-check     position: The middle position among three same-direction lanes agrees with a lane line
                        and an adjacent same-direction lane on each side. | roles: Both white solid boundaries
                        fit same-direction lane separation on an intersection approach. | markings: The
                        straight-only arrow agrees with a through lane bounded by solid lane lines; arrows in
                        adjacent lanes do not govern my lane. | unseen: No distant stop line, crosswalk, or
                        waiting-area detail is claimed; the far intersection pavement is too small to read
                        reliably. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white same-direction lane divider prohibits crossing
                        it to change lanes to the left.
Step 5  Rule            right_boundary: In China, a solid white same-direction lane divider prohibits crossing
                        it to change lanes to the right.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left lane divider prohibits
                        crossing to the left.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right lane divider prohibits
                        crossing to the right.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits this movement.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight, subject to the intersection signals and
                        traffic; do not cross either solid divider. For a turn, select the appropriately
                        marked lane before the solid-line section, and identify the stop line as you approach
                        because it is not readable here.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 993, 18.0 s

culane_test__d193_06051123_0635_02160 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road in China approaches a signal-controlled intersection. My car is in
                        the rightmost approach lane, beside a hatched roadside island; the total number of
                        same-direction lanes cannot be counted confidently at the cropped left edge. (lanes
                        None, mine None, insufficient)
Step 2  Left            A continuous white solid line separates my lane from another same-direction lane on
                        the left; no curb lies along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line curves along the right side of my lane, with white
                        diagonal hatching beyond it and a raised landscaped island farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white arrow has a single head pointing right, connected to a
                        bent shaft.; line:stop_line (full): A transverse white stop line crosses the lane
                        immediately before the pedestrian crossing.; line:crosswalk (full): White zebra-
                        crossing stripes extend across the approach ahead of the stop line.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to my left, and the
                        right edge line confirms that my lane is rightmost; the cropped view prevents a
                        reliable total count or numerical lane index. | roles: The white solid left lane
                        separator and white solid right roadway edge fit their assigned roles. | markings: The
                        right-only arrow agrees with the rightmost approach position; the stop line and
                        crosswalk do not add permitted movement directions. | unseen: No lane count is
                        inferred beyond the visible coverage, and the island curb is not treated as the
                        immediate lane boundary. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: The solid roadway edge beside the channelized island must not be
                        crossed to drive into the hatched area.
Step 5  Rule            arrow:right: The right-only lane-use arrow permits a right turn and excludes straight,
                        left-turn and U-turn movements from this lane.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before this line.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires yielding to pedestrians and must not
                        be obstructed.
Step 6  change_left     prohibited (correct): The solid white lane separator prohibits crossing to the left.
Step 6  change_right    prohibited (correct): The solid right edge borders a channelized island and prohibits
                        moving across into it.
Step 6  go_straight     prohibited (correct): The right-only arrow excludes going straight.
Step 6  turn_left       prohibited (correct): The right-only arrow excludes turning left.
Step 6  turn_right      allowed (correct): The single right-turn arrow permits turning right.
Step 6  u_turn          prohibited (correct): The right-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a right turn only; do not cross either solid boundary or enter the
                        hatched island. Obey the applicable signals, stop before the stop line when required,
                        and yield to pedestrians and cyclists crossing your path.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4505, out 1403, 28.83 s

culane_test__d193_06051123_0635_03690 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road in China approaches a broad signal-controlled intersection. My
                        car is in the straight-ahead lane, with a left-turn lane on its left and a right-turn
                        lane on its right; the far-right roadway division is less clear. (lanes None, mine 2,
                        partial)
Step 2  Left            A continuous white boundary, with a closely parallel white stripe visible beside it,
                        separates my lane from the lane bearing a left-turn arrow; there is no curb.
                        white double_solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs from beside the hood toward the intersection, separating my
                        lane from the lane bearing a right-turn arrow; there is no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in the middle of my lane has one head pointing
                        straight ahead.; line:stop_line (full): A transverse white stop line crosses my lane
                        just before the pedestrian crossing.; line:crosswalk (full): White zebra-crossing
                        stripes extend across the road immediately beyond the stop line.
Step 4  Cross-check     position: The lane lines on both sides agree with having another same-direction lane
                        on each side. My lane is second from the left; the complete count toward the far right
                        is uncertain. | roles: The white solid longitudinal boundaries fit same-direction lane
                        separators on an intersection approach. | markings: The straight-only arrow agrees
                        with a dedicated approach lane bounded by solid white lines. The neighboring turn
                        arrows are outside my lane. | unseen: No total lane count is asserted because the far-
                        right roadway division is unclear. | result: consistent
Step 5  Rule            left_boundary: In China, the solid white lane boundary prohibits crossing it to change
                        into the lane on the left.
Step 5  Rule            right_boundary: In China, the solid white lane boundary prohibits crossing it to
                        change into the lane on the right.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before this line.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires yielding to pedestrians and keeping
                        the crossing unobstructed.
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits this movement.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, subject to the traffic signal and crossing
                        traffic; do not cross either solid boundary to reach a turn lane. Stop before the stop
                        line when required and yield to pedestrians at the crosswalk.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4505, out 1399, 27.64 s

culane_test__d193_06051411_0691_03960 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road in China continues ahead with a central metal fence separating opposing
                        traffic and parked vehicles along the shops on the right. My car is in the leftmost of
                        two apparent same-direction lanes; the lane divider is faint. (lanes 2, mine 1,
                        partial)
Step 2  Left            A continuous white line runs beside the central metal fence, with a yellow strip
                        farther left beneath the fence; opposing traffic is beyond the fence.
                        white solid, curb yes, center_line, evidence full
Step 2  Right           Faint, worn white longitudinal segments with intervening gaps separate my lane from
                        the roadway to its right; no physical divider is visible along these segments.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The central fence on the left places my lane leftmost; the faint divider on
                        the right is consistent with a second same-direction lane. | roles: The physical
                        central separator establishes the left boundary's role despite the nearest paint being
                        white; the worn broken white marking on the right fits a lane divider. | markings: No
                        readable arrows, words, symbols, waiting areas or transverse lines are visible in my
                        lane. | unseen: The lane count remains tentative because the right divider is worn; no
                        intersection layout or markings beyond the visible stretch are inferred. | result:
                        consistent
Step 5  Rule            left_boundary: In China, the central physical separator must not be crossed, so
                        leaving the lane to the left is prohibited.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 6  change_left     prohibited (correct): The central physical fence prohibits crossing the left boundary.
Step 6  change_right    allowed (correct): The visible broken white lane divider permits a safe lane change to
                        the right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Keep clear of the central fence and cross the worn right-hand divider only after
                        confirming the adjacent lane is clear, watching for parked vehicles pulling out. No
                        visible intersection arrows establish a turning lane or turning permission.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 968, 20.36 s

culane_test__d193_06051603_0727_01080 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane right-hand branch of a divided urban road, with a painted
                        splitter and physical divider separating it from the parallel carriageway on the left.
                        The branch continues ahead; no intersection or lane ending is visible. (lanes 1, mine
                        1, full)
Step 2  Left            A solid white line borders a tapered area of white diagonal hatching on the left,
                        which leads to a physical divider; parallel traffic lanes lie beyond.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A concrete barrier forms the right edge of the branch, with a narrow dusty strip at
                        its base and no distinct painted boundary line visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The branch has one lane, so the car is both leftmost and rightmost; roadway
                        edges on both sides agree with that position. | roles: The white solid line borders
                        the painted splitter rather than an adjacent usable lane, while the concrete barrier
                        forms the right roadway edge. | markings: No arrows, words, symbols or transverse
                        lines are visible within the lane; the diagonal hatching lies outside its left
                        boundary. | unseen: No lane-use arrow, intersection, stop line or waiting area has
                        been inferred beyond the visible stretch. | result: consistent
Step 5  Rule            left_boundary: In China, the solid boundary of the channelizing splitter must not be
                        crossed to leave this branch or enter the hatched area.
Step 5  Rule            right_boundary: The concrete roadway barrier is not a traversable boundary, so moving
                        out of the lane across it is prohibited.
Step 6  change_left     prohibited (correct): The solid white splitter boundary prohibits crossing into the
                        channelizing area.
Step 6  change_right    prohibited (correct): The concrete barrier prohibits leaving the lane to the right.
Step 6  go_straight     not_applicable: No visible lane-use or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: both lateral departures are prohibited by their boundaries, and no
                        intersection movement permission is inferred from the absence of lane-use markings.
Advice                  Stay within this branch, keeping right of the solid splitter boundary and clear of the
                        concrete barrier. No turn assignment or stopping point is visible; follow subsequent
                        signs and markings as they become readable.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 934, 19.77 s

culane_test__d193_06051603_0727_01620 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           My car is on a single-lane elevated ramp curving left, with concrete barriers on both
                        sides. No intersection or lane ending is visible ahead. (lanes 1, mine 1, full)
Step 2  Left            A pale yellow solid line follows the left edge beside a concrete barrier topped by a
                        metal guardrail; another elevated roadway lies beyond.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white edge line follows the foot of the concrete barrier on the right, with no
                        adjacent travel lane.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane, bounded by roadway edges on both sides, agrees with my car being
                        in lane 1. | roles: Both solid lines follow physical roadway edges rather than
                        separating travel lanes. | markings: There are no visible arrows, words, symbols or
                        transverse markings to conflict with the boundaries. | unseen: No markings or
                        intersection geometry beyond the visible curve have been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The solid roadway edge and concrete barrier prohibit leaving the ramp
                        across the left boundary.
Step 5  Rule            right_boundary: The solid roadway edge and concrete barrier prohibit leaving the ramp
                        across the right boundary.
Step 6  change_left     prohibited (correct): The left solid edge line and concrete barrier prohibit crossing
                        out of the lane.
Step 6  change_right    prohibited (correct): The right solid edge line and concrete barrier prohibit crossing
                        out of the lane.
Step 6  go_straight     not_applicable: No marking governs this action; following the ramp's curve is not an
                        intersection movement.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the single ramp lane and follow its leftward curve; do not cross either
                        edge. The left-pointing chevron signs reinforce the curve, and no stop line is
                        visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 786, 14.65 s

culane_test__d193_06051734_0757_00000 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided expressway in China continues straight, with no visible intersection, ramp
                        or lane ending. My car is in the middle of three lanes travelling in this direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A white broken line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and a middle-lane position agree with a same-direction lane line
                        on each side. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No visible arrows, words, symbols, transverse lines or marked
                        waiting areas conflict with the boundaries. | unseen: No unseen intersection markings
                        or distant lane-end features have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a white broken lane divider permits crossing to the adjacent
                        lane when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a white broken lane divider permits crossing to the adjacent
                        lane when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The white broken lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay in the middle lane to continue along the expressway; either broken divider may be
                        crossed after signalling and checking for a safe gap. No turn guidance or stopping
                        point is visible, and the absence of turn markings does not authorize turning or
                        making a U-turn on the expressway.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 772, 11.19 s

culane_test__d193_06051734_0757_02430 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided expressway in China continues straight ahead, with no visible intersection,
                        ramp or lane ending. My car is in the middle of three lanes travelling in this
                        direction. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible dashes and gaps ahead, separates my lane from
                        another same-direction lane on the right; its nearest section is obscured by the hood,
                        and no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lane-line boundaries place my lane between a lane on either side,
                        consistent with lane 2 of 3. | roles: Both white broken boundaries fit same-direction
                        lane separators. | markings: No guidance markings are visible in my lane; the
                        transverse pavement seam is not a painted stop line. | unseen: No markings beneath the
                        hood or beyond the visible road have been inferred; the visible stretches establish
                        both boundary patterns. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane separator permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue along the expressway in your lane; either broken white boundary may be
                        crossed for a safe lane change after checking traffic and signalling. No intersection,
                        turning guidance or stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 804, 12.42 s

culane_test__d193_06051734_0757_04050 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A single-lane ramp curves right toward an overpass, with guardrails on both sides. My
                        car occupies the only lane; no intersection or lane ending is visible. (lanes 1, mine
                        1, full)
Step 2  Left            A continuous white solid line follows the left edge of the lane, with a narrow paved
                        strip and a raised concrete edge supporting a guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white solid line follows the right edge of the lane, with a paved
                        shoulder and a raised concrete edge supporting a guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane with roadway edge lines on both sides agrees with my lane being
                        both the leftmost and rightmost lane. | roles: Both white solid lines border roadside
                        strips and guardrails rather than adjacent traffic lanes, consistent with edge lines.
                        | markings: No guidance markings are visible within the lane; there are no conflicting
                        arrows, words or waiting areas. | unseen: No markings or intersection layout beyond
                        the visible bend have been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white roadway edge line restricts ordinary crossing onto the
                        roadside strip, and the physical roadside barrier is not traversable.
Step 5  Rule            right_boundary: The solid white roadway edge line restricts ordinary crossing onto the
                        shoulder, which is not an additional travel lane.
Step 6  change_left     prohibited (correct): The solid left roadway edge line and physical roadside edge
                        prohibit an ordinary move out of the lane.
Step 6  change_right    prohibited (correct): The solid right roadway edge line restricts ordinary movement
                        onto the shoulder.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid white edge lines and follow the ramp's right-hand curve,
                        adjusting speed for the bend and limited visibility. The roadside chevrons reinforce
                        the curve; no intersection movement or stopping point is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 863, 15.55 s

culane_test__d193_06060642_0768_00360 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road continues straight ahead, with no clearly visible intersection or lane
                        ending. My car is in the rightmost of two lanes in this direction, alongside a
                        landscaped roadside strip. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line runs along the right edge of my lane, with a narrow paved margin
                        and a raised landscaped curb beyond it.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider and right roadway edge agree with my lane being lane 2
                        of 2. | roles: The white dashed left line separates same-direction lanes; the white
                        dashed right line marks the roadway edge beside a narrow margin. | markings: No
                        arrows, words, symbols, waiting areas, or transverse markings are discernible in my
                        lane. | unseen: No movement designation or intersection marking is inferred from the
                        distant roadway. The curb beyond the right edge line is not treated as the lane
                        boundary itself. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe.
Step 5  Rule            right_boundary: In China, a broken white roadway edge line permits temporary crossing
                        where necessary and safe, but does not authorize driving over the curb beyond it.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white edge line permits temporary
                        crossing into the paved margin, not crossing the curb beyond it.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue within the lane; you may change left across the dashed divider when safe. The
                        right dashed edge is not another traffic lane: cross it only temporarily when
                        necessary, and do not mount the curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 4505, out 987, 20.63 s

culane_test__d193_06060642_0768_00900 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road curves gently right, with no intersection or lane ending clearly
                        visible ahead. My car is in the rightmost of two lanes in its direction. (lanes 2,
                        mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line follows the right edge of my lane beside a raised curb, with
                        planted vegetation beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my lane
                        being lane 2 of 2. | roles: The broken white divider fits a same-direction lane line,
                        and the solid white line beside the curb fits a roadway edge. | markings: No guidance
                        markings are visible within my lane, so none conflict with the boundaries. | unseen:
                        No unseen arrows or intersection markings have been inferred; the next intersection is
                        outside the clearly visible stretch. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge and raised curb prohibit an ordinary lane
                        change out of the roadway on this side.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (correct): The solid roadway edge and raised curb prohibit leaving the lane
                        to the right.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Follow the gentle right bend within your lane; change left across the broken divider
                        only when safe, and do not cross the right edge or curb. No visible lane-use arrows
                        establish which lane to use for turns at the next intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 737, 11.59 s

culane_test__d193_06060642_0768_03060 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China runs beside an elevated roadway, with a junction farther
                        ahead. My car is in the rightmost of three same-direction traffic lanes. (lanes 3,
                        mine 3, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from the
                        lane occupied by the green bus; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved roadside strip and
                        a raised sidewalk curb farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (partial): A small white bent arrow ahead in my lane has a head pointing
                        right; its details are reduced by distance.
Step 4  Cross-check     position: The lane line on the left and roadway edge line on the right agree with my
                        lane being third from the left and rightmost. | roles: The broken white separator fits
                        a same-direction lane line; the continuous white line beside the roadside strip fits
                        an edge line. | markings: The visible right-pointing arrow is compatible with the
                        rightmost lane, but its distant details limit certainty about whether it has another
                        head. | unseen: No stop line or waiting area is identifiable, and the distant arrow is
                        not treated as conclusively excluding an additional movement. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A solid white roadway edge line must not ordinarily be crossed to
                        drive onto the roadside strip.
Step 5  Rule            arrow:right: A right-pointing lane-use arrow permits a right turn; other movements are
                        excluded only if the complete arrow confirms that no additional direction is shown.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe lane change left.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits an ordinary crossing onto
                        the roadside strip.
Step 6  go_straight     not_determined: The distant arrow is not clear enough to establish whether it also has
                        a straight-ahead head.
Step 6  turn_left       not_determined: The arrow's complete set of heads cannot be confirmed at this
                        distance.
Step 6  turn_right      allowed: The visible right-pointing arrowhead permits a right turn.
Step 6  u_turn          not_determined: The arrow's complete set of heads cannot be confirmed at this
                        distance.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Keep within the solid right edge line; a left lane change is possible across the
                        broken line only when clear of the bus and other traffic. The visible arrow supports a
                        right turn, but confirm its complete shape and the junction controls before choosing
                        another movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1116, 23.56 s

culane_test__d193_06060748_0790_02970 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad, divided urban roadway in China carries several lanes of same-direction
                        traffic. My car is behind the red hatchback in the middle lane; no intersection or
                        lane ending is clearly visible ahead. (lanes 5, mine 3, full)
Step 2  Left            A white broken line lies immediately left of my lane, with a long painted dash and a
                        gap visible; another same-direction traffic lane lies beyond, with no curb at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line lies immediately right of my lane, with a long painted segment
                        ending before the foreground gap; another same-direction lane occupied by the cream
                        minibus lies beyond, with no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 3 of 5 has same-direction lanes on both sides, consistent with both
                        boundaries being lane lines. | roles: The white broken boundaries are consistent with
                        separators between same-direction traffic lanes. | markings: No arrows, words,
                        symbols, transverse lines, or waiting areas are visible in my lane. | unseen: Traffic
                        obscures portions of the road ahead; no unseen junction, lane-use arrow, or waiting
                        area has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The broken white left lane line permits a safe lane change.
Step 6  change_right    allowed (correct): The broken white right lane line permits a safe lane change.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the broken boundaries permit lane changes, while no visible marking
                        determines an intersection movement or waiting-area entry.
Advice                  Remain in your lane unless a lane change is needed; either broken boundary may be
                        crossed only after checking for a safe gap in the heavy traffic. No visible markings
                        establish a turn lane or stopping point, so reassess when the road ahead becomes
                        visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1065, 22.73 s

culane_test__d193_06060919_0820_00450 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way street in China continues ahead, with parked cars along the right
                        side and oncoming traffic to the left. My car is in the single visible through lane of
                        its direction; no intersection or lane end is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A faded yellow line runs along the left of my lane, with opposing traffic beyond it;
                        wear and the short visible stretch make its solid-versus-broken pattern uncertain.
                        yellow none, curb no, center_line, evidence partial
Step 2  Right           No painted boundary is clearly visible on the right; the raised roadside curb is
                        visible in places, with parked cars obscuring much of its continuation.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and roadside edge on the right agree with one
                        visible lane in my direction and my lane being leftmost. | roles: Yellow paint and
                        opposing traffic support the center-line role; the raised roadside curb supports the
                        right-edge role. | markings: No readable guidance markings appear in my lane. |
                        unseen: The yellow line's pattern cannot be established reliably, and parked cars
                        obscure portions of the right edge and distant roadway; no hidden arrows or
                        intersection markings are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing, while a broken
                        yellow center line permits crossing when safe; the uncertain pattern prevents deciding
                        whether crossing here is permitted.
Step 5  Rule            right_boundary: The raised roadside curb is a physical roadway boundary and must not
                        be crossed as a lane-change maneuver.
Step 6  change_left     not_determined (WRONG, label allowed): The yellow center-line pattern is unclear, so
                        its crossing permission cannot be determined.
Step 6  change_right    prohibited (correct): The raised roadside curb prohibits leaving the roadway across
                        this boundary.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in the current lane rather than crossing the uncertain yellow center line or
                        the right curb. Watch for pedestrians, scooters and parked vehicles; no visible
                        intersection markings establish turning permissions or a stopping location.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 948, 19.29 s

culane_test__d193_06060925_0822_01260 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road runs beside and beneath an elevated structure, with no
                        intersection or lane ending visible ahead. My car is in the rightmost of three lanes
                        traveling in this direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line follows the right roadway edge, with a narrow gutter, raised
                        curb and metal pedestrian fence immediately beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my car
                        occupying lane 3 of 3. | roles: The broken white divider fits a same-direction lane
                        line, and the solid white line alongside the curb fits a roadway edge line. |
                        markings: No guidance arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No intersection layout or markings beyond the visible
                        stretch have been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The roadway edge and raised curb do not permit a normal lane-change
                        movement onto the fenced roadside.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The raised curb and fenced roadway edge prohibit moving out of
                        the lane to the right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain within the right roadway edge; you may change left across the broken white line
                        after checking traffic. No visible markings establish turn permissions or a stopping
                        position at a next intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 854, 15.68 s

culane_test__d193_06060925_0822_02700 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban boulevard in China continues straight ahead, with no intersection or
                        lane ending clearly visible. My car is in the third of four same-direction lanes,
                        counted from the left. (lanes 4, mine 3, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the right; the solid roadside line and curb lie beyond that
                        adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four same-direction lanes and an ego position of third from the left agree
                        with ordinary lane lines on both sides: two lanes lie to the left and one to the
                        right. | roles: Both boundaries are white broken lines, consistent with separation of
                        same-direction traffic. | markings: No readable guidance arrows, words, symbols,
                        waiting areas, or transverse markings appear in my lane. | unseen: No distant
                        intersection layout or markings beyond the readable stretch have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may change lanes across either broken white divider after checking surrounding
                        traffic and signaling. No visible marking assigns intersection movements here; follow
                        the lane arrows, signs, and signals when they become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 880, 15.11 s

culane_test__d193_06060925_0822_04140 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China has three lanes in this direction, with an overpass
                        ahead. My car is in the rightmost lane beside the roadside curb. (lanes 3, mine 3,
                        full)
Step 2  Left            A white broken line, with a long dash and a clear gap visible, separates my lane from
                        another same-direction lane on the left; there is no curb here.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A faint continuous white line follows the right side of my lane alongside a raised
                        roadside curb, with a sidewalk and railing beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.
Step 4  Cross-check     position: Three lanes and position 3 agree with a same-direction lane line on the left
                        and a roadway edge on the right. | roles: The broken white left line fits a same-
                        direction lane separator; the continuous white right line and curb fit the roadway
                        edge. | markings: The straight-only arrow is consistent with this through lane; no
                        other guidance marking is readable in my lane. | unseen: No distant stop line, waiting
                        area, or additional arrow has been inferred from the road beyond the readable stretch.
                        | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane separator permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: The solid white roadway edge and raised curb prohibit an ordinary lane
                        change or departure across this side.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires proceeding straight from this
                        lane rather than turning left, turning right, or making a U-turn.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid roadway edge and raised curb prohibit leaving the lane
                        to the right.
Step 6  go_straight     allowed (correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken line when safe. For a
                        turn or U-turn, first find an appropriately marked lane; do not cross the right edge
                        or curb.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 965, 17.76 s

culane_test__d193_06060925_0822_04320 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues straight beneath a pedestrian footbridge,
                        with a bus stop along the right curb. My car is to the right of two apparent through
                        lanes; the curbside paved strip may be a bus bay rather than another continuous
                        traffic lane. (lanes None, mine 3, partial)
Step 2  Left            A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           Broad white broken segments separate my lane from a paved curbside strip beside the
                        bus stop; the raised sidewalk curb lies beyond that strip, not directly at this
                        boundary.
                        white dashed, curb no, unknown, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line agrees with same-direction lanes to my left. Whether the
                        curbside strip counts as another lane cannot be established confidently, so the total
                        lane count is left unspecified. | roles: The white broken left boundary fits a same-
                        direction lane divider. The right boundary is visibly broken and white, but its lane-
                        divider versus bus-bay-edge role is uncertain. | markings: No guidance marking is
                        readable within my lane. The visible directional arrow to the left lies beyond my left
                        boundary and does not govern my lane. | unseen: No direction arrow, special-lane
                        designation, intersection stop line, or waiting area has been inferred where none is
                        visible. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A broken white boundary does not itself prohibit crossing, but the
                        uncertain function of the curbside strip prevents establishing whether my car may
                        enter it.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    not_determined (WRONG, label prohibited): The curbside strip's function and any
                        special-use restriction are not established by the visible boundary.
Step 6  go_straight     not_applicable: No marking in my lane governs this movement.
Step 6  turn_left       not_applicable: No marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the current lane; change left across the broken divider only when safe. Do
                        not assume the curbside bus-stop strip is available for ordinary driving, and confirm
                        lane-use markings before choosing a turning lane farther ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1332, 32.96 s

culane_test__d193_06060925_0822_04680 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues straight ahead, with a landscaped divider on
                        the left and a landscaped roadside strip on the right. My car is in the rightmost of
                        three same-direction lanes; no intersection stop line is visible ahead. (lanes 3, mine
                        3, full)
Step 2  Left            A single white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right edge of my lane, with a narrow paved
                        margin and a raised landscaped curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A worn white arrow directly ahead of the hood has one head
                        pointing straight forward, with no visible turning branch.
Step 4  Cross-check     position: Three same-direction lanes and ego lane index 3 agree with a lane divider on
                        the left and a roadway edge on the right. | roles: The broken white left boundary fits
                        a same-direction lane divider; the solid white right boundary and roadside curb fit a
                        roadway edge. | markings: The straight-only arrow agrees with the continuing through
                        lane; no words, waiting areas or conflicting markings are visible in my lane. |
                        unseen: No hidden marking or distant intersection layout has been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider may be crossed to
                        change lanes when safe.
Step 5  Rule            right_boundary: The solid white roadway edge and raised curb do not permit an ordinary
                        lane change out of the roadway on the right.
Step 5  Rule            arrow:straight: A straight-only guidance arrow requires traffic using this lane to
                        proceed straight rather than turn left, turn right or make a U-turn.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing into the adjacent
                        lane when safe.
Step 6  change_right    prohibited (correct): The solid white roadway edge and raised curb prohibit leaving
                        the lane to the right.
Step 6  go_straight     allowed: The straight-only arrow permits proceeding straight.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to continue straight; do not turn from it or cross the right edge.
                        For another movement, change left across the broken divider only when safe and select
                        a lane whose markings permit that movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 4505, out 995, 17.5 s

culane_test__d193_06060925_0822_05310 | lane | Test A | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road in China has three visible lanes in this direction, with a
                        planted median on the left and a raised separator beside a parallel roadway on the
                        right. My car is in the rightmost lane; no intersection or lane ending is clearly
                        visible ahead. (lanes 3, mine 3, full)
Step 2  Left            A worn white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white solid line runs along the right of my lane, with a narrow paved margin and a
                        raised curb beyond it; diagonal hatching farther ahead lies outside my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and an ego position of 3 agree with a same-direction lane line
                        on the left and a roadway edge line on the right. | roles: The broken white separator
                        fits a lane line, and the solid white line beside the paved margin fits an edge line.
                        | markings: No guidance marking is readable inside my lane; the hatching to the right
                        is outside its boundary. | unseen: No distant intersection layout or hidden lane-use
                        arrow has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane line permits crossing to change lanes
                        when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: A solid white roadway edge line must not be crossed for ordinary lane
                        changing or driving onto the roadside margin.
Step 6  change_left     allowed (correct): The broken white lane line permits a safe lane change to the left.
Step 6  change_right    prohibited (correct): The solid white roadway edge line prohibits ordinary crossing
                        onto the roadside margin.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay inside the right edge line; a left lane change is permitted only after checking
                        traffic and clearance. No visible marking establishes turn permissions here, so follow
                        the lane guidance as it becomes visible ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 888, 15.42 s

culane_test__d37_05181608_0235_03090 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban road approaches a signal-controlled intersection in China. My car follows a
                        taxi in the rightmost visible motor-vehicle approach lane, with a painted channelizing
                        area on the left and a fence separating the right-side non-motorized space. (lanes
                        None, mine None, insufficient)
Step 2  Left            A solid white diagonal line borders a white-chevron channelizing area on the left; a
                        large yellow traffic barrel stands farther left, while vehicles obscure the more
                        distant lane layout.
                        white solid, curb no, other, evidence full
Step 2  Right           A solid white line runs beside a low white metal fence on the right, with cyclists and
                        non-motorized space beyond the fence.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A transverse white stopping line is visible to the right of
                        the taxi near the intersection; the taxi hides its continuation across my lane.;
                        line:crosswalk (partial): Broad white pedestrian-crossing stripes extend across the
                        approach ahead, partly hidden by the taxi and other road users.
Step 4  Cross-check     position: The right-side fence and edge line place my lane at the right edge of the
                        motor carriageway. The channelizing area on the left does not establish the number or
                        indexing of the other approach lanes. | roles: The solid white channelizing boundary
                        and the solid white boundary beside the non-motorized space fit their observed roles.
                        | markings: The stopping line and pedestrian crossing are consistent with the
                        intersection approach; no readable lane-use arrow is visible. | unseen: The taxi and
                        hood conceal substantial pavement in my lane, so a hidden directional arrow cannot be
                        ruled out. The complete same-direction lane count cannot be established. | result:
                        consistent
Step 5  Rule            left_boundary: In China, the solid boundary of a painted channelizing area prohibits
                        crossing into or driving through that area.
Step 5  Rule            right_boundary: The fence separating motor traffic from the adjacent non-motorized
                        space prohibits leaving this lane across the right boundary.
Step 5  Rule            line:stop_line: When required to stop for intersection control, the vehicle must stop
                        before the stopping line.
Step 5  Rule            line:crosswalk: Drivers must yield to pedestrians as required at the marked crossing
                        and must not stop on it.
Step 6  change_left     prohibited (correct): The solid white channelizing boundary prohibits crossing into
                        the painted exclusion area.
Step 6  change_right    prohibited (correct): The right-side fence prohibits crossing into the adjacent non-
                        motorized space.
Step 6  go_straight     not_determined: The taxi and hood conceal pavement where a lane-use arrow could
                        determine this movement.
Step 6  turn_left       not_determined: The taxi and hood conceal pavement where a lane-use arrow could
                        determine this movement.
Step 6  turn_right      not_determined: The taxi and hood conceal pavement where a lane-use arrow could
                        determine this movement.
Step 6  u_turn          not_determined: The taxi and hood conceal pavement where a directional or prohibited-
                        movement marking could determine this movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay between the channelizing boundary and the fence; neither side permits a lane
                        change here. Confirm the lane's directional markings as the taxi moves, obey the
                        traffic signals, and stop before the stopping line when required while keeping the
                        crossing clear.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4505, out 1239, 25.35 s

culane_test__d37_05181608_0235_03720 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A divided urban road in China continues straight, with no intersection or lane ending
                        visible. My car is in the leftmost of three apparent same-direction lanes, beside the
                        fenced central divider. (lanes 3, mine 1, partial)
Step 2  Left            A solid white line runs along the left side of my lane beside a raised central divider
                        and metal fence, with opposing traffic beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments with intervening gaps separate my lane from the adjacent
                        same-direction lane; vehicles obscure part of the boundary farther ahead.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left divider edge and right lane line place my car in the leftmost lane;
                        three lanes appear present, although traffic obscures portions of the farther-right
                        layout. | roles: The solid white line beside the physical median fits a carriageway
                        edge, and the broken white line separates same-direction lanes. | markings: No
                        guidance arrows, words, symbols, waiting areas or transverse markings are visible in
                        my lane. | unseen: No hidden markings have been inferred; the lane count and farther
                        portions of the right boundary remain partly obscured. | result: consistent
Step 5  Rule            left_boundary: The solid carriageway edge and raised central divider prohibit leaving
                        my lane across the left boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane line permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 6  change_left     prohibited (correct): The solid left edge and physical central divider prohibit
                        crossing.
Step 6  change_right    allowed (correct): The visible broken white lane line permits a safe lane change into
                        the adjacent lane.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the boundary decisions follow the visible boundary rules, while no
                        intersection movements are authorized or prohibited by unseen markings.
Advice                  Keep clear of the central divider; a rightward lane change is permitted across the
                        broken white line only after checking the nearby vehicles and finding a safe gap. No
                        visible arrows establish turn permissions, so reassess lane guidance when approaching
                        an intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 970, 20.99 s

culane_test__d37_05181608_0235_05220 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A wide urban road in China has several lanes of queued traffic approaching an
                        intersection. My car is behind the brown sedan; traffic and the cropped roadway edges
                        prevent a reliable count of all same-direction lanes or my lane's index. (lanes None,
                        mine None, insufficient)
Step 2  Left            A single continuous white painted line runs along the left of my lane, with same-
                        direction vehicles beyond it and no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single continuous white painted line runs along the right of my lane, with another
                        same-direction traffic lane beyond it and no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane lines show that my lane has same-direction lanes on both sides; the
                        total count and exact index remain uncertain. | roles: Both white solid boundaries are
                        consistent with same-direction lane-dividing lines on an intersection approach. |
                        markings: No guidance marking or transverse line is readable on the exposed pavement
                        in my lane; queued vehicles conceal much of the lane ahead. | unseen: No arrows, stop
                        line, or waiting area have been inferred beneath the vehicles or in the obscured
                        intersection approach. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes to the left.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes to the right.
Step 6  change_left     prohibited (correct): The solid white lane-dividing line prohibits crossing the left
                        boundary.
Step 6  change_right    prohibited (correct): The solid white lane-dividing line prohibits crossing the right
                        boundary.
Step 6  go_straight     not_determined: Vehicles obscure the lane ahead where a movement arrow could govern
                        straight travel.
Step 6  turn_left       not_determined: Vehicles obscure the lane ahead where a movement arrow or prohibited-
                        turn marking could govern a left turn.
Step 6  turn_right      not_determined: Vehicles obscure the lane ahead where a movement arrow or prohibited-
                        turn marking could govern a right turn.
Step 6  u_turn          not_determined: Vehicles obscure the lane ahead where a movement arrow or prohibited-
                        U-turn marking could govern a U-turn.
Step 6  enter_waiting_areanot_determined: The intersection approach ahead is obscured, so the presence and
                          accessibility of a marked left-turn waiting area cannot be determined.
Step 7  Reflect         consistent
Advice                  Remain between the solid white lines and do not change lanes across them. As traffic
                        advances, check the revealed lane arrows, stop line, and intersection signals before
                        choosing a movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 883, 17.16 s

culane_test__d37_05181608_0235_05340 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A wide urban road in China has closely queued traffic traveling in the same direction,
                        with an apparent signalized intersection ahead. My car is between two white lane
                        boundaries behind a maroon sedan; traffic obscures the full road width and the lane's
                        distant end. (lanes None, mine None, insufficient)
Step 2  Left            A white line appears continuous along the visible stretch on the left, with same-
                        direction vehicles beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white line appears continuous along the visible stretch on the right, with same-
                        direction vehicles beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Same-direction traffic lies on both sides, consistent with two lane-line
                        boundaries and an interior lane; the total lane count and exact index cannot be
                        established. | roles: White continuous lines are consistent with solid separators
                        between same-direction lanes. | markings: No guidance marking is readable in the
                        exposed portion of my lane; vehicles obscure much of the pavement ahead. | unseen: No
                        arrow, stop line, waiting area, or exact lane count has been inferred from the traffic
                        arrangement. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes to the left.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes to the right.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        neighboring lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        neighboring lane.
Step 6  go_straight     not_determined: Vehicles hide the pavement where a lane-use arrow could determine the
                        permitted movement.
Step 6  turn_left       not_determined: Vehicles hide the pavement where a lane-use arrow could determine the
                        permitted movement.
Step 6  turn_right      not_determined: Vehicles hide the pavement where a lane-use arrow could determine the
                        permitted movement.
Step 6  u_turn          not_determined: Vehicles hide the pavement where a directional or prohibited-movement
                        marking could govern a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines and do not change lanes across them. Wait until
                        lane-use markings and the intersection controls are clearly visible before choosing a
                        movement, and leave adequate space behind the sedan.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 867, 15.63 s

culane_test__d37_05181919_0299_02970 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road in China continues toward a distant intersection. My car is in
                        the rightmost of three same-direction motor-vehicle lanes, with roadside activity and
                        vehicles to the right. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line runs along my lane's right side; a roadside strip
                        containing a car and two-wheelers lies beyond it, with no curb at the line itself.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white forward-pointing arrow is painted in my lane
                        immediately behind the car ahead; its head and shaft are visible.
Step 4  Cross-check     position: Three same-direction lanes and position 3 agree with a lane divider on the
                        left and a roadway edge on the right. | roles: The broken white divider fits a same-
                        direction lane line; the solid white boundary fits the roadside edge. | markings: The
                        straight arrow is consistent with the continuing lane; no conflicting word, arrow or
                        waiting area is visible. | unseen: No hidden marking has been inferred; the car ahead
                        obscures part of the farther pavement, and the distant intersection markings cannot be
                        read. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when safe and without impeding other traffic.
Step 5  Rule            right_boundary: A solid white roadway edge line must not ordinarily be crossed to
                        leave the motor-vehicle lane for the roadside strip.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires continuing straight and does
                        not permit left turns, right turns or U-turns from this lane.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid white roadway edge prohibits ordinary crossing into
                        the roadside strip.
Step 6  go_straight     allowed (correct): The straight arrow permits continuing straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight, maintaining clearance from the car ahead and
                        roadside traffic. For another movement, find an appropriately marked lane before the
                        intersection; change left only when safe and do not cross the solid right edge.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 984, 18.16 s

culane_test__d37_05181919_0299_03120 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches a signal-controlled intersection. Three
                        same-direction lanes are visible, and my car is in the middle lane. (lanes 3, mine 2,
                        full)
Step 2  Left            A continuous white solid line separates my lane from the same-direction lane occupied
                        by the taxi on the left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from another same-direction lane on
                        the right; the roadside railing is beyond that adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A large white forward-pointing arrowhead is visible
                        immediately ahead, with its lower shaft obscured by the hood.; arrow:straight (full):
                        A smaller white straight-ahead arrow is visible farther ahead in the same lane.
Step 4  Cross-check     position: A lane line on each side agrees with my car being in lane 2 of 3. | roles:
                        Both white solid boundaries separate same-direction lanes and fit their lane-line
                        roles. | markings: The repeated straight arrows agree with each other; neither
                        boundary contradicts the straight-only guidance. | unseen: The nearest arrow's lower
                        shaft is hidden by the hood. Traffic obscures portions of the distant approach, so no
                        unseen stop line or crosswalk is asserted. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes left.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes right.
Step 5  Rule            arrow:straight: The straight-ahead lane-use arrow permits proceeding straight and
                        prohibits left turns, right turns and U-turns from this lane.
Step 5  Rule            arrow:straight: The repeated straight-ahead arrow confirms that this lane is for
                        straight movement only.
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing the left boundary.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing the right boundary.
Step 6  go_straight     allowed (correct): The straight-ahead arrows permit straight movement.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel and do not cross either solid white boundary.
                        Obey the signal ahead and stop behind the stop line when required, locating it as the
                        vehicles ahead clear the view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1065, 19.65 s

culane_test__d37_05190927_0395_02340 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road in China approaches an intersection, with a truck directly ahead
                        and other traffic to the right. My car is in the leftmost lane beside a planted
                        median; vehicles obscure the outer lanes and much of the intersection approach. (lanes
                        None, mine 1, partial)
Step 2  Left            A solid white line runs beside a raised planted-median curb on the left, with fencing
                        and opposing traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous white line separates my lane from same-direction traffic on the right;
                        its farther continuation is obscured by vehicles.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left establishes my lane as the leftmost, and the
                        lane line on the right separates it from another same-direction lane; the total lane
                        count remains obscured. | roles: The white line beside the median fits an edge line,
                        and the solid white separator on the right fits a same-direction lane line. |
                        markings: No guidance marking is readable in the exposed part of my lane; the truck
                        hides the pavement farther ahead. | unseen: No arrow, stop line, waiting area, or
                        total lane count has been inferred from the obscured pavement. | result: consistent
Step 5  Rule            left_boundary: The raised median forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            right_boundary: In China, a solid white same-direction lane separator prohibits
                        crossing it to change lanes.
Step 6  change_left     prohibited (correct): The raised median curb prohibits leaving the lane to the left.
Step 6  change_right    prohibited (correct): The visible solid white lane separator prohibits crossing to the
                        right.
Step 6  go_straight     not_determined: The truck obscures the approach pavement where a lane-use arrow could
                        govern this movement.
Step 6  turn_left       not_determined: The truck obscures the approach pavement where a lane-use arrow could
                        govern this movement.
Step 6  turn_right      not_determined: The truck obscures the approach pavement where a lane-use arrow could
                        govern this movement.
Step 6  u_turn          not_determined: The truck obscures any lane-use or prohibited-movement marking that
                        could decide this movement.
Step 6  enter_waiting_areanot_determined: The truck and distant traffic obscure the area ahead where a left-
                          turn waiting area might be marked.
Step 7  Reflect         consistent
Advice                  Remain between the median and the solid white separator; do not cross either boundary.
                        Leave enough space behind the truck to read the lane arrows and locate any stop line
                        before committing to an intersection movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 909, 15.99 s

culane_test__d37_05190927_0395_02430 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban road in China approaches a signalized intersection with a pedestrian
                        crossing. My car is in the leftmost of three same-direction lanes, beside a raised
                        traffic island. (lanes 3, mine 1, full)
Step 2  Left            A raised concrete island curb forms the left side of my lane; a pole obscures part of
                        it, and no continuous painted boundary can be established beside it.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A solid white line runs along the right side of my lane toward the intersection, with
                        another same-direction traffic lane beyond it.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; its lower shaft is hidden by the hood.; line:stop_line (full): A
                        transverse white stop line crosses my lane before the pedestrian crossing.;
                        line:crosswalk (full): Broad white zebra-crossing stripes extend across the roadway
                        ahead of the stop line.
Step 4  Cross-check     position: The island on the left and the lane divider on the right agree with my lane
                        being the leftmost of three same-direction lanes. | roles: The raised island is a
                        physical roadway edge; the white solid line separates same-direction lanes. |
                        markings: The visible straight arrowhead agrees with an intersection approach lane;
                        the stop line precedes the pedestrian crossing. | unseen: The arrow's lower portion is
                        hidden by the hood, and part of the left edge is obscured by the pole; no hidden paint
                        or additional arrowhead is asserted. | result: consistent
Step 5  Rule            left_boundary: The raised traffic-island curb prohibits leaving the lane across its
                        left side.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        excludes turns, although the hidden lower portion limits confirmation that this is the
                        complete arrow.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before the stop line.
Step 5  Rule            line:crosswalk: Drivers must yield to pedestrians using the crossing and must not
                        obstruct it.
Step 6  change_left     prohibited (correct): The raised island curb prohibits crossing the left boundary.
Step 6  change_right    prohibited (correct): The solid white lane divider prohibits crossing the right
                        boundary.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel.
Step 6  turn_left       not_determined (correct): The lower portion of the arrow is hidden, so a possible
                        additional directional branch cannot be excluded.
Step 6  turn_right      not_determined (correct): The lower portion of the arrow is hidden, so a possible
                        additional directional branch cannot be excluded.
Step 6  u_turn          not_determined (correct): The complete arrow is not visible, leaving any additional
                        U-turn guidance unconfirmed.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the visible straight arrowhead supports straight travel, while the
                        concealed remainder prevents definitive exclusion of additional arrow movements.
Advice                  Stay between the island and the solid white divider; the visible arrow supports
                        proceeding straight, but does not establish permission to turn. Obey the traffic
                        signal, stop before the stop line when required, and yield to pedestrians on the
                        crossing.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 1229, 21.5 s

culane_test__d37_05190927_0395_05220 | lane | Test A | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A narrow, tree-lined urban road carries opposing traffic on the left, with parked
                        vehicles along the right. My car is in the single visible through lane in its
                        direction; no intersection or lane ending is clearly visible ahead. (lanes 1, mine 1,
                        full)
Step 2  Left            A faded yellow line runs along the left of my lane, appearing continuous in the
                        exposed stretch; a cyclist and vehicles obscure its nearer portion, and opposing
                        vehicles lie beyond it.
                        yellow solid, curb no, center_line, evidence partial
Step 2  Right           Two parallel solid white lines run along the right of my lane, with parked vehicles
                        beyond them; the nearby SUV obscures part of this boundary, and no curb forms the
                        immediate lane boundary.
                        white double_solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One through lane in my direction agrees with a center line on the left and a
                        roadside parking boundary on the right. | roles: The yellow line separates opposing
                        traffic; the white lines separate the through lane from the roadside parking space
                        rather than another visible through lane. | markings: No readable arrows, words,
                        symbols, waiting areas, or transverse lines are visible in my lane. | unseen: The
                        obscured portions of both boundaries and the distant roadway are not treated as fully
                        observed; no unseen intersection markings are inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing into the
                        opposing side for a lane change or overtaking.
Step 5  Rule            right_boundary: The visible solid white roadside boundary is not a broken lane-change
                        opening and prohibits crossing it into the parking-side space in this stretch.
Step 6  change_left     prohibited (correct): The visible solid yellow center line prohibits crossing to the
                        left.
Step 6  change_right    prohibited (correct): The visible solid white roadside boundary prohibits crossing to
                        the right.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary decisions apply only to crossing the visible boundaries, and no
                        intersection movement permission is inferred from the absence of visible guidance
                        markings.
Advice                  Remain between the visible boundaries and slow down for the cyclist, opposing traffic,
                        and parked SUV. No turn guidance or stop line is readable ahead; reassess when the
                        road and any junction markings become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4505, out 931, 17.64 s
```
