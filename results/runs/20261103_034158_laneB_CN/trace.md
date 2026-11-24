# Reasoning of lane run 20261103_034158_laneB_CN

```text
culane_test__d100_05251207_0380_01410 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A straight, tree-lined divided road continues ahead, with no intersection or lane
                        ending clearly visible. My car is in the rightmost of three same-direction motor-
                        vehicle lanes, beside a paved roadside strip used by a cyclist. (lanes 3, mine 3,
                        full)
Step 2  Left            A broken white line with clearly visible dashes and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from a paved roadside strip with a
                        cyclist; the raised sidewalk curb is beyond that strip, not directly along my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego position 3 agree with a lane line on the
                        left and an edge line on the right. | roles: The broken white left boundary fits a
                        same-direction lane divider; the solid white right boundary fits the motor-vehicle
                        carriageway edge. | markings: No arrows, words, symbols, transverse lines or waiting
                        areas are discernible in my lane. | unseen: No unseen intersection, lane-use arrow or
                        distant stop line has been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits my car to change into the lane on
                        the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The solid white edge line normally prohibits crossing to the roadside
                        strip, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
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
Advice                  Stay inside the solid right edge line and give the cyclist ample clearance; a left
                        lane change is permitted when safe. No visible arrow assigns an intersection movement,
                        and no stop line is discernible ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 912, 15.52 s

culane_test__d100_05251207_0380_02130 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, tree-lined road continues straight ahead, with no visible intersection or
                        lane ending. My car is in the middle of three lanes travelling in this direction.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; the roadside fence is beyond that lane, not at my
                        lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes with my lane second from the left agrees with a same-direction
                        lane line on each side. | roles: Both white broken boundaries fit crossable same-
                        direction lane lines. | markings: No arrows, words, symbols, transverse lines or
                        waiting areas are visible in my lane. | unseen: No intersection layout or markings
                        beyond the visible road stretch have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the adjacent lane on
                        the left. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent lane on
                        the right. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 6  change_left     allowed (correct): The left broken white lane line permits lane changes under
                        CN-5.2.3.
Step 6  change_right    allowed (correct): The right broken white lane line permits lane changes under
                        CN-5.2.3.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either adjacent lane may be entered across the broken
                        white line when safe. No intersection movement guidance or stop line is visible, so
                        select a turning lane only when further guidance becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 760, 9.83 s

culane_test__d100_05251207_0380_02190 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues straight ahead; no
                        intersection or lane ending is visible. My car is in the middle lane. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with being in lane 2 of 3. | roles: Both
                        broken white boundaries fit crossable lines separating same-direction lanes. |
                        markings: No arrows, words, symbols, transverse lines or marked waiting areas are
                        visible in my lane. | unseen: No unseen features are inferred; distant pavement
                        details cannot be resolved, and no intersection is visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the lane on the left
                        when safe. [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white lane line permits changing into the lane on the right
                        when safe. [[CN-5.2.3]]
Step 6  change_left     allowed (correct): The broken white lane line is crossable under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line is crossable under CN-5.2.3.
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
                        traffic and clearance. No visible markings assign intersection movements or a stopping
                        point; check guidance farther ahead before choosing a turning lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8604, out 824, 11.94 s

culane_test__d100_05251207_0380_02400 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues straight ahead, with no intersection or lane ending
                        visible. My car is in the middle of three same-direction lanes; vehicles are parked
                        along the far-right roadside. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from the
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible segments and gaps, separates my lane from the same-
                        direction lane on the right; the roadside curb lies beyond that lane, not at my lane
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying lane 2 of 3. | roles:
                        Both white broken boundaries fit separators between same-direction lanes. | markings:
                        No guidance arrows, text, symbols, transverse lines or waiting areas are visible in my
                        lane. | unseen: No markings are inferred beyond the visible road or beneath vehicles
                        and the hood. | result: consistent
Step 5  Rule            left_boundary: The broken white lane boundary permits changing into the adjacent left
                        lane when safe. [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white lane boundary permits changing into the adjacent
                        right lane when safe. [[CN-5.2.3]]
Step 6  change_left     allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
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
Step 7  Reflect         consistent
Advice                  You may remain in this lane or cross either broken white boundary when safe, checking
                        the van to the left and the delivery vehicle to the right. No visible marking
                        establishes an intersection turn assignment or stopping point; check the markings and
                        controls farther ahead before choosing a turn lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8604, out 850, 15.02 s

culane_test__d100_05251207_0380_03270 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban road continues straight ahead, with no intersection or lane ending
                        clearly visible. My car is in the rightmost of three lanes travelling in this
                        direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved roadside
                        strip and a raised sidewalk curb farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge line on the right agree with my
                        car occupying lane 3 of 3. | roles: The broken white separator fits a same-direction
                        lane line, and the solid white right boundary fits a carriageway edge line. |
                        markings: No readable arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No distant lane-use marking or intersection layout has
                        been inferred; the curb beyond the roadside strip is not treated as the immediate lane
                        boundary. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to change into the adjacent
                        left lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, except in an
                        emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain inside the solid right edge line; a left lane change is permitted after
                        checking traffic. No visible pavement arrow establishes a turn lane here, so check the
                        lane guidance farther ahead before choosing an intersection movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 931, 17.01 s

culane_test__d100_05251222_0385_01140 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead beside an elevated structure on the left, with no
                        intersection or lane ending visible. My car is in the leftmost of three same-direction
                        lanes. (lanes 3, mine 1, full)
Step 2  Left            A continuous white line runs along the left edge of my lane beside a raised curb, with
                        a narrow verge and metal guardrail beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with clearly visible long dashes and gaps separates my lane from
                        another same-direction lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left road edge and right lane divider agree with my lane being the
                        leftmost of three same-direction lanes. | roles: The broken white right boundary fits
                        a same-direction lane line. The left boundary is physically a road edge, although its
                        visible white paint differs from the yellow left-edge colour specified in CN-5.4.3;
                        its colour has not been inferred from its position. | markings: No arrows, words,
                        symbols, transverse lines or marked waiting areas are visible in my lane. | unseen: No
                        markings or intersection geometry have been inferred beyond the visible road; the hood
                        and vehicles conceal some pavement. | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, so my car must not
                        move left across it in ordinary driving. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits my car to change into the same-
                        direction lane on the right when safe. [CN-5.2.3] "On roads with two or more lanes in
                        the same direction, the crossable lane line shall be used on sections where vehicles
                        may change lanes."
Step 6  change_left     prohibited (correct): The solid left edge line prohibits normal crossing under
                        CN-4.2.2-a, and a raised curb also bounds that side.
Step 6  change_right    allowed (correct): The broken white lane line permits a right lane change under
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
Advice                  Keep within the left edge line and do not cross toward the curb or guardrail; a right
                        lane change is permitted after checking traffic. No visible markings establish turn
                        permissions or a stopping point, so follow the guidance encountered farther ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 929, 15.54 s

culane_test__d100_05251222_0385_01710 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches an intersection beside an elevated structure. My
                        car is in the second of four visible lanes travelling in this direction, behind a
                        silver sedan. (lanes 4, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the same-direction lane occupied by
                        the dark sedan on the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white longitudinal arrow shaft is visible behind the
                        silver sedan, but the sedan hides the arrowhead and any possible branches; a straight-
                        only direction cannot be confirmed.; line:crosswalk (partial): White pedestrian-
                        crossing stripes are visible across the approach ahead, with the portion in my lane
                        partly obscured by the silver sedan.
Step 4  Cross-check     position: The second-of-four position agrees with same-direction lanes beyond both
                        lane boundaries. | roles: Both white solid boundaries fit no-crossing lane lines on an
                        intersection approach. | markings: The partially visible arrow does not establish its
                        complete directions; the crossing does not resolve that uncertainty. | unseen: The
                        arrowhead, possible arrow branches, and pavement immediately beneath the silver sedan
                        are hidden; no stop line or waiting area is asserted beneath it. | result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits crossing to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: A guide arrow permits its indicated movements, but the hidden
                        arrowhead prevents identification of the complete permitted movements here.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the crosswalk, and it does not
                        determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined (WRONG, label allowed): The sedan hides the arrowhead that would
                        establish whether straight travel is indicated.
Step 6  turn_left       not_determined (WRONG, label prohibited): The sedan hides any arrow branches that
                        would establish whether a left turn is indicated.
Step 6  turn_right      not_determined (WRONG, label prohibited): The sedan hides any arrow branches that
                        would establish whether a right turn is indicated.
Step 6  u_turn          not_determined (WRONG, label prohibited): The sedan hides the complete arrow needed to
                        determine whether a U-turn is indicated.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Stay within the solid white boundaries and confirm the complete lane arrow when the
                        sedan no longer obscures it before selecting an intersection movement. Watch for
                        pedestrians at the crossing and obey the intersection signals; the stopping position
                        in your lane is obscured.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1226, 23.26 s

culane_test__d100_05251222_0385_02280 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A multilane urban road runs beside an elevated structure, with traffic ahead obscuring
                        the distant approach. My car is in the leftmost lane; the right side of the
                        carriageway is obscured, so the total lane count cannot be confirmed. (lanes None,
                        mine 1, partial)
Step 2  Left            A continuous white painted line follows a raised curb on the left, with a narrow
                        planted strip and metal guardrail beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments separated by clear gaps divide my lane from another same-
                        direction lane on the right, with no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge establishes my lane as leftmost, and the right lane
                        line confirms another same-direction lane; the total number remains obscured. | roles:
                        The broken white right boundary fits a same-direction lane line. The left boundary is
                        visibly white despite the supplied rule prescribing yellow for a left edge; its
                        curbside position establishes its edge role without changing the observed color. |
                        markings: No arrows, words, symbols, transverse lines, or waiting areas are visible in
                        my lane. | unseen: No distant arrows or stop line are inferred from the overhead
                        signs; traffic obscures the far portion of the lane. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary, which also has a physical curb. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane boundary permits changing into the adjacent
                        same-direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a curb lies alongside it.
Step 6  change_right    allowed (correct): The broken white lane line permits changing right under CN-5.2.3.
Step 6  go_straight     not_determined (WRONG, label prohibited): The distant lane approach is obscured, so
                        any movement-defining pavement arrow cannot be established.
Step 6  turn_left       not_determined (WRONG, label allowed): The distant lane approach is obscured, so any
                        movement-defining pavement arrow cannot be established.
Step 6  turn_right      not_determined (WRONG, label prohibited): The distant lane approach is obscured, so
                        any movement-defining pavement arrow cannot be established.
Step 6  u_turn          not_determined (WRONG, label allowed): The distant lane approach is obscured, so any
                        movement-defining pavement arrow or prohibition cannot be established.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Do not cross the solid left edge or curb; a right lane change is permitted by the
                        broken line, but the nearby car makes a careful gap check essential. Check the
                        overhead lane-direction signs and farther pavement markings before choosing your
                        intersection movement; the roadside U-turn sign indicates a facility 100 m ahead, not
                        an immediate turn.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left', 'arrow:u_turn']), actions False, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1058, 31.85 s

culane_test__d100_05251222_0385_02400 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs beside an elevated structure, with traffic continuing
                        ahead. My car is in the second of four same-direction lanes; traffic obscures the
                        distant lane markings and any intersection approach. (lanes 4, mine 2, full)
Step 2  Left            A continuous white solid line separates my lane from another same-direction lane on
                        the left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from another same-direction lane on
                        the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; its shaft and any possible branches are hidden by the hood.
Step 4  Cross-check     position: The second lane of four has a same-direction lane to its left and two to its
                        right, consistent with lane-line boundaries on both sides. | roles: Both boundaries
                        are white solid lines, consistent with no-crossing separators between same-direction
                        lanes. | markings: The visible forward arrowhead is compatible with the boundaries,
                        but its hidden lower portion prevents confirming whether it is a straight-only or
                        combined arrow. | unseen: No hidden arrow branches, distant stop line, or waiting area
                        have been assumed. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing the left boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing the right boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible forward arrowhead permits straight travel, but the hidden
                        remainder prevents establishing whether another direction is also indicated.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       not_determined (WRONG, label prohibited): The arrow's lower portion is hidden, so a
                        possible left branch cannot be checked.
Step 6  turn_right      not_determined (WRONG, label prohibited): The arrow's lower portion is hidden, so a
                        possible right branch cannot be checked.
Step 6  u_turn          not_determined (WRONG, label prohibited): The arrow's lower portion is hidden, so a
                        possible U-turn component cannot be checked.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Stay within the solid white boundaries; the visible arrowhead supports continuing
                        straight. Do not assume a turn is permitted until the complete lane arrow is visible;
                        no stopping position can be identified in this view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1178, 20.43 s

culane_test__d100_05251222_0385_04920 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection beneath an elevated
                        railway. My car is in a through lane, with one same-direction lane visible to the left
                        and another to the right; the truck obscures the far-right layout. (lanes None, mine
                        2, partial)
Step 2  Left            A single solid white line separates my lane from the same-direction lane on the left;
                        no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from the same-direction lane occupied by
                        the truck on the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted directly ahead of my
                        car.; line:stop_line (partial): A transverse white stop line is visible ahead, with
                        part of its span hidden by the car in front.; line:crosswalk (partial): White
                        pedestrian-crossing stripes lie beyond the stop line; the car ahead obscures part of
                        the crossing across my lane.
Step 4  Cross-check     position: Lane lines on both sides agree with an interior lane; one same-direction
                        lane is visible on the left, making my lane second from the left. The total count is
                        uncertain because the truck hides the far-right layout. | roles: Both solid white
                        boundaries fit same-direction no-crossing lane lines on an intersection approach. |
                        markings: The straight arrow agrees with a through guide lane bounded by solid white
                        lines and approaching a stop line and crossing. | unseen: No additional arrow beneath
                        the leading car or road boundary behind the truck is inferred; the transverse markings
                        are recorded as partially obscured. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing out of my lane to the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing out of my lane to the
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
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalk markings; this
                        crossing does not determine any of the seven lane-movement actions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane to proceed straight, subject to the traffic signals, and do not
                        cross either solid boundary. If required to stop, stop before the stop line and keep
                        the pedestrian crossing clear; turning requires selecting an appropriate lane before
                        the solid-line approach.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1497, 27.89 s

culane_test__d100_05251222_0385_05250 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided multilane road continues straight beneath and beyond an elevated roadway,
                        with no intersection or lane ending visible. My car is in the leftmost of three same-
                        direction lanes, alongside a hatched strip and median barrier. (lanes 3, mine 1, full)
Step 2  Left            A solid white line borders my lane on the left, with white diagonal hatching and a
                        metal median barrier farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left edge boundary and right lane divider agree with my car occupying
                        lane 1 of three same-direction lanes. | roles: The broken white right boundary fits a
                        same-direction lane divider. The left boundary functions as an edge beside a hatched
                        strip, although its visible white paint differs from the prescribed yellow for a left
                        carriageway edge; its observed color is retained. | markings: No arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. The diagonal
                        hatching lies outside its left boundary. | unseen: No intersection movements or
                        distant markings have been inferred; no lane end is visible. | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, except in an
                        emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits changing lanes to
                        the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid white left boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a lane change under
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
Advice                  Remain within the lane and do not cross the solid left boundary into the hatched
                        strip. You may change right across the broken divider when safe; no visible
                        intersection arrows or stop line establish turning permissions or a stopping position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1057, 19.87 s

culane_test__d100_05251309_0397_03150 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction approaches a junction area. My
                        car is in the rightmost lane, behind the SUV; the junction and the lane's end are not
                        clearly visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line runs beside a raised curb, with a planted separator and
                        a separate paved path beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (partial): A white combined straight-and-right arrow is visible
                        behind the SUV: the right-pointing head and branching shaft are clear, while the
                        forward head is obscured by the SUV.
Step 4  Cross-check     position: The lane line on the left and road edge on the right agree with my lane
                        being third from the left and rightmost of three lanes. | roles: The broken white
                        separator fits a same-direction lane line, and the solid white line beside the curb
                        fits a right roadway edge. | markings: The visible right arrowhead is compatible with
                        the rightmost lane; the apparent forward branch is partly hidden, so its head cannot
                        be confirmed. | unseen: The forward arrowhead, the lane's end, and any markings hidden
                        by vehicles or beyond the readable stretch are not treated as fully observed. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane separator permits changing into the adjacent lane
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing, and the
                        raised curb also forms a physical boundary. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight_right: The visible right-pointing head permits a right turn, but the
                        obscured forward head prevents fully confirming the other permitted movement.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white boundary prohibits normal crossing under
                        CN-4.2.2-a, and a curb lies immediately beyond it.
Step 6  go_straight     not_determined (WRONG, label allowed): The forward arrowhead is hidden by the SUV,
                        leaving straight-ahead permission unconfirmed.
Step 6  turn_left       not_determined (WRONG, label prohibited): The visible arrow points right, but its
                        other head is obscured, so the complete set of permitted directions cannot be
                        confirmed.
Step 6  turn_right      allowed (correct): The clearly visible right arrowhead permits a right turn under
                        CN-5.13.1.
Step 6  u_turn          not_determined (WRONG, label prohibited): Part of the arrow is obscured, preventing
                        confirmation of its complete directional restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  This lane visibly permits a right turn; confirm the obscured forward arrowhead before
                        relying on it for another movement. You may change left across the broken line when
                        safe, but do not cross the solid right edge or curb.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1061, 19.79 s

culane_test__d100_05251309_0397_03390 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad divided urban road approaches a signalized intersection. My car is in an
                        interior approach lane, with another lane on each side; the far-left lane layout is
                        not clear enough to count all lanes reliably. (lanes None, mine None, insufficient)
Step 2  Left            A solid white line separates my lane from the lane occupied by the white van on the
                        left; there is no curb along this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from another approach lane on the right; the
                        raised roadside island is beyond that adjacent lane, not at my boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrow is visible immediately ahead
                        of the hood, which hides the lower part of its shaft.; arrow:straight (full): A
                        smaller white straight-ahead arrow is visible farther ahead in the same lane.;
                        line:stop_line (partial): A transverse white line is visible at the intersection
                        approach, although its full width is difficult to distinguish at this distance.
Step 4  Cross-check     position: Both boundaries separate same-direction lanes, so my lane is an interior
                        lane; the total lane count and numerical position remain unresolved. | roles: The
                        solid white boundaries fit no-crossing lane lines on an intersection approach. |
                        markings: The repeated forward arrows agree with each other and with a straight-
                        through guide lane bounded by solid white lines. | unseen: The hood obscures the
                        nearest arrow's lower shaft, and distant details limit the stop-line observation;
                        neither hidden detail is treated as fully visible. | result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits crossing into the lane on the
                        left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The forward arrow permits proceeding straight and does not permit
                        turning left, turning right, or making a U-turn from this lane. [CN-5.13.1] "Guide
                        arrows indicate the direction of travel for vehicles. (Table 1 meanings: straight
                        ahead; straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            arrow:straight: The repeated forward arrow confirms the straight-ahead movement for
                        this lane. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 5  Rule            line:stop_line: The transverse stop line identifies where to stop when required to
                        wait or yield. [CN-6.4.1-2] "The stop line marks where vehicles stop when yielding or
                        waiting to proceed. It is a solid white line. ..."
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight-ahead arrows permit this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only lane arrows do not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only lane arrows do not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only lane arrows do not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or directly adjacent two-way left-
                          turn lane is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to proceed straight and do not cross either solid boundary. For a
                        turn, select an appropriately marked lane before the solid-line section; obey the
                        applicable signal and stop before the stop line when required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1896, 43.63 s

culane_test__d100_05251327_0403_00180 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban carriageway with three lanes in this direction continues toward a
                        distant overhead structure; no intersection or stop line is clearly visible. My car is
                        in the leftmost lane, beside a raised, landscaped roadside strip. (lanes 3, mine 1,
                        full)
Step 2  Left            A single solid white line runs along the left of my lane, with a narrow paved margin
                        and raised curb beyond it, followed by trees and landscaping.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long segments and gaps, separates my lane from
                        another lane travelling in the same direction; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is hidden by the hood.
Step 4  Cross-check     position: The left roadway edge and the same-direction lane on the right agree with
                        being lane 1 of 3. | roles: The broken white right boundary fits a crossable lane
                        line. The left boundary is visibly white and solid beside a curb; its physical
                        position establishes an edge line, although its white colour differs from the cited
                        convention for a left edge. | markings: The visible forward arrowhead is consistent
                        with the continuing lane; no conflicting word, symbol or marked waiting area is
                        visible. | unseen: The hood hides the lower portion of the arrow. No hidden arrow
                        shaft, distant stop line or intersection geometry has been asserted. | result:
                        consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken lane line permits changing into the adjacent same-direction
                        lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            arrow:straight: The visible straight-ahead guide arrow indicates proceeding straight,
                        rather than turning left, right or making a U-turn. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits ordinary crossing under
                        CN-4.2.2-a; a raised curb also lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     allowed (correct): The visible forward arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not indicate a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not indicate a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not indicate a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; do not cross the solid left edge. You may change right
                        across the broken line when safe, but a turn would require finding an appropriately
                        marked lane farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1067, 18.88 s

culane_test__d100_05251327_0403_00630 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined urban road continues ahead without a visible intersection or
                        lane ending. My car is in the left lane of two lanes travelling in this direction.
                        (lanes 2, mine 1, full)
Step 2  Left            A continuous pale white line runs along the left of my lane, with a narrow paved
                        margin and a concrete barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego lane 1 agree with a left roadway edge and a lane divider
                        on the right. | roles: The broken white right boundary fits a same-direction lane
                        line. The left solid line marks the physical roadway edge, although its visible white
                        colour differs from the supplied rule's usual yellow left-edge colour. | markings: No
                        arrows, text, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: No hidden markings or intersection features have been inferred; the lane
                        continues beyond the visible stretch. | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing, except in an
                        emergency when safe; the concrete barrier also prevents ordinary passage. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left edge prohibits normal crossing under CN-4.2.2-a,
                        with a concrete barrier beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits changing right under CN-5.2.3.
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
Advice                  Continue within your lane, or change right across the broken white divider after
                        checking traffic and clearance. Do not cross the solid left edge; no intersection
                        movement guidance or stopping point is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 880, 14.58 s

culane_test__d100_05251327_0403_00930 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead; no intersection or lane ending is clearly
                        visible. My car is in the leftmost of three visible lanes in this direction, beside a
                        landscaped median. (lanes 3, mine 1, full)
Step 2  Left            A single solid white line runs along the left of my lane, with a narrow paved strip
                        and a raised median curb beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has a single head pointing
                        straight ahead.
Step 4  Cross-check     position: The left edge beside the median and the same-direction lane to the right
                        agree with my lane being lane 1 of 3. | roles: The broken white right boundary fits a
                        same-direction lane line. The left boundary is visibly white despite its position at
                        the left roadway edge; its edge role follows from the median, not an assumed yellow
                        colour. | markings: The straight-only arrow is compatible with both boundaries; no
                        other readable guidance marking is visible in my lane. | unseen: No stop line, waiting
                        area or distant lane-end marking is inferred from the obscured and distant roadway. |
                        result: consistent
Step 5  Rule            left_boundary: The solid left edge line normally prohibits crossing it, except in an
                        emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            arrow:straight: The single straight arrow allows straight travel and does not permit
                        left turns, right turns or U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane; do not cross the solid line beside the median. If
                        you need a different movement, change right only when safe and select an appropriately
                        marked lane farther ahead; no stopping position is visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1088, 19.33 s

culane_test__d100_05251327_0403_01200 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, barrier-lined urban road continues ahead with three lanes in this
                        direction. My car is in the middle lane; no intersection, ramp or lane ending is
                        clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible painted segments and gaps separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible painted segments and gaps separates my lane from
                        another same-direction lane on the right; the roadside barrier is beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): White Chinese pavement text is visible ahead in my lane,
                        including a character resembling 环; the complete message farther ahead is obscured by
                        vehicles and distance.
Step 4  Cross-check     position: Three lanes and a middle-lane position agree with a same-direction lane line
                        on each side. | roles: Both boundaries are broken white lines, consistent with
                        crossable same-direction lane lines. | markings: The visible pavement text does not
                        conflict with either boundary; no readable directional arrow or marked waiting area is
                        visible in my lane. | unseen: The complete pavement message and markings beneath
                        vehicles cannot be read; no hidden arrow or direction is inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the lane on my left
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane line permits changing into the lane on my right
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            text:other: This is pavement text, but its incomplete message establishes no
                        permission or prohibition for the seven assessed actions. [CN-5.14.1] "Pavement text
                        markings are generally white. They are arranged vertically and read from near to far
                        along the direction of travel ... or horizontally from left t"
Step 6  change_left     allowed (correct): The broken white left lane line permits crossing under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white right lane line permits crossing under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action,
                        and no lane end is visible.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  You may cross either broken white boundary when safe, but no lane change is required
                        by the visible markings. Keep following the roadway and check later arrows and signs
                        for intersection directions; no stopping position is visible here.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation accepted, contradictions
                        []
Tokens                  in 8604, out 984, 16.22 s

culane_test__d100_05251327_0403_02340 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban roadway curves gently left, with a fenced parallel roadway on the left and a
                        sidewalk on the right. My car occupies the left of two apparent same-direction lanes;
                        no intersection or lane ending is visible. (lanes 2, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised curb and fence on the left, with a
                        separate roadway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A pale white continuous line separates my lane from a paved strip on the right; there
                        is no curb at this line, and the strip's traffic function is not visibly marked.
                        white solid, curb no, unknown, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left edge places my car leftmost. Two lanes are apparent, but the right-
                        hand strip could instead be a non-motorized lane, so the same-direction motor-lane
                        count is uncertain. | roles: The left boundary is visibly a white edge line beside a
                        curb, despite the usual yellow convention for a left edge. The right white line could
                        separate same-direction lanes or mark a motor/non-motor boundary; its role is
                        unresolved. | markings: No readable arrows, words, symbols, transverse lines or
                        waiting areas appear in the visible portion of my lane. | unseen: No traffic
                        designation is assigned to the right-hand strip, and no markings are inferred beyond
                        the visible road. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the adjacent raised curb also physically bounds the lane. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid longitudinal line normally prohibits crossing to the
                        right, regardless of the unresolved function of the adjacent strip. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No marking governs this action in the visible stretch.
Step 6  turn_left       not_applicable: No marking governs this action in the visible stretch.
Step 6  turn_right      not_applicable: No marking governs this action in the visible stretch.
Step 6  u_turn          not_applicable: No marking governs this action in the visible stretch.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid boundaries and follow the bend; do not cross either boundary
                        for an ordinary lane change. A roadside 30 km/h limit sign is visible, but no
                        intersection movement arrows or stopping position can be identified ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1111, 22.28 s

culane_test__d100_05251327_0403_03870 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A narrow urban road runs beside an elevated structure and curves ahead. My car is in
                        the left of two apparent same-direction lanes; the car ahead obscures much of my lane,
                        and no intersection or lane ending is visible. (lanes 2, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised curb and narrow paved walkway on the
                        left, with a wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears continuous over the exposed stretch to the right of my car, with
                        another paved traffic lane beyond; its continuation ahead is obscured by the car.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and edge line place my lane at the left edge of this
                        carriageway; the line and paved lane to the right support a tentative count of two
                        lanes. | roles: The white right-hand lane line fits separation of same-direction
                        traffic. The left edge paint is visibly white rather than the yellow normally
                        specified for a left carriageway edge; its physical position beside the curb supports
                        its edge-line role. | markings: No arrows, words, symbols, transverse lines or waiting
                        areas can be identified in the exposed portion of my lane. | unseen: The car ahead
                        hides much of the lane surface, and the lane's eventual end is not visible; no
                        markings are inferred in those areas. | result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal line normally prohibits crossing to the
                        left, where a raised curb also forms the physical road edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white lane separator prohibits crossing into the
                        lane on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling
                        in the same direction and prohibits vehicles on the solid-line side from crossing. It
                        has two forms: sin"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a curb lies immediately beyond.
Step 6  change_right    prohibited (correct): The exposed solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The lane's end and any movement-governing markings there are not
                        visible.
Step 6  turn_left       not_determined: The lane's end and any movement-governing markings there are not
                        visible.
Step 6  turn_right      not_determined: The lane's end and any movement-governing markings there are not
                        visible.
Step 6  u_turn          not_determined: The lane's end and any movement-governing markings there are not
                        visible.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay between the visible boundaries and leave space behind the car ahead; do not cross
                        the solid line on either side. Reassess lane-direction markings when the road ahead
                        becomes visible, since this photo does not establish which intersection movements your
                        lane permits.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1032, 20.01 s

culane_test__d100_05251327_0403_03960 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road runs beside an elevated structure and bends ahead. My car is in the left
                        of two apparent same-direction lanes, behind a sedan; no intersection or lane ending
                        is clearly visible. (lanes 2, mine 1, full)
Step 2  Left            A white line appears continuous along the raised left curb, with a narrow paved strip
                        and the structure wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white longitudinal line separates my lane from pavement to the right; only one
                        continuous stretch is visible between the sedan and the hood, so a repeating solid or
                        broken pattern cannot be established.
                        white none, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and the lane separator on the right agree with my lane
                        being the leftmost of two same-direction lanes. | roles: The white right separator
                        fits a same-direction lane line. The left line is visibly white despite its left-edge
                        position; its edge role follows from the adjacent curb, not an assumed yellow colour.
                        | markings: No guidance marking is readable in my lane, so there is no visible marking
                        conflict. | unseen: The right line's repeating pattern cannot be established. The
                        sedan and hood obscure pavement, and the lane's eventual end is outside clear view. |
                        result: consistent
Step 5  Rule            left_boundary: The visible solid longitudinal line normally prohibits crossing the
                        left boundary. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel,
                        take these forms: a solid line means crossing is normally prohibited, and may be
                        crossed in an emergen"
Step 5  Rule            right_boundary: Crossing permission depends on whether this line is solid or broken,
                        which the visible stretch does not establish. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left boundary normally prohibits crossing under
                        CN-4.2.2-a, and a raised curb lies immediately beyond.
Step 6  change_right    not_determined (WRONG, label prohibited): The right boundary's solid or broken pattern
                        is not established, so its crossing permission is undecided.
Step 6  go_straight     not_applicable: No visible marking governs this action.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the current lane and do not cross the solid left edge or curb. Before
                        moving right, obtain a clear view of the separator; the visible markings do not
                        establish which lane to use for a later turn.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1050, 20.54 s

culane_test__d100_05251627_0452_02850 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches an underpass with traffic queued ahead. My car is in
                        the leftmost lane beside a central fence; vehicles obscure the far-right lane layout
                        and the end of my lane. (lanes None, mine 1, partial)
Step 2  Left            A solid yellow line runs beside the raised base of a central metal fence, with
                        opposing traffic beyond it.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A worn white line appears continuous along the visible stretch between my lane and the
                        taxi's lane, but vehicles conceal its continuation ahead; no curb is visible.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The central fence and left edge line place my lane leftmost; the white lane
                        line confirms another same-direction lane on the right, but the total count is
                        obscured. | roles: The yellow left edge line and white same-direction separator fit
                        their assigned roles. | markings: No readable guidance markings are visible in my
                        lane; traffic conceals the farther pavement. | unseen: No arrows, stop line, or
                        waiting area have been inferred from the obscured road ahead. | result: consistent
Step 5  Rule            left_boundary: The solid yellow boundary normally prohibits crossing, and the central
                        fence also physically prevents moving left. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The visible solid white lane line prohibits crossing into the lane on
                        the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the
                        same direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid yellow boundary prohibits normal crossing under
                        CN-4.2.2-a, and a central fence blocks this side.
Step 6  change_right    prohibited (correct): The visible solid white lane separator prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: Traffic hides the lane-end pavement where any governing direction
                        arrow would be visible.
Step 6  turn_left       not_determined: Traffic hides the lane-end pavement where any governing direction
                        arrow would be visible.
Step 6  turn_right      not_determined: Traffic hides the lane-end pavement where any governing direction
                        arrow would be visible.
Step 6  u_turn          not_determined: Traffic hides the lane-end pavement where any governing arrow or
                        prohibition marking would be visible.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Stay within the current lane without crossing either visible solid boundary. Leave
                        space behind the queue and reassess lane arrows, stopping markings, and signals as the
                        obscured approach becomes visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1037, 21.84 s

culane_test__d100_05251718_0469_00390 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection with a zebra crossing.
                        My car is in an interior approach lane; the complete same-direction lane count and its
                        index from the left cannot be established confidently from this view. (lanes None,
                        mine None, insufficient)
Step 2  Left            A single solid white line runs along my lane's left side, with another same-direction
                        lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along my lane's right side, with another same-direction
                        lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; its lower shaft is obscured.; line:stop_line (full): A solid white
                        transverse stop line crosses my lane before the zebra crossing.; line:crosswalk
                        (full): White zebra-crossing stripes extend across my lane beyond the stop line.
Step 4  Cross-check     position: Both boundaries separate my lane from same-direction lanes, confirming an
                        interior position without establishing the total lane count or exact index. | roles:
                        The solid white boundaries fit same-direction no-crossing lane lines on an
                        intersection approach. | markings: The visible forward arrowhead agrees with a
                        straight-ahead approach lane; the stop line precedes the crosswalk, and no waiting
                        area is visible ahead of my lane. | unseen: The arrow's lower shaft is hidden by the
                        hood, and the outer lane arrangement is not confidently resolved; neither has been
                        reconstructed. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing my left boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing my right boundary.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The forward-pointing guide arrow permits straight travel rather than a
                        turn from this lane. [CN-5.13.1] "Guide arrows indicate the direction of travel for
                        vehicles. (Table 1 meanings: straight ahead; straight or left; left; straight or
                        right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the zebra crossing, which does
                        not independently govern any of the seven movement actions.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible straight arrowhead permits straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only guide arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only guide arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only guide arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel and do not cross either solid boundary to
                        change lanes. Follow the applicable traffic signal, stopping before the stop line when
                        required and keeping the crosswalk clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1417, 25.08 s

culane_test__d100_05251718_0469_01320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road passes beneath a pedestrian footbridge, with two lanes travelling in
                        this direction. My car is in the left lane; no intersection or lane ending is visible
                        ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line follows a raised curb on the left, with a paved pedestrian area,
                        planting and bridge supports beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible painted segment and gap farther ahead, separates
                        my lane from another lane travelling in the same direction.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left road edge and right lane divider agree with my car occupying lane 1
                        of 2. | roles: The broken white right boundary fits a same-direction lane divider. The
                        left paint appears white despite the supplied convention specifying yellow for a left
                        edge; its curbside position establishes its edge role. | markings: No guidance
                        markings are visible within my lane, and no marked waiting area is visible. | unseen:
                        The lead vehicle hides some pavement ahead; no markings or distant lane-end features
                        have been inferred beneath it. | result: consistent
Step 5  Rule            left_boundary: Crossing the solid left boundary is normally prohibited, and the raised
                        curb also physically bounds the lane. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    allowed (correct): The broken white lane divider permits a lane change under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay clear of the left curb and do not cross the solid left edge; a rightward lane
                        change is permitted by the broken divider only when traffic allows. No visible lane-
                        use arrows establish which lane to use for turns at a later intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 912, 17.4 s

culane_test__d100_05251718_0469_02040 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with no intersection or lane
                        ending visible. My car is in the left of two lanes travelling in this direction.
                        (lanes 2, mine 1, full)
Step 2  Left            A raised concrete curb borders my lane on the left, with a planted median beyond; no
                        separate painted boundary line can be confidently distinguished from the pale curb and
                        gutter.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A broken white line, with visible long segments and intervening gaps, separates my
                        lane from another lane travelling in the same direction; there is no curb at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left median curb and right lane divider agree with my car occupying lane
                        1 of 2. | roles: The white broken right boundary fits a same-direction lane divider;
                        the left curb forms the roadway edge. | markings: No guidance arrows, words, symbols,
                        transverse lines or waiting areas are discernible in my lane. | unseen: A separate
                        painted line beside the left curb is uncertain and has not been asserted; pavement
                        beneath the vehicles and beyond the visible stretch is obscured. | result: consistent
Step 5  Rule            left_boundary: This passage recognizes a curb as a clear physical edge that may
                        replace an edge marking; under the supplied boundary definitions, moving across this
                        raised physical edge is prohibited. [CN-5.4.5] "Where a non-motorized lane is needed
                        and there is no separating facility between it and the motor vehicle lanes, a
                        motor/non-motor separation line shall be prov"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The raised median curb forms a physical boundary, so moving
                        across it is prohibited.
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
Step 7  Reflect         consistent
Advice                  Stay clear of the left median curb; you may change to the right lane after checking
                        traffic and yielding appropriately. No visible markings assign intersection movements
                        or a stopping point, so reassess the guidance farther ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 987, 19.72 s

culane_test__d100_05251718_0469_02250 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined divided urban road continues straight ahead, with no intersection or lane
                        ending visible. My car is in the left lane of two lanes travelling in this direction.
                        (lanes 2, mine 1, full)
Step 2  Left            A continuous raised concrete curb borders my lane on the left, with grass, trees and a
                        planted median beyond; no painted boundary line is discernible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible painted segments and intervening gaps, separates my
                        lane from the same-direction lane occupied by the silver car; there is no curb along
                        this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left physical roadway edge and right lane divider agree with my car
                        occupying lane 1 of 2. | roles: The left curb forms the roadway edge; the broken white
                        line on the right fits a same-direction lane divider. | markings: No arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. | unseen: No unseen
                        markings are inferred; the next intersection and any markings there are outside the
                        visible stretch. | result: consistent
Step 5  Rule            left_boundary: No supplied passage explicitly authorizes crossing a curb; under the
                        physical-edge definition, leaving my lane across this raised curb is prohibited.
Step 5  Rule            right_boundary: The broken white same-direction lane divider permits changing into the
                        lane on my right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The raised curb is a physical roadway edge and may not be
                        crossed as a lane change.
Step 6  change_right    allowed (correct): The broken white lane divider permits changing right under
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
Advice                  Remain clear of the left curb; changing right across the broken white line is
                        permitted only when the adjacent lane is safe, particularly with the silver car
                        alongside ahead. No visible markings establish turn permissions or a stopping position
                        at the next intersection.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 878, 14.97 s

culane_test__d100_05251718_0469_05070 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban roadway continues ahead, with vehicles obscuring the distant
                        approach. Two same-direction lanes are visible near the car; my car is in the left
                        lane beside a raised landscaped median. (lanes 2, mine 1, full)
Step 2  Left            A continuous raised gray curb borders the lane on the left, with landscaping beyond;
                        no painted longitudinal line is clearly visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and right lane divider agree with my lane being the leftmost
                        of two visible same-direction lanes. | roles: The curb forms the left roadway edge,
                        and the broken white line separates same-direction lanes. | markings: No guidance
                        markings are readable in my lane, so none contradict the boundaries. | unseen: No
                        pavement arrows, stop line, or waiting area have been inferred from the overhead sign
                        or from the obscured distance. | result: consistent
Step 5  Rule            left_boundary: No supplied passage explicitly permits crossing a raised curb; the
                        physical roadway edge prohibits moving left onto the landscaped median.
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent lane
                        on the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The raised curb is a physical boundary, not a crossable lane
                        divider.
Step 6  change_right    allowed (correct): The broken white lane line permits a rightward lane change under
                        CN-5.2.3.
Step 6  go_straight     not_applicable: No visible pavement marking governs this action.
Step 6  turn_left       not_applicable: No visible pavement marking governs this action.
Step 6  turn_right      not_applicable: No visible pavement marking governs this action.
Step 6  u_turn          not_applicable: No visible pavement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Do not cross the left curb; a rightward lane change is permitted by the broken line,
                        but check the nearby vehicle and blind spot first. Follow the overhead lane-direction
                        sign and check pavement arrows farther ahead before choosing an intersection movement;
                        no stopping position is visible here.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 877, 16.0 s

culane_test__d100_05251718_0469_05190 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A tree-lined urban road continues ahead, with opposing traffic to the left and a curb
                        along the right. My car is in the middle of three lanes travelling in this direction;
                        no intersection or lane ending is clearly visible. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the right; the roadside curb is beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego lane index 2 agree with a same-direction lane line on
                        each side. | roles: Both boundaries are broken white lines, consistent with crossable
                        same-direction lane separators. | markings: No guidance arrows, text, symbols,
                        transverse lines or waiting areas are visible in my lane. | unseen: No markings or
                        intersection layout have been inferred from the distant, partly vehicle-obscured road.
                        | result: consistent
Step 5  Rule            left_boundary: The broken white lane separator permits my car to change into the
                        adjacent lane on the left. [[CN-5.2.3]]
Step 5  Rule            right_boundary: The broken white lane separator permits my car to change into the
                        adjacent lane on the right. [[CN-5.2.3]]
Step 6  change_left     allowed (correct): The broken white lane line permits changing left under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits changing right under CN-5.2.3.
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
Step 7  Reflect         Consistent: both lane changes are permitted by the visible broken lane lines, while no
                        visible marking governs the remaining actions.
Advice                  You may remain in the middle lane or cross either broken white boundary when safe
                        after checking adjacent traffic. No visible marking assigns intersection movements or
                        a stopping position; check the markings and controls farther ahead before selecting a
                        turn lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation unlisted, contradictions []
Tokens                  in 8604, out 925, 14.97 s

culane_test__d100_05251947_0499_00840 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead beside an elevated roadway, with no intersection
                        or lane ending visible. My car is in the leftmost of three visible lanes travelling in
                        this direction. (lanes 3, mine 1, full)
Step 2  Left            A continuous white line runs beside the raised concrete median on the left, with
                        opposing traffic beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Broken white segments with visible gaps separate my lane from another same-direction
                        traffic lane on the right, without a curb.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and a same-direction lane line on the right
                        agree with my lane being the leftmost of three lanes. | roles: The broken white right
                        boundary fits a crossable lane line. The left boundary is visibly white despite the
                        cited standard specifying yellow for a left carriageway edge; its physical position
                        beside the median establishes its edge-line role. | markings: No arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. | unseen: No unseen
                        intersection layout or movement restriction has been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing the left
                        boundary; the concrete median also physically prevents moving left. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a concrete median lies immediately beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits a rightward lane change under
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
Advice                  Stay within the lane beside the median; do not cross its solid left edge. A rightward
                        lane change is permitted by the broken line, but check adjacent traffic and blind
                        spots first; no intersection movement guidance or stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 921, 16.86 s

culane_test__d100_05251947_0499_04830 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road continues straight ahead in low light, with vehicles in the
                        distance. My car is in the rightmost of three visible same-direction lanes; the next
                        intersection and lane end are not clearly visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line follows the right side of my lane beside a raised curb and planted
                        roadside strip; its distant continuation is difficult to see in the darkness.
                        white solid, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:straight (partial): A faint white forward-pointing arrow is visible ahead in my
                        lane, although its outline is blurred by distance and low light.
Step 4  Cross-check     position: The left lane divider and right roadside edge agree with my car occupying
                        lane 3 of 3. | roles: The broken white left boundary fits a same-direction lane
                        divider, and the solid white right boundary fits a roadway edge. | markings: The
                        visible straight arrow is compatible with the lane continuing forward between these
                        boundaries. | unseen: The distant lane end, any stop line, and further markings cannot
                        be resolved; no such features are asserted. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits my car to change to the adjacent
                        lane on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The visible solid right boundary normally prohibits crossing it; the
                        raised curb also forms a physical road edge. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits continuing straight and does not
                        permit left turns, right turns, or U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white right boundary prohibits ordinary crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (WRONG, label prohibited): The visible forward arrow permits straight travel
                        under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (WRONG, label allowed): The straight-only arrow does not permit a right
                        turn under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No waiting area or adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, and do not cross the solid right edge or mount the
                        curb. If a turn is intended, identify an appropriately marked lane ahead and change
                        lanes only where permitted and safe; the distant intersection controls and stopping
                        position are not clear here.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight'], missed ['arrow:right']), actions False, unsafe ['go_straight'],
                        citation accepted, contradictions []
Tokens                  in 8604, out 1153, 20.67 s

culane_test__d100_05252026_0512_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit, divided urban road at night, with traffic continuing ahead toward distant
                        signals. My car is in the rightmost of three visible lanes in this direction; the
                        distant intersection approach is not clearly readable. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with a narrow paved strip and
                        a raised roadside edge farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and my rightmost position agree with a lane
                        divider on the left and a roadway edge line on the right. | roles: The broken white
                        divider fits a same-direction lane line; the solid white line fits the right roadway
                        edge. | markings: No readable arrows, words, symbols, transverse lines or waiting
                        areas are visible in my lane. | unseen: No distant lane-use marking or stop line is
                        inferred; the far approach is too small and dark to read. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent lane
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, except in
                        an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction
                        of travel, take these forms: a solid line means crossing is normally prohibited, and
                        may be crossed in an emergen"
Step 6  change_left     allowed (correct): The visible broken white lane divider permits crossing under
                        CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_determined: The distant approach is unreadable, so any lane-use arrow governing
                        the next intersection cannot be determined.
Step 6  turn_left       not_determined: The distant approach is unreadable, so any lane-use arrow or turn-
                        prohibition marking cannot be determined.
Step 6  turn_right      not_determined: The distant approach is unreadable, so any lane-use arrow or turn-
                        prohibition marking cannot be determined.
Step 6  u_turn          not_determined: The distant approach is unreadable, so any lane-use arrow or U-turn
                        prohibition cannot be determined.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay inside the solid right edge line; a left lane change is permitted across the
                        broken divider when safe. Read the lane arrows and applicable signals closer to the
                        intersection before selecting a turning lane or deciding where to stop.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1036, 20.56 s

culane_test__d100_05252026_0512_01020 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road at night, with traffic continuing ahead in the same direction and
                        opposing headlights farther left. My lane has another same-direction lane on its left
                        and right; darkness prevents a reliable count of all lanes, and no intersection or
                        lane ending is clearly visible. (lanes None, mine 2, partial)
Step 2  Left            A white broken longitudinal line separates my lane from the lane occupied by the car
                        ahead-left; its more distant portions are obscured by traffic and glare, and no curb
                        forms this boundary.
                        white dashed, curb no, lane_line, evidence partial
Step 2  Right           A white broken longitudinal line, with a visible dash and adjoining gap, separates my
                        lane from pavement carrying same-direction traffic on the right; no curb forms this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane lines indicate same-direction lanes on both sides; the opposing
                        traffic beyond the lane on the left supports my lane being second from the left, while
                        the total lane count remains uncertain. | roles: White broken boundaries fit same-
                        direction lane separators. | markings: No readable arrows, words, symbols, transverse
                        lines or marked waiting areas are visible in my lane. | unseen: No distant
                        intersection layout or lane-use direction has been inferred from the dark roadway. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane separator permits changing into the adjacent lane
                        on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The broken white lane separator permits changing into the adjacent
                        lane on the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     allowed (correct): The visible broken white lane boundary permits crossing under
                        CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane boundary permits crossing under CN-5.2.3.
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
Step 7  Reflect         Consistent: crossing the visible broken lane boundaries is permitted, while absent
                        movement markings are not treated as permission for intersection movements.
Advice                  You may cross either visible broken lane separator after checking adjacent traffic and
                        blind spots. No turn assignment or stopping position can be identified here; continue
                        cautiously and look for clearer markings, signs and signals ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1118, 24.92 s

culane_test__d100_05252026_0512_01350 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road at night, with traffic continuing ahead and no clearly visible
                        intersection or lane ending. My car is in the rightmost visible motor-vehicle lane;
                        darkness and glare prevent a reliable count of all same-direction lanes. (lanes None,
                        mine None, insufficient)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved margin and
                        raised roadside edge farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line confirms another same-direction lane to my left, while
                        the right edge line places my lane at the right edge of the motor carriageway; the
                        total lane count remains uncertain. | roles: The broken white lane separator and solid
                        white right edge line fit their observed roles. | markings: No readable arrows, words,
                        symbols, transverse lines or marked waiting areas are visible in my lane. | unseen: No
                        total lane count or distant intersection markings are inferred through darkness and
                        glare. | result: consistent
Step 5  Rule            left_boundary: The broken white lane separator permits changing into the adjacent
                        same-direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, except in a
                        safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
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
Advice                  Stay inside the solid right edge line; a left lane change is permitted across the
                        broken separator when safe. No visible marking establishes the permitted movements at
                        the next intersection, so check the approaching arrows, signs and signals before
                        choosing a turn lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1073, 21.13 s

culane_test__d193_06042058_0527_02610 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit tunnel carries two lanes in this direction, with no intersection or lane ending
                        visible ahead. My car is in the right-hand lane. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb lies on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow roadside margin
                        and a raised tunnel-side edge beyond it, partly obscured by darkness.
                        white solid, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego lane index 2 agree with a lane divider on the left and a
                        roadway edge on the right. | roles: The broken white divider fits a same-direction
                        lane line, and the solid white right boundary fits a carriageway edge line. |
                        markings: No guidance arrows, words, symbols, transverse lines or waiting areas are
                        visible in my lane. | unseen: No distant intersection layout is inferred; the raised
                        edge beyond the right line is only partly visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits my car to change into the lane on
                        the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, with an
                        exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue within the right-hand lane; a move into the left lane is permitted across the
                        broken divider when safe. Do not cross the solid right edge line in normal driving; no
                        intersection movement or stopping location is marked in the visible stretch.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 874, 14.05 s

culane_test__d193_06042058_0527_03240 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A lit road at night continues straight ahead, with no intersection or lane ending
                        visible. My car is in the right lane of two lanes travelling in this direction; a
                        vehicle is alongside in the left lane. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from the
                        same-direction lane occupied by the vehicle on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line, tinted by the yellow street lighting, borders my lane on the
                        right, with a paved shoulder and roadside posts beyond it; no raised curb is visible
                        at the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my lane
                        being the second and rightmost of two same-direction lanes. | roles: The broken white
                        separator fits a same-direction lane line, and the solid white right boundary fits a
                        roadway edge line. | markings: No arrows, words, symbols, transverse lines or marked
                        waiting areas are visible in my lane. | unseen: No markings are inferred beyond the
                        visible nighttime stretch; no intersection layout is inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing lanes to the left when
                        safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes."
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
Advice                  Remain within the right edge line; a left lane change is permitted by the markings,
                        but wait until the vehicle alongside is safely clear. No visible markings specify
                        movements at a future intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 863, 14.11 s

culane_test__d193_06051114_0632_02790 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a signal-controlled intersection. My car is behind the
                        red car in a lane with a straight-ahead arrow; one same-direction lane is visible to
                        the left, but the total lane count on the right is unclear. (lanes None, mine 2,
                        partial)
Step 2  Left            A worn white line appears continuous along the left side of my lane, with another
                        traffic lane beyond it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence partial
Step 2  Right           A faded solid white line runs along the right side of my lane, separating it from
                        further same-direction roadway; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        arrow:straight (full): A worn white arrow ahead of the hood has a forward-pointing
                        head and no visible turning branch.
Step 4  Cross-check     position: Lane boundaries on both sides indicate adjacent same-direction lanes. The
                        visible lane to the left places my lane second from the left, but the far-right layout
                        does not support a reliable total count. | roles: White longitudinal lines between
                        same-direction lanes fit lane-line roles; the visible stretches appear solid, although
                        worn paint reduces confidence. | markings: The straight arrow agrees with an
                        intersection approach bounded by solid lane lines. The left-turn arrow in the adjacent
                        left lane is outside my lane. | unseen: The red car obscures part of the lane ahead,
                        and no stop line can be confidently identified. No additional marking or waiting area
                        is inferred. | result: consistent
Step 5  Rule            left_boundary: The visible solid white lane boundary prohibits crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The visible solid white lane boundary prohibits crossing to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The straight-ahead guide arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
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
Advice                  Remain in this lane to proceed straight and do not cross its solid boundaries. Follow
                        the traffic signals and stop at the stop line when required; its position is not
                        clearly visible behind the vehicle ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1129, 20.52 s

culane_test__d193_06051114_0632_04320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided, tree-lined urban road continues ahead, with opposing traffic behind a
                        central fence and a separate roadside carriageway on the right. My car is in the left
                        of two same-direction lanes; no intersection or lane ending is clearly visible. (lanes
                        2, mine 1, full)
Step 2  Left            A solid white line runs beside the raised base of a continuous central fence, with
                        opposing traffic beyond; the fence physically bounds this side.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A worn broken white line, with a visible segment and gap, separates my lane from the
                        same-direction lane occupied by the black sedan; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood, but the hood hides its lower shaft and any possible branching
                        portion.
Step 4  Cross-check     position: The physical median edge on the left and a same-direction lane line on the
                        right agree with being lane 1 of 2. | roles: The broken white right boundary fits a
                        crossable lane line. The left boundary is visibly white despite the supplied rule
                        specifying yellow for a left carriageway edge; its physical position beside the median
                        establishes its edge role without changing the observed color. | markings: The visible
                        straight arrowhead is compatible with this lane, but the hidden lower portion prevents
                        excluding an additional movement. No waiting area or transverse marking is
                        identifiable ahead. | unseen: No hidden arrow branch, distant stop line, or
                        intersection layout is assumed. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the adjacent physical median also blocks that movement. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane boundary permits changing into the adjacent
                        same-direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            arrow:straight: The visible straight arrowhead indicates straight travel, but the
                        obscured lower portion does not establish whether another direction is also indicated.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, with a physical median beyond.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3,
                        subject to a safe gap.
Step 6  go_straight     allowed: The visible forward arrowhead permits straight travel under CN-5.13.1.
Step 6  turn_left       not_determined: The hood hides the portion of the arrow that would establish or
                        exclude a left branch.
Step 6  turn_right      not_determined: The hood hides the portion of the arrow that would establish or
                        exclude a right branch.
Step 6  u_turn          not_determined: The obscured lower arrow prevents determining whether a U-turn
                        indication accompanies the visible straight head.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; do not cross the median-side solid line. A rightward
                        lane change is permitted only with a safe gap around the black sedan; confirm the
                        complete arrow and intersection guidance before choosing any turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1138, 22.64 s

culane_test__d193_06051123_0635_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road approaches a broad intersection with a zebra crossing. My car is
                        in the leftmost of two visible lanes in its direction. (lanes 2, mine 1, full)
Step 2  Left            A single solid yellow line runs along the left of my lane to the intersection
                        approach, with opposing-direction roadway beyond and no curb.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right, with no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A solid white transverse stop line crosses my lane just before
                        the zebra crossing.; line:crosswalk (full): Broad white zebra-crossing stripes cross
                        the roadway immediately beyond the stop line.
Step 4  Cross-check     position: The yellow centre line on the left places my lane leftmost, and the white
                        lane line on the right separates it from the second same-direction lane. | roles: The
                        solid yellow centre line and solid white same-direction lane separator fit their
                        assigned roles. | markings: The stop line and crossing agree with the intersection
                        approach; no directional arrow or waiting area is visible in my lane. | unseen: The
                        hood hides the pavement immediately beneath the car; no marking is inferred there. |
                        result: consistent
Step 5  Rule            left_boundary: The single solid yellow centre line prohibits my car from crossing the
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
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the zebra crossing; it
                        identifies a pedestrian crossing and does not determine any of the seven movement
                        actions.
Step 6  change_left     prohibited (correct): The single solid yellow centre line prohibits crossing under
                        CN-6.1.4.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_applicable: No visible directional marking governs this action.
Step 6  turn_left       not_applicable: No visible directional marking governs this action.
Step 6  turn_right      not_applicable: No visible directional marking governs this action.
Step 6  u_turn          not_applicable: No visible directional marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the boundaries prohibit crossing on their respective sides, while the stop
                        line and crosswalk do not establish permitted intersection movements.
Advice                  Stay within this lane without crossing either solid boundary; the visible markings do
                        not establish which intersection movements this lane serves. Stop before the stop line
                        when required and watch for pedestrians on the crossing.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1081, 17.42 s

culane_test__d193_06051123_0635_00900 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A two-way urban road curves gently left ahead, with sidewalks on both sides and no
                        clearly visible intersection. My car is in the single motor-vehicle lane in its
                        direction. (lanes 1, mine 1, full)
Step 2  Left            A single continuous yellow line separates my lane from opposing traffic space on the
                        left; no curb forms this boundary.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single solid white line runs along the right of my lane, with a paved roadside strip
                        and then a raised sidewalk curb beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane in my direction agrees with the center line on the left and roadway
                        edge line on the right. | roles: The solid yellow center line separates opposing
                        directions; the solid white edge line marks the right edge of the motor-vehicle lane.
                        | markings: No arrows, words, symbols, transverse lines or waiting areas are visible
                        in my lane. | unseen: No markings are inferred beyond the visible road; the roadside
                        curb is beyond the white boundary rather than forming it. | result: consistent
Step 5  Rule            left_boundary: The single solid yellow center line prohibits my car from crossing the
                        left boundary. [CN-6.1.4] "A single solid yellow line prohibits vehicles in both
                        directions from crossing. It is generally used on two-lane two-way roads with limited
                        sight distance or wh"
Step 5  Rule            right_boundary: Crossing the solid white right boundary is normally prohibited, with
                        an exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing under CN-6.1.4.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the left boundary separately prohibits crossing it.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Follow the road within the yellow center line and white right edge line; do not cross
                        either boundary for an ordinary maneuver. No visible arrows assign intersection
                        movements, and no stop line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 834, 13.47 s

culane_test__d193_06051123_0635_00990 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road continues ahead, with no clear intersection or lane ending
                        visible. My car is in the leftmost of two apparent lanes in its direction. (lanes 2,
                        mine 1, full)
Step 2  Left            A single broken yellow line, with visible painted segments and gaps, separates my lane
                        from opposing traffic; there is no curb along this boundary.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A single broken white line, with visible segments and gaps, separates my lane from the
                        paved lane to its right; the sidewalk curb lies beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow centre line places my lane leftmost in its direction, and the
                        white lane line indicates another lane to the right, consistent with two lanes and ego
                        index 1. | roles: The broken yellow centre line separates opposing traffic, while the
                        broken white lane line separates same-direction lanes. | markings: No arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. | unseen: No
                        movements at a distant intersection or markings hidden beyond the visible road have
                        been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken yellow centre line may be crossed to overtake or turn only
                        when doing so does not affect safety. [CN-5.1.1] "The crossable centre line separates
                        traffic flows in opposite directions. It means vehicles may cross the line to
                        overtake, turn or make a U-turn when this does"
Step 5  Rule            right_boundary: The broken white lane line permits changing into the adjacent same-
                        direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     allowed (correct): CN-5.1.1 permits crossing the broken yellow centre line when safe,
                        but opposing traffic lies beyond it.
Step 6  change_right    allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action at
                        the lane's end.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in your lane unless a safe lane change is needed; crossing left would enter
                        opposing traffic, not another same-direction lane. No visible lane-use arrows or stop
                        line specify turning movements or a stopping position.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 981, 18.59 s

culane_test__d193_06051123_0635_01980 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad urban road approaches a distant intersection. My car is in the middle of three
                        lanes travelling in this direction. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; there is no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; the roadside curb is beyond that adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead,
                        with no turning branch.
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying lane 2 of 3. | roles:
                        Both boundaries are white solid lines separating same-direction lanes, consistent with
                        no-crossing lane lines. | markings: The straight-only arrow is consistent with an
                        intersection approach bounded by solid lane lines; the turning arrows in adjacent
                        lanes do not govern my lane. | unseen: No distant stop line or additional distant
                        marking is claimed; fine details at the intersection are too far away to resolve. |
                        result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from my lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left lane line prohibits crossing
                        under CN-6.2.1.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right lane line prohibits crossing
                        under CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting-area marking or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not cross either solid white boundary. Turning
                        requires an appropriate lane reached where lane changes are permitted; obey the
                        intersection signals and stop before the stop line if required when it becomes
                        visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 967, 14.62 s

culane_test__d193_06051123_0635_02160 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection with a pedestrian
                        crossing. My car is in the rightmost of three visible approach lanes, beside a
                        channelized roadside island. (lanes 3, mine 3, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line curves along the right side of my lane, with white diagonal
                        channelizing stripes beyond it and a raised roadside island farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white bent arrow has a single arrowhead pointing right.;
                        line:stop_line (partial): A transverse white stop line crosses the lane just before
                        the pedestrian crossing; its paint is faint.; line:crosswalk (full): White zebra-
                        crossing bars extend across the approach ahead.
Step 4  Cross-check     position: Three approach lanes and position 3 agree with a same-direction lane line on
                        the left and a roadway edge on the right. | roles: The solid white left line fits an
                        intersection-approach lane separator; the solid white right line fits an edge beside a
                        channelized island. | markings: The right-turn-only arrow agrees with the rightmost
                        approach position and the curved right edge. The diagonal striped area is outside my
                        lane, not an area within it. | unseen: No hidden arrowheads or waiting areas are
                        assumed; the faint stop line is assigned partial evidence. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits crossing into the lane on my left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid longitudinal edge line normally prohibits crossing to the
                        right, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:right: The right-turn arrow permits a right turn and excludes straight travel,
                        left turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate the
                        direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or left;
                        left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers zebra crossings, and this
                        marking does not determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     prohibited (correct): The single right-turn arrow does not permit straight travel
                        under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The single right-turn arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      allowed (correct): The right-turn arrow permits this movement under CN-5.13.1.
Step 6  u_turn          prohibited (correct): The single right-turn arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane for a right turn only; do not cross either solid boundary or enter the
                        striped island area. Obey the applicable signal, stop before the stop line when
                        required, and check for pedestrians at the crossing.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1224, 20.63 s

culane_test__d193_06051123_0635_03690 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road approaches a broad intersection with a pedestrian crossing ahead. My car
                        is in the middle of three visible approach lanes in its direction. (lanes 3, mine 2,
                        full)
Step 2  Left            Two closely spaced solid white lines separate my lane from the lane on the left; no
                        curb is visible along this boundary.
                        white double_solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line separates my lane from another approach lane on the right, with no
                        curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in the middle of my lane has one head pointing
                        straight ahead.; line:stop_line (full): A transverse solid white stop line crosses my
                        lane before the pedestrian crossing.; line:crosswalk (full): White zebra-crossing
                        stripes extend across my lane immediately beyond the stop line.
Step 4  Cross-check     position: The middle position among three lanes agrees with same-direction lane
                        boundaries on both sides. | roles: The white longitudinal boundaries fit separation of
                        same-direction approach lanes; both are visibly continuous. | markings: The straight-
                        only arrow is consistent with a bounded intersection guide lane, followed by a stop
                        line and crosswalk. | unseen: No hidden markings or waiting areas have been inferred;
                        the hood obscures the pavement immediately beneath the vehicle. | result: consistent
Step 5  Rule            left_boundary: The continuous white boundary normally prohibits crossing to the left;
                        the passages provide no specific double-white lane-line rule. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane on the
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
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalks; this marking
                        identifies the pedestrian crossing and does not determine any of the seven actions.
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
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
Advice                  Stay in this lane to proceed straight; do not cross either solid boundary to reach a
                        turn lane here. Obey the intersection signals, stop before the stop line when
                        required, and watch for pedestrians and crossing traffic.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1170, 18.03 s

culane_test__d193_06051411_0691_03960 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban road continues ahead beside shops and parked vehicles, with opposing traffic
                        separated by a metal median fence. My car is in the leftmost of two apparent lanes;
                        the right-hand lane markings are faint, and no intersection or lane end is clearly
                        visible. (lanes 2, mine 1, partial)
Step 2  Left            A continuous pale white line follows the metal median fence on the left; the fence
                        forms a physical boundary, with opposing traffic beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           Faint white longitudinal segments with intervening gaps appear on the right,
                        separating my lane from roadway beside the parked vehicles; parts are worn and
                        obscured by the hood, and no curb forms this immediate boundary.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and apparent lane divider on the right place my
                        car in lane 1 of an apparent two lanes. | roles: The faint broken white right boundary
                        fits a same-direction lane divider. The left paint appears white rather than the
                        yellow specified for a left edge; its physical position beside the median fence
                        nevertheless identifies it as an edge, not a lane divider. | markings: No readable
                        arrows, words, symbols, transverse lines or waiting areas are visible in my lane. |
                        unseen: The right divider and lane count are uncertain because the paint is faint. No
                        intersection-end markings or hidden lane-use arrows have been inferred. | result:
                        Consistent spatial interpretation, with an observed left-edge colour discrepancy and
                        partial evidence for the right divider.
Step 5  Rule            left_boundary: The visible solid longitudinal line normally prohibits crossing, and
                        the median fence also physically prevents moving left. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The apparent broken white same-direction divider permits changing
                        lanes where it is identifiable and safe to cross. [CN-5.2.3] "On roads with two or
                        more lanes in the same direction, the crossable lane line shall be used on sections
                        where vehicles may change lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a median fence blocks it.
Step 6  change_right    allowed (correct): The visible broken white divider permits a lane change under
                        CN-5.2.3; confirm the faint divider and check the adjacent lane first.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the left boundary governs crossing it, not an unseen intersection movement.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the boundary decisions apply only to crossing their respective sides, and
                        no intersection movement is inferred from the absence of visible arrows.
Advice                  Stay clear of the median fence; do not cross the solid left edge. A rightward lane
                        change is permitted by the apparent broken divider only after confirming its course
                        and checking traffic and parked vehicles; no visible markings establish turn
                        permissions or a stopping position ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1031, 18.46 s

culane_test__d193_06051603_0727_01080 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane elevated branch separating from the wider carriageway on
                        the left. A painted separator leads into a physical divider ahead; no intersection or
                        lane ending is visible. (lanes 1, mine 1, full)
Step 2  Left            A worn solid white line borders a diagonally hatched separator on the left, with other
                        traffic lanes beyond; the separator develops into a physical divider farther ahead.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A concrete barrier forms the right edge, with no distinct painted boundary line
                        visible along its base.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The car occupies the only lane of this separated branch; the lanes beyond
                        the left separator belong to the adjacent carriageway. | roles: The white left line
                        outlines a separator between same-direction branches, rather than separating opposing
                        traffic; the right boundary is a physical roadway edge. | markings: No arrows, text,
                        transverse lines or waiting areas are visible in the ego lane. The diagonal hatching
                        is outside its left boundary. | unseen: No yellow paint, in-lane arrow or painted
                        right edge line has been inferred. | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal boundary normally prohibits crossing to the
                        left. [CN-4.2.2-a] "Longitudinal markings, set along the direction of travel, take
                        these forms: a solid line means crossing is normally prohibited, and may be crossed in
                        an emergen"
Step 5  Rule            right_boundary: No supplied passage specifically governs crossing a concrete barrier;
                        this physical lane edge prohibits moving out of the lane to the right.
Step 6  change_left     prohibited (correct): The solid white boundary normally prohibits crossing under
                        CN-4.2.2-a, and a physical divider continues ahead.
Step 6  change_right    prohibited (correct): The concrete barrier is a physical boundary that cannot be
                        crossed.
Step 6  go_straight     not_applicable: No visible in-lane directional marking governs this action.
Step 6  turn_left       not_applicable: No visible in-lane directional marking governs this action.
Step 6  turn_right      not_applicable: No visible in-lane directional marking governs this action.
Step 6  u_turn          not_applicable: No visible in-lane directional marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary restrictions govern only lateral departures, and the absence of
                        directional markings does not establish permission for intersection movements.
Advice                  Remain within this branch and follow its course; do not cross the solid left boundary
                        or hatched separator, and keep clear of the right barrier. No stop line or movement-
                        selection arrow is visible.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 907, 18.22 s

culane_test__d193_06051603_0727_01620 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           The car is on an elevated, barrier-lined ramp curving left. One undivided lane is
                        visible in this direction, with no intersection or lane ending visible ahead. (lanes
                        1, mine 1, full)
Step 2  Left            A faded pale-yellow solid line follows the left pavement edge beside a raised concrete
                        barrier and guardrail; no gaps are visible along the exposed stretch.
                        yellow solid, curb yes, edge_line, evidence full
Step 2  Right           A pale-white solid line follows the right pavement edge alongside a concrete barrier,
                        with no visible dash-and-gap pattern.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Edge boundaries on both sides agree with one visible lane and the car
                        occupying lane 1. | roles: The yellow left edge and white right edge fit their
                        respective edge-line roles; both follow physical barriers. | markings: No arrows,
                        words, symbols, transverse lines or marked waiting areas are visible in the lane. |
                        unseen: No markings beyond the visible curve or beneath the hood are inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing; the concrete
                        barrier also physically bounds the roadway. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing; the concrete
                        barrier also physically bounds the roadway. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The solid left edge line normally prohibits crossing under
                        CN-4.2.2-a, and a concrete barrier lies beside it.
Step 6  change_right    prohibited (correct): The solid right edge line normally prohibits crossing under
                        CN-4.2.2-a, and a concrete barrier lies beside it.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the road's left curve is not a turn instruction.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay within the single ramp lane and follow its leftward curve without crossing either
                        edge. The chevron signs reinforce the curve; no stop line or intersection movement
                        instruction is visible.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8604, out 900, 16.18 s

culane_test__d193_06051734_0757_00000 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided expressway with three lanes in this direction continues straight ahead; no
                        intersection, ramp connection or lane ending is visible. My car is in the middle lane.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes with my car in lane 2 agree with a same-direction lane beyond
                        each boundary. | roles: Both boundaries are broken white lines, consistent with
                        crossable same-direction lane lines. | markings: No arrows, words, symbols, marked
                        areas or transverse lines are visible in my lane. | unseen: No hidden markings or
                        distant intersection features have been inferred. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits my car to change into the lane on
                        the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction,
                        the crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane line permits my car to change into the lane on
                        the right when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 6  change_left     allowed (correct): The broken white lane line permits lane changes under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits lane changes under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either broken white boundary may be crossed for a safe
                        lane change after checking traffic. No visible marking requires a lane change or a
                        stop, and no intersection movement is specified here.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation in_pack_not_accepted, contradictions []
Tokens                  in 8604, out 792, 10.68 s

culane_test__d193_06051734_0757_02430 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided highway with three lanes in this direction continues straight ahead; no
                        intersection or lane ending is visible. My car is in the middle lane. (lanes 3, mine
                        2, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps ahead of the hood, separates my lane
                        from another same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 2 agree with a lane line and another
                        lane on each side. | roles: Both white broken boundaries fit same-direction crossable
                        lane lines. | markings: No arrows, text, symbols, marked waiting areas or transverse
                        traffic markings are visible in my lane. | unseen: No hidden markings or distant lane-
                        end features have been inferred; the transverse pavement seam is not treated as a
                        traffic marking. | result: consistent
Step 5  Rule            left_boundary: The broken white lane boundary permits my car to change to the lane on
                        the left. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane boundary permits my car to change to the lane on
                        the right. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue in the middle lane; either broken boundary may be crossed for a lane change
                        after checking traffic and blind spots. No turn guidance or stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 827, 11.56 s

culane_test__d193_06051734_0757_04050 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           The car is on a single-lane ramp curving right toward an overpass. Guardrails enclose
                        both sides, and no intersection or lane ending is visible. (lanes 1, mine 1, full)
Step 2  Left            A single solid white line bounds the lane on the left, with a narrow paved margin and
                        a raised edge and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A single solid white line bounds the lane on the right, with a paved margin and a
                        raised edge and metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are roadway edges rather than separators from adjacent
                        lanes, consistent with one lane and ego lane index 1. | roles: Both lines are visibly
                        solid white roadway edges. The left edge is white despite the supplied rule normally
                        specifying yellow for a left edge; its observed color is retained. | markings: No
                        arrows, text, symbols, transverse lines or marked waiting areas are visible in the
                        lane. | unseen: No markings or lane continuation beyond the visible bend are inferred.
                        | result: consistent
Step 5  Rule            left_boundary: The solid left boundary normally prohibits crossing it, except in a
                        safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing it, except in a
                        safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 6  change_left     prohibited (correct): Crossing the solid left edge line is normally prohibited by
                        CN-4.2.2-a.
Step 6  change_right    prohibited (correct): Crossing the solid right edge line is normally prohibited by
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the road's rightward curve is not a turn arrow.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay between the solid white edge lines and follow the ramp's rightward curve, as also
                        indicated by the roadside chevrons. Do not cross either boundary; no intersection
                        movement or stopping point is marked in the visible stretch.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 854, 12.59 s

culane_test__d193_06060642_0768_00360 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A straight, two-way urban road with two lanes in this direction; my car is in the
                        rightmost lane beside a planted roadside strip. No intersection or lane ending is
                        clearly visible ahead. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another lane
                        travelling in the same direction; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white edge marking runs beside a raised curb, with a planted strip beyond the
                        curb.
                        white dashed, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and position 2 agree with a lane line on the left
                        and a roadway edge on the right. | roles: The broken white left line fits a same-
                        direction lane divider; the white right marking and curb fit the roadway edge. |
                        markings: No arrows, text, symbols, transverse lines or waiting areas are visible in
                        my lane. | unseen: No movements are inferred from the distant road, where an
                        intersection and its markings cannot be resolved. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent lane
                        on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: This marking identifies the roadway edge; although the broken paint is
                        crossable, the raised curb is a physical boundary that must not be driven across, for
                        which no supplied passage gives a separate curb rule. [CN-5.4.1] "The carriageway edge
                        line marks the edge of motor vehicle lanes or non-motorized vehicle lanes, or the
                        boundary between motor vehicle lanes and non-motorized ve"
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change under CN-5.2.3.
Step 6  change_right    prohibited (correct): The raised curb physically bounds the right side; a broken edge
                        marking does not authorize driving over it.
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
Advice                  Continue within the lane; a left lane change is permitted when safe, but do not cross
                        the right-hand curb. No visible direction arrows establish turn permissions, and no
                        stopping line is visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1068, 21.65 s

culane_test__d193_06060642_0768_00900 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way road curves gently right, with an overpass visible farther ahead and
                        no clear intersection in the visible stretch. My car is in the rightmost of two lanes
                        travelling in this direction. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with a visible long dash and gaps, separates my lane from another
                        same-direction lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line follows the right edge of my lane beside a raised curb
                        and planted strip, with parked vehicles beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 2 agree with a lane line on the
                        left and a roadway edge on the right. | roles: The broken white line fits a same-
                        direction lane separator; the solid white line beside the curb fits the right roadway
                        edge. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        discernible in my lane. | unseen: No unseen markings or intersection layout have been
                        inferred; the distant road does not show a readable lane endpoint. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane separator permits my car to change into the
                        adjacent left lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The solid right boundary normally prohibits crossing, apart from the
                        stated safe emergency exception; the raised curb is also a physical edge. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane line permits a lane change under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white boundary normally prohibits crossing under
                        CN-4.2.2-a, and a curb lies beside it.
Step 6  go_straight     not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No visible arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Follow the gently curving lane; you may change left across the broken white line when
                        safe, but do not cross the solid right edge or curb. No visible lane-use arrows
                        establish which lane to use for turns at a later intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 803, 12.57 s

culane_test__d193_06060642_0768_03060 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban multilane road runs beside an elevated roadway, with a junction indicated
                        farther ahead. My car is in the rightmost of three visible motor-vehicle lanes
                        travelling in this direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line with visible dashes and gaps separates my lane from the adjacent
                        lane occupied by the green bus; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a paved roadside strip
                        beyond it and a raised sidewalk curb farther away.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (partial): A small white arrow farther ahead in my lane appears to bend
                        right; its distant shape is not clear enough to exclude an additional arrowhead.
Step 4  Cross-check     position: The lane line to the left and roadway edge line to the right agree with my
                        position as lane 3 of 3. | roles: The broken white separator fits a same-direction
                        lane line, and the solid white roadside boundary fits a right edge line. | markings:
                        The visible rightward arrow is compatible with the rightmost lane, but its complete
                        set of arrowheads cannot be confirmed. | unseen: No stop line or waiting area can be
                        identified; the distant lane end is not fully resolved, and no additional arrowhead is
                        assumed. | result: consistent
Step 5  Rule            left_boundary: The broken white lane separator permits changing into the adjacent
                        same-direction lane when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: Crossing the solid right boundary is normally prohibited, except in an
                        emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set along the direction of
                        travel, take these forms: a solid line means crossing is normally prohibited, and may
                        be crossed in an emergen"
Step 5  Rule            arrow:right: The visible rightward arrowhead indicates a permitted right turn, but the
                        unclear remainder prevents a complete determination of the lane's permitted movements.
                        [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles. (Table 1
                        meanings: straight ahead; straight or left; left; straight or right; right; U-turn;
                        straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3, subject
                        to safe clearance from the bus.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_determined: The distant arrow is insufficiently clear to determine whether it also
                        has a straight-ahead head.
Step 6  turn_left       not_determined: The complete distant arrow cannot be read confidently enough to
                        determine all excluded movements.
Step 6  turn_right      allowed: The visible rightward arrowhead permits a right turn under CN-5.13.1.
Step 6  u_turn          not_determined: The complete distant arrow cannot be read confidently enough to
                        determine all excluded movements.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Do not cross the solid right edge line; a left lane change is permitted only with a
                        safe gap, particularly around the bus. The distant arrow appears to permit a right
                        turn, but confirm its full shape and the junction signs before committing to another
                        movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1170, 24.78 s

culane_test__d193_06060748_0790_02970 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A broad multilane divided road carries dense traffic ahead; no intersection or lane
                        ending is visible. My car is in the middle lane, behind the red hatchback. (lanes 5,
                        mine 3, full)
Step 2  Left            A broken white line separates my lane from another same-direction lane on the left; a
                        long dash and a gap are visible, with no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line separates my lane from the same-direction lane occupied by the
                        cream minibus on the right; a dash and gap are visible, although the minibus hides
                        part of the continuation, and there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Five same-direction lanes, with my lane third from the left, agree with
                        ordinary lane lines and additional lanes on both sides. | roles: Both boundaries are
                        broken white lines, consistent with separation of same-direction lanes. | markings: No
                        arrows, words, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No hidden guidance markings or intersection movements have been
                        inferred; vehicles obscure some pavement farther ahead. | result: consistent
Step 5  Rule            left_boundary: The broken white lane line permits changing into the lane on the left
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane line permits changing into the lane on the right
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
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
Advice                  Either broken boundary permits a lane change, but nearby vehicles require a safe gap
                        before moving. No visible marking assigns an intersection movement or stopping
                        position; keep your lane unless a change is needed and safe.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1025, 19.33 s

culane_test__d193_06060919_0820_00450 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           An urban two-way street continues ahead, with parked vehicles along the right side and
                        pedestrians near the roadside. My car is in the single visible travel lane of its
                        direction; no intersection or lane ending is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A faded broken yellow line lies to my left, with a visible painted segment and gap;
                        opposing traffic occupies the roadway beyond it, and there is no curb along this
                        boundary.
                        yellow dashed, curb no, center_line, evidence partial
Step 2  Right           The right side leads to parked cars and a raised roadside curb; no painted boundary is
                        discernible, and parked vehicles obscure part of the curb and pavement beside it.
                        none none, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: A centre line on the left and the roadway edge on the right agree with one
                        travel lane in my direction and lane index 1. | roles: The broken yellow marking fits
                        an opposing-traffic centre line; the raised curb defines the right roadway edge
                        without a clearly visible painted edge line. | markings: No readable arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. | unseen: The
                        yellow paint is faded, and parked cars hide portions of the right edge; no hidden
                        pavement markings or distant intersection controls are inferred. | result: consistent
Step 5  Rule            left_boundary: The crossable centre line permits crossing into the opposing side only
                        when doing so does not affect safety. [CN-5.1.1] "The crossable centre line separates
                        traffic flows in opposite directions. It means vehicles may cross the line to
                        overtake, turn or make a U-turn when this does"
Step 5  Rule            right_boundary: No supplied passage expressly permits crossing a raised curb; the
                        physical roadway edge is not a permissible lane-change path.
Step 6  change_left     allowed (correct): The visible broken yellow centre line permits crossing under
                        CN-5.1.1 when safe, but the space beyond is for opposing traffic.
Step 6  change_right    prohibited (correct): The raised curb forms a physical roadway boundary, not an
                        available lane-change path.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the centre line governs boundary crossing only.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain in the current travel lane and leave clearance for parked cars and pedestrians,
                        especially the pedestrian immediately to the right. Crossing the broken yellow line is
                        conditional on safety and enters opposing traffic space; no visible markings establish
                        turn permissions or a stopping location.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1081, 23.77 s

culane_test__d193_06060925_0822_01260 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead beside an elevated roadway, with no intersection
                        or lane ending visible. My car is in the rightmost of three lanes travelling in this
                        direction. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible long segments and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous solid white line follows the right edge of my lane beside a raised curb
                        and metal roadside fence.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane line on the left and road edge on the right agree with my car
                        occupying lane 3 of 3. | roles: The broken white line fits a same-direction lane
                        divider; the solid white line beside the curb fits the right roadway edge. | markings:
                        No arrows, text, symbols, transverse lines or marked waiting areas are visible in my
                        lane. | unseen: No hidden markings are inferred; traffic and distance limit inspection
                        farther ahead, and the next intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the adjacent lane
                        on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing, so my car must
                        not move out across it toward the curb. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits normal crossing under
                        CN-4.2.2-a, and a curb lies beyond it.
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
Advice                  Stay within the right edge line; a left lane change is permitted after checking
                        traffic and yielding as needed. No visible markings establish turn permissions or a
                        stopping point at the next intersection, so reassess as it comes into view.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 891, 15.97 s

culane_test__d193_06060925_0822_02700 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban boulevard continues straight ahead, with four lanes in this direction.
                        My car is in the third lane from the left; no intersection or lane ending is clearly
                        visible. (lanes 4, mine 3, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the roadside curb is beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The third of four lanes has same-direction lanes on both sides, consistent
                        with both boundaries being lane lines. | roles: Both white broken boundaries fit
                        crossable same-direction lane lines. | markings: No arrows, words, symbols, transverse
                        lines or marked waiting areas are visible in my lane. | unseen: No distant
                        intersection layout or hidden guidance markings have been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The broken white lane boundary permits my car to change into the
                        adjacent lane on the left when safe. [CN-5.2.3] "On roads with two or more lanes in
                        the same direction, the crossable lane line shall be used on sections where vehicles
                        may change lanes."
Step 5  Rule            right_boundary: The broken white lane boundary permits my car to change into the
                        adjacent lane on the right when safe. [CN-5.2.3] "On roads with two or more lanes in
                        the same direction, the crossable lane line shall be used on sections where vehicles
                        may change lanes."
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
Advice                  You may cross either dashed boundary to change lanes when safe, yielding to traffic
                        already in the adjacent lane. No visible marking assigns intersection movements or a
                        stopping position; check guidance farther ahead before selecting a turn lane.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 861, 14.11 s

culane_test__d193_06060925_0822_04140 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road with three lanes in this direction continues toward an overpass.
                        My car is in the rightmost lane; no intersection stop line is visible ahead. (lanes 3,
                        mine 3, full)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        lane travelling in the same direction; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A faint continuous white line follows the right road edge beside a narrow paved margin
                        and raised curb, with a roadside barrier beyond.
                        white solid, curb yes, edge_line, evidence partial
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted in my lane immediately
                        ahead of the hood; its head points forward without a turning branch.
Step 4  Cross-check     position: Three lanes and ego position 3 agree with a same-direction lane line on the
                        left and the road edge on the right. | roles: The broken white left boundary fits a
                        crossable lane line; the continuous white right boundary fits a right carriageway
                        edge. | markings: The straight-ahead arrow agrees with the continuing lane; no
                        conflicting marking or marked waiting area is visible. | unseen: The right paint is
                        faint, so its evidence is partial; distant pavement and any eventual intersection
                        markings cannot be read. | result: consistent
Step 5  Rule            left_boundary: The broken white lane boundary permits a lane change to the left when
                        safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the crossable
                        lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the visible solid right boundary is normally prohibited, with
                        an exception for a safe emergency crossing. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only arrow permits proceeding straight and does not
                        permit left turns, right turns or U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The visible solid right edge prohibits normal crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane; a left lane change is permitted when safe, but do not
                        cross the right edge. For a turn or U-turn, find an appropriately marked lane farther
                        ahead rather than turning from this straight-only lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1024, 18.02 s

culane_test__d193_06060925_0822_04320 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues beneath a pedestrian footbridge, with a bus stop along
                        the right side. Four same-direction lanes are visible; my car is in the third lane
                        from the left. (lanes 4, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broad broken white line, with visible dashes and gaps, separates my lane from the
                        lane beside the bus stop; there is no curb at this boundary, and the roadside curb
                        lies beyond that adjacent lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The third of four lanes has another same-direction lane on each side,
                        consistent with both boundaries being lane lines. | roles: Both boundaries are broken
                        white lines, consistent with separation of same-direction traffic. | markings: No
                        guidance marking is readable within my lane; the visible arrow to the left belongs to
                        another lane. | unseen: No bus-only restriction is inferred from the bus or bus stop,
                        and no distant or obscured lane marking is asserted. | result: consistent
Step 5  Rule            left_boundary: The broken white lane boundary permits changing to the lane on the left
                        when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The broken white lane boundary permits crossing into the adjacent
                        right lane, subject to any separately applicable lane restrictions. [CN-5.2.3] "On
                        roads with two or more lanes in the same direction, the crossable lane line shall be
                        used on sections where vehicles may change lanes."
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white lane line permits crossing under
                        CN-5.2.3; no special-lane marking is readable.
Step 6  go_straight     not_applicable: No marking in my lane governs this action.
Step 6  turn_left       not_applicable: No marking in my lane governs this action.
Step 6  turn_right      not_applicable: No marking in my lane governs this action.
Step 6  u_turn          not_applicable: No marking in my lane governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  The visible broken boundaries permit lane changes when safe, but check for bus-lane
                        restrictions before entering the right lane and watch for buses at the stop. No
                        readable marking in your lane establishes intersection movements or a stopping
                        position.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation accepted, contradictions []
Tokens                  in 8604, out 1454, 33.44 s

culane_test__d193_06060925_0822_04680 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with a landscaped median on the left and a
                        landscaped roadside strip on the right. My car is in the rightmost of three same-
                        direction lanes; the distant lane end or intersection is not clearly visible. (lanes
                        3, mine 3, full)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line follows the right side of my lane, with a narrow paved margin and a
                        raised curb beside the landscaped strip beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A worn white arrow in my lane has a single head pointing
                        straight ahead.
Step 4  Cross-check     position: The lane line on the left and roadway edge on the right agree with my
                        position as lane 3 of 3. | roles: The broken white separator fits a same-direction
                        lane line, and the solid white line beside the roadside curb fits a right edge line. |
                        markings: The straight-ahead arrow is compatible with the longitudinal boundaries; no
                        conflicting marking is visible in my lane. | unseen: No stop line, waiting area, or
                        additional distant lane-use marking can be identified; none has been inferred. |
                        result: consistent
Step 5  Rule            left_boundary: The broken white lane separator permits changing into the lane on the
                        left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: Crossing the solid right edge line is normally prohibited, with only
                        the stated safe emergency exception. [CN-4.2.2-a] "Longitudinal markings, set along
                        the direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns, and U-turns from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane line permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed: The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited: The straight-only arrow does not permit a left turn under CN-5.13.1.
Step 6  turn_right      prohibited: The straight-only arrow does not permit a right turn under CN-5.13.1.
Step 6  u_turn          prohibited: The straight-only arrow does not permit a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane, or change left across the broken separator when safe.
                        For a turn or U-turn, find an appropriately marked lane; do not cross the solid right
                        edge line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation accepted,
                        contradictions []
Tokens                  in 8604, out 1104, 20.49 s

culane_test__d193_06060925_0822_05310 | lane | Test B | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with a raised roadside strip separating the main
                        carriageway from a parallel road on the right. My car is in the rightmost of three
                        apparent same-direction lanes; distant markings are faint. (lanes 3, mine 3, partial)
Step 2  Left            A worn white broken line, with visible segments and gaps, separates my lane from
                        another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A faded continuous white line runs along the right of my lane, with a narrow paved
                        margin and a raised curb farther beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line and right roadway edge support a rightmost-lane position;
                        the total of three lanes is less certain because the farther-left markings are faint.
                        | roles: The broken white line fits a same-direction lane divider, and the solid white
                        line fits the right roadway edge. | markings: No readable arrow, text, symbol, or
                        transverse marking is visible in my lane; diagonal markings farther ahead lie outside
                        its right boundary. | unseen: No lane-use direction or intersection stop line is
                        inferred from the distant, indistinct roadway. | result: consistent
Step 5  Rule            left_boundary: The broken white lane divider permits changing into the same-direction
                        lane on the left when safe. [CN-5.2.3] "On roads with two or more lanes in the same
                        direction, the crossable lane line shall be used on sections where vehicles may change
                        lanes."
Step 5  Rule            right_boundary: The solid right edge line normally prohibits crossing onto the paved
                        margin, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white edge line normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     not_applicable: No visible marking governs this movement.
Step 6  turn_left       not_applicable: No visible marking governs this movement.
Step 6  turn_right      not_applicable: No visible marking governs this movement.
Step 6  u_turn          not_applicable: No visible marking governs this movement.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Remain inside the solid right edge line; a left lane change is permitted across the
                        broken divider when safe. No visible lane-use arrow establishes which lane to use for
                        turns, so check clearer markings and signs farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 870, 14.54 s

culane_test__d37_05181608_0235_03090 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban road approaches a signal-controlled intersection with a pedestrian crossing
                        ahead. My car follows a taxi in the rightmost visible motor-vehicle lane, between a
                        painted separator on the left and a roadside railing on the right; the complete same-
                        direction lane count is obscured. (lanes None, mine None, insufficient)
Step 2  Left            A solid white line borders a white diagonally hatched separator on the left, with
                        other motor traffic beyond; a large yellow protective drum obscures part of the near
                        separator.
                        white solid, curb no, other, evidence partial
Step 2  Right           A solid white line runs along the right side of the lane beside a metal separation
                        railing, with a narrow roadside area and sidewalk beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A transverse white stop line is visible ahead to the right
                        of the taxi; the taxi hides its continuation across my lane.; line:crosswalk
                        (partial): White pedestrian-crossing stripes extend across the road beyond the stop
                        line, with the taxi obscuring part of the crossing.
Step 4  Cross-check     position: The right edge and railing establish that this is the rightmost visible
                        motor-vehicle lane. Occlusion and the left-side separator prevent a reliable total
                        lane count or numerical lane index. | roles: The white outlined and hatched separator
                        fits a channelizing boundary, while the solid white line beside the railing fits a
                        right roadway edge. | markings: The stop line and crossing agree with an intersection
                        approach. No lane-use arrow can be read in the exposed pavement; the taxi obscures
                        much of the lane ahead. | unseen: No arrow direction or hidden lane count is inferred.
                        The near left separator and portions of the transverse markings remain obscured. |
                        result: consistent
Step 5  Rule            left_boundary: The channelizing separator requires my car to follow the designated
                        path and prohibits driving on or across its outline and hatching. [CN-6.6.1-3]
                        "Channelizing lines show that vehicles must follow the set path and may not drive on
                        or across the lines. ... Channelizing lines separating traffic in the same d"
Step 5  Rule            right_boundary: Crossing the solid white boundary is normally prohibited, and the
                        adjacent railing also prevents an ordinary move to the right. [CN-4.2.2-a]
                        "Longitudinal markings, set along the direction of travel, take these forms: a solid
                        line means crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            line:stop_line: The white stop line identifies where my car must stop when yielding or
                        waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop when
                        yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers the pedestrian crossing; it
                        does not determine any of the seven lane-movement permissions.
Step 6  change_left     prohibited (correct): CN-6.6.1-3 prohibits crossing the outlined channelizing
                        separator on the left.
Step 6  change_right    prohibited (correct): The solid right boundary prohibits normal crossing under
                        CN-4.2.2-a, and a railing lies alongside it.
Step 6  go_straight     not_determined: The taxi obscures pavement where a governing lane-use arrow could be
                        painted, so the permitted direction cannot be established.
Step 6  turn_left       not_determined: The taxi obscures possible lane-use markings; neither boundary
                        determines the intersection turn permission.
Step 6  turn_right      not_determined: No readable arrow establishes a right-turn permission, and the taxi
                        hides much of the approach pavement.
Step 6  u_turn          not_determined: Possible governing lane-use markings are obscured by the taxi.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay between the left separator and right railing; do not change lanes across either
                        boundary. Confirm this lane's permitted direction when the taxi clears the markings,
                        obey the signals, and stop before the stop line when required while keeping the
                        pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        accepted, contradictions []
Tokens                  in 8604, out 1354, 27.61 s

culane_test__d37_05181608_0235_03720 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A divided urban road continues ahead, with opposing traffic behind the median fence on
                        the left. My car is in the leftmost lane; vehicles obscure parts of the roadway
                        farther ahead. (lanes 3, mine 1, full)
Step 2  Left            A continuous pale white line runs beside a raised median curb and metal fence, with
                        opposing traffic beyond the fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line separates my lane from the same-direction lane containing the
                        white hatchback; a dash and adjoining gaps are visible ahead, but the hatchback hides
                        part of the nearer stretch.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left and a same-direction lane divider on the right
                        agree with my lane being the first of three lanes. | roles: The broken white right
                        boundary fits a crossable lane line. The left edge paint appears white, although the
                        supplied rule specifies yellow for a left carriageway edge; its visible color has not
                        been changed to fit the rule. | markings: No arrows, words, symbols, transverse lines
                        or waiting areas are visible in my lane. | unseen: The white hatchback obscures part
                        of the right boundary, and traffic limits inspection farther ahead; no hidden markings
                        have been inferred. | result: Consistent, apart from the observed left-edge color
                        differing from the supplied edge-line color specification.
Step 5  Rule            left_boundary: The visible solid boundary normally prohibits crossing to the left, and
                        the raised median also physically bounds the lane. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The broken white lane divider permits changing into the adjacent same-
                        direction lane where the crossing can be made safely. [CN-5.2.3] "On roads with two or
                        more lanes in the same direction, the crossable lane line shall be used on sections
                        where vehicles may change lanes."
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised median lies beyond it.
Step 6  change_right    allowed (correct): The visible broken white lane divider permits a lane change under
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
Step 7  Reflect         Consistent: boundary decisions apply only to crossing their respective sides, and the
                        absence of visible movement markings is not treated as permission to turn.
Advice                  Stay clear of the median; a rightward lane change is permitted by the visible broken
                        divider, but only after checking the white hatchback and other traffic. No visible
                        arrows establish which lane to use for turns, and no stop line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1248, 26.22 s

culane_test__d37_05181608_0235_05220 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A congested multilane urban road approaches a signalized intersection. My car is
                        behind the dark sedan, with same-direction traffic on both sides; vehicles obscure the
                        outer lanes and most pavement ahead. (lanes None, mine None, insufficient)
Step 2  Left            A continuous white solid line separates my lane from the same-direction lane occupied
                        by the silver van on the left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line separates my lane from the same-direction lane occupied
                        by the silver sedan and gray vehicle on the right; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries are lane lines, confirming at least one same-direction lane
                        on each side; the total lane count and exact index cannot be established through the
                        traffic. | roles: The white solid boundaries fit no-crossing lines between same-
                        direction lanes. | markings: No guidance marking or transverse line is readable in the
                        exposed portion of my lane; the sedan and queued traffic obscure the remaining
                        pavement. | unseen: No arrows, stop line, waiting area, or exact outer-lane
                        arrangement have been inferred from the obscured pavement. | result: consistent
Step 5  Rule            left_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the left. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 5  Rule            right_boundary: The solid white lane line prohibits my car from crossing into the lane
                        on the right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in
                        the same direction and prohibits vehicles on the solid-line side from crossing. It has
                        two forms: sin"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: Traffic obscures the pavement where lane-direction arrows would
                        determine this movement.
Step 6  turn_left       not_determined: Traffic obscures the pavement where lane-direction arrows or movement
                        prohibitions would determine this movement.
Step 6  turn_right      not_determined: Traffic obscures the pavement where lane-direction arrows or movement
                        prohibitions would determine this movement.
Step 6  u_turn          not_determined: Traffic obscures the pavement where lane-direction arrows or movement
                        prohibitions would determine this movement.
Step 6  enter_waiting_areanot_determined: The lane end and intersection pavement are obscured, so a waiting
                          area ahead cannot be established.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines; do not change lanes across either boundary. As
                        traffic clears, verify this lane's arrows and the stop line, and obey the intersection
                        signals before proceeding.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 905, 15.62 s

culane_test__d37_05181608_0235_05340 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A wide urban road with several same-direction lanes is congested on the approach to a
                        signalized intersection. My car is between two occupied lanes, but traffic obscures
                        the outer road limits and much of the pavement ahead. (lanes None, mine None,
                        insufficient)
Step 2  Left            A continuous white line runs along the left of my lane, with another lane of queued
                        vehicles beyond it and no curb between the lanes.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with another lane of queued
                        vehicles beyond it and no curb between the lanes.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Both boundaries separate same-direction lanes, so my lane is an interior
                        lane; the total lane count and exact index cannot be established. | roles: The white
                        solid boundaries fit no-crossing lane lines between same-direction lanes. | markings:
                        No guidance marking is readable in the exposed pavement of my lane; the vehicle ahead
                        obscures possible arrows and the intersection approach. | unseen: No arrows, stop
                        line, waiting area, or exact lane count have been inferred from the traffic or
                        signals. | result: consistent
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
Step 6  go_straight     not_determined: Traffic hides the pavement where lane-direction arrows could determine
                        this movement.
Step 6  turn_left       not_determined: Traffic hides the pavement where lane-direction arrows could determine
                        this movement.
Step 6  turn_right      not_determined: Traffic hides the pavement where lane-direction arrows could determine
                        this movement.
Step 6  u_turn          not_determined: Traffic hides possible directional or prohibited-movement markings
                        ahead.
Step 6  enter_waiting_areanot_determined: The intersection approach ahead is obscured, so the presence of a
                          left-turn waiting area cannot be established.
Step 7  Reflect         consistent
Advice                  Stay between the solid white lines; do not change lanes across them. As traffic
                        clears, verify this lane's arrows and stop line, and obey the applicable signals
                        before entering the intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 848, 14.0 s

culane_test__d37_05181919_0299_02970 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road runs toward a distant intersection. My car is in the rightmost
                        of three apparent motor-vehicle lanes, behind a dark sedan; roadside activity lies to
                        the right. (lanes 3, mine 3, partial)
Step 2  Left            A broken white line, with a visible long segment and gap, separates my lane from
                        another forward-travel lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a roadside paved strip, a
                        black car and two-wheelers beyond it; no raised curb is visible along the line, and
                        the strip's precise function is unclear.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is visible immediately ahead of
                        the hood, with its forward-pointing head behind the sedan.
Step 4  Cross-check     position: The left lane line and apparent right edge line agree with my car occupying
                        the third, rightmost motor-vehicle lane; the roadside strip makes the total count
                        somewhat uncertain. | roles: The broken white left line fits a same-direction lane
                        divider, and the solid white right line fits a carriageway edge, although the use of
                        the space beyond is not fully established. | markings: The straight arrow agrees with
                        a through lane; no conflicting marking is visible. | unseen: No bicycle designation,
                        distant stop line or waiting area is identifiable; traffic and distance obscure the
                        end of the lane. | result: consistent
Step 5  Rule            left_boundary: The broken same-direction lane divider permits changing lanes to the
                        left when safe. [CN-5.2.3] "On roads with two or more lanes in the same direction, the
                        crossable lane line shall be used on sections where vehicles may change lanes."
Step 5  Rule            right_boundary: The visible solid longitudinal line normally prohibits crossing to the
                        right, except in a safe emergency. [CN-4.2.2-a] "Longitudinal markings, set along the
                        direction of travel, take these forms: a solid line means crossing is normally
                        prohibited, and may be crossed in an emergen"
Step 5  Rule            arrow:straight: The straight-only guide arrow permits proceeding straight and excludes
                        left turns, right turns and U-turns from this lane. [CN-5.13.1] "Guide arrows indicate
                        the direction of travel for vehicles. (Table 1 meanings: straight ahead; straight or
                        left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing under CN-5.2.3.
Step 6  change_right    prohibited (correct): The solid white boundary normally prohibits crossing under
                        CN-4.2.2-a.
Step 6  go_straight     allowed (correct): The straight arrow permits this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrow does not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrow does not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrow does not permit a U-turn under
                        CN-5.13.1.
Step 6  enter_waiting_areanot_determined: The lane end is obscured, so the presence of an accessible waiting
                          area ahead cannot be established.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight; a leftward lane change is permitted across the
                        broken line when safe, but do not cross the solid right boundary. For another
                        movement, find an appropriately marked lane in advance, and check the obscured
                        intersection controls and stopping position as you approach.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1160, 21.99 s

culane_test__d37_05181919_0299_03120 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a signal-controlled intersection. My car is in an
                        interior lane; nearby vehicles obscure the full lane layout on the left. (lanes None,
                        mine None, insufficient)
Step 2  Left            A solid white line runs along the left of my lane, with another same-direction traffic
                        lane beyond it and no curb on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line runs along the right of my lane, with another same-direction
                        traffic lane beyond it; the roadside railing is farther right, not on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the hood hides the lower shaft.; arrow:straight (full): A smaller
                        white straight-ahead arrow is visible farther ahead in my lane.
Step 4  Cross-check     position: The lane boundaries establish that another same-direction lane lies on each
                        side; the total count and exact index are left unknown because the farther-left layout
                        is obscured. | roles: Both white solid boundaries fit same-direction no-crossing lane
                        lines. | markings: The visible straight-ahead arrows agree with each other and with a
                        lane bounded by solid approach lines. | unseen: The near arrow's lower shaft is hidden
                        by the hood, and traffic obscures the distant lane end; no stop line or waiting area
                        is asserted. | result: consistent
Step 5  Rule            left_boundary: The solid white lane boundary prohibits crossing to the left.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            right_boundary: The solid white lane boundary prohibits crossing to the right.
                        [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The forward-pointing arrow indicates straight-ahead travel rather than
                        a turn. [CN-5.13.1] "Guide arrows indicate the direction of travel for vehicles.
                        (Table 1 meanings: straight ahead; straight or left; left; straight or right; right;
                        U-turn; straigh"
Step 5  Rule            arrow:straight: The repeated straight-ahead arrow allows proceeding straight and
                        excludes left, right and U-turn movements from this lane. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing under
                        CN-6.2.1.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     allowed (correct): The straight-ahead arrows permit this movement under CN-5.13.1.
Step 6  turn_left       prohibited (correct): The straight-only arrows do not permit a left turn under
                        CN-5.13.1.
Step 6  turn_right      prohibited (correct): The straight-only arrows do not permit a right turn under
                        CN-5.13.1.
Step 6  u_turn          prohibited (correct): The straight-only arrows do not permit a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_determined: No marked waiting area is visible, but traffic obscures the lane end
                          where an area ahead would need to be checked.
Step 7  Reflect         consistent
Advice                  Stay within the solid white boundaries and use this lane for straight-ahead travel,
                        not turns. The signal ahead appears red: stop behind the queue and check the stop line
                        as it becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1513, 34.27 s

culane_test__d37_05190927_0395_02340 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban divided road approaches an intersection, with a truck directly ahead and
                        other traffic to the right. My car is in the leftmost lane beside a raised planted
                        median; vehicles obscure the full width of the carriageway and the lane's far end.
                        (lanes None, mine 1, partial)
Step 2  Left            A solid white painted line runs beside a raised curb, with a planted median and
                        fencing beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A solid white line separates my lane from another same-direction lane; the nearby
                        silver car obscures part of its nearer continuation.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left establishes that my lane is leftmost, and the
                        lane line on the right establishes another same-direction lane; the total lane count
                        remains obscured. | roles: The solid white right boundary fits a no-crossing lane
                        line. The left boundary is visibly white despite being beside the median; its physical
                        position establishes its edge role, although its color differs from the prescribed
                        yellow left edge. | markings: No guidance marking is readable in the exposed portion
                        of my lane; the truck obscures the pavement farther ahead. | unseen: No arrow, stop
                        line, waiting area, or total lane count has been inferred from the obscured pavement.
                        | result: consistent
Step 5  Rule            left_boundary: The solid longitudinal line normally prohibits crossing to the left,
                        and the raised median also physically blocks that movement. [CN-4.2.2-a] "Longitudinal
                        markings, set along the direction of travel, take these forms: a solid line means
                        crossing is normally prohibited, and may be crossed in an emergen"
Step 5  Rule            right_boundary: The solid white lane line prohibits crossing into the lane on the
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 6  change_left     prohibited (correct): The solid left boundary prohibits normal crossing under
                        CN-4.2.2-a, and a raised median lies beyond.
Step 6  change_right    prohibited (correct): The visible solid white lane line prohibits crossing under
                        CN-6.2.1.
Step 6  go_straight     not_determined: The truck hides the approach pavement where a governing lane-use arrow
                        could be marked.
Step 6  turn_left       not_determined: The truck hides the approach pavement where a governing lane-use arrow
                        could be marked.
Step 6  turn_right      not_determined: The truck hides the approach pavement where a governing lane-use arrow
                        could be marked.
Step 6  u_turn          not_determined: The truck hides any governing arrow or prohibited-movement marking
                        farther ahead.
Step 6  enter_waiting_areanot_determined: The truck obscures the lane end and any possible waiting area ahead.
Step 7  Reflect         consistent
Advice                  Stay between the median and the solid white line; do not change lanes across either
                        boundary. Leave enough distance behind the truck to reveal the lane arrows and
                        stopping position before choosing an intersection movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 952, 19.62 s

culane_test__d37_05190927_0395_02430 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           An urban multilane road approaches a pedestrian crossing and intersection. My car is
                        in the leftmost lane beside a raised traffic island; three same-direction lanes are
                        visible. (lanes 3, mine 1, full)
Step 2  Left            A raised island with a pale curb and a utility pole forms the left boundary; no
                        distinct painted longitudinal line is readable along it.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A solid white line runs along the right side of my lane toward the crossing, with
                        another same-direction lane beyond it.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower shaft is hidden by the hood.; line:stop_line (full): A
                        transverse solid white line crosses my lane immediately before the pedestrian
                        crossing.; line:crosswalk (partial): Broad white pedestrian-crossing stripes extend
                        across my lane ahead, with portions obscured by the truck.
Step 4  Cross-check     position: The island on the left and a same-direction lane line on the right agree
                        with my lane being the leftmost of three lanes. | roles: The right solid white line
                        fits a same-direction lane boundary; the raised island forms a physical left roadway
                        edge without a clearly painted line. | markings: The visible straight arrow, stop line
                        and crosswalk are compatible with an intersection approach; no waiting area is
                        visible. | unseen: The hood hides the lower arrow shaft, and the truck hides part of
                        the crossing and farther pavement; no additional arrowhead or hidden marking is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: No supplied passage explicitly governs crossing this unpainted raised
                        curb; as a physical boundary it is not an available lane-change path.
Step 5  Rule            right_boundary: The solid white lane boundary prohibits crossing into the lane on my
                        right. [CN-6.2.1] "The no-crossing lane line separates vehicles travelling in the same
                        direction and prohibits vehicles on the solid-line side from crossing. It has two
                        forms: sin"
Step 5  Rule            arrow:straight: The visible straight-ahead guide arrow permits proceeding straight and
                        does not authorize left turns, right turns or U-turns. [CN-5.13.1] "Guide arrows
                        indicate the direction of travel for vehicles. (Table 1 meanings: straight ahead;
                        straight or left; left; straight or right; right; U-turn; straigh"
Step 5  Rule            line:stop_line: The solid white stop line identifies where my car must stop when
                        yielding or waiting to proceed. [CN-6.4.1-2] "The stop line marks where vehicles stop
                        when yielding or waiting to proceed. It is a solid white line. ..."
Step 5  Rule            line:crosswalk: No supplied passage specifically covers crosswalk markings, and this
                        marking does not determine any of the seven movement actions.
Step 6  change_left     prohibited (correct): The raised island curb is a physical boundary, not a traversable
                        lane-change path.
Step 6  change_right    prohibited (correct): The solid white lane line prohibits crossing under CN-6.2.1.
Step 6  go_straight     allowed (correct): The visible forward arrowhead indicates straight travel under
                        CN-5.13.1.
Step 6  turn_left       prohibited (WRONG, label not_determined): The straight-only guide arrow does not
                        authorize a left turn under CN-5.13.1.
Step 6  turn_right      prohibited (WRONG, label not_determined): The straight-only guide arrow does not
                        authorize a right turn under CN-5.13.1.
Step 6  u_turn          prohibited (WRONG, label not_determined): The straight-only guide arrow does not
                        authorize a U-turn under CN-5.13.1.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Stay in this lane for straight travel; do not cross the solid white line or drive over
                        the island curb. Yield to pedestrians and stop before the stop line when required by
                        traffic control or conditions.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions False, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 1377, 25.2 s

culane_test__d37_05190927_0395_05220 | lane | Test B | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           A tree-lined, two-way urban street continues ahead, with opposing vehicles on the left
                        and parked vehicles on the right. My car is in the single visible through lane of its
                        direction; no intersection or lane ending is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A faint yellow line appears continuous along the left side of my lane, with opposing
                        traffic beyond; the cyclist obscures its nearest portion, and no curb is visible along
                        it.
                        yellow solid, curb no, center_line, evidence partial
Step 2  Right           Two parallel solid white lines run along the right side beside parked vehicles; the
                        nearest stretch and the roadside beyond are partly hidden by the black SUV.
                        white double_solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One through lane in my direction agrees with a center line on the left and a
                        boundary to roadside parking on the right. | roles: The yellow left line separates
                        opposing traffic; the white right lines bound the through roadway beside parking
                        rather than another visible through lane. | markings: No readable arrows, words,
                        symbols, transverse lines or waiting areas are visible in my lane. | unseen: The
                        cyclist hides the nearest left boundary, and parked vehicles hide parts of the right
                        roadside; no hidden markings or intersection layout have been inferred. | result:
                        consistent
Step 5  Rule            left_boundary: The visible single solid yellow center line prohibits my car from
                        crossing to the left. [CN-6.1.4] "A single solid yellow line prohibits vehicles in
                        both directions from crossing. It is generally used on two-lane two-way roads with
                        limited sight distance or wh"
Step 5  Rule            right_boundary: The solid longitudinal white lines normally prohibit crossing to the
                        right, except in an emergency when safe. [CN-4.2.2-a] "Longitudinal markings, set
                        along the direction of travel, take these forms: a solid line means crossing is
                        normally prohibited, and may be crossed in an emergen"
Step 6  change_left     prohibited (correct): The visible solid yellow center line prohibits crossing under
                        CN-6.1.4.
Step 6  change_right    prohibited (correct): The solid white longitudinal boundary normally prohibits
                        crossing under CN-4.2.2-a.
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
Advice                  Remain between the visible solid boundaries and give the cyclist ample clearance,
                        slowing or waiting rather than crossing into opposing traffic or the parked vehicles.
                        No visible marking establishes turning permissions or a stopping point at an upcoming
                        intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation accepted, contradictions []
Tokens                  in 8604, out 948, 16.47 s
```
