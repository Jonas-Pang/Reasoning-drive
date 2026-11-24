# Reasoning of lane run 20261114_005514_laneD_CN

```text
culane_test__d100_05251207_0380_01410 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, based on the Chinese roadside lettering, with traffic
                        keeping right. My car is in the rightmost of three same-direction lanes on a tree-
                        lined divided road continuing straight ahead; no intersection or lane ending is
                        clearly visible. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A single continuous white line separates my lane from a paved roadside strip occupied
                        by a cyclist; the raised sidewalk curb is farther right, not at this painted boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and position 3 agree with a lane divider on my
                        left and the roadway edge on my right. | roles: The broken white line fits a same-
                        direction lane divider, and the continuous white line beside the cyclist's roadside
                        strip fits an edge line. | markings: No arrows, words, symbols, transverse lines, or
                        waiting areas are discernible in my lane. | unseen: No unseen lane-use arrow or
                        intersection marking is inferred; the eventual lane endpoint is beyond the clearly
                        readable stretch. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: The continuous white roadway edge restricts ordinary crossing into the
                        roadside non-motorized strip.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (correct): The continuous white edge line restricts crossing into the
                        roadside strip.
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
Advice                  Continue within the current lane, keeping clear of the cyclist and roadside strip;
                        change left only after checking traffic. No visible arrows establish turn permissions,
                        so reassess the lane guidance when approaching an intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 880, 13.57 s

culane_test__d100_05251207_0380_02130 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, inferred from the Chinese
                        writing and road layout. My car is in the middle of three same-direction lanes on a
                        divided urban road; no intersection or lane ending is visible ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line, with long dashes and visible gaps, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with long dashes and visible gaps, separates my lane from another
                        same-direction lane on the right; the roadside fence is beyond that lane, not at my
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes with my car in lane 2 agrees with a same-direction lane line on
                        each side. | roles: Both white broken boundaries fit ordinary same-direction lane
                        separators. | markings: No guidance markings are visible within my lane, and none
                        contradict the boundaries. | unseen: No unseen arrows, intersection markings, or
                        waiting areas have been inferred; the next intersection is outside the visible
                        stretch. | result: consistent
Step 5  Rule            left_boundary: Under Chinese marking rules, a white broken lane separator permits
                        crossing to change lanes when safe.
Step 5  Rule            right_boundary: Under Chinese marking rules, a white broken lane separator permits
                        crossing to change lanes when safe.
Step 6  change_left     allowed (correct): The white broken left lane separator permits a safe lane change.
Step 6  change_right    allowed (correct): The white broken right lane separator permits a safe lane change.
Step 6  go_straight     not_applicable: No marking governs this action in the visible stretch.
Step 6  turn_left       not_applicable: No marking governs this action in the visible stretch.
Step 6  turn_right      not_applicable: No marking governs this action in the visible stretch.
Step 6  u_turn          not_applicable: No marking governs this action in the visible stretch.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  You may remain in the middle lane or cross either broken separator when safe, after
                        checking mirrors and blind spots. No visible arrows determine a lane for a future
                        turn, and no stopping line is visible; reassess as junction markings come into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 765, 10.93 s

culane_test__d100_05251207_0380_02190 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           Likely mainland China, inferred from Chinese writing and the road layout; traffic
                        keeps right. My car is in the middle of three same-direction lanes on a divided urban
                        road, with no intersection or lane ending clearly visible ahead. (lanes 3, mine 2,
                        full)
Step 2  Left            A white broken line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the roadside curb is beyond that lane, not at my lane
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 2 agree with a same-direction lane beyond each
                        boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        separators. | markings: No readable guidance markings are visible in my lane, so none
                        contradict the boundaries. | unseen: No intersection-end markings or movements are
                        inferred from the distant roadway. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane separator permits crossing to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: In mainland China, a broken white lane separator permits crossing to
                        change lanes when safe and without obstructing other traffic.
Step 6  change_left     allowed (correct): The white broken lane separator permits a safe lane change left.
Step 6  change_right    allowed (correct): The white broken lane separator permits a safe lane change right.
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
Step 7  Reflect         consistent: lane-change permissions follow the broken boundaries, while no
                        intersection-movement permission is inferred from their absence.
Advice                  You may change to either adjacent lane across the broken white lines after checking
                        traffic, particularly vehicles on the right. No visible arrows establish turn lanes or
                        a stopping point; follow markings and controls as they become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 784, 11.97 s

culane_test__d100_05251207_0380_02400 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, inferred from the Chinese road signs and blue
                        vehicle plates, with traffic keeping right. My car is in the middle of three same-
                        direction lanes on a divided urban road; no intersection or lane ending is clearly
                        visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with a long dash and gaps visible, separates my lane from the
                        lane containing the white van; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with separated dashes visible, separates my lane from the right-
                        hand lane containing the small delivery vehicle; the roadside curb is beyond that
                        lane, not at my boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lane-line boundaries agree with my lane being the middle lane of three
                        same-direction lanes. | roles: Both white broken lines fit same-direction lane-divider
                        roles. | markings: No guidance arrows, words, symbols, marked areas or transverse
                        lines are discernible in my lane. | unseen: The distant lane endpoint is not readable;
                        no markings or intersection layout have been inferred there. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white same-direction lane divider permits
                        crossing to change lanes when safe and without impeding other traffic.
Step 5  Rule            right_boundary: In mainland China, a broken white same-direction lane divider permits
                        crossing to change lanes when safe and without impeding other traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  go_straight     not_determined: The lane endpoint and any movement-governing markings there are too
                        distant to assess.
Step 6  turn_left       not_determined: The lane endpoint and any movement-governing markings there are too
                        distant to assess.
Step 6  turn_right      not_determined: The lane endpoint and any movement-governing markings there are too
                        distant to assess.
Step 6  u_turn          not_determined: The lane endpoint and any movement-governing markings there are too
                        distant to assess.
Step 6  enter_waiting_areanot_applicable: No marking governs this action: no left-turn waiting area or
                          adjacent two-way left-turn lane is visible.
Step 7  Reflect         consistent: lane-change permissions follow the visible broken dividers, while endpoint
                        movements remain undecided because their governing features cannot be assessed.
Advice                  Continue within the middle lane; either lane change is permitted by the visible
                        markings only after checking surrounding traffic, especially the van to the left and
                        delivery vehicle to the right. Reassess arrows and lane assignments nearer the next
                        junction; no stopping line is visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 864, 13.08 s

culane_test__d100_05251207_0380_03270 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese-language road signs and road
                        layout, with traffic keeping right. My car is in the rightmost of three same-direction
                        lanes on a tree-lined divided urban road; no intersection or lane ending is clearly
                        visible ahead. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with visible long dashes and gaps, separates my lane from another
                        same-direction traffic lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line borders my lane on the right, with a narrow paved roadside
                        strip beyond it and a raised sidewalk curb farther right, rather than directly at the
                        painted boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego lane index 3 agree with a lane divider on
                        the left and a roadway edge line on the right. | roles: The broken white left line
                        fits a same-direction lane divider, and the continuous white right line fits the
                        roadway edge beside a roadside strip. | markings: No arrows, words, symbols,
                        transverse lines or marked waiting areas are visible in my lane; the overhead sign is
                        not a pavement marking. | unseen: No unseen pavement arrows or intersection geometry
                        have been inferred; the distant lane endpoint is not clearly visible. | result:
                        consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a broken white lane divider
                        permits crossing to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A solid white roadway edge line restricts crossing onto the roadside
                        strip during ordinary driving.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  change_right    prohibited (correct): The solid white roadway edge line restricts crossing onto the
                        roadside strip.
Step 6  go_straight     not_applicable: No visible pavement marking governs this action.
Step 6  turn_left       not_applicable: No visible pavement marking governs this action.
Step 6  turn_right      not_applicable: No visible pavement marking governs this action.
Step 6  u_turn          not_applicable: No visible pavement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain inside the right edge line; a move into the lane on your left is permitted
                        after checking traffic and signaling. The overhead sign indicates upcoming route
                        choices, but no visible pavement arrows establish which intersection movements this
                        lane permits.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 928, 18.04 s

culane_test__d100_05251222_0385_01140 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           Likely mainland China, inferred from the Chinese writing and road layout, with traffic
                        keeping right. My car is in the leftmost of three same-direction lanes on a divided
                        urban road beside an elevated structure; no intersection or lane ending is visible
                        ahead. (lanes 3, mine 1, full)
Step 2  Left            A solid white line follows the left edge of my lane beside a raised curb and narrow
                        planted strip, with a metal guardrail beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider agree with my lane being the
                        leftmost of three same-direction lanes. | roles: The solid white line beside the curb
                        fits a roadway edge, and the broken white line between same-direction lanes fits a
                        lane divider. | markings: No visible arrows, words, symbols, transverse lines or
                        waiting areas conflict with the boundaries. | unseen: No unseen intersection markings
                        or lane-end instructions have been inferred; the road continues beyond the visible
                        stretch. | result: consistent
Step 5  Rule            left_boundary: Under the inferred mainland Chinese rules, this solid roadway edge and
                        raised curb prohibit moving out of the lane across the left boundary here.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 6  change_left     prohibited (correct): The solid left roadway edge and raised curb prohibit crossing to
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
Step 7  Reflect         consistent: only the boundary-crossing actions are governed by the visible markings,
                        and no intersection movement permission has been inferred.
Advice                  Stay within the left roadway edge; you may change into the lane on the right after
                        checking clearance. No intersection guidance or stop line is visible, so determine
                        turn-lane requirements from markings farther ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 915, 14.38 s

culane_test__d100_05251222_0385_01710 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, suggested by Chinese
                        writing, blue vehicle plates and the road layout. My car is in the second of four
                        apparent same-direction lanes on an urban road beside an elevated structure,
                        approaching a signalized intersection. (lanes 4, mine 2, partial)
Step 2  Left            A white continuous line runs along the left of my lane, with another traffic lane
                        beyond it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white continuous line runs along the right of my lane toward the intersection, with
                        the black sedan's lane beyond it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (insufficient): A white longitudinal arrow shaft is visible behind the
                        silver car, but the car obscures the arrowhead and any branches, so its permitted
                        directions cannot be read reliably.; line:crosswalk (partial): White transverse
                        crosswalk stripes are visible near the intersection, partly obscured by the silver
                        car.
Step 4  Cross-check     position: Lane lines on both sides agree with an interior lane, apparently second from
                        the left; the far-right lane count is less certain. | roles: White solid lines fit
                        same-direction lane separators on an intersection approach. | markings: The arrow
                        shaft does not establish the arrow's directions, and the crosswalk does not resolve
                        them; neither conflicts with the boundaries. | unseen: The arrow:straight label
                        identifies the visible longitudinal component only, not a confirmed straight-only
                        arrow; its head and possible branches are hidden. No separate stop line can be
                        identified reliably. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a solid white lane separator
                        prohibits crossing it to change lanes.
Step 5  Rule            right_boundary: Under mainland Chinese marking rules, a solid white lane separator
                        prohibits crossing it to change lanes.
Step 5  Rule            arrow:straight: Lane-use arrows prescribe the indicated intersection movements, but
                        this obscured arrow cannot establish which movements apply.
Step 5  Rule            line:crosswalk: The crosswalk requires attention and yielding to pedestrians as
                        applicable, but does not prescribe the lane's turning movements.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     not_determined (WRONG, label allowed): The arrowhead is hidden by the silver car,
                        leaving its permitted directions unresolved.
Step 6  turn_left       not_determined (WRONG, label prohibited): The hidden arrowhead and possible branches
                        prevent determining whether left turns are permitted.
Step 6  turn_right      not_determined (WRONG, label prohibited): The hidden arrowhead and possible branches
                        prevent determining whether right turns are permitted.
Step 6  u_turn          not_determined (WRONG, label prohibited): The obscured lane-use arrow prevents
                        determining its movement restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: both lane changes are prohibited by visible solid separators, intersection
                        movements remain unresolved because the arrowhead is obscured, and no waiting area is
                        identified.
Advice                  Stay between the solid white lines and confirm the complete lane arrow before
                        committing to an intersection movement. Obey the traffic signals, keep the crosswalk
                        clear and stop at the designated stop line if required once it becomes visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 4533, out 1152, 20.38 s

culane_test__d100_05251222_0385_02280 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        writing, blue registration plates and road-sign style. My car is in the leftmost lane
                        of a multilane urban road beside an elevated structure; the next junction and the
                        lane's terminal markings are not visible. (lanes 4, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised curb and guardrail on the left, with a
                        planted strip beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken paint, with visible dashes and gaps, separates my lane from another same-
                        direction traffic lane on the right; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge and right lane divider place my car in lane 1; four
                        same-direction lanes appear present, although vehicles obscure the far-right roadway
                        extent. | roles: The solid white line beside the curb fits a roadway edge, and the
                        broken white line fits a same-direction lane divider. | markings: No guidance marking
                        is readable on the visible pavement of my lane; the overhead directional sign is
                        context, not a painted lane marking. | unseen: The far-right lane count is uncertain,
                        and pavement farther ahead is hidden by vehicles and perspective; no arrow or terminal
                        marking has been inferred from the sign. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese road rules, the solid roadway edge and
                        raised curb prohibit leaving the lane across this left boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe.
Step 6  change_left     prohibited (correct): The solid white roadway edge and raised curb prohibit crossing
                        the left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a rightward lane change when
                        safe.
Step 6  go_straight     not_determined (WRONG, label prohibited): The lane-end pavement where a governing
                        arrow could appear is hidden farther ahead.
Step 6  turn_left       not_determined (WRONG, label allowed): The lane-end pavement where a governing arrow
                        could appear is hidden farther ahead.
Step 6  turn_right      not_determined (WRONG, label prohibited): The lane-end pavement where a governing
                        arrow could appear is hidden farther ahead.
Step 6  u_turn          not_determined (WRONG, label allowed): The lane-end pavement where a governing arrow
                        or prohibited-movement marking could appear is hidden farther ahead.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: boundary decisions follow the visible lines and curb, junction movements
                        remain undecided because their pavement markings are hidden, and signs have not been
                        substituted for lane markings.
Advice                  Do not cross the left edge; a rightward lane change is permitted by the broken line
                        only when a safe gap exists. The overhead sign indicates left-turn/U-turn use for the
                        leftmost lane, so confirm the upcoming pavement markings and junction controls before
                        choosing your movement.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added [], missed
                        ['arrow:left', 'arrow:u_turn']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 4533, out 1045, 21.14 s

culane_test__d100_05251222_0385_02400 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        writing, blue vehicle plates and road layout. My car is in the second of four same-
                        direction lanes on an urban road beside an elevated structure; the road continues
                        ahead, but the next junction is not clearly visible. (lanes 4, mine 2, partial)
Step 2  Left            A continuous white solid line runs along my lane's left side, with another traffic
                        lane beyond it and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line runs along my lane's right side, with another traffic
                        lane beyond it and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; its shaft and any lower branches are hidden by the hood.
Step 4  Cross-check     position: Lane lines on both sides agree with my car occupying an interior lane; four
                        same-direction lanes appear present, though the outer-right layout is partly obscured
                        by vehicles. | roles: White solid lines are consistent with same-direction lane
                        dividers that prohibit crossing. | markings: The visible forward arrowhead is
                        compatible with this lane continuing ahead; the hidden lower portion prevents
                        excluding additional arrow branches. | unseen: No hidden arrow branches are asserted,
                        and no stop line, waiting area or intersection layout is inferred. | result:
                        consistent
Step 5  Rule            left_boundary: In mainland China, a solid white lane divider prohibits crossing it to
                        leave this lane.
Step 5  Rule            right_boundary: In mainland China, a solid white lane divider prohibits crossing it to
                        leave this lane.
Step 5  Rule            arrow:straight: A forward lane-use arrow permits proceeding straight, but the obscured
                        lower portion prevents determining whether additional movements are also indicated.
Step 6  change_left     prohibited (correct): The solid white left lane divider prohibits crossing.
Step 6  change_right    prohibited (correct): The solid white right lane divider prohibits crossing.
Step 6  go_straight     allowed (correct): The visible forward arrowhead permits straight travel.
Step 6  turn_left       not_determined (WRONG, label prohibited): The arrow's lower portion is hidden, so a
                        left-turn branch cannot be confirmed or excluded.
Step 6  turn_right      not_determined (WRONG, label prohibited): The arrow's lower portion is hidden, so a
                        right-turn branch cannot be confirmed or excluded.
Step 6  u_turn          not_determined (WRONG, label prohibited): The incomplete arrow prevents establishing
                        the full lane-use restriction governing a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Continue straight within the solid white boundaries; do not change lanes across them.
                        Before attempting any turn, obtain a clear view of the complete lane arrow and
                        junction controls.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1113, 20.73 s

culane_test__d100_05251222_0385_04920 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese vehicle
                        markings and blue registration plates. My car is approaching a large signalized
                        intersection beneath an elevated railway, apparently in the second lane from the left;
                        the total number of approach lanes is uncertain. (lanes None, mine 2, partial)
Step 2  Left            A continuous white line separates my lane from the adjacent approach lane on the left;
                        no curb is visible along it.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates my lane from another approach lane on the right; no
                        curb is visible along it.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white straight-ahead arrow is painted in my lane, with its
                        forward tip partly obscured by the car ahead.; line:stop_line (partial): A transverse
                        white stop line crosses my lane near the car ahead, which obscures part of it.;
                        line:crosswalk (partial): White zebra-crossing stripes extend across the approach
                        beyond the stop line, partly obscured by vehicles.
Step 4  Cross-check     position: A same-direction lane is visible on the left, consistent with my lane being
                        second from the left; another lane is visible on the right, but the far-right extent
                        is uncertain. | roles: Both white solid boundaries fit same-direction lane separators
                        on an intersection approach. | markings: The visible straight arrow is consistent with
                        an intersection approach lane bounded by solid lane lines; the stop line and crosswalk
                        do not conflict with it. | unseen: The total lane count is not asserted; the arrow tip
                        and portions of the transverse markings are obscured. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes on this approach.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes on this approach.
Step 5  Rule            arrow:straight: The straight-ahead lane-use arrow requires proceeding straight rather
                        than turning left, right, or making a U-turn from this lane.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before this line.
Step 5  Rule            line:crosswalk: The crossing requires yielding to pedestrians as applicable and must
                        not be obstructed.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The visible straight-ahead arrow permits straight travel.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary rules govern lane changes, the identifiable straight arrow
                        governs intersection movements, and no waiting-area action is inferred.
Advice                  Remain in this lane for straight travel and do not cross either solid boundary to
                        change lanes. Obey the applicable signal, stop before the stop line when required, and
                        keep the pedestrian crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4533, out 1363, 25.45 s

culane_test__d100_05251222_0385_05250 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, suggested by the blue license
                        plates and road layout. My car is in the leftmost of three same-direction lanes on a
                        divided road, with a bridge ahead and no intersection or lane ending visible. (lanes
                        3, mine 1, full)
Step 2  Left            A solid white line borders my lane on the left, with a diagonally striped buffer and a
                        metal median barrier beyond it; the barrier does not directly bound my lane.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left edge line and the lane line on the right agree with my car being in
                        lane 1 of three same-direction lanes. | roles: The solid white line beside the striped
                        median buffer fits an edge line, and the broken white line between traffic lanes fits
                        a lane line. | markings: No guidance markings are visible within my lane; the diagonal
                        stripes lie outside its left boundary. | unseen: No hidden arrows or intersection
                        markings have been inferred; the lane's eventual endpoint is outside the visible
                        scene. | result: consistent
Step 5  Rule            left_boundary: Under Chinese road-marking rules, this solid white roadway edge
                        restricts crossing into the striped buffer, so my car must not leave the lane across
                        it during ordinary driving.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent same-
                        direction lane when safe and without interfering with other traffic.
Step 6  change_left     prohibited (correct): The solid white edge line prohibits crossing into the striped
                        buffer.
Step 6  change_right    allowed (correct): The broken white lane divider permits a lane change when safe.
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
Advice                  Stay to the right of the solid left edge line and out of the striped buffer; change
                        right only after checking traffic. No visible markings establish turn permissions or a
                        stopping point, so reassess when the next junction becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 946, 16.41 s

culane_test__d100_05251309_0397_03150 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with right-hand traffic, based on the Chinese
                        roadside writing, blue licence plates and road layout. My car is in the rightmost of
                        three same-direction lanes on a divided urban road, approaching a junction whose far
                        end is obscured by distance and vehicles. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line follows the right side of my lane beside a raised curb,
                        beyond which lies a planted strip and a separate paved path.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight_right (partial): A white combined straight-and-right arrow is painted
                        ahead in my lane; its right-pointing head is clear, while the SUV partly obscures the
                        forward head.
Step 4  Cross-check     position: The rightmost position in three lanes agrees with a lane divider on the left
                        and a curb-side road edge on the right. | roles: The white broken divider fits a same-
                        direction lane line, and the solid white line beside the curb fits a roadway edge. |
                        markings: The visible combined straight-and-right arrow is compatible with this
                        rightmost lane and does not conflict with either boundary. | unseen: The forward
                        arrowhead is partly obscured, and no stop line or crosswalk can be resolved farther
                        ahead; neither is assumed. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a broken white lane divider
                        permits crossing to change lanes when safe.
Step 5  Rule            right_boundary: The solid roadway edge and raised curb do not permit leaving this
                        traffic lane across its right boundary.
Step 5  Rule            arrow:straight_right: A combined straight-and-right lane-use arrow permits straight
                        travel or a right turn, not a left turn or U-turn.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid road edge and raised curb prohibit crossing out of the
                        lane to the right.
Step 6  go_straight     allowed (correct): The identifiable straight-and-right arrow permits straight travel,
                        although its forward head is partly obscured.
Step 6  turn_left       prohibited (correct): The straight-and-right lane-use arrow excludes a left turn from
                        this lane.
Step 6  turn_right      allowed (correct): The clearly visible right-pointing arrowhead permits a right turn.
Step 6  u_turn          prohibited (correct): The straight-and-right lane-use arrow excludes a U-turn from
                        this lane.
Step 6  enter_waiting_areanot_applicable: No visible waiting-area marking governs this action.
Step 7  Reflect         consistent
Advice                  Use this lane for straight travel or a right turn, subject to the junction controls;
                        do not cross the curb-side boundary. For a left turn or U-turn, first move safely
                        across the broken divider into an appropriately marked lane; no stopping position is
                        readable in this image.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1041, 19.26 s

culane_test__d100_05251309_0397_03390 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese writing,
                        blue vehicle plates and road layout. The car is approaching a wide signal-controlled
                        intersection, apparently in the third of four approach lanes, although the far-left
                        lane arrangement is less clear. (lanes 4, mine 3, partial)
Step 2  Left            A continuous white line runs along the left of my lane, with the lane occupied by the
                        white van beyond it; no curb is visible on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, separating it from another
                        approach lane; the raised roadside curb is beyond that adjacent lane.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A forward-pointing white arrowhead is visible immediately
                        ahead of the hood, but the lower portion of the arrow is obscured.; arrow:straight
                        (partial): A smaller white forward-pointing arrow is visible farther ahead in my lane;
                        its fine details are indistinct at this distance.; line:stop_line (partial): A
                        transverse white stopping line is visible near the intersection entrance, with its
                        exact edges less distinct in the distance.
Step 4  Cross-check     position: Lane lines on both sides agree with an interior lane, with another same-
                        direction lane on each side; the apparent third-of-four position remains tentative
                        because the far-left arrangement is less clear. | roles: The white continuous
                        boundaries fit solid approach-lane separators rather than center lines or roadside
                        edges. | markings: The visible forward arrowheads agree with each other and do not
                        conflict with the lane boundaries; obscured arrow portions prevent confidently
                        excluding additional directional branches. | unseen: No hidden arrow branch is
                        asserted, and the distant far-left lane arrangement and transverse marking are treated
                        as uncertain. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        into the lane on the left.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        into the lane on the right.
Step 5  Rule            arrow:straight: The visible forward arrowhead permits proceeding straight, but the
                        obscured remainder prevents establishing whether another movement is also indicated.
Step 5  Rule            arrow:straight: The distant forward arrow supports straight travel, but its indistinct
                        details cannot reliably establish additional permitted movements.
Step 5  Rule            line:stop_line: The stop line indicates where the vehicle must stop when required by
                        the traffic signal or traffic control.
Step 6  change_left     prohibited (correct): The solid white left lane separator prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane separator prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The visible forward arrowheads permit straight travel.
Step 6  turn_left       not_determined (WRONG, label prohibited): The obscured and distant arrow details
                        prevent reliably determining whether a left-turn branch is present.
Step 6  turn_right      not_determined (WRONG, label prohibited): The obscured and distant arrow details
                        prevent reliably determining whether a right-turn branch is present.
Step 6  u_turn          not_determined (WRONG, label prohibited): The complete directional arrow markings
                        cannot be read well enough to determine U-turn permission.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain between the solid white lines; the visible arrows support continuing straight,
                        subject to the applicable signal. Do not assume this lane permits a turn from the
                        incomplete arrow views, and stop before the stop line whenever required.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:stop_line'], missed []), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 4533, out 1529, 30.95 s

culane_test__d100_05251327_0403_00180 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, suggested by the Chinese writing on
                        the truck and the roadway layout. My car is in the leftmost of three same-direction
                        lanes on a divided urban road; the road continues ahead, but the next intersection is
                        not clearly visible. (lanes 3, mine 1, full)
Step 2  Left            A solid white line runs along the left of my lane, beside a raised curb and a paved
                        strip with trees beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction traffic lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead; the hood hides the lower shaft, and no branching head is visible.
Step 4  Cross-check     position: The left roadway edge and the lane divider on the right agree with being in
                        lane 1 of three. | roles: The solid white line beside the curb fits a roadway edge;
                        the broken white line fits a same-direction lane divider. | markings: The visible
                        forward-pointing arrow agrees with a through lane, with no conflicting marking
                        visible. | unseen: The arrow's lower shaft is hidden by the hood, and the distant lane
                        endpoint cannot be inspected; no distant stop line, crosswalk, or waiting area is
                        inferred. | result: consistent
Step 5  Rule            left_boundary: Under the apparent Chinese road-marking rules, this solid roadway edge
                        and raised curb prohibit leaving the lane across its left boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 6  change_left     prohibited (correct): The solid left roadway edge and raised curb prohibit crossing to
                        the left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a rightward lane change when
                        safe.
Step 6  go_straight     allowed (correct): The visible forward arrowhead identifies the permitted straight
                        movement.
Step 6  turn_left       prohibited (correct): The straight-only lane-use arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only lane-use arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only lane-use arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent: the visible arrowhead identifies the movement despite its hidden lower
                        shaft, boundary rules govern only lateral crossing, and no unseen endpoint marking is
                        assumed.
Advice                  Remain in this lane to continue straight; a rightward lane change is permitted after
                        checking surrounding traffic, but do not cross the left edge or curb. For a turn or
                        U-turn, find an appropriately marked lane ahead; the next stopping point is not
                        visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1003, 17.29 s

culane_test__d100_05251327_0403_00630 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        writing and roadway layout. My car is in the left lane of a two-lane, barrier-
                        separated urban roadway continuing ahead; no intersection or lane ending is visible.
                        (lanes 2, mine 1, full)
Step 2  Left            A solid white line runs along the left of my lane, with a narrow paved margin and a
                        concrete barrier topped by fencing beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with visible long dashes and intervening gaps, separates my lane
                        from another same-direction lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and my position as lane 1 agree with a roadway edge
                        on my left and a lane divider on my right. | roles: The solid white left edge and
                        broken white same-direction divider fit their observed roles. | markings: No arrows,
                        words, symbols, transverse lines, or marked waiting areas are visible in my lane. |
                        unseen: No hidden markings or movements at an unseen intersection have been inferred;
                        the country identification is tentative. | result: consistent
Step 5  Rule            left_boundary: Under the inferred mainland Chinese rules, the solid roadway edge line
                        must not be crossed, and the concrete barrier also prevents leaving the roadway on
                        this side.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes
                        across it when safe.
Step 6  change_left     prohibited (correct): The solid left roadway edge and concrete barrier prohibit
                        crossing this boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing into the adjacent
                        lane when safe.
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
Step 7  Reflect         Consistent: only the boundary-crossing actions are governed by visible markings, and
                        no permission for an unseen intersection movement is inferred.
Advice                  Remain within the left roadway edge; you may move into the right lane across the
                        broken white divider after checking traffic. No intersection movement guidance or stop
                        line is visible, so do not infer turning permission from this view.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 894, 14.66 s

culane_test__d100_05251327_0403_00930 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese writing and road layout, with
                        traffic keeping right. My car is in the leftmost of three same-direction lanes on a
                        divided urban road approaching a junction whose details are distant. (lanes 3, mine 1,
                        full)
Step 2  Left            A solid white line runs along the left of my lane beside a raised curb and a planted
                        central divider.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White long dashes separated by visible gaps divide my lane from another same-direction
                        traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A large white arrow in my lane has a single head pointing
                        straight ahead.
Step 4  Cross-check     position: The left roadway edge and the right lane divider agree with my car being in
                        lane 1 of three same-direction lanes. | roles: The solid white line beside the central
                        divider fits a roadway edge; the broken white line on the right fits a same-direction
                        lane divider. | markings: The straight-only arrow is consistent with a through lane;
                        no conflicting words, arrows, or waiting areas are visible in my lane. | unseen: No
                        distant stop line or obscured marking has been inferred; the exact junction layout is
                        too distant to read. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, the solid roadway edge and raised
                        divider prohibit leaving the lane across its left boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 6  change_left     prohibited (correct): The solid left edge and raised divider prohibit crossing to the
                        left.
Step 6  change_right    allowed (correct): The broken white right lane divider permits a lane change when
                        safe.
Step 6  go_straight     allowed (correct): The single straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight; do not cross the left edge or turn from this lane.
                        If another movement is needed, change right only when safe and seek the appropriate
                        signed or marked lane; no stop line is clearly visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 951, 15.99 s

culane_test__d100_05251327_0403_01200 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be Taiwan, with traffic keeping right, suggested by the Chinese road
                        lettering and road layout. My car is in the middle of three same-direction lanes on a
                        divided, barrier-lined elevated road; no intersection or lane ending is visible ahead.
                        (lanes 3, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        traffic lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line, with visible dashes and gaps, separates my lane from another
                        traffic lane on the right; the concrete barrier is beyond that adjacent lane, not at
                        my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        text:other (partial): White Chinese characters are painted lengthwise in my lane
                        ahead; foreshortening and the vehicle ahead prevent a reliable reading of the complete
                        inscription.
Step 4  Cross-check     position: Three lanes and ego lane 2 agree with a same-direction lane line on each
                        side. | roles: Both broken white boundaries fit ordinary same-direction lane
                        separators. | markings: The partially legible Chinese inscription does not establish a
                        directional arrow or conflict with the boundary observations; no waiting area is
                        visible. | unseen: The complete inscription and the distant roadway beneath vehicles
                        are not readable; no unseen arrow, intersection, or text meaning has been assumed. |
                        result: consistent
Step 5  Rule            left_boundary: Under Taiwan's rules, a broken white lane separator permits crossing to
                        the adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: Under Taiwan's rules, a broken white lane separator permits crossing
                        to the adjacent same-direction lane when safe.
Step 5  Rule            text:other: The inscription cannot be read reliably enough to assign its specific
                        restriction, and text alone does not govern any of the seven requested maneuvers.
Step 6  change_left     allowed (correct): The broken white lane separator permits a safe lane change left.
Step 6  change_right    allowed (correct): The broken white lane separator permits a safe lane change right.
Step 6  go_straight     not_applicable: No visible directional arrow or prohibited-movement marking governs
                        this action.
Step 6  turn_left       not_applicable: No visible directional arrow or prohibited-movement marking governs
                        this action.
Step 6  turn_right      not_applicable: No visible directional arrow or prohibited-movement marking governs
                        this action.
Step 6  u_turn          not_applicable: No visible directional arrow or prohibited-movement marking governs
                        this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: the broken lane lines permit lane changes, while no intersection movement
                        or waiting-area permission is inferred from the unreadable text.
Advice                  Remain in your lane or cross either broken white boundary only after checking traffic
                        and signaling. Read the Chinese pavement restriction as it becomes clearer; no visible
                        intersection or turn-lane guidance establishes where to turn.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['text:other'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1116, 20.36 s

culane_test__d100_05251327_0403_02340 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese writing,
                        blue vehicle plates and road layout. My car is in the left lane of a two-lane urban
                        carriageway bending gently left; no intersection or lane ending is visible. (lanes 2,
                        mine 1, full)
Step 2  Left            A solid white line follows a raised curb and fenced separating strip on the left, with
                        a separate roadway beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line separates my lane from another paved traffic lane on the
                        right; there is no curb at this line.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two lanes and ego lane index 1 agree with a roadway edge on the left and a
                        lane divider on the right. | roles: The white solid left edge line alongside a curb
                        and the white solid right lane divider fit their observed roles. | markings: No
                        guidance arrows, words, symbols or transverse markings are visible in my lane. |
                        unseen: No markings are inferred beneath the car ahead or beyond the visible road; the
                        next intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised curb do not permit leaving the lane
                        to the left onto the separating strip.
Step 5  Rule            right_boundary: Under Chinese road-marking rules, a solid white lane divider prohibits
                        crossing it to change lanes.
Step 6  change_left     prohibited (correct): The left roadway edge has a raised curb and separating strip
                        that must not be crossed.
Step 6  change_right    prohibited (correct): The solid white lane divider prohibits crossing into the lane on
                        the right.
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
Step 7  Reflect         consistent: both boundary-crossing actions are prohibited, while no visible movement
                        or waiting-area marking governs the remaining actions.
Advice                  Stay within the current lane without crossing either boundary, and observe the posted
                        30 km/h limit. No turn-lane assignment or stopping point is visible; reassess the
                        markings as the road ahead comes into view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 874, 15.08 s

culane_test__d100_05251327_0403_03870 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese writing and
                        blue Chinese-format registration plate. My car is in the left of two apparent same-
                        direction lanes on a narrow urban road beside an elevated structure; the road
                        continues ahead, but the car in front obscures the distant layout. (lanes 2, mine 1,
                        partial)
Step 2  Left            A continuous white line runs along the left side of my lane beside a raised curb and a
                        narrow sidewalk, with the elevated structure's wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white longitudinal line segment separates my lane from roadway on the right; the car
                        ahead and my hood limit the visible stretch, so a complete dash-and-gap pattern cannot
                        be confirmed.
                        white none, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left roadway edge places my car in the leftmost lane; the white
                        separator and roadway to its right suggest a second same-direction lane, although the
                        complete layout is not clear. | roles: The white solid line beside the left curb fits
                        an edge line. The white line on the right fits a same-direction lane separator, but
                        its solid or broken pattern is unresolved. | markings: No readable guidance marking is
                        visible in my lane; there is no visible marking that contradicts the boundary
                        interpretation. | unseen: No arrow or waiting area has been inferred beneath the car
                        ahead. The right boundary's pattern and the distant lane layout remain uncertain; its
                        pattern value denotes that no complete pattern can be established, not an absence of
                        paint. | result: consistent
Step 5  Rule            left_boundary: In China, the solid roadway edge and raised curb do not permit an
                        ordinary lane-change movement onto the sidewalk.
Step 5  Rule            right_boundary: In China, a broken white lane separator permits crossing when safe,
                        whereas a solid white separator prohibits crossing; the visible stretch does not
                        establish which applies.
Step 6  change_left     prohibited (correct): The solid left edge and raised curb prohibit moving out onto the
                        sidewalk.
Step 6  change_right    not_determined (WRONG, label prohibited): The right separator's solid or broken
                        pattern cannot be established, leaving crossing permission undecided.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the left crossing is prohibited, the uncertain right separator leaves that
                        crossing undecided, and no unseen movement guidance is treated as permission.
Advice                  Remain within the lane and leave stopping space behind the braking car; do not cross
                        the left edge or mount the curb. Confirm the right separator and any guidance revealed
                        ahead before changing lanes or choosing a turning lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1089, 23.33 s

culane_test__d100_05251327_0403_03960 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese writing and
                        blue Chinese registration plate. My car is in the left of two apparent same-direction
                        lanes on an urban road beside an elevated structure; the road continues ahead, but the
                        lead car obscures much of the lane and no intersection is clearly visible. (lanes 2,
                        mine 1, partial)
Step 2  Left            A single continuous white line runs beside a raised curb and narrow paved strip on the
                        left, with the elevated structure's wall beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line separates my lane from roadway on the right; its exposed foreground
                        portion is continuous, but the lead car hides the farther stretch, so a solid line
                        cannot confidently be distinguished from a long dash.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: A left roadway edge and an apparent same-direction lane to the right support
                        identifying my lane as the leftmost of two lanes, although the overall layout is
                        partly obscured. | roles: The white line beside the left curb fits an edge-line role;
                        the white line on the right fits a lane separator, but its complete pattern is
                        uncertain. | markings: No arrows, words, symbols, waiting areas or transverse lines
                        are readable in the visible portions of my lane. | unseen: The right boundary's
                        complete pattern and markings beneath or beyond the lead car cannot be established; no
                        hidden marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: The roadway edge and raised curb do not permit an ordinary driving
                        maneuver out of the lane onto the paved strip on the left.
Step 5  Rule            right_boundary: Under Chinese marking rules, a solid white lane separator prohibits
                        crossing and a broken white separator permits a safe lane change, but the visible
                        stretch does not establish which pattern applies.
Step 6  change_left     prohibited (correct): The left roadway edge is bounded by a raised curb, which
                        prohibits driving across it.
Step 6  change_right    not_determined (WRONG, label prohibited): The right separator's solid-versus-broken
                        pattern is partly hidden, leaving crossing permission undecided.
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
Step 7  Reflect         Consistent: the curb prohibits moving left, the uncertain right-line pattern leaves
                        moving right undecided, and no unseen directional marking is used to assign movement
                        permissions.
Advice                  Remain in your lane behind the lead car and do not cross the left curb. Before
                        changing right or choosing a turning lane, wait until the separator pattern and any
                        upcoming lane-use markings are clearly visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1021, 20.65 s

culane_test__d100_05251627_0452_02850 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese signage, blue
                        registration plates and opposing traffic to the left of the median fence. My car is in
                        the leftmost lane approaching a signal-controlled junction beneath an overpass;
                        vehicles obscure the full lane count and the end of my lane. (lanes None, mine 1,
                        partial)
Step 2  Left            A continuous yellow line runs beside a raised median base and metal fence, with
                        opposing traffic beyond.
                        yellow solid, curb yes, center_line, evidence full
Step 2  Right           A worn white line appears continuous along the visible stretch to the right of my
                        lane, with same-direction vehicles beyond; its farther portion is obscured by traffic.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median boundary places my lane leftmost, and the white boundary
                        separates it from another same-direction lane; traffic obscures the total lane count.
                        | roles: The yellow median boundary separates opposing directions, while the white
                        line separates same-direction lanes. | markings: No guidance marking can be identified
                        on the exposed pavement in my lane; the hood, vehicles and distant shadow obscure
                        other portions. | unseen: No hidden arrow, stop line or waiting area has been
                        inferred; the right line is described as solid only over its visible stretch. |
                        result: consistent
Step 5  Rule            left_boundary: In China, the solid yellow opposing-traffic boundary must not be
                        crossed, and the median barrier also prevents leaving the lane to the left.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits changing lanes
                        across its visible solid stretch.
Step 6  change_left     prohibited (correct): The solid yellow boundary and physical median prohibit crossing
                        to the left.
Step 6  change_right    prohibited (correct): The visible solid white lane boundary prohibits crossing to the
                        right.
Step 6  go_straight     not_determined: The lane-end pavement is obscured, so a governing directional marking
                        cannot be established.
Step 6  turn_left       not_determined: The lane-end pavement is obscured, so a governing directional marking
                        cannot be established.
Step 6  turn_right      not_determined: The lane-end pavement is obscured, so a governing directional marking
                        cannot be established.
Step 6  u_turn          not_determined: The lane-end pavement is obscured, so a governing directional or
                        prohibited-movement marking cannot be established.
Step 6  enter_waiting_areanot_determined: The junction approach is obscured, preventing confirmation of a
                          marked waiting area ahead.
Step 7  Reflect         consistent
Advice                  Remain between the median and the solid white line; do not change lanes across either
                        boundary. Slow for the queue and obey the junction signals, confirming lane arrows and
                        the stop line as they become visible before choosing a junction movement.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 966, 19.44 s

culane_test__d100_05251718_0469_00390 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the blue registration
                        plates, Chinese-style road signs and road layout. My car is approaching a signalized
                        intersection in an interior lane of a wide urban road; the full extent of the same-
                        direction lanes cannot be counted confidently from this view. (lanes None, mine None,
                        insufficient)
Step 2  Left            A continuous white line runs along the left side of my lane toward the intersection,
                        with another traffic lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right side of my lane toward the intersection,
                        with another traffic lane beyond it and no curb.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; its lower shaft is obscured by the hood.; line:stop_line (full): A
                        solid white transverse stop line crosses my lane before the pedestrian crossing.;
                        line:crosswalk (full): Broad white pedestrian-crossing stripes extend across my lane
                        beyond the stop line.
Step 4  Cross-check     position: Both boundaries separate my lane from other same-direction lanes, confirming
                        an interior position; the total lane count and exact index remain uncertain. | roles:
                        The white solid lines fit same-direction lane dividers on an intersection approach. |
                        markings: The visible forward arrow, stop line and crosswalk are mutually consistent;
                        no waiting area is visible ahead of my lane. | unseen: The arrow shaft is partly
                        hidden by the hood, and the complete lateral lane arrangement is uncertain; neither is
                        reconstructed. | result: consistent
Step 5  Rule            left_boundary: Under Chinese road-marking rules, a solid white lane divider prohibits
                        crossing it to change lanes.
Step 5  Rule            right_boundary: Under Chinese road-marking rules, a solid white lane divider prohibits
                        crossing it to change lanes.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns and U-turns from this lane.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before this line.
Step 5  Rule            line:crosswalk: The marked pedestrian crossing requires yielding to pedestrians and
                        keeping the crossing clear.
Step 6  change_left     prohibited (correct): The solid white left lane divider prohibits crossing into the
                        adjoining lane.
Step 6  change_right    prohibited (correct): The solid white right lane divider prohibits crossing into the
                        adjoining lane.
Step 6  go_straight     allowed (correct): The visible forward arrowhead identifies a straight-ahead lane.
Step 6  turn_left       prohibited (correct): The straight-only lane arrow excludes a left turn.
Step 6  turn_right      prohibited (correct): The straight-only lane arrow excludes a right turn.
Step 6  u_turn          prohibited (correct): The straight-only lane arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjoining two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight-ahead travel and do not cross either solid divider;
                        turning requires an appropriate lane selected before the solid-line section. Obey the
                        applicable signal, stop before the stop line when required, and keep the pedestrian
                        crossing clear.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4533, out 1388, 26.1 s

culane_test__d100_05251718_0469_01320 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, inferred from the simplified Chinese writing and
                        blue vehicle plates, with traffic keeping right. My car is in the left lane of a two-
                        lane urban carriageway passing beneath a pedestrian bridge; no intersection or lane
                        ending is visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A solid white line follows the raised curb on the left, with a paved pedestrian area
                        and bridge supports beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible long dash and gap farther ahead, separates my lane
                        from another lane carrying traffic in the same direction; there is no curb at this
                        boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and my position as lane 1 agree with a left roadway
                        edge and a right lane divider. | roles: The solid white line beside the left curb fits
                        an edge line; the broken white divider on the right fits a same-direction lane line. |
                        markings: No guidance markings are visible within my lane, so none contradict the
                        boundaries. | unseen: Vehicles obscure some pavement ahead, and the next intersection
                        is not visible; no markings or intersection layout have been inferred there. | result:
                        consistent
Step 5  Rule            left_boundary: Under mainland Chinese road-marking rules, the solid roadway edge and
                        raised curb prohibit leaving this lane across its left boundary.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe and without interfering with other traffic.
Step 6  change_left     prohibited (correct): The solid left roadway edge and raised curb prohibit crossing to
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
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: only the boundary-crossing actions are decided by the visible markings,
                        and no intersection movement permission is inferred.
Advice                  Stay within the left curb boundary; moving into the right lane is permitted only after
                        checking traffic and clearance. No visible arrows establish which lane to use for
                        turns at the next intersection, and no stop line is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 902, 15.08 s

culane_test__d100_05251718_0469_02040 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, inferred from the Chinese
                        writing and the divided-road layout. My car is in the left of two same-direction lanes
                        on a tree-lined urban road; no intersection or lane ending is visible ahead. (lanes 2,
                        mine 1, full)
Step 2  Left            A raised concrete curb borders the lane beside a planted median; no separate painted
                        boundary line is clearly visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           A white broken line, with a visible long dash and gaps, separates my lane from another
                        same-direction traffic lane; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 1 agree with a median curb on
                        the left and a lane separator on the right. | roles: The physical median edge fits the
                        left edge role, and the broken white line fits separation of same-direction lanes. |
                        markings: No guidance markings are visible within my lane, so there is no conflict
                        with either boundary. | unseen: No separate paint is inferred from the light-colored
                        curb; no distant intersection markings or movements are assumed. | result: consistent
Step 5  Rule            left_boundary: The raised median curb is a physical roadway boundary and must not be
                        crossed to leave this lane.
Step 5  Rule            right_boundary: Under Chinese road-marking rules, a broken white same-direction lane
                        separator permits crossing to change lanes when safe.
Step 6  change_left     prohibited (correct): The raised median curb prohibits leaving the lane across the
                        left boundary.
Step 6  change_right    allowed (correct): The broken white lane separator permits a rightward lane change
                        when safe.
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
Advice                  Stay clear of the median curb; you may change to the right lane across the broken
                        white line after checking traffic and blind spots. No visible markings establish
                        turning permissions or a stopping point ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 860, 14.79 s

culane_test__d100_05251718_0469_02250 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, based on the blue Chinese-style vehicle plates, with traffic
                        keeping right. My car is in the leftmost of two same-direction lanes on a tree-lined
                        divided urban road; no intersection or lane ending is clearly visible ahead. (lanes 2,
                        mine 1, full)
Step 2  Left            A raised concrete curb borders the lane on the left, with grass, trees and a hedge
                        beyond; no separate painted boundary line is clearly visible.
                        none none, curb yes, edge_line, evidence full
Step 2  Right           White broken line segments separate my lane from the same-direction lane on the right;
                        the silver car obscures part of the farther boundary, and no curb forms this side of
                        my lane.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The left curb and right lane divider agree with my car being in lane 1 of
                        two same-direction lanes. | roles: The physical left edge and white broken same-
                        direction divider fit their assigned roles. | markings: No readable guidance markings
                        or waiting areas are visible in my lane, so none contradict the boundaries. | unseen:
                        No paint is inferred along the left curb; the right divider's partial obstruction is
                        acknowledged. No unseen intersection markings are inferred. | result: consistent
Step 5  Rule            left_boundary: The raised road-edge curb is not a traversable lane boundary and
                        prohibits moving left across it.
Step 5  Rule            right_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when it is safe and does not interfere with other traffic.
Step 6  change_left     prohibited (correct): The raised left curb prohibits crossing out of the roadway.
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
Step 7  Reflect         Consistent: the boundary decisions follow the observed curb and broken divider, while
                        the absence of visible movement markings is not treated as permission for intersection
                        movements.
Advice                  Stay within the left curb; a rightward lane change is permitted by the divider only
                        when clear of the silver car and other traffic. No turn assignment or stopping line is
                        visible, so follow the markings and controls that become visible farther ahead.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1076, 22.66 s

culane_test__d100_05251718_0469_05070 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, suggested by the blue
                        lane-direction sign, vehicle plates and road layout. My car is in the left lane of a
                        tree-lined, divided urban road with two visible lanes in this direction; the road
                        continues ahead, with no intersection or lane end clearly visible. (lanes 2, mine 1,
                        full)
Step 2  Left            A narrow solid white line runs beside the raised curb on the left, with a planted
                        median beyond; its distant portion becomes difficult to distinguish.
                        white solid, curb yes, edge_line, evidence partial
Step 2  Right           A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction traffic lane on the right; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two visible same-direction lanes and ego position 1 agree with the median-
                        side edge on the left and a lane divider on the right. | roles: The white line beside
                        the median curb fits an edge line, and the broken white divider fits a same-direction
                        lane line. | markings: No pavement arrows, words, symbols, transverse lines or waiting
                        areas are readable in my visible lane; the overhead sign is context, not a pavement
                        marking. | unseen: No lane-end markings are inferred from the overhead sign; the next
                        intersection and any markings there are outside the readable view. | result:
                        consistent
Step 5  Rule            left_boundary: In mainland China, the raised median curb is not a traversable lane
                        boundary and prohibits leaving this lane across the left side.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits crossing to change
                        lanes when safe and without obstructing other traffic.
Step 6  change_left     prohibited (correct): The raised median curb prohibits crossing the left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the lane
                        on the right.
Step 6  go_straight     not_determined: The next intersection and any lane-use pavement markings governing its
                        movements are not visible.
Step 6  turn_left       not_determined: The next intersection and any lane-use pavement markings governing its
                        movements are not visible.
Step 6  turn_right      not_determined: The next intersection and any lane-use pavement markings governing its
                        movements are not visible.
Step 6  u_turn          not_determined: The next intersection and any pavement markings governing U-turns are
                        not visible.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: boundary-crossing decisions follow the visible boundaries, intersection
                        movements remain undecided because their governing features are out of view, and no
                        waiting area is inferred.
Advice                  Stay clear of the median curb; a rightward lane change is permitted by the dashed
                        divider only when traffic allows. Check the overhead lane-direction sign and upcoming
                        pavement markings before choosing a lane for an intersection movement; no stopping
                        line is visible here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 985, 17.81 s

culane_test__d100_05251718_0469_05190 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, suggested by the
                        Chinese writing, blue vehicle plates and road layout. My car is in the middle of three
                        same-direction lanes on a tree-lined urban road; no intersection or lane ending is
                        clearly visible ahead. (lanes 3, mine 2, full)
Step 2  Left            A broken white line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with visible dashes and gaps separates my lane from another same-
                        direction lane on the right; the roadside curb is beyond that adjacent lane, not at my
                        lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Lane 2 of 3 agrees with having an adjacent same-direction lane across each
                        boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No arrows, words, symbols, transverse lines or marked waiting
                        areas are visible in my lane. | unseen: No distant intersection layout or obscured
                        pavement markings are inferred; the country identification is tentative. | result:
                        consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a broken white lane divider
                        permits crossing to change lanes when safe without interfering with other traffic.
Step 5  Rule            right_boundary: Under mainland Chinese marking rules, a broken white lane divider
                        permits crossing to change lanes when safe without interfering with other traffic.
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
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Either adjacent lane may be entered across the broken white divider after checking
                        traffic and signalling. No visible movement arrows or stop line establish turn-lane
                        assignments or a stopping point; follow upcoming markings, signs and signals.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 875, 14.22 s

culane_test__d100_05251947_0499_00840 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese-looking
                        building signage and roadway layout. My car is in the leftmost lane of an apparently
                        three-lane divided urban expressway; the road continues ahead beside an elevated
                        roadway, with no intersection or lane ending visible. (lanes 3, mine 1, partial)
Step 2  Left            A solid white line runs along a raised concrete median barrier on the left, with
                        opposing traffic beyond the barrier.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A broken white line, with a visible dash and gaps along its course, separates my lane
                        from another same-direction traffic lane on the right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left median edge and right lane divider place my car in lane 1; three
                        same-direction lanes appear present, although the outermost roadway is dark and less
                        distinct. | roles: The solid white median-edge line and broken white same-direction
                        lane divider fit their assigned roles. | markings: No arrows, words, symbols, waiting
                        areas or transverse markings are visible in my lane. | unseen: The total lane count is
                        tentative because the far-right roadway is poorly illuminated; no intersection beyond
                        the visible stretch is inferred. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, the solid roadway edge and concrete
                        median do not permit leaving the lane across this boundary.
Step 5  Rule            right_boundary: A broken white lane divider permits changing into the adjacent same-
                        direction lane when safe.
Step 6  change_left     prohibited (correct): The solid median-edge line and physical barrier prohibit
                        crossing the left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits crossing into the adjacent
                        lane when safe.
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
Advice                  Continue along the roadway without crossing the left median boundary; a rightward lane
                        change is permitted by the dashed marking only when safe. No intersection, turning
                        guidance or stopping point is visible, so these observations do not authorize a turn
                        or U-turn.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 868, 15.56 s

culane_test__d100_05251947_0499_04830 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the road layout,
                        markings and roadside development, though the country is uncertain. My car appears to
                        be in the rightmost of three same-direction lanes on a divided urban road; the road
                        continues ahead, but its next junction is not clearly visible. (lanes 3, mine 3,
                        partial)
Step 2  Left            A white broken line, with visible long painted segments and gaps, separates my lane
                        from another traffic lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white continuous line follows the right side of my lane beside a raised curb and
                        planted roadside strip; darkness reduces detail farther ahead.
                        white solid, curb yes, edge_line, evidence partial
Step 3  Markings        symbol:other (insufficient): A small pale painted shape lies ahead within my lane, but
                        distance and low light prevent reliable identification of its shape or any arrowheads.
Step 4  Cross-check     position: The apparent rightmost-lane position agrees with a lane divider on the left
                        and a curbed roadway edge on the right; the total of three lanes is less certain in
                        the dark left portion of the image. | roles: The broken white divider fits a same-
                        direction lane line, and the continuous white line beside the curb fits a roadway
                        edge. | markings: The distant painted shape cannot establish lane-use directions and
                        therefore cannot be checked against a particular permitted movement. | unseen: No
                        direction has been assigned to the unreadable paint, and no unseen stop line,
                        intersection layout or waiting area has been assumed. | result: consistent
Step 5  Rule            left_boundary: Under the presumed Chinese rules, a broken white same-direction lane
                        divider permits crossing to change lanes when safe.
Step 5  Rule            right_boundary: The curbed roadway edge is not an available lane-change route, so my
                        car must not drive across it.
Step 5  Rule            symbol:other: Unidentified paint cannot establish a movement permission or restriction
                        until its actual form can be read.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The raised curb at the roadway edge prohibits leaving the lane
                        across that side.
Step 6  go_straight     not_determined (WRONG, label prohibited): Distant lane-use paint and the lane's
                        eventual end are not readable enough to establish the permitted movement.
Step 6  turn_left       not_determined (WRONG, label prohibited): The distant paint cannot be checked for a
                        left-turn arrow or restriction.
Step 6  turn_right      not_determined (WRONG, label allowed): The distant paint cannot be checked for a
                        right-turn arrow or restriction.
Step 6  u_turn          not_determined (WRONG, label prohibited): The distant paint cannot be checked for a
                        U-turn arrow or restriction.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable in view.
Step 7  Reflect         consistent: boundary decisions apply only to crossing their respective sides, and
                        unreadable guidance has not been converted into a movement permission or prohibition.
Advice                  Stay within the curbed right edge; a left lane change is permitted only after checking
                        traffic and blind spots. Read the upcoming lane arrows and any junction controls
                        before choosing a turning lane, since this dark image does not establish the permitted
                        movements.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['symbol:other'], missed ['arrow:right']), actions False, unsafe [], citation None,
                        contradictions []
Tokens                  in 4533, out 1292, 28.37 s

culane_test__d100_05252026_0512_00450 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        building inscription and the divided-road traffic arrangement. My car is in the
                        rightmost visible through lane of a lit urban road at night; the total lane count and
                        the next intersection layout are not clear enough to establish. (lanes None, mine
                        None, insufficient)
Step 2  Left            A broken white line, with a visible dash and gap, separates my lane from another same-
                        direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right side of my lane, with a paved roadside
                        strip beyond it and a raised roadside edge farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider establishes another same-direction lane to the left,
                        and the right edge line places my car in the rightmost through lane; darkness prevents
                        a reliable total count and therefore a numeric index from the left. | roles: The
                        broken white divider fits a same-direction lane line, and the solid white line beside
                        the roadside strip fits a roadway edge line. | markings: No readable arrow, word,
                        symbol, waiting area, or transverse marking is visible in my lane. | unseen: No
                        numeric lane count, distant lane-use marking, or intersection layout has been inferred
                        from the dark and distant pavement. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a broken white same-direction
                        lane divider permits crossing to change lanes when safe.
Step 5  Rule            right_boundary: A solid white roadway edge line generally prohibits crossing into the
                        roadside strip during ordinary driving.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid white roadway edge line prohibits an ordinary move
                        across it into the roadside strip.
Step 6  go_straight     not_determined: The lane end and any movement-controlling markings there are too
                        distant and dark to read.
Step 6  turn_left       not_determined: The lane end and any movement-controlling markings there are too
                        distant and dark to read.
Step 6  turn_right      not_determined: The lane end and any movement-controlling markings there are too
                        distant and dark to read.
Step 6  u_turn          not_determined: The lane end and any movement-controlling markings there are too
                        distant and dark to read.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         Consistent: boundary rules determine only lateral crossing, intersection movements
                        remain undecided because the lane end is not readable, and no waiting area is
                        reported.
Advice                  Stay inside the right edge line; change left only after checking surrounding traffic.
                        Read the upcoming lane arrows and intersection controls before choosing a turning
                        lane, since neither the permitted intersection movements nor a stopping location can
                        be established here.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1147, 24.66 s

culane_test__d100_05252026_0512_01020 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be Russia, with traffic keeping right, although the country cannot be
                        established confidently from this nighttime image. My car is on a multilane urban
                        road, apparently in the second lane from the left; darkness prevents a reliable count
                        of all same-direction lanes or identification of the next intersection. (lanes None,
                        mine 2, partial)
Step 2  Left            A white longitudinal marking separates my lane from a same-direction lane containing a
                        car on the left; only a limited stretch is illuminated, so its solid or broken pattern
                        is uncertain, and no curb is visible along this boundary.
                        white none, curb no, lane_line, evidence partial
Step 2  Right           White elongated dashes with dark gaps separate my lane from another same-direction
                        lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A same-direction lane is visible on each side, consistent with my car
                        apparently occupying the second lane from the left; the total lane count remains
                        uncertain. | roles: The white separators fit lane-line roles; the left separator's
                        pattern cannot be established reliably. | markings: No arrows, words, symbols,
                        transverse lines, or waiting areas can be identified in my lane. | unseen: The country
                        is tentative, the total lane count is unknown, and neither the left-line pattern nor
                        markings at the unseen lane end are inferred. | result: consistent
Step 5  Rule            left_boundary: Under the presumed Russian rules, a broken lane separator may be
                        crossed when safe but a solid lane separator may not, so the unresolved pattern leaves
                        crossing permission uncertain.
Step 5  Rule            right_boundary: Under the presumed Russian rules, a broken white lane separator
                        permits changing lanes across it when safe.
Step 6  change_left     not_determined (WRONG, label allowed): The left lane separator's pattern is not
                        sufficiently visible to determine crossing permission.
Step 6  change_right    allowed (correct): The visible broken white lane separator permits crossing when safe.
Step 6  go_straight     not_determined: The lane end is not visible well enough to determine whether a
                        movement arrow governs it.
Step 6  turn_left       not_determined: The lane end is not visible well enough to determine whether a
                        movement arrow or prohibition governs it.
Step 6  turn_right      not_determined: The lane end is not visible well enough to determine whether a
                        movement arrow or prohibition governs it.
Step 6  u_turn          not_determined: The lane end is not visible well enough to determine whether an arrow
                        or prohibited-movement marking governs it.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is identifiable in view.
Step 7  Reflect         consistent
Advice                  A rightward lane change is permitted by the visible dashed separator, subject to a
                        safe gap; do not cross the left separator until its pattern is clear. Stay in your
                        lane and reassess turn guidance and any stopping requirement when the road ahead is
                        better illuminated.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 964, 17.03 s

culane_test__d100_05252026_0512_01350 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This is likely Russia, with traffic keeping right, although the country cannot be
                        confirmed from the indistinct roadside lettering and road layout. My car is in the
                        rightmost through lane of a divided urban road at night; the total lane count and the
                        next intersection are not clearly visible. (lanes None, mine None, insufficient)
Step 2  Left            A broken white line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with a narrow paved margin
                        and a raised roadside curb farther to its right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane line establishes another same-direction lane to my left, and
                        the right edge line places my lane at the right edge of the carriageway; darkness
                        prevents a reliable total lane count or numerical lane index. | roles: The broken
                        white line fits a same-direction lane separator, and the continuous white line
                        alongside the roadside margin fits an edge line. | markings: No readable arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane. | unseen: No
                        distant intersection layout or lane-use direction is inferred; the curb beyond the
                        right margin is not treated as the immediate lane boundary. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Russian rules, a broken white lane separator may be
                        crossed for a lane change when safe.
Step 5  Rule            right_boundary: Under the inferred Russian rules, a solid roadway edge line may be
                        crossed to stop on the shoulder where stopping is permitted, but does not authorize
                        driving along the shoulder.
Step 6  change_left     allowed (correct): The broken white lane separator permits crossing into the adjacent
                        lane when safe.
Step 6  change_right    allowed (WRONG, label prohibited): The edge-line exception permits crossing onto the
                        roadside margin for a lawful stop, not for continued shoulder travel.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: rightward crossing is allowed only under the edge-line stopping exception,
                        and no intersection movement is decided from absent lane-use markings.
Advice                  Continue within the lane; a left lane change requires checking surrounding traffic,
                        while crossing the right edge is not permission to travel on the shoulder. The next
                        junction and its movement markings are not readable, so reassess turn lanes and
                        stopping requirements as they become visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 4533, out 1134, 23.41 s

culane_test__d193_06042058_0527_02610 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears most likely to be China, with traffic keeping right, suggested by the
                        blue rear plate and road layout, though the country is uncertain. My car is in the
                        right-hand lane of a two-lane divided carriageway at night; the road continues ahead
                        with no visible intersection or lane ending. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, tinted by the yellow lighting, shows distinct dashes and gaps;
                        another same-direction lane lies beyond it, with a concrete median farther left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line, tinted by the lighting, borders a narrow paved roadside
                        strip; no raised curb is clearly visible at the line.
                        white solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego position 2 agree with a lane divider on the
                        left and a roadway edge on the right. | roles: The broken white divider and continuous
                        white edge marking fit their observed roles. | markings: No arrows, words, symbols,
                        transverse lines or waiting areas are discernible in my lane. | unseen: The country is
                        inferred rather than established; the right roadside physical edge and distant road
                        details are not fully resolved. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        crossing to change lanes when safe.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, the solid roadway edge line must not
                        ordinarily be crossed to drive onto the roadside strip.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (correct): The solid roadway edge line prohibits an ordinary move onto the
                        roadside strip.
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
Step 7  Reflect         consistent: boundary decisions follow the inferred regional rules, and no intersection
                        movement is decided from the roadway boundaries.
Advice                  Remain within the right-hand lane; move left across the broken divider only after
                        checking traffic, including the vehicle ahead-left. Do not cross the solid right edge
                        line; no intersection movement guidance or stopping point is visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 893, 14.74 s

culane_test__d193_06042058_0527_03240 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears most likely to be China, with traffic keeping right, although the country
                        cannot be confirmed from the small, unreadable signs. My car is in the right lane of a
                        two-lane carriageway at night, with the road continuing ahead and no visible
                        intersection or lane ending. (lanes 2, mine 2, full)
Step 2  Left            A broken white line, with a visible long dash and gaps, separates my lane from the
                        same-direction lane occupied by the white vehicle; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line, tinted by the street lighting, borders my lane on the right,
                        with a paved roadside strip and delineator posts beyond rather than a curb forming the
                        lane boundary.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and my position as lane 2 agree with a lane divider
                        on the left and a roadway edge on the right. | roles: The broken white divider fits a
                        same-direction lane line, and the continuous white roadside line fits an edge line. |
                        markings: No arrows, words, symbols, transverse markings or waiting areas are
                        discernible in my lane. | unseen: The country is tentative, sign text is unreadable,
                        and the distant road is too dark to establish markings at any eventual intersection;
                        none have been invented. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        crossing to change lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, the solid white roadway edge
                        restricts crossing onto the roadside strip during ordinary driving.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe, but
                        the vehicle alongside must be allowed for.
Step 6  change_right    prohibited (correct): The solid white roadway edge restricts crossing onto the
                        roadside strip.
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
Advice                  Stay within the right edge line; change left only after the white vehicle has cleared
                        and a safe gap exists. No visible markings assign intersection movements or a stopping
                        point, so reassess when an intersection or readable guidance becomes visible.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 907, 16.05 s

culane_test__d193_06051114_0632_02790 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese writing, blue vehicle plates
                        and road layout; traffic keeps right. My car is approaching a signalized intersection
                        in the second lane from the left, with the total number of same-direction lanes
                        uncertain because the outer-right markings are faint. (lanes None, mine 2, partial)
Step 2  Left            A worn white broken line separates my lane from another lane on the left; dash
                        segments and intervening gaps are visible, with no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A faded white broken line runs along my lane's right side, with another same-direction
                        lane beyond it and no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A worn white arrow ahead of the car has a forward-pointing head
                        and a straight stem, with no visible turning branch.
Step 4  Cross-check     position: A lane lies to the left and another to the right, consistent with the ego
                        lane being second from the left; the total lane count remains uncertain. | roles:
                        White broken boundaries fit separators between lanes carrying traffic in the same
                        direction. | markings: The straight arrow agrees with a through lane bounded by
                        ordinary lane separators; the arrow in the neighboring left lane is not an ego-lane
                        marking. | unseen: No stop line or crosswalk can be confidently identified across my
                        lane, and the faint outer-right markings have not been used to assert a total lane
                        count. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane separator permits crossing to
                        change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A broken white lane separator permits a safe lane change to the right.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires traffic leaving this lane at
                        the intersection to proceed straight rather than turn left, turn right or make a
                        U-turn.
Step 6  change_left     allowed (WRONG, label prohibited): The broken white lane separator permits crossing
                        when safe.
Step 6  change_right    allowed (WRONG, label prohibited): The broken white lane separator permits crossing
                        when safe.
Step 6  go_straight     allowed (correct): The straight-only arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane to go straight, obeying the traffic signal and stopping at the
                        stop line when required once it is identifiable. For a turn, change safely into an
                        appropriately marked lane before the intersection; do not turn directly from this
                        straight-only lane.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe ['change_left', 'change_right'], citation None,
                        contradictions []
Tokens                  in 4533, out 1241, 26.56 s

culane_test__d193_06051114_0632_04320 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese-language exit sign and blue
                        vehicle plates; traffic keeps right. My car is in the left lane of a two-lane urban
                        carriageway, with opposing traffic beyond the central fence and no clear intersection
                        visible ahead. (lanes 2, mine 1, full)
Step 2  Left            A continuous white solid line follows the central metal fence on the left, with
                        opposing traffic beyond the fence.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A worn white broken line separates my lane from the lane occupied by the black sedan;
                        a dash and intervening gap are visible, with no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood; the lower portion of the arrow is hidden by the hood.
Step 4  Cross-check     position: Two same-direction lanes and position 1 agree with the fenced roadway edge
                        on the left and a lane divider on the right. | roles: The white solid line borders the
                        physically separated carriageway rather than directly separating opposing lanes; the
                        broken white line divides same-direction lanes. | markings: The visible forward
                        arrowhead agrees with the continuing lane, but the hidden lower portion prevents
                        completely checking for additional branches. | unseen: No additional arrowhead,
                        transverse line, or waiting area is asserted; the arrow's lower portion and distant
                        lane end are not clearly visible. | result: consistent
Step 5  Rule            left_boundary: In mainland China, the fenced roadway edge cannot be crossed to leave
                        this lane.
Step 5  Rule            right_boundary: A broken white same-direction lane divider permits changing lanes
                        across it when safe.
Step 5  Rule            arrow:straight: A forward lane-use arrow permits proceeding straight, while any
                        additional permitted movements depend on whether other arrow branches are present.
Step 6  change_left     prohibited (correct): The physical central fence prohibits leaving the lane across its
                        left boundary.
Step 6  change_right    allowed (correct): The broken white lane divider permits a right lane change when
                        safe.
Step 6  go_straight     allowed: The visible forward arrowhead permits straight travel.
Step 6  turn_left       not_determined: The hood hides the lower arrow portion, so an additional left-turn
                        branch cannot be ruled out.
Step 6  turn_right      not_determined: The hood hides the lower arrow portion, so an additional right-turn
                        branch cannot be ruled out.
Step 6  u_turn          not_determined: The incomplete arrow prevents establishing whether a U-turn branch is
                        present.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the visible forward head supports straight travel, but the incomplete
                        arrow does not justify deciding other movements; boundary decisions apply only to
                        crossing their respective sides.
Advice                  Continue straight in this lane; a right lane change is permitted only after checking
                        the nearby sedan and other traffic. Do not cross the central fence, and confirm
                        complete lane arrows and intersection controls before attempting a turn.
Score                   lane False, boundaries {'left': False, 'right': True}, markings False (added
                        ['arrow:straight'], missed []), actions True, unsafe [], citation None, contradictions
                        []
Tokens                  in 4533, out 1087, 22.1 s

culane_test__d193_06051123_0635_00450 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping to the right, based on the road layout,
                        markings and streetscape. My car is in the leftmost of two apparent motor-vehicle
                        lanes approaching an urban intersection and a broad pedestrian crossing. (lanes 2,
                        mine 1, partial)
Step 2  Left            A single continuous yellow line runs along the left of my lane toward the stop line,
                        with opposing-direction roadway beyond and no curb along it.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single continuous white line runs from beside the hood to the stop line, separating
                        my lane from another apparent motor-vehicle lane; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        line:stop_line (full): A transverse solid white stop line crosses my lane immediately
                        before the pedestrian crossing.; line:crosswalk (full): Broad white zebra-crossing
                        stripes extend across my lane beyond the stop line.
Step 4  Cross-check     position: The yellow center line makes my lane the leftmost of its direction, and the
                        white lane line indicates another same-direction lane on the right; the function of
                        the farther-right paved strip is less certain. | roles: The solid yellow center line
                        and solid white same-direction lane divider fit their assigned roles. | markings: The
                        stop line precedes the crosswalk, and neither conflicts with the boundaries; no
                        directional arrow is visible in my lane. | unseen: Paint beneath the hood is hidden,
                        and the exact classification of the farther-right strip cannot be confirmed; no hidden
                        arrow or marking is inferred. | result: consistent
Step 5  Rule            left_boundary: Under Chinese road-marking rules, a solid yellow center line prohibits
                        crossing into the opposing side.
Step 5  Rule            right_boundary: A solid white lane-dividing line prohibits changing lanes across it on
                        this approach.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before this line.
Step 5  Rule            line:crosswalk: The zebra crossing requires yielding to pedestrians and keeping the
                        crossing unobstructed.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white lane divider prohibits crossing the
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
Step 7  Reflect         Consistent: both boundary-crossing actions are prohibited, while intersection
                        movements are not assigned permission or prohibition without a visible governing
                        directional marking.
Advice                  Stay between the solid boundaries on this approach; the visible markings do not
                        establish which intersection movements this lane serves. Confirm applicable signs and
                        controls, yield to pedestrians, and stop before the stop line whenever stopping is
                        required.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions False, unsafe [], citation
                        None, contradictions []
Tokens                  in 4533, out 1177, 21.24 s

culane_test__d193_06051123_0635_00900 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, inferred from the road
                        markings, streetscape and visible Chinese-style signage. My car is in the single
                        general-traffic lane in its direction on an undivided urban road bending gently left;
                        no intersection or lane ending is clearly visible. (lanes 1, mine 1, full)
Step 2  Left            A single continuous yellow line borders my lane on the left, with opposing-direction
                        roadway beyond it and no curb.
                        yellow solid, curb no, center_line, evidence full
Step 2  Right           A single continuous white line borders my lane on the right, with a paved roadside
                        strip beyond it and a raised sidewalk curb farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line on the left and white roadway edge line on the right
                        agree with one general-traffic lane in my direction, indexed 1. | roles: The solid
                        yellow line separates opposing directions, while the solid white line separates the
                        traffic lane from the roadside strip. | markings: No arrows, words, symbols, waiting
                        areas or transverse markings are visible in my lane. | unseen: No lane-use direction
                        or distant intersection layout is inferred; the precise use of the roadside strip is
                        not established. | result: consistent
Step 5  Rule            left_boundary: Under the inferred mainland Chinese rules, a solid yellow center line
                        prohibits crossing into the opposing side for a lane change or overtaking.
Step 5  Rule            right_boundary: Under the inferred mainland Chinese rules, the solid white roadway
                        edge line prohibits ordinary crossing into the roadside strip.
Step 6  change_left     prohibited (correct): The solid yellow center line prohibits crossing the left
                        boundary.
Step 6  change_right    prohibited (correct): The solid white roadway edge line prohibits ordinary crossing of
                        the right boundary.
Step 6  go_straight     not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_left       not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  turn_right      not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action.
Step 6  u_turn          not_applicable: No visible lane-use arrow or prohibited-movement marking governs this
                        action; the center line governs boundary crossing instead.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary restrictions govern only the corresponding crossing actions, and
                        no intersection movement is decided without a visible governing marking.
Advice                  Stay between the yellow center line and white edge line, without crossing either in
                        this stretch. Follow the road's bend cautiously; no visible arrow establishes a turn
                        lane or a place to stop.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 882, 13.45 s

culane_test__d193_06051123_0635_00990 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, based on the Chinese writing and road layout, with traffic
                        keeping right. My car is in the leftmost of two apparent same-direction lanes on an
                        urban road continuing ahead; no intersection or lane ending is clearly visible. (lanes
                        2, mine 1, full)
Step 2  Left            A single yellow broken line, with a visible dash and gap, runs along my lane's left
                        side; opposing-direction roadway lies beyond it, with no curb at this boundary.
                        yellow dashed, curb no, center_line, evidence full
Step 2  Right           A white broken line, showing separated painted segments, runs along my lane's right
                        side; another paved traffic lane lies beyond it, with the roadside curb farther right.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The yellow center line places my lane leftmost in its direction, and the
                        white lane line separates it from the second lane on the right. | roles: The yellow
                        broken center line and white broken same-direction lane line fit the inferred Chinese
                        road layout. | markings: No visible arrows, words, symbols, transverse lines or
                        waiting areas conflict with the boundary interpretation. | unseen: No movement
                        restrictions or markings beyond the readable stretch have been inferred; the next
                        intersection is not visible. | result: consistent
Step 5  Rule            left_boundary: In China, a broken yellow center line may be crossed for overtaking or
                        avoidance when lawful and safe, without obstructing opposing traffic.
Step 5  Rule            right_boundary: A broken white lane line permits changing into the adjacent same-
                        direction lane when safe.
Step 6  change_left     allowed (correct): The broken yellow center line permits conditional crossing, but
                        this enters opposing-direction roadway rather than another same-direction lane.
Step 6  change_right    allowed (correct): The broken white lane line permits a safe change into the lane on
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
Step 7  Reflect         consistent: boundary-crossing permissions are conditional, and no intersection
                        movement is decided from boundaries or absent arrows.
Advice                  Stay right of the yellow center line for normal travel; a rightward lane change is
                        permitted after checking traffic. No visible arrows assign intersection movements, so
                        reassess lane choice and any stopping requirements as the next junction comes into
                        view.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1040, 19.74 s

culane_test__d193_06051123_0635_01980 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese writing and
                        roadway layout. The car is in the middle of three same-direction lanes on a broad
                        urban road approaching an intersection. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line separates my lane from another same-direction lane on the
                        left; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line separates my lane from another same-direction lane on the
                        right; the roadside curb is beyond that lane, not at my lane boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead.
Step 4  Cross-check     position: Three same-direction lanes and ego lane index 2 agree with having a same-
                        direction lane across each boundary. | roles: The white solid lines fit lane
                        separators on an intersection approach; the yellow center lines are farther left and
                        do not bound my lane. | markings: The straight-only arrow agrees with a middle through
                        lane; arrows in neighboring lanes do not govern my lane. | unseen: No stop line,
                        crosswalk, or waiting area can be identified in my lane; distant pavement details are
                        too small to resolve. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes to the left.
Step 5  Rule            right_boundary: In China, a solid white lane separator prohibits crossing it to change
                        lanes to the right.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 6  change_left     prohibited (WRONG, label allowed): The solid white left lane separator prohibits
                        crossing into the adjacent lane.
Step 6  change_right    prohibited (WRONG, label allowed): The solid white right lane separator prohibits
                        crossing into the adjacent lane.
Step 6  go_straight     allowed (correct): The lane's straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Continue straight from this lane, subject to intersection controls and traffic
                        conditions. For a turn, select an appropriately marked lane before the solid
                        separators begin; do not cross either solid line here.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 938, 15.66 s

culane_test__d193_06051123_0635_02160 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese storefront
                        lettering and road layout. My car is in the rightmost approach lane of a broad urban
                        signal-controlled intersection; the full set of same-direction lanes is not clearly
                        separable at the left edge of the photo. (lanes None, mine None, insufficient)
Step 2  Left            A single solid white line separates my lane from another approach lane on the left and
                        extends toward the intersection.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A solid white line curves along the right side of my lane, with white diagonal
                        channelizing stripes beyond it and a raised landscaped curb farther right.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (full): A white arrow has a single head pointing right, with its stem
                        bending right from the forward direction.; line:stop_line (full): A white transverse
                        stop line crosses the lane just before the pedestrian crossing.; line:crosswalk
                        (full): White zebra-crossing stripes extend across the approach ahead of the stop
                        line.
Step 4  Cross-check     position: The left lane line confirms another same-direction lane on my left, while
                        the right edge line places me in the rightmost lane; the total count and numerical
                        lane index remain uncertain. | roles: The solid white left divider fits an approach
                        lane line, and the solid white right line fits the roadway edge beside the channelized
                        area. | markings: The right-only arrow is consistent with the rightmost approach lane;
                        the stop line and crosswalk do not conflict with that movement. The diagonal stripes
                        are outside my lane. | unseen: No total lane count or numerical lane index is inferred
                        from the cropped left side, and the curb beyond the striped area is not treated as the
                        immediate lane boundary. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white approach lane divider prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: The roadway edge beside the channelizing stripes does not permit an
                        ordinary lane change into the marked exclusion area.
Step 5  Rule            arrow:right: The right-only lane-use arrow permits a right turn and excludes straight
                        travel, left turns and U-turns from this lane.
Step 5  Rule            line:stop_line: When required to stop, the vehicle must stop before this line.
Step 5  Rule            line:crosswalk: The pedestrian crossing requires yielding to pedestrians and keeping
                        the crossing clear.
Step 6  change_left     prohibited (correct): The solid white lane divider prohibits crossing to the lane on
                        the left.
Step 6  change_right    prohibited (correct): The right edge borders a channelized exclusion area, not a lane
                        available to enter.
Step 6  go_straight     prohibited (correct): The right-only arrow excludes straight travel.
Step 6  turn_left       prohibited (correct): The right-only arrow excludes a left turn.
Step 6  turn_right      allowed (correct): The right-only arrow permits a right turn.
Step 6  u_turn          prohibited (correct): The right-only arrow excludes a U-turn.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Use this lane only to turn right; do not cross the solid left divider or enter the
                        striped area on the right. Obey applicable signals, stop before the stop line when
                        required, and yield to pedestrians and other conflicting traffic.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4533, out 1219, 21.06 s

culane_test__d193_06051123_0635_03690 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese storefront
                        lettering and road layout. The car is in the middle of three same-direction approach
                        lanes at a signalized urban intersection. (lanes 3, mine 2, full)
Step 2  Left            A solid white longitudinal boundary, with a closely parallel pale stripe visible
                        alongside it, separates my lane from the left-turn lane; no curb lies between the
                        lanes.
                        white double_solid, curb no, lane_line, evidence full
Step 2  Right           A solid white longitudinal boundary with a closely parallel white stripe separates my
                        lane from the lane on its right; there is no curb at this boundary.
                        white double_solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead
                        and no branching head.; line:stop_line (full): A transverse white stop line spans my
                        lane immediately before the pedestrian crossing.; line:crosswalk (full): White zebra-
                        crossing bars cross the approach immediately beyond the stop line.
Step 4  Cross-check     position: The middle position among three approach lanes agrees with having a same-
                        direction lane beyond each white boundary. | roles: The white solid boundaries fit
                        same-direction lane dividers on an intersection approach. | markings: The straight-
                        only arrow agrees with this through lane; the left-turn arrow visible to the left
                        belongs to the adjacent lane, not mine. | unseen: No hidden continuation, waiting
                        area, or additional arrow head has been inferred. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes on this approach.
Step 5  Rule            right_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes on this approach.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 5  Rule            line:stop_line: When required to stop by the signal or traffic control, stop before
                        this line.
Step 5  Rule            line:crosswalk: Keep the pedestrian crossing clear and yield to pedestrians as
                        required.
Step 6  change_left     prohibited (correct): The solid white left lane divider prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane divider prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The straight-only arrow permits the straight movement.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for straight travel and do not cross either solid divider to
                        change lanes here. Obey the intersection signal, stop before the stop line when
                        required, and keep the crosswalk clear.
Score                   lane False, boundaries {'left': False, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4533, out 1355, 25.01 s

culane_test__d193_06051411_0691_03960 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be an urban road in mainland China, inferred from the simplified-
                        Chinese shop signs and vehicles keeping to the right of the central fence. My car is
                        in the leftmost of two apparent same-direction lanes; the road bends gently left
                        ahead, with parked vehicles along the right side and no visible intersection. (lanes
                        2, mine 1, partial)
Step 2  Left            A continuous pale white line runs beside the central metal fence, with yellow paint
                        farther toward the fence; opposing traffic is visible beyond the physical divider.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A faint white broken line appears to separate my lane from the roadway to the right,
                        but worn paint makes the dash-and-gap sequence difficult to trace; parked vehicles lie
                        farther right.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median-side physical edge places my car in the leftmost lane; the faint
                        divider to the right suggests a second same-direction lane, although its delineation
                        is uncertain. | roles: The white solid line alongside the median fits an edge line,
                        while the faint white broken marking fits a same-direction lane divider. | markings:
                        No readable arrows, words, symbols, waiting areas or transverse markings are visible
                        in my lane. | unseen: The right boundary's broken pattern and therefore the exact lane
                        count remain uncertain because the paint is faint; no unseen intersection markings are
                        assumed. | result: consistent
Step 5  Rule            left_boundary: Under the inferred mainland Chinese rules, the central physical divider
                        must not be crossed, so leaving the lane to the left is prohibited.
Step 5  Rule            right_boundary: A confirmed white broken lane divider permits changing lanes when
                        safe, but the worn marking here does not establish that permission confidently.
Step 6  change_left     prohibited (correct): The central physical divider prohibits crossing to the left.
Step 6  change_right    not_determined (WRONG, label allowed): The worn right boundary does not establish its
                        crossable pattern confidently.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Follow the road beside the median without crossing the fence-side boundary. Confirm
                        the worn right-hand lane marking and check for traffic and parked-vehicle movements
                        before changing right; no visible markings establish turn permissions or a stopping
                        point.
Score                   lane False, boundaries {'left': False, 'right': True}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 922, 18.27 s

culane_test__d193_06051603_0727_01080 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        signage and traffic arrangement. My car is on a single-lane right-hand branch of an
                        urban divided road, with a hatched separation area to the left and a concrete barrier
                        to the right; no intersection is visible ahead. (lanes 1, mine 1, full)
Step 2  Left            A continuous white line borders my lane on the left, with white diagonal hatching
                        beyond it and delineator posts farther ahead; additional same-direction roadway lies
                        beyond the separation area.
                        white solid, curb no, edge_line, evidence full
Step 2  Right           A concrete barrier forms the right side of my lane, with a narrow dirty paved margin
                        at its base and no distinct painted boundary line visible.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The branch has one lane, bounded by a separation-area edge on the left and a
                        physical roadway edge on the right; the adjacent roadway beyond the hatching is not
                        another lane within this branch. | roles: The solid white line beside the hatched
                        separation area fits an edge-line role, and the concrete barrier forms the right
                        roadway edge. | markings: No arrows, words, symbols, or transverse markings are
                        visible within my lane; the diagonal hatching lies outside its left boundary. |
                        unseen: No direction arrow or downstream intersection restriction has been inferred
                        from the branch's alignment. | result: consistent
Step 5  Rule            left_boundary: In mainland China, the solid boundary of a traffic-separation area must
                        not be crossed to drive into or across the hatched area.
Step 5  Rule            right_boundary: The concrete roadway barrier is a physical boundary that vehicles must
                        not cross.
Step 6  change_left     prohibited (correct): The solid white boundary beside the hatched separation area
                        prohibits crossing to the left.
Step 6  change_right    prohibited (correct): The concrete barrier prohibits leaving the lane to the right.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: the boundaries prohibit lateral departures, while no movement permission
                        or restriction is inferred from the road's alignment alone.
Advice                  Remain within this single-lane branch; do not cross the hatched separation area or
                        approach the right barrier. Follow the signs ahead for routing, since no lane-use
                        arrows or stopping point are visible here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 936, 18.56 s

culane_test__d193_06051603_0727_01620 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           Likely mainland China, inferred from the Chinese building lettering and road
                        environment, with traffic keeping right. My car is on a single-lane elevated ramp
                        curving left between concrete barriers; no intersection or lane ending is visible.
                        (lanes 1, mine 1, full)
Step 2  Left            A narrow, continuous pale white edge stripe follows the concrete barrier on the left;
                        the paint is dirty and its color is somewhat uncertain, with another elevated roadway
                        beyond the barrier.
                        white solid, curb yes, edge_line, evidence partial
Step 2  Right           A worn solid white stripe follows the base of the concrete barrier on the right, with
                        no adjacent traffic lane beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane, bounded by roadway edges and concrete barriers on both sides,
                        agrees with my lane being the leftmost and rightmost lane. | roles: The continuous
                        pale edge stripes and barriers fit roadway-edge boundaries rather than lane dividers.
                        | markings: No arrows, text, symbols, transverse lines or waiting areas are visible in
                        my lane. | unseen: The left stripe's color is uncertain because of dirt and lighting;
                        the ramp beyond the bend is not visible. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese road rules, the roadway edge and concrete
                        barrier do not permit leaving the lane to the left.
Step 5  Rule            right_boundary: Under the inferred Chinese road rules, the roadway edge and concrete
                        barrier do not permit leaving the lane to the right.
Step 6  change_left     prohibited (correct): The left roadway edge and concrete barrier prohibit moving out
                        of the lane on that side.
Step 6  change_right    prohibited (correct): The right roadway edge and concrete barrier prohibit moving out
                        of the lane on that side.
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
Step 7  Reflect         Consistent: both lateral departures are prohibited by the physical roadway boundaries,
                        while no visible markings govern intersection movements or entry to a waiting area.
Advice                  Stay within the ramp's barriers and follow its leftward curve, adjusting speed for the
                        bend and the vehicle ahead. The chevron boards indicate the curve; no intersection
                        movement or stopping point is shown.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 878, 14.91 s

culane_test__d193_06051734_0757_00000 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           Likely China, with traffic keeping right, suggested by the expressway signage and
                        median anti-glare screens, though the country is not certain. My car is in the middle
                        of three lanes on a divided expressway continuing straight, with no intersection or
                        lane ending visible. (lanes 3, mine 2, full)
Step 2  Left            A white broken line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line with visible long dashes and gaps separates my lane from another
                        same-direction lane on the right; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and ego position 2 agree with a same-direction lane beyond each
                        boundary. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No arrows, words, symbols, transverse lines or marked areas are
                        visible in my lane. | unseen: No hidden markings or intersection movements have been
                        inferred; the country identification remains tentative. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        crossing to change lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        crossing to change lanes when safe and without interfering with other traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent left lane.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe change into the
                        adjacent right lane.
Step 6  go_straight     not_applicable: No marking governs this action.
Step 6  turn_left       not_applicable: No marking governs this action.
Step 6  turn_right      not_applicable: No marking governs this action.
Step 6  u_turn          not_applicable: No marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent
Advice                  Continue along the expressway in your lane; either adjacent lane can be entered across
                        the broken divider after checking traffic and signaling. No junction, turn guidance or
                        stopping line is visible, so these markings do not establish permission for turns or a
                        U-turn.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 789, 11.37 s

culane_test__d193_06051734_0757_02430 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be a divided expressway in China, with traffic keeping right; the
                        highway layout, green roadside screening and distant green signs suggest China, though
                        the country is uncertain. My car is in the middle of three same-direction lanes, with
                        open highway ahead and no visible intersection or lane ending. (lanes 3, mine 2, full)
Step 2  Left            A white broken line, with visible long dashes and intervening gaps, separates my lane
                        from another same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, visible ahead as dashes separated by gaps, separates my lane from
                        another same-direction lane on the right; its nearest portion is hidden by the hood,
                        and no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three lanes and a middle-lane position agree with a same-direction lane line
                        on each side. | roles: Both white broken boundaries fit ordinary same-direction lane
                        dividers. | markings: No guidance arrows, words, symbols, waiting areas or transverse
                        traffic markings are visible in my lane; the transverse pavement seam is not a painted
                        traffic marking. | unseen: No hidden lane-use marking or junction is inferred; the
                        visible stretches establish both boundary patterns despite foreground hood occlusion.
                        | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        crossing into the adjacent same-direction lane when safe.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, a broken white lane divider permits
                        crossing into the adjacent same-direction lane when safe.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change to the
                        right.
Step 6  go_straight     not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_left       not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  turn_right      not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  u_turn          not_applicable: No lane-use arrow or prohibited-movement marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: both lane changes follow the broken-divider rules, and the remaining
                        actions are not applicable to the visible markings rather than permissions to turn on
                        the expressway.
Advice                  Continue along the expressway; neither visible boundary requires a lane change, and
                        either may be crossed when safe after checking mirrors and blind spots. No turn
                        facility or stopping line is visible; use a designated exit for leaving the
                        expressway.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 941, 15.11 s

culane_test__d193_06051734_0757_04050 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, where traffic keeps right; the green-and-white bend
                        chevrons and distant blue road sign support that inference, though the country is not
                        certain. My car is in the only lane of a single-lane ramp curving right toward an
                        overpass; no intersection or ramp end is visible. (lanes 1, mine 1, full)
Step 2  Left            A continuous solid white line runs along the left of my lane, with a narrow paved
                        margin and a raised concrete edge supporting a metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A continuous solid white line curves right along my lane, with a paved shoulder and a
                        raised concrete edge supporting a metal guardrail beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: One lane, with my lane first from the left, agrees with roadway edge lines
                        on both sides and no adjacent traffic lanes. | roles: Both white solid lines follow
                        the ramp margins, consistent with edge lines rather than lane dividers or a center
                        line. | markings: No arrows, words, symbols, transverse lines or waiting areas are
                        visible within my lane. | unseen: No markings are inferred beyond the bend; the ramp
                        end and any later movement controls are not visible. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, the solid white roadway edge
                        restricts crossing onto the left margin, and the guardrail is not a traversable lane
                        boundary.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, the solid white roadway edge
                        restricts ordinary driving onto the right shoulder, and the guardrail prevents travel
                        beyond the roadway.
Step 6  change_left     prohibited (correct): The solid white edge line restricts crossing onto the left
                        margin.
Step 6  change_right    prohibited (correct): The solid white edge line restricts crossing onto the right
                        shoulder.
Step 6  go_straight     not_determined: The ramp end is hidden, so any marking governing the movement there
                        cannot be assessed.
Step 6  turn_left       not_determined: The ramp end is hidden, so any marking governing the movement there
                        cannot be assessed.
Step 6  turn_right      not_determined: The ramp end is hidden, so any marking governing the movement there
                        cannot be assessed.
Step 6  u_turn          not_determined: The ramp end is hidden, so any marking governing the movement there
                        cannot be assessed.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Follow the ramp's rightward curve between the solid white edge lines; do not use the
                        margins or shoulder as another lane. Slow for the bend and reassess movement choices
                        when the ramp end becomes visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 890, 14.64 s

culane_test__d193_06060642_0768_00360 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, suggested by the blue vehicle
                        plates and road layout. My car is in the rightmost of two same-direction lanes on a
                        landscaped urban road; no intersection or lane ending is clearly visible ahead. (lanes
                        2, mine 2, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white edge marking runs beside a raised curb and planted strip; some of the
                        more distant marking is difficult to distinguish.
                        white dashed, curb yes, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and position 2 agree with a lane divider on the
                        left and a curbed roadway edge on the right. | roles: The broken white left line fits
                        a same-direction lane divider; the right white marking follows the curbed roadway
                        edge. | markings: No readable arrows, words, symbols, transverse lines or waiting
                        areas are visible in my lane. | unseen: No distant intersection layout or hidden
                        guidance markings have been assumed; the distant right edge is less clear. | result:
                        consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a broken white lane divider may be
                        crossed to change lanes when safe.
Step 5  Rule            right_boundary: The broken edge paint does not authorize driving over the raised curb
                        into the planted strip.
Step 6  change_left     allowed (correct): The broken white lane divider permits crossing when safe.
Step 6  change_right    prohibited (correct): The raised curb physically bounds the roadway and must not be
                        crossed into the planted strip.
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
Advice                  Continue within the curbed roadway; changing left across the broken divider is
                        permitted when safe, but do not move right over the curb. No visible markings
                        establish turn permissions or a stopping point, so reassess as the next junction
                        becomes visible.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1027, 19.34 s

culane_test__d193_06060642_0768_00900 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, suggested by the blue
                        license plates and opposing traffic to the left of the yellow center markings. My car
                        is in the rightmost of two same-direction lanes on an urban road curving gently right
                        toward a distant overpass; no intersection is clearly visible. (lanes 2, mine 2, full)
Step 2  Left            A white broken line, with a visible dash and intervening gaps, separates my lane from
                        another same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line follows the right edge of my lane beside a raised curb,
                        with planted landscaping and a separate paved area beyond.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Two same-direction lanes and ego lane index 2 agree with a lane divider on
                        the left and a roadway edge on the right. | roles: The white broken left line fits a
                        same-direction lane divider; the solid white right line beside a curb fits a roadway
                        edge. | markings: No guidance arrows, words, symbols, transverse lines, or waiting
                        areas are visible in my lane. | unseen: No unseen marking is inferred; markings at a
                        subsequent intersection cannot be assessed from this view. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a broken white same-direction
                        lane divider permits crossing to change lanes when safe.
Step 5  Rule            right_boundary: The solid roadway edge beside a raised curb is not a permissible lane-
                        change route, so my car must not leave the lane across this boundary.
Step 6  change_left     allowed (correct): The broken white lane divider permits a lane change when safe.
Step 6  change_right    prohibited (correct): The solid roadway edge and raised curb prohibit leaving the lane
                        to the right.
Step 6  go_straight     not_applicable: No visible marking governs this action.
Step 6  turn_left       not_applicable: No visible marking governs this action.
Step 6  turn_right      not_applicable: No visible marking governs this action.
Step 6  u_turn          not_applicable: No visible marking governs this action.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         consistent: boundary decisions follow their respective rules, and no intersection
                        movement permission is inferred from the absence of guidance markings.
Advice                  Follow the lane around the gentle right bend; changing left is permitted only when
                        safe, while crossing the right curb boundary is not. Choose any later turning lane
                        using the markings visible nearer the junction, since this image provides no turning
                        guidance or stop line.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 878, 15.47 s

culane_test__d193_06060642_0768_03060 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese writing and road-sign style,
                        with traffic keeping right. The car is in the rightmost of three same-direction lanes
                        on an urban road approaching a junction, alongside an elevated roadway. (lanes 3, mine
                        3, full)
Step 2  Left            A white broken line, with a visible long dash and gap, separates this lane from the
                        lane occupied by the green bus; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line separates this lane from a narrow paved roadside strip, with a
                        raised sidewalk curb farther to the right rather than directly along the line.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:right (partial): A small white directional arrow ahead appears to bend right;
                        its head and shaft are distant and not clear enough to exclude an additional straight-
                        ahead head.
Step 4  Cross-check     position: Two lanes lie to the left, consistent with a lane line on the left and a
                        roadway edge line on the right. | roles: The broken white left boundary fits a same-
                        direction lane divider; the continuous white right boundary fits the edge of the
                        motor-vehicle carriageway. | markings: The apparent rightward arrow is compatible with
                        the rightmost lane, but its complete set of heads cannot be confirmed from this image.
                        | unseen: The distant arrow is not treated as conclusively right-turn-only, and no
                        stop line or waiting area can be identified ahead. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking conventions, a broken white lane divider
                        permits crossing to change lanes when safe.
Step 5  Rule            right_boundary: The continuous white roadway edge line restricts crossing onto the
                        roadside strip during ordinary driving.
Step 5  Rule            arrow:right: A right-turn lane arrow permits a right turn, but the incomplete reading
                        here does not establish whether another movement is also permitted.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The continuous white edge line restricts crossing into the
                        roadside strip.
Step 6  go_straight     not_determined: The distant arrow cannot be read well enough to determine whether it
                        includes a straight-ahead head.
Step 6  turn_left       not_determined: The distant arrow's complete configuration is not sufficiently clear
                        to determine all movement restrictions.
Step 6  turn_right      allowed: The visible rightward arrowhead indicates a permitted right turn.
Step 6  u_turn          not_determined: The distant arrow's complete configuration is not sufficiently clear
                        to determine all movement restrictions.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent: the rightward head supports turning right, while the incomplete arrow
                        reading leaves the other junction movements undecided.
Advice                  Stay inside the solid right edge line; a left lane change is possible across the
                        broken line if clear, especially checking the bus. Confirm the distant lane arrow
                        before choosing a junction movement, and obey any signals and stop line as they become
                        visible.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:right'], missed []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1115, 22.47 s

culane_test__d193_06060748_0790_02970 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese roadside
                        text and vehicle plates. My car is on a busy multilane divided highway; traffic
                        obscures the distant road, and the cropped view prevents a reliable count of all same-
                        direction lanes or my lane's index. (lanes None, mine None, insufficient)
Step 2  Left            A white broken line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white longitudinal line separates my lane from the lane occupied by the cream
                        minibus; a long segment is visible, but the minibus hides the continuation needed to
                        distinguish a broken line from a solid one confidently; there is no curb at this
                        boundary.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: Same-direction lanes are visible on both sides of my lane, consistent with
                        both boundaries being lane lines; the full lane count and index remain uncertain. |
                        roles: White longitudinal separators fit same-direction lane-line roles; the right
                        boundary's complete pattern is obscured. | markings: No arrows, words, symbols,
                        transverse lines, or waiting areas are visible in my lane. | unseen: The right
                        boundary is visibly continuous over its exposed segment, but its overall solid-versus-
                        broken pattern is not established; no distant intersection markings are inferred. |
                        result: Consistent, with the right boundary's pattern treated as unresolved rather
                        than established as solid.
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A broken white lane divider permits a safe lane change, whereas a
                        solid white lane divider prohibits crossing; the obscured pattern prevents selecting
                        the applicable rule confidently.
Step 6  change_left     allowed (correct): The visible broken white lane divider permits a safe left lane
                        change.
Step 6  change_right    not_determined (WRONG, label allowed): The minibus obscures whether the right divider
                        is solid or broken, leaving crossing permission unresolved.
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
Step 7  Reflect         Consistent: left crossing is permitted by the observed broken divider, right crossing
                        remains undecided because its pattern is obscured, and no unobserved movement markings
                        are used to authorize turns.
Advice                  Maintain a safe following distance in the dense traffic; a left lane change is
                        permitted by the marking only when a safe gap exists. Avoid crossing the right divider
                        until its pattern is clear, and follow any applicable restrictions indicated by the
                        roadside Chinese signs.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1390, 31.99 s

culane_test__d193_06060919_0820_00450 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be an urban street in China, with traffic keeping right, suggested by
                        the Chinese writing, blue vehicle plates and traffic positions. My car is in the
                        single visible through lane of its direction, with oncoming traffic to the left and
                        parked cars along the right; no intersection is clearly visible ahead. (lanes 1, mine
                        1, full)
Step 2  Left            A faded yellow longitudinal marking lies to my left, with opposing traffic beyond it;
                        wear and perspective prevent confidently distinguishing a continuous line from broken
                        segments.
                        yellow solid, curb no, center_line, evidence partial
Step 2  Right           No painted boundary is visible on the right; the raised roadside curb forms the
                        physical edge, with parked cars beside it and the sidewalk beyond.
                        none none, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: A center line on the left and the roadside edge on the right agree with one
                        visible lane in my direction, indexed 1. | roles: The yellow marking separates
                        opposing traffic; the unpainted curb forms the right road edge. The yellow marking's
                        solid or broken pattern remains uncertain. | markings: No readable guidance arrows,
                        words, symbols, transverse lines or waiting areas are visible in my lane. | unseen:
                        The left marking's continuity cannot be established; its pattern attribute must not be
                        treated as a confirmed solid line. The distant roadway is partly obscured by vehicles.
                        | result: Consistent, with the left boundary pattern unresolved.
Step 5  Rule            left_boundary: In China, a solid yellow center line prohibits crossing, whereas a
                        broken yellow center line permits crossing when safe, so the unresolved pattern
                        prevents a crossing decision.
Step 5  Rule            right_boundary: The raised roadside curb is not a traversable lane boundary and
                        prohibits moving right across it onto the sidewalk.
Step 6  change_left     not_determined (WRONG, label allowed): The yellow center line governs crossing left,
                        but its worn solid-or-broken pattern is unresolved.
Step 6  change_right    prohibited (correct): The raised roadside curb prohibits crossing right onto the
                        sidewalk.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: left crossing remains undecided because the governing pattern is unclear,
                        right crossing is prohibited by the curb, and no unmarked movement is treated as
                        positively permitted.
Advice                  Remain to the right of the yellow center marking and do not cross it unless its
                        pattern and the safety of doing so become clear. Leave clearance from parked cars and
                        pedestrians; no visible lane-use arrows establish turn permissions ahead.
Score                   lane False, boundaries {'left': False, 'right': False}, markings True (added [],
                        missed []), actions False, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1132, 23.84 s

culane_test__d193_06060925_0822_01260 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, suggested by the Chinese
                        writing, blue registration plates and traffic arrangement. My car is in the rightmost
                        of three same-direction lanes on a divided urban road beside an elevated structure; no
                        intersection or lane ending is visible ahead. (lanes 3, mine 3, full)
Step 2  Left            A white broken line, with visible long dashes and intervening gaps, separates my lane
                        from another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white solid line runs beside a raised curb and metal roadside fence on
                        the right, with no adjacent motor-vehicle lane beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Three same-direction lanes and ego lane index 3 agree with a lane divider on
                        the left and the roadway edge on the right. | roles: The broken white divider fits a
                        same-direction lane line; the solid white line beside the curb fits a roadway edge. |
                        markings: No guidance arrows, words, symbols, waiting areas or transverse markings are
                        discernible in my lane. | unseen: No movement restriction or intersection layout is
                        inferred beyond the visible road; distant pavement details are too small to read. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe and without interfering with other traffic.
Step 5  Rule            right_boundary: The solid roadway edge and raised curb do not permit an ordinary lane
                        change onto the roadside.
Step 6  change_left     allowed (correct): The broken white lane divider permits a left lane change when safe.
Step 6  change_right    prohibited (correct): The roadway edge and raised curb prohibit leaving the lane to
                        the right as an ordinary lane change.
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
Advice                  Remain within the right edge; a left lane change is permitted only after checking
                        traffic and blind spots. No visible marking establishes turn permissions or a stopping
                        point, so check the markings and controls nearer the next intersection.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 878, 14.02 s

culane_test__d193_06060925_0822_02700 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, suggested by the
                        Chinese writing, road design and vehicle arrangement. My car is in the third of four
                        same-direction lanes on a divided urban boulevard; the road continues ahead with no
                        clearly visible intersection or lane ending. (lanes 4, mine 3, full)
Step 2  Left            A white broken line, with a visible long dash and gap, separates my lane from another
                        same-direction lane on the left; there is no curb at this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white broken line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the right; the solid roadway edge and raised curb are farther
                        right, beyond that lane.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Four same-direction lanes and position three agree with having an adjacent
                        lane on each side. | roles: Both white broken boundaries fit same-direction lane-
                        divider roles. | markings: No readable arrows, words, symbols, transverse lines or
                        waiting areas appear in my visible lane. | unseen: The distant continuation is too
                        small to resolve markings at any eventual intersection; no such markings have been
                        inferred. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white lane divider permits crossing to
                        change lanes when safe without obstructing other traffic.
Step 5  Rule            right_boundary: In mainland China, a broken white lane divider permits crossing to
                        change lanes when safe without obstructing other traffic.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    allowed (correct): The broken white lane divider permits a safe lane change right.
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
                        blind spots. No visible marking assigns this lane a turning movement; check the lane
                        arrows, signs and signals when approaching the next intersection.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 913, 14.8 s

culane_test__d193_06060925_0822_04140 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese road signs and
                        the traffic arrangement. My car is in the rightmost of three lanes on a divided urban
                        road, approaching an overpass; no intersection or lane end is clearly visible. (lanes
                        3, mine 3, full)
Step 2  Left            A broken white line, with a visible long dash and gaps farther ahead, separates my
                        lane from another same-direction lane; there is no curb on this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A solid white line follows the right side of my lane, with a narrow paved margin and a
                        raised roadside curb and barrier beyond it.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white arrow in my lane has one head pointing straight ahead
                        and no visible turn branches.
Step 4  Cross-check     position: The left lane divider and right roadway edge agree with my car occupying
                        lane 3 of 3. | roles: The broken white line fits a same-direction lane divider, and
                        the solid white line beside the roadside margin fits a roadway edge. | markings: The
                        straight-only arrow is consistent with the through lane and its boundaries; the arrow
                        farther left belongs to another lane. | unseen: No intersection, stop line, waiting
                        area, or additional guidance marking can be identified in my lane; none has been
                        inferred beyond the visible stretch. | result: consistent
Step 5  Rule            left_boundary: Under Chinese marking rules, a broken white lane divider permits
                        crossing to change lanes when safe.
Step 5  Rule            right_boundary: The solid white roadway edge restricts crossing out of the traffic
                        lane during ordinary driving.
Step 5  Rule            arrow:straight: The straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The solid white roadway edge restricts crossing to the right.
Step 6  go_straight     allowed (correct): The straight arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible left-turn waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         consistent
Advice                  Continue straight in this lane and do not cross the solid right edge. For another
                        movement, select an appropriately marked lane where permitted; a safe left lane change
                        is possible across the broken divider, but no stopping position is visible here.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 979, 17.08 s

culane_test__d193_06060925_0822_04320 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        writing, vehicle plates and road layout. My car is on a divided urban road approaching
                        a pedestrian overbridge and a roadside bus stop; it appears to occupy the third of
                        four same-direction lanes, although traffic partly obscures the leftmost lanes. (lanes
                        4, mine 3, partial)
Step 2  Left            A broken white line, with visible long dashes and gaps, separates my lane from another
                        same-direction lane on the left; no curb forms this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A broken white line with broad dashes and intervening gaps separates my lane from the
                        lane beside the bus stop; the raised roadside curb is beyond that adjacent lane, not
                        at my lane boundary.
                        white dashed, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Same-direction lanes on both sides agree with my lane being an interior
                        lane, apparently third of four; the precise count is less certain because the left
                        side is partly obscured. | roles: Both white broken boundaries fit same-direction lane
                        separators. A bus and bus stop alone do not establish that the right-hand lane is
                        legally reserved. | markings: No guidance marking is readable within my lane. The
                        visible arrow to the left lies across my left boundary and does not govern my lane. |
                        unseen: No bus-lane restriction or unseen arrow is assumed. The next intersection and
                        the eventual end of my lane are not visible. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a broken white same-direction lane separator permits
                        crossing to change lanes when safe and without obstructing other traffic.
Step 5  Rule            right_boundary: A broken white same-direction lane separator permits crossing when
                        safe, subject to any separately established restriction on the adjacent lane.
Step 6  change_left     allowed (correct): The visible broken white lane separator permits a safe lane change
                        to the left.
Step 6  change_right    allowed (WRONG, label prohibited): The visible broken white lane separator permits a
                        safe lane change to the right; no reserved-lane marking is readable.
Step 6  go_straight     not_determined: The next intersection and any lane-use marking governing movement
                        there are outside the visible stretch.
Step 6  turn_left       not_determined: The next intersection and any lane-use marking governing a left turn
                        from my lane are not visible.
Step 6  turn_right      not_determined: The next intersection and any lane-use marking governing a right turn
                        from my lane are not visible.
Step 6  u_turn          not_determined: The next intersection and any marking governing a U-turn from my lane
                        are not visible.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: the broken boundaries permit conditional lane changes, unseen intersection
                        movements remain undetermined, and no visible waiting area governs entry.
Advice                  Either visible broken boundary may be crossed when safe; check for buses and any
                        posted restrictions before entering the right-hand lane. Continue watching for lane-
                        use arrows and intersection controls ahead, since this image does not establish which
                        lane to use for turning.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions False, unsafe ['change_right'], citation None, contradictions []
Tokens                  in 4533, out 1239, 28.43 s

culane_test__d193_06060925_0822_04680 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be an urban divided road in China, with traffic keeping right,
                        inferred from Chinese writing, blue license plates and the road layout. My car is in
                        the rightmost of three same-direction lanes, approaching a junction area whose distant
                        markings are not clearly visible. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right side of my lane, with a narrow paved
                        margin and a raised landscaped curb beyond it.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight_right (full): A worn white arrow in my lane has a forward-pointing head
                        and a branch pointing right.
Step 4  Cross-check     position: Three same-direction lanes and a rightmost ego position agree with a lane
                        divider on the left and a roadway edge on the right. | roles: The broken white divider
                        fits a same-direction lane line, and the continuous white line beside the paved margin
                        fits an edge line. | markings: The combined straight-and-right arrow is compatible
                        with the rightmost lane; no conflicting word, symbol or waiting area is visible. |
                        unseen: No distant stop line or intersection marking is asserted; vehicles and
                        distance limit inspection of the far end of the lane. | result: consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: A solid white roadway edge line does not permit an ordinary driving
                        maneuver out of the lane onto the roadside margin.
Step 5  Rule            arrow:straight_right: The combined straight-and-right lane-use arrow permits
                        proceeding straight or turning right, rather than turning left or making a U-turn from
                        this lane.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change left.
Step 6  change_right    prohibited (correct): The solid roadway edge line restricts crossing onto the roadside
                        margin.
Step 6  go_straight     allowed: The lane-use arrow includes a straight-ahead head.
Step 6  turn_left       prohibited: The straight-and-right arrow does not permit a left turn from this lane.
Step 6  turn_right      allowed: The lane-use arrow includes a right-turn head.
Step 6  u_turn          prohibited: The straight-and-right lane-use arrow does not permit a U-turn from this
                        lane.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight or turn right, subject to junction controls and
                        yielding requirements. For a left turn or U-turn, move left safely across the broken
                        divider into an appropriately marked lane; do not use the roadside margin.
Score                   lane False, boundaries {'left': True, 'right': True}, markings False (added
                        ['arrow:straight_right'], missed []), actions True, unsafe [], citation None,
                        contradictions []
Tokens                  in 4533, out 1130, 21.61 s

culane_test__d193_06060925_0822_05310 | lane | Test D | gpt-6.1-sol
-------------------------------------------------------------------
Step 1  Scene           This appears to be an urban divided road in China, with traffic keeping right; Chinese
                        writing and blue vehicle plates support that inference. My car is in the rightmost of
                        three through lanes, with a raised separator and a parallel roadway on the right; no
                        intersection or lane end is clearly visible ahead. (lanes 3, mine 3, full)
Step 2  Left            A faded white broken line, with visible dashes and gaps, separates my lane from
                        another same-direction lane on the left; there is no curb along this boundary.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A white continuous line runs along the right of my lane, with a narrow paved strip and
                        a raised curb beyond it separating this carriageway from the parallel roadway.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The left lane divider and right roadway edge agree with my car occupying
                        lane 3 of 3. | roles: The broken white line fits a same-direction lane divider, and
                        the continuous white line alongside the raised separator fits a roadway edge. |
                        markings: No arrows, words, symbols or transverse markings are readable within my
                        lane; the diagonal painted area farther ahead is outside its right boundary. | unseen:
                        No movement arrow or intersection layout has been inferred from the distant roadway. |
                        result: consistent
Step 5  Rule            left_boundary: In China, a broken white lane divider permits crossing to change lanes
                        when it is safe and does not obstruct other traffic.
Step 5  Rule            right_boundary: The continuous white roadway edge and raised separator do not permit
                        an ordinary lane change onto or across the roadside strip.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe lane change to the
                        left.
Step 6  change_right    prohibited (correct): The continuous roadway edge and raised separator prohibit an
                        ordinary move across the right boundary.
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
Advice                  Stay within the right edge line; change left across the broken divider only after
                        checking traffic. The visible markings do not establish permitted movements at the
                        next intersection, so look for subsequent lane arrows and signs before choosing a
                        turning lane.
Score                   lane False, boundaries {'left': True, 'right': False}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1021, 21.22 s

culane_test__d37_05181608_0235_03090 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, with traffic keeping right, based on the Chinese
                        writing, blue registration plates and traffic arrangement. My car is behind a taxi in
                        a channelized approach to an intersection, with other motor traffic to the left and a
                        railing to the right; the full approach lane count cannot be established. (lanes None,
                        mine None, insufficient)
Step 2  Left            A white solid line borders a diagonally painted channelizing area on the left; a
                        yellow crash barrel obscures its nearer continuation, and other motor traffic is
                        beyond it.
                        white solid, curb no, other, evidence partial
Step 2  Right           A white solid line runs beside a metal separating railing on the right, with a
                        separate paved area beyond the railing.
                        white solid, curb yes, edge_line, evidence full
Step 3  Markings        line:stop_line (partial): A transverse white line is visible ahead, with its portion
                        directly ahead of my car obscured by the taxi.; line:crosswalk (partial): Broad white
                        pedestrian-crossing stripes are visible farther ahead across the approach, partly
                        obscured by the taxi and other road users.
Step 4  Cross-check     position: The right railing establishes the right edge of this channelized lane, but
                        the channelizing area and incomplete view prevent a reliable count of all same-
                        direction lanes or an ordinal lane index. | roles: The solid white left boundary fits
                        a channelizing boundary rather than an ordinary broken lane divider; the right solid
                        white line and railing fit a roadway edge. | markings: The visible stop line and
                        crossing are compatible with an intersection approach; no lane-use arrow can be read
                        in the exposed pavement. | unseen: The taxi hides a substantial portion of the lane,
                        including pavement where directional markings could be present; no arrow or permitted
                        turn has been inferred. | result: consistent
Step 5  Rule            left_boundary: In mainland China, a solid channelizing boundary must not be crossed to
                        drive through the painted channelizing area.
Step 5  Rule            right_boundary: The physical separating railing prevents and prohibits leaving the
                        lane across this edge.
Step 5  Rule            line:stop_line: When required to stop, stop before the stop line rather than beyond
                        it.
Step 5  Rule            line:crosswalk: Approach the pedestrian crossing cautiously and yield to pedestrians
                        as required.
Step 6  change_left     prohibited (correct): The visible solid channelizing boundary prohibits crossing into
                        the painted separation area.
Step 6  change_right    prohibited (correct): The separating railing prohibits crossing the right boundary.
Step 6  go_straight     not_determined: The taxi hides pavement that could contain the lane-use marking
                        governing this movement.
Step 6  turn_left       not_determined: The taxi hides pavement that could contain the lane-use marking
                        governing this movement.
Step 6  turn_right      not_determined: The taxi hides pavement that could contain the lane-use marking
                        governing this movement.
Step 6  u_turn          not_determined: The taxi hides pavement that could contain a governing directional or
                        prohibited-movement marking.
Step 6  enter_waiting_areanot_applicable: No left-turn waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: both boundary-crossing actions are prohibited, hidden directional guidance
                        leaves intersection movements undecided, and no visible waiting area governs entry.
Advice                  Remain between the channelizing boundary and the railing; do not cross either to
                        change lanes. Let the taxi uncover the lane guidance before choosing an intersection
                        movement, obey the applicable signal, and stop before the stop line when required
                        while keeping the crossing clear.
Score                   lane False, boundaries {'left': True, 'right': False}, markings False (added
                        ['line:crosswalk', 'line:stop_line'], missed []), actions True, unsafe [], citation
                        None, contradictions []
Tokens                  in 4533, out 1210, 23.46 s

culane_test__d37_05181608_0235_03720 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese storefront
                        lettering, blue registration plates and vehicles on either side of the median fence.
                        My car is in the leftmost lane of a divided urban road; at least two same-direction
                        lanes are visible, but the total width and any intersection ahead are not clear.
                        (lanes None, mine 1, partial)
Step 2  Left            A continuous white line runs beside a raised median curb and metal fence, with
                        opposing traffic beyond.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           White broken paint separates my lane from the adjacent same-direction lane; a dash and
                        intervening unpainted stretch are visible ahead, while the nearest portion is hidden
                        by the hood.
                        white dashed, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median-side edge makes my lane the leftmost, and the broken line on the
                        right separates another same-direction lane; the total lane count remains uncertain. |
                        roles: The white solid median-edge line and white broken lane divider fit their
                        assigned roles. | markings: No readable arrows, words, symbols, waiting areas or
                        transverse lines are visible in my lane. | unseen: No hidden paint has been
                        reconstructed; the road farther ahead and the nearest right boundary are partly
                        obscured. | result: consistent
Step 5  Rule            left_boundary: The solid roadway edge and raised median do not permit leaving the lane
                        to the left.
Step 5  Rule            right_boundary: In China, a broken white lane divider permits changing into the
                        adjacent lane when it is safe.
Step 6  change_left     prohibited (correct): The solid median edge and raised curb prohibit crossing to the
                        left.
Step 6  change_right    allowed (correct): The visible broken white lane divider permits a safe lane change to
                        the right.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use or prohibited-movement marking governs this
                        action.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         Consistent: boundary rules govern only lateral changes, and the absence of visible
                        movement markings is not treated as permission for intersection movements.
Advice                  Stay clear of the median; a rightward lane change is permitted across the broken white
                        line only after checking the adjacent traffic. No visible arrows establish which lane
                        to use for turns, so check the markings and controls farther ahead.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1052, 22.76 s

culane_test__d37_05181608_0235_05220 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, inferred from the Chinese writing and blue
                        registration plates, with traffic keeping right. My car is in an interior lane of a
                        congested multilane urban road approaching an apparent signalized intersection;
                        vehicles obscure the outer lanes and the lane's end. (lanes None, mine None,
                        insufficient)
Step 2  Left            A single white line appears continuous and solid along the visible stretch to my left,
                        with another same-direction traffic lane beyond it and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along my right to the vehicles ahead, with another
                        same-direction traffic lane beyond it and no curb at this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: Same-direction lanes are visible on both sides, consistent with an interior
                        lane; the total lane count and exact index cannot be established because the outer
                        roadway is obscured. | roles: Both white solid boundaries fit lane separators on a
                        Chinese intersection approach. | markings: No guidance markings or transverse lines
                        can be read in the exposed portion of my lane; vehicles conceal much of the pavement
                        ahead. | unseen: No arrows, stop line, crosswalk, or waiting area have been inferred
                        from their expected locations. | result: consistent
Step 5  Rule            left_boundary: Under mainland Chinese marking rules, a solid white lane separator
                        prohibits crossing it to change lanes to the left.
Step 5  Rule            right_boundary: Under mainland Chinese marking rules, a solid white lane separator
                        prohibits crossing it to change lanes to the right.
Step 6  change_left     prohibited (correct): The visible solid white lane separator prohibits crossing the
                        left boundary.
Step 6  change_right    prohibited (correct): The visible solid white lane separator prohibits crossing the
                        right boundary.
Step 6  go_straight     not_determined: Vehicles hide the pavement ahead where a lane-use arrow could
                        determine this movement.
Step 6  turn_left       not_determined: Vehicles hide the pavement ahead where a lane-use arrow or prohibited-
                        turn marking could determine this movement.
Step 6  turn_right      not_determined: Vehicles hide the pavement ahead where a lane-use arrow or prohibited-
                        turn marking could determine this movement.
Step 6  u_turn          not_determined: Vehicles hide the pavement ahead where a lane-use arrow or prohibited-
                        U-turn marking could determine this movement.
Step 6  enter_waiting_areanot_determined: The intersection approach and pavement ahead are obscured, so the
                          presence of a qualifying waiting area cannot be established.
Step 7  Reflect         consistent
Advice                  Stay between the solid white boundaries and do not change lanes across them. Wait for
                        the queue to reveal your lane's arrows and stop line, then follow the applicable lane
                        directions and traffic signals without entering an unconfirmed waiting area.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 900, 14.69 s

culane_test__d37_05181608_0235_05340 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be China, with right-hand traffic, based on the Chinese writing, blue
                        registration plates and traffic arrangement. My car is queued on a multilane urban
                        road approaching an intersection; vehicles obscure the outer lanes and the end of my
                        lane. (lanes None, mine None, insufficient)
Step 2  Left            A white line runs continuously along the visible left side of my lane, with another
                        same-direction traffic lane beyond; no curb is visible.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A white line runs continuously along the visible right side of my lane, with same-
                        direction vehicles beyond; no curb is visible.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        none
Step 4  Cross-check     position: The lane lines and adjacent traffic establish that my lane has another same-
                        direction lane on each side, but the outer roadway limits are obscured, preventing an
                        exact lane count or index. | roles: White solid lines are consistent with same-
                        direction lane dividers on an intersection approach in China. | markings: No in-lane
                        guidance marking is readable on the exposed pavement; vehicles conceal much of the
                        approach and the lane end. | unseen: No arrows, stop line, crosswalk or waiting area
                        are inferred from the obscured pavement. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes to the left.
Step 5  Rule            right_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes to the right.
Step 6  change_left     prohibited (correct): The visible solid white lane divider prohibits crossing to the
                        left.
Step 6  change_right    prohibited (correct): The visible solid white lane divider prohibits crossing to the
                        right.
Step 6  go_straight     not_determined: Vehicles obscure the lane-use markings that could determine whether
                        straight travel is permitted.
Step 6  turn_left       not_determined: Vehicles obscure the lane-use markings that could determine whether a
                        left turn is permitted.
Step 6  turn_right      not_determined: Vehicles obscure the lane-use markings that could determine whether a
                        right turn is permitted.
Step 6  u_turn          not_determined: Vehicles obscure any lane-use or prohibited-movement marking governing
                        a U-turn.
Step 6  enter_waiting_areanot_determined: The intersection approach is obscured, so the presence and
                          accessibility of a marked waiting area cannot be established.
Step 7  Reflect         consistent
Advice                  Remain between the solid white lane dividers and leave a safe gap in the queue.
                        Confirm the lane arrows, signals and stopping position as they become visible; this
                        image does not establish which intersection movements your lane permits.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 948, 18.37 s

culane_test__d37_05181919_0299_02970 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese
                        storefronts, blue vehicle plates and traffic layout. My car is in the rightmost of
                        three same-direction motor-vehicle lanes on a divided urban road, approaching a
                        distant intersection. (lanes 3, mine 3, full)
Step 2  Left            A broken white line, with visible dashes and gaps, separates my lane from another
                        same-direction lane on the left.
                        white dashed, curb no, lane_line, evidence full
Step 2  Right           A continuous white line runs along the right of my lane, with a roadside strip
                        containing a car and two-wheelers beyond it; no curb directly bounds my lane.
                        white solid, curb no, edge_line, evidence full
Step 3  Markings        arrow:straight (full): A white straight-ahead arrow is painted immediately ahead of
                        the hood, with its forward-pointing head visible behind the car ahead.
Step 4  Cross-check     position: Three motor-vehicle lanes and ego position 3 agree with a lane divider on
                        the left and a roadway-edge boundary on the right. | roles: The broken white line fits
                        a same-direction lane divider; the solid white line fits the boundary to the roadside
                        strip. | markings: The straight-ahead arrow is compatible with both boundaries; arrows
                        in adjacent lanes do not govern my lane. | unseen: No unseen stop line or waiting area
                        is inferred; the car ahead and distance obscure some pavement farther ahead. | result:
                        consistent
Step 5  Rule            left_boundary: In China, a broken white same-direction lane divider permits crossing
                        to change lanes when safe.
Step 5  Rule            right_boundary: The solid white roadway-edge boundary restricts crossing into the
                        roadside strip during ordinary driving.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow requires proceeding straight rather
                        than turning left, turning right or making a U-turn from this lane.
Step 6  change_left     allowed (correct): The broken white lane divider permits a safe left lane change.
Step 6  change_right    prohibited (correct): The solid white edge boundary restricts crossing into the
                        roadside strip.
Step 6  go_straight     allowed (correct): The straight-ahead arrow permits proceeding straight.
Step 6  turn_left       prohibited (correct): The straight-only arrow excludes a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrow excludes a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrow excludes a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Use this lane to continue straight, leaving room for the car ahead. For another
                        movement, select an appropriately marked lane where permitted; do not cross the solid
                        right boundary into the roadside strip.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1067, 20.18 s

culane_test__d37_05181919_0299_03120 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be an urban road in China, likely Beijing, based on the Chinese
                        lettering and taxi livery; traffic keeps right. My car is in the middle of three same-
                        direction lanes approaching a signalized intersection. (lanes 3, mine 2, full)
Step 2  Left            A single solid white line runs along my lane's left side, with another traffic lane
                        and a taxi beyond it; no curb forms this boundary.
                        white solid, curb no, lane_line, evidence full
Step 2  Right           A single solid white line runs along my lane's right side, with another traffic lane
                        and cars beyond it; the roadside railing is farther right, not on this boundary.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A large white forward-pointing arrowhead is visible
                        immediately ahead of the hood; its lower shaft is hidden by the hood.; arrow:straight
                        (partial): A smaller white straight-ahead arrow is visible farther ahead in my lane,
                        though its detail is reduced by distance.
Step 4  Cross-check     position: Two lane-line boundaries place my lane between another same-direction lane
                        on each side, consistent with lane 2 of 3. | roles: The white longitudinal lines
                        separate same-direction traffic, and their visible continuous stretches support solid
                        lane-line classifications. | markings: The visible forward arrowheads agree with each
                        other and indicate a straight-through lane; no conflicting marking is visible. |
                        unseen: The near arrow's shaft is hidden by the hood, and the intersection approach is
                        partly obscured by vehicles and distance; no stop line, crosswalk, or waiting area is
                        asserted. | result: consistent
Step 5  Rule            left_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            right_boundary: In China, a solid white lane-dividing line prohibits crossing it to
                        change lanes.
Step 5  Rule            arrow:straight: A straight-only lane-use arrow permits proceeding straight and
                        excludes left turns, right turns, and U-turns from this lane.
Step 5  Rule            arrow:straight: The repeated straight-ahead arrow reinforces that this lane is for
                        straight-through movement only.
Step 6  change_left     prohibited (correct): The solid white left lane line prohibits crossing into the
                        adjacent lane.
Step 6  change_right    prohibited (correct): The solid white right lane line prohibits crossing into the
                        adjacent lane.
Step 6  go_straight     allowed (correct): The visible straight-ahead arrowheads permit straight-through
                        movement.
Step 6  turn_left       prohibited (correct): The straight-only arrows exclude a left turn from this lane.
Step 6  turn_right      prohibited (correct): The straight-only arrows exclude a right turn from this lane.
Step 6  u_turn          prohibited (correct): The straight-only arrows exclude a U-turn from this lane.
Step 6  enter_waiting_areanot_applicable: No visible marked waiting area or adjacent two-way left-turn lane
                          governs this action.
Step 7  Reflect         Consistent: the visible arrowheads establish straight-only guidance despite their
                        partially hidden shafts, and neither solid boundary permits a lane change.
Advice                  Stay in this lane for straight travel and do not cross either solid white boundary.
                        Obey the signal before entering the intersection; for a turn, use an appropriately
                        marked lane reached only where lane changing is permitted.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1114, 17.32 s

culane_test__d37_05190927_0395_02340 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be mainland China, based on the Chinese writing and vehicle plates,
                        with traffic keeping right. My car is in the leftmost of three apparent same-direction
                        lanes on a divided urban road approaching an intersection; vehicles obscure much of
                        the approach. (lanes 3, mine 1, partial)
Step 2  Left            A solid white line runs beside a raised planted median with fencing; opposing traffic
                        is beyond the median.
                        white solid, curb yes, edge_line, evidence full
Step 2  Right           A white line appears continuous along the visible approach, separating my lane from
                        the adjacent same-direction lane; vehicles obscure its continuation ahead.
                        white solid, curb no, lane_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: The median edge on the left agrees with my lane being leftmost; the lane
                        line on the right separates an adjacent same-direction lane. Three lanes appear
                        present, although nearby vehicles obscure parts of their boundaries. | roles: The
                        white median-side edge line and white same-direction lane separator fit their assigned
                        roles. | markings: No guidance marking is readable in my lane, so none contradicts the
                        boundaries. | unseen: The truck hides much of my lane ahead, including any lane-use
                        arrow or transverse marking; no hidden marking has been assumed. | result: consistent
Step 5  Rule            left_boundary: The raised median forms a physical roadway edge that my car must not
                        cross.
Step 5  Rule            right_boundary: Under mainland Chinese marking rules, a solid white lane separator
                        prohibits crossing it to change lanes along the visible solid stretch.
Step 6  change_left     prohibited (correct): The raised median prohibits leaving the lane across the left
                        boundary.
Step 6  change_right    prohibited (correct): The visible solid white lane separator prohibits crossing to the
                        right.
Step 6  go_straight     not_determined: The truck obscures the approach where a lane-use arrow could determine
                        this movement.
Step 6  turn_left       not_determined: The truck obscures the approach where a lane-use arrow could determine
                        this movement.
Step 6  turn_right      not_determined: The truck obscures the approach where a lane-use arrow could determine
                        this movement.
Step 6  u_turn          not_determined: Any lane-use or prohibited-movement marking ahead is obscured by the
                        truck.
Step 6  enter_waiting_areanot_applicable: No visible waiting area or adjacent two-way left-turn lane governs
                          this action.
Step 7  Reflect         consistent
Advice                  Stay between the median and the solid white separator, and leave space behind the
                        truck. Confirm the lane-use arrows, stop line and intersection controls as they become
                        visible before choosing a movement.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 948, 17.04 s

culane_test__d37_05190927_0395_02430 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be China, with traffic keeping right, based on the Chinese writing,
                        vehicle plates and traffic arrangement. My car is in the leftmost of three apparent
                        same-direction lanes approaching an urban intersection and pedestrian crossing, beside
                        a raised median island. (lanes 3, mine 1, partial)
Step 2  Left            A raised concrete island forms the left side of my lane, with a pole on it; its edge
                        curves toward the crossing, and no continuous painted boundary can be clearly
                        distinguished alongside it.
                        none none, curb yes, edge_line, evidence partial
Step 2  Right           A white solid line runs from beside the hood toward the crossing, separating my lane
                        from another same-direction traffic lane; no curb is present on this side.
                        white solid, curb no, lane_line, evidence full
Step 3  Markings        arrow:straight (partial): A white forward-pointing arrowhead is visible immediately
                        ahead of the hood, but the lower shaft and any possible branches are obscured by the
                        hood.; line:stop_line (full): A transverse white stop line crosses my lane immediately
                        before the pedestrian crossing.; line:crosswalk (partial): Broad white zebra-crossing
                        stripes extend across my lane ahead, partly occupied by vehicles and pedestrians.
Step 4  Cross-check     position: The island on the left is consistent with my lane being leftmost; the white
                        lane divider on the right confirms at least one adjacent same-direction lane. Three
                        lanes appear present, but vehicles and perspective make the total less certain. |
                        roles: The raised island is a physical roadway edge, and the white solid line
                        separates same-direction lanes. | markings: The visible straight arrowhead is
                        compatible with the approach lane, stop line and crossing; its obscured lower portion
                        prevents excluding additional turn branches. | unseen: No hidden arrow branches or
                        painted line beside the island are assumed; the lane count and obscured markings have
                        reduced evidence. | result: consistent
Step 5  Rule            left_boundary: The raised island is a physical boundary that my car must not cross.
Step 5  Rule            right_boundary: In China, a solid white lane divider prohibits crossing it to change
                        lanes along the marked stretch.
Step 5  Rule            arrow:straight: The visible forward arrowhead permits proceeding straight, but its
                        hidden lower portion prevents determining whether additional movements are indicated.
Step 5  Rule            line:stop_line: When required to stop, my car must stop before the stop line.
Step 5  Rule            line:crosswalk: My car must yield to pedestrians using the crossing and must not
                        obstruct it.
Step 6  change_left     prohibited (correct): The raised island prohibits crossing the left boundary.
Step 6  change_right    prohibited (correct): The solid white lane divider prohibits crossing the right
                        boundary.
Step 6  go_straight     allowed (correct): The visible straight arrowhead permits proceeding straight.
Step 6  turn_left       not_determined (correct): The hood hides the lower arrow and any possible left-turn
                        branch.
Step 6  turn_right      not_determined (correct): The hood hides the lower arrow and any possible right-turn
                        branch.
Step 6  u_turn          not_determined (correct): The hood hides the lower arrow, preventing confirmation or
                        exclusion of a U-turn indication.
Step 6  enter_waiting_areanot_applicable: No marked left-turn waiting area or adjacent two-way left-turn lane
                          is visible.
Step 7  Reflect         consistent
Advice                  Remain in this lane for the visibly indicated straight movement; do not cross the
                        island or solid white divider. Confirm the complete arrow before attempting a turn,
                        obey the signals, and stop before the stop line when required while yielding to
                        pedestrians.
Score                   lane False, boundaries {'left': False, 'right': True}, markings None (added None,
                        missed None), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1352, 26.24 s

culane_test__d37_05190927_0395_05220 | lane | Test D | gpt-6.1-sol
------------------------------------------------------------------
Step 1  Scene           This appears to be an urban street in China, with traffic keeping right, inferred from
                        the blue vehicle plates, vehicle positions and road layout. My car is in the single
                        visible through lane in this direction, with opposing traffic on the left and vehicles
                        beside the roadway on the right; no intersection or lane end is clearly visible ahead.
                        (lanes 1, mine 1, full)
Step 2  Left            A yellow line appears solid along the visible stretch, with opposing vehicles beyond
                        it; the nearby cyclist obscures its foreground continuation, and no curb forms this
                        boundary.
                        yellow solid, curb no, center_line, evidence partial
Step 2  Right           Two closely spaced white lines appear continuous along the visible stretch, separating
                        my lane from the roadside strip occupied by vehicles; the nearby SUV obscures part of
                        this side, and no curb directly bounds my lane.
                        white double_solid, curb no, edge_line, evidence partial
Step 3  Markings        none
Step 4  Cross-check     position: One through lane in my direction agrees with a center line on the left and a
                        roadside edge boundary on the right. | roles: The yellow line separates opposing
                        traffic; the white lines separate the through lane from the roadside strip rather than
                        a clearly established second through lane. | markings: No readable arrows, words,
                        symbols, waiting areas or transverse markings are visible in my lane. | unseen: The
                        cyclist and SUV obscure nearby portions of the boundaries, and distant pavement detail
                        is not readable; no unseen guidance marking has been inferred. | result: consistent
Step 5  Rule            left_boundary: Under the inferred Chinese rules, a solid yellow center line prohibits
                        crossing into the opposing side for overtaking or a lateral move.
Step 5  Rule            right_boundary: Under the inferred Chinese rules, the continuous white roadway
                        boundary must not be crossed into the roadside strip in ordinary driving.
Step 6  change_left     prohibited (correct): The visible solid yellow center line prohibits crossing to the
                        left.
Step 6  change_right    prohibited (correct): The visible continuous white roadside boundary prohibits
                        crossing to the right in ordinary driving.
Step 6  go_straight     not_applicable: No visible lane-use marking governs this action.
Step 6  turn_left       not_applicable: No visible lane-use marking governs this action.
Step 6  turn_right      not_applicable: No visible lane-use marking governs this action.
Step 6  u_turn          not_applicable: No visible lane-use or prohibited-movement marking governs this action
                        at a lane end.
Step 6  enter_waiting_areanot_applicable: No marked waiting area or adjacent two-way left-turn lane is
                          visible.
Step 7  Reflect         Consistent: boundary restrictions govern only lateral crossing, and the absence of
                        visible movement markings does not establish permission for any movement at an unseen
                        intersection.
Advice                  Stay between the visible boundaries and slow down for the cyclist immediately ahead
                        and the SUV close on the right. No turn guidance or stop line is readable here;
                        reassess the markings when the road ahead becomes clear.
Score                   lane True, boundaries {'left': True, 'right': True}, markings True (added [], missed
                        []), actions True, unsafe [], citation None, contradictions []
Tokens                  in 4533, out 1036, 20.3 s
```
