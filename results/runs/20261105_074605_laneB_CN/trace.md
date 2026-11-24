# Reasoning of lane run 20261105_074605_laneB_CN

```text
culane_test__d100_05251207_0380_01410 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A straight, tree-lined road has three motor-vehicle lanes in this direction. My car is
                        in the rightmost lane, with a cyclist in the roadside strip beyond the right boundary;
                        no intersection or lane ending is clearly visible ahead. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with clearly visible dashes and gaps, separates my lane from
                        another motor-vehicle lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved roadside
                        strip and a cyclist beyond it; the raised sidewalk curb lies farther right, not at
                        this line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and position 3 agree with a same-direction lane line on the left
                        and a roadway edge line on the right. | roles: The broken white left line fits a
                        crossable lane separator; the solid white right line fits the edge adjoining the
                        roadside strip. | markings: No arrows, words, symbols, marked areas or transverse
                        lines are identifiable in my lane. | unseen: No distant intersection layout or hidden
                        guidance markings have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing to the adjacent lane on the
                        left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, except in
                        an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane separator permits a lane change under
                        CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
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
Advice                  Stay within the right solid edge line and leave clearance for the cyclist; changing
                        left across the broken line is permitted when safe. No visible markings establish turn
                        permissions or a stopping position, so reassess as the road ahead becomes clearer.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 880, 15.85 s

culane_test__d100_05251207_0380_02130 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, three-lane road continues ahead, with no intersection or lane ending
                        visible. My car is in the middle lane. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the roadside fence is beyond that lane, not at my lane
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and the middle-lane position agree with a same-direction lane
                        line on each side. | roles: Both boundaries are broken white lines, consistent with
                        crossable same-direction lane dividers. | markings: No arrows, text, symbols,
                        transverse lines or marked waiting areas are visible in my lane. | unseen: No hidden
                        markings or intersection movements have been inferred; the hood hides the closest
                        pavement and the distant road is not readable in detail. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the lane on the
                        left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the lane on the
                        right when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
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
Advice                  Continue in the middle lane; either broken divider may be crossed after checking
                        traffic and signaling. No visible marking specifies a turning lane or stopping point,
                        so reassess lane guidance as you approach any junction.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 774, 11.18 s

culane_test__d100_05251207_0380_02190 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues straight ahead; no
                        intersection or lane ending is visible. My car is in the middle lane. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line with long painted dashes and visible gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with long painted dashes and visible gaps separates my lane from
                        another same-direction lane on the right; the roadside curb lies beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with a same-direction lane across each boundary. | roles:
                        Both boundaries are broken white lines, consistent with crossable same-direction lane
                        lines. | markings: No arrows, words, symbols, transverse lines or marked waiting areas
                        are visible in my lane. | unseen: No markings or intersection features have been
                        inferred beyond the visible road. | result: consistent
Step 5  Rule            left_boundary: The broken white lane boundary permits changing to the lane on my left.
                        [CN-5.2.3] "On roads with two or more lanes in the same direction, the crossable lane
                        line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane boundary permits changing to the lane on my
                        right. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
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
Advice                  You may remain in the middle lane or cross either broken white boundary after checking
                        that it is safe. No visible markings assign intersection movements or a stopping
                        position; check the markings farther ahead before choosing a turn lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 791, 12.2 s

culane_test__d100_05251207_0380_02400 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues ahead; no
                        intersection or lane ending is clearly visible. My car is in the middle lane, with
                        vehicles in both adjacent lanes and parked vehicles farther right. (lanes 3, mine 2,
                        full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from the
                        lane occupied by the white van; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from the right-
                        hand lane occupied by the delivery tricycle; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with being in lane 2 of 3. | roles: Both
                        boundaries are broken white lines separating same-direction lanes, consistent with
                        their lane-line roles. | markings: No guidance arrows, words, symbols, transverse
                        lines or marked waiting areas are visible in my lane. | unseen: No distant
                        intersection layout or movement restriction has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to change into the lane on
                        the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane line permits my car to change into the lane on
                        the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible marking governs this movement.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may cross either broken lane line when safe, but check carefully for the van on
                        the left and the delivery tricycle on the right. No visible arrows determine the lane
                        to use for a future turn, and no stopping line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 820, 12.86 s

culane_test__d100_05251207_0380_03270 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with no intersection or lane
                        ending clearly visible. My car is in the rightmost of three lanes travelling in this
                        direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line borders my lane on the right, with a paved roadside
                        strip and then a raised sidewalk curb beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 3 agree with a lane line on the left
                        and a roadway edge line on the right. | roles: The broken white line fits a crossable
                        same-direction lane separator; the solid white line fits the right roadway edge. |
                        markings: No arrows, text, symbols, transverse lines or marked waiting areas are
                        visible in my lane. | unseen: No unseen lane-use marking or distant intersection
                        layout has been inferred; the curb lies beyond the right edge line rather than forming
                        the immediate lane boundary. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to change into the adjacent
                        lane on the left. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the
                        roadside strip, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
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
Advice                  Remain inside the solid right edge line; a left lane change is permitted by the broken
                        line when safe. No visible pavement arrows assign intersection movements, so follow
                        upcoming lane guidance and signs rather than assuming this lane permits a particular
                        turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 923, 15.83 s

culane_test__d100_05251222_0385_01140 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided multilane urban road continues ahead beside an elevated structure, with no
                        intersection or lane ending visible. My car is in the leftmost of three lanes
                        travelling in this direction. (lanes 3, mine 1, full)
Step 2  Left            A single solid white line runs along the left edge of my lane beside a raised curb and
                        a metal guardrail, with vegetation beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my lane
                        being lane 1 of 3. | roles: The broken white right boundary fits a same-direction lane
                        line. The left boundary is visibly white despite being a left edge, which differs from
                        the yellow left-edge convention in CN-5.4.3; its physical position beside the curb and
                        guardrail establishes its edge role. | markings: No arrows, words, symbols, transverse
                        lines or marked waiting areas are visible in my lane. | unseen: No intersection
                        movements or markings beyond the visible road stretch have been inferred. | result:
                        Consistent observations; the observed left-edge paint colour is retained rather than
                        replaced by the expected colour.
Step 5  Rule            left_boundary: The solid left edge line normally prohibits crossing, and the adjacent
                        curb and guardrail also form a physical boundary. [CN-4.2.2-a] "Longitudinal markings,
                        set along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a curb and guardrail lie beside it.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
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
Step 7  Reflect         Consistent: only boundary-crossing actions are decided by the visible boundaries; no
                        intersection movement is inferred from them.
Advice                  Follow the current lane along the road and do not cross its left edge. You may change
                        right across the broken white line after checking traffic; no visible markings
                        establish turn-lane choices or a stopping point ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 932, 17.75 s

culane_test__d100_05251222_0385_01710 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A multilane urban road runs beside and beneath an elevated structure toward an
                        intersection. My car is in the second of four apparent same-direction lanes, behind a
                        silver sedan. (lanes 4, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another traffic lane on the left; the
                        median curb and guardrail are farther left, beyond that lane.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the adjacent lane containing a dark
                        sedan; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white longitudinal arrow shaft is visible immediately
                        behind the silver sedan; its head and any additional branches are obscured, so the
                        apparent straight arrow cannot be read completely.; line:crosswalk (partial): White
                        transverse pedestrian-crossing stripes extend across the approach ahead; the portion
                        in my lane is partly hidden by the silver sedan.
Step 4  Cross-check     position: Lane lines on both sides agree with an interior lane, second from the left
                        among four same-direction lanes. | roles: Both boundaries are white and solid,
                        consistent with no-crossing lane separators on an intersection approach. | markings:
                        The partially obscured arrow is compatible with a guide lane, but its complete set of
                        permitted directions cannot be checked. The crosswalk does not establish lane-use
                        directions. | unseen: The arrowhead, possible branches, and pavement beneath the sedan
                        are hidden; no stop line or additional arrow direction is asserted. | result:
                        consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            arrow:straight: A guide arrow specifies permitted travel directions, but the obscured
                        head prevents a reliable determination of this arrow's complete directions.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks; this transverse
                        marking does not govern any of the seven requested actions.
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined (WRONG, label allowed): The sedan hides the arrowhead needed to confirm
                        the permitted movement under CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The obscured arrowhead and possible branches
                        prevent determining whether a left turn is permitted.
Step 6  turn_right      not_determined (WRONG, label prohibited): The obscured arrowhead and possible branches
                        prevent determining whether a right turn is permitted.
Step 6  u_turn          not_determined (WRONG, label prohibited): The complete arrow is hidden, so its
                        permitted directions cannot be established.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid white boundaries; do not change lanes across them. Confirm the
                        complete lane arrow when the sedan clears it, obey the intersection signals, and keep
                        the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1277, 25.27 s

culane_test__d100_05251222_0385_02280 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs alongside an elevated structure, with traffic continuing
                        ahead toward a distant junction. My car is in the leftmost lane; vehicles obscure the
                        outer lanes and the distant approach markings. (lanes None, mine 1, partial)
Step 2  Left            A single solid white line follows a raised curb on the left, with a planted strip and
                        metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long segments and intervening gaps, separates my
                        lane from another same-direction traffic lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and a same-direction lane on the right establish my
                        lane as leftmost; the total lane count remains obscured. | roles: The broken white
                        right boundary fits a same-direction lane line. The left paint appears white despite
                        the prescribed yellow for a left edge; its curbside position establishes its edge role
                        without changing the observed colour. | markings: No guidance markings are readable on
                        the visible pavement within my lane; overhead signs are not pavement markings. |
                        unseen: No distant arrows, stop line, waiting area or total lane count have been
                        inferred through traffic. | result: consistent
Step 5  Rule            left_boundary: The solid left edge line normally prohibits crossing; the raised curb
                        also forms a physical roadway edge. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane boundary permits a lane change under
                        CN-5.2.3.
Step 6  go_straight     not_determined (WRONG, label prohibited): Distant lane-end pavement markings are
                        obscured and cannot establish this movement.
Step 6  turn_left       not_determined (WRONG, label allowed): Distant lane-end pavement markings are obscured
                        and cannot establish this movement.
Step 6  turn_right      not_determined (WRONG, label prohibited): Distant lane-end pavement markings are
                        obscured and cannot establish this movement.
Step 6  u_turn          not_determined (WRONG, label allowed): Distant lane-end pavement markings are
                        obscured; the roadside U-turn sign is context, not an observed lane arrow.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Do not cross the solid left edge; a rightward lane change is permitted by the dashed
                        line only when the adjacent traffic allows it. The sign indicates a U-turn opportunity
                        100 m ahead, but confirm lane-use signs and pavement arrows before selecting a
                        junction movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left', 'arrow:u_turn']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 935, 20.18 s

culane_test__d100_05251222_0385_02400 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs beside an elevated structure, with traffic continuing
                        toward a distant junction. My car is in the second lane from the left among four
                        visible same-direction lanes. (lanes 4, mine 2, full)
Step 2  Left            A solid white line separates my lane from another traffic lane on the left; no curb
                        forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from the lane occupied by the white sedan on the
                        right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead and a short portion of
                        its shaft are visible immediately above the hood; the lower portion is obscured, so
                        additional branches cannot be checked.
Step 4  Cross-check     position: The second-of-four position agrees with having same-direction lanes beyond
                        both boundaries. | roles: Both solid white boundaries fit no-crossing same-direction
                        lane lines. | markings: The visible forward arrowhead agrees with the lane continuing
                        ahead; no words, waiting areas or transverse lines are identifiable in my lane. |
                        unseen: The hood hides the lower arrow, and distant traffic obscures the end of the
                        lane; no extra arrow branches or stop line are assumed. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but the
                        obscured remainder prevents confirming whether another movement is also indicated.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The obscured lower arrow prevents checking
                        for an additional left-turn branch.
Step 6  turn_right      not_determined (WRONG, label prohibited): The obscured lower arrow prevents checking
                        for an additional right-turn branch.
Step 6  u_turn          not_determined (WRONG, label prohibited): The obscured lower arrow prevents confirming
                        the complete movement restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight within this lane and do not cross either solid white boundary.
                        Confirm the complete lane arrow and junction controls before attempting any turn; no
                        stopping position can be identified in this view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1056, 19.91 s

culane_test__d100_05251222_0385_04920 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A wide urban road approaches a signal-controlled intersection beneath an elevated
                        railway. My car is in the marked lane behind the dark sedan; the full same-direction
                        lane count and my lane's index are uncertain because the outer lanes and opposing-
                        traffic separation are not clearly traceable. (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line runs along my lane's left side, with another marked traffic
                        lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along my lane's right side, with additional roadway and
                        same-direction traffic beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white straight-ahead arrow is painted in my lane; its
                        shaft and part of its forward-pointing head are visible, while the sedan obscures the
                        upper portion.; line:stop_line (partial): A transverse white stop line is visible
                        approaching the intersection, with its right portion obscured by the sedan.;
                        line:crosswalk (partial): White pedestrian-crossing stripes lie beyond the stop line;
                        vehicles obscure the portion directly ahead.
Step 4  Cross-check     position: Lane lines on both sides establish that my lane is an interior lane, but do
                        not establish the total lane count or exact index. | roles: Both solid white
                        boundaries fit same-direction lane separators on an intersection approach. | markings:
                        The visible straight arrow is consistent with an intersection guide lane bounded by
                        solid white lines; the stop line and crossing are consistent with the intersection
                        ahead. | unseen: The full arrow head, portions of the transverse markings, and the
                        outer lane arrangement are obscured or unclear; no exact lane count is inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white lane separator prohibits my car from crossing to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane separator prohibits my car from crossing to the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible straight-ahead guidance permits proceeding straight, but
                        the obscured portion limits certainty about any additional arrow head. [CN-5.13.1]
                        "Guide arrows indicate the direction of travel for vehicles. (Table 1 meanings:
                        straight ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks; this marking
                        identifies a pedestrian crossing and does not determine any of the seven actions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward-pointing arrow permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The sedan obscures part of the arrow head,
                        preventing a confident check for an additional left-turn head.
Step 6  turn_right      not_determined (WRONG, label prohibited): The sedan obscures part of the arrow head,
                        preventing a confident check for an additional right-turn head.
Step 6  u_turn          not_determined (WRONG, label prohibited): The obscured upper arrow portion prevents
                        fully establishing the lane's complete directional guidance.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable in view.
Step 7  Reflect         consistent
Advice                  Remain between the solid white lines and follow the visible straight-ahead guidance;
                        do not change lanes across either boundary. Obey the traffic signals, stop before the
                        stop line when required, and keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1378, 28.99 s

culane_test__d100_05251222_0385_05250 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues ahead beside an elevated roadway, with no
                        intersection or lane ending visible. My car is in the leftmost of three lanes
                        travelling in this direction. (lanes 3, mine 1, full)
Step 2  Left            A solid white line borders my lane on the left, with a diagonally striped paved strip
                        and a median guardrail beyond it; the guardrail does not directly border my lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another lane
                        travelling in the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane divider on the right agree with my car
                        occupying lane 1 of 3. | roles: The broken white right boundary fits a same-direction
                        lane divider. The left boundary functions as an edge line, although its visibly white
                        paint differs from the yellow specified for a left edge by CN-5.4.3; its colour has
                        not been inferred from its position. | markings: No guidance arrows, words, symbols or
                        transverse lines are visible in my lane. The diagonal striping lies outside its left
                        boundary. | unseen: No unseen intersection markings or lane directions have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, except in an
                        emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane divider permits lane changes under CN-5.2.3.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain within the solid left edge and keep out of the striped strip. A rightward lane
                        change is permitted when safe; no visible lane-use arrows establish turn choices
                        ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 902, 19.77 s

culane_test__d100_05251309_0397_03150 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues toward a distant
                        junction approach. My car is in the rightmost lane, beside a curbed planted verge.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs beside a raised curb, with a planted verge and a separate
                        paved path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (partial): A white combined straight-and-right arrow is visible
                        ahead; the right-pointing head is clear, while the forward portion is partly obscured
                        by the SUV.
Step 4  Cross-check     position: The rightmost position in three same-direction lanes agrees with a lane
                        divider on the left and a roadway edge on the right. | roles: The broken white left
                        line fits a crossable same-direction lane divider; the solid white right line fits the
                        roadway edge beside the curb. | markings: The straight-and-right arrow is consistent
                        with a rightmost lane; no conflicting pavement marking is visible. | unseen: The SUV
                        partly hides the forward portion of the arrow, and distant pavement details and the
                        lane's eventual stopping point cannot be read; no unseen stop line or waiting area is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing; the curb also
                        forms a physical roadway edge. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight_right: The combined arrow permits straight travel or a right turn, not
                        a left turn or U-turn. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits normal crossing under
                        CN-4.2.2-a, and a curb lies alongside it.
Step 6  go_straight     allowed (correct): The identifiable straight-and-right arrow permits straight travel
                        under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-and-right arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      allowed (correct): The right-pointing arrowhead permits a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-and-right arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Use this lane for straight travel or a right turn, subject to junction signs and
                        signals. If a different movement is needed, select an appropriately marked lane by
                        crossing the broken left divider when safe; do not cross the solid right edge or curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1126, 22.15 s

culane_test__d100_05251309_0397_03390 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad divided urban road approaches a signal-controlled intersection. My car is in a
                        through lane, with several lanes to the left and a separate lane to the right; the
                        far-left lane layout is difficult to count confidently. (lanes None, mine None,
                        insufficient)
Step 2  Left            A single white solid line runs along the left of my lane, with another same-direction
                        lane occupied by a white van beyond it.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single white solid line runs along the right of my lane, separating it from another
                        traffic lane; the raised roadside island is beyond that adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrow is partly concealed by the
                        hood near the bottom of my lane.; arrow:straight (full): A second white straight-ahead
                        arrow is visible farther ahead in my lane.; line:stop_line (partial): A transverse
                        white stopping line is faintly visible at the intersection approach; its extent is
                        difficult to distinguish at this distance.
Step 4  Cross-check     position: Both boundaries separate same-direction lanes, consistent with my lane
                        having adjacent lanes on both sides; the total lane count and numerical position
                        remain uncertain. | roles: The white solid lines fit same-direction no-crossing lane
                        boundaries on an intersection approach. | markings: The visible straight arrows agree
                        with each other and with a solid-lined through guide lane. | unseen: The hood hides
                        the lower part of the nearest arrow, and distant transverse markings are not fully
                        resolved; no additional symbols or waiting areas are inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits my car from crossing into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            arrow:straight: The forward arrow indicates straight travel from this lane.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            arrow:straight: The fully visible straight arrow allows straight travel rather than
                        left, right or U-turn movements. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when required to yield
                        or wait. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 6  change_left     prohibited (correct): The solid white left lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane boundary prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The fully visible straight arrow permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain in this lane to go straight, without crossing either solid boundary. For a
                        turn, select an appropriately marked lane before the solid-lined approach; obey the
                        applicable traffic signal and stop before the stop line when required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1582, 33.81 s

culane_test__d100_05251327_0403_00180 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban carriageway continues straight toward a distant overhead structure. My
                        car is in the leftmost of three visible same-direction lanes, beside a raised
                        landscaped divider; no intersection stop line is clearly visible ahead. (lanes 3, mine
                        1, full)
Step 2  Left            A single solid white line runs along the left side of my lane, with a raised curb and
                        paved landscaped divider beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible dashes and intervening gaps, separates my lane from
                        the same-direction lane occupied by the dark sedan; there is no curb here.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A large white forward-pointing arrowhead is visible directly
                        ahead in my lane; its lower shaft is hidden by the hood.
Step 4  Cross-check     position: The left roadway edge and the same-direction lane line on the right agree
                        with my car being in lane 1 of 3. | roles: The broken white right boundary fits a
                        same-direction lane line. The left boundary is visibly white despite being the left
                        roadway edge; its color is reported as seen rather than changed to the yellow normally
                        specified for that position. | markings: The visible forward arrowhead agrees with a
                        through lane; no conflicting word, area or arrowhead is visible in my lane. | unseen:
                        The arrow shaft is partly hidden by the hood, and distant pavement details cannot be
                        resolved; no unseen stop line or waiting area is inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal boundary normally prohibits crossing to the
                        left; no supplied curb-specific passage authorizes driving across the raised edge.
                        [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take these
                        forms: a solid line means crossing is normally prohibited, and may be crossed in an
                        emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane line permits a lane change to the
                        right when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            arrow:straight: The visible straight-ahead guide arrow permits continuing straight and
                        does not permit left turns, right turns or U-turns from this lane. [CN-5.13.1] "Guide
                        arrows indicate the direction of travel for vehicles. (Table 1 meanings: straight
                        ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, with a raised curb beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.3, subject
                        to a safe gap.
Step 6  go_straight     allowed (correct): The identifiable forward arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent: the visible arrowhead determines the indicated movement despite the hidden
                        shaft, and each boundary governs only crossing on its own side.
Advice                  Continue straight in this lane; do not cross the solid left edge or mount the curb. A
                        rightward lane change is permitted across the broken line when clear, but use a
                        suitably marked lane for any later turn rather than turning from this straight-only
                        lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1086, 19.52 s

culane_test__d100_05251327_0403_00630 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined road continues ahead without a visible intersection or lane
                        ending. My car is in the left lane of two lanes travelling in this direction. (lanes
                        2, mine 1, full)
Step 2  Left            A continuous pale white solid line runs along the left of my lane, with a narrow paved
                        margin and a concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with clearly visible long dashes and gaps, separates my lane from
                        another traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my car
                        occupying lane 1 of 2. | roles: The broken white right boundary fits a same-direction
                        lane line. The left boundary is visibly pale white, although CN-5.4.3 specifies yellow
                        for a left edge line; its edge role is established by the adjacent barrier, not
                        inferred from paint colour. | markings: No arrows, words, symbols, transverse lines or
                        marked waiting areas are visible in my lane. | unseen: No markings or intersection
                        controls beyond the visible road have been inferred. | result: Consistent spatial
                        interpretation; the observed left-edge colour differs from the supplied colour
                        convention.
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing it; the adjacent
                        concrete barrier also forms a physical roadway edge. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane boundary permits changing into the adjacent
                        same-direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left edge prohibits normal crossing under CN-4.2.2-a,
                        and a concrete barrier lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
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
Step 7  Reflect         Consistent: boundaries govern only their respective crossing actions, and no
                        intersection movement permission is inferred from the road continuing ahead.
Advice                  Stay within the left solid edge; a rightward lane change is permitted across the
                        broken line after checking traffic and blind spots. No turn guidance or stopping line
                        is visible ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 906, 16.48 s

culane_test__d100_05251327_0403_00930 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road continues straight ahead, with two visible motor-vehicle lanes
                        in this direction. My car is in the leftmost lane beside the planted median; the
                        distant intersection approach is not fully visible. (lanes 2, mine 1, full)
Step 2  Left            A single solid white line runs along the left of my lane, with a narrow paved strip
                        and a raised median curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has a single head pointing
                        straight ahead.
Step 4  Cross-check     position: The left roadway edge and the same-direction lane on the right agree with my
                        lane being lane 1 of 2. | roles: The broken white right boundary fits a crossable lane
                        line. The left line visibly marks the median-side roadway edge, although its white
                        paint differs from the prescribed yellow left-edge colour. | markings: The straight
                        arrow is compatible with the lane boundaries; no conflicting word, arrow or marked
                        waiting area is visible. | unseen: No distant stop line or additional marking hidden
                        by vehicles is inferred. | result: consistent; the observed white left-edge paint is
                        retained rather than inferred to be yellow.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            arrow:straight: The straight-only guide arrow permits continuing straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane boundary permits a lane change under
                        CN-5.2.3.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to continue straight, and do not cross the solid left edge. A
                        right lane change is permitted when safe, but use a lane explicitly marked for the
                        intended turn rather than turning from this straight-only lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1219, 26.13 s

culane_test__d100_05251327_0403_01200 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A barrier-lined, divided urban roadway continues straight ahead, with no intersection
                        or lane ending visible. My car is in the middle of three lanes travelling in this
                        direction. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long segments and gaps, separates my lane from
                        another traffic lane on the right; the concrete roadside barrier is beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): White Chinese pavement text is visible ahead in my lane,
                        appearing to include the character 环; the complete message is not clearly readable.
Step 4  Cross-check     position: Lane lines on both sides agree with my position in lane 2 of 3, with one
                        same-direction lane on each side. | roles: Both boundaries are broken white lines,
                        consistent with crossable same-direction lane dividers. | markings: The visible
                        pavement text does not conflict with the boundaries; no directional arrow or marked
                        waiting area is visible in my lane. | unseen: The complete pavement message and the
                        road beyond the visible stretch are not inferred. The transverse roadway seam is not
                        identified as a stop line. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent left
                        lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent right
                        lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            text:other: This is pavement text, but its incomplete reading establishes no
                        restriction on any of the seven assessed actions. [CN-5.14.1] "Pavement text markings
                        are generally white. They are arranged vertically and read from near to far along the
                        direction of travel ... or horizontally from left t"
Step 6  change_left     allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in the middle lane to follow the roadway; either broken divider may be crossed
                        after checking traffic and ensuring a safe gap. No visible intersection guidance
                        establishes a lane for turning or a place to stop.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8604, out 969, 16.56 s

culane_test__d100_05251327_0403_02340 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road curves gently left, with a fenced median on the left and a
                        sidewalk on the right. My car is in the leftmost of two same-direction lanes; no
                        intersection or lane ending is visible. (lanes 2, mine 1, full)
Step 2  Left            A single continuous white line runs beside a raised median curb and fence, with
                        opposing traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single continuous white line separates my lane from another same-direction lane on
                        the right; there is no curb at this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left median edge and right lane separator agree with my lane being lane
                        1 of 2. | roles: The white right lane separator fits its role. The left edge paint
                        appears white despite the supplied rule specifying yellow for a left carriageway edge;
                        its observed color is retained. | markings: No arrows, words, symbols, waiting areas
                        or transverse markings are visible in my lane. | unseen: No markings beyond the
                        visible road stretch are inferred. | result: Consistent spatial interpretation; the
                        observed left-edge color differs from the prescribed color.
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the raised median also physically bounds the lane. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane separator prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised median lies beyond it.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
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
Step 7  Reflect         Consistent: boundaries govern only lateral crossing, and no intersection movement
                        permission is inferred from their absence of arrows.
Advice                  Stay within the current lane and do not cross either solid boundary in the visible
                        stretch. Follow the gentle curve and the posted 30 km/h limit; no turn guidance or
                        stopping line is visible ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 903, 18.38 s

culane_test__d100_05251327_0403_03870 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A narrow urban road runs between an elevated structure on the left and a tree-lined
                        sidewalk on the right. My car is in the left of two same-direction lanes, behind a
                        car; the road continues ahead, but the lane's distant end is obscured. (lanes 2, mine
                        1, full)
Step 2  Left            A solid white line follows a raised curb on the left, with a narrow paved walkway and
                        a wall beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white longitudinal segment separates my lane from the lane on the right; its
                        continuation is obscured by the car ahead and the hood, so a dash-and-gap pattern
                        cannot be confirmed, and there is no curb at this boundary.
                        white none, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane line on the right agree with my car
                        occupying lane 1 of 2. | roles: The white right boundary fits separation of same-
                        direction lanes, although its pattern is uncertain. The left line is visibly white
                        despite being the left roadway edge; its colour has not been inferred from its
                        position. | markings: No guidance markings can be read in the exposed portion of my
                        lane; the car ahead obscures much of its surface. | unseen: The right boundary's solid
                        or broken pattern and any guidance markings farther ahead cannot be established. |
                        result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal line normally prohibits crossing the
                        left boundary; the raised curb also forms a physical roadway edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: A solid same-direction lane boundary prohibits crossing, but this
                        boundary's pattern is not sufficiently visible to establish whether that prohibition
                        applies. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid white left edge line prohibits normal crossing under
                        CN-4.2.2-a, and a raised curb lies beside it.
Step 6  change_right    not_determined (WRONG, label prohibited): The right lane boundary's pattern is
                        obscured, so crossing permission cannot be established.
Step 6  go_straight     not_determined: The car ahead obscures the lane surface and distant guidance markings
                        that could determine this movement.
Step 6  turn_left       not_determined: The lane's end and any governing direction markings are obscured.
Step 6  turn_right      not_determined: The lane's end and any governing direction markings are obscured.
Step 6  u_turn          not_determined: The lane's end and any governing direction or prohibition markings are
                        obscured.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the current lane and maintain space behind the braking car; do not cross
                        the solid left edge or curb. Confirm the right boundary pattern and downstream lane
                        arrows before changing lanes or selecting an intersection movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1006, 18.98 s

culane_test__d100_05251327_0403_03960 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road runs beside an elevated structure, with two lanes apparently travelling
                        in the same direction. My car is in the left lane behind a sedan; the lane's end and
                        any intersection markings are not visible. (lanes 2, mine 1, full)
Step 2  Left            A continuous white line follows a raised curb on the left, with a narrow sidewalk and
                        the elevated structure's wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears continuous along the visible stretch to the right of my car,
                        separating another paved traffic lane; the sedan hides its continuation ahead.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and a lane divider on the right agree with my car
                        occupying lane 1 of 2. | roles: The white right divider fits a same-direction lane
                        line. The left edge paint is visibly white, despite the usual yellow specified for a
                        left carriageway edge; its curb-side position establishes its edge role. | markings:
                        No arrows, words, symbols, transverse lines or waiting areas can be identified on the
                        exposed pavement in my lane. | unseen: The sedan obscures much of my lane ahead, and
                        the lane end is not visible; no hidden arrows or intersection markings have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        left, where a raised curb also forms a physical boundary. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white same-direction lane divider prohibits crossing
                        into the lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles
                        travelling in the same direction and prohibits vehicles on the solid-line side from
                        crossing. It has two forms: sin"
Step 6  change_left     prohibited (correct): The solid white left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised curb lies beyond it.
Step 6  change_right    prohibited (correct): The visible solid white lane divider prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The sedan and unseen lane end conceal any lane-use arrow that would
                        govern this movement.
Step 6  turn_left       not_determined: The sedan and unseen lane end conceal any lane-use or prohibited-turn
                        marking.
Step 6  turn_right      not_determined: The sedan and unseen lane end conceal any lane-use or prohibited-turn
                        marking.
Step 6  u_turn          not_determined: The sedan and unseen lane end conceal any lane-use or prohibited-U-
                        turn marking.
Step 6  enter_waiting_areanot_determined: No adjacent two-way left-turn lane is visible, but the obscured
                          approach prevents determining whether a waiting area lies ahead.
Step 7  Reflect         consistent
Advice                  Stay within the visible boundaries and maintain space behind the sedan; do not cross
                        the solid right divider or the left curb-side line. Check the lane-use markings and
                        any stop line when the approach becomes visible before choosing an intersection
                        movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 963, 19.26 s

culane_test__d100_05251627_0452_02850 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches an underpass, with traffic queued ahead. My car is in
                        the leftmost lane beside a median fence; vehicles obscure the far-right roadway edge
                        and the continuation beneath the bridge. (lanes None, mine 1, partial)
Step 2  Left            A continuous white painted line runs beside the median fence, with yellow paint
                        farther toward the fence and opposing traffic beyond the physical divider.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A worn, apparently continuous white line separates my lane from the same-direction
                        lane occupied by taxis; vehicles obscure its farther continuation.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left places my lane first from the left, and the
                        right lane line confirms another same-direction lane; the total lane count is
                        obscured. | roles: The white right boundary fits a same-direction lane line. The white
                        left line is observed beside a physical median; its colour is reported as seen rather
                        than inferred from its position. | markings: No readable arrows, words, symbols,
                        transverse lines or waiting areas appear in the exposed portion of my lane. | unseen:
                        No lane count or hidden guidance markings are inferred; vehicles and the underpass
                        obscure the farther roadway. | result: consistent
Step 5  Rule            left_boundary: The visible solid boundary normally prohibits crossing, and the
                        physical median also prevents a leftward departure. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white lane line prohibits crossing into the lane on
                        my right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median fence lies beyond it.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The lane's eventual end and any movement arrows there are hidden by
                        traffic and the underpass.
Step 6  turn_left       not_determined: The lane's eventual end and any movement arrows there are hidden.
Step 6  turn_right      not_determined: The lane's eventual end and any movement arrows there are hidden.
Step 6  u_turn          not_determined: The lane's eventual end and any movement or prohibition markings there
                        are hidden.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain between the median and the solid white line, maintaining space behind the
                        queue. Do not cross either boundary; reassess lane-direction markings when the roadway
                        ahead becomes visible and obey the applicable signals.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1025, 23.42 s

culane_test__d100_05251718_0469_00390 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in the third of four apparent same-direction approach lanes.
                        (lanes 4, mine 3, partial)
Step 2  Left            A single solid white line separates my lane from another approach lane on the left; no
                        curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the lane containing the silver car on
                        the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white straight-ahead arrowhead is visible immediately
                        ahead of the hood; the lower shaft is obscured by the hood.; line:stop_line (full): A
                        transverse solid white stop line crosses my lane before the pedestrian crossing.;
                        line:crosswalk (full): White zebra-crossing stripes extend across my lane beyond the
                        stop line.
Step 4  Cross-check     position: Same-direction lanes are visible on both sides, consistent with an interior
                        lane. Four lanes and position three appear likely, but the far-left layout is less
                        clear. | roles: Both solid white boundaries fit same-direction lane separators on an
                        intersection approach. | markings: The visible straight arrow agrees with the approach
                        guide lane; the stop line precedes the crosswalk. | unseen: The arrow shaft is partly
                        hidden and the far-left lane arrangement is uncertain; neither is treated as fully
                        visible. No waiting area is identifiable. | result: consistent
Step 5  Rule            left_boundary: The solid white lane separator prohibits crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane separator prohibits crossing to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible straight-ahead arrow permits proceeding straight, not
                        turning left, right or making a U-turn from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalk markings; this
                        pedestrian crossing does not determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The readable straight arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Stay in this lane for straight travel and do not cross either solid white boundary.
                        Follow the applicable traffic signal, stop before the stop line when required, and
                        keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1329, 25.53 s

culane_test__d100_05251718_0469_01320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues beneath a pedestrian footbridge; no intersection or
                        lane ending is visible. My car is in the left of two same-direction lanes, behind a
                        silver sedan. (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs beside a raised curb on the left, with a paved pedestrian
                        area, vegetation and bridge supports beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction traffic lane; vehicles obscure portions farther ahead.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego position 1 agree with a roadway edge on the left and a
                        same-direction lane line on the right. | roles: The white broken right boundary fits a
                        crossable lane line. The left boundary is visibly white despite being the left roadway
                        edge; its physical curb and roadside surroundings establish its role without changing
                        the observed color. | markings: No guidance arrows, text, symbols, transverse lines or
                        waiting areas are visible in my lane. | unseen: No markings are inferred beneath the
                        sedan or beyond the visible road; the next intersection and its lane-use markings are
                        not visible. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the raised curb also forms a physical roadway edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid white left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised curb lies alongside it.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible marking governs this action.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the left curb and solid edge line; a right lane change is permitted by
                        the broken line if traffic allows. No visible arrows establish intersection movements,
                        and no stop line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 856, 15.99 s

culane_test__d100_05251718_0469_02040 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight, with no intersection or lane
                        ending visible. My car is in the left lane of two lanes in this direction, beside the
                        planted median. (lanes 2, mine 1, full)
Step 2  Left            An unpainted raised curb borders the lane on the left, with a planted median beyond;
                        no painted longitudinal line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and intervening gaps, separates my lane
                        from another traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego lane index 1 agree with the median curb on the left and a
                        same-direction lane across the right boundary. | roles: The left curb forms the
                        roadway edge; the broken white line fits a crossable same-direction lane divider. |
                        markings: No guidance markings are visible within my lane, and none conflict with the
                        boundaries. | unseen: No distant intersection layout, hidden guidance marking, or
                        painted line beside the left curb has been inferred. | result: consistent
Step 5  Rule            left_boundary: A curb can define the road edge without a painted edge line; crossing
                        this raised physical edge is prohibited under the boundary definitions. [CN-5.4.5]
                        "Where a non-motorized lane is needed and there is no separating facility between it
                        and the motor vehicle lanes, a motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: The broken white lane divider permits my car to change into the lane
                        on the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The raised median curb is a physical edge that must not be
                        crossed.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
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
Advice                  Remain within the lane and do not cross the median curb; a right lane change is
                        permitted after checking traffic. No intersection movement assignments or stopping
                        point are visible, so reassess the markings as you approach a junction.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 824, 14.68 s

culane_test__d100_05251718_0469_02250 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with no intersection or lane
                        ending visible. My car is in the left lane of two lanes travelling in this direction.
                        (lanes 2, mine 1, full)
Step 2  Left            A raised concrete curb forms the left edge beside a planted median; no painted
                        longitudinal line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the adjacent same-direction lane; sections
                        farther ahead are partly obscured by vehicles.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The curb on the left and a same-direction lane on the right agree with my
                        car occupying lane 1 of 2. | roles: The physical median curb forms the left roadway
                        edge; the broken white line fits a same-direction lane divider. | markings: No
                        guidance arrows, words, symbols, transverse lines or marked waiting areas are visible
                        in my lane. | unseen: No markings are inferred beneath vehicles or beyond the visible
                        road; the right boundary is partly obscured farther ahead. | result: consistent
Step 5  Rule            left_boundary: A curb can define the roadway edge without a painted edge line;
                        crossing this physical boundary is not an available lane-change movement. [CN-5.4.5]
                        "Where a non-motorized lane is needed and there is no separating facility between it
                        and the motor vehicle lanes, a motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane where safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The raised median curb is a physical boundary that my car cannot
                        cross as a lane change.
Step 6  change_right    allowed (correct): The visible broken white lane divider permits crossing under
                        CN-5.2.3.
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
Advice                  Stay within the curb and broken white divider; a right lane change is permitted by the
                        marking, but check the nearby car and available gap first. No visible intersection
                        markings establish turn permissions or a stopping point.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 862, 18.51 s

culane_test__d100_05251718_0469_05070 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues ahead toward traffic and an overhead lane-
                        direction sign. My car is in the leftmost of two visible lanes in this direction,
                        beside the raised landscaped median. (lanes 2, mine 1, full)
Step 2  Left            A faint pale yellow solid line runs beside the raised curb on the left, with a
                        landscaped median beyond; the paint is worn and its colour is not fully clear.
                        yellow solid, curb yes, edge_line, evidence partial
Step 2  Right           A broken white line, with a visible long dash and intervening gap, separates my lane
                        from another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego lane index 1 agree with a median-side edge on the left and
                        a same-direction lane line on the right. | roles: The faint yellow solid marking is
                        consistent with a left roadway edge, and the broken white marking is consistent with a
                        crossable same-direction lane boundary. | markings: No pavement arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. | unseen: The left
                        paint colour is uncertain because it is faint; the raised curb is clearly visible. No
                        pavement direction is inferred from the overhead sign or from vehicles hiding the
                        distant road. | result: consistent
Step 5  Rule            left_boundary: The raised curb establishes a physical roadway edge, not a lane-change
                        route; the passage recognizes this physical edge but does not separately authorize
                        crossing it. [CN-5.4.5] "Where a non-motorized lane is needed and there is no
                        separating facility between it and the motor vehicle lanes, a motor/non-motor
                        separation line shall be prov"
Step 5  Rule            right_boundary: The broken white lane boundary permits changing into the adjacent lane
                        on the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The raised median curb is a physical edge, so moving across this
                        boundary is prohibited regardless of the faint paint.
Step 6  change_right    allowed (correct): The broken white lane line permits a right lane change under
                        CN-5.2.3.
Step 6  go_straight     not_applicable: No visible pavement marking governs this movement.
Step 6  turn_left       not_applicable: No visible pavement marking governs this movement.
Step 6  turn_right      not_applicable: No visible pavement marking governs this movement.
Step 6  u_turn          not_applicable: No visible pavement marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the median curb; a right lane change is permitted across the broken line
                        only after checking adjacent traffic. The overhead sign provides lane-direction
                        context, but no pavement arrows or stopping point are readable here; confirm the
                        required lane before the intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1015, 25.9 s

culane_test__d100_05251718_0469_05190 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban road with three lanes in this direction continues ahead; no
                        intersection or lane ending is clearly visible. My car is in the middle lane. (lanes
                        3, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside curb lies beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego position 2 agree with a lane line and
                        another same-direction lane on each side. | roles: Both white broken boundaries fit
                        crossable same-direction lane lines. | markings: No guidance marking is visible in my
                        lane, and no marked waiting area is visible ahead or directly to its left. | unseen:
                        No distant intersection layout, lane-end marking, or hidden pavement marking is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the lane on the left
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane line permits changing into the lane on the right
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 6  change_left     allowed (correct): The left broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    allowed (correct): The right broken white lane line permits crossing under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You may cross either broken white boundary to change lanes when traffic conditions
                        permit. No visible marking establishes turn permissions or a stopping point; check the
                        markings and controls as you approach the next intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 821, 13.46 s

culane_test__d100_05251947_0499_00840 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with an elevated roadway alongside on the right
                        and opposing traffic beyond the median on the left. My car is in the leftmost of three
                        visible lanes travelling in this direction; no intersection or lane ending is visible.
                        (lanes 3, mine 1, full)
Step 2  Left            A single solid line that appears white runs beside a raised concrete median on the
                        left, with opposing traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible painted segments and intervening gaps, separates my
                        lane from another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median-side left edge and the lane line on the right agree with my car
                        occupying lane 1 of 3. | roles: The broken white right boundary fits a same-direction
                        lane line. The left line appears white rather than the yellow specified for a left
                        edge, but its location alongside the physical median establishes its edge role. |
                        markings: No arrows, words, symbols, transverse lines or waiting areas are visible in
                        my lane. | unseen: No intersection movements or markings beyond the visible road
                        section have been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the physical median also prevents an ordinary lane change. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left edge line prohibits ordinary crossing under
                        CN-4.2.2-a, and a concrete median lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the solid median-side boundary. You may change right across the broken
                        white line after checking traffic; no visible lane-use arrows determine movements at a
                        future intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 876, 16.17 s

culane_test__d100_05251947_0499_04830 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban divided road continues straight ahead in low light; no intersection
                        or lane ending is clearly visible. My car is in the rightmost of three visible lanes
                        in this direction. (lanes 3, mine 3, full)
Step 2  Left            A faded white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white line appears continuous beside the raised curb and planted verge on the right,
                        although darkness reduces its clarity.
                        white solid, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:straight (partial): A small white forward-pointing arrow is visible farther
                        ahead in my lane; its detail is reduced by distance and low light.
Step 4  Cross-check     position: The rightmost position agrees with a same-direction lane line on the left
                        and a curbed roadway edge on the right. | roles: The broken white left boundary fits a
                        crossable lane line; the white right boundary beside the verge fits a roadway edge. |
                        markings: The visible straight arrow is consistent with the continuing lane and does
                        not conflict with either boundary. | unseen: The distant intersection layout and any
                        farther markings cannot be resolved; none are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing; the raised curb
                        also forms a physical edge rather than an adjacent traffic lane. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right edge prohibits normal crossing under CN-4.2.2-a,
                        and a raised curb lies beside it.
Step 6  go_straight     allowed (WRONG, label prohibited): The identifiable straight arrow permits this
                        movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (WRONG, label allowed): The straight-only arrow does not permit a right
                        turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to continue straight; do not cross the right edge or curb. For a
                        turn, identify the appropriate marked lane farther ahead and move left across the
                        broken line only when safe; distant markings are difficult to read.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation accepted, contradictions []
Tokens                  in 8604, out 1104, 22.96 s

culane_test__d100_05252026_0512_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit, divided urban road at night, with vehicles ahead and a physical median on the
                        left. My car is in the rightmost apparent through lane; darkness makes the full
                        carriageway lane count uncertain. (lanes None, mine None, insufficient)
Step 2  Left            White broken paint, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved margin and a
                        raised roadside edge farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line establishes at least one same-direction lane to my left,
                        and the right edge line places my lane at the right edge; the total lane count cannot
                        be established confidently in the darkness. | roles: The broken white left boundary
                        fits a same-direction lane divider, and the solid white right boundary fits a roadway
                        edge. | markings: No readable guidance markings or transverse lines are visible within
                        my lane. | unseen: No arrow, intersection stop line, or waiting area is inferred from
                        the distant lights; the full lane count remains unspecified. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits my car to change into the
                        adjacent same-direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in
                        the same direction, the crossable lane line shall be used on sections where vehicles
                        may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, except in a
                        safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
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
Advice                  Stay inside the solid right edge line; a left lane change is permitted by the broken
                        divider if safe. No readable lane-use arrows or stop line establish intersection
                        movements or a stopping position here, so check the approach markings and signals as
                        they become clearer.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1073, 26.6 s

culane_test__d100_05252026_0512_01020 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A multilane urban road at night, with opposing traffic to the left and vehicles
                        travelling ahead. My car is in the second visible lane from the left; darkness
                        obscures the far-right roadway and the eventual intersection approach. (lanes None,
                        mine 2, partial)
Step 2  Left            A broken white line, with a visible dash and adjoining gap, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with a bright dash and visible gap, separates my lane from
                        roadway used by same-direction traffic on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane is visible on each side, consistent with my lane being
                        second from the left; the total lane count cannot be confirmed in the dark. | roles:
                        Both white broken boundaries fit crossable same-direction lane lines. | markings: No
                        arrows, words, symbols, marked areas or transverse lines can be read in my lane; the
                        distant lane end is not sufficiently visible to establish its movement restrictions. |
                        unseen: No distant arrow, stop line, waiting area or exact total lane count has been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane boundary permits changing into the adjacent lane
                        on the left. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane boundary permits changing into the adjacent lane
                        on the right. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    allowed (correct): The visible broken white lane line permits crossing under CN-5.2.3.
Step 6  go_straight     not_determined: The distant lane end and any governing direction markings are obscured
                        by darkness.
Step 6  turn_left       not_determined: The distant lane end and any governing direction markings are obscured
                        by darkness.
Step 6  turn_right      not_determined: The distant lane end and any governing direction markings are obscured
                        by darkness.
Step 6  u_turn          not_determined: The distant lane end and any governing direction or prohibition
                        markings are obscured by darkness.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible to
                          govern this action.
Step 7  Reflect         consistent
Advice                  Either visible broken boundary may be crossed when traffic conditions permit a safe
                        lane change. Do not assume this lane permits a particular intersection movement;
                        confirm the arrows, signs, signals and stopping position as they become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 966, 18.42 s

culane_test__d100_05252026_0512_01350 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road at night, with traffic continuing ahead and no clearly visible
                        intersection or lane ending. My car is in the rightmost lane; darkness and glare make
                        the total number of same-direction lanes uncertain. (lanes None, mine None, partial)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along the right of my lane, with a paved roadside strip beyond
                        it; the raised roadside edge is farther away rather than forming the immediate lane
                        boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to my left, and the
                        right edge line supports my position in the rightmost lane. The total lane count and
                        numerical index remain uncertain. | roles: The broken white left line fits a same-
                        direction lane divider; the solid white right line fits the right roadway edge. |
                        markings: No readable arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No distant intersection layout or lane-use direction has
                        been inferred through the darkness and glare. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits my car to change lanes to the
                        left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Keep within the solid right edge line; a left lane change is permitted by the broken
                        divider if traffic conditions allow. No visible arrows establish intersection
                        movements, so reassess the lane guidance as it becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 944, 19.99 s

culane_test__d193_06042058_0527_02610 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit tunnel carries two lanes in this direction, with vehicles ahead and no visible
                        intersection or lane ending. My car is in the right-hand lane. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, tinted by the tunnel lighting, has visible dashes and gaps and
                        separates my lane from another same-direction lane.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line, tinted by the tunnel lighting, borders my lane on the right,
                        with a narrow roadside strip and tunnel wall beyond; no raised curb directly bounds my
                        lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my car occupying lane 2
                        of 2. | roles: The broken white line fits a same-direction lane separator; the solid
                        white line fits the right roadway edge. | markings: No visible arrows, words, symbols
                        or transverse markings conflict with the boundaries. | unseen: No lane-end markings
                        are inferred beyond the visible stretch. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the lane on the left
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, except in
                        an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane separator permits lane changes under
                        CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
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
Advice                  Stay within the right lane unless a safe left lane change is needed; do not cross the
                        solid right edge line in ordinary driving. No intersection movement guidance or
                        stopping line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 822, 14.35 s

culane_test__d193_06042058_0527_03240 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit road continues ahead at night, with no intersection, ramp or lane ending
                        visible. My car is in the right lane of two lanes travelling in this direction. (lanes
                        2, mine 2, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from the
                        lane occupied by the white vehicle on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved shoulder and
                        roadside posts beyond it; no raised curb is visible.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and road edge on the right agree with my lane
                        being lane 2 of 2. | roles: The broken white line fits a same-direction lane
                        separator, and the solid white line fits a right carriageway edge. | markings: No
                        arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No distant intersection layout or markings beyond the visible road
                        have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the
                        shoulder, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
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
Advice                  Remain within the right lane and do not cross the solid edge line onto the shoulder in
                        normal driving. A left lane change is permitted by the markings, but wait until the
                        white vehicle alongside has cleared and a safe gap is available.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 839, 14.22 s

culane_test__d193_06051114_0632_02790 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection, with opposing traffic
                        beyond the median on the left. My car is behind the red car in a middle lane; worn
                        markings make the total number of same-direction lanes uncertain. (lanes None, mine 2,
                        partial)
Step 2  Left            A worn white line runs along the left of my lane and appears continuous over the
                        visible stretch, with another same-direction lane beyond it and no curb at this
                        boundary.
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           A white solid line extends forward along the right of my lane, with another same-
                        direction lane beyond it and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A worn white arrow ahead of the hood has a forward-pointing
                        head and a straight stem, with no visible turning branch.
Step 4  Cross-check     position: Lane lines on both sides place my lane between other same-direction lanes.
                        One lane is visible to the left, supporting index 2; the total lane count remains
                        uncertain. | roles: White longitudinal lines fit separation of same-direction traffic.
                        The left line is worn, so its apparent continuous pattern is less certain. | markings:
                        The straight arrow agrees with a through guide lane bounded by solid white lines; no
                        conflicting marking is visible. | unseen: No stop line, waiting area, or additional
                        arrow is reliably identifiable farther ahead; the red car and distance limit
                        inspection of that pavement. | result: consistent
Step 5  Rule            left_boundary: The visible solid white lane boundary prohibits crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits crossing to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and does not
                        permit left turns, right turns, or U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The visible left boundary is solid white; CN-6.2.1 prohibits
                        crossing it.
Step 6  change_right    prohibited (correct): The right boundary is solid white; CN-6.2.1 prohibits crossing
                        it.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting-area marking or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent: the visible solid boundaries prohibit lane changes, and only the straight
                        movement is permitted by the lane arrow.
Advice                  Stay in this lane to proceed straight and do not cross the visible solid boundaries.
                        For a turn, select an appropriately marked lane where lane changes are permitted; obey
                        the signals and watch for a stop line as the obscured pavement becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1146, 23.14 s

culane_test__d193_06051114_0632_04320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road continues ahead, with a fenced median on the left and a raised
                        separator beside a parallel roadway on the right. My car is in the left of two same-
                        direction lanes; no intersection or lane ending is clearly visible. (lanes 2, mine 1,
                        full)
Step 2  Left            A continuous solid white line runs beside the raised base of a median fence, with
                        opposing traffic beyond the fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A worn broken white line separates my lane from the lane occupied by the black car;
                        visible paint and gaps establish the broken pattern, although the car obscures part of
                        its continuation.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is hidden by the hood.
Step 4  Cross-check     position: The median edge on the left and a same-direction lane on the right agree
                        with my lane being lane 1 of 2. | roles: The broken white right boundary fits a same-
                        direction lane line. The left boundary is visibly white despite being beside the
                        median; its edge role follows the physical separation, not an assumed yellow colour. |
                        markings: The visible straight arrow agrees with a continuing travel lane; no
                        conflicting in-lane marking is visible. | unseen: The arrow shaft and parts of the
                        right boundary are obscured. No stop line, waiting area, or distant intersection
                        layout has been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the physical median also prevents an ordinary lane change. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            arrow:straight: The visible straight guide arrow permits straight travel rather than
                        left, right, or U-turn movements. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits ordinary crossing under
                        CN-4.2.2-a, and a median fence lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane boundary permits a lane change under
                        CN-5.2.3.
Step 6  go_straight     allowed: The identifiable forward arrow permits straight travel under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only guide arrow does not permit a left turn under CN-5.13.1.
Step 6  turn_right      prohibited: The straight-only guide arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited: The straight-only guide arrow does not permit a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not cross the left median boundary. A right lane
                        change is permitted by the markings, but wait for a safe gap around the black car; no
                        stopping position is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1107, 21.72 s

culane_test__d193_06051123_0635_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road approaches an intersection with a zebra crossing. My car is in
                        the leftmost of two visible same-direction motor-vehicle lanes; a narrower roadside
                        strip lies farther right. (lanes 2, mine 1, full)
Step 2  Left            A single continuous yellow line runs along my lane's left side to the stop line, with
                        opposing traffic space beyond and no curb.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line runs along my lane's right side to the stop line, with
                        another same-direction lane beyond and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white transverse stop line crosses my lane immediately
                        before the zebra crossing.; line:crosswalk (full): White zebra-crossing stripes extend
                        across my lane beyond the stop line.
Step 4  Cross-check     position: The yellow center line on the left and same-direction lane line on the right
                        agree with being lane 1 of 2. | roles: The solid yellow center line and solid white
                        lane divider fit their assigned roles. | markings: The stop line precedes the
                        crosswalk; no visible lane-use arrow or waiting area conflicts with the boundaries. |
                        unseen: No direction arrow is visible in the exposed lane; pavement beneath the hood
                        cannot be inspected. No hidden arrow or distant marking has been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits my car from crossing the
                        left boundary. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both
                        directions from crossing. It is generally used on two-lane two-way roads with limited
                        sight distance or wh"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks, and this
                        transverse marking does not determine any of the seven actions.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing under CN-6.1.4.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white lane line prohibits crossing under
                        CN-6.2.1.
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
Step 7  Reflect         consistent: both boundary crossings are prohibited, while the transverse markings do
                        not determine intersection movements.
Advice                  Stay between the solid boundaries; do not change lanes on this approach. When required
                        to stop, stop before the white stop line and keep the crosswalk clear; the visible
                        pavement markings alone do not establish which intersection movements this lane
                        permits.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1143, 20.66 s

culane_test__d193_06051123_0635_00900 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A two-way urban road curves gently ahead, with sidewalks on both sides and no clear
                        intersection or lane ending visible. My car is in the single motor-vehicle lane on the
                        right of the yellow center line. (lanes 1, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane, with opposing-direction
                        roadway beyond and no curb at the line.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, with a paved roadside strip
                        and a raised sidewalk curb farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane in my direction agrees with a center line on the left and a roadway
                        edge line on the right. | roles: The solid yellow center line separates opposing
                        directions; the solid white edge line bounds the motor-vehicle roadway on the right. |
                        markings: No arrows, words, symbols, transverse lines or marked waiting areas are
                        visible in my lane. | unseen: No purpose is assumed for the unmarked roadside strip,
                        and no distant intersection layout is inferred. | result: consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits my car from crossing to
                        the left. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both directions
                        from crossing. It is generally used on two-lane two-way roads with limited sight
                        distance or wh"
Step 5  Rule            right_boundary: The solid white longitudinal edge line normally prohibits crossing to
                        the right, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing under CN-6.1.4.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action; the center line governs crossing the
                        left boundary, not a movement at an unseen intersection.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Follow the road within the yellow center line and white right edge line; do not cross
                        either in normal driving. No visible lane-use arrow or stop line establishes turning
                        choices or a stopping position ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 820, 12.96 s

culane_test__d193_06051123_0635_00990 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A two-way urban street continues ahead, with no clearly visible intersection or lane
                        ending. My car is in the single visible motor-vehicle lane in its direction, between a
                        yellow centre line and a white boundary beside a narrow roadside strip. (lanes 1, mine
                        1, full)
Step 2  Left            A broken yellow line with visible long segments and gaps lies immediately left of my
                        lane, with opposing roadway beyond and no curb at the line.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A broken white line with visible segments and gaps separates my lane from a narrow
                        roadside strip; a raised sidewalk curb lies beyond that strip, not at the line itself.
                        white dashed, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow centre line makes my lane the leftmost in my direction; the white
                        roadside boundary makes it the rightmost motor-vehicle lane, consistent with one lane.
                        | roles: Broken yellow fits a crossable centre line, and broken white fits a
                        carriageway edge or motor/non-motor separation line. | markings: No arrows, text,
                        symbols, transverse lines or marked waiting areas are visible in my lane. | unseen:
                        The roadside strip's precise use is not visibly labelled; no bicycle designation or
                        distant intersection markings are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken centre line may be crossed to overtake or manoeuvre only
                        when doing so does not affect safety. [CN-5.1.1] "The crossable centre line separates
                        traffic flows in opposite directions. It means vehicles may cross the line to
                        overtake, turn or make a U-turn when this does"
Step 5  Rule            right_boundary: The broken white boundary permits crossing; this does not establish
                        that the roadside strip is a normal motor-vehicle travel lane. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): CN-5.1.1 permits crossing the broken yellow centre line when safe,
                        accounting for opposing traffic.
Step 6  change_right    allowed (correct): CN-4.2.2-a permits crossing the broken white boundary.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No arrow or prohibited-movement marking governs this action; the
                        centre line governs boundary crossing only.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the current motor-vehicle lane; no visible directional marking
                        requires a lane change or identifies a turning lane. Cross the centre line only when
                        safe, and do not treat the narrow roadside strip as an additional motor-vehicle lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 896, 16.6 s

culane_test__d193_06051123_0635_01980 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road with three lanes in this direction approaches an intersection in the
                        distance. My car is in the middle lane. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line separates my lane from the adjacent lane on the left; no
                        curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the adjacent lane on the right; the
                        roadside curb is beyond that adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.
Step 4  Cross-check     position: Lane 2 of 3 agrees with a same-direction lane beyond each boundary. | roles:
                        Both white solid boundaries fit no-crossing lane lines on an intersection approach. |
                        markings: The straight-only arrow agrees with the solid approach boundaries; the turn
                        arrows in neighboring lanes do not govern my lane. | unseen: No distant stop line or
                        waiting area is identifiable, and none is inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing the left
                        boundary. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing the right
                        boundary. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right lane boundary prohibits
                        crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane without crossing either solid boundary. For a turn,
                        select the appropriate turn lane before the solid-line section rather than changing
                        lanes here; obey the intersection signals and stop before the stop line if required
                        when it becomes visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 917, 14.97 s

culane_test__d193_06051123_0635_02160 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signalized intersection. My car is in the
                        rightmost approach lane, with a painted channelizing area and sidewalk to its right;
                        the full set of same-direction lanes extends beyond the left side of the image. (lanes
                        None, mine None, insufficient)
Step 2  Left            A continuous solid white line separates my lane from another approach lane on the
                        left; no curb is present along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line curves along the right side of my lane, with white diagonal
                        channelizing stripes beyond it and a raised sidewalk farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white arrow has a single head pointing right, connected to a
                        bent stem; no straight-ahead head is visible.; line:stop_line (full): A transverse
                        solid white stop line spans the lane ahead, immediately before the pedestrian
                        crossing.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane on the left, and the
                        right edge confirms the rightmost position; the total lane count and numerical index
                        cannot be established from the cropped left side. | roles: The solid white left
                        boundary fits an intersection approach lane line, and the solid white right boundary
                        fits a roadway edge alongside a channelizing buffer. | markings: The right-only arrow
                        agrees with the rightmost approach position; the stop line does not add another
                        permitted movement. | unseen: No lane count or numerical index is inferred from the
                        cropped roadway. The diagonal striped area lies outside my lane, and the crosswalk is
                        beyond its stop line. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing into the
                        adjacent lane. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid longitudinal boundary normally prohibits crossing to the
                        right, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:right: The right-only arrow permits a right turn and excludes straight travel, a
                        left turn, and a U-turn from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     prohibited (correct): The right-only arrow does not permit straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The right-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      allowed (correct): The right arrow permits a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The right-only arrow does not permit a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a right turn only, remaining left of the striped channelizing area;
                        do not cross either solid boundary. Obey the applicable signals, stop before the stop
                        line when required, and yield to pedestrians in the crossing ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1281, 25.42 s

culane_test__d193_06051123_0635_03690 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signalized intersection with a pedestrian
                        crossing. My car is in the middle of three visible motor-vehicle approach lanes.
                        (lanes 3, mine 2, full)
Step 2  Left            Two closely spaced solid white lines run along my left side toward the intersection,
                        with a left-turn lane beyond and no curb.
                        white double_solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along my right side toward the intersection, separating my
                        lane from another motor-vehicle lane, with no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.;
                        line:stop_line (full): A transverse solid white stop line crosses the end of my
                        approach lane before the pedestrian crossing.; line:crosswalk (full): White zebra-
                        crossing stripes extend across the roadway immediately beyond the stop line.
Step 4  Cross-check     position: Lane lines on both sides agree with my position in lane 2 of 3, with a same-
                        direction lane on each side. | roles: Both boundaries are white and separate same-
                        direction lanes; their solid appearance is consistent with restricted crossing on an
                        intersection approach. | markings: The straight-only arrow agrees with a dedicated
                        through approach lane bounded by solid lines; the stop line precedes the crosswalk. |
                        unseen: No hidden arrow, waiting area, pavement text or other guidance marking has
                        been inferred. | result: consistent
Step 5  Rule            left_boundary: The visible solid white lines normally prohibit crossing to the left;
                        the supplied lane-line passages do not specifically describe this double-solid white
                        configuration. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits crossing into the lane on my
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: The supplied passages contain no specific crosswalk rule, and this
                        marking does not determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): Crossing the solid left boundary is normally prohibited by
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight, and do not cross either solid boundary here;
                        turning requires selecting an appropriate turn lane before the solid-line approach.
                        Obey the traffic signal, stop before the stop line when required, and watch for
                        pedestrians at the crossing.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1312, 25.29 s

culane_test__d193_06051411_0691_03960 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road continues ahead with a central separation fence on the left and shops
                        and parked vehicles on the right. My car is in the left lane of two apparent same-
                        direction lanes; the lane divider is faint. (lanes 2, mine 1, partial)
Step 2  Left            A continuous white line runs along the left of my lane beside a raised separator and
                        metal fence; a yellow strip is visible farther left at the separator base, with
                        opposing traffic beyond the fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A faint white broken divider, with visible painted stretches and intervening gaps,
                        runs to my right; roadway continues beyond it toward parked vehicles, but the paint is
                        worn and partly obscured by the hood.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider support my position as the
                        leftmost of two apparent same-direction lanes. | roles: The broken white divider fits
                        a same-direction lane line. The left line appears white despite the rule specifying
                        yellow for a left edge; its edge role follows the visible physical separator, not an
                        assumed paint colour. | markings: No readable arrows, words, symbols, transverse lines
                        or waiting areas are visible in my lane. | unseen: The right divider is faint, so the
                        lane count remains uncertain. No intersection or markings beyond the visible road are
                        inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the physical separator also prevents a normal lane change. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible broken white lane divider permits changing into the
                        adjacent same-direction lane. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised separator lies beyond it.
Step 6  change_right    allowed (correct): The identifiable broken white lane divider permits crossing under
                        CN-5.2.3, subject to checking traffic.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the left separator; a rightward lane change is permitted across the
                        broken divider only after checking traffic and clearance from parked vehicles. No
                        visible lane-use arrows or stop line establish turn assignments or a stopping
                        position.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 913, 21.09 s

culane_test__d193_06051603_0727_01080 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane right-hand branch of a divided urban road, beside a
                        painted separation area that leads into a physical divider. The branch continues
                        ahead; no intersection or lane ending is visible. (lanes 1, mine 1, full)
Step 2  Left            A worn solid white line borders a wedge of diagonal white hatching on the left, with
                        other traffic lanes beyond; farther ahead the separation becomes a physical divider.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A concrete barrier with a raised base forms the right edge; no separate painted
                        boundary line is clearly visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        area:channelizing (full): A tapered white outlined area with diagonal white infill
                        adjoins the left edge of the lane and leads toward the divider.
Step 4  Cross-check     position: The single lane is bounded by the separation area and divider on the left
                        and a concrete barrier on the right; neither boundary separates two lanes within this
                        branch. | roles: The white outline separates same-direction road branches, and the
                        right physical barrier forms the roadway edge. | markings: The channelizing area
                        agrees with the road split. No lane-use arrows, words, stop lines or waiting areas are
                        visible in the ego lane. | unseen: No hidden arrow or destination movement has been
                        inferred; the channelizing area is beside the lane rather than a usable part of it. |
                        result: consistent
Step 5  Rule            left_boundary: The channelizing outline and infill prohibit driving across the left
                        boundary into the separation area. [CN-6.6.1-3] "Channelizing lines show that vehicles
                        must follow the set path and may not drive on or across the lines. ... Channelizing
                        lines separating traffic in the same d"
Step 5  Rule            right_boundary: No supplied passage specifically governs crossing a concrete barrier;
                        the physical edge makes leaving the lane to the right prohibited under the action
                        definitions.
Step 5  Rule            area:channelizing: Vehicles must follow the designated path and may not drive on or
                        across the channelizing markings. [CN-6.6.1-3] "Channelizing lines show that vehicles
                        must follow the set path and may not drive on or across the lines. ... Channelizing
                        lines separating traffic in the same d"
Step 6  change_left     prohibited (correct): CN-6.6.1-3 prohibits crossing the channelizing outline and
                        hatching; a physical divider continues ahead.
Step 6  change_right    prohibited (correct): The concrete barrier forms a non-crossable physical edge.
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
Advice                  Remain on this branch between the separation area and the right barrier; do not cross
                        the hatching to reach the lanes on the left. No intersection movement guidance or
                        stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['area:channelizing'], missed []), actions True, unsafe [], citation
                        in_pack_not_accepted, contradictions []
Tokens                  in 8604, out 974, 17.88 s

culane_test__d193_06051603_0727_01620 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An elevated, barrier-lined ramp curves left ahead. My car is on a single unmarked
                        carriageway; no intersection or lane ending is visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous concrete barrier with a metal rail forms the left edge; a pale pavement
                        margin runs beside it, but no distinct painted boundary line is visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A continuous concrete barrier forms the right edge, with a narrow gutter-like pavement
                        margin beside it and no distinct painted boundary line visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The two physical roadway edges and absence of an internal lane divider agree
                        with one lane, indexed 1. | roles: Both boundaries are physical roadway edges rather
                        than painted lane lines; edge_line describes their position. | markings: No guidance
                        markings are visible in my lane, so there is no conflict with the boundaries. |
                        unseen: No paint colour or pattern is inferred from the pale pavement margins; the
                        road beyond the visible curve is not assessed. | result: consistent
Step 5  Rule            left_boundary: No supplied passage specifically governs crossing a concrete barrier;
                        the physical-edge definition makes moving across this boundary prohibited.
Step 5  Rule            right_boundary: No supplied passage specifically governs crossing a concrete barrier;
                        the physical-edge definition makes moving across this boundary prohibited.
Step 6  change_left     prohibited (correct): The concrete barrier is a physical edge that cannot be crossed.
Step 6  change_right    prohibited (correct): The concrete barrier is a physical edge that cannot be crossed.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the leftward road curve is not a turn arrow.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay between the barriers and follow the ramp's leftward curve, guided also by the
                        visible chevron signs. No intersection movement or stopping location is marked in the
                        visible stretch.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation none, contradictions []
Tokens                  in 8604, out 837, 14.89 s

culane_test__d193_06051734_0757_00000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided expressway continues straight ahead, with no intersection, ramp or lane
                        ending visible. My car is in the middle of three lanes travelling in this direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        travel lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        travel lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with a same-direction lane beyond each boundary. | roles:
                        Both broken white boundaries fit crossable same-direction lane lines. | markings: No
                        arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No hidden lane-end markings or distant features have been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the adjacent lane on
                        the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent lane on
                        the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in your current lane; either adjacent lane may be entered across the broken
                        white line after checking traffic and signalling. No turning facility, waiting area or
                        stop line is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8604, out 750, 9.25 s

culane_test__d193_06051734_0757_02430 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided highway with three lanes in this direction continues straight ahead; no
                        intersection or lane ending is visible. My car is in the middle lane. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps ahead separates my lane from another
                        same-direction lane on the right; its nearest portion is hidden by the hood, and no
                        curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One same-direction lane on each side agrees with three lanes and ego lane
                        index 2. | roles: Both broken white boundaries fit crossable same-direction lane
                        lines; the outer solid lines and barriers are not my lane boundaries. | markings: No
                        arrows, words, symbols, marked areas or transverse traffic markings are visible in my
                        lane. | unseen: The hood hides the nearest right-boundary segment, but its color and
                        broken pattern are visible farther ahead; no hidden markings or intersection movements
                        are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to change into the lane on
                        the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane line permits my car to change into the lane on
                        the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either dashed boundary may be crossed for a lane change
                        after checking traffic and blind spots. No intersection movement guidance or stopping
                        point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 853, 12.81 s

culane_test__d193_06051734_0757_04050 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A single-lane ramp curves right toward an overpass, with guardrails on both sides. My
                        car is in the sole travel lane; no intersection or lane ending is visible. (lanes 1,
                        mine 1, full)
Step 2  Left            A single solid white line follows the left edge of the lane, with a narrow paved
                        margin, raised concrete edge and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line curves right along the lane, with a paved shoulder, raised
                        concrete edge and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edge lines, consistent with one travel lane and
                        ego lane index 1. | roles: Both solid lines visibly mark roadway edges rather than
                        separating travel lanes. The left paint is white, despite the supplied convention
                        specifying yellow for a left edge line; its observed color is retained. | markings: No
                        arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: The road beyond the bend is not visible; no markings or lane
                        destination are inferred there. | result: Consistent in lane geometry; the visible
                        white left edge differs from the supplied color convention.
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, with an exception
                        for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the rightward road curve is not a turn arrow.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary restrictions govern only crossing their respective sides, and no
                        intersection movement permission is inferred from the road's curvature.
Advice                  Stay between the solid white lines and follow the ramp's rightward curve; do not move
                        onto either roadside margin. The roadside chevrons warn of the bend, and no stop line
                        is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 890, 14.19 s

culane_test__d193_06060642_0768_00360 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A straight, tree-lined two-way road continues ahead, with two lanes in this direction.
                        My car is in the rightmost lane, beside a landscaped roadside strip; no intersection
                        or lane ending is clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible segments and gaps follows the right road edge,
                        immediately alongside a raised curb and landscaped strip.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and position 2 agree with a lane line on the left
                        and a road edge on the right. | roles: The broken white left line fits a crossable
                        same-direction lane divider; the white right line fits a right-hand edge line,
                        alongside a physical curb. | markings: No arrows, words, symbols, transverse lines or
                        waiting areas are visibly painted in my lane. | unseen: No unseen intersection layout
                        or distant lane-use marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the same-direction
                        lane on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The broken white marking is an edge-line form, but it does not
                        authorize driving over the raised curb that physically bounds this side of my lane.
                        [CN-5.4.2] "Carriageway edge lines take the forms of solid, broken and broken-solid
                        lines. ... The broken edge line has 60 cm segments and 30 cm gaps (also called a
                        "dense "
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The raised curb physically bounds the lane; the broken edge
                        marking does not make the curb a traversable exit.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the lane and keep clear of the right curb; a left lane change is
                        permitted by the broken divider when safe. No visible lane-use arrows determine
                        movements at the next intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1026, 26.18 s

culane_test__d193_06060642_0768_00900 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road curves gently right, with no intersection or lane ending clearly
                        visible ahead. My car is in the rightmost of two lanes in its direction. (lanes 2,
                        mine 2, full)
Step 2  Left            A broken white line, with a visible long dash and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs beside a raised curb, with a planted strip and parked
                        vehicles beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge agree with my car occupying lane 2
                        of 2. | roles: The broken white left line fits a same-direction lane separator; the
                        solid white right line beside the curb fits a roadway edge. | markings: No arrows,
                        text, symbols, transverse lines or marked waiting areas are visible in my lane. |
                        unseen: No unseen markings or intersection movements have been inferred; the distant
                        lane endpoint is not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane separator allows my car to change left when safe.
                        [CN-5.2.3] "On roads with two or more lanes in the same direction, the crossable lane
                        line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing, and the raised
                        curb is not a usable lane-change route. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line prohibits normal crossing under
                        CN-4.2.2-a, with a raised curb beyond.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Follow the road's gentle right curve within your lane; change left across the broken
                        line only when safe, and do not cross the solid right edge or curb. No visible lane-
                        use arrows establish which lane to use for turns at a later intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 782, 13.8 s

culane_test__d193_06060642_0768_03060 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road runs beside an elevated roadway, with an intersection approach
                        farther ahead. My car is in the rightmost of three visible lanes in this direction.
                        (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from the lane
                        occupied by the green bus; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane, with a narrow paved strip and a raised
                        sidewalk curb farther to its right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (partial): A small white arrow-like marking is visible far ahead in my
                        lane; a rightward-pointing portion is discernible, but its complete shape and any
                        additional head cannot be resolved.
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my
                        position in lane 3 of 3. | roles: The broken white separator fits a same-direction
                        lane line, and the solid white line fits the right roadway edge. | markings: The
                        distant arrow is within my lane, but its incomplete visibility prevents confirming
                        whether it indicates right only or a combined movement. | unseen: No complete arrow
                        shape, stop line, crossing, or waiting area is claimed; the intersection approach is
                        too distant to resolve all markings. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing left when safe. [CN-5.2.3]
                        "On roads with two or more lanes in the same direction, the crossable lane line shall
                        be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right boundary is normally prohibited, except in a
                        safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            arrow:right: A rightward arrow permits a right turn, but the unresolved remainder
                        prevents deciding whether another movement is also indicated. [CN-5.13.1] "Guide
                        arrows indicate the direction of travel for vehicles. (Table 1 meanings: straight
                        ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3, subject
                        to a safe gap.
Step 6  change_right    prohibited (correct): The solid white boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_determined: The distant arrow is only partly readable; an additional straight head
                        cannot be confirmed or excluded.
Step 6  turn_left       not_determined: The complete distant arrow cannot be resolved, so its full movement
                        restriction is uncertain.
Step 6  turn_right      allowed: The discernible rightward arrow portion permits a right turn under CN-5.13.1.
Step 6  u_turn          not_determined: The complete distant arrow cannot be resolved, so its full movement
                        restriction is uncertain.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Remain inside the solid right edge line; a left lane change is permitted only when
                        clear of the bus and other traffic. Confirm the distant arrow and junction controls
                        before committing to a movement, as the photograph does not resolve the complete arrow
                        or a stopping position.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1096, 23.24 s

culane_test__d193_06060748_0790_02970 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A wide, divided multilane road with dense traffic ahead; no intersection or lane
                        ending is visible. My car is in an interior lane behind the red hatchback, but
                        vehicles and the cropped road edges prevent a reliable count of all lanes. (lanes
                        None, mine None, insufficient)
Step 2  Left            A broken white line separates my lane from the lane containing the white van on the
                        left; a dash and its forward gap are visible, with no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white longitudinal stripe separates my lane from the lane containing the large cream
                        minibus; its continuation is obscured by the minibus, so a solid or broken pattern
                        cannot be established reliably, and there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries separate same-direction lanes, placing my lane in the
                        interior of the carriageway; the total lane count and exact index remain uncertain. |
                        roles: The white paint and adjacent same-direction vehicles support lane-line roles.
                        Only the left boundary's broken pattern is established; the right stripe is locally
                        continuous but its overall pattern is obscured. | markings: No readable arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. | unseen: The right
                        boundary's locally solid appearance does not establish a no-crossing line. Traffic
                        hides the road farther ahead, so unseen markings and the next intersection's lane
                        directions are not inferred. | result: consistent
Step 5  Rule            left_boundary: The visible broken white lane line permits changing to the adjacent
                        lane on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: A broken line permits crossing and a solid line normally prohibits it,
                        but the obscured pattern prevents deciding which applies on the right. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    not_determined (WRONG, label allowed): The right boundary's solid-versus-broken
                        pattern is obscured, leaving the applicable crossing restriction undecided.
Step 6  go_straight     not_applicable: No visible marking governs this action.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         Consistent: the uncertain right boundary does not establish permission to cross, and
                        no intersection movements are inferred from lane boundaries.
Advice                  Maintain a safe following distance in the queue; a left lane change is permitted by
                        the marking only when a safe gap exists. Do not assume you may cross the right
                        boundary until its pattern is clear; no visible arrow establishes the lane to use for
                        a future turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1267, 31.2 s

culane_test__d193_06060919_0820_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way street continues ahead, with opposing traffic on the left and parked
                        cars along the right curb. My car is in the single visible travel lane in its
                        direction; no intersection or lane ending is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A worn yellow broken line lies to the left of my car, with visible painted segments
                        and gaps; opposing traffic is beyond it and there is no curb.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           The roadway meets a raised curb on the right, partly obscured by parked cars and
                        pedestrians; no painted boundary is visible.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The center line on the left and roadside curb on the right agree with one
                        travel lane in my direction, with my car in lane 1. | roles: The broken yellow line
                        fits an opposing-traffic center line; the curb forms the physical road edge on the
                        right. | markings: No visible arrows, words, symbols, transverse lines or waiting
                        areas contradict the boundaries. | unseen: No markings are inferred beneath parked
                        vehicles, and no intersection-end markings are inferred beyond the visible road. |
                        result: consistent
Step 5  Rule            left_boundary: The broken yellow center line may be crossed to overtake or turn only
                        when doing so does not affect safety. [CN-5.1.1] "The crossable centre line separates
                        traffic flows in opposite directions. It means vehicles may cross the line to
                        overtake, turn or make a U-turn when this does"
Step 5  Rule            right_boundary: No supplied passage directly governs crossing a curb; under the
                        physical-boundary definition, moving across this raised road edge is prohibited.
Step 6  change_left     allowed (correct): CN-5.1.1 permits crossing the broken yellow center line when safe,
                        subject to opposing traffic.
Step 6  change_right    prohibited (correct): The raised curb forms a physical road edge and prohibits moving
                        across it.
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
Step 7  Reflect         Consistent: the center line governs only crossing left, the curb governs only crossing
                        right, and neither is used to decide movements at an unseen intersection.
Advice                  Remain in the travel lane and leave clearance from parked cars and pedestrians on the
                        right. Cross the broken center line only when safe and clear of opposing traffic; no
                        visible markings establish turn permissions or a stopping position ahead.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 960, 21.06 s

culane_test__d193_06060925_0822_01260 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road with three lanes in this direction runs beside an elevated
                        roadway. My car is in the rightmost lane; no intersection or lane ending is clearly
                        visible ahead. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line follows the right roadway edge beside a raised curb and metal
                        pedestrian fence, with a narrow paved strip between the line and curb.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 3 agree with a same-direction lane line on the
                        left and a roadway edge on the right. | roles: The broken white left line fits a
                        crossable lane divider; the solid white right line fits the right carriageway edge. |
                        markings: No guidance arrows, words, symbols, transverse lines or marked waiting areas
                        are visible in my lane. | unseen: No distant intersection layout or markings obscured
                        by traffic are inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent lane
                        on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: Crossing the solid right boundary is normally prohibited; the raised
                        curb also forms a physical limit. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits a left lane change under
                        CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white boundary prohibits normal crossing under
                        CN-4.2.2-a, with a curb beyond.
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
Advice                  Stay within the right edge line; a left lane change is permitted by the broken divider
                        after checking traffic. No visible lane-use arrows establish which lane to use for a
                        turn at the next intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 861, 15.84 s

culane_test__d193_06060925_0822_02700 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad divided urban road continues straight ahead, with a planted median on the left
                        and a planted roadside separator on the right. My car is in the third of four lanes
                        travelling in this direction; no intersection or lane ending is clearly visible.
                        (lanes 4, mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside curb lies beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four lanes with my car in lane 3 agrees with two lanes to the left, one to
                        the right, and lane-line boundaries on both sides. | roles: Both boundaries are broken
                        white lines, consistent with separation of same-direction lanes. | markings: No
                        readable arrows, words, symbols, transverse lines or marked waiting areas are visible
                        in my lane. | unseen: No movement guidance is inferred from the distant road, and no
                        markings hidden by vehicles or the hood are asserted. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to change into the adjacent
                        lane on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The broken white lane line permits my car to change into the adjacent
                        lane on the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     allowed (correct): The broken white lane line allows a lane change under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line allows a lane change under CN-5.2.3.
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
Advice                  You may change lanes across either broken white boundary after checking traffic and
                        blind spots. No lane change is indicated as necessary here; choose a turn lane only
                        when subsequent arrows or signs identify it.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 939, 16.88 s

culane_test__d193_06060925_0822_04140 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight toward an overpass, with three lanes in this
                        direction. My car is in the rightmost lane; no intersection stop line or lane ending
                        is visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a visible long dash and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A faint continuous white line follows the right road edge beside a raised curb, with a
                        sidewalk and railing beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow immediately ahead has a single forward-pointing
                        head and no turning branch.
Step 4  Cross-check     position: Three lanes and position 3 agree with a same-direction lane line on the left
                        and a road edge on the right. | roles: The broken white left boundary fits a crossable
                        lane line; the solid white right boundary and curb fit the right roadway edge. |
                        markings: The straight arrow is compatible with the continuing lane; no conflicting
                        word, symbol or waiting area is visible. | unseen: No markings beyond the readable
                        stretch or behind vehicles are inferred; the distant lane endpoint is not visible. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the lane on the left
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited; the curb
                        also forms a physical roadway edge. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only arrow permits straight travel and excludes left
                        turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken line when safe; do
                        not cross the right edge toward the curb. For a turn or U-turn, find an appropriately
                        marked lane farther ahead rather than turning from this straight-only lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 996, 17.56 s

culane_test__d193_06060925_0822_04320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues beneath a pedestrian
                        footbridge. My car is in the middle lane; a bus stop is on the right, and no
                        intersection or lane ending is clearly visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from another
                        traffic lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with broad visible dashes and gaps separates my lane from the
                        traffic lane beside the bus stop; the roadside curb is beyond that lane, not at my
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my position in lane 2 of 3. | roles:
                        Both white broken boundaries fit separation of traffic travelling in the same
                        direction. | markings: No guidance marking is readable within my lane; the arrow
                        visible to the left belongs to the adjacent lane. | unseen: The distant lane surface
                        is partly obscured by vehicles and perspective; no unseen arrows, bus-lane
                        designation, or intersection markings have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane boundary permits changing into the adjacent left
                        lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane boundary permits changing into the adjacent
                        right lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     allowed (correct): The visible broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    allowed (WRONG, label prohibited): The visible broken white lane line permits crossing
                        under CN-5.2.3; no special-lane designation is readable.
Step 6  go_straight     not_applicable: No visible marking in my lane governs this movement.
Step 6  turn_left       not_applicable: No visible marking in my lane governs this movement.
Step 6  turn_right      not_applicable: No visible marking in my lane governs this movement.
Step 6  u_turn          not_applicable: No visible marking in my lane governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Either broken boundary permits a lane change when safe; check for buses and any posted
                        restrictions before moving right. No visible lane-use arrow establishes turn
                        permissions, and no stop line is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8604, out 933, 18.51 s

culane_test__d193_06060925_0822_04680 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with a side-road junction beyond the planted
                        island on the right. There are three lanes in this direction, and my car is in the
                        rightmost lane. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along the right side of my lane, with a narrow paved margin
                        and a raised curb beside the planted island beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A faded white arrow has one forward-pointing head and a
                        straight shaft in my lane.
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my lane
                        being lane 3 of 3. | roles: The broken white line fits a crossable same-direction lane
                        divider; the solid white line fits the right roadway edge. | markings: The straight
                        arrow is compatible with the continuing lane and both boundaries; no conflicting
                        guidance marking is visible. | unseen: No distant stop line, additional arrow, or
                        waiting area has been inferred; the roadway farther ahead is partly obscured by
                        vehicles and distance. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits my car to change into the
                        adjacent lane on the left when safe. [CN-5.2.3] "On roads with two or more lanes in
                        the same direction, the crossable lane line shall be used on sections where vehicles
                        may change lanes."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing to the paved
                        margin, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns, and U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed: The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited: The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; do not cross the solid right edge line. If a turn is
                        needed, change left safely across the broken divider and find a lane marked for the
                        intended movement.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1084, 21.97 s

culane_test__d193_06060925_0822_05310 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with a planted median on the left and a raised
                        strip separating a parallel roadway on the right. My car is in the rightmost of three
                        visible lanes; no intersection or lane ending is clearly visible. (lanes 3, mine 3,
                        full)
Step 2  Left            A worn broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with a narrow paved margin
                        and a raised curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The rightmost position in three lanes agrees with a same-direction lane line
                        on the left and a roadway edge on the right. | roles: The broken white left boundary
                        fits a crossable lane line; the solid white right boundary fits a right-hand
                        carriageway edge. | markings: No readable arrows, words, symbols or transverse
                        markings appear in my lane. The small hatched area farther ahead is outside its right
                        boundary. | unseen: No distant lane-use direction or intersection layout has been
                        inferred; details beyond the clearly visible road stretch are unresolved. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to change into the adjacent
                        same-direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, except in an
                        emergency when safe; the raised curb is also a physical boundary. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
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
Advice                  Stay within the right edge line; a move left across the broken line is permitted after
                        checking traffic. No visible lane-use marking establishes a turn choice or stopping
                        point, so check the markings and controls farther ahead before selecting a turning
                        lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 926, 17.53 s

culane_test__d37_05181608_0235_03090 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban road approaches a signal-controlled intersection. My car follows a taxi in a
                        channelized lane, with a painted separation area on the left and a roadside railing on
                        the right; vehicles and the channelization obscure a reliable count of the approach
                        lanes. (lanes None, mine None, insufficient)
Step 2  Left            A solid white line borders a white diagonal-painted separation area on the left; a
                        large yellow traffic drum obscures part of this side, with other traffic beyond.
                        white solid, curb no, other, evidence partial
Step 2  Right           A solid white line runs along the right side toward the intersection, with a physical
                        metal railing immediately beyond it separating this lane from roadside space.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A transverse solid white line is visible ahead to the right
                        of the taxi, while the taxi hides its continuation across the lane.; line:crosswalk
                        (partial): White pedestrian-crossing stripes cross the approach beyond the stop line;
                        the taxi obscures part of the crossing in my lane.
Step 4  Cross-check     position: The right edge and railing place my lane at the right side of the motor-
                        vehicle approach. The painted separation on the left does not establish how many same-
                        direction lanes exist, so neither lane count nor numerical lane position is assigned.
                        | roles: The solid white right edge fits the roadway-edge role. The left solid white
                        line outlines a painted separation rather than clearly serving as an ordinary lane
                        divider. | markings: The stop line and pedestrian crossing are consistent with an
                        intersection approach. No readable lane-use arrow is visible, and the taxi hides
                        pavement where one could be painted. | unseen: No turn arrow, lane-use restriction, or
                        waiting area has been inferred from lane position or the taxi's position. The obscured
                        parts of the approach remain uncertain. | result: consistent
Step 5  Rule            left_boundary: The solid outline of the adjacent diagonal-painted channelizing area
                        prohibits driving across it. [CN-6.6.1-3] "Channelizing lines show that vehicles must
                        follow the set path and may not drive on or across the lines. ... Channelizing lines
                        separating traffic in the same d"
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing, and the physical
                        railing also prevents an ordinary move to the right. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers pedestrian-crossing markings;
                        under the supplied definitions, this marking does not determine any of the seven
                        actions.
Step 6  change_left     prohibited (correct): The visible solid outline of the channelizing area prohibits
                        crossing under CN-6.6.1-3.
Step 6  change_right    prohibited (correct): The solid white boundary prohibits ordinary crossing under
                        CN-4.2.2-a, and a railing lies beyond it.
Step 6  go_straight     not_determined: The taxi obscures potential lane-use arrows, so the permitted
                        intersection movement cannot be determined.
Step 6  turn_left       not_determined: The taxi obscures potential lane-use arrows, so the permitted
                        intersection movement cannot be determined.
Step 6  turn_right      not_determined: The taxi obscures potential lane-use arrows; right-side lane position
                        alone does not establish permission to turn.
Step 6  u_turn          not_determined: The taxi obscures potential movement markings, so permission cannot be
                        determined.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Stay between the channelizing boundary and the right railing; do not change lanes
                        across either side here. Confirm the lane's movement markings when the taxi clears
                        them, obey the intersection signals, and stop before the stop line when required
                        without blocking the pedestrian crossing.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1289, 26.79 s

culane_test__d37_05181608_0235_03720 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road continues ahead, with opposing traffic behind the median fence
                        on the left. My car is in the leftmost lane; vehicles and perspective obscure the full
                        lane layout and the next intersection. (lanes None, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised median curb and metal fence, with
                        opposing traffic beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments separate my lane from the same-direction lane containing
                        the white hatchback; the hatchback and hood obscure part of the line.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left supports position 1, and the right lane line
                        confirms another same-direction lane; the total lane count remains uncertain. | roles:
                        The broken white right boundary fits a same-direction lane line. The left paint
                        appears white despite its position beside the median; its physical edge role is clear,
                        and its color has not been inferred from that role. | markings: No guidance arrows,
                        text, symbols, marked areas or transverse lines are visible in my lane. | unseen: The
                        distant lane end and pavement beneath vehicles are not visible; no markings there have
                        been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary, which also has a physical median curb and fence. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median curb and fence lie beyond it.
Step 6  change_right    allowed (correct): The visible broken white lane line permits a lane change under
                        CN-5.2.3, subject to safe clearance.
Step 6  go_straight     not_determined: The next intersection approach and any movement arrows there are
                        beyond the readable visible stretch.
Step 6  turn_left       not_determined: The next intersection approach and any movement arrows there are
                        beyond the readable visible stretch.
Step 6  turn_right      not_determined: The next intersection approach and any movement arrows there are
                        beyond the readable visible stretch.
Step 6  u_turn          not_determined: The next intersection approach and any movement restrictions there are
                        beyond the readable visible stretch.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the median; a rightward lane change is permitted by the broken line only
                        when there is a safe gap around the white hatchback. Check the next approach's arrows
                        and controls before choosing an intersection movement; no stopping position is visible
                        here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1058, 23.97 s

culane_test__d37_05181608_0235_05220 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A congested multilane urban road approaches a signal-controlled intersection. My car
                        is between other same-direction lanes, behind a dark sedan; traffic obscures the
                        roadway edges and the end of my lane. (lanes None, mine None, insufficient)
Step 2  Left            A white line appears continuous along the visible stretch on my left, with another
                        lane of queued vehicles beyond it and no curb at this boundary; vehicles obscure its
                        continuation.
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           A white line appears continuous along the visible stretch on my right, with another
                        lane of queued vehicles beyond it and no curb at this boundary; vehicles obscure its
                        continuation.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines and same-direction vehicles on both sides establish that my lane
                        is an interior lane, but the obscured outer lanes prevent a total count or an exact
                        index from the left. | roles: The visible white longitudinal lines fit same-direction
                        lane boundaries; their visible stretches appear solid. | markings: No guidance marking
                        or transverse line can be read in the exposed part of my lane; traffic hides much of
                        the pavement ahead. | unseen: No arrows, stop line, waiting area, or exact lane count
                        have been inferred from the queued vehicles or intersection context. | result:
                        consistent
Step 5  Rule            left_boundary: The visible solid white lane boundary prohibits my car from crossing to
                        the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The visible solid white lane boundary prohibits my car from crossing
                        to the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 6  change_left     prohibited (correct): The visible solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The visible solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: Queued vehicles hide the lane-use markings that would determine the
                        permitted intersection movements.
Step 6  turn_left       not_determined: Queued vehicles hide the lane-use markings that would determine
                        whether this lane permits a left turn.
Step 6  turn_right      not_determined: Queued vehicles hide the lane-use markings that would determine
                        whether this lane permits a right turn.
Step 6  u_turn          not_determined: Queued vehicles hide any arrow or prohibited-movement marking that
                        would determine U-turn permission.
Step 6  enter_waiting_areanot_determined: Traffic obscures the lane end and pavement directly to the left
                          farther ahead, so a marked waiting area cannot be established.
Step 7  Reflect         consistent
Advice                  Stay within the visible solid white boundaries and leave space behind the sedan.
                        Confirm the lane arrows and traffic signals as the queue advances; the correct lane
                        for each movement and the stopping position are not visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 925, 17.07 s

culane_test__d37_05181608_0235_05340 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A broad urban road has several same-direction lanes with dense queued traffic ahead.
                        My car is in an interior lane behind a dark sedan; vehicles obscure the distant
                        approach and prevent a reliable total lane count or lane index. (lanes None, mine
                        None, insufficient)
Step 2  Left            A single solid white line runs along the left of my lane, with another same-direction
                        traffic lane beyond it and no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, with another same-direction
                        traffic lane beyond it and no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines and same-direction vehicles on both sides establish an interior
                        lane, but the outer lanes cannot be counted reliably. | roles: Both solid white
                        boundaries fit same-direction no-crossing lane lines. | markings: No arrows, words,
                        symbols, marked areas or transverse lines are readable in the exposed portion of my
                        lane; traffic hides much of the lane ahead. | unseen: No lane count, exact lane index,
                        hidden arrow, stop line or waiting area has been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing the left
                        boundary. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing the right
                        boundary. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: Traffic obscures the lane ahead where a governing direction arrow
                        could be painted.
Step 6  turn_left       not_determined: Traffic obscures the lane ahead where a governing arrow or prohibition
                        could be painted.
Step 6  turn_right      not_determined: Traffic obscures the lane ahead where a governing arrow or prohibition
                        could be painted.
Step 6  u_turn          not_determined: Traffic obscures the lane ahead where a governing arrow or prohibition
                        could be painted.
Step 6  enter_waiting_areanot_determined: The distant approach and any potential waiting area are obscured by
                          queued vehicles.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines and maintain a safe gap behind the sedan. Wait
                        until lane arrows and the intersection approach become visible before choosing a
                        movement; no stopping position can be identified from this view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 860, 16.71 s

culane_test__d37_05181919_0299_02970 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road with three same-direction motor-vehicle lanes continues toward a
                        distant intersection. My car is in the rightmost lane behind a dark sedan, beside a
                        roadside strip with vehicles and pedestrians. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another motor-vehicle lane on the left; there is no curb along this line.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, separating it from the
                        roadside strip occupied by vehicles and two-wheelers; no raised curb forms this
                        immediate boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (partial): A white straight-ahead arrow is visible directly ahead of my
                        car; its forward portion is partly obscured by the sedan.
Step 4  Cross-check     position: The third of three lanes has another same-direction lane on its left and a
                        roadside edge on its right, consistent with the boundary roles. | roles: The broken
                        white left line fits a same-direction lane divider, and the solid white right line
                        fits a carriageway edge. | markings: The identifiable straight-ahead arrow agrees with
                        a through lane; no conflicting marking is visible. | unseen: The sedan obscures part
                        of the arrow and pavement farther ahead; no hidden stop line or additional guidance
                        marking is inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent lane
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right boundary is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-ahead guide arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The identifiable straight arrow permits this movement under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent; the partially obscured arrow remains identifiable, and boundary rules
                        govern only their respective crossing actions.
Advice                  Use this lane to continue straight, and do not cross the solid right edge into the
                        roadside strip. If you need to turn, select an appropriately marked lane where a safe,
                        permitted lane change is available; watch for vehicles entering from the right.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1134, 22.88 s

culane_test__d37_05181919_0299_03120 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection. My car is in a
                        through lane with traffic lanes on both sides; the far-left roadway is partly obscured
                        by the taxi. (lanes 4, mine 3, partial)
Step 2  Left            A solid white line runs along the left of my lane, with another same-direction lane
                        beyond it and no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along the right of my lane, separating it from the lane
                        occupied by the dark car ahead; the roadside railing is farther right, beyond that
                        lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A large white forward-pointing arrowhead is visible
                        immediately ahead of the hood; its lower shaft is hidden by the hood.; arrow:straight
                        (full): A smaller white straight-ahead arrow is visible farther ahead in the same
                        lane.
Step 4  Cross-check     position: The apparent four-lane layout places my lane third from the left, with same-
                        direction lanes on both sides, consistent with both boundaries being lane lines. The
                        far-left count remains partly obscured. | roles: Both boundaries are white solid
                        lines, consistent with no-crossing separation between same-direction lanes on an
                        intersection approach. | markings: The two visible straight arrows agree with each
                        other and with the solid approach-lane boundaries. | unseen: The nearest arrow shaft
                        is hidden, and traffic obscures parts of the distant approach; no hidden stop line,
                        crosswalk, or waiting area has been asserted. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            arrow:straight: The near straight-ahead arrow directs my car straight rather than
                        left, right, or into a U-turn. [CN-5.13.1] "Guide arrows indicate the direction of
                        travel for vehicles. (Table 1 meanings: straight ahead; straight or left; left;
                        straight or right; right; U-turn; straigh"
Step 5  Rule            arrow:straight: The farther straight-ahead arrow confirms that this lane is for
                        straight movement. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible straight arrows permit straight movement under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrows do not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrows do not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrows do not permit a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting-area or adjacent two-way left-turn-lane marking
                          governs this action.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines and proceed straight only when the traffic signal
                        permits; the visible signal ahead is red. Turning requires an appropriately marked
                        lane reached before the solid-line section, and the stopping position ahead must be
                        checked as queued traffic clears.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1339, 29.65 s

culane_test__d37_05190927_0395_02340 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches an intersection, with my car behind a truck in the
                        leftmost lane beside a planted median. At least three same-direction traffic streams
                        are visible, but vehicles obscure the far-right roadway edge and the exact lane count.
                        (lanes None, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised median curb, with planting and fencing
                        beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from the same-direction lane occupied by the
                        silver car; its farther portion is obscured by traffic.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left establishes my lane as the leftmost; the lane
                        line on the right separates another same-direction lane. The total count remains
                        uncertain. | roles: The solid white right boundary fits a no-crossing lane line. The
                        left paint appears white despite being beside the median; its edge role follows the
                        visible curb, not an assumed yellow colour. | markings: No guidance marking can be
                        read in the exposed portion of my lane; the truck hides much of the approach. |
                        unseen: No arrow, stop line, waiting area, or exact total lane count has been inferred
                        from the obscured pavement. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the raised median also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 6  change_left     prohibited (correct): The visible solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, with a raised median beyond.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The truck obscures the approach pavement where a lane-direction arrow
                        could determine this movement.
Step 6  turn_left       not_determined: The truck obscures any lane-direction or prohibited-turn marking
                        ahead.
Step 6  turn_right      not_determined: The truck obscures any lane-direction or prohibited-turn marking
                        ahead.
Step 6  u_turn          not_determined: The truck obscures any arrow or prohibited-U-turn marking ahead.
Step 6  enter_waiting_areanot_determined: Traffic obscures the lane end and any possible waiting-area entrance
                          ahead.
Step 7  Reflect         consistent
Advice                  Stay within the visible solid boundaries and leave space behind the truck. Confirm the
                        lane arrows, intersection controls, and stop line as they become visible before
                        choosing a movement or entering any waiting area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 951, 19.35 s

culane_test__d37_05190927_0395_02430 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches an intersection with a pedestrian crossing. My car
                        is in the leftmost approach lane beside a raised traffic island; a bus partly obscures
                        the lanes to the right. (lanes 3, mine 1, partial)
Step 2  Left            A raised concrete traffic-island curb forms the left edge of my lane; no painted
                        longitudinal line is clearly visible along it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from another same-direction lane on
                        the right.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; its lower shaft is obscured.; line:stop_line (full): A solid white
                        transverse stop line crosses my lane before the pedestrian crossing.; line:crosswalk
                        (partial): White zebra-crossing stripes extend across my lane ahead of the stop line,
                        with some portions obscured by vehicles.
Step 4  Cross-check     position: The island edge on the left agrees with my lane being leftmost, and the
                        right lane line confirms another same-direction lane. Three approach lanes appear
                        present, but the bus obscures part of the rightmost lane. | roles: The solid white
                        right boundary fits a same-direction lane separator; the raised island forms a
                        physical left roadway edge without clearly visible paint. | markings: The visible
                        forward arrowhead agrees with an intersection approach bounded by a solid lane line.
                        Its hidden lower portion prevents confidently excluding an additional arrow branch. |
                        unseen: No paint is inferred along the island, and no additional arrow head or waiting
                        area is inferred from obscured pavement. | result: consistent
Step 5  Rule            left_boundary: No supplied passage directly authorizes crossing a raised island curb;
                        as a physical boundary it prohibits moving left out of this lane.
Step 5  Rule            right_boundary: The solid white lane separator prohibits my car from crossing into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 5  Rule            arrow:straight: The visible forward arrowhead permits proceeding straight, but the
                        obscured lower arrow prevents determining whether another movement is also indicated.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks; this marking does
                        not determine any of the seven movement permissions.
Step 6  change_left     prohibited (correct): The raised island curb physically bounds the lane; crossing it
                        is prohibited.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (correct): The lower arrow is hidden by the hood, so an additional
                        left-turn branch cannot be excluded.
Step 6  turn_right      not_determined (correct): The lower arrow is hidden by the hood, so an additional
                        right-turn branch cannot be excluded.
Step 6  u_turn          not_determined (correct): The complete arrow is not visible, so its full movement
                        restriction cannot be established.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay within this lane for the visibly indicated straight movement; do not cross the
                        island curb or solid white separator. Confirm the complete lane arrow before
                        attempting any turn, and stop before the stop line when required while keeping the
                        pedestrian crossing clear.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1381, 27.26 s

culane_test__d37_05190927_0395_05220 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A tree-lined, two-way urban street with one visible travel lane in each direction and
                        vehicles parked along the right. My car is in the single forward lane; no intersection
                        or lane ending is clearly visible ahead. (lanes 1, mine 1, full)
Step 2  Left            A faint yellow line appears continuous along the left of my lane, with opposing
                        vehicles beyond it; the nearby cyclist and the hood obscure its nearest portion, and
                        no curb forms this boundary.
                        yellow solid, curb no, center_line, evidence partial
Step 2  Right           Two closely spaced solid white lines run along the right of my travel lane, with
                        parked vehicles beyond; the nearby black SUV obscures part of the roadside.
                        white double_solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One forward travel lane agrees with a centre line on the left and a roadside
                        parking boundary on the right. | roles: The yellow centre line separates opposing
                        traffic, while the white roadside lines separate the travel lane from parking. |
                        markings: No readable arrows, words, symbols, waiting areas or transverse markings are
                        visible in my lane. | unseen: The nearest left boundary and parts of the right
                        roadside are obscured; no hidden markings or intersection geometry are inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The visible single solid yellow centre line prohibits my car from
                        crossing to the left. [CN-6.1.4] "A single solid yellow line prohibits vehicles in
                        both directions from crossing. It is generally used on two-lane two-way roads with
                        limited sight distance or wh"
Step 5  Rule            right_boundary: The solid longitudinal white boundary normally prohibits crossing to
                        the right, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The visible solid yellow centre line prohibits crossing under
                        CN-6.1.4.
Step 6  change_right    prohibited (correct): The solid white roadside boundary normally prohibits crossing
                        under CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use marking governs this action; the centre line
                        governs boundary crossing, not an unseen intersection movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain between the visible solid boundaries and slow for the cyclist immediately ahead
                        and the parked SUV on the right. No visible arrow establishes an intersection
                        movement, and no stop line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 939, 19.08 s
```
